# Landing Page Skill v3.5 experimental

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

v3.5 is an experimental evolution over v3.1. The core hypothesis remains that premium landing-page work fails less from missing design knowledge than from **drift between global truth/intent/direction and many locally plausible decisions**. Later iterations added evidence-fit routing and causal negative control. v3.5 consolidates those behaviors into a more basis-form runtime: fewer parallel sources of truth, more novel decisions derivable from compact non-overlapping rules, without removing domain detail that helps the model decode quality.

## Stable v3 foundation

For incomplete briefs:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

The material workflow remains:

`ORIENT → DISCOVER → SYNTHESIZE → DIRECT → COMPOSE → SYSTEMIZE → REALIZE → REFINE → CRITIQUE`

The user owns business truth and authority; the agent owns professional design, marketing, art direction, UX, motion and implementation judgment unless a real blocker requires human authority.

## v3.3 — continuity with bidirectional creative learning

The lightweight control model is:

`TRUTH → INTENT → DIRECTION → EXPRESSION → EXECUTION`

The layers have unequal inertia. Facts and authoritative constraints should not drift. Page intent should change only when a stronger truthful framing is established. Creative direction is a working hypothesis. Composition and implementation stay highly revisable.

Making can teach: a render, prototype or composition experiment may reveal a stronger truthful proposition. That becomes an upstream hypothesis to verify against product evidence and authority. Creativity may discover strategy; it may not invent truth.

When material evidence appears, fix the lowest level that fully explains it. **REFINE** when the governing idea still works; **RE-DIVERGE** when the idea itself is wrong, unsupported, generic in realization, or dominated by a materially stronger idea.

## v3.3.1 — evidence must match the question

For a material uncertainty, identify what can actually settle it and use the cheapest valid resolver. Factual/technical truth, authority, creative/perceptual judgment, artifact/runtime behavior and causal market outcomes require different evidence and are deliberately non-interchangeable.

Adjacent pre-click/post-action context is inspected only when it materially changes a page decision. Behavioral data generates/prioritizes hypotheses; correlation is not treated as causal diagnosis.

No evidence ledger, confidence score, mandatory analytics step, CRO workflow or A/B-testing stage was added.

## v3.4 — negative control without an anti-template

High-end generative work can fail through **counterfeit quality**: a familiar signal is mistaken for the underlying property it merely suggests.

The runtime therefore constrains false inference rather than aesthetic territory:

- polish is not resolution;
- style signals are not specificity or premium quality;
- novelty/complexity is not sophistication;
- repetition is not coherence, and components are not composition.

Any mechanism remains valid when the brief independently earns it. The skill challenges the contextual competent-but-generic attractor before commitment and falsifies concrete proxy failures after render. Cross-run mode collapse remains an evaluation concern rather than a runtime self-awareness requirement.

## v3.5 — basis-form consolidation

v3.5 does not add a new framework. It removes overlapping specifications and makes ownership explicit:

- `SKILL.md` now owns one **canonical quality basis**: truth, meaning, specificity, hierarchy, coherence, expression, distinction, craft, technical mastery and reality. References project it rather than redefining quality.
- `marketing.md` owns one **canonical page-intent basis** (`page job`, audience, arrival context, offer, proposition, proof, friction, action) and one visitor-state model. Discovery fills the same basis; composition consumes it.
- epistemic status is now orthogonal to creative choice: truth-bearing items are `KNOWN`, `INFERRED` or `UNKNOWN`; factual claims are `SUPPORTED`, `QUALIFIED` or `UNSUPPORTED`; creativity is not an evidence status.
- research has one rule in both directions: continue only while expected information can materially change a decision; stop when it is unlikely to do so.
- workflow mode is classified by how much valid solution basis remains, not merely by whether a page file already exists.
- `control.md` remains the owner of the compact direction contract. `design-quality.md` projects that contract through only the expressive media relevant to the brief instead of requiring a field for typography, color, imagery, motion, etc. when a medium has no job.
- `verification.md` derives QA from `quality claim → falsifier → valid evidence → severity`, while viewport/craft/multi-lens checks remain decoding/falsifier-finding aids rather than parallel definitions of quality.

The consolidation deliberately preserves concrete typography, imagery, motion, accessibility, performance and craft guidance where examples improve decodability. Basis-form is not textual minimalism.

## Runtime files

Runtime lives in `skills/landing-page/`:

- `SKILL.md` — canonical quality basis, autonomy, evidence fit, negative control, modes, invariants, method, gates and hard stops.
- `references/control.md` — canonical creative direction/continuity contract and pivot model.
- `references/discovery.md` — decision authority, research value, reference study, synthesis and evidence status.
- `references/marketing.md` — canonical page intent, visitor-state model, proposition, proof, narrative and conversion.
- `references/design-quality.md` — design projection of quality, art direction, causal negative control, visual grammar and craft.
- `references/technical-excellence.md` — performance, responsive behavior, semantics, motion, accessibility and graceful degradation.
- `references/verification.md` — quality-to-falsifier verification basis, browser/render loop, deterministic/perceptual QA, critique lenses and completion.

## Evaluation assets

Development assets live in `development/landing-page/evals/` and never ship:

- `behavioral-evals.json` — natural-language regressions. v2.2 adds basis-form boundary cases for creative-vs-evidence separation, CREATE-depth on an existing obsolete page, inactive expressive media, and research stopping.
- `creative-benchmark.json` — eight unrelated domain briefs for blind creative-diversity/mode-collapse testing.
- `rubric.md` — reliability, evidence fit, decision-basis integrity, creative performance, anti-rigidity, blind comparison and evidence-level rules.
- `independent-ab-protocol.md` — pinned v3.1-vs-v3.5 blind protocol across continuity, negative control, basis-form guardrails and full rendered builds.
- `proxy-audit-2026-09-11.md` — historical record of the earlier v3.2/v3.3 audit; it is intentionally not rewritten to imply later versions were independently tested there.

## Current test status

Repository CI validates structure, contracts, JSON and token budgets. That is structural evidence only.

Therefore:

- structural validation is real when CI passes on the current head;
- instruction audits and same-context proxy reasoning are L1/L2 evidence only;
- targeted regression cases protect against obvious architecture mistakes but do not establish broad superiority;
- separate executor contexts plus blind rendered review remain required before claiming v3.5 is behaviorally/creatively superior to v3.1;
- real repeated project performance remains the strongest evidence level.

## Acceptance principle

Do not accept v3.5 merely because the runtime is shorter, cleaner or more theoretically elegant.

Basis-form is an improvement only if it reduces contradiction/context cost and improves generalization **without losing decodability, specificity, conceptual strength, composition, expressive range, inventiveness, technical rigor or craft**. A compact rule that causes omitted relevant work is a regression. A concrete list that merely decodes a real axis may be worth keeping.

Unrelated briefs must also remain visually diverse: either a recurring conventional house aesthetic or a recurring anti-default aesthetic is a failure.

## Tool dependence

The strongest mode has repository/files and runtime access, web/search when public context matters, browser rendering/screenshots, accessibility/performance tooling when relevant, and image/design generation when central assets or exploration benefit.

If a capability is missing, degrade explicitly and never claim evidence that was not collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
