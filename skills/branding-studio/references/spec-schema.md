# Brand spec and portfolio registry schema — v3 semantics

Canonical templates:
- `templates/brand-spec.template.json`
- `templates/portfolio.template.json`

The spec is a **semantic contract and persistent brand state**. It is not a transcript of the agent's reasoning and not proof that the brand is strategically or aesthetically good.

## State model

The single `brand-spec.json` contains three semantic kinds of persistent state.

### 1. Contract

Committed decisions that govern future work:
- `strategy`;
- `creative_direction` preferred/committed direction;
- `naming`;
- `verbal`;
- `visual`;
- architecture/touchpoint constraints.

Contract changes require COMMIT discipline and versioning.

### 2. Beliefs / evidence

`research.findings` stores evidence and hypotheses that support or challenge decisions.

V3 finding shape:

```json
{
  "id": "E-001",
  "claim": "...",
  "kind": "fact | observation | hypothesis",
  "source": "...",
  "confidence": "high | medium | low",
  "validation": "verified | needs_field_research",
  "state": "active | challenged | superseded"
}
```

Rules:
- `id` is stable and unique inside the spec so rationales/changelog entries can refer to evidence without copying it;
- `active` means still usable as evidence;
- `challenged` means credible new signal creates material doubt;
- `superseded` means newer evidence has replaced it for current decisions;
- challenged/superseded findings remain history; do not silently delete consequential evidence;
- a hypothesis may remain active while awaiting V4 proof, but downstream claims must preserve that uncertainty.

Existing pre-v3 specs may lack `id`/`state`; migrate them when they next undergo meaningful CREATE/EVOLVE work. Do not force a redesign merely to update schema metadata.

### 3. History

`meta.changelog` is the compact decision history. Store only events useful for future judgment:
- creation/promotion;
- system-level patches;
- EVOLVE commitments;
- meaningful evidence shifts;
- migrations of important equity.

Do not persist prompts, every explored route, every generated candidate or routine application.

## Validation ladder

### V1 Structural / deterministic

`validate_structure.py` can verify only machine-checkable properties such as:
- required structure / non-placeholder decision fields;
- evidence record shape/provenance and v3 evidence IDs/states;
- negative specifications;
- DTCG token structure/reference resolution;
- declared contrast pairs;
- modular scale math **only when mode=modular**;
- logo production-state coherence;
- naming-triage state;
- trial-application presence.

### V2 Semantic

The model reviews:
- rationale quality;
- strategy coherence;
- evidence-to-claim fit;
- creative specificity;
- identity grammar;
- application performance;
- usefulness of exclusions.

### V3 Contextual

Representative applications/renders prove whether the system works in the environments that matter.

### V4 Reality

External evidence covers real perception, behavior, recognition, stakeholder truth/authority and specialist/legal conclusions.

Never infer V2/V3/V4 validity from `exit 0`.

## Required conceptual blocks

| Block | Purpose |
|---|---|
| `meta` | identity, version, tier, touchpoints, architecture, compact changelog |
| `research` | beliefs/evidence, provenance and unresolved reality needs |
| `strategy` | audience, alternatives, right-to-win, differentiation, context, theme |
| `creative_direction` | central idea, tensions, principles, references, meaningful exploration |
| `naming` | selected name and clearance triage |
| `verbal` | voice, tone/moments, negatives |
| `visual` | identity grammar and production rules |
| `trial_applications` | contextual proof before freezing consequential system decisions |
| `portfolio_summary` | compact projection for architecture-aware collision checks |

## Rationales and evidence references

Important decisions contain `$rationale`.

Where specific findings materially support a decision, use existing `evidence_refs` fields or mention stable evidence IDs in the rationale/changelog rather than duplicating claims.

Structural validation checks rationale presence, not causal quality. V2 review determines whether reasoning is genuinely supported and non-circular.

## Negative specification

Minimum negatives:
- `strategy.customer.who_it_is_NOT`;
- `naming.$excludes` when naming is in scope;
- `creative_direction.$excludes`;
- `verbal.not_like_this`;
- `visual.$excludes`.

Negatives must reduce ambiguity, not merely add adjectives.

## Typography and spacing

`visual.typography.hierarchy.mode`:
- `modular` → provide `base_px`, `ratio`, `steps`; validator checks math;
- `custom` → explicit role relationships; no mathematical scale required;
- `fluid` → explicit rules/min/max behavior; no modular-scale requirement.

Family count is contextual.

There is no universal 4/8pt spacing requirement. Encode grids/spacing only where the touchpoints need them.

## Logo / signature production

`visual.logo.production.status`:
- `final` — reproducible master exists and applicable production checks can pass;
- `concept` — strategic/creative concept exists, production remains;
- `external_craft_required` — specialist execution is needed and a production brief is required.

A raster concept must not be promoted to `final` merely because it looks finished.

## Trial applications

For `full` tier:
- at least one tested representative application is required;
- more are expected when declared touchpoints stress the grammar differently.

A trial records:
- touchpoint;
- job;
- artifact/reference;
- failures found;
- system changes caused by the test;
- status.

Trials are V3 contextual evidence, not V4 market evidence.

## Portfolio registry

The registry stores:
- architecture defaults;
- relationship policy by architecture model;
- shared/inherited cues;
- each brand's compact `portfolio_summary`.

`portfolio_collision.py` reports collision/similarity signals. Missing evidence is `UNKNOWN`.

Similarity is interpreted by architecture:
- house of brands usually seeks separation;
- endorsed systems may share parent cues;
- branded house may intentionally share many cues;
- hybrid requires explicit policy.

## File lifecycle

Each mission reads the current persistent state first.

- CREATE/EVOLVE may commit updated canonical files;
- APPLY/AUDIT do not mutate the contract for a one-off artifact problem;
- recurring/system-level failures may create a patch/EVOLVE candidate;
- evidence can move `active → challenged → superseded` without automatically changing the contract;
- every contract change must be versioned and explained in `meta.changelog`.
