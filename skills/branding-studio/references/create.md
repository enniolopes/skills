# CREATE mode — build a brand system from evidence to application

Creation is not a sequence of asset-generation prompts. The operating sequence is:

**Interrogate → Research → Strategy → Creative Direction → Naming & Verbal → Identity Grammar → Trial Applications → Converge → Validate → Deliver**

Do not skip from strategy directly to logo/palette/type.

## 0. Choose the investment tier

### PROVISIONAL
For a thesis that may still pivot. Preserve the same spec structure, but allow explicitly pending depth.

Minimum:
- customer / not-customer;
- competitive alternative;
- right to win;
- differentiation/theme;
- preliminary naming triage;
- concise verbal principles + negatives;
- creative direction;
- simple identity grammar suitable for declared MVP touchpoints;
- at least one trial application;
- explicit pending items.

A provisional identity should be promotable without throwing away its reasoning.

### FULL
For a durable venture, an existing organization, or when the user explicitly needs a production-grade system.

Requires the complete workflow below, deeper evidence, production decisions, trial applications, semantic review, legal pendencies and migration/usage guidance where relevant.

## 1. Interrogate — ask only for authority the model cannot invent

Obtain the minimum non-derivable truth:

- What does the organization/product do?
- For whom? **For whom not?**
- What would the audience use/do if this did not exist?
- What capability, asset, ethos or evidence gives this brand a right to win?
- What geographic and language markets matter?
- What is the relationship to the venture studio / parent brand?
- Where will the brand live first? Record those touchpoints in `meta.touchpoints`.
- What constraints are real: legal names, legacy equity, accessibility, production, budget, timing?

Adapt the register:
- **startup** — category legibility, speed of comprehension, investor/customer dual audience, pivot tolerance.
- **research_institute** — scientific/institutional authority, multiple stakeholders, funding/government context, longevity and documentation.

Do not ask the user for information that can be responsibly discovered by desk research.

## 2. Research — distinguish evidence from inference

Research direct and indirect alternatives, category language, category visual codes, current context and relevant legacy material.

Every material finding that feeds a decision should be representable in `research.findings`:

```json
{
  "claim": "what was found",
  "kind": "fact | observation | hypothesis",
  "source": "URL, document, interview, dataset or 'founder statement'",
  "confidence": "high | medium | low",
  "validation": "verified | needs_field_research"
}
```

Rules:
- competitor websites can support observations about competitor behavior;
- desk research cannot prove what customers actually perceive or remember;
- founder statements are useful evidence of intent/inside knowledge, but are not automatically market facts;
- if the decision depends on audience perception and no field evidence exists, state the hypothesis and validation need.

### Category map

Record:
- conventions worth keeping because they aid category recognition;
- conventions worth breaking because they cause sameness or contradict strategy;
- why each choice matters.

Do not break convention merely to appear novel.

## 3. Portfolio fit — before creative generation

Load the portfolio registry and the candidate's architecture model.

Use sister brands as constraints only where the architecture requires separation. A house of brands and a branded house have different goals.

Record relevant overlaps/avoidances in the spec, then later run:

```bash
python scripts/portfolio_collision.py portfolio.json spec.json
```

Treat its output as **collision signals produced by a studio policy**, not scientific measurement of brand distinctiveness.

## 4. Strategy — compress the evidence into choices

Build:
- customer and not-customer;
- competitive alternatives;
- right to win;
- differentiation;
- context;
- theme / organizing idea;
- category entry points or equivalent demand situations;
- manifesto/mission only when useful to the register.

Use the Because test as a **reasoning check**, not a machine-proof:
> `[theme] because [right_to_win/evidence]`

Use an onliness statement when it clarifies a real positioning difference. Do not force the word "only" when the market does not support an exclusivity claim.

Before proceeding, perform a semantic review:
- Does the strategy make a choice?
- Is it supported by available evidence?
- Does it give the creative work useful tension?
- Is any claim stronger than its evidence?

If not, iterate strategy before design.

## 5. Creative Direction — bridge strategy and identity

Read `creative-direction.md`.

