import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / "systems" / "research" / "skills" / "research-map" / "scripts" / "epistemic.py"
spec = importlib.util.spec_from_file_location("epistemic_validate", SCRIPT)
ep = importlib.util.module_from_spec(spec)
sys.modules["epistemic_validate"] = ep
spec.loader.exec_module(ep)

MAP = """# RESEARCH.map — epistemic fixture

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
Registration: https://example.org/registration, 2026-09-14

## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | Y < 0 | primary decision rule fails | — | `protocol.md#h1` |

## Gates
| Phase | State | Blocked by | Evidence |
|---|---|---|---|
| 1 Problem | reached | | `problem-brief.md` |
| 2 Literature | pending | | |
| 3 Protocol | reached | | `protocol.md` |
| 4 Data | reached | | `data.csv` |
| 5 Analysis | pending | | |
| 6 Writing | pending | | |
| 7 Review | pending | | |
| 8 Publication | pending | | |

## Deferred

## Last session
- 2026-09-14: fixture initialized.
- Next: run primary analysis.
"""

PROTOCOL = """# Protocol

## question
Does X change Y?

Claim: associational
Unit of analysis: municipality
Estimand: E1 population contrast
Refutation: primary decision rule fails
Objection: selection
Who cares: programme office
Non-goals: mechanisms

## h1
H1: X predicts lower Y. Estimand E1. Primary test T1.
"""

PLAN = """# Analysis plan

Freeze: frozen

## H1

Estimand: E1
Primary test: T1
Mode: confirmatory
Generated from: none

### Design
Claim type: associational
Population: municipalities
Exposure: X
Outcome: Y
Contrast: X vs not X
Time: 2026
Identification: descriptive associational contrast
Dependence: cluster by region

### Decision rule
CONFIRMED when: interval is below zero under T1
REFUTED when: interval is above zero under T1
INCONCLUSIVE when: interval includes zero under T1

### Assumptions
| ID | Assumption | Check | Failure action |
|---|---|---|---|
| A1 | regional dependence is material | K1 | BLOCKED |

### Primary analysis
Test: T1
Estimator: pre-specified estimator
Inference: clustered interval
Why this estimates E1: targets the recorded contrast

### Sensitivity
- S1: alternate defensible specification

### Specification dimensions
- none

### Interpretation boundary
May claim: association under E1
May not claim: causal effect
"""


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def commit(root: Path, message: str) -> str:
    git(root, "add", ".")
    git(root, "commit", "-m", message)
    return git(root, "rev-parse", "HEAD")


def build_base(root: Path, plan_text: str = PLAN) -> str:
    (root / "aggregates").mkdir()
    (root / "paper").mkdir()
    (root / "notebooks").mkdir()
    (root / ".research" / "runs").mkdir(parents=True)
    (root / "RESEARCH.map").write_text(MAP, encoding="utf-8")
    (root / "protocol.md").write_text(PROTOCOL, encoding="utf-8")
    (root / "analysis-plan.md").write_text(plan_text, encoding="utf-8")
    (root / "decisions.md").write_text("# Decisions\n", encoding="utf-8")
    (root / "problem-brief.md").write_text("Construct: Y\nPopulation: municipalities\nMeasure: Y\nReference: D-1\nMagnitude: 100\nFalsification: checked\nVerdict: SHOWN\n", encoding="utf-8")
    (root / "references.bib").write_text("", encoding="utf-8")
    (root / "data.csv").write_text("x,y\n0,1\n1,0\n", encoding="utf-8")
    git(root, "init")
    git(root, "config", "user.email", "research@example.org")
    git(root, "config", "user.name", "Research Test")
    return commit(root, "freeze protocol and plan")


