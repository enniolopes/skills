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

import validate_structure
import portfolio_collision
import asset_checks


def valid_spec(tier="full"):
    spec = json.loads((ROOT / "templates" / "brand-spec.template.json").read_text())
    spec["meta"]["brand_name"] = "Northstar"
    spec["meta"]["tier"] = tier
    spec["meta"]["touchpoints"] = ["web"]
    spec["meta"]["architecture"]["model"] = "house-of-brands"
    spec["meta"]["architecture"]["$rationale"] = "Independent venture inside the studio portfolio."

    spec["research"]["findings"] = [{
        "id": "E-001",
        "claim": "Competitor A uses a blue geometric identity.",
        "kind": "observation",
        "source": "https://example.com/competitor-a",
        "confidence": "high",
        "validation": "verified",
        "state": "active"
    }]

    spec["strategy"]["customer"]["who_it_is"] = "Technical operations leaders."
    spec["strategy"]["customer"]["who_it_is_NOT"] = "General consumer audiences."
    spec["strategy"]["customer"]["insight"] = "They need fast comprehension without consumer-tech tropes."
    spec["strategy"]["customer"]["$rationale"] = "Derived from founder interviews and buying-process evidence."
    spec["strategy"]["right_to_win"]["statement"] = "Proprietary operational data and domain expertise."
    spec["strategy"]["right_to_win"]["evidence_refs"] = ["E-001"]
    spec["strategy"]["right_to_win"]["$rationale"] = "Supported by internal capability evidence."
    spec["strategy"]["differentiation"]["statement"] = "Operational clarity rather than generic AI automation."
    spec["strategy"]["differentiation"]["$rationale"] = "Competitor audit shows category convergence around generic AI claims."
    spec["strategy"]["context"]["chosen_context"] = "AI tooling is converging visually and verbally."
    spec["strategy"]["context"]["$rationale"] = "Observed across the current competitor set."
    spec["strategy"]["theme"]["statement"] = "Make operations legible."
    spec["strategy"]["theme"]["because_test"] = "Make operations legible because proprietary data exposes hidden operational structure."
    spec["strategy"]["theme"]["onliness"] = "A focused operational-intelligence system for this workflow."
    spec["strategy"]["theme"]["$rationale"] = "Compresses the customer problem and right-to-win."

    spec["creative_direction"]["central_idea"]["statement"] = "Reveal the hidden operating layer."
    spec["creative_direction"]["central_idea"]["$rationale"] = "Translates the theme into a visual and verbal behavior."
    spec["creative_direction"]["principles"] = [{
        "name": "Reveal structure",
        "rule": "Use progressive disclosure and visible systems rather than decoration.",
        "enables": ["layering"],
        "excludes": ["ambient gradients"],
        "$rationale": "Directly expresses the operating-layer idea."
    }]
    spec["creative_direction"]["$excludes"] = "Generic AI glow, robots and abstract network spheres."

    spec["naming"]["in_scope"] = True
    spec["naming"]["name"] = "Northstar"
    spec["naming"]["$rationale"] = "Signals orientation while remaining broader than the initial product."
    spec["naming"]["$excludes"] = "AI suffixes and descriptive workflow names."
    spec["naming"]["clearance"]["status"] = "no_apparent_collision"
    spec["naming"]["clearance"]["search_date"] = "2026-09-04"
    spec["naming"]["clearance"]["evidence"] = ["current INPI/domain triage"]

    spec["verbal"]["principles"] = ["Precise"]
    spec["verbal"]["not_like_this"] = [{
        "example": "Revolutionize everything with next-gen AI.",
        "why_not": "Generic hype obscures operational specificity."
    }]

    spec["visual"]["$overall_rationale"] = "Visible structure turns the strategic idea into repeatable visual behavior."
    spec["visual"]["$excludes"] = "Generic neon gradients and undifferentiated SaaS minimalism."
    spec["visual"]["identity_grammar"]["principles"] = ["layered structure"]
    spec["visual"]["identity_grammar"]["$rationale"] = "Derived from the creative direction."
    spec["visual"]["tokens"] = {
        "color": {
            "text": {"$value": "#111111", "$type": "color"},
            "background": {"$value": "#ffffff", "$type": "color"}
        }
    }
    spec["visual"]["contrast_pairs"] = [{
        "text": "{color.text}",
        "background": "{color.background}",
        "usage": "body"
    }]
    spec["visual"]["palette"]["colors"] = ["#111111", "#ffffff"]
    spec["visual"]["palette"]["$rationale"] = "High-clarity base supports the structural device."
    spec["visual"]["palette"]["$excludes"] = "Blue-purple AI gradient conventions."
    spec["visual"]["typography"]["families"] = ["Example Sans"]
    spec["visual"]["typography"]["roles"] = ["display + text"]
    spec["visual"]["typography"]["hierarchy"] = {
        "mode": "custom",
        "base_px": None,
        "ratio": None,
        "steps": [],
        "rules": ["Display is 2–3x body depending on viewport; body remains 16–18px."]
    }
    spec["visual"]["typography"]["$rationale"] = "One variable family supports both precision and range."
    spec["visual"]["typography"]["$excludes"] = "Default geometric SaaS pairing."
    spec["visual"]["logo"]["concept"] = "Layered N wordmark device."
    spec["visual"]["logo"]["production"] = {
        "status": "final",
        "master_format": "svg",
        "master_path": "assets/northstar.svg",
        "production_brief": ""
    }
    spec["visual"]["logo"]["$rationale"] = "The layered N embodies the reveal-structure idea."
    spec["visual"]["logo"]["$excludes"] = "Network nodes, sparkle stars and robot motifs."

    spec["trial_applications"] = [{
        "touchpoint": "web",
        "job": "Explain the product to a technical buyer.",
        "artifact": "trials/homepage",
        "failures_found": [],
        "system_changes": [],
        "status": "tested"
    }]

    spec["portfolio_summary"] = {
        "name": {"name": "Northstar", "approach": "suggestive", "construct": "real-word"},
        "primary_color_oklch": {"L": 0.55, "C": 0.10, "H": 0},
        "logo_morphology": ["wordmark", "layered"],
        "creative_territory": ["precise", "structural"],
        "shared_cues": []
    }
    return spec


