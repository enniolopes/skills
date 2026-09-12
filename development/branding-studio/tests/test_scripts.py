import json
import os
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
ROOT = REPO_ROOT / "skills" / "branding-studio"
sys.path.insert(0, str(ROOT / "scripts"))

import asset_checks
import portfolio_collision
import validate_structure


def valid_spec():
    spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
    spec["meta"].update({"brand_name": "Northstar", "tier": "full", "touchpoints": ["website"]})
    spec["strategy"]["brand_job"]["statement"] = "Make a complex product legible to technical buyers."
    spec["strategy"]["audience"]["primary"] = "Technical operations leaders."
    spec["strategy"]["offer_truth"]["statement"] = "The product exposes operational structure from workflow data."
    spec["strategy"]["alternatives"] = ["manual analysis"]
    spec["strategy"]["position"]["statement"] = "Operational clarity without another generic AI layer."
    spec["strategy"]["right_to_win"]["statement"] = "Domain-specific workflow data."
    spec["strategy"]["desired_meaning"] = "Precise operational clarity."
    spec["creative_direction"].update({
        "thesis": "Reveal the hidden operating layer.",
        "principles": ["Reveal structure progressively."],
        "signature": "Layered reveal behavior.",
    })
    spec["evidence"] = [{
        "id": "E-001",
        "claim": "The product uses workflow data.",
        "kind": "fact",
        "source": "internal product documentation",
        "status": "active",
    }]
    spec["strategy"]["offer_truth"]["evidence_refs"] = ["E-001"]
    spec["visual"] = {
        "logo": {"production": {"status": "final", "master_format": "svg", "master_path": "assets/logo.svg"}}
    }
    spec["portfolio_summary"] = {
        "name": {"name": "Northstar", "approach": "suggestive", "construct": "real-word"},
        "primary_color_oklch": {"L": 0.55, "C": 0.10, "H": 0},
        "logo_morphology": ["wordmark"],
        "creative_territory": ["precise"],
        "shared_cues": [],
    }
    return spec


class BrandingStudioScriptTests(unittest.TestCase):
    def test_sparse_v4_contract_is_valid(self):
        spec = valid_spec()
        spec["meta"]["version"] = "2.3.0"
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_VALID")

    def test_evidence_references_must_resolve(self):
        spec = valid_spec()
        spec["strategy"]["offer_truth"]["evidence_refs"] = ["E-999"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_final_logo_requires_a_master(self):
        spec = valid_spec()
        del spec["visual"]["logo"]["production"]["master_path"]
        self.assertEqual(validate_structure.validate(spec)["verdict"], "STRUCTURALLY_INVALID")

    def test_legacy_contract_remains_operable(self):
        legacy = {
            "meta": {"version": "3.0.0", "tier": "full", "touchpoints": ["web"]},
            "research": {"findings": []},
            "visual": {"typography": {"hierarchy": {"mode": "custom", "rules": ["Explicit relationship"]}}},
        }
        self.assertEqual(validate_structure.validate(legacy)["verdict"], "STRUCTURALLY_VALID")

    def test_portfolio_comparison_is_advisory(self):
        candidate = valid_spec()["portfolio_summary"]
        sister = deepcopy(candidate)
        sister["name"]["name"] = "Northstar Labs"
        sister["logo_morphology"] = []
        result = portfolio_collision.compare(
            candidate,
            sister,
            portfolio_collision.DEFAULT_POLICIES["branded-house"],
        )
        self.assertNotIn("severity", result["morphology"])
        self.assertIsNone(result["morphology"]["tag_jaccard"])

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
