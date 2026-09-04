# EVOLVE intent — change the contract only when its rationale no longer serves

EVOLVE changes the brand system without discarding accumulated equity. It uses the global **SEARCH → PROVE → COMMIT → ADAPT** loop with a deliberately high bar for MARKET/HIGH-COST commitments.

Evolution is controlled change to the source of truth. Regeneration is not the default.

## SEARCH — establish whether change is actually needed

Start from the current spec, not from aesthetic preference.

Legitimate triggers include:
- customer/audience changed;
- competitive/category context changed materially;
- offering or organizational strategy changed;
- an important new touchpoint cannot be served by the current grammar;
- V4 evidence shows a material perception/behavior problem;
- recurring application failures reveal a system gap;
- production/accessibility/legal constraints changed.

Weak triggers include:
- stakeholder boredom;
- trend chasing;
- vague "make it modern" requests;
- replacing recognized assets because a new team prefers something else;
- a single local metric moving without broader evidence.

For every affected element ask:
- What was the committed rationale?
- Which evidence/belief supported it?
- Is that premise still active, challenged or superseded?
- What new signal exists?
- What happens if we preserve it?
- What equity/dependencies are lost if we change it?

If no genuinely new evidence or strategic truth exists, treat the work as refinement/AUDIT/APPLY rather than claiming learning or broad evolution.

## Minimize the change surface

Classify each relevant element:
- preserve;
- refine;
- replace;
- retire;
- add.

Re-open only the necessary dependency chain:
- strategy changed → revisit creative direction and downstream identity;
- new touchpoint only → first test APPLY;
- naming/legal problem → reopen naming without gratuitous visual redesign;
- typography production failure → reopen the type system, not the whole brand;
- repeated execution ambiguity → patch guidance before redesigning identity.

Do not preserve a broken decision merely because it exists; do not destroy a valid decision merely because change is exciting.

## PROVE — scale rigor with equity and consequence

### V1 Structural
Validate the changed spec/assets with applicable deterministic tools.

### V2 Semantic
Prove that:
- the old rationale is actually invalidated or insufficient;
- the new decision is causally derived from current evidence;
- unchanged elements remain coherent;
- the change does not create gratuitous category/portfolio collision.

### V3 Contextual
Re-run representative applications for every materially affected touchpoint. Compare old vs new when doing so reveals whether the change solves the actual problem.

### V4 Reality
Require stronger external evidence as commitment radius rises, especially for:
- established renaming;
- positioning changes;
- architecture changes;
- retirement of distinctive assets with possible equity;
- claims about perception, recognition or customer behavior.

A high-cost change with weak V4 evidence should remain a recommendation/experiment, not an automatic contract mutation.

## COMMIT — minimum justified delta

Before commit:
1. evidence is sufficient for the radius;
2. the legitimate authority owner has approved MARKET/HIGH-COST changes;
3. migration/rollback consequences are understood.

Version `meta.version`:
- **major** — positioning/theme/architecture changes that materially redefine the system;
- **minor** — identity/verbal system change with strategy mostly intact;
- **patch** — correction/refinement with no meaningful semantic change.

Record in `meta.changelog`:
- trigger;
- evidence refs/new signal;
- before/after summary;
- affected touchpoints;
- migration consequence.

Run:

```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
```

Run `asset_checks.py` on changed SVG masters and perform V2/V3 checks appropriate to the change.

## ADAPT — learn without destabilizing the brand

After deployment, new signals should first update beliefs/evidence state:

`active → challenged → superseded`

Only when evidence materially invalidates a committed rationale should the contract change again.

Do not optimize a long-lived brand system for every short-term metric. Stability is a feature when the rationale still holds.

## Provisional → full

Promotion is an EVOLVE operation:
- resolve important evidence gaps;
- complete naming/legal triage;
- deepen only the verbal/visual dimensions needed by durable touchpoints;
- resolve production masters;
- complete representative trials;
- update portfolio registry.

Promotion strengthens valid reasoning; it does not automatically redesign the brand.

## Delivery

Deliver:
- updated spec;
- explicit versioned diff;
- evidence/authority basis for the change;
- changed masters/briefs;
- updated representative applications;
- migration plan;
- updated portfolio registry where applicable;
- V1/V2/V3 results and unresolved V4/legal/craft pendencies.
