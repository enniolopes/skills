# EVOLVE — change only what evidence invalidates

Use EVOLVE when a committed rationale or system may no longer serve. Preserve valid equity and change the smallest justified surface.

## 1. Establish whether change is warranted

Start from current state and committed rationales, not aesthetic preference.

Classify each genuinely new signal before anything else:
- no material effect;
- supports an existing belief;
- challenges a belief (mark the finding `challenged`);
- invalidates a rationale or reveals a recurring system failure.

Only the last class normally warrants EVOLVE; the second and third update beliefs in `research.findings`, not the contract. Self-critique, regeneration or polishing without new evidence is none of these.

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
- vague “make it modern” requests;
- replacing recognized assets because a new team prefers something else;
- one local metric moving without broader evidence.

For every affected element trace:
- committed rationale;
- supporting evidence/belief;
- current evidence state;
- genuinely new signal;
- consequence of preserving it;
- equity/dependencies lost by changing it.

If no new evidence or strategic truth exists, route the work to refinement/AUDIT/APPLY rather than claiming broad evolution.

## 2. Minimize the change surface

Classify each relevant element:
- preserve;
- refine;
- replace;
- retire;
- add.

Re-open only the necessary dependency chain:
- strategy changed → revisit creative direction and affected downstream identity;
- new touchpoint only → test APPLY first;
- naming/legal problem → reopen naming without gratuitous visual redesign;
- typography production failure → reopen typography, not the whole brand;
- repeated execution ambiguity → patch guidance before redesigning identity.

Do not preserve a broken decision merely because it exists; do not destroy a valid one merely because change is attractive.

## 3. Prove the delta

Apply the verification ladder from `SKILL.md` proportionally to equity and consequence.

At minimum:
- run V1 checks on changed spec/assets;
- at V2, show that the old rationale is invalidated/insufficient, the new decision follows from current evidence, unchanged elements remain coherent, and the delta does not create gratuitous category/portfolio collision;
- at V3, re-run representative applications for materially affected touchpoints; compare old vs new when that reveals whether the actual problem is solved;
- require stronger V4 evidence as radius rises, especially for established renaming, positioning/architecture changes, retirement of distinctive assets and claims about perception/behavior.

A HIGH-COST change with weak V4 evidence remains a recommendation/experiment, not an automatic contract mutation.

## 4. Commit a versioned minimum delta

Before commit, ensure evidence, legitimate authority and migration/rollback understanding are sufficient for the radius.

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

Run applicable deterministic tools:

```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
```

Use `asset_checks.py` for changed SVG masters and complete appropriate V2/V3 verification.

After deployment, update beliefs first as new evidence arrives. Contract should change again only when evidence materially invalidates a committed rationale. Do not tune a long-lived brand system to every short-term metric.

## Provisional → full

Treat promotion as EVOLVE:
- resolve important evidence gaps;
- complete naming/legal triage;
- deepen only verbal/visual dimensions required by durable touchpoints;
- resolve production masters;
- complete representative trials;
- update portfolio registry.

Promotion strengthens valid reasoning; it does not imply redesign.

## Delivery

Deliver:
- updated spec;
- explicit versioned diff;
- evidence/authority basis;
- changed masters/briefs;
- updated representative applications;
- migration plan;
- portfolio update where applicable;
- verification results and unresolved V4/legal/craft pendencies.
