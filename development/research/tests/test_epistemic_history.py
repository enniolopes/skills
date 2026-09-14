import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / "systems" / "research" / "skills" / "research-map" / "scripts" / "epistemic.py"
spec = importlib.util.spec_from_file_location("epistemic_history", SCRIPT)
ep = importlib.util.module_from_spec(spec)
sys.modules["epistemic_history"] = ep
spec.loader.exec_module(ep)

MAP = """# RESEARCH.map
## Layout
- protocol: protocol.md
- decisions: decisions.md
- aggregates: aggregates/
- documents: paper/
- notebooks: notebooks/
- references: references.bib
- floor: 5
## Question
Q → `protocol.md#question`
Problem: SHOWN → `problem-brief.md`
Registration: https://example.org/reg, 2026-09-14
## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | p | r | INCONCLUSIVE | `protocol.md#h1` |
## Gates
| Phase | State | Blocked by | Evidence |
|---|---|---|---|
| 1 Problem | pending | | |
| 2 Literature | pending | | |
| 3 Protocol | pending | | |
| 4 Data | pending | | |
| 5 Analysis | pending | | |
| 6 Writing | pending | | |
| 7 Review | pending | | |
| 8 Publication | pending | | |
## Deferred
## Last session
- 2026-09-14: fixture.
- Next: reopen.
"""

OLD_PLAN = """# Analysis plan
Freeze: frozen
## H1
Estimand: E1
Primary test: T1
Mode: confirmatory
Generated from: none
Dependence: region
CONFIRMED when: T1 below zero
REFUTED when: T1 above zero
INCONCLUSIVE when: otherwise
| ID | Assumption | Check | Failure action |
|---|---|---|---|
| A1 | a | K1 | BLOCKED |
May claim: old E1 association
May not claim: causality
"""

NEW_PLAN = OLD_PLAN.replace("Estimand: E1", "Estimand: E2").replace("Primary test: T1", "Primary test: T3").replace("old E1", "new E2")


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=root, text=True, capture_output=True, check=True).stdout.strip()


def commit(root: Path, message: str) -> str:
    git(root, "add", ".")
    git(root, "commit", "-m", message)
    return git(root, "rev-parse", "HEAD")


class EpistemicHistoryTests(unittest.TestCase):
    def test_reopen_does_not_rewrite_old_run_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "aggregates").mkdir()
            (root / "paper").mkdir()
            (root / "notebooks").mkdir()
            (root / ".research" / "runs").mkdir(parents=True)
            for name, content in {
                "RESEARCH.map": MAP,
                "protocol.md": "# Protocol\n## question\nQ\n## h1\nH1 E1 T1\n",
                "analysis-plan.md": OLD_PLAN,
                "decisions.md": "# Decisions\n",
                "problem-brief.md": "# Brief\n",
                "references.bib": "",
                "data.csv": "x,y\n0,1\n1,0\n",
            }.items():
                (root / name).write_text(content, encoding="utf-8")
            git(root, "init")
            git(root, "config", "user.email", "history@example.org")
            git(root, "config", "user.name", "History Test")
            freeze = commit(root, "old freeze")

            (root / "aggregates" / "old.csv").write_text("estimate\n-0.2\n", encoding="utf-8")
            run_commit = commit(root, "old primary run")
            manifest = {
                "id": "RUN-001",
                "mode": "confirmatory",
                "analysis_role": "primary",
                "commit": run_commit,
                "protocol_freeze": freeze,
                "analysis_plan_freeze": freeze,
                "hypothesis": "H1",
                "estimand": "E1",
                "test": "T1",
                "registration": "https://example.org/reg",
                "inputs": [{"id": "DATA1", "path": "data.csv", "role": "confirmatory"}],
                "outputs": [{"result": "R1", "artifact": "aggregates/old.csv"}],
            }
            (root / ".research" / "runs" / "RUN-001.json").write_text(json.dumps(manifest), encoding="utf-8")
            commit(root, "record old run")

            (root / "analysis-plan.md").write_text(NEW_PLAN, encoding="utf-8")
            commit(root, "reopen with new estimand and primary test")

            _, current_plan, _ = ep.check_plan(root)
            runs, _, result_index = ep.check_runs(root, root / "RESEARCH.map", current_plan)
            self.assertEqual(runs.status, "PASS")
            self.assertEqual(result_index["R1"]["estimand"], "E1")
            self.assertEqual(result_index["R1"]["frozen_primary_test"], "T1")


if __name__ == "__main__":
    unittest.main()
