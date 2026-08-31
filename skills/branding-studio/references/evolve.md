# EVOLVE mode — versioning the spec when it stops serving

Evolution, never regeneration. Most systems in use largely work; the job is to build on what passes and replace only what fails (Malinic). A full rebrand is the exception, not the default.

## Admission gate (Fielding) — before anything else

Ask what changed. Legitimate reasons: **the customer, the competition, the context or the offering** changed — or execution demonstrably fails to deliver (with evidence, not impressions). Illegitimate reasons: the owner is bored, a new manager arrived, a wish to "modernize" without cause. If the reason is illegitimate, **refuse citing the rule** and explain the cost: identity builds memory through repetition; changing without cause destroys the asset being built (new assets start at fame ~0 — every rebrand resets part of the clock).

## Flow

1. **Audit the current system** (AUDIT mode applied to the identity itself): what still derives correctly from strategy? What did the declared change invalidate?
2. **Minimum scope**: list only the elements whose derivation broke. Everything whose `$rationale` remains valid is **preserved by obligation** — touching what works requires its own justification.
3. **Regenerate only the scope**, following create.md for the affected elements (including a fresh portfolio consultation if color/morphology/name change).
4. **Versioned diff**: semantic bump in `meta.version` (major = theme/positioning changed; minor = a system element changed; patch = fix/refinement). Changelog entry with trigger and changes. Deliver the explicit diff (before → after, per element, with the new rationale).
5. **Revalidate**: `validate_spec.py` + `portfolio_distance.py`. Update `portfolio_summary` in the registry. If promoting a provisional brand to full, this is the mode: fill the pending blocks, complete clearance, construct the mark.
6. **Migration plan**: list affected touchpoints (site, decks, stationery, product) for the user to prioritize, and re-compile the deliverable formats from `meta.touchpoints`. Beware destructive simplification: removing recognized distinctive elements "to modernize" erases memory structures — a recognized asset is equity, not fat.
