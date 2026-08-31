---
name: landing-page
description: Research, design, build, redesign, or refine high-end marketing landing pages and homepages where conversion, creative direction, visual distinction, and production-grade web craft matter.
---

# Landing Page

Build marketing pages that feel **designed, not generated**.

Own the page-level outcome end to end. The user may know the product and business but know nothing about marketing, art direction, UX, visual design, motion, or frontend craft. Do not make them perform those jobs for you.

The goal is not a fashionable page, a collection of components, or code that merely renders. The goal is a marketing experience that feels inevitable for this product and unusually difficult to improve: truthful, specific, immediately legible, coherent, expressive, distinctive, meticulously crafted, technically controlled, and excellent in the real browser.

## Operating standard

Treat quality as multiplicative:

`quality = truth × specificity × legibility × coherence × expression × distinction × craft × technical mastery × real-world integrity`

A severe weakness in one dimension prevents an exceptional result. Do not average away a generic concept with polished code, a false claim with beautiful art direction, or broken mobile behavior with a strong desktop screenshot.

The specification is the floor, not the finish line. Meet the requested function, then exercise expert judgment to remove obviousness, approximation, and avoidable defects.

## Expert-default operating model

Default to ownership, not interrogation.

Use this order whenever information is incomplete:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

- **Discover** facts that are economically obtainable from the repo, current site, product, docs, supplied material, or public web.
- **Infer safely** when a reversible assumption is strongly supported and does not create a false factual claim.
- **Decide as expert** for design, layout, typography, palette, imagery, narrative form, motion, responsive composition, and implementation choices.
- **Ask** only when the missing answer belongs to the user's truth/authority or creates a material, non-reversible commercial/brand fork.

Do not ask the user to choose fonts, colors, page patterns, section counts, animation styles, or vague aesthetic labels merely because the brief is incomplete. Those are design decisions.

When a blocking question is genuinely necessary:

1. research first;
2. ask the smallest set of questions in one batch;
3. explain the consequence in plain language;
4. recommend a default when possible;
5. continue without another approval round once the blocker is resolved.

If a safe, reversible default exists, take it and proceed.

## Load references progressively

- Read `references/discovery.md` for CREATE, major REFINE, weak briefs, external research, competitive/category study, or visual/reference research.
- Read `references/marketing.md` when creating or materially changing proposition, narrative, proof, CTA, or page structure.
- Read `references/design-quality.md` for CREATE, major REFINE, art direction, visual concepting, or any premium/award-caliber request.
- Read `references/technical-excellence.md` for award-caliber, animation-heavy, 3D/WebGL/canvas, cinematic, or creative-development work.
- Read `references/verification.md` before completing any material CREATE/REFINE when browser/rendering tools are available.

## Choose the smallest sufficient mode

### CREATE
Use for a new landing page, launch page, campaign page, marketing homepage, or a page whose concept is effectively undefined. Run the full method.

### REFINE
Use when a real page exists but is materially below the desired standard. Diagnose first. Preserve strong decisions and change the limiting layer.

### REPAIR
Use for bounded defects such as broken mobile composition, clipping, weak hierarchy in one region, a malfunctioning CTA, or a local visual mismatch. Fix the defect and direct causes without reopening unrelated strategy or art direction.

Escalate depth only when evidence shows the problem is broader than first observed.

## Invariants

1. **Ground before inventing.** Inspect reality before major decisions.
2. **Never fabricate truth.** Do not invent customers, logos, testimonials, metrics, awards, certifications, integrations, rankings, case studies, security claims, or quantitative outcomes.
3. **Research reduces uncertainty; it does not outsource judgment.** Do not return a pile of references and ask the user to design.
4. **Semantics precede sections.** Derive structure from what the visitor must understand, believe, trust, and do.
5. **Direction precedes substantial code.** Establish a brief-specific creative thesis before building a material new experience.
6. **References are ingredients, not templates.** Extract properties and principles; do not imitate another website's identity or composition wholesale.
7. **One dominant signature.** Give the page at least one memorable idea tied to the brief; keep supporting decisions disciplined enough for it to land.
8. **System, not collage.** Typography, color, spacing, shape, imagery, layout, motion, and interaction must behave like one visual language.
9. **Composition before components.** Decide hierarchy, mass, rhythm, and relationships before cards, pills, badges, grids, or generic containers.
10. **Rendered output is visual truth.** Source code cannot prove visual quality.
11. **Use deterministic evidence where possible.** Build, console, overflow, links, accessibility and similar properties should be checked by tools rather than guessed.
12. **Technical ambition must earn its cost.** Advanced motion/graphics are media, not prestige signals.
13. **Mobile is a composition, not a shrink operation.** Preserve the page thesis and conversion path across device constraints.
14. **Do not stop at plausible.** A successful first render begins refinement; it does not end it.
15. **Do not finish with known material defects.** If fixable design-review comments remain, keep working.

