# Discovery, Desk Research, and Reference Study

Load this reference for CREATE, major REFINE, weak/underspecified briefs, public desk research, competitive/category study, or visual/reference research.

The purpose of research is **not** to make the user act as creative director. Research exists to reduce avoidable uncertainty, widen the creative search space, and give the agent enough evidence to make better decisions autonomously.

## Decision order

Always prefer:

`discover → infer safely → choose as expert → ask only if blocking`

A good run should usually reduce the number of questions the user has to answer.

## What belongs to the agent vs. the user

### Agent-owned by default

Decide these without asking a non-expert user unless they explicitly want to collaborate:

- visual direction;
- typography character and pairing;
- palette and color hierarchy;
- page composition and section architecture;
- imagery direction;
- interaction/motion language;
- responsive adaptation;
- layout density;
- visual signature;
- technical mechanism and frontend implementation;
- how to translate existing brand/product material into the page.

### User/external-authority owned

Do not invent:

- product capabilities;
- pricing/terms not found in evidence;
- legal/compliance/security claims;
- customer identities or testimonials;
- performance/outcome metrics;
- business commitments;
- whether a material brand/positioning departure is authorized when current constraints explicitly forbid it.

When one of these is blocking, ask in consequences, not design jargon.

Bad: `Do you prefer an editorial or cinematic direction?`

Better: `The current product is sold through enterprise demos, while the new campaign brief points toward self-serve trial. I can optimize the page for one primary action; I recommend enterprise demo because that is the current live sales path. Should this campaign instead prioritize trial?`

## Research trigger

Research when it can materially change one of:

- proposition;
- audience model;
- proof strategy;
- category conventions;
- distinction opportunity;
- creative direction;
- implementation feasibility.

Do not research because research is available.

### CREATE

Default to meaningful discovery unless the user has already supplied a strong, evidence-rich brief and reference set.

### REFINE

Diagnose first. Research only the layers limiting quality. If the problem is generic category positioning, study category/visual saturation. If the problem is local craft, do not reopen market research.

### REPAIR

Usually no external research. Stay local unless the defect depends on an external technical fact.

## Source hierarchy

For factual/product truth, prefer:

1. user-supplied/canonical product documentation;
2. live first-party product/site/pricing/docs;
3. repository/product behavior;
4. trustworthy primary external sources;
5. secondary reporting;
6. community/review evidence as anecdotal context only.

For visual/creative research, provenance matters less than understanding what is being learned. Never copy protected artwork or another site's identity; extract abstract properties and create an original composition.

## Internal evidence

Before any external lane, inspect what is already available:

- product/site/application and its real UI;
- repository, framework, design primitives, tokens, fonts, assets, routing and patterns;
- docs, pricing, changelog, demos and screenshots;
- brand assets, copy and prior campaigns;
- supplied customer evidence and claims;
- existing analytics/research present in the working context.

## Desk research lanes

Use only the lanes that answer material questions.

### 1. Product truth

Find:

- what the product actually does;
- core mechanism/workflow;
- target user/buyer;
- offer and conversion path;
- strongest real product evidence;
- constraints/limitations relevant to copy;
- brand language and product vernacular.

Useful sources include docs, product UI, pricing, changelog, help center, demos, launch material and repository assets.

### 2. Audience/context

Infer or research:

- sophistication level;
- likely arrival intent;
- language used to describe the problem;
- risk/objection profile;
- how quickly they need to understand the offer;
- device/context when material.

Avoid manufacturing a detailed persona from weak evidence. Use the smallest audience model that changes design decisions.

### 3. Category grammar

Study direct alternatives to answer:

- what conventions help visitors orient quickly;
- what information/proof categories are expected;
- what vocabulary is stable enough to use;
- where competitors create friction or ambiguity.

A convention is not automatically a cliché. Preserve useful interaction/content grammar when it reduces cognitive cost.

### 4. Saturation / anti-reference

Identify patterns that have become generic in the category:

- repeated compositions;
- repeated visual metaphors;
- repeated claims/taglines;
- repeated color/type tropes;
- gratuitous interaction patterns;
- proof devices everyone uses without differentiation.

Record these as **anti-references** when avoiding them creates useful whitespace.

Do not reject a saturated pattern if it remains the clearest solution. Distinction is not novelty for its own sake.

### 5. Proof norms

Find what makes claims believable in this category:

- product demonstration;
- case evidence;
- technical detail;
- before/after state;
- quantified outcome;
- certification/standard;
- customer/peer proof;
- transparent mechanism.

Use only evidence actually available to the project. Research can tell you what proof would be valuable; it cannot fabricate it.

### 6. Technical precedent

For unusual interactions, 3D, WebGL, scroll narrative, audio, video, device inputs, or performance-sensitive work, research implementation precedent only when uncertainty is real.

