import importlib.util
import tempfile
import unittest
from pathlib import Path
import zipfile


DEV_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = DEV_ROOT / "package_skill.py"
spec = importlib.util.spec_from_file_location("package_skill", SCRIPT)
package_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_skill)


class PackageSkillTests(unittest.TestCase):
    def test_runtime_source_matches_explicit_manifest(self):
        actual = package_skill.runtime_file_set()
        expected = set(package_skill.RUNTIME_FILES)
        self.assertEqual(actual, expected)

        top_level = {Path(rel).parts[0] for rel in actual}
        self.assertEqual(top_level, {"SKILL.md", "references", "templates", "scripts"})

    def test_package_contains_only_runtime_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "branding-studio.zip"
            package_skill.package(output)

            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())

            expected = {
                f"branding-studio/{rel}" for rel in package_skill.RUNTIME_FILES
            }
            self.assertEqual(names, expected)
            self.assertNotIn("branding-studio/README.md", names)
            self.assertFalse(any("/tests/" in name for name in names))
            self.assertFalse(any("/evals/" in name for name in names))
            self.assertFalse(any("package_skill.py" in name for name in names))
            self.assertFalse(any("validate_spec.py" in name for name in names))
            self.assertFalse(any("portfolio_distance.py" in name for name in names))


if __name__ == "__main__":
    unittest.main()
