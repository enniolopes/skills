# Landing Page Skill v3.3 experimental

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

v3.3 is an experimental evolution over v3.1. Its hypothesis is narrow: premium landing-page work fails less from missing design knowledge than from **drift between global truth/intent/direction and many locally plausible decisions**. The solution must improve continuity without turning creative work into a state machine.

## Stable v3 foundation

For incomplete briefs:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

The material workflow remains:

`ORIENT → DISCOVER → SYNTHESIZE → DIRECT → COMPOSE → SYSTEMIZE → REALIZE → REFINE → CRITIQUE`

The user owns business truth and authority; the agent owns professional design, marketing, art direction, UX, motion and implementation judgment unless a real blocker requires human authority.

## v3.3 experiment — continuity with bidirectional creative learning

The lightweight control model is:

`TRUTH → INTENT → DIRECTION → EXPRESSION → EXECUTION`

The layers have unequal inertia. Facts and authoritative constraints should not drift. Page intent should change only when a stronger truthful framing is established. Creative direction is a working hypothesis. Composition and implementation stay highly revisable.

The model is **not purely top-down**. Making can teach. A render, prototype or composition experiment may reveal that the original proposition is weak and a stronger truthful framing exists. That discovery becomes an upstream hypothesis to verify against product evidence and authority. Creativity may discover strategy; it may not invent truth.

When material evidence appears, fix the lowest level that fully explains it. **REFINE** when the governing idea still works; **RE-DIVERGE** when the idea itself produces wrong meaning, lacks specificity/evidence support, or a demonstrably stronger idea emerges. Repeated local exceptions are evidence that the problem may live one level upstream.

This is intentionally not a copy of `branding-studio`'s persistent-state architecture. There is no mission-state schema or creative validator. Those mechanisms should be introduced only if independent tests demonstrate a problem they actually solve.

## Runtime files

Runtime lives in `skills/landing-page/`:

- `SKILL.md` — compact operating kernel, autonomy, routing, creative-control principle, modes, invariants, method, gates and hard stops.
- `references/control.md` — lightweight creative continuity/pivot model; loaded at DIRECT and material pivot points, not as early procedural ceremony.
- `references/discovery.md` — desk research, reference study, synthesis and question policy.
- `references/marketing.md` — proposition, proof, narrative and conversion.
- `references/design-quality.md` — art direction, hierarchy, coherence, distinction and craft.
- `references/technical-excellence.md` — performance, responsive behavior, semantics, motion, accessibility and graceful degradation.
- `references/verification.md` — browser/render loop, deterministic/perceptual QA, critique lenses and completion.

## Evaluation assets

Development assets live in `development/landing-page/evals/` and never ship:

- `behavioral-evals.json` — natural-language regression cases; criteria describe outcomes and deliberately avoid requiring internal control vocabulary.
- `creative-benchmark.json` — eight unrelated domain briefs for blind creative-diversity/mode-collapse testing.
- `rubric.md` — reliability, creative performance, anti-rigidity, blind comparison and evidence-level rules.
- `proxy-audit-2026-09-11.md` — what was actually testable in the current environment, findings, limitations and changes caused by the audit.

## Current test status

The current environment could run repository CI but did not expose an independent Claude/Codex runner or model API credentials. Therefore:

- structural validation is real;
- instruction and proxy-behavior audits are useful but not independent performance evidence;
- creative diversity was stress-tested conceptually across eight domains;
- a blinded independent v3.1-vs-v3.3 A/B remains required before treating v3.3 as proven or merging solely on quality claims.

The proxy audit changed the skill in four material ways:

1. compressed `control.md` and delayed its loading to reduce context/salience pressure;
2. made learning bidirectional so creative work can reveal a stronger truthful proposition;
3. rewrote evals that were overfit to the v3.2 taxonomy;
4. added escalation when many local patches suggest an upstream problem.

## Acceptance principle

Do not accept an experimental version merely because it follows process more reliably.

It must improve continuity and productive pivots **without a material regression in specificity, conceptual strength, composition, expressive range, inventiveness or craft**. Run unrelated briefs together: if the skill creates a recurring house aesthetic, that is a regression even when each page is polished.

## Tool dependence

The strongest mode has repository/files and runtime access, web/search when public context matters, browser rendering/screenshots, accessibility/performance tooling when relevant, and image/design generation when central assets or exploration benefit.

If a capability is missing, degrade explicitly and never claim evidence that was not collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
