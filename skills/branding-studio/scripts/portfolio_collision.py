#!/usr/bin/env python3
"""
portfolio_collision.py — architecture-aware portfolio collision signals.

This tool does NOT calculate a universal "brand distance" score.

It compares a candidate's compact portfolio summary against sister brands and
reports per-dimension similarity signals. Whether similarity is a problem depends
on the declared brand-architecture policy.

Missing data is UNKNOWN, never "maximum distance".

Usage:
    python portfolio_collision.py portfolio.json candidate-spec.json

Exit codes:
    0 = no HIGH policy collision detected
    1 = at least one HIGH policy collision detected
"""

import difflib
import json
import re
import sys
import unicodedata


DEFAULT_POLICIES = {
    "house-of-brands": {
        "name": "separate",
        "morphology": "separate",
        "color": "prefer_separate",
        "creative_territory": "separate",
    },
    "endorsed": {
        "name": "separate",
        "morphology": "separate",
        "color": "allow",
        "creative_territory": "separate",
    },
    "branded-house": {
        "name": "allow_related",
        "morphology": "allow_related",
        "color": "allow_related",
        "creative_territory": "allow_related",
    },
    "hybrid": {
        "name": "custom",
        "morphology": "custom",
        "color": "custom",
        "creative_territory": "custom",
    },
}

SEPARATE_HIGH = 0.75
SEPARATE_MEDIUM = 0.50
PREFER_SEPARATE_HIGH = 0.85

VALID_INTENTS = {"separate", "prefer_separate", "allow", "allow_related", "custom"}


def _normalize_text(value):
    value = unicodedata.normalize("NFKD", str(value or "")).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def _tags(value):
    if not isinstance(value, list):
        return None
    out = {_normalize_text(x) for x in value if _normalize_text(x)}
    return out or None


def jaccard_similarity(a, b):
    a, b = _tags(a), _tags(b)
    if a is None or b is None:
        return None
    union = a | b
    return len(a & b) / len(union) if union else None


def name_similarity(a, b):
    if not isinstance(a, dict) or not isinstance(b, dict):
        return None

    w1 = _normalize_text(a.get("name"))
    w2 = _normalize_text(b.get("name"))
    if not w1 or not w2:
        return None
    if w1 == w2:
        return 1.0

    lexical = difflib.SequenceMatcher(None, w1, w2).ratio()

    tax_signals = []
    for key in ("approach", "construct"):
        v1 = _normalize_text(a.get(key))
        v2 = _normalize_text(b.get(key))
        if v1 and v2:
            tax_signals.append(1.0 if v1 == v2 else 0.0)

    taxonomy = sum(tax_signals) / len(tax_signals) if tax_signals else None
    return lexical if taxonomy is None else (0.75 * lexical + 0.25 * taxonomy)


def color_similarity(a, b):
    """Heuristic OKLCH similarity in [0,1]. Returns None when either color is unknown."""
    if not isinstance(a, dict) or not isinstance(b, dict):
        return None
    try:
        l1, c1, h1 = float(a["L"]), float(a["C"]), float(a["H"])
        l2, c2, h2 = float(b["L"]), float(b["C"]), float(b["H"])
    except (KeyError, TypeError, ValueError):
        return None

    dh = abs(h1 - h2) % 360
    dh = min(dh, 360 - dh) / 180.0
    dl = min(1.0, abs(l1 - l2))
    dc = min(1.0, abs(c1 - c2) / 0.4)
    distance = min(1.0, 0.65 * dh + 0.20 * dl + 0.15 * dc)
    return 1.0 - distance


def classify_similarity(value):
    if value is None:
        return "UNKNOWN"
    if value >= 0.85:
        return "VERY_HIGH"
    if value >= 0.65:
        return "HIGH"
    if value >= 0.40:
        return "MEDIUM"
    return "LOW"


def policy_signal(dimension, similarity, intent, exact_name=False):
    if similarity is None:
        return {
            "severity": "UNKNOWN",
            "message": f"{dimension}: insufficient data for collision check",
        }

    if exact_name and dimension == "name":
        return {
            "severity": "HIGH",
            "message": "name: exact normalized name collision",
        }

    if intent == "separate":
        if similarity >= SEPARATE_HIGH:
            return {
                "severity": "HIGH",
                "message": (
                    f"{dimension}: similarity {similarity:.3f} conflicts with policy 'separate' "
                    f"(studio heuristic threshold >= {SEPARATE_HIGH})"
                ),
            }
        if similarity >= SEPARATE_MEDIUM:
            return {
                "severity": "MEDIUM",
                "message": (
                    f"{dimension}: similarity {similarity:.3f} deserves review under policy 'separate'"
                ),
            }
        return {"severity": "LOW", "message": f"{dimension}: no material collision signal"}

    if intent == "prefer_separate":
        if similarity >= PREFER_SEPARATE_HIGH:
            return {
                "severity": "MEDIUM",
                "message": (
                    f"{dimension}: strong overlap {similarity:.3f}; policy prefers separation but does not forbid sharing"
                ),
            }
        return {"severity": "LOW", "message": f"{dimension}: acceptable under prefer_separate"}

    if intent in {"allow", "allow_related"}:
        return {
            "severity": "INFO",
            "message": f"{dimension}: similarity {similarity:.3f} is permitted by architecture policy '{intent}'",
        }

    return {
        "severity": "UNKNOWN",
        "message": f"{dimension}: custom policy requires human/model interpretation",
    }


