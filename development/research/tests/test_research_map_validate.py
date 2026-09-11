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

GATES = "\n".join(f"| {i} {name} | pending | | |" for i, name in enumerate(
    ["Problem", "Literature", "Protocol", "Data", "Analysis", "Writing", "Review", "Publication"], 1))

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

## Deferred
- 2026-09-09: spatial lag model as an alternative specification — enters when: H1 reaches a terminal state and the cluster bootstrap is reported

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
- **Who cares:** the state programme office
- **Non-goals:** mechanisms

## h1
H1 text.
"""

DECISIONS_OK = """# Decisions

### D-1 · 2026-09-01
Decision: cluster bootstrap.
Rationale: spatial clustering.
Revision condition: Moran's I within null band.

### D-2 · 2026-09-02
Decision: radius 873 m.
Rationale: median geocoding drift.
D-1 is unaffected by this decision.
Revise when: drift distribution changes.
"""

DECISIONS_BAD = DECISIONS_OK + """
### D-2 · 2026-09-03
Decision: duplicate id, no revision.
Rationale: none.
"""

PAPER = """# Results

We found 5,913 kitchens and a correlation of ρ = 0.61 (95% CI 0.55–0.67).
The coefficient was -0.31 (SE 0.09; p < 0.001), see Section 5.1 and Table 23.
The share was 12.5% in 2026; see https://example.org/x for 5,913 units.
Page 42 <!-- rm:ignore: page reference, not a result -->
Under Lei 14.628/2023 and Portaria GM nº 1.111 the registry is public.
See doi:10.1000/xyz123 for 4,618 earlier kitchens.

```text
9999 inside a fence is ignored
```

~~~
8888 inside a tilde fence is ignored
~~~
"""

NOTEBOOK_CLEAN = {"cells": [{"cell_type": "code", "source": "x = 1", "outputs": [], "execution_count": None}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}
NOTEBOOK_DIRTY = {"cells": [{"cell_type": "code", "source": "x", "outputs": [{"output_type": "stream", "text": "1"}], "execution_count": 3}], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}

BIB = """@comment{This is a comment with no doi}
@string{jpub = "Journal of Public Health"}
@article{ok, title={T}, doi={10.1073/pnas.1708274114}}
@book{kkv, title={Designing Social Inquiry}, isbn={9780691034713}}
@article{nodoi, title={T2}}
"""


PROTOCOL_TEXT = PROTOCOL

BRIEF = """# Problem brief — fixture

- **Construct:** kitchens per 100k inhabitants; validated by: registry audit against field visits (ρ = 0.61)
- **Population:** all municipalities, 2026
- **Measure:** count of registered kitchens
- **Reference:** the 3,000 kitchens the programme planned; fixed in D-1,
  before the magnitude notebook existed
