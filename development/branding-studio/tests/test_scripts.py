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


def valid_spec(tier="full"):
    spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
    spec["meta"]["brand_name"] = "Northstar"
    spec["meta"]["tier"] = tier
    spec["meta"]["touchpoints"] = ["website", "sales deck"]

    spec["strategy"]["brand_job"]["statement"] = "Make a complex operational product immediately legible to technical buyers."
    spec["strategy"]["brand_job"]["evidence_refs"] = ["E-001"]
    spec["strategy"]["audience"]["primary"] = "Technical operations leaders."
    spec["strategy"]["audience"]["not_for"] = "General consumer audiences."
    spec["strategy"]["offer_truth"]["statement"] = "The product exposes hidden operational structure from proprietary workflow data."
    spec["strategy"]["offer_truth"]["evidence_refs"] = ["E-001"]
    spec["strategy"]["alternatives"] = ["manual analysis", "generic AI tooling"]
    spec["strategy"]["position"]["statement"] = "Operational intelligence that makes systems legible rather than adding another AI layer."
    spec["strategy"]["right_to_win"]["statement"] = "Proprietary workflow data plus domain-specific operational models."
    spec["strategy"]["desired_meaning"] = "Precise operational clarity with enough character to avoid generic enterprise AI coding."

    spec["creative_direction"]["thesis"] = "Reveal the hidden operating layer."
    spec["creative_direction"]["principles"] = [
        "Reveal structure through progressive layering rather than decorative network motifs.",
        "Let information density become part of the identity instead of hiding it."
    ]
    spec["creative_direction"]["signature"] = "Layered reveal behavior that exposes relationships progressively."
    spec["creative_direction"]["excludes"] = ["generic AI glow used as a quality signal"]

    spec["evidence"] = [{
        "id": "E-001",
        "claim": "The product uses proprietary workflow data and operational models.",
        "kind": "fact",
        "source": "internal product documentation",
        "status": "active"
    }]

    spec["visual"] = {
        "tokens": {
            "color": {
                "text": {"$value": "#111111", "$type": "color"},
                "background": {"$value": "#ffffff", "$type": "color"}
            }
        },
        "contrast_pairs": [{
            "text": "{color.text}",
            "background": "{color.background}",
            "usage": "body"
        }],
        "typography": {
            "hierarchy": {
                "mode": "custom",
                "rules": ["Display is 2–3x body depending on content and viewport."]
            }
        },
        "logo": {
            "production": {
                "status": "final",
                "master_format": "svg",
                "master_path": "assets/northstar.svg"
            }
        }
    }

    spec["portfolio_summary"] = {
        "name": {"name": "Northstar", "approach": "suggestive", "construct": "real-word"},
        "primary_color_oklch": {"L": 0.55, "C": 0.10, "H": 0},
        "logo_morphology": ["wordmark", "layered"],
        "creative_territory": ["precise", "structural"],
        "shared_cues": []
    }
    return spec


def legacy_v3_spec():
    return {
        "meta": {"version": "3.0.0", "tier": "full", "touchpoints": ["web"]},
        "research": {
            "findings": [{
                "id": "E-001",
                "claim": "A current observation exists.",
                "kind": "observation",
                "source": "https://example.com/source",
                "confidence": "high",
                "validation": "verified",
                "state": "active"
            }]
        },
        "visual": {
            "typography": {
                "hierarchy": {"mode": "custom", "rules": ["Explicit relationship"]}
            }
        }
    }


class ValidateStructureTests(unittest.TestCase):
    def test_v4_sparse_contract_is_valid(self):
        report = validate_structure.validate(valid_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("sparse contract major version" in x for x in report["passed"]))

    def test_v4_does_not_require_rationale_fields(self):
        spec = valid_spec()
        self.assertFalse(any("rationale" in key.lower() for key in spec.keys()))
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")

    def test_v4_rejects_duplicate_evidence_ids(self):
        spec = valid_spec()
        duplicate = deepcopy(spec["evidence"][0])
        duplicate["claim"] = "A second claim with the same id."
        spec["evidence"].append(duplicate)
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("duplicate" in x for x in report["failures"]))

    def test_v4_rejects_unknown_evidence_reference(self):
        spec = valid_spec()
        spec["strategy"]["brand_job"]["evidence_refs"] = ["E-999"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("unknown evidence id" in x for x in report["failures"]))

    def test_custom_typography_needs_no_modular_scale(self):
        report = validate_structure.validate(valid_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("mode=custom" in x for x in report["passed"]))

    def test_final_logo_requires_master_path_and_format(self):
        spec = valid_spec()
        del spec["visual"]["logo"]["production"]["master_path"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("final logo" in x for x in report["failures"]))

    def test_zero_hue_is_valid(self):
        report = validate_structure.validate(valid_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("H=0 is valid" in x for x in report["passed"]))

    def test_naming_collision_is_state_not_creative_verdict(self):
        spec = valid_spec()
        spec["naming"] = {"clearance": {"status": "collision"}}
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("naming clearance state" in x for x in report["passed"]))

    def test_legacy_v3_remains_operable_without_old_rationale_requirements(self):
        report = validate_structure.validate(legacy_v3_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("legacy v3" in x for x in report["warnings"]))

    def test_pre_v3_evidence_can_lack_ids(self):
        spec = legacy_v3_spec()
        spec["meta"]["version"] = "2.4.0"
        del spec["research"]["findings"][0]["id"]
        del spec["research"]["findings"][0]["state"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("legacy v2" in x for x in report["warnings"]))


class PortfolioCollisionTests(unittest.TestCase):
    def test_missing_morphology_stays_unknown(self):
        cand = valid_spec()["portfolio_summary"]
        sister = deepcopy(cand)
        sister["name"]["name"] = "Other"
        sister["logo_morphology"] = []
        result = portfolio_collision.compare(
            cand,
            sister,
            portfolio_collision.DEFAULT_POLICIES["house-of-brands"],
        )
        self.assertIsNone(result["morphology"]["tag_jaccard"])

    def test_branded_house_similarity_is_context_not_severity(self):
        cand = valid_spec()["portfolio_summary"]
        sister = deepcopy(cand)
        sister["name"]["name"] = "Northstar Labs"
        result = portfolio_collision.compare(
            cand,
            sister,
            portfolio_collision.DEFAULT_POLICIES["branded-house"],
        )
        self.assertEqual(result["morphology"]["architecture_context"], "related_expected")
        self.assertNotIn("severity", result["morphology"])

    def test_name_comparison_exposes_raw_signals(self):
        signals = portfolio_collision.name_signals(
            {"name": "North Star", "approach": "suggestive", "construct": "compound"},
            {"name": "Northstar", "approach": "suggestive", "construct": "compound"},
        )
        self.assertTrue(signals["exact_normalized_match"])
        self.assertTrue(signals["same_approach"])
        self.assertTrue(signals["same_construct"])


class AssetCheckTests(unittest.TestCase):
    def test_raster_image_blocks_svg_master(self):
        svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <image href="data:image/png;base64,AAAA" width="100" height="100"/>
        </svg>"""
        with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as handle:
            handle.write(svg)
            path = handle.name
        try:
            report = asset_checks.inspect_svg(path)
            self.assertEqual(report["verdict"], "SVG_STRUCTURE_INVALID")
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
