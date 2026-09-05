# CREATE — establish a brand system

Use CREATE for a new brand or an existing identity with no canonical spec. Commit the smallest defensible system that can govern the venture's real touchpoints.

## Choose investment tier

### PROVISIONAL
Use when thesis, market or offering may still pivot.

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

Keep provisional work promotable without discarding valid reasoning.

### FULL
Use for durable ventures, existing organizations or commitments that justify production-grade depth.

Require deeper evidence, production decisions, semantic review, current legal/market triage where relevant, and representative trials across materially different touchpoint stresses. Do not choose FULL merely because more work can be generated.

## 1. Inspect reality before asking

Recover from available sources:
- what the organization/product does;
- existing name, assets and equity;
- direct/indirect alternatives and category context;
- public audience/category evidence;
- current geographic/language context;
- portfolio/parent relationship;
- touchpoints and production constraints.

Do not ask the user to repeat inspectable facts. Use the Truth/Authority/Reality gates from `SKILL.md` only when inspection cannot resolve a material dependency.

## 2. Record material evidence

Store consequential findings in `research.findings` using `spec-schema.md`.

Preserve provenance and uncertainty:
- public competitor behavior is evidence about competitors, not customer perception;
- founder statements can establish intent/internal knowledge, not automatic market truth;
- unverified perception hypotheses remain hypotheses and carry an explicit V4 gap when consequential.

## 3. Build strategy from evidence

Make explicit choices about:
- customer and not-customer;
- competitive alternatives;
- right to win;
- differentiation;
- relevant cultural/category context;
- theme / organizing idea;
- category entry points or equivalent demand situations when useful;
- mission/manifesto only when it changes behavior.

Use the Because test as a reasoning aid:

`[theme] because [right_to_win/evidence]`

Use an onliness statement only when it clarifies a real difference; never manufacture exclusivity.

## 4. Derive expression

Load `creative-direction.md` and translate strategy into a central idea, productive tensions, behavioral principles, reference/anti-reference properties, distinctive-asset hypotheses, art direction and meaningful exclusions.

Explore materially different organizing ideas/grammars, not cosmetic variants or a fixed route count. Stop when additional routes stop producing materially different useful possibilities.

When naming is in scope, use `naming.md`. For visual identity, use `identity-craft.md`.

Define only what declared touchpoints need:
- signature/mark/wordmark concept and production state;
- typography roles/hierarchy;
- color system;
- imagery/illustration/iconography;
- composition behavior;
- reusable distinctive devices;
- motion/sound only when relevant;
- machine-consumable tokens only when useful.

Treat family count, scale model, geometry/expression, minimalism and route count as contextual decisions, not laws.

## 5. Prove before full commitment

Apply the verification ladder from `SKILL.md` proportionally.

For V1, run applicable deterministic checks:

```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
python scripts/asset_checks.py path/to/logo.svg   # only when SVG is claimed as a final master
```

Use `color_tools.py` where exact color/contrast work matters.

For V2, review at minimum:
- evidence-to-claim fit;
- usefulness of strategic choices;
- causal quality of rationales;
- strategy → creative direction derivation;
- specificity vs category cliché;
- coherence of verbal/visual grammar;
- whether exclusions meaningfully constrain behavior.

For V3, test representative applications from `meta.touchpoints` before FULL commitment and whenever a system decision has material radius. Choose a small set that exposes different stresses such as tiny/large, dense/expressive, institutional/promotional, screen/print or static/motion.

For each trial, state the job, apply the same grammar, identify failures, fix recurring system causes and re-test. One-off failures stay local to the artifact.

Use V4 only when market-level or high-cost decisions depend on external reality. If unavailable, distinguish hypothesis, pending proof and approved risk; do not fabricate closure.

## 6. Commit and deliver

Converge on the route that best satisfies strategy, evidence strength, creative specificity, contextual performance, production feasibility, portfolio architecture and commitment radius. Do not expose an unranked menu merely because generation was cheap.

Before MARKET/HIGH-COST commitment, ensure required authority and evidence are sufficient.

Commit only the necessary persistent/output state:
- `brand-spec.json`;
- production masters or explicit concept/production-brief status;
- representative trials;
- portfolio registry where applicable;
- touchpoint deliverables actually required.

Deliver the committed result, concise semantic review, applicable verification, and explicit V4/legal/craft pendencies. Do not deliver the internal exploration transcript.