def add_run(root: Path, freeze: str, *, run_id: str = "RUN-001", test: str = "T1", mode: str = "confirmatory", generated_input: str = "DATA2") -> str:
    (root / "aggregates" / "h1.csv").write_text("estimate,lower,upper\n-0.3,-0.5,-0.1\n", encoding="utf-8")
    run_commit = commit(root, "execute analysis")
    manifest = {
        "id": run_id,
        "mode": mode,
        "commit": run_commit,
        "protocol_freeze": freeze,
        "analysis_plan_freeze": freeze,
        "hypothesis": "H1",
        "estimand": "E1",
        "test": test,
        "registration": "https://example.org/registration",
        "inputs": [{"id": generated_input, "path": "data.csv", "role": "confirmatory" if mode == "confirmatory" else "discovery"}],
        "outputs": [{"result": "R1", "artifact": "aggregates/h1.csv"}],
    }
    (root / ".research" / "runs" / f"{run_id}.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    commit(root, "record run manifest")
    return run_commit


class EpistemicValidatorTests(unittest.TestCase):
    def test_valid_confirmatory_chain_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            freeze = build_base(root)
            add_run(root, freeze)
            (root / "paper" / "results.md").write_text(
                "The estimate was below zero. <!-- claim:C1 inference:I1 result:R1 decides:H1 -->\n",
                encoding="utf-8",
            )
            commit(root, "write claim")
            plan_result, plan, _ = ep.check_plan(root)
            runs_result, runs, results = ep.check_runs(root, root / "RESEARCH.map", plan)
            lineage = ep.check_lineage(root, root / "RESEARCH.map", plan, results)
            exposure = ep.check_exposure(plan, runs)
            self.assertNotEqual(plan_result.status, "FAIL")
            self.assertEqual(runs_result.status, "PASS")
            self.assertEqual(lineage.status, "PASS")
            self.assertEqual(exposure.status, "PASS")

    def test_missing_primary_test_fails_plan(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build_base(root, PLAN.replace("Primary test: T1", "Primary test: TBD"))
            result, _, _ = ep.check_plan(root)
            self.assertEqual(result.status, "FAIL")

    def test_plan_freeze_after_run_fails_temporal_check(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            freeze = build_base(root)
            (root / "aggregates" / "h1.csv").write_text("estimate\n-0.3\n", encoding="utf-8")
            run_commit = commit(root, "execute before late freeze")
            (root / "analysis-plan.md").write_text(PLAN + "\n<!-- late edit -->\n", encoding="utf-8")
            late_freeze = commit(root, "late analysis plan freeze")
            manifest = {
                "id": "RUN-001",
                "mode": "confirmatory",
                "commit": run_commit,
                "protocol_freeze": freeze,
                "analysis_plan_freeze": late_freeze,
                "hypothesis": "H1",
                "estimand": "E1",
                "test": "T1",
                "inputs": [{"id": "DATA2", "path": "data.csv", "role": "confirmatory"}],
                "outputs": [{"result": "R1", "artifact": "aggregates/h1.csv"}],
            }
            (root / ".research" / "runs" / "RUN-001.json").write_text(json.dumps(manifest), encoding="utf-8")
            commit(root, "record invalid manifest")
            _, plan, _ = ep.check_plan(root)
            result, _, _ = ep.check_runs(root, root / "RESEARCH.map", plan)
            self.assertEqual(result.status, "FAIL")
            self.assertTrue(any("does not predate" in line for line in result.lines))

    def test_non_primary_result_cannot_decide_hypothesis(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            freeze = build_base(root)
            add_run(root, freeze, test="T2", mode="exploratory")
            (root / "paper" / "results.md").write_text(
                "Exploratory result decides H1. <!-- claim:C1 inference:I1 result:R1 decides:H1 -->\n",
                encoding="utf-8",
            )
            _, plan, _ = ep.check_plan(root)
            _, _, results = ep.check_runs(root, root / "RESEARCH.map", plan)
            lineage = ep.check_lineage(root, root / "RESEARCH.map", plan, results)
            self.assertEqual(lineage.status, "FAIL")
            self.assertTrue(any("primary test" in line for line in lineage.lines))

    def test_discovery_data_cannot_confirm_generated_hypothesis(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            freeze = build_base(root, PLAN.replace("Generated from: none", "Generated from: DATA1"))
            add_run(root, freeze, generated_input="DATA1")
            _, plan, _ = ep.check_plan(root)
            _, runs, _ = ep.check_runs(root, root / "RESEARCH.map", plan)
            exposure = ep.check_exposure(plan, runs)
            self.assertEqual(exposure.status, "FAIL")

    def test_discovery_reuse_is_allowed_when_run_is_exploratory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            freeze = build_base(root, PLAN.replace("Generated from: none", "Generated from: DATA1"))
            add_run(root, freeze, mode="exploratory", generated_input="DATA1")
            _, plan, _ = ep.check_plan(root)
            _, runs, _ = ep.check_runs(root, root / "RESEARCH.map", plan)
            exposure = ep.check_exposure(plan, runs)
            self.assertEqual(exposure.status, "PASS")


if __name__ == "__main__":
    unittest.main()
