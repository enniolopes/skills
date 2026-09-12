# Landing Page Skill v3.4 experimental

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

v3.4 is an experimental evolution over v3.1. The core hypothesis remains that premium landing-page work fails less from missing design knowledge than from **drift between global truth/intent/direction and many locally plausible decisions**. The experiment now also addresses two related failure classes: using the wrong kind of evidence to settle a material question, and using familiar visual/technical signals as substitutes for the quality they merely resemble.

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

The model is **not purely top-down**. Making can teach. A render, prototype or composition experiment may reveal that the original proposition is weak and a stronger truthful framing exists. That discovery becomes an upstream hypothesis to verify against product evidence and authority. Creativity may discover strategy; it may not invent truth.

When material evidence appears, fix the lowest level that fully explains it. **REFINE** when the governing idea still works; **RE-DIVERGE** when the idea itself produces wrong meaning, lacks specificity/evidence support, or a demonstrably stronger idea emerges. Repeated local exceptions are evidence that the problem may live one level upstream.

This is intentionally not a copy of `branding-studio`'s persistent-state architecture. There is no mission-state schema or creative validator. Those mechanisms should be introduced only if independent tests demonstrate a problem they actually solve.

## v3.3.1 — evidence must match the question

For a material uncertainty, the runtime now asks what can actually settle it and uses the cheapest valid resolver available.

Factual/technical truth, authority, creative/perceptual judgment, artifact/runtime behavior and causal market outcomes require different evidence. They are deliberately non-interchangeable. The skill also inspects adjacent pre-click/post-action context only when it materially changes a page decision, and treats behavioral data as evidence for hypotheses rather than automatic causal diagnosis.

No evidence ledger, confidence score, mandatory analytics step, CRO workflow or A/B-testing stage was added.

## v3.4 — negative control without an anti-template

The new hypothesis is that high-end generative work often fails through **counterfeit quality**: a familiar signal is mistaken for the underlying property it normally suggests.

The runtime therefore constrains false inference rather than aesthetic territory. Four high-coverage anti-substitutions guide art direction:

- polish is not resolution;
- style signals are not specificity or premium quality;
- novelty/complexity is not sophistication;
- repetition is not coherence, and components are not composition.

Any mechanism remains valid when the brief independently earns it. Before committing a major direction, the skill challenges the most available competent-but-generic solution for that brief/category and asks what specific evidence or meaning earns the choice. It does not mechanically invert category conventions.

After rendering, verification looks for concrete manifestations of the same failure: polish hiding unresolved hierarchy, category/trend defaults with weak brief dependence, component convenience replacing composition, repeated geometry replacing coherent variation, and novelty/complexity adding cost without meaning.

Cross-run mode collapse remains an evaluation problem rather than a runtime self-awareness requirement. The eval rubric explicitly fails both a recurring conventional house style and a recurring "anti-AI" house style.

## Runtime files

Runtime lives in `skills/landing-page/`:

- `SKILL.md` — compact operating kernel, autonomy, evidence fit, counterfeit-quality guardrail, modes, invariants, method, gates and hard stops.
- `references/control.md` — lightweight creative continuity/pivot model; loaded at DIRECT and material pivot points, not as early procedural ceremony.
- `references/discovery.md` — desk research, reference study, synthesis and question policy.
- `references/marketing.md` — proposition, proof, narrative and conversion.
- `references/design-quality.md` — art direction, hierarchy, coherence, distinction, causal negative control and craft.
- `references/technical-excellence.md` — performance, responsive behavior, semantics, motion, accessibility and graceful degradation.
- `references/verification.md` — browser/render loop, deterministic/perceptual QA, counterfeit-quality falsification, critique lenses and completion.

## Evaluation assets

Development assets live in `development/landing-page/evals/` and never ship:

- `behavioral-evals.json` — natural-language regression cases; criteria describe outcomes and deliberately avoid requiring internal control vocabulary. v2.1 adds targeted cases for false proxies and the opposite guardrail: preserving familiar mechanisms when the brief genuinely earns them.
- `creative-benchmark.json` — eight unrelated domain briefs for blind creative-diversity/mode-collapse testing.
- `rubric.md` — reliability, evidence fit, creative performance, counterfeit-quality resolution, anti-rigidity, blind comparison and evidence-level rules.
- `independent-ab-protocol.md` — pinned v3.1-vs-v3.4 blind protocol, including continuity/control, targeted negative-control guardrails and full rendered creative builds.
- `proxy-audit-2026-09-11.md` — historical record of what was actually testable during the earlier v3.2/v3.3 audit, findings, limitations and changes caused by that audit. It is not rewritten to imply later versions were tested there.

## Current test status

Repository CI can validate structure, contracts, JSON and token budgets. The current work has not yet produced independent behavioral evidence that v3.4 is superior to v3.1.

Therefore:

- structural validation after each runtime change is real when CI passes;
- instruction and proxy-behavior audits remain L1/L2 evidence only;
- targeted negative-control evals protect against obvious regressions but were written close to the new hypothesis and must not be treated as proof of broad superiority;
- the independent protocol requires separate executor contexts and blind rendered comparison before behavioral/creative superiority is claimed;
- a real-project track remains the strongest evidence level.

## Acceptance principle

Do not accept an experimental version merely because it follows process or rejects familiar AI patterns more reliably.

It must improve continuity, evidence fit and resolution **without a material regression in specificity, conceptual strength, composition, expressive range, inventiveness or craft**. Familiar forms must remain available when earned. Run unrelated briefs together: if the skill creates either a recurring conventional house aesthetic or a recurring anti-default aesthetic, that is a regression even when each page is polished.

## Tool dependence

The strongest mode has repository/files and runtime access, web/search when public context matters, browser rendering/screenshots, accessibility/performance tooling when relevant, and image/design generation when central assets or exploration benefit.

If a capability is missing, degrade explicitly and never claim evidence that was not collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
