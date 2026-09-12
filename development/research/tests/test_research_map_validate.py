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
sys.modules["rm_validate"] = rm
spec.loader.exec_module(rm)

GATES = "\n".join(
    f"| {i} {name} | pending | | |"
    for i, name in enumerate(["Problem", "Literature", "Protocol", "Data", "Analysis", "Writing", "Review", "Publication"], 1)
)

MAP = f"""# RESEARCH.map — fixture

## Layout
- protocol: protocol.md
- decisions: decisions.md
- aggregates: aggregates/
- documents: paper/
- notebooks: notebooks/
- references: references.bib
- floor: 5

## Question
Does X change Y? → `protocol.md#question`
Problem: SHOWN → `problem-brief.md`
Registration: none

## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | Y < 0 | interval includes `0.05` | INCONCLUSIVE | `protocol.md#h1` |

## Gates
| Phase | State | Blocked by | Evidence |
|---|---|---|---|
{GATES.replace("| 1 Problem | pending | | |", "| 1 Problem | reached | | `decisions.md#d-1` |").replace("| 8 Publication | pending | | |", "| 8 Publication | blocked | ethics — PI | |")}

## Facts that were once wrong
| Was | Is | Produced by |
|---|---|---|
| 4,618 units | 5,913 | `notebooks/clean.ipynb` |

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

## Deferred
- 2026-09-09: alternative model — enters when: H1 reaches a terminal state

## Last session
- 2026-09-09: reconciled registry.
- Next: fit models in DRY_RUN.
"""

PROTOCOL = """# Protocol

## Question
Does X change Y?

- **Claim:** associational
- **Unit of analysis:** municipality
- **Estimand:** population all municipalities 2026; contrast X vs not X; outcome Y at t+1; intercurrent events none; summary difference
- **Refutation:** interval includes 0 under the primary test
- **Objection:** selection — answered in phase 3
- **Who cares:** programme office
- **Non-goals:** mechanisms

## h1
H1 text.
"""

DECISIONS = """# Decisions

### D-1 · 2026-09-01
Decision: cluster bootstrap.
Rationale: spatial clustering.
Revision condition: dependence no longer material.
"""

BRIEF = """# Problem brief — fixture

- **Construct:** units per 100k inhabitants; validated by: registry audit
- **Population:** all municipalities, 2026
- **Measure:** count of registered units
- **Reference:** the 3,000 units the programme planned; fixed in D-1 before the magnitude notebook existed
- **Magnitude:** 5,913 units, from `aggregates/results.csv`
- Distribution: concentrated in capitals
- **Falsification:** recount after de-duplication still 5,913
- **Verdict:** SHOWN — excess against the plan holds after falsification
"""

PAPER = """# Results

We found 5,913 units. The coefficient was -0.31 (SE 0.09; p < 0.001).
"""

NOTEBOOK = {"cells": [{"cell_type": "code", "source": "x = 1", "outputs": [], "execution_count": None}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
BIB = "@article{ok, title={T}, doi={10.1073/pnas.1708274114}}"


def build(root: Path) -> None:
    (root / "aggregates").mkdir()
    (root / "paper").mkdir()
    (root / "notebooks").mkdir()
    (root / "RESEARCH.map").write_text(MAP, encoding="utf-8")
    (root / "protocol.md").write_text(PROTOCOL, encoding="utf-8")
    (root / "decisions.md").write_text(DECISIONS, encoding="utf-8")
    (root / "problem-brief.md").write_text(BRIEF, encoding="utf-8")
    (root / "aggregates" / "results.csv").write_text(
        "metric,value\nunits,5913\nbeta,-0.31\nse,0.09\nplanned,3000\n",
        encoding="utf-8",
    )
    (root / "paper" / "results.md").write_text(PAPER, encoding="utf-8")
    (root / "notebooks" / "clean.ipynb").write_text(json.dumps(NOTEBOOK), encoding="utf-8")
    (root / "references.bib").write_text(BIB, encoding="utf-8")


def results(root: Path):
    return {r.name: r for r in rm.run(root / "RESEARCH.map", root, offline=True, min_int=20, only=None)}


class ResearchMapValidatorTests(unittest.TestCase):
    def test_valid_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            self.assertTrue(all(r.status != "FAIL" for r in results(root).values()))

    def test_invalid_map_structure_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            broken = MAP.replace("| 1 Problem | reached | | `decisions.md#d-1` |", "| 1 Problem | done | | |")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            self.assertEqual(results(root)["map"].status, "FAIL")

    def test_reached_gate_needs_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            broken = MAP.replace("| 1 Problem | reached | | `decisions.md#d-1` |", "| 1 Problem | reached | | |")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            self.assertEqual(results(root)["map"].status, "FAIL")

    def test_unbacked_number_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "problem-brief.md").write_text(BRIEF.replace("5,913 units", "7,777 units"), encoding="utf-8")
            self.assertEqual(results(root)["numbers"].status, "FAIL")


if __name__ == "__main__":
    unittest.main()