- **Magnitude:** 5,913 kitchens, from `aggregates/results.csv`
- Distribution: concentrated in state capitals
- **Falsification:** recount after de-duplication still 5,913; trend flat
- **Verdict:** SHOWN — excess against the plan holds after falsification
"""


def build(root: Path, decisions: str = DECISIONS_OK, extra_paper: str = "", bib: str = BIB) -> None:
    (root / "aggregates").mkdir()
    (root / "paper").mkdir()
    (root / "notebooks").mkdir()
    (root / "RESEARCH.map").write_text(MAP, encoding="utf-8")
    (root / "protocol.md").write_text(PROTOCOL, encoding="utf-8")
    (root / "decisions.md").write_text(decisions, encoding="utf-8")
    (root / "aggregates" / "results.csv").write_text(
        "metric,value\nkitchens,5913\nrho,0.6083\nlow,0.5512\nhigh,0.6701\nshare,0.125\nbeta,-0.31\nse,0.09\nplanned,3000\n",
        encoding="utf-8")
    (root / "paper" / "results.md").write_text(PAPER + extra_paper, encoding="utf-8")
    (root / "notebooks" / "clean.ipynb").write_text(json.dumps(NOTEBOOK_CLEAN), encoding="utf-8")
    (root / "references.bib").write_text(bib, encoding="utf-8")
    (root / "problem-brief.md").write_text(BRIEF, encoding="utf-8")


def run_all(root: Path):
    return {r.name: r for r in rm.run(root / "RESEARCH.map", root, offline=True, min_int=20, only=None)}


class MapTests(unittest.TestCase):
    def test_clean_map_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            self.assertEqual(run_all(root)["map"].status, "PASS", run_all(root)["map"].lines)

    def test_structure_failures(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            broken = MAP.replace("| 1 Problem | reached | | `decisions.md#d-1` |", "| 1 Problem | done | | |") \
                        .replace("`notebooks/clean.ipynb` |\n\n## Provenance", "`notebooks/missing.ipynb` |\n\n## Provenance") \
                        .replace("## Deferred\n", "") \
                        .replace("Registration: none\n", "") \
                        .replace("| 4 Data | pending | | |\n", "")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            joined = " ".join(run_all(root)["map"].lines)
            for needle in ("state 'done'", "missing.ipynb", "missing section '## Deferred'", "Registration", "missing phase(s) 4"):
                self.assertIn(needle, joined)

    def test_optional_sections_may_be_absent_but_order_holds(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            lean = MAP.split("## Facts that were once wrong")[0] + "## Deferred" + MAP.split("## Deferred")[1]
            (root / "RESEARCH.map").write_text(lean, encoding="utf-8")
            self.assertEqual(run_all(root)["map"].status, "PASS", run_all(root)["map"].lines)
            swapped = MAP.replace("## Provenance", "## Verif").replace("## Verification", "## Provenance").replace("## Verif", "## Verification")
            (root / "RESEARCH.map").write_text(swapped, encoding="utf-8")
            self.assertIn("out of order", " ".join(run_all(root)["map"].lines))

    def test_reached_gate_needs_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "RESEARCH.map").write_text(MAP.replace("| reached | | `decisions.md#d-1` |", "| reached | | |"), encoding="utf-8")
            self.assertIn("names no evidence", " ".join(run_all(root)["map"].lines))
            (root / "RESEARCH.map").write_text(MAP.replace("| reached | | `decisions.md#d-1` |", "| reached | | `decisions/missing.md` |"), encoding="utf-8")
            self.assertIn("does not resolve", " ".join(run_all(root)["map"].lines))
            doi = MAP.replace("| 8 Publication | blocked | ethics — PI | |", "| 8 Publication | reached | | https://doi.org/10.1000/xyz |")
            (root / "RESEARCH.map").write_text(doi, encoding="utf-8")
            self.assertNotIn("8 Publication", " ".join(run_all(root)["map"].lines))

    def test_more_than_three_open_hypotheses_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            rows = "".join(f"| H{i} | p | r | — | `protocol.md#h1` |\n" for i in range(2, 6))
            (root / "RESEARCH.map").write_text(MAP.replace("INCONCLUSIVE | `protocol.md#h1` |\n", "INCONCLUSIVE | `protocol.md#h1` |\n" + rows), encoding="utf-8")
            joined = " ".join(run_all(root)["map"].lines)
            self.assertIn("4 without a terminal state", joined)
            three = MAP.replace("INCONCLUSIVE | `protocol.md#h1` |\n", "INCONCLUSIVE | `protocol.md#h1` |\n" + rows.split("| H5")[0])
            (root / "RESEARCH.map").write_text(three, encoding="utf-8")
            self.assertEqual(run_all(root)["map"].status, "PASS", run_all(root)["map"].lines)

    def test_brief_reference_names_the_decision_that_fixed_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "problem-brief.md").write_text(BRIEF.replace("fixed in D-1,", "fixed beforehand,"), encoding="utf-8")
            self.assertIn("Reference names no decision", " ".join(run_all(root)["map"].lines))
            (root / "problem-brief.md").write_text(BRIEF.replace("D-1", "D-9"), encoding="utf-8")
            self.assertIn("D-9, not a block", " ".join(run_all(root)["map"].lines))

    def test_problem_statement_fields_are_required_at_the_question_pointer(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            weakened = PROTOCOL_TEXT.replace("- **Estimand:**", "- Estimando:").replace("- **Who cares:**", "- Quem:")
            (root / "protocol.md").write_text(weakened, encoding="utf-8")
            joined = " ".join(run_all(root)["map"].lines)
            self.assertIn("Estimand", joined)
            self.assertIn("Who cares", joined)
            self.assertNotIn("Refutation", joined)
            (root / "protocol.md").write_text("# Protocol\n\n## Other\n", encoding="utf-8")
            self.assertIn("no heading for anchor #question", " ".join(run_all(root)["map"].lines))

    def test_problem_brief_fields_verdict_and_gate_rule(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            # missing fields
            (root / "problem-brief.md").write_text(BRIEF.replace("- **Reference:**", "- Ref:").replace("- **Falsification:**", "- F:"), encoding="utf-8")
            joined = " ".join(run_all(root)["map"].lines)
            self.assertIn("Reference", joined)
            self.assertIn("Falsification", joined)
            # verdict disagrees with the map
            (root / "problem-brief.md").write_text(BRIEF.replace("**Verdict:** SHOWN", "**Verdict:** NOT_SHOWN"), encoding="utf-8")
            self.assertIn("Verdict is NOT_SHOWN", " ".join(run_all(root)["map"].lines))
            # protocol reached before the problem is shown
            (root / "problem-brief.md").write_text(BRIEF, encoding="utf-8")
            broken = MAP.replace("Problem: SHOWN → `problem-brief.md`", "Problem: PENDING").replace("| 3 Protocol | pending | |", "| 3 Protocol | reached | |")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            self.assertIn("does not freeze before the problem is SHOWN", " ".join(run_all(root)["map"].lines))
            # PENDING without a brief is fine while nothing past phase 2 is reached
            (root / "RESEARCH.map").write_text(MAP.replace("Problem: SHOWN → `problem-brief.md`", "Problem: PENDING"), encoding="utf-8")
            self.assertEqual(run_all(root)["map"].status, "PASS", run_all(root)["map"].lines)
            # missing Problem line
            (root / "RESEARCH.map").write_text(MAP.replace("Problem: SHOWN → `problem-brief.md`\n", ""), encoding="utf-8")
            self.assertIn("gate 1B", " ".join(run_all(root)["map"].lines))

    def test_problem_brief_numbers_are_checked(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "problem-brief.md").write_text(BRIEF.replace("5,913 kitchens", "7,777 kitchens"), encoding="utf-8")
            numbers = run_all(root)["numbers"]
            self.assertEqual(numbers.status, "FAIL")
            self.assertTrue(any("problem-brief.md" in l and "7,777" in l for l in numbers.lines), numbers.lines)

    def test_deferred_items_need_date_and_entry_condition(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            broken = MAP.replace("## Deferred\n", "## Deferred\n- try a Bayesian version some day\n")
            (root / "RESEARCH.map").write_text(broken, encoding="utf-8")
            joined = " ".join(run_all(root)["map"].lines)
            self.assertIn("Deferred", joined)
            self.assertIn("enters when", joined)

    def test_backticked_numbers_are_not_pointers(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            self.assertNotIn("`0.05`", " ".join(run_all(root)["map"].lines))


class NumbersTests(unittest.TestCase):
    def flagged(self, extra_paper: str = "") -> str:
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), extra_paper=extra_paper)
            numbers = run_all(root)["numbers"]
            return " ".join(numbers.lines)

    def test_matches_and_ignores(self):
        flagged = self.flagged()
        self.assertNotIn("5,913", flagged)      # exact
        self.assertNotIn("0.61", flagged)       # 0.6083 rounds to 0.61
        self.assertNotIn("0.55", flagged)       # range endpoints
        self.assertNotIn("0.67", flagged)
        self.assertNotIn("12.5", flagged)       # 0.125 as percent
        self.assertNotIn("2026", flagged)       # year
        self.assertNotIn(" 42", flagged)        # rm:ignore
        self.assertNotIn("9999", flagged)       # ``` fence
        self.assertNotIn("8888", flagged)       # ~~~ fence
        self.assertNotIn("0.001", flagged)      # p-value threshold
        self.assertNotIn("5.1", flagged)        # Section label
        self.assertNotIn(" 23", flagged)        # Table label

    def test_negative_numbers_are_checked_with_their_sign(self):
        self.assertNotIn("0.31", self.flagged())                     # -0.31 present in aggregates
        self.assertIn("0.77", self.flagged("\nEstimate -0.77 (SE 0.09).\n"))  # -0.77 absent → flagged
        self.assertIn("0.31", self.flagged("\nThe estimate was 0.31 (positive).\n"))  # sign error → flagged
        self.assertNotIn("0.67", self.flagged("\nRange 0.55-0.67 with a hyphen.\n"))  # a range dash is not a sign

    def test_identifiers_are_not_numbers(self):
        self.assertNotIn("37", self.flagged("\nSee D-37 and H-21 and F10.\n"))

    def test_legal_instruments_are_identifiers(self):
        flagged = self.flagged("\nDecreto nº 11.936 and Directive 2016/679 and the Act 1.234 apply; 3.333 is a count.\n")
        self.assertNotIn("14.628", flagged)   # fixture line: Lei 14.628/2023
        self.assertNotIn("1.111", flagged)    # Portaria GM nº 1.111
        self.assertNotIn("11.936", flagged)
        self.assertNotIn("1.234", flagged)
        self.assertIn("3.333", flagged)

    def test_ignore_marker_needs_a_reason(self):
        flagged = self.flagged("\nThe sample had 7,777 units. <!-- rm:ignore -->\nAlso 6,666 units. <!-- rm:ignore: quoted from the funder's call -->\n")
        self.assertIn("rm:ignore without a reason", flagged)
        self.assertNotIn("6,666", flagged)
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            self.assertIn("1 rm:ignore marker(s)", run_all(root)["numbers"].summary)

    def test_url_skips_only_its_span(self):
        flagged = self.flagged()
        self.assertIn("4,618", flagged)         # on the doi line, still checked, absent → flagged
        self.assertNotIn("units", flagged)      # 5,913 on the URL line matched

    def test_unsupported_numbers_are_reported(self):
        flagged = self.flagged("\nUnsupported: 7,777 units and 0.99 precision.\n")
        self.assertIn("7,777", flagged)
        self.assertIn("0.99", flagged)

    def test_empty_inputs_are_not_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "aggregates" / "results.csv").unlink()
            self.assertEqual(run_all(root)["numbers"].status, "NOT_VERIFIED")


class DecisionsTests(unittest.TestCase):
    def test_cross_reference_does_not_open_a_block(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            decisions = run_all(root)["decisions"]
            self.assertEqual(decisions.status, "PASS", decisions.lines)
            self.assertIn("2 decision block(s)", decisions.summary)

    def test_duplicate_and_missing_revision(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), decisions=DECISIONS_BAD)
            joined = " ".join(run_all(root)["decisions"].lines)
            self.assertIn("appears twice", joined)
            self.assertIn("no `Revision condition:`", joined)

    def test_no_blocks_is_not_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), decisions="# Decisions\n\nnothing yet\n")
            self.assertEqual(run_all(root)["decisions"].status, "NOT_VERIFIED")

    def test_table_rows_are_counted_not_passed(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), decisions=DECISIONS_OK + "\n| Id | Decision |\n|---|---|\n| D-3 | radius |\n| **D-4** | pool |\n")
            decisions = run_all(root)["decisions"]
            self.assertEqual(decisions.status, "NOT_VERIFIED")
            self.assertIn("2 decision id(s) live in table rows", decisions.summary)

    def test_empty_revision_and_unknown_supersedes(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), decisions=DECISIONS_OK + "\n### D-3 · 2026-09-04 · pool definition\nSupersedes: D-7\nRationale: none.\nRevision condition: —\n")
            joined = " ".join(run_all(root)["decisions"].lines)
            self.assertIn("empty `Revision condition:`", joined)
            self.assertIn("supersedes D-7, which is not an earlier block", joined)
            build2 = DECISIONS_OK + "\n### D-3 · 2026-09-04 · pool definition\nSupersedes: D-2\nRationale: drift re-measured.\nRevision condition: drift changes again.\n"
            (root / "decisions.md").write_text(build2, encoding="utf-8")
            self.assertEqual(run_all(root)["decisions"].status, "PASS", run_all(root)["decisions"].lines)


class DisclosureTests(unittest.TestCase):
    def test_small_cells_under_documents_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "paper" / "data").mkdir()
            (root / "paper" / "data" / "linkage.md").write_text(
                "| status | 2024 | 2025 |\n|---|---|---|\n| matched | 5913 | 6000 |\n| conflict | 3 | 0 |\n| rank | 1 | 2 | <!-- rm:ignore: ranks, not counts -->\n", encoding="utf-8")
            (root / "paper" / "data" / "cells.csv").write_text("group,n\na,12\nb,4\n", encoding="utf-8")
            disclosure = run_all(root)["disclosure"]
            self.assertEqual(disclosure.status, "FAIL")
            joined = " ".join(disclosure.lines)
            self.assertIn("linkage.md:4  cell 3", joined)
            self.assertIn("cells.csv:3  cell 4", joined)
            self.assertNotIn("rank", joined)
            self.assertNotIn("cell 0", joined)

    def test_no_floor_is_not_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "RESEARCH.map").write_text(MAP.replace("- floor: 5\n", ""), encoding="utf-8")
            self.assertEqual(run_all(root)["disclosure"].status, "NOT_VERIFIED")
            (root / "RESEARCH.map").write_text(MAP.replace("- floor: 5\n", "- floor: five\n"), encoding="utf-8")
            self.assertIn("floor must be one integer", " ".join(run_all(root)["map"].lines))


class CitationsTests(unittest.TestCase):
    def test_offline_skips_comment_and_accepts_isbn_but_flags_unsourced(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            citations = run_all(root)["citations"]
            self.assertEqual(citations.status, "FAIL")
            joined = " ".join(citations.lines)
            self.assertIn("nodoi", joined)
            self.assertNotIn("kkv", joined)
            self.assertNotIn("comment", joined)

    def test_offline_clean_bib_is_not_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), bib="@article{ok, doi={10.1/x}}\n@book{b, isbn={1}}\n")
            citations = run_all(root)["citations"]
            self.assertEqual(citations.status, "NOT_VERIFIED")
            self.assertIn("1 book(s) by ISBN", citations.summary)


class NotebooksAndCliTests(unittest.TestCase):
    def test_notebook_outputs_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp))
            (root / "notebooks" / "dirty.ipynb").write_text(json.dumps(NOTEBOOK_DIRTY), encoding="utf-8")
            notebooks = run_all(root)["notebooks"]
            self.assertEqual(notebooks.status, "FAIL")
            self.assertTrue(any("dirty.ipynb" in l for l in notebooks.lines))

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            build(root := Path(tmp), bib="@article{ok, doi={10.1/x}}\n")
            (root / "paper" / "results.md").write_text("# Results\n\nWe found 5,913 kitchens.\n\n| a | b |\n|---|---|\n| x | 12 |\n", encoding="utf-8")
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