Seek:

- browser/capability support;
- performance traps;
- accessibility implications;
- fallback strategies;
- simpler mechanisms that may deliver the same experience.

## Reference study: build a visual world, not a collage

A reference study should lead to a design thesis, not a shopping list of websites.

### Pool A — adjacent/category

Use direct competitors/peers mainly to map:

- familiar grammar;
- saturation;
- expected proof;
- what not to imitate.

Do not derive the signature primarily from adjacent references; that tends to pull toward the category mean.

### Pool B — peer-class digital craft

Use high-quality digital references to study transferable properties such as:

- full-page rhythm;
- composition;
- typographic hierarchy;
- image/product integration;
- motion choreography;
- interaction feedback;
- technical restraint/ambition;
- responsive transformation.

### Pool C — non-adjacent world

Prefer this pool when distinction matters. Search the subject's own world and neighboring disciplines:

- editorial/print;
- architecture/interiors;
- industrial/product design;
- film titles/cinematography;
- photography;
- packaging;
- scientific/technical visualization;
- maps/signage;
- fashion/textile;
- physical materials;
- instruments/control surfaces;
- historical/domain artifacts.

This pool should help the page feel culturally and materially specific rather than like a remix of current web galleries.

## Reference extraction protocol

For every reference worth keeping, record mentally or explicitly:

- `SOURCE` — what the reference is;
- `EXTRACT` — the abstract property worth learning from;
- `RELEVANCE` — why that property serves this brief;
- `REJECT` — what must not be copied/carried over;
- `ROLE` — convention, inspiration, technical precedent, or anti-reference.

Example:

```text
SOURCE: scientific imaging console
EXTRACT: dense annotation around one high-contrast primary field
RELEVANCE: makes complex evidence feel inspectable and controlled
REJECT: literal medical palette and faux instrumentation
ROLE: non-adjacent inspiration
```

Do not write `make it look like [reference]` as the design strategy.

## Moodboard / visual-world synthesis

If image search, screenshots, a design canvas, or image generation is available, it can be useful to externalize the visual world. The artifact is optional; the synthesis is mandatory.

A useful visual-world synthesis contains:

- 2–3 emotional anchors;
- material/texture vocabulary;
- typography character, not necessarily exact font yet;
- composition/density principles;
- imagery/crop/lighting behavior;
- color relationships;
- motion/interaction character;
- one or more domain-specific motifs;
- anti-references/clichés to avoid;
- signature territory worth exploring.

Do not let a moodboard become a contract to copy. Its job is to establish a **world of possibilities**.

## Preserve independent ideation

References can create anchoring. For high-ambition work, do at least one of these before committing:

- form an initial thesis from the product/domain before studying peer designs;
- include non-adjacent references;
- generate at least one concept whose governing idea does not come from a reference site;
- explicitly list what the category does repeatedly and design away from it when appropriate.

The test is not whether the work is unprecedented. It is whether the solution was **derived**, not merely adopted.

## Synthesis object

Compress research into this minimal basis:

```yaml
working_brief:
  page_job:
  audience:
  arrival_context:
  offer:
  proposition:
  proof:
  friction:

market:
  conventions_to_preserve:
  cliches_to_avoid:
  proof_norms:
  differentiation_space:

creative:
  emotional_target:
  visual_world:
  signature_territory:
  technical_opportunity:

constraints:
  brand:
  implementation:
  truth_or_authority_gaps:
```

This is an internal decision object, not a mandatory user-facing document. Its job is to make the agent decisive; expose it only when it helps collaboration.

## Evidence classification

Tag every item of the brief internally:

- `KNOWN` — supported by user input or inspected evidence;
- `INFERRED` — reasonable, reversible interpretation that creates no false fact;
- `CREATIVE` — concept, expression, metaphor, art direction;
- `UNKNOWN` — must not be represented as fact.

Resolve `KNOWN`, `INFERRED` and `CREATIVE` yourself. Only an `UNKNOWN` that blocks truth, authority, or a material irreversible fork may become a question (see the question protocol). If a reversible default exists, take it and continue.

## Research stopping rule

Stop when additional research is no longer likely to change:

- the working proposition;
- a material proof decision;
- the category/anti-reference map;
- the creative thesis;
- the technical feasibility choice.

Do not collect references after the direction is already sufficiently grounded merely to appear thorough.

## Question protocol

After discovery/synthesis, ask only if all are true:

1. the answer is not reasonably discoverable;
2. a safe reversible assumption is not available;
3. the answer materially changes truth, authority, commercial outcome, or brand position;
4. proceeding would create avoidable rework or a misleading result.

If asking:

- batch questions;
- use plain language;
- state what you found;
- give a recommendation/default;
- ask for the minimum decision.

Never ask a non-expert to solve the design problem you were engaged to solve.
