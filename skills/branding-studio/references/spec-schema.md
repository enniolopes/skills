# Brand spec and portfolio registry schema

Canonical templates:
- `templates/brand-spec.template.json`
- `templates/portfolio.template.json`

The spec is a **semantic contract and source of truth**, not proof that the brand is strategically or aesthetically good.

## Validation classes

### Structural / deterministic
`validate_structure.py` can verify:
- required fields exist;
- decision blocks contain non-empty rationales/negatives;
- evidence records have provenance/status;
- DTCG token leaves are structurally valid;
- declared token references resolve;
- declared contrast pairs meet configured WCAG criteria;
- modular scales are mathematically consistent **when the type-system mode is modular**;
- logo production status/brief fields are coherent;
- full-tier naming triage is not unresolved collision/not-searched;
- trial applications exist where required.

### Semantic
The model must review:
- rationale quality;
- strategy coherence;
- evidence-to-claim fit;
- creative specificity;
- identity grammar;
- application performance;
- whether exclusions are useful rather than arbitrary.

Never infer semantic validity from `exit 0`.

## Required conceptual blocks

| Block | Purpose |
|---|---|
| `meta` | identity, version, tier, touchpoints, architecture, changelog |
| `research` | evidence/provenance and unresolved validation needs |
| `strategy` | audience, alternatives, right-to-win, differentiation, context, theme |
| `creative_direction` | central idea, tensions, principles, references, exploration |
| `naming` | selected name and clearance triage |
| `verbal` | voice, tone/moments, negatives |
| `visual` | identity grammar and production rules |
| `trial_applications` | stress tests before freezing a full system |
| `portfolio_summary` | small comparable projection for portfolio collision checks |

## Rationales

Important decisions should contain `$rationale`.

Structural validation checks only that rationale text exists and is not placeholder-like. Semantic review determines whether the reasoning is actually causal, evidence-backed and non-circular.

## Negative specification

Minimum negatives:
- `strategy.customer.who_it_is_NOT`;
- `naming.$excludes` when naming is in scope;
- `creative_direction.$excludes`;
- `verbal.not_like_this`;
- `visual.$excludes`.

Negatives should reduce ambiguity, not merely add adjectives.

## Research evidence

Each material finding:

```json
{
  "claim": "...",
  "kind": "fact | observation | hypothesis",
  "source": "...",
  "confidence": "high | medium | low",
  "validation": "verified | needs_field_research"
}
```

`source` may be a URL, internal document, founder statement, interview or dataset. A hypothesis may intentionally remain unverified, but downstream decisions must not overstate it.

## Typography

`visual.typography.hierarchy.mode`:
- `modular` → provide `base_px`, `ratio`, `steps`; validator checks math.
- `custom` → provide explicit role relationships; no mathematical scale is required.
- `fluid` → provide min/max/behavior and touchpoint rules; no modular-scale requirement.

Family count is not fixed.

## Spacing / grids

No universal 4/8pt requirement.

If a touchpoint/system needs spacing tokens or a grid, encode the relevant rules and tokens. Their existence is conditional.

## Logo / signature production

`visual.logo.production.status`:
- `final`;
- `concept`;
- `external_craft_required`.

A concept can be strategically approved without pretending a production master exists.

When `final` and SVG is the declared master, run `asset_checks.py`.

## Trial applications

For `full` tier:
- at least one real trial application is required;
- more are expected when touchpoints stress materially different conditions.

A trial records:
- touchpoint;
- job;
- artifact/reference;
- failures found;
- system changes caused by the test;
- status.

## Portfolio registry

The registry stores:
- studio architecture defaults;
- relationship policy by architecture model;
- shared/inherited cues;
- each brand's compact `portfolio_summary`.

`portfolio_collision.py` reports raw similarity/collision signals. Missing evidence is `UNKNOWN`.

Do not interpret sister-brand similarity without the declared architecture:
- house of brands usually wants separation;
- endorsed systems may share parent cues;
- branded house may intentionally share many cues;
- hybrid requires explicit policy.

## File lifecycle

Each operation reads the current spec/registry from persistent files.

CREATE/EVOLVE return updated canonical files.
APPLY/AUDIT should not mutate the spec unless a real system-level change is explicitly accepted.
