# Canonical brand state

Use `brand-spec.json` as the sparse private operating contract for future brand work. It records what is in force, not how it got there. Persist only information whose absence would materially increase future drift.

Canonical template: `templates/brand-spec.template.json`.

## Version fields

Keep schema compatibility separate from brand evolution:
- `meta.schema_version` — structural schema version. Current canonical schema is `5`.
- `meta.version` — this brand contract's semantic version, starting independently from the schema (for example `1.0.0`).

Increment `meta.version` when durable brand meaning/rules change. Do not change `meta.schema_version` for ordinary brand evolution.

Legacy specs (schema 4, v3 or earlier) remain operable and are interpreted using their historical shape until a meaningful migration occurs.

## Core contract

A schema-5 contract keeps only the always-useful decision core:
- `meta` — schema version, brand-contract version, brand identity, maturity and declared touchpoints;
- `strategy` — brand job, audience (with the language the brand speaks to it), offer truth, alternatives, position, right to win and desired meaning;
- `creative_direction` — thesis, principles and signature.

Add expression/domain blocks only when they are materially active: `verbal`, `visual`, `naming`, `architecture`, `portfolio_summary`, or other medium-specific rules future operators genuinely need.

Absence means "not material to this contract," not "forgot to complete the template."

## Instrument, not ledger

The contract has no lifecycle fields. No item carries a `status`, a date of change, a superseded predecessor or a record of a rejected alternative. Version control owns history; the delivery report owns pending matters. Top-level blocks such as `evidence`, `history`, `changelog`, `decisions`, `open_questions` or `unresolved` do not belong in the file.

Do not persist:
- rejected or superseded creative routes;
- prompts or internal reasoning transcripts;
- research notes or the list of sources consulted;
- routine trial applications after they have done their job;
- framework outputs that do not govern future work;
- empty placeholder sections;
- a field merely because another brand might need it.

## Provenance as `basis`

When a clause depends on a fact that a future operator might otherwise overturn for the wrong reason, attach `basis`: one sentence stating the fact, with its source only when the source is inspectable. Attach it to the clause, not to a separate table; no IDs, no references.

```json
"right_to_win": {
  "statement": "The only network that already operates in 27 states.",
  "basis": "Kitchen registry, 2025 census: 1,340 active units."
}
```

Prefer concise causal language over a rationale on every object. Most clauses need no `basis`.

## Strategy fields

### `brand_job`
The business/organizational transition the brand must help produce. This is not a mission statement.

### `audience`
`primary` — who the system primarily needs to serve. `language` — the language the brand speaks to them (BCP 47 tag, for example `pt-BR`); every reader-facing deliverable is written in it. Add a `not_for` boundary only when it materially improves future judgment.

### `offer_truth`
The relevant truth about the product, service or organization that expression must not contradict.

### `alternatives`
The meaningful alternatives/category context against which the brand must be understood. Keep only decision-changing alternatives.

### `position`
The intended place/meaning the brand should establish relative to those alternatives. Do not store a slogan here unless the slogan itself is the durable strategic decision.

### `right_to_win`
The credible basis that makes the position defensible.

### `desired_meaning`
What the designed system intends to make understandable/associable. Actual achieved perception remains an external claim.

## Creative direction fields

Keep the durable direction compact:
- `thesis` — governing expressive idea;
- `principles` — only behavioral rules that materially change choices;
- `signature` — characteristic behavior/cue that helps the system cohere.

Add `excludes` only when likely false routes/collisions need to be prevented in future work.

## Verbal and visual blocks

Use open objects rather than forcing every brand into the same inventory.

Examples of legitimate keys when needed:
- `verbal.principles`, `verbal.tone_by_moment`, `verbal.message_behavior`, `verbal.excludes`;
- `visual.identity_grammar`, `visual.typography`, `visual.palette`, `visual.logo`, `visual.imagery`, `visual.iconography`, `visual.composition`, `visual.motion`, `visual.tokens`, `visual.contrast_pairs`.

Name every element by its role in the system, never by its origin or appearance. A token or palette entry carries the role as its key and the reader-facing name, in the audience's language, in `name`; renaming is then one edit.

```json
"green": { "$type": "color", "$value": "#1F6E43", "name": "Verde Rede" }
```

When a visual decision governs future work, persist the durable behavior or relationship another operator needs, not merely the asset or value. Keep examples, channel recipes and one-off application choices out of canonical state.

## Naming

Add `naming` only when naming is part of the brand contract. Preserve the selected name, its strategic job when needed, material exclusions and dated clearance/linguistic triage. Triage does not become definitive legal clearance merely because it is persisted.

## Architecture / portfolio

Add architecture or portfolio state only for brands that actually participate in a multi-brand relationship. `portfolio_summary` is an optional compact projection for comparison workflows, not proof of market distinctiveness.

## Production state

For production assets such as a logo, use explicit status when needed:
- `final` — reproducible master exists and applicable production checks can be run;
- `concept` — direction exists but production remains unresolved;
- `external_craft_required` — specialist execution is needed and acceptance criteria/brief should be supplied.

This is the current state of an asset, not a history. Do not promote raster or generated concepts to `final` because they look polished.

## Machine-checkable structures

When declared:
- design tokens should use a consistent machine-consumable shape and resolvable aliases;
- contrast pairs should reference actual colors used for a real text/UI relationship;
- modular typography should provide enough numbers for its math to be checked;
- custom/fluid typography may use explicit rules without a modular ratio.

Machine validation establishes only those structural/technical properties.

## Publication

The contract is an operating file for the people and agents who run the brand. Keep it outside any directory the host serves publicly; the public package is the brand book and its assets. Publish the contract alongside them only when the owner decides the strategy it contains is public.

## Migration

On the next meaningful CREATE/EVOLVE operation, migrate by **compressing** valid state into schema 5:
- set `meta.schema_version` to `5`;
- add `strategy.audience.language`;
- fold each `evidence` record that a clause still depends on into that clause's `basis`; discard the rest, including `status`, `evidence_refs` and any other lifecycle field;
- give tokens a reader-facing `name` where the book will display them;
- preserve valid strategy, equity and production rules;
- remove exploration history and ceremonial fields;
- do not redesign merely to migrate schema.

APPLY/AUDIT may operate a legacy spec without forcing migration when the existing state is sufficient for the requested artifact.