def _candidate_summary(candidate):
    return candidate.get("portfolio_summary", candidate)


def _architecture_model(candidate, portfolio):
    meta_model = (
        candidate.get("meta", {})
        .get("architecture", {})
        .get("model")
        if isinstance(candidate, dict)
        else None
    )
    if meta_model in DEFAULT_POLICIES:
        return meta_model
    studio_default = portfolio.get("studio", {}).get("default_architecture")
    return studio_default if studio_default in DEFAULT_POLICIES else "house-of-brands"


def _policy(candidate, portfolio, model):
    arch = candidate.get("meta", {}).get("architecture", {}) if isinstance(candidate, dict) else {}
    custom = arch.get("collision_policy")
    if isinstance(custom, dict) and custom:
        policy = custom
        source = "candidate.meta.architecture.collision_policy"
    else:
        portfolio_policy = (
            portfolio.get("studio", {})
            .get("relationship_policies", {})
            .get(model)
        )
        if isinstance(portfolio_policy, dict) and portfolio_policy:
            policy = portfolio_policy
            source = f"portfolio.studio.relationship_policies.{model}"
        else:
            policy = DEFAULT_POLICIES[model]
            source = f"built-in default for {model}"

    normalized = {}
    for dim in ("name", "morphology", "color", "creative_territory"):
        value = str(policy.get(dim, "custom"))
        normalized[dim] = value if value in VALID_INTENTS else "custom"
    return normalized, source


def compare(candidate_summary, sister_summary, policy):
    similarities = {
        "name": name_similarity(candidate_summary.get("name"), sister_summary.get("name")),
        "morphology": jaccard_similarity(
            candidate_summary.get("logo_morphology"),
            sister_summary.get("logo_morphology"),
        ),
        "color": color_similarity(
            candidate_summary.get("primary_color_oklch"),
            sister_summary.get("primary_color_oklch"),
        ),
        "creative_territory": jaccard_similarity(
            candidate_summary.get("creative_territory"),
            sister_summary.get("creative_territory"),
        ),
    }

    cand_name = _normalize_text(candidate_summary.get("name", {}).get("name"))
    sister_name = _normalize_text(sister_summary.get("name", {}).get("name"))
    exact_name = bool(cand_name and sister_name and cand_name == sister_name)

    signals = {}
    for dim, sim in similarities.items():
        signals[dim] = {
            "similarity": None if sim is None else round(sim, 3),
            "similarity_band": classify_similarity(sim),
            "policy": policy[dim],
            **policy_signal(dim, sim, policy[dim], exact_name=exact_name),
        }
    return signals


def main(portfolio_path, candidate_path):
    with open(portfolio_path, encoding="utf-8") as f:
        portfolio = json.load(f)
    with open(candidate_path, encoding="utf-8") as f:
        candidate = json.load(f)

    model = _architecture_model(candidate, portfolio)
    policy, policy_source = _policy(candidate, portfolio, model)
    cand_summary = _candidate_summary(candidate)

    comparisons = []
    high = medium = 0

    for sister in portfolio.get("brands", []):
        sister_summary = sister.get("portfolio_summary", sister)
        signals = compare(cand_summary, sister_summary, policy)
        high += sum(1 for s in signals.values() if s["severity"] == "HIGH")
        medium += sum(1 for s in signals.values() if s["severity"] == "MEDIUM")
        comparisons.append(
            {
                "brand": sister.get("brand_name")
                or sister_summary.get("name", {}).get("name")
                or "?",
                "signals": signals,
            }
        )

    if high:
        verdict = "REVIEW_COLLISIONS"
    elif medium:
        verdict = "PASS_WITH_SIGNALS"
    else:
        verdict = "NO_POLICY_COLLISION_DETECTED"

    output = {
        "candidate": cand_summary.get("name", {}).get("name", "?"),
        "architecture_model": model,
        "policy": policy,
        "policy_source": policy_source,
        "verdict": verdict,
        "comparisons": comparisons,
        "method_note": (
            "Per-dimension similarity uses transparent studio heuristics. No composite score is produced. "
            "Thresholds are governance policy, not empirical laws of brand distinctiveness. Missing data stays UNKNOWN."
        ),
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 1 if high else 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(0)
    sys.exit(main(sys.argv[1], sys.argv[2]))
