import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / "systems" / "research" / "skills" / "research-map" / "scripts" / "validate.py"
spec = importlib.util.spec_from_file_location("rm_validate", SCRIPT)
rm = importlib.util.module_from_spec(spec)
sys.modules["rm_validate"] = rm  # dataclasses resolve annotations through sys.modules
spec.loader.exec_module(rm)


MAP = """# RESEARCH.map — fixture

## Layout
- protocol: protocol.md
- decisions: decisions.md
- aggregates: aggregates/
- documents: paper/, protocol.md
- notebooks: notebooks/
- references: references.bib

## Question
Does X change Y? → `protocol.md#question`

## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | Y < 0 | interval includes 0 | INCONCLUSIVE | `protocol.md#h1` |

## Gates
| Phase | State | Blocked by |
|---|---|---|
| 1 Problem | reached | |
| 8 Publication | blocked | ethics — PI |

## Facts that were once wrong
| Was | Is | Produced by |
|---|---|---|
| 4,618 kitchens | 5,913 | `notebooks/clean.ipynb` |

## Provenance
| Input | Location | Read by |
|---|---|---|
| registry | `aggregates/results.csv` | `notebooks/clean.ipynb` |

## Verification
```bash
make paper
```

## Open decisions
- D-?: pool definition — unblocked by: PI

## Last session
- 2026-09-09: reconciled registry.
- Next: fit models in DRY_RUN.
"""

DECISIONS_OK = """# Decisions

### D-1 · 2026-09-01
Decision: cluster bootstrap.
Rationale: spatial clustering.
Revision condition: Moran's I within null band.

### D-2 · 2026-09-02
Decision: radius 873 m.
Rationale: median geocoding drift.
Revise when: drift distribution changes.
"""

DECISIONS_BAD = DECISIONS_OK + """
### D-2 · 2026-09-03
Decision: duplicate id, no revision.
Rationale: none.
"""

PAPER = """# Results

We found 5,913 kitchens and a correlation of ρ = 0.61 (95% CI 0.55–0.67).
The share was 12.5% in 2026.
Page 42 <!-- rm:ignore -->
See doi:10.1000/xyz123 for 4,618 earlier kitchens.

```text
9999 inside a fence is ignored
```
"""

