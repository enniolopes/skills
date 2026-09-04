import importlib.util
import tempfile
import unittest
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "package_skill.py"
spec = importlib.util.spec_from_file_location("package_skill", SCRIPT)
package_skill = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package_skill)


class PackageSkillTests(unittest.TestCase):
    def test_package_has_portable_root_and_required_skill_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "branding-studio.zip"
            package_skill.package(output)
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()

            self.assertIn("branding-studio/SKILL.md", names)
            self.assertTrue(all(name.startswith("branding-studio/") for name in names))
            self.assertFalse(any("/__pycache__/" in name or "/dist/" in name for name in names))


if __name__ == "__main__":
    unittest.main()
