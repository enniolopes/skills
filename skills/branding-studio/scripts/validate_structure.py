#!/usr/bin/env python3
"""
validate_structure.py — deterministic structural validator for branding-studio v2.

This tool checks only what code can prove from the brand spec:
- required structure / non-placeholder decision fields;
- evidence record shape and provenance;
- negative specifications;
- DTCG token shape and alias resolution;
- declared WCAG 2.x contrast pairs;
- modular type-scale math, only when the hierarchy mode is modular;
- logo production-state coherence;
- naming-triage state;
- trial-application presence.

Exit 0 means STRUCTURALLY_VALID. It does NOT mean the strategy, rationale,
creative direction or aesthetics are good. Those require semantic review.
"""

import json
import math
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from color_tools import check_pair  # noqa: E402


PLACEHOLDER_MARKERS = (
    "fill in",
    "declared at creation",
    "statement",
    "why this",
    "what was",
    "pending block",
)

VALID_KINDS = {"fact", "observation", "hypothesis"}
VALID_CONFIDENCE = {"high", "medium", "low"}
VALID_VALIDATION = {"verified", "needs_field_research"}
VALID_TIERS = {"provisional", "full"}
VALID_HIERARCHY = {"modular", "custom", "fluid"}
VALID_PRODUCTION = {"final", "concept", "external_craft_required"}

DIGITAL_TOUCHPOINT_TERMS = (
    "web", "website", "app", "ui", "product", "digital", "interface", "saas"
)


def _get(d, path, default=None):
    cur = d
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            return default
        cur = cur[key]
    return cur


def _text(value, min_len=4):
    if not isinstance(value, str):
        return False
    s = value.strip()
    if len(s) < min_len:
        return False
    low = s.lower()
    return not any(marker in low for marker in PLACEHOLDER_MARKERS)


def _nonblank(value):
    return isinstance(value, str) and bool(value.strip())


def _nonempty_list(value):
    return isinstance(value, list) and any(
        (isinstance(x, str) and x.strip()) or isinstance(x, dict)
        for x in value
    )


def resolve_token(spec, ref):
    """Resolve a DTCG alias like {color.semantic.text} to a terminal value."""
    seen = set()
    while isinstance(ref, str) and ref.startswith("{") and ref.endswith("}"):
        path = ref[1:-1]
        if path in seen:
            return None, f"circular token reference: {ref}"
        seen.add(path)
        node = _get(spec, f"visual.tokens.{path}")
        if not isinstance(node, dict) or "$value" not in node:
            return None, f"token reference does not resolve: {ref}"
        ref = node["$value"]
    return ref, None


def walk_tokens(node, path, errors):
    if not isinstance(node, dict):
        errors.append(f"token group is not an object: {path}")
        return
    if "$value" in node:
        if "$type" not in node:
            errors.append(f"token missing $type: {path}")
        return
    for key, value in node.items():
        if key.startswith("_") or key.startswith("$"):
            continue
        walk_tokens(value, f"{path}.{key}", errors)


def _validate_modular_scale(hierarchy, failures, passed):
    base = hierarchy.get("base_px")
    ratio = hierarchy.get("ratio")
    steps = hierarchy.get("steps", [])
    if not (
        isinstance(base, (int, float))
        and base > 0
        and isinstance(ratio, (int, float))
        and ratio > 1
        and isinstance(steps, list)
        and steps
        and all(isinstance(x, (int, float)) and x > 0 for x in steps)
    ):
        failures.append(
            "typography hierarchy mode=modular requires positive base_px, ratio>1 and numeric steps"
        )
        return

    bad = []
    for size in steps:
        try:
            n = round(math.log(size / base, ratio))
        except (ValueError, ZeroDivisionError):
            bad.append(str(size))
            continue
        expected = base * (ratio ** n)
        if abs(size - expected) / expected > 0.015:
            bad.append(f"{size} (nearest scale value ~{expected:.2f})")

    if bad:
        failures.append("modular typography steps outside 1.5% tolerance: " + ", ".join(bad))
    else:
        passed.append(f"modular typography scale is mathematically consistent (base={base}, ratio={ratio})")


