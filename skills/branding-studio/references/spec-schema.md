# Brand spec and portfolio registry schema

Canonical templates live in `templates/brand-spec.template.json` and `templates/portfolio.template.json`. Copy the template; never invent your own structure — the validator (`scripts/validate_spec.py`) depends on these exact paths.

## Structural invariants (the validator fails without them)

1. **`$rationale` mandatory** in: strategy.customer, right_to_win, differentiation, context, naming, visual.palette, visual.typography, visual.logo. Real content, not circular rhetoric — it must point to the lever/brief that generated the decision.
2. **Negative specification mandatory**: `strategy.customer.who_it_is_NOT`, `naming.$excludes`, `visual.$excludes`, `visual.logo.$excludes`, `verbal.not_like_this` (≥1 counter-example).
3. **`strategy.theme.because_test`** filled ("[theme] BECAUSE [right to win]" closing logically) and `onliness` containing "only".
4. **DTCG tokens**: every leaf has `$value` and `$type`; aliases as `{color.primitive.x}`; three layers (primitive → semantic → component where applicable).
5. **`visual.contrast_pairs`**: ≥1 pair with `usage` ∈ {body, large, ui}; references resolve to hex; all pass WCAG AA.
6. **`visual.typography.scale`**: base_px + ratio + steps consistent (step ≈ base·ratio^n, 1.5% tolerance).
7. **`visual.logo.clear_space`** proportional (defined in terms of the logo itself), never absolute px.
8. **`verbal.voice_chart`**: each principle covers the 6 dimensions (concepts, vocabulary, verbosity, grammar, punctuation, capitalization).
9. **`meta.touchpoints`** declared — drives which deliverable formats are compiled.
10. **`meta.tier`**: "provisional" tolerates a pending voice chart and pending clearance (as warnings); "full" requires triaged clearance (inpi_status ≠ not_searched).

## Blocks and purpose

| Block | Purpose | Feeds |
|---|---|---|
| `meta` | document identity, tier, touchpoints, portfolio architecture, changelog | EVOLVE (versioning), deliverable compilation |
| `strategy` | four levers + theme + manifesto + CEPs | derivation of everything |
| `naming` | decision + taxonomy + clearance with status | portfolio_distance, legal pendencies |
| `verbal` | voice chart + negatives + moments | copy audits |
| `visual` | DTCG tokens + palette + typography + constructed logo | deterministic checks |
| `discarded_routes` | justification of the single route (Malinic) | defense of the decision |
| `portfolio_summary` | comparable projection of the brand | portfolio_distance.py |

## Portfolio registry

One file per studio. When a brand is approved: copy the spec's `portfolio_summary` into `brands[]`, point `spec_path`, set `tier`, update `occupied_territories`. Morphology tags use a controlled vocabulary (so Jaccard works): `geometric, organic, monogram, letterform, wordmark, abstract-symbol, circular-grid, square-grid, angular, curved, negative-space, modular`.

## File lifecycle

The environment resets between conversations: the spec and the registry live in the user's files (git repository or project knowledge in Claude.ai). Every mode starts by requesting/reading those files and ends by delivering updated versions as presented files. Never assume a previous version is "in memory".
