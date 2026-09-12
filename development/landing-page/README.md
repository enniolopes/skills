# Landing Page Skill v3.5.1 experimental

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

v3.5.1 is an experimental evolution over v3.1. The core hypothesis remains that premium landing-page work fails less from missing design knowledge than from **drift between global truth/intent/direction and many locally plausible decisions**. Later iterations added evidence-fit routing and causal negative control. v3.5 consolidates overlapping decision models and removes parallel sources of truth while preserving concrete domain detail that helps the model act well.

The consolidation was informed by basis-form's case→rule discipline, but the runtime does **not** claim its quality dimensions are a mathematically orthogonal basis. Judge the change by behavior, coverage, context cost and resistance to drift — not by architecture vocabulary.

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

## v3.5 — decision-model consolidation

v3.5 does not add a framework. It removes overlapping specifications and makes decision ownership clearer:

- `SKILL.md` keeps one quality model: truth, meaning, specificity, hierarchy, coherence, expression, distinction, craft, technical mastery and reality. References use those dimensions without redefining them.
- `marketing.md` keeps one page-intent model (`page job`, audience, arrival context, offer, proposition, proof, friction, action) and one visitor-state model. Discovery fills the same model; composition consumes it.
- epistemic status is separate from creative choice: truth-bearing items are `KNOWN`, `INFERRED` or `UNKNOWN`; factual claims are `SUPPORTED`, `QUALIFIED` or `UNSUPPORTED`; creativity is not an evidence status.
- research has one rule in both directions: continue only while expected information can materially change a decision; stop when it is unlikely to do so.
- workflow mode is classified by how much valid solution remains, not merely by whether a page file already exists.
- `control.md` keeps the compact direction contract. `design-quality.md` applies it only through expressive media that have a real job instead of requiring typography, color, imagery, motion, etc. as mandatory fields.
- `verification.md` uses `quality claim → falsifier → valid evidence → severity`, while viewport/craft/multi-lens checks remain ways to find failures rather than parallel definitions of quality.

The consolidation deliberately preserves concrete typography, imagery, motion, accessibility, performance and craft guidance where examples improve decodability. Compression is not textual minimalism.

## Runtime files

Runtime lives in `skills/landing-page/`:

- `SKILL.md` — quality model, autonomy, evidence fit, negative control, modes, invariants, method, gates and hard stops.
- `references/control.md` — creative direction/continuity contract and pivot model.
- `references/discovery.md` — decision authority, research value, reference study, synthesis and evidence status.
- `references/marketing.md` — page intent, visitor-state model, proposition, proof, narrative and conversion.
- `references/design-quality.md` — art direction, causal negative control, visual grammar and craft.
- `references/technical-excellence.md` — performance, responsive behavior, semantics, motion, accessibility and graceful degradation.
- `references/verification.md` — quality-to-falsifier verification, browser/render loop, deterministic/perceptual QA, critique lenses and completion.

## Evaluation

`development/landing-page/evals/` never ships and contains only three durable assets:

- `behavioral-evals.json` — 14 high-signal regression cases, one per materially distinct failure mechanism or necessary inverse guardrail.
- `creative-benchmark.json` — eight unrelated briefs for blind creative-quality and mode-collapse testing.
- `evaluation.md` — evidence levels, pinned independent A/B procedure, evaluation criteria, acceptance rule and iteration policy.

Historical proxy audits and parallel rubric/protocol documents were removed; Git history is sufficient if that evidence ever needs to be inspected again.

## Current test status

Repository CI validates structure, contracts, JSON and token budgets. That is structural evidence only.

Independent executor contexts plus blind rendered review remain required before claiming v3.5.1 is behaviorally or creatively superior to v3.1. Targeted regressions protect against known failure mechanisms; they do not establish broad superiority. Real repeated project performance remains the strongest evidence level.

## Acceptance principle

Do not accept v3.5.1 merely because the runtime is shorter, cleaner or more theoretically elegant.

The consolidation is an improvement only if it reduces contradiction/context cost and improves generalization **without losing decodability, specificity, conceptual strength, composition, expressive range, inventiveness, technical rigor or craft**. A compact rule that causes omitted relevant work is a regression. A concrete list that improves reliable decoding may be worth keeping.

Unrelated briefs must also remain visually diverse: either a recurring conventional house aesthetic or a recurring anti-default aesthetic is a failure.

## Tool dependence

The strongest mode has repository/files and runtime access, web/search when public context matters, browser rendering/screenshots, accessibility/performance tooling when relevant, and image/design generation when central assets or exploration benefit.

If a capability is missing, degrade explicitly and never claim evidence that was not collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