Create a creative direction that translates strategy into:
- central brand idea;
- narrative/metaphoric territory;
- 3–5 visual/verbal principles;
- productive tensions (e.g. precise ↔ humane);
- reference frame and anti-reference frame;
- distinctive-asset hypotheses;
- art-direction rules;
- explicit exclusions.

Explore multiple genuinely different creative routes. Different routes must differ in underlying idea/grammar, not merely color or font.

Record meaningful alternatives in `creative_direction.exploration`. There is no mandatory number of client-facing options.

## 6. Naming and verbal identity

If naming is needed, follow `naming.md`.

Build the verbal system from strategy + creative direction:
- voice principles;
- vocabulary and concepts;
- verbosity / grammar / punctuation / capitalization where useful;
- counter-examples (`not_like_this`);
- tone by moment/context;
- key message hierarchy where the brand needs it.

Avoid personality adjectives that cannot change actual writing behavior.

## 7. Identity Grammar — build a language, not a bag of assets

Read `identity-craft.md`.

Define:
- visual principles;
- mark/wordmark/signature concept and production status;
- typography roles and hierarchy model;
- color system;
- imagery/illustration;
- iconography;
- composition/grid behavior;
- motion/sound only if relevant;
- reusable distinctive devices;
- tokens where machine-consumable reuse is valuable.

### Important non-laws

The following are choices, not invariants:
- one vs two+ type families;
- modular vs custom type scale;
- 4/8pt spacing;
- geometric vs expressive mark;
- minimalism;
- one client-facing route vs several.

Choose from the brand's communication problem and touchpoints.

### Color

Use OKLCH tooling where useful for scales and comparisons. Accessibility contrast is a constraint for relevant digital/text applications, not a rationale for choosing the brand hue.

Do not infer meaning from universal "color psychology" tables.

### Logo / signature

The skill may concept and art-direct any morphology.

Set `visual.logo.production.status`:
- `final` — a reproducible master exists and has passed applicable deterministic checks;
- `concept` — concept is approved but production craft remains;
- `external_craft_required` — specialist execution is needed.

Do not call a generated raster image a final logo master.

## 8. Trial Applications — stress the system before freezing it

Create representative applications from `meta.touchpoints` **before** final convergence.

Choose the smallest set that exposes different stresses:
- tiny vs large;
- dense information vs expressive communication;
- light vs dark;
- static vs motion;
- institutional vs promotional;
- screen vs print where relevant.

For each trial:
- state the job;
- apply the same identity grammar;
- note what broke;
- fix the system cause, not only the mockup.

A full-tier identity should have at least one completed trial application and normally several where the touchpoints differ materially.

## 9. Converge

Select the route that best satisfies:
1. strategy;
2. creative specificity;
3. distinctiveness in context;
4. application performance;
5. production feasibility;
6. portfolio policy.

Recommend a preferred route. Show alternatives only when they add decision value or the user asks.

Do not use a composite "creative score" as a substitute for judgment.

## 10. Validate and deliver

### Deterministic
```bash
python scripts/validate_structure.py spec.json
python scripts/portfolio_collision.py portfolio.json spec.json
python scripts/asset_checks.py path/to/logo.svg   # for SVG masters
```

### Semantic
Review:
- rationale quality;
- evidence-to-claim fit;
- strategy-to-creative derivation;
- coherence of verbal/visual grammar;
- category fit vs distinction;
- trial-application performance;
- unresolved contradictions.

### External/human
List explicitly:
- legal/trademark review;
- field research still required;
- specialist craft dependencies;
- final organizational decision/approval.

### Compile deliverables from touchpoints

Examples:
- web/product → semantic tokens/CSS only when useful;
- deck → deck template/application;
- print/institutional → print color specs/document template;
- social/campaign → reusable composition and content templates;
- signage/environment → production and legibility rules.

Do not generate formats the brand does not need.

## Delivery

Deliver:
- updated `brand-spec.json`;
- identity masters or production briefs with status;
- trial applications;
- portfolio registry update;
- compiled touchpoint artifacts;
- readable guidelines derived from the spec;
- semantic review summary;
- explicit pending evidence/legal/craft decisions.