def validate(spec):
    failures, warnings, passed = [], [], []

    tier = str(_get(spec, "meta.tier", "")).strip().lower()
    if tier not in VALID_TIERS:
        failures.append("meta.tier must be provisional or full")
    else:
        passed.append(f"tier declared: {tier}")
    provisional = tier == "provisional"

    touchpoints = [
        t.strip()
        for t in _get(spec, "meta.touchpoints", [])
        if isinstance(t, str) and t.strip()
    ]
    if touchpoints:
        passed.append(f"touchpoints declared: {touchpoints}")
    else:
        failures.append("meta.touchpoints is empty")

    required_rationales = [
        "strategy.customer.$rationale",
        "strategy.right_to_win.$rationale",
        "strategy.differentiation.$rationale",
        "strategy.context.$rationale",
        "strategy.theme.$rationale",
        "creative_direction.central_idea.$rationale",
        "visual.$overall_rationale",
        "visual.identity_grammar.$rationale",
        "visual.typography.$rationale",
    ]
    naming_in_scope = bool(_get(spec, "naming.in_scope", True))
    if naming_in_scope:
        required_rationales.append("naming.$rationale")
    if _get(spec, "visual.logo", None) is not None:
        required_rationales.append("visual.logo.$rationale")

    for path in required_rationales:
        if _text(_get(spec, path)):
            passed.append(f"rationale present: {path}")
        else:
            failures.append(
                f"missing/non-substantive rationale: {path} — structural presence only; semantic quality is reviewed separately"
            )

    negatives = [
        ("strategy.customer.who_it_is_NOT", "not-customer"),
        ("creative_direction.$excludes", "creative exclusions"),
        ("visual.$excludes", "visual exclusions"),
    ]
    if naming_in_scope:
        negatives.append(("naming.$excludes", "naming exclusions"))

    for path, label in negatives:
        if _text(_get(spec, path)):
            passed.append(f"negative specification present: {label}")
        else:
            failures.append(f"negative specification missing: {path}")

    not_like = _get(spec, "verbal.not_like_this", [])
    if any(isinstance(x, dict) and _text(x.get("example")) and _text(x.get("why_not")) for x in not_like):
        passed.append("verbal counter-example present")
    else:
        (warnings if provisional else failures).append(
            "verbal.not_like_this has no substantive counter-example"
        )

    findings = _get(spec, "research.findings", [])
    valid_findings = 0
    if isinstance(findings, list):
        for i, finding in enumerate(findings):
            if not isinstance(finding, dict):
                failures.append(f"research.findings[{i}] must be an object")
                continue
            claim = finding.get("claim")
            kind = str(finding.get("kind", "")).strip()
            source = finding.get("source")
            confidence = str(finding.get("confidence", "")).strip()
            validation_state = str(finding.get("validation", "")).strip()
            problems = []
            if not _text(claim):
                problems.append("claim")
            if kind not in VALID_KINDS:
                problems.append("kind")
            if not _text(source):
                problems.append("source")
            if confidence not in VALID_CONFIDENCE:
                problems.append("confidence")
            if validation_state not in VALID_VALIDATION:
                problems.append("validation")
            if problems:
                failures.append(
                    f"research.findings[{i}] invalid fields: {', '.join(problems)}"
                )
            else:
                valid_findings += 1

    if valid_findings:
        passed.append(f"research provenance records valid: {valid_findings}")
    else:
        (warnings if provisional else failures).append(
            "no valid research finding with claim/kind/source/confidence/validation"
        )

    principles = _get(spec, "creative_direction.principles", [])
    good_principles = [
        p for p in principles
        if isinstance(p, dict) and _text(p.get("name")) and _text(p.get("rule"))
        and _text(p.get("$rationale"))
    ] if isinstance(principles, list) else []
    if good_principles:
        passed.append(f"creative principles declared: {len(good_principles)}")
    else:
        failures.append("creative_direction.principles has no substantive principle")

    tokens = _get(spec, "visual.tokens", {})
    if tokens:
        token_errors = []
        walk_tokens(tokens, "visual.tokens", token_errors)
        failures.extend(token_errors)
        if not token_errors:
            passed.append("declared design tokens are structurally DTCG-compatible")
    else:
        warnings.append("visual.tokens empty — acceptable when no machine-consumable token system is needed")

    pairs = _get(spec, "visual.contrast_pairs", [])
    needs_digital_contrast = any(
        term in tp.lower() for tp in touchpoints for term in DIGITAL_TOUCHPOINT_TERMS
    )
    if not pairs and needs_digital_contrast:
        (warnings if provisional else failures).append(
            "digital touchpoint declared but visual.contrast_pairs is empty"
        )
    elif isinstance(pairs, list):
        for i, pair in enumerate(pairs):
            if not isinstance(pair, dict):
                failures.append(f"visual.contrast_pairs[{i}] must be an object")
                continue
            fg, e1 = resolve_token(spec, pair.get("text", ""))
            bg, e2 = resolve_token(spec, pair.get("background", ""))
            if e1 or e2:
                failures.append(f"contrast pair {i} unresolved: {e1 or e2}")
                continue
            usage = pair.get("usage", "body")
            if not (
                isinstance(fg, str) and isinstance(bg, str)
                and re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", fg)
                and re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", bg)
            ):
                failures.append(f"contrast pair {i} does not resolve to hex colors")
                continue
            result = check_pair(fg, bg, usage)
            if result["wcag_aa"]:
                passed.append(
                    f"declared contrast pair {i} passes WCAG AA ({usage}): {result['wcag_ratio']}:1"
                )
            else:
                failures.append(
                    f"declared contrast pair {i} fails WCAG AA ({usage}): {result['wcag_ratio']}:1"
                )
            if not result["apca_ok"]:
                warnings.append(
                    f"declared contrast pair {i} has low APCA/Lc signal: {result['apca_lc']} (quality signal, not compliance)"
                )

    families = _get(spec, "visual.typography.families", [])
    roles = _get(spec, "visual.typography.roles", [])
    if not _nonempty_list(families):
        (warnings if provisional else failures).append("visual.typography.families is empty")
    if not _nonempty_list(roles):
        failures.append("visual.typography.roles is empty")

    hierarchy = _get(spec, "visual.typography.hierarchy", {})
    mode = str(hierarchy.get("mode", "")).strip().lower() if isinstance(hierarchy, dict) else ""
    if mode not in VALID_HIERARCHY:
        failures.append("visual.typography.hierarchy.mode must be modular, custom or fluid")
    elif mode == "modular":
        _validate_modular_scale(hierarchy, failures, passed)
    else:
        rules = hierarchy.get("rules", [])
        if _nonempty_list(rules):
            passed.append(f"typography hierarchy mode={mode} has explicit rules")
        else:
            failures.append(f"typography hierarchy mode={mode} requires explicit rules")

    logo = _get(spec, "visual.logo", {})
    if isinstance(logo, dict) and logo:
        production = logo.get("production", {})
        status = str(production.get("status", "")).strip()
        if status not in VALID_PRODUCTION:
            failures.append("visual.logo.production.status invalid")
        elif status == "final":
            if _nonblank(production.get("master_format")) and _nonblank(production.get("master_path")):
                passed.append("logo production status=final with declared master")
            else:
                failures.append("final logo requires production.master_format and production.master_path")
        elif status == "external_craft_required":
            if _text(production.get("production_brief"), min_len=20):
                passed.append("external logo craft dependency has production brief")
            else:
                failures.append("external_craft_required logo needs a substantive production_brief")
        elif status == "concept":
            if tier == "full":
                failures.append("full tier cannot finish with logo production.status=concept; finalize or mark external_craft_required")
            else:
                warnings.append("logo remains concept-stage in provisional tier")

    if naming_in_scope:
        clearance = _get(spec, "naming.clearance", {})
        status = str(clearance.get("status", "not_searched")).strip()
        if tier == "full":
            if status in {"not_searched", "collision"}:
                failures.append(f"full-tier naming clearance unresolved: status={status}")
            elif status == "uncertain":
                warnings.append("naming clearance uncertain — specialist review is still required")
            else:
                passed.append(f"naming triage state acceptable for structural delivery: {status}")
        elif status in {"not_searched", "uncertain"}:
            warnings.append(f"provisional naming triage pending/uncertain: {status}")

    trials = _get(spec, "trial_applications", [])
    good_trials = [
        t for t in trials
        if isinstance(t, dict)
        and _nonblank(t.get("touchpoint"))
        and _text(t.get("job"))
        and t.get("status") in {"tested", "approved"}
    ] if isinstance(trials, list) else []
    if good_trials:
        passed.append(f"trial applications tested: {len(good_trials)}")
    else:
        (warnings if provisional else failures).append(
            "no trial application with substantive touchpoint/job and status tested|approved"
        )

    summary = _get(spec, "portfolio_summary", {})
    summary_name = _get(summary, "name.name", "")
    if naming_in_scope and not _text(summary_name):
        warnings.append("portfolio_summary.name is empty; portfolio name collision will be UNKNOWN")
    morph = summary.get("logo_morphology", []) if isinstance(summary, dict) else []
    if not _nonempty_list(morph):
        warnings.append("portfolio_summary.logo_morphology empty; morphology collision will be UNKNOWN")
    color = summary.get("primary_color_oklch") if isinstance(summary, dict) else None
    if isinstance(color, dict):
        h = color.get("H")
        if h is not None and isinstance(h, (int, float)) and 0 <= h <= 360:
            passed.append("portfolio_summary primary hue declared (H=0 is valid)")
        else:
            warnings.append("portfolio_summary.primary_color_oklch has invalid/missing hue")
    elif color is None:
        warnings.append("portfolio_summary.primary_color_oklch unknown/not applicable")

    verdict = "STRUCTURALLY_VALID" if not failures else "STRUCTURALLY_INVALID"
    return {
        "brand": _get(spec, "meta.brand_name", "?"),
        "version": _get(spec, "meta.version", "?"),
        "tier": tier or "?",
        "verdict": verdict,
        "failures": failures,
        "warnings": warnings,
        "passed": passed,
        "scope_note": (
            "Deterministic structural validation only. Semantic quality, strategic coherence, "
            "creative quality, field perception and legal conclusions are outside this verdict."
        ),
    }


def main(path):
    with open(path, encoding="utf-8") as f:
        spec = json.load(f)
    report = validate(spec)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["verdict"] == "STRUCTURALLY_VALID" else 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(0)
    sys.exit(main(sys.argv[1]))