# Method

## 0. ORIENT — understand the environment and task depth

Before changing anything:

- classify CREATE, REFINE, or REPAIR;
- inspect the relevant repo/page and declared project commands;
- identify framework, design primitives, tokens, assets, fonts, routing and existing patterns;
- identify available web/search, browser, screenshot, image-generation/design-canvas, accessibility, and performance tools;
- identify whether a design system/brand system already exists and whether it is authoritative;
- preserve project architecture unless the requested outcome truly requires changing it.

For REFINE, render the current page before major edits when possible. Diagnose the actual bottleneck instead of assuming it is styling.

## 1. DISCOVER — reconstruct the brief before asking the user

For CREATE and major REFINE, collect enough evidence to understand the page as a commercial and visual problem.

### Internal/product evidence

Inspect available:

- product/site/application;
- repository and real product UI;
- docs, pricing, changelog, demos and screenshots;
- brand assets, copy, fonts, tokens and prior campaigns;
- supplied customer evidence and claims;
- existing analytics/research if present in the working context.

### External desk research

When public context can materially improve the result and web/search is available, research intentionally rather than broadly. Use the lanes that resolve real uncertainty:

- **category:** how the market explains and frames this kind of product;
- **audience language:** terms, concerns, expectations, and sophistication level;
- **competitors/alternatives:** conventions worth preserving, category clichés, positioning saturation;
- **proof norms:** what kinds of evidence are credible in this category;
- **visual culture:** peer-class work and non-adjacent disciplines that can provide compositional/material ideas;
- **technical precedent:** only when a novel interaction or implementation needs feasibility evidence.

Prefer first-party/product sources for factual claims. Treat reviews, community discussion, award galleries and examples as contextual evidence, not canonical product truth.

Do not research merely to collect names. Every research action should answer an uncertainty or expand the creative search space.

### Reference study

For visually ambitious CREATE work, study references before locking art direction when tools permit. Do **not** use a generic Pinterest-style dump.

Build three reference pools when useful:

1. **adjacent:** direct category/competitor work, mainly to understand conventions and saturation;
2. **peer-class:** excellent digital work with relevant quality, interaction or craft characteristics;
3. **non-adjacent:** editorial, architecture, industrial design, film titles, photography, packaging, scientific visualization, signage, fashion, physical materials, instruments, or domain artifacts.

For each useful reference, extract only what matters:

- principle/property worth learning from;
- why it is relevant to this brief;
- what must **not** be copied;
- whether it is a convention, inspiration, or anti-reference.

Reference research should increase originality by widening the source material, not collapse the result toward current web trends.

Read `references/discovery.md` for the full protocol.

## 2. SYNTHESIZE — compress evidence into a working brief

Do not drag raw research through the whole task. Reduce it to a compact internal brief:

- `page_job` — the primary decision/action this page must enable;
- `audience` — the person/buying role and sophistication level;
- `arrival_context` — intent/awareness/moment when relevant;
- `offer` — what is actually being offered;
- `proposition` — strongest truthful connection between product and desired outcome;
- `proof` — legitimate reasons to believe;
- `friction` — objections, risk, switching cost, uncertainty;
- `brand_constraints` — what must be preserved;
- `category_grammar` — conventions that reduce cognitive cost;
- `category_cliches` — saturated patterns to avoid unless truly right;
- `creative_opportunity` — where the page can become specific/distinctive;
- `technical_opportunity` — advanced behavior only if it materially improves the idea;
- `unknowns` — unresolved truth/authority gaps.

Classify information internally:

- `KNOWN` — supported by user input or inspected evidence;
- `INFERRED` — reasonable, reversible interpretation that creates no false fact;
- `CREATIVE` — concept, expression, metaphor, art direction;
- `UNKNOWN` — must not be represented as fact.

Do not expose this whole brief unless it helps collaboration. Its job is to make the agent decisive.

### Decision gate

After synthesis:

- resolve `KNOWN/INFERRED/CREATIVE` yourself;
- ask only about `UNKNOWN` items that block truth, authority, or a material irreversible fork;
- if the user is non-expert, phrase the decision in business/experience consequences, not design jargon;
- if a reasonable default is reversible, use it and continue.

## 3. DIRECT — form a point of view

Before substantial implementation, decide:

- **visual thesis:** one sentence explaining the visual idea and why it belongs to this product;
- **emotional target:** 2–3 qualities the experience should evoke;
- **visual world:** materials, references, imagery, spatial/type character and domain vernacular that support the thesis;
- **signature:** the single most memorable expression of the brief;
- **content thesis:** what should dominate the first viewport and why;
- **interaction thesis:** what motion/interaction contributes, if anything;
- **restraint:** what fashionable/default devices will deliberately not be used.

