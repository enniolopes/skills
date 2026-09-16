import json
import os
import tempfile
import unittest
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
ROOT = REPO_ROOT / "skills" / "branding-studio"
sys.path.insert(0, str(ROOT / "scripts"))

import asset_checks
import validate_structure


def valid_spec():
    spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
    spec["meta"].update({"brand_name": "Northstar", "tier": "full", "touchpoints": ["website"]})
    spec["strategy"]["brand_job"]["statement"] = "Make a complex product legible to technical buyers."
    spec["strategy"]["audience"].update({"primary": "Technical operations leaders.", "language": "en"})
    spec["strategy"]["offer_truth"] = {
        "statement": "The product exposes operational structure from workflow data.",
        "basis": "Product documentation, section 2.",
    }
    spec["strategy"]["alternatives"] = ["manual analysis"]
    spec["strategy"]["position"]["statement"] = "Operational clarity without another generic AI layer."
    spec["strategy"]["right_to_win"]["statement"] = "Domain-specific workflow data."
    spec["strategy"]["desired_meaning"] = "Precise operational clarity."
    spec["creative_direction"].update({
        "thesis": "Reveal the hidden operating layer.",
        "principles": ["Reveal structure progressively."],
        "signature": "Layered reveal behavior.",
    })
    spec["visual"] = {
        "logo": {"production": {"status": "final", "master_format": "svg", "master_path": "assets/logo.svg"}},
        "tokens": {"color": {"ink": {"$type": "color", "$value": "#101010", "name": "Ink"}}},
    }
    return spec


class BrandingStudioScriptTests(unittest.TestCase):
    def test_sparse_contract_is_valid(self):
        spec = valid_spec()
        spec["meta"]["version"] = "2.3.0"
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_VALID")

    def test_template_declares_current_schema(self):
        spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
        self.assertEqual(spec["meta"]["schema_version"], validate_structure.SCHEMA_VERSION)

    def test_audience_language_is_required(self):
        spec = valid_spec()
        del spec["strategy"]["audience"]["language"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_ledger_blocks_are_rejected(self):
        spec = valid_spec()
        spec["evidence"] = [{"id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "active"}]
        spec["open_questions"] = ["Confirm the green."]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("evidence, open_questions" in f for f in report["failures"]))

    def test_final_logo_requires_a_master(self):
        spec = valid_spec()
        del spec["visual"]["logo"]["production"]["master_path"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_schema_4_contract_is_legacy_with_warning(self):
        legacy = valid_spec()
        legacy["meta"]["schema_version"] = 4
        del legacy["strategy"]["audience"]["language"]
        legacy["evidence"] = [{
            "id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "superseded",
        }]
        legacy["strategy"]["offer_truth"]["evidence_refs"] = ["E-001"]
        report = validate_structure.validate(legacy)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("legacy schema 4" in w for w in report["warnings"]))

    def test_schema_4_evidence_references_must_resolve(self):
        legacy = valid_spec()
        legacy["meta"]["schema_version"] = 4
        legacy["evidence"] = [{"id": "E-001", "claim": "x", "kind": "fact", "source": "y", "status": "active"}]
        legacy["strategy"]["offer_truth"]["evidence_refs"] = ["E-999"]
        self.assertEqual(validate_structure.validate(legacy)["verdict"], "STRUCTURALLY_INVALID")

    def test_pre_schema_contract_remains_operable(self):
        legacy = {
            "meta": {"version": "3.0.0", "tier": "full", "touchpoints": ["web"]},
            "research": {"findings": []},
            "visual": {"typography": {"hierarchy": {"mode": "custom", "rules": ["Explicit relationship"]}}},
        }
        self.assertEqual(validate_structure.validate(legacy)["verdict"], "STRUCTURALLY_VALID")

    def test_raster_content_blocks_svg_master(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><image href="data:image/png;base64,AAAA"/></svg>'
        with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as handle:
            handle.write(svg)
            path = handle.name
        try:
            self.assertEqual(asset_checks.inspect_svg(path)["verdict"], "SVG_STRUCTURE_INVALID")
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