NOTEBOOK_CLEAN = {"cells": [{"cell_type": "code", "source": "x = 1", "outputs": [], "execution_count": None}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
NOTEBOOK_DIRTY = {"cells": [{"cell_type": "code", "source": "x", "outputs": [{"output_type": "stream", "text": "1"}], "execution_count": 3}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}

BIB = """@article{ok, title={T}, doi={10.1073/pnas.1708274114}}
@article{nodoi, title={T2}}
"""


def build(root: Path, decisions: str = DECISIONS_OK, extra_paper: str = "") -> None:
    (root / "aggregates").mkdir()
    (root / "paper").mkdir()
    (root / "notebooks").mkdir()
    (root / "RESEARCH.map").write_text(MAP, encoding="utf-8")
    (root / "protocol.md").write_text("# Protocol\n\n## question\n\n## h1\n", encoding="utf-8")
    (root / "decisions.md").write_text(decisions, encoding="utf-8")
    (root / "aggregates" / "results.csv").write_text("metric,value\nkitchens,5913\nrho,0.6083\nlow,0.5512\nhigh,0.6701\nshare,0.125\n", encoding="utf-8")
    (root / "paper" / "results.md").write_text(PAPER + extra_paper, encoding="utf-8")
    (root / "notebooks" / "clean.ipynb").write_text(json.dumps(NOTEBOOK_CLEAN), encoding="utf-8")
    (root / "references.bib").write_text(BIB, encoding="utf-8")


class ValidateTests(unittest.TestCase):
    def run_all(self, root: Path):
        results = rm.run(root / "RESEARCH.map", root, offline=True, min_int=20, only=None)
        return {r.name: r for r in results}

    def test_clean_repository_passes_except_offline_citations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root)
            results = self.run_all(root)
            self.assertEqual(results["map"].status, "PASS", results["map"].lines)
            self.assertEqual(results["numbers"].status, "PASS", results["numbers"].lines)
            self.assertEqual(results["decisions"].status, "PASS", results["decisions"].lines)
            self.assertEqual(results["notebooks"].status, "PASS", results["notebooks"].lines)
            # references.bib has an entry with neither doi nor url: that is a FAIL even offline
            self.assertEqual(results["citations"].status, "FAIL")
            self.assertTrue(any("nodoi" in l for l in results["citations"].lines))

    def test_numbers_rounding_percent_and_ignores(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root, extra_paper="\nUnsupported: 7,777 units and 0.99 precision.\n")
            numbers = self.run_all(root)["numbers"]
            self.assertEqual(numbers.status, "FAIL")
            flagged = " ".join(numbers.lines)
            self.assertIn("7,777", flagged)
            self.assertIn("0.99", flagged)
            self.assertNotIn("5,913", flagged)      # exact
            self.assertNotIn("0.61", flagged)       # 0.6083 rounds to 0.61
            self.assertNotIn("12.5", flagged)       # 0.125 as percent
            self.assertNotIn("2026", flagged)       # year
            self.assertNotIn("42", flagged)         # rm:ignore
            self.assertNotIn("4,618", flagged)      # line carries doi → skipped
            self.assertNotIn("9999", flagged)       # fenced

    def test_decisions_require_revision_condition_and_unique_increasing_ids(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root, decisions=DECISIONS_BAD)
            decisions = self.run_all(root)["decisions"]
            self.assertEqual(decisions.status, "FAIL")
            joined = " ".join(decisions.lines)
            self.assertIn("appears twice", joined)
            self.assertIn("no `Revision condition:`", joined)

    def test_notebook_outputs_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root)
            (root / "notebooks" / "dirty.ipynb").write_text(json.dumps(NOTEBOOK_DIRTY), encoding="utf-8")
            notebooks = self.run_all(root)["notebooks"]
            self.assertEqual(notebooks.status, "FAIL")
            self.assertTrue(any("dirty.ipynb" in l for l in notebooks.lines))

    def test_map_structure_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root)
            broken = MAP.replace("| 1 Problem | reached | |", "| 1 Problem | done | |") \
                        .replace("`notebooks/clean.ipynb` |\n\n## Provenance", "`notebooks/missing.ipynb` |\n\n## Provenance") \
                        .replace("## Open decisions\n", "")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            result = self.run_all(root)["map"]
            self.assertEqual(result.status, "FAIL")
            joined = " ".join(result.lines)
            self.assertIn("state 'done'", joined)
            self.assertIn("missing.ipynb", joined)
            self.assertIn("Open decisions", joined)

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(root)
            (root / "references.bib").write_text("@article{ok, doi={10.1/x}}\n", encoding="utf-8")
            self.assertEqual(rm.main([str(root / "RESEARCH.map"), "--offline"]), 0)
            self.assertEqual(rm.main([str(root / "RESEARCH.map"), "--offline", "--strict"]), 1)

    def test_interpretations(self):
        self.assertEqual(rm.interpretations("5,913"), [(5913.0, 0), (5.913, 3)])
        self.assertEqual(rm.interpretations("5.913"), [(5913.0, 0), (5.913, 3)])
        self.assertEqual(rm.interpretations("0.125"), [(0.125, 3)])      # leading zero: never thousands
        self.assertEqual(rm.interpretations("1.234.567"), [(1234567.0, 0)])
        self.assertEqual(rm.interpretations("1.234,56"), [(1234.56, 2)])
        self.assertEqual(rm.interpretations("1,234.56"), [(1234.56, 2)])
        self.assertEqual(rm.interpretations("0,61"), [(0.61, 2)])
        self.assertEqual(rm.interpretations("873"), [(873.0, 0)])


if __name__ == "__main__":
    unittest.main()
