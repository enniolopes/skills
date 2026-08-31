#!/usr/bin/env python3
"""
validate_spec.py — Validates a brand spec against the skill's invariants.

Deterministic checks (pass/fail):
  1. RATIONALE: every decision block has a non-empty $rationale — no element
     exists without justifying itself from strategy. This is the anti-generic mechanism.
  2. NEGATIVE SPECIFICATION: key blocks have $excludes / who_it_is_NOT /
     not_like_this filled — without the excluded case, audits become opinion.
  3. THEME: the "because" test is filled (theme connects to right_to_win) and onliness.
  4. TOKENS: DTCG leaves have $value and $type; {a.b.c} references resolve.
  5. CONTRAST: every pair declared in visual.contrast_pairs passes WCAG 2.2 AA
     (legal floor) and reports Lc/APCA (quality score).
  6. TYPE SCALE: steps ≈ base * ratio^n (1.5% tolerance).
  7. LOGO: proportional clear_space declared; if type "expressive", an external brief is required.
  8. VOICE CHART: every principle covers Podmajersky's 6 dimensions.
  9. TIER: provisional specs may leave clearance/full voice chart pending, but the
     pending blocks must be explicitly marked (see spec-schema.md).

Usage: python validate_spec.py path/to/brand-spec.json
Output: JSON report; exit 0 = valid, 1 = failures.
"""
import json
import math
import re
import sys

sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from color_tools import check_pair  # noqa: E402

VOICE_DIMENSIONS = {"concepts", "vocabulary", "verbosity", "grammar", "punctuation", "capitalization"}


def _get(d, path, default=None):
    cur = d
    for k in path.split('.'):
        if not isinstance(cur, dict) or k not in cur:
            return default
        cur = cur[k]
    return cur


def _filled(x):
    return isinstance(x, str) and len(x.strip()) > 8 and 'fill in' not in x.lower()


def resolve_token(spec, ref):
    """Resolve '{color.semantic.text}' -> hex, following DTCG aliases."""
    seen = set()
    while isinstance(ref, str) and ref.startswith('{') and ref.endswith('}'):
        path = ref[1:-1]
        if path in seen:
            return None, f"circular reference: {ref}"
        seen.add(path)
        node = _get(spec, f"visual.tokens.{path}")
        if node is None:
            return None, f"reference does not resolve: {ref}"
        ref = node.get('$value') if isinstance(node, dict) else node
    if isinstance(ref, str) and re.fullmatch(r'#([0-9a-fA-F]{3}|[0-9a-fA-F]{6})', ref.strip()):
        return ref.strip(), None
    return None, f"final value is not hex: {ref!r}"


def walk_tokens(node, path, errors):
    if not isinstance(node, dict):
        return
    if '$value' in node:
        if '$type' not in node:
            errors.append(f"token missing $type: {path}")
        return
    for k, v in node.items():
        if k.startswith('_') or k.startswith('$'):
            continue
        walk_tokens(v, f"{path}.{k}", errors)