class ValidateStructureTests(unittest.TestCase):
    def test_zero_hue_is_valid(self):
        report = validate_structure.validate(valid_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("H=0 is valid" in x for x in report["passed"]))

    def test_full_collision_blocks(self):
        spec = valid_spec()
        spec["naming"]["clearance"]["status"] = "collision"
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("collision" in x for x in report["failures"]))

    def test_custom_typography_needs_no_modular_scale(self):
        report = validate_structure.validate(valid_spec())
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("mode=custom" in x for x in report["passed"]))

    def test_v3_requires_evidence_id_and_state(self):
        spec = valid_spec()
        del spec["research"]["findings"][0]["id"]
        del spec["research"]["findings"][0]["state"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("id" in x and "state" in x for x in report["failures"]))

    def test_v3_rejects_duplicate_evidence_ids(self):
        spec = valid_spec()
        duplicate = deepcopy(spec["research"]["findings"][0])
        duplicate["claim"] = "A second independent observation exists."
        spec["research"]["findings"].append(duplicate)
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_INVALID")
        self.assertTrue(any("duplicate" in x for x in report["failures"]))

    def test_pre_v3_evidence_remains_backward_compatible(self):
        spec = valid_spec()
        spec["meta"]["version"] = "2.4.0"
        del spec["research"]["findings"][0]["id"]
        del spec["research"]["findings"][0]["state"]
        report = validate_structure.validate(spec)
        self.assertEqual(report["verdict"], "STRUCTURALLY_VALID")
        self.assertTrue(any("pre-v3 evidence format accepted" in x for x in report["warnings"]))


class PortfolioCollisionTests(unittest.TestCase):
    def test_missing_morphology_is_unknown(self):
        cand = valid_spec()["portfolio_summary"]
        sister = deepcopy(cand)
        sister["name"]["name"] = "Other"
        sister["logo_morphology"] = []
        policy = portfolio_collision.DEFAULT_POLICIES["house-of-brands"]
        result = portfolio_collision.compare(cand, sister, policy)
        self.assertEqual(result["morphology"]["severity"], "UNKNOWN")

    def test_branded_house_allows_related_cues(self):
        cand = valid_spec()["portfolio_summary"]
        sister = deepcopy(cand)
        sister["name"]["name"] = "Northstar Labs"
        result = portfolio_collision.compare(
            cand,
            sister,
            portfolio_collision.DEFAULT_POLICIES["branded-house"],
        )
        self.assertNotEqual(result["morphology"]["severity"], "HIGH")
        self.assertEqual(result["morphology"]["severity"], "INFO")


class AssetCheckTests(unittest.TestCase):
    def test_raster_image_blocks_svg_master(self):
        svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <image href="data:image/png;base64,AAAA" width="100" height="100"/>
        </svg>"""
        with tempfile.NamedTemporaryFile("w", suffix=".svg", delete=False) as f:
            f.write(svg)
            path = f.name
        try:
            report = asset_checks.inspect_svg(path)
            self.assertEqual(report["verdict"], "SVG_STRUCTURE_INVALID")
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
