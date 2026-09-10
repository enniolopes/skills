import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SKILL = REPO_ROOT / "systems" / "research" / "skills" / "scientific-method"
REFERENCE = SKILL / "reference"
DESIGN = REPO_ROOT / "development" / "research" / "design"


class ScientificMethodTests(unittest.TestCase):
    def test_every_phase_in_skill_has_a_reference_file_and_vice_versa(self):
        text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        cited = set(re.findall(r"`reference/(\d\d-[a-z]+\.md)`", text))
        present = {p.name for p in REFERENCE.glob("*.md")}
        self.assertEqual(cited, present)
        self.assertEqual(len(present), 8)

    def test_reference_files_follow_the_distilled_shape(self):
        for path in REFERENCE.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            for marker in ("Verified 2026-", "**When this applies.**", "**What it requires.**",
                           "**The error it prevents.**", "**Exit gate.**", "**Sources.**"):
                self.assertIn(marker, text, f"{path.name} lacks {marker}")
            self.assertLessEqual(len(text.splitlines()), 70, f"{path.name}: longer than a screen")

    def test_skill_stays_under_the_design_word_budget(self):
        body = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[-1]
        self.assertLessEqual(len(body.split()), 2500)

    def test_every_reference_source_is_in_the_verification_table(self):
        table = (DESIGN / "sources-verified.md").read_text(encoding="utf-8")
        expected = ["Nosek", "Lakens", "Simonsohn", "Gilbert", "Gebru", "Wilkinson", "VanderWeele",
                    "Wagstaff", "Anselin", "Moran", "Cameron", "Gopen", "Schimel", "Heard", "von Elm",
                    "Benchimol", "Munafò", "King", "Booth", "Page", "Hernán", "Hundepool", "FAPESP",
                    "Elsevier", "SciELO", "Gelman", "Simmons"]
        for name in expected:
            self.assertIn(name, table, f"{name} cited in reference/ but absent from sources-verified.md")

    def test_terminal_states_are_named_consistently(self):
        states = {"CONFIRMED", "REFUTED", "INCONCLUSIVE", "BLOCKED", "NOT_VERIFIED"}
        skill = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        analysis = (REFERENCE / "05-analysis.md").read_text(encoding="utf-8")
        agent = (REPO_ROOT / "systems" / "research" / "agents" / "reviewer-2.md").read_text(encoding="utf-8")
        for state in states:
            self.assertIn(state, skill)
            self.assertIn(state, analysis)
        for heading in ("VERDICT", "CLAIMS", "FINDINGS", "CHECKS RUN", "NOT VERIFIED", "BASIS"):
            self.assertIn(heading, agent)


if __name__ == "__main__":
    unittest.main()
