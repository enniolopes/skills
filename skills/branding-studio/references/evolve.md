# EVOLVE mode — change the brand system without discarding accumulated equity

Evolution is a controlled change to the source of truth. Regeneration is not the default.

## Admission gate

Establish what changed and what evidence supports change.

Legitimate triggers include:
- customer/audience changed;
- competitive context changed;
- offering/category changed;
- organizational strategy changed;
- an important new touchpoint cannot be served by the current system;
- field evidence shows the identity is failing materially;
- production/accessibility/legal constraints changed.

Weak triggers include:
- stakeholder boredom;
- trend chasing;
- "make it modern" without a business/communication problem;
- replacing a recognized asset only because a new team prefers something else.

A weak trigger does not automatically forbid all change, but it is insufficient to justify destroying equity. Challenge it and request the real problem.

## Flow

### 1. Diagnose
Audit the current system and evidence.

For each relevant element:
- current rationale;
- whether the premise is still true;
- what changed;
- evidence;
- impact if preserved;
- impact if changed.

### 2. Minimize scope
Preserve elements whose rationale still holds unless a new system-level reason overrides it.

Classify:
- preserve;
- refine;
- replace;
- retire;
- add.

### 3. Re-open only necessary phases
Examples:
- strategy changed → revisit creative direction and downstream identity;
- new touchpoint only → first test whether APPLY can solve it;
- naming/legal issue → rerun naming without gratuitously changing visual identity;
- typography production failure → revisit type system, not the whole brand.

### 4. Re-explore where the premise changed
For affected creative dimensions, use CREATE's creative-direction / identity-craft process.

Do not preserve a broken decision merely because it exists; do not destroy a valid decision merely because change is exciting.

### 5. Version
Update `meta.version`:
- major — positioning/theme/architecture changes that materially redefine the system;
- minor — identity/verbal system change with strategy mostly intact;
- patch — correction/refinement with no meaningful semantic change.

Record:
- trigger;
- evidence;
- before;
- after;
- new rationale;
- affected touchpoints.

### 6. Trial and migrate
Re-run representative trial applications for affected touchpoints.

Create a migration plan:
- immediate;
- next production cycle;
- legacy allowed;
- deprecated date where relevant.

### 7. Revalidate
Run:
```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
```

Run `asset_checks.py` on changed SVG masters.

Then perform semantic review of the changed derivation.

## Provisional → full

Promotion is an EVOLVE operation:
- fill evidence/strategy gaps;
- complete naming/legal triage;
- deepen verbal/visual system;
- resolve production masters;
- complete trial applications;
- update portfolio registry.

Promotion should strengthen the existing reasoning when it is still valid, not automatically redesign the brand.

## Delivery

Deliver:
- updated spec;
- explicit versioned diff;
- changed masters/briefs;
- updated trial applications;
- migration plan;
- updated portfolio registry;
- validation outputs;
- unresolved evidence/legal/craft pendencies.