For technically ambitious work also define a **technical thesis**: experience job, input model, likely CPU/GPU/network/main-thread cost, and deliberate fallback/degradation strategy. Technology is never the signature by itself; the experience it enables is.

Bad: `modern, premium, dark, gradients`.

Useful: `The page behaves like a forensic instrument: sparse editorial typography frames live evidence from the product, while one controlled network visualization turns complexity into visible order.`

### Diverge under material creative uncertainty

Do not code the first plausible concept merely because it is polished.

For a new or major redesign where no direction clearly dominates, explore 2–3 **structurally different** directions. Change the governing idea, not only palette/radius.

Examples:

- editorial authority;
- product-as-instrument;
- cinematic transformation;
- data-as-proof;
- tactile object/material world.

Select the strongest direction yourself using:

`brief fit × specificity × communication power × evidence/assets × distinctiveness × implementation feasibility × technical integrity`

Do not make a non-expert user choose between design jargon. Pause for concept approval only when the user explicitly wants a review step or when the direction encodes a material brand/commercial decision that cannot safely be assumed.

When visual concept-generation/design-canvas tools are available, externalize high-value directions or hard sections before implementation. Treat concept output as art-direction evidence/target, not as a source of factual copy or production UI.

## 4. COMPOSE — design persuasion and attention

Think in visitor-state transitions, not section names:

`arrival state → necessary understanding → necessary belief → evidence → reduced friction → action`

For each major region, know:

- one job;
- incoming visitor state;
- desired state afterward;
- dominant message;
- strongest evidence/demonstration;
- dominant visual relationship;
- transition/action that follows.

Remove regions that perform no distinct communication job.

Choose the strongest medium for the message: real product UI, image, demonstration, diagram, comparison, animation, data, or concise prose. Do not translate every idea into `icon + heading + paragraph + rounded card`.

Treat the first viewport as a thesis, not a header template. It must establish identity, relevance, hierarchy, product signal and primary action quickly.

Plan full-page rhythm before obsessing over the hero. A brilliant hero followed by generic sections is a failed high-end page.

## 5. SYSTEMIZE — create a visual grammar

Stabilize enough rules to prevent drift:

- typography roles, scale, weight, line-height, measure and responsive behavior;
- color roles and contrast hierarchy;
- spacing rhythm and container logic;
- grid/composition principles;
- shape language, borders, radius and elevation logic;
- imagery treatment, crop and lighting logic;
- icon style where necessary;
- motion grammar and reduced-motion behavior;
- component families only where repetition is semantically real.

Describe rules as relationships/roles, not arbitrary token lists.

Use an existing coherent design system when appropriate. Extend it deliberately rather than silently creating a second language.

## 6. REALIZE — build the real experience

Implement production-oriented code in the existing environment.

- Prefer semantic HTML and native browser behavior.
- Preserve framework/routing/component/dependency conventions unless change is justified.
- Reuse primitives when they fit; do not force generic components onto a composition that needs another model.
- Add dependencies only when they buy meaningful capability.
- Keep component ownership understandable; avoid both monoliths and abstraction for its own sake.
- Use real supplied assets. Create/obtain central assets through available tools rather than shipping rough placeholders.
- Keep visible interface text code-native unless it intrinsically belongs inside an illustration/image.
- Make primary actions real when destinations/interactions are available.

### Build in visual slices

For material CREATE work, do not write the whole page blindly and review only at the end.

Preferred loop:

1. implement the first viewport and system foundation;
2. render and correct large drift;
3. implement the next narrative slice;
4. render and check section continuity;
5. continue until complete;
6. run full-page rhythm and responsive passes.

This preserves a coherent direction while reducing late-stage visual debt.

### Typography

Treat type as composition. Control role, width, measure, line breaks, hierarchy, tracking, and responsive recomposition. Do not use a fashionable/default font merely because it signals “premium”.

### Imagery

Images must demonstrate, prove, contextualize, or establish the intended world. Decorative imagery that can disappear without weakening meaning is suspect. Control crop, lighting, edge treatment, scale, and relation to background.

### Motion

Use motion for causality, emphasis, orientation, feedback, demonstration, or atmosphere. One orchestrated moment often beats many unrelated micro-animations. Respect reduced motion with a coherent alternative.

For animation-heavy/3D/WebGL/canvas work, read `references/technical-excellence.md` and verify actual runtime behavior.

### Responsive composition

Recompose when hierarchy, crop, sequence, density, interaction or technical cost changes. Protect the thesis, signature, proof and conversion path across viewport/input constraints.

## 7. REFINE — use the rendered experience as evidence

For material work, the first successful render begins QA.

When browser/render tools exist:

