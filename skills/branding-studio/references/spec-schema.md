# Brand spec and portfolio state

Canonical templates:
- `templates/brand-spec.template.json`
- `templates/portfolio.template.json`

Use `brand-spec.json` as the semantic contract and persistent brand state. Do not store internal reasoning transcripts, and do not treat structural validity as proof of strategic/creative quality.

## State model

### Contract

Committed decisions that govern future work:
- `strategy`;
- committed `creative_direction`;
- `naming`;
- `verbal`;
- `visual`;
- architecture/touchpoint constraints.

Version every material contract change.

### Beliefs / evidence

Store evidence and hypotheses in `research.findings`:

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
- keep `id` stable and unique so rationales/changelog can reference evidence without copying it;
- `active` = still usable as evidence;
- `challenged` = credible new signal creates material doubt;
- `superseded` = newer evidence replaces it for current decisions;
- keep challenged/superseded findings when they explain consequential history;
- an active hypothesis can await V4 proof, but downstream claims must preserve that uncertainty.

Pre-v3 specs may lack `id`/`state`; migrate them during the next meaningful CREATE/EVOLVE operation. Do not redesign merely to migrate schema metadata.

### History

Use `meta.changelog` only for events that improve future judgment:
- creation/promotion;
- system-level patches;
- EVOLVE commitments;
- meaningful evidence shifts;
- migrations of important equity.

Do not persist prompts, every explored route/candidate or routine applications.

## Conceptual blocks

| Block | Purpose |
|---|---|
| `meta` | identity, version, tier, touchpoints, architecture, compact changelog |
| `research` | evidence/hypotheses, provenance and unresolved reality needs |
| `strategy` | audience, alternatives, right-to-win, differentiation, context, theme |
| `creative_direction` | central idea, tensions, principles, references, exploration |
| `naming` | selected name and clearance triage |
| `verbal` | voice, tone/moments, negatives |
| `visual` | identity grammar and production rules |
| `trial_applications` | V3 contextual proof for consequential system decisions |
| `portfolio_summary` | compact projection for architecture-aware collision checks |

## Structural validation scope

`scripts/validate_structure.py` can establish V1 properties only, including:
- required structure and non-placeholder decision fields;
- evidence shape/provenance and v3 evidence IDs/states;
- negative specifications;
- DTCG token structure/reference resolution;
- declared contrast pairs;
- modular-scale math only when `mode=modular`;
- logo production-state coherence;
- naming-triage state;
- required trial-application presence.

A passing structural validator does not establish V2 semantic quality, V3 contextual performance or V4 reality.

## Rationales and evidence references

Use `$rationale` on important decisions.

When specific findings materially support a decision, use existing `evidence_refs` or stable evidence IDs in rationale/changelog rather than duplicating claims.

V1 checks rationale presence. V2 determines whether the reasoning is causal, supported and non-circular.

## Negative specification

Minimum negatives:
- `strategy.customer.who_it_is_NOT`;
- `naming.$excludes` when naming is in scope;
- `creative_direction.$excludes`;
- `verbal.not_like_this`;
- `visual.$excludes`.

Use negatives that reduce future ambiguity, not decorative adjectives.

## Typography and spacing

`visual.typography.hierarchy.mode`:
- `modular` → provide `base_px`, `ratio`, `steps`; validate the math;
- `custom` → provide explicit role relationships; no mathematical scale required;
- `fluid` → provide explicit rules/min/max behavior; no modular scale required.

Family count is contextual. Do not impose a universal 4/8pt spacing system; encode spacing/grid rules only when touchpoints need them.

## Logo / signature production

`visual.logo.production.status`:
- `final` — reproducible master exists and applicable production checks can pass;
- `concept` — strategic/creative concept exists but production remains;
- `external_craft_required` — specialist execution is needed and a production brief is required.

Do not promote raster concepts to `final` merely because they look finished.

## Trial applications

For `full` tier, require at least one tested representative application; add more when declared touchpoints stress the grammar differently.

Record:
- touchpoint;
- job;
- artifact/reference;
- failures found;
- system changes caused by the trial;
- status.

Trials are V3 evidence, not V4 market evidence.

## Portfolio registry

Store:
- architecture defaults;
- relationship policy by architecture model;
- shared/inherited cues;
- each brand's compact `portfolio_summary`.

Use `scripts/portfolio_collision.py` for similarity/collision signals and preserve missing evidence as `UNKNOWN`.

Interpret similarity by architecture:
- house of brands usually seeks separation;
- endorsed systems may share parent cues;
- branded house may intentionally share many cues;
- hybrid requires explicit policy.

## Lifecycle

Read current persistent state before acting.

- CREATE/EVOLVE may commit canonical state changes;
- APPLY/AUDIT do not mutate contract for one-off artifact problems;
- recurring/system-level failures may create a patch/EVOLVE candidate;
- evidence may move `active → challenged → superseded` without automatically changing contract;
- every contract change must be versioned and explained in `meta.changelog`.
