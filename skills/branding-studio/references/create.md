# CREATE intent — establish a brand system

CREATE is the intent for a new brand or an existing identity that has no canonical spec. It runs the global **SEARCH → PROVE → COMMIT → ADAPT** control plane from `SKILL.md`.

The goal is not to complete a human agency checklist. The goal is to reach the smallest defensible brand commitment that can govern the venture's real touchpoints.

## Investment tier

### PROVISIONAL
Use when the thesis, market or offering may still pivot.

Minimum committed state:
- customer / not-customer;
- competitive alternatives;
- right to win;
- differentiation/theme;
- preliminary naming triage when naming is in scope;
- concise verbal principles + negatives;
- creative direction;
- identity grammar sufficient for declared MVP touchpoints;
- at least one representative trial application;
- explicit V4/legal/craft pendencies.

A provisional identity must be promotable without discarding valid reasoning.

### FULL
Use for durable ventures, existing organizations, or when a production-grade system is justified.

Requires deeper evidence, production decisions, representative trials across materially different stresses, semantic review, current legal/market triage where relevant, and operational guidance for the declared touchpoints.

Do not force FULL merely because the model can generate more work.

## SEARCH

### 1. Inspect before interrupting

Use available context and tools to recover:
- what the organization/product does;
- existing name/assets/equity;
- category and direct/indirect alternatives;
- public audience/category evidence;
- current market/geographic/language context;
- portfolio/parent relationship;
- existing touchpoints and production constraints.

Do not ask the user to repeat facts already available in files, sites, repositories or other inspectable sources.

### 2. Use human input only where it has unique value

Invoke the global gates when needed:
- **Truth** — unpublished strategy, future direction, internal capability, ownership, constraints;
- **Authority** — strategic commitments such as positioning, architecture or high-cost naming;
- **Reality** — audience/stakeholder evidence that does not exist in inspectable sources.

Examples of good questions:
- "Which of these two future business directions is actually committed for the next 12–24 months?"
- "Is this legacy name an asset the company intends to preserve, or is replacement genuinely on the table?"

Examples of bad questions:
- "Do you prefer serif or sans?"
- "Which palette do you like?"

### 3. Record evidence without overstating it

Material findings belong in `research.findings`:

```json
{
  "id": "E-001",
  "claim": "what was found",
  "kind": "fact | observation | hypothesis",
  "source": "URL, document, interview, dataset or founder statement",
  "confidence": "high | medium | low",
  "validation": "verified | needs_field_research",
  "state": "active | challenged | superseded"
}
```

Rules:
- competitor behavior observed publicly is evidence about competitors;
- it is not proof of what customers perceive or remember;
- founder statements are evidence of intent/internal knowledge, not automatically market facts;
- if a consequential decision rests on an unverified perception hypothesis, mark the V4 gap explicitly.

### 4. Build strategy from evidence

Compress the evidence into choices:
- customer and not-customer;
- competitive alternatives;
- right to win;
- differentiation;
- relevant cultural/category context;
- theme / organizing idea;
- category entry points or equivalent demand situations when useful;
- mission/manifesto only when it changes behavior.

Use the Because test as a reasoning aid, not machine proof:

`[theme] because [right_to_win/evidence]`

Use an onliness statement only when it clarifies a real difference; never manufacture exclusivity.

### 5. Search creative lineages

Read `creative-direction.md`.

Translate strategy into:
- central idea;
- productive tensions;
- visual/verbal principles;
- reference and anti-reference properties;
- distinctive-asset hypotheses;
- art direction;
- meaningful exclusions.

Explore **different organizing ideas/grammars**, not a fixed number of cosmetic variants. Stop when new routes are no longer materially different or useful.

### 6. Build naming/verbal/identity candidates

Naming → use `naming.md`.

Identity → use `identity-craft.md`.

The identity is a grammar, not a bag of assets. Define only what the declared touchpoints need:
- signature/mark/wordmark concept and production state;
- typography roles/hierarchy;
- color system;
- imagery/illustration/iconography;
- composition behavior;
- motion/sound only when relevant;
- reusable distinctive devices;
- machine-consumable tokens only when useful.

Choices such as number of type families, modular/custom scale, geometry vs expression, minimalism or route count are contextual decisions — not laws.

## PROVE

Apply verification proportional to commitment.

### V1 Structural
Run applicable deterministic checks:

```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
python scripts/asset_checks.py path/to/logo.svg   # when SVG is a final master
```

Use `color_tools.py` where exact color/contrast work is relevant.

### V2 Semantic
Critique:
- evidence-to-claim fit;
- whether strategy makes a useful choice;
- causal quality of rationales;
- strategy → creative direction derivation;
- creative specificity vs category cliché;
- coherence of verbal/visual grammar;
- whether exclusions actually constrain behavior.

Do not let model consensus masquerade as external validation.

### V3 Contextual
Before a FULL commitment, and whenever the system choice has material radius, create representative trial applications from `meta.touchpoints`.

Choose a small set that exposes different stresses, for example:
- tiny vs large;
- dense information vs expressive communication;
- institutional vs promotional;
- screen vs print;
- static vs motion.

For each trial:
- state the job;
- apply the same grammar;
- identify what broke;
- fix the system cause when the failure recurs across applications;
- otherwise fix only the artifact.

### V4 Reality
Use when a market-level claim or high-cost commitment depends on reality:
- customer/stakeholder interviews;
- recognition/comprehension/recall tests;
- behavioral/analytics evidence;
- current legal/trademark specialist opinion;
- operational constraints owned by the organization.

If V4 evidence is unavailable, distinguish `hypothesis`, `pending proof` and `approved risk`. Do not fabricate closure.

## COMMIT

Converge aggressively. Recommend the route that best satisfies:
1. strategy;
2. evidence strength;
3. creative specificity;
4. contextual performance;
5. production feasibility;
6. portfolio architecture;
7. commitment radius.

Do not expose a menu merely because generation was cheap.

Before committing MARKET/HIGH-COST decisions, verify that the required human authority and V4 evidence are sufficient. Lower-radius design choices should normally be made autonomously.

Commit by updating:
- `brand-spec.json`;
- production masters or explicit production briefs/status;
- representative trials;
- portfolio registry where applicable;
- only the touchpoint deliverables the brand actually needs.

## ADAPT

Creation may surface new evidence during trials or launch preparation.

Classify it:
- artifact issue → fix artifact;
- guidance gap that will recur → small system patch;
- challenged belief → update finding state/confidence;
- invalidated rationale/system failure → create EVOLVE candidate.

Do not restart CREATE because one downstream asset is imperfect.

## Delivery

Deliver the **committed result**, not the exploration transcript:
- current `brand-spec.json`;
- selected identity route;
- final masters where verifiable, otherwise concept/production brief status;
- representative trial applications;
- portfolio registry update where needed;
- compiled touchpoint artifacts;
- concise semantic review;
- explicit V4/legal/craft pendencies.