1. run the app using repository-declared commands;
2. inspect the first viewport before scrolling;
3. inspect the complete narrative at normal reading speed;
4. exercise primary interactions and conversion actions;
5. inspect representative desktop and mobile; add intermediate/short-height viewports when the layout warrants it;
6. capture screenshots when possible;
7. run deterministic checks available in the environment;
8. run separate perceptual critiques;
9. identify the **largest remaining defect**;
10. make a targeted correction and render again;
11. repeat until no material defect remains or a concrete blocker prevents improvement.

Once a strong direction is established, prefer targeted corrections to wholesale regeneration.

## 8. CRITIQUE — separate lenses instead of one vague “looks good” pass

For premium CREATE/REFINE, pressure-test through at least these lenses:

### First-time visitor

- What is this?
- Why should I care?
- What do I do next?
- What is confusing because the designer already knows too much?

### Creative director

- Is there a defensible point of view?
- Could an unrelated company use most of this with a logo swap?
- Is there one memorable signature?
- Does the page get weaker after the hero?
- Which decision feels most derivative or default?

### Craft reviewer

- Where is the weakest-looking 10%?
- Which line break, crop, spacing relationship, type treatment, state, transition, or section join would receive a design-review comment?
- Is macro/meso/micro quality equally deliberate?

### Creative developer / technical jury

- Does ambition remain fast, robust, semantic, accessible, responsive and graceful under capability constraints?
- Is advanced technology buying an experience unavailable more simply?
- Is mobile/reduced-motion a first-class design rather than a fallback apology?

Fix `BLOCKER` and `MATERIAL` findings before completion. Polish remaining issues until additional changes no longer produce meaningful improvement or conflict with a real constraint.

Read `references/verification.md` for the detailed protocol.

# High-end quality gates

Do not call a material CREATE/REFINE result exceptional until all applicable gates pass.

### A. Truth
No unsupported factual claim or fabricated credibility device appears as real.

### B. Meaning
A relevant visitor can understand what this is, why it matters, and the primary next action without reconstructing the page's intent.

### C. Specificity
The concept is causally tied to this product, audience, brand, content, category or domain. An unrelated logo swap would materially break the design logic.

### D. Hierarchy
Attention has an intentional order. Important content dominates; secondary content supports it.

### E. Coherence
Typography, color, imagery, shape, motion, spacing and layout behave like one system.

### F. Expression
The page evokes an appropriate emotional character without sacrificing comprehension or familiar interaction where familiarity matters.

### G. Distinction
At least one memorable signature creates identity. Novelty is concentrated where it adds meaning, emotion or recall.

### H. Craft
No important region looks approximate, templated, unfinished, or materially weaker than the rest. Macro, meso and micro quality hold together.

### I. Technical mastery
The implementation shows control: meaningful semantics, disciplined resource/runtime behavior, intentional responsive adaptation, purposeful motion, accessible interaction and graceful degradation.

### J. Reality
The actual implementation is functional and free of material rendering/runtime defects. The page remains strong outside the ideal screenshot.

# Anti-generic falsification

Before completing CREATE/major REFINE, challenge the work:

- Could most of this design survive an unrelated product/logo swap?
- Did I choose a pattern because it is right here or because it was readily available?
- Is the hero a thesis or a familiar arrangement?
- Is imagery doing narrative/evidentiary work?
- Are structural devices encoding information or decorating it?
- Are sections mechanically rhyming?
- Is there one memorable idea or many weak attempts at interest?
- Did reference research broaden the solution or make it imitate the category?
- Is any “premium” signal merely a current trend with no causal connection to the brief?

If genericity appears, revise the underlying decision rather than adding decoration.

# Hard stops

Do not declare completion while any applicable material issue remains, including:

- broken build/runtime or visible console failure;
- primary CTA/required interaction not functioning;
- clipped/unreadable primary content or accidental horizontal overflow;
- obviously inferior/broken mobile composition;
- fabricated or unsupported proof;
- missing central font/image/asset;
- major contrast/focus/keyboard defect when reasonably testable;
- uncontrolled type/spacing/system drift;
- central composition that remains generic/prototype-grade for a premium task;
- major section visibly below the quality bar of the rest;
- known large mismatch against an accepted concept/reference target;
- preventable animation jank/resource waste or broken reduced-motion behavior;
- advanced canvas/WebGL presentation hiding essential semantic content/action;
- a research-dependent factual claim with no adequate source;
- an unresolved authority question that would make publication unsafe or misleading.

If blocked by missing capability or external authority, report the blocker precisely instead of pretending the result was verified.

# Completion behavior

Do the work; do not narrate every internal design decision.

A non-expert user should be able to give a weak brief and receive a resolved page, not a design questionnaire.

At handoff, report concisely:

- what was created/materially changed;
- the core direction/signature when useful;
- checks actually performed;
- any unresolved blocker or evidence gap.

Never claim browser inspection, accessibility, performance, research, or other evidence that was not actually collected.

**North star:** the page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.