def validate(spec):
    failures, warnings, passed = [], [], []
    tier = str(_get(spec, "meta.tier", "full")).strip().lower()
    provisional = tier.startswith("provisional")

    # touchpoints declared (drives deliverable compilation)
    tps = _get(spec, "meta.touchpoints", [])
    real_tps = [t for t in tps if isinstance(t, str) and 'declared at creation' not in t and t.strip()]
    if real_tps:
        passed.append(f"touchpoints declared: {real_tps}")
    else:
        failures.append("meta.touchpoints empty — without declared touchpoints there is nothing to compile deliverables for")

    # 1-2. rationale + negatives on decision blocks
    require_rationale = [
        "strategy.customer", "strategy.right_to_win", "strategy.differentiation",
        "strategy.context", "naming", "visual.palette", "visual.typography", "visual.logo",
    ]
    for p in require_rationale:
        if _filled(_get(spec, p + ".$rationale")):
            passed.append(f"rationale present: {p}")
        else:
            failures.append(f"NO RATIONALE: {p}.$rationale empty — decision does not justify itself from strategy")

    negatives = [
        ("strategy.customer.who_it_is_NOT", "who the customer is NOT"),
        ("naming.$excludes", "name types avoided"),
        ("visual.$excludes", "visual territory avoided"),
        ("visual.logo.$excludes", "morphologies avoided"),
    ]
    for p, label in negatives:
        if _filled(_get(spec, p)):
            passed.append(f"negative specification present: {label}")
        else:
            failures.append(f"NO NEGATIVE: {p} — without the excluded case, audits become opinion")
    nlt = _get(spec, "verbal.not_like_this", [])
    if not nlt or not any(_filled(x.get("example", "")) for x in nlt):
        failures.append("NO NEGATIVE: verbal.not_like_this empty — voice without a counter-example")

    # 3. theme
    if _filled(_get(spec, "strategy.theme.because_test")):
        passed.append("'because' test declared")
    else:
        failures.append("strategy.theme.because_test empty — theme does not connect to right_to_win")
    onl = _get(spec, "strategy.theme.onliness", "")
    if _filled(onl) and ("only" in onl.lower() or "unic" in onl.lower() or "únic" in onl.lower()):
        passed.append("onliness statement present")
    else:
        warnings.append("onliness weak/absent — if 'only' does not fit the sentence, there is no zag (Neumeier)")

    # 4. DTCG tokens
    tok_errors = []
    walk_tokens(_get(spec, "visual.tokens", {}), "visual.tokens", tok_errors)
    failures += tok_errors
    if not tok_errors:
        passed.append("tokens in DTCG format ($value/$type)")

    # 5. contrast
    pairs = _get(spec, "visual.contrast_pairs", [])
    if not pairs:
        failures.append("no contrast pair declared — nothing verifiable in the palette")
    for pair in pairs:
        fg, e1 = resolve_token(spec, pair.get("text", ""))
        bg, e2 = resolve_token(spec, pair.get("background", ""))
        if e1 or e2:
            failures.append(f"contrast pair does not resolve: {e1 or e2}")
            continue
        r = check_pair(fg, bg, pair.get("usage", "body"))
        if r["wcag_aa"]:
            passed.append(f"WCAG AA ok ({pair.get('usage')}): {fg} on {bg} = {r['wcag_ratio']}:1, Lc {r['apca_lc']}")
        else:
            failures.append(f"FAILS WCAG AA ({pair.get('usage')}): {fg} on {bg} = {r['wcag_ratio']}:1")
        if not r["apca_ok"]:
            warnings.append(f"Lc below recommended ({pair.get('usage')}): {r['apca_lc']} — passes the legal floor but perceptual legibility is weak")

    # 6. type scale
    sc = _get(spec, "visual.typography.scale", {})
    base, ratio, steps = sc.get("base_px"), sc.get("ratio"), sc.get("steps", [])
    if base and ratio and steps:
        bad = []
        for s in steps:
            n = round(math.log(s / base, ratio))
            expected = base * (ratio ** n)
            if abs(s - expected) / expected > 0.015:
                bad.append(f"{s}px (expected ~{expected:.2f})")
        if bad:
            failures.append("steps outside the modular scale: " + ", ".join(bad))
        else:
            passed.append(f"modular scale consistent (base {base}, ratio {ratio})")
    else:
        failures.append("type scale incomplete (base_px, ratio, steps)")

    # 7. logo
    cs = _get(spec, "visual.logo.clear_space", "")
    if _filled(cs) and ("proportional" in cs.lower() or "x" in cs.lower()):
        passed.append("proportional clear space declared")
    else:
        failures.append("clear_space missing or non-proportional — absolute values do not scale")
    if "expressive" in str(_get(spec, "visual.logo.type", "")).lower() and "constructible" not in str(_get(spec, "visual.logo.type", "")).lower():
        warnings.append("logo type EXPRESSIVE: outside the constructible domain — require a brief for an external designer + acceptance criteria")

    # 8. voice chart
    vc = _get(spec, "verbal.voice_chart", {})
    principles = [k for k in vc if not k.startswith('_')]
    if not principles:
        (warnings if provisional else failures).append("voice_chart empty" + (" (tolerated in provisional tier — mark as pending)" if provisional else ""))
    for pr in principles:
        covered = {k for k, v in vc[pr].items() if _filled(str(v))} if isinstance(vc[pr], dict) else set()
        missing = VOICE_DIMENSIONS - covered
        if missing:
            (warnings if provisional else failures).append(f"voice_chart['{pr}'] missing dimensions: {sorted(missing)}")
        else:
            passed.append(f"voice_chart['{pr}'] covers all 6 dimensions")

    # 9. one-route delivery: discarded routes must exist (exploration happened)
    routes = _get(spec, "discarded_routes", [])
    if any(_filled(x.get("route", "")) and _filled(x.get("why_discarded", "")) for x in routes):
        passed.append("discarded routes recorded — single delivery is justified by exploration")
    else:
        (warnings if provisional else failures).append(
            "discarded_routes empty — a single route without recorded alternatives suggests no exploration (one big idea requires it)")

    # 10. portfolio projection: the summary feeds portfolio_distance.py
    ps = _get(spec, "portfolio_summary", {})
    ps_name = _get(ps, "name.name", "") if isinstance(ps.get("name"), dict) else ""
    ps_ok = bool(str(ps_name).strip()) \
        and isinstance(ps.get("primary_color_oklch"), dict) and ps["primary_color_oklch"].get("H") not in (None, 0) \
        and any(str(t).strip() and 'tags:' not in str(t) for t in ps.get("logo_morphology", []))
    if ps_ok:
        passed.append("portfolio_summary filled — brand is comparable against sisters")
    else:
        failures.append("portfolio_summary incomplete (name/oklch/morphology) — portfolio_distance.py cannot run; anti-convergence check is impossible")

    # 11. tier-specific
    if provisional:
        passed.append("tier: provisional — clearance and full voice chart may remain pending, promotion to full requires them")
    else:
        status = str(_get(spec, "naming.clearance.inpi_status", "not_searched"))
        if status == "not_searched":
            failures.append("full tier with naming.clearance.inpi_status = not_searched — triage is mandatory before full delivery")

    return {
        "brand": _get(spec, "meta.brand_name", "?"),
        "version": _get(spec, "meta.version", "?"),
        "tier": tier,
        "verdict": "VALID" if not failures else "INVALID",
        "failures": failures, "warnings": warnings, "passed": passed,
        "note": "Deterministic checks. Heuristic judgment (hierarchy, gestalt, tone-to-moment fit) is done by the model in AUDIT mode, always kept separate from these numbers.",
    }


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(0)
    with open(sys.argv[1]) as f:
        spec = json.load(f)
    report = validate(spec)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    sys.exit(0 if report["verdict"] == "VALID" else 1)
