# Landing Page Skill v3.2 experimental

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

v3.2 is an experimental control-plane iteration over v3.1. It does **not** replace the creative method with a rigid state machine. Its purpose is narrower: preserve global intent across long local execution while keeping creative direction revisable when real evidence falsifies it or a materially stronger idea emerges.

## v3 foundation

v3 treats the user as the owner of business truth and authority, **not** as the design director. For incomplete briefs, the skill follows:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

The full material workflow remains:

`ORIENT → DISCOVER → SYNTHESIZE → DIRECT → COMPOSE → SYSTEMIZE → REALIZE → REFINE → CRITIQUE`

It includes:

- explicit desk research and source hierarchy;
- product/category/competitor/proof-norm research;
- reference and visual-world studies using adjacent, peer-class, and non-adjacent sources;
- anti-imitation rules and anti-reference mapping;
- compact synthesis before art direction;
- expert-default decision ownership for visual/UX/implementation choices;
- blocking-question protocol for truth, authority, and irreversible commercial/brand forks;
- multi-lens critique: first-time visitor, creative director, craft reviewer, technical jury;
- convergence rules so the agent repairs the largest remaining defect rather than endlessly regenerating.

## v3.2 experiment — creative control without creative freezing

The hypothesis under test is that the main long-horizon failure is not lack of design knowledge but **drift between a global creative/strategic intent and many locally plausible implementation decisions**.

v3.2 adds a small control model:

`FOUNDATION → INTENT → DIRECTION → SYSTEM / COMPOSITION → EXECUTION`

The layers have different inertia. Product truth and authoritative constraints should change only with evidence; page intent should remain stable until the decision problem changes; creative direction is a committed hypothesis; composition and implementation remain much freer.

When new evidence arrives, especially from the real browser, the agent should classify the lowest layer that explains the failure before editing. It should **REFINE** when the governing direction remains valid and **RE-DIVERGE** when the direction itself is materially falsified or a clearly stronger governing idea emerges.

This is intentionally not a copy of `branding-studio`'s persistent brand-state architecture. Landing pages are more ephemeral and exploratory. v3.2 therefore does **not** yet add a persistent mission-state schema or runtime control scripts. Those should be considered only if behavioral evals show that prose-level control improves pivot quality but still fails continuity in long sessions.

## Runtime files

Runtime lives in `skills/landing-page/` and contains only what the skill needs while operating.

- `SKILL.md` — operating kernel and routing: standard, autonomy model, creative-control kernel, modes, invariants, method, gates, hard stops, completion. Kept under the 5,000-token budget CI enforces; procedural depth lives in references.
- `references/control.md` — decision-layer inertia, direction as falsifiable hypothesis, wildcard exploration, finding classification, REFINE vs RE-DIVERGE, late better ideas, creative debt, anti-rigidity.
- `references/discovery.md` — desk research, reference studies, synthesis, and question policy.
- `references/marketing.md` — landing-page semantics, proof, claims, narrative, and conversion.
- `references/design-quality.md` — high-end art direction, hierarchy, coherence, distinction, and craft.
- `references/technical-excellence.md` — creative-development quality: performance, responsive behavior, semantics, motion, accessibility, and graceful degradation.
- `references/verification.md` — browser loop, deterministic QA, perceptual QA, critique lenses, and completion.

## Development files

Development assets belong in `development/landing-page/` and are never shipped.

Committed in this experiment:

- `evals/behavioral-evals.json` — regression cases for continuity of intent, root-layer diagnosis, pivot quality, wildcard exploration, genericity, anti-rigidity, mobile transformation and rendered-evidence response.
- `evals/rubric.md` — separates reliability/control from creative performance, includes anti-rigidity and cross-run creative mode-collapse tests, and defines blind v3.1-vs-v3.2 comparison behavior.

Still useful future additions after the first experiment:

- trigger/near-miss evals if invocation quality needs work;
- concrete benchmark briefs with reproducible repositories/assets;
- a lightweight persistent mission-state only if long-run continuity remains a demonstrated failure;
- deterministic runtime helpers only for properties code can actually prove.

## Evaluation principle

Do not accept v3.2 merely because it follows the process more reliably.

The experiment succeeds only if it improves long-horizon coherence and pivot correctness **without a material regression in specificity, conceptual strength, distinction, composition, expressive range or inventiveness**.

Run unrelated briefs as a batch to detect mode collapse. If pages repeatedly converge on the same visual lineage because of the control model, the experiment is a regression even when each individual result looks polished.

## Installation

### Claude.ai / Claude Skills

Upload a packaged `landing-page.skill` file when the product accepts `.skill` packages. It is a ZIP-format skill bundle containing the runtime skill directory.

### Claude Code

Copy `skills/landing-page/` to either:

- `~/.claude/skills/landing-page/` for personal/global use, or
- `<project>/.claude/skills/landing-page/` for project-scoped use.

## Tool dependence

The skill owns judgment and method; it cannot create tools that the host does not expose.

Its strongest mode has access to:

- repository/files and shell/runtime;
- web/search for desk research when public context matters;
- browser rendering/screenshots;
- accessibility/performance tooling when appropriate;
- image/design generation tools when central visual assets or concept exploration benefit from them.

If a capability is missing, the skill must degrade explicitly and must not claim research, rendering, accessibility, performance or other evidence that was not actually collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
