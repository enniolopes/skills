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
        cited = set(re.findall(r"`reference/([\w-]+\.md)`", text))
        present = {p.name for p in REFERENCE.glob("*.md")}
        self.assertEqual(cited, present)
        self.assertEqual(len([n for n in present if n[:2].isdigit()]), 8)
        self.assertIn("problem-statement.md", present)
        self.assertIn("problem-brief.md", present)

    def test_reference_files_follow_the_distilled_shape(self):
        for path in REFERENCE.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            for marker in ("Sources located 2026-", "**When this applies.**", "**What it requires.**",
                           "**The error it prevents.**", "**Exit gate.**", "**Sources.**"):
                self.assertIn(marker, text, f"{path.name} lacks {marker}")
            self.assertLessEqual(len(text.splitlines()), 75, f"{path.name}: longer than a screen")

    def test_skill_stays_under_the_design_word_budget(self):
        body = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[-1]
        self.assertLessEqual(len(body.split()), 2500)

    def test_every_reference_source_is_in_the_verification_table(self):
        table = (DESIGN / "sources-verified.md").read_text(encoding="utf-8")
        expected = ["Lesko", "Fox", "Loeb", "Bardach", "Kingdon", "Mitroff", "Jacobs", "Shook", "Fitzpatrick",
                    "Getzels", "Chi, Feltovich", "Heilmeier", "E9(R1)", "Alvesson", "Hulley", "Simon", "Rittel", "Passi", "Nosek", "Lakens", "Simonsohn", "Gilbert", "Gebru", "Wilkinson", "VanderWeele",
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
        for heading in ("VERDICT", "CLAIMS", "FINDINGS", "CHECKS RUN", "NOT_VERIFIED", "BASIS"):
            self.assertIn(heading, agent)
        self.assertNotIn("NOT VERIFIED", agent, "one spelling of the state everywhere")

    def test_runtime_is_domain_neutral(self):
        """The pieces serve any research; the origin case lives in development/ only."""
        origin_terms = re.compile(
            r"cozinha|kitchen|habilita|solid[aá]ri|delbem|cozsolidarias|\bMDS\b|VIGISAN|CadInsan|Bolsa|\bPBF\b|"
            r"regi[oõ]es imediatas|5,913|4,618|299/137|566/133",
            re.I,
        )
        runtime = list((REPO_ROOT / "systems" / "research" / "skills").rglob("*")) + \
            list((REPO_ROOT / "systems" / "research" / "agents").glob("*.md"))
        for path in runtime:
            if path.is_file() and path.suffix in {".md", ".py", ".json", ".map"}:
                hit = origin_terms.search(path.read_text(encoding="utf-8"))
                if hit:
                    self.fail(f"{path.relative_to(REPO_ROOT)}: origin-case term {hit.group(0)!r} in runtime")

    def test_no_origin_case_codes_or_repo_paths_leak_into_runtime(self):
        for path in [*REFERENCE.glob("*.md"), SKILL / "SKILL.md"]:
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"\bF\d{1,2}\)|origin case|design record", path.name)


if __name__ == "__main__":
    unittest.main()
