import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNTIME_ROOT = REPO_ROOT / "skills" / "branding-studio"
SKILL = RUNTIME_ROOT / "SKILL.md"
REFERENCES = sorted((RUNTIME_ROOT / "references").glob("*.md"))
RUNTIME_MARKDOWN = [SKILL, *REFERENCES]

FORBIDDEN_META_PHRASES = (
    "operating constitution",
    "this skill is",
    "the skill can",
    "the skill may",
    "the skill's result",
    "host ai already",
    "human agency org chart",
    "compatibility wrapper",
    "package_skill.py",
    "development/branding-studio",
    "docs/branding-studio",
    "readme.md",
)

CONTROL_PLANE = "SEARCH → PROVE → COMMIT → ADAPT"


class RuntimeContextTests(unittest.TestCase):
    def test_runtime_markdown_contains_no_development_metadocumentation(self):
        for path in RUNTIME_MARKDOWN:
            text = path.read_text(encoding="utf-8").lower()
            for phrase in FORBIDDEN_META_PHRASES:
                self.assertNotIn(phrase, text, f"{path}: forbidden runtime meta-text: {phrase}")

    def test_runtime_body_does_not_explain_itself_as_a_skill(self):
        for path in RUNTIME_MARKDOWN:
            text = path.read_text(encoding="utf-8")
            if path == SKILL:
                # Ignore YAML frontmatter metadata; inspect executable body only.
                parts = text.split("---", 2)
                body = parts[2] if len(parts) == 3 else text
            else:
                body = text
            self.assertIsNone(
                re.search(r"\bskill\b", body, flags=re.IGNORECASE),
                f"{path}: runtime prose should instruct/define domain behavior, not explain the skill",
            )

    def test_global_control_plane_has_one_canonical_home(self):
        occurrences = {
            path: path.read_text(encoding="utf-8").count(CONTROL_PLANE)
            for path in RUNTIME_MARKDOWN
        }
        self.assertEqual(occurrences[SKILL], 1)
        for path in REFERENCES:
            self.assertEqual(
                occurrences[path],
                0,
                f"{path}: global kernel belongs in SKILL.md; references should contain intent/domain deltas",
            )

    def test_runtime_title_is_not_release_or_architecture_documentation(self):
        body = SKILL.read_text(encoding="utf-8").split("---", 2)[-1]
        first_heading = next(line for line in body.splitlines() if line.startswith("# "))
        self.assertEqual(first_heading, "# Branding Studio")
        self.assertNotRegex(first_heading, r"\bv\d+\b")


if __name__ == "__main__":
    unittest.main()
