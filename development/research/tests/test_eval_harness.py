from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVAL_DIR = ROOT / "development" / "research" / "evals"
sys.path.insert(0, str(EVAL_DIR))
SPEC = importlib.util.spec_from_file_location("research_eval_run", EVAL_DIR / "run.py")
assert SPEC and SPEC.loader
RUN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUN)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)
    return result.stdout.strip()


class EvalHarnessTests(unittest.TestCase):
    def test_prose_mention_is_not_tool_use(self) -> None:
        transcript = "\n".join(
            [
                json.dumps({"type": "system", "subtype": "init", "tools": ["Task", "Read"]}),
                json.dumps(
                    {
                        "type": "assistant",
                        "message": {"content": [{"type": "text", "text": "I should call Task reviewer-2."}]},
                    }
                ),
            ]
        )
        self.assertEqual(RUN.tool_uses(transcript), [])

    def test_structured_review_and_artifact_are_observed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git(root, "init")
            git(root, "config", "user.email", "eval@example.invalid")
            git(root, "config", "user.name", "Eval")
            (root / "paper.md").write_text("draft\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "fixture")
            initial = git(root, "rev-parse", "HEAD")

            (root / "paper.md").write_text("changed\n", encoding="utf-8")
            review_dir = root / ".research" / "reviews"
            review_dir.mkdir(parents=True)
            (review_dir / "REVIEW-001.md").write_text("VERDICT: FAIL\n", encoding="utf-8")

            transcript = "\n".join(
                [
                    json.dumps(
                        {
                            "type": "system",
                            "subtype": "init",
                            "tools": ["Task", "Read", "Write"],
                        }
                    ),
                    json.dumps(
                        {
                            "type": "assistant",
                            "message": {
                                "content": [
                                    {
                                        "type": "tool_use",
                                        "name": "Task",
                                        "input": {
                                            "subagent_type": "research:reviewer-2",
                                            "prompt": "review the manuscript",
                                        },
                                    }
                                ]
                            },
                        }
                    ),
                ]
            )

            observed = RUN.deterministic_observations(root, initial, transcript)
            self.assertTrue(observed["separate_agent_invoked"])
            self.assertTrue(observed["reviewer2_invoked"])
            self.assertEqual(observed["reviewer2_call_indices"], [0])
            self.assertEqual(observed["review_records"], [".research/reviews/REVIEW-001.md"])
            self.assertIn("paper.md", observed["changed_paths"])
            self.assertIn(".research/reviews/REVIEW-001.md", observed["changed_paths"])
            self.assertIn("Task", observed["available_tools"])


if __name__ == "__main__":
    unittest.main()
