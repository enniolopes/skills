# Canonical brand state

Use `brand-spec.json` as the sparse durable operating contract for future brand work. Persist only information whose absence would materially increase future drift.

Canonical template: `templates/brand-spec.template.json`.

## Core contract

A v4 contract keeps a small always-useful core:
- `meta` — brand identity, spec version, maturity and declared touchpoints;
- `strategy` — brand job, audience, offer truth, alternatives, position, right to win and desired meaning;
- `creative_direction` — thesis, principles, signature and meaningful exclusions;
- `verbal` — only active verbal rules;
- `visual` — only active visual/production rules;
- `evidence` — only consequential evidence references that future judgment still needs.

Add optional blocks such as `naming`, `architecture`, `portfolio_summary`, `motion` or machine tokens only when the brand actually uses them.

Absence means “not material to this contract,” not “forgot to complete the template.”

## Sparse-state rule

Do not persist:
- rejected or superseded creative routes;
- prompts or internal reasoning transcripts;
- generic desk-research notes;
- routine trial applications after they have done their job;
- every source consulted;
- framework outputs that do not govern future work;
- empty placeholder sections;
- a field merely because another brand might need it.

Persist a rationale only when future operators would otherwise be likely to change a consequential decision for the wrong reason. Prefer concise causal language over a rationale field attached to every object.

## Strategy fields

### `brand_job`
The business/organizational transition the brand must help produce. This is not a mission statement.

### `audience`
Who the system primarily needs to serve and, when materially useful, who it is not for.

### `offer_truth`
The relevant truth about the product, service or organization that expression must not contradict.

### `alternatives`
The meaningful alternatives/category context against which the brand must be understood. Keep only decision-changing alternatives.

### `position`
The intended place/meaning the brand should establish relative to those alternatives. Do not store a slogan here unless the slogan itself is the durable strategic decision.

### `right_to_win`
The credible basis that makes the position defensible. Reference evidence when future work needs provenance.

### `desired_meaning`
What the audience should be able to understand or associate from the designed system. Treat actual achieved perception as external evidence, not as a property the spec can declare true.

## Creative direction fields

Keep the durable direction compact:
- `thesis` — governing expressive idea;
- `principles` — only behavioral rules that materially change choices;
- `signature` — characteristic behavior/cue that helps the system cohere;
- `excludes` — false routes/collisions that future work is likely to fall into.

Do not persist an exploration history. A future operator needs the selected grammar, not all discarded candidates.

## Evidence

Use `evidence` only for consequential factual/observational/hypothesis records that remain relevant to future decisions.

Recommended shape:

```json
{
  "id": "E-001",
  "claim": "...",
  "kind": "fact | observation | hypothesis",
  "source": "...",
  "status": "active | challenged | superseded"
}
```

Rules:
- keep IDs stable and unique;
- preserve uncertainty in downstream claims;
- challenge or supersede evidence before changing dependent contract decisions;
- do not use confidence labels when they do not change action;
- do not store ordinary research simply to prove that research happened.

## Verbal and visual blocks

Use open objects rather than forcing every brand into the same inventory.

Examples of legitimate keys when needed:
- `verbal.principles`, `verbal.tone_by_moment`, `verbal.message_behavior`, `verbal.excludes`;
- `visual.identity_grammar`, `visual.typography`, `visual.palette`, `visual.logo`, `visual.imagery`, `visual.iconography`, `visual.composition`, `visual.motion`, `visual.tokens`, `visual.contrast_pairs`.

Exact structures may be domain-specific. Prefer the smallest shape that another competent operator can apply correctly.

## Naming

Add `naming` only when naming is part of the brand contract. Preserve the selected name, its strategic job when needed, material exclusions and dated clearance/linguistic triage. Triage does not become definitive legal clearance merely because it is persisted.

## Architecture / portfolio

Add architecture or portfolio state only for brands that actually participate in a multi-brand relationship. Architecture policy can intentionally require shared cues; similarity is not universally a defect.

`portfolio_summary` is an optional compact projection for comparison workflows. It is not proof of market distinctiveness.

## Production state

For production assets such as a logo, use explicit status when needed:
- `final` — reproducible master exists and applicable production checks can be run;
- `concept` — direction exists but production remains unresolved;
- `external_craft_required` — specialist execution is needed and acceptance criteria/brief should be supplied.

Do not promote raster or generated concepts to `final` because they look polished.

## Machine-checkable structures

When declared:
- design tokens should use a consistent machine-consumable shape and resolvable aliases;
- contrast pairs should reference actual colors used for a real text/UI relationship;
- modular typography should provide enough numbers for its math to be checked;
- custom/fluid typography may use explicit rules without a modular ratio.

Machine validation establishes only those structural/technical properties.

## Versioning and migration

Increment the spec version when durable contract meaning changes. The project/version-control environment should carry detailed history; do not duplicate a long changelog inside the contract.

Legacy v3 specs remain operable. On the next meaningful CREATE/EVOLVE operation, migrate by **compressing** valid state into the v4 contract:
- preserve valid strategy, equity and production rules;
- carry forward only evidence still needed for judgment;
- remove exploration history and ceremonial fields;
- omit inactive framework/media blocks;
- do not redesign merely to migrate schema.

APPLY/AUDIT may operate a legacy spec without forcing migration when the existing state is sufficient for the requested artifact.
