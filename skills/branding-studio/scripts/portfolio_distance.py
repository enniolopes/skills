#!/usr/bin/env python3
"""
portfolio_distance.py — Portfolio anti-convergence (internal Distinctive Asset Grid).

Compares a candidate brand against every sister brand in the portfolio registry
and computes a composite distance per dimension. Weighting follows the empirical
hierarchy of asset strength (Ehrenberg-Bass / Romaniuk): SHAPE and NAME weigh more
than COLOR — shape is the strongest distinctive asset (40% fame / 71% uniqueness
in a 1,162-asset benchmark); color is the weakest (12% / 39%) and legally almost
never ownable. Two sisters sharing a color is therefore a smaller risk than two
sisters sharing logo morphology or name type.

Dimensions compared (all from the brand spec / registry):
  color        — OKLCH distance of the primary hue (circular) + L,C
  shape        — Jaccard of logo morphology tags (e.g., geometric, monogram,
                 letterform, angular, organic, circular-grid...)
  name         — 2-axis taxonomy: approach (descriptive/suggestive/abstract)
                 and construct (real-word/compound/coined) + crude phonetic collision
  personality  — Jaccard of personality/territory adjectives

Usage:
  python portfolio_distance.py portfolio.json candidate.json
  (candidate.json = full brand spec or a summary with the registry's fields)

Output: JSON with per-sister and per-dimension distance, composite score [0..1]
(0 = identical, 1 = maximum distance) and convergence flags.
Default alert thresholds: composite < 0.35, or any high-weight dimension < 0.25.
"""
import json
import math
import sys

WEIGHTS = {"shape": 0.40, "name": 0.30, "color": 0.15, "personality": 0.15}
COMPOSITE_THRESHOLD = 0.35
HIGH_WEIGHT_THRESHOLD = 0.25  # applies to shape and name

APPROACH_POS = {"descriptive": 0.0, "suggestive": 0.5, "evocative": 0.5, "abstract": 1.0}


def _norm_tags(x):
    return {str(t).strip().lower() for t in (x or []) if str(t).strip()}


def jaccard_distance(a, b):
    a, b = _norm_tags(a), _norm_tags(b)
    if not a and not b:
        return 1.0  # nothing declared on either side: no evidence of collision
    inter, union = len(a & b), len(a | b)
    return 1.0 - (inter / union if union else 0.0)


def dist_color(c1, c2):
    """c = {"L":..,"C":..,"H":..} in OKLCH. Circular hue dominates (weight 0.7)."""
    if not c1 or not c2:
        return 1.0
    dh = abs(c1["H"] - c2["H"]) % 360
    dh = min(dh, 360 - dh) / 180.0                        # [0..1]
    dl = abs(c1.get("L", 0.5) - c2.get("L", 0.5))         # [0..1]
    dc = abs(c1.get("C", 0.1) - c2.get("C", 0.1)) / 0.4   # ~[0..1]
    return min(1.0, 0.7 * dh + 0.15 * dl + 0.15 * min(1.0, dc))


def dist_name(n1, n2):
    if not n1 or not n2:
        return 1.0
    a1 = APPROACH_POS.get(str(n1.get("approach", "")).lower(), 0.5)
    a2 = APPROACH_POS.get(str(n2.get("approach", "")).lower(), 0.5)
    d_approach = abs(a1 - a2)  # [0..1]
    d_construct = 0.0 if str(n1.get("construct", "")).lower() == str(n2.get("construct", "")).lower() else 1.0
    # crude phonetic collision: same first 3 letters or same marked suffix
    w1, w2 = str(n1.get("name", "")).lower(), str(n2.get("name", "")).lower()
    phon = 0.0
    if w1 and w2:
        if w1[:3] == w2[:3]:
            phon += 0.5
        for suf in ("ify", "ly", "io", "ai", "tech", "lab", "labs", "hub", "ia"):
            if w1.endswith(suf) and w2.endswith(suf):
                phon += 0.5
                break
    return max(0.0, min(1.0, 0.4 * d_approach + 0.3 * d_construct + 0.3 * (1.0 - min(1.0, phon))))


def compare(cand, sister):
    d = {
        "color": round(dist_color(cand.get("primary_color_oklch"), sister.get("primary_color_oklch")), 3),
        "shape": round(jaccard_distance(cand.get("logo_morphology"), sister.get("logo_morphology")), 3),
        "name": round(dist_name(cand.get("name"), sister.get("name")), 3),
        "personality": round(jaccard_distance(cand.get("personality"), sister.get("personality")), 3),
    }
    composite = round(sum(WEIGHTS[k] * d[k] for k in WEIGHTS), 3)
    flags = []
    if composite < COMPOSITE_THRESHOLD:
        flags.append(f"CONVERGENCE: composite distance {composite} < {COMPOSITE_THRESHOLD}")
    for k in ("shape", "name"):
        if d[k] < HIGH_WEIGHT_THRESHOLD:
            flags.append(f"CONVERGENCE in {k.upper()} (high-weight asset): {d[k]} < {HIGH_WEIGHT_THRESHOLD}")
    if d["color"] < 0.15:
        flags.append("Warning: same color territory (low weight, but combined with another collision it becomes a problem)")
    return {"distances": d, "composite": composite, "flags": flags}


def main(portfolio_path, candidate_path):
    with open(portfolio_path) as f:
        portfolio = json.load(f)
    with open(candidate_path) as f:
        cand = json.load(f)
    # accepts a full spec or a summary: extract the summary if it is a spec
    if "portfolio_summary" in cand:
        cand = cand["portfolio_summary"]
    results = []
    for sister in portfolio.get("brands", []):
        r = compare(cand, sister.get("portfolio_summary", sister))
        r["brand"] = sister.get("brand_name") or sister.get("portfolio_summary", {}).get("name", {}).get("name", "?")
        results.append(r)
    any_flag = any(r["flags"] for r in results)
    out = {
        "candidate": cand.get("name", {}).get("name", "?"),
        "verdict": "REJECT/REVISE" if any_flag else "APPROVED: sufficient distance from the portfolio",
        "comparisons": sorted(results, key=lambda r: r["composite"]),
        "method": "Weighted distance (shape 0.40, name 0.30, color 0.15, personality 0.15) reflecting the empirical hierarchy of asset distinctiveness.",
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 1 if any_flag else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(0)
    sys.exit(main(sys.argv[1], sys.argv[2]))
