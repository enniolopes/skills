# Landing Page Skill v3

A high-autonomy Claude Skill for researching, directing, designing, implementing, and refining premium marketing landing pages and marketing homepages.

## What changed in v3

v3 treats the user as the owner of business truth and authority, **not** as the design director. For incomplete briefs, the skill follows:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

The full material workflow is:

`ORIENT → DISCOVER → SYNTHESIZE → DIRECT → COMPOSE → SYSTEMIZE → REALIZE → REFINE → CRITIQUE`

It adds:

- explicit desk research and source hierarchy;
- product/category/competitor/proof-norm research;
- reference and mood/world studies using adjacent, peer-class, and non-adjacent sources;
- anti-imitation rules and anti-reference mapping;
- compact synthesis before art direction;
- expert-default decision ownership for visual/UX/implementation choices;
- blocking-question protocol for truth, authority, and irreversible commercial/brand forks;
- multi-lens critique: first-time visitor, creative director, craft reviewer, technical jury;
- convergence rules so the agent repairs the largest remaining defect rather than endlessly regenerating;
- development evals for autonomy, research, truth, creative direction, production craft, and graceful degradation.

## Runtime files

Runtime lives in `skills/landing-page/` and contains only what the skill needs while operating.

- `SKILL.md` — operating kernel and routing: standard, operating model, modes, invariants, the method as one line per phase, gates, hard stops, completion. Kept under the 5,000-token budget CI enforces; each phase's procedure lives in the reference that owns it.
- `references/discovery.md` — desk research, reference studies, synthesis, and question policy.
- `references/marketing.md` — landing-page semantics, proof, claims, narrative, and conversion.
- `references/design-quality.md` — high-end art direction, hierarchy, coherence, distinction, and craft.
- `references/technical-excellence.md` — creative-development quality: performance, responsive behavior, semantics, motion, accessibility, and graceful degradation.
- `references/verification.md` — browser loop, deterministic QA, perceptual QA, critique lenses, and completion.

## Development files

Development assets belong in `development/landing-page/` and are never shipped. The v3 development bundle carried these files; they are not yet committed to this repository:

- `evals/evals.json` — Anthropic skill-creator compatible behavioral evals.
- `evals/trigger-evals.json` — positive and near-miss trigger cases.
- `evals/rubric.md` — output-quality and blind-comparison rubric.

The official Anthropic packager excludes `evals/` from the runtime `.skill` package. Keep the development ZIP if you want to benchmark and evolve the skill.

## Installation

### Claude.ai / Claude Skills

Upload the packaged `landing-page.skill` file when the product accepts `.skill` packages. It is a ZIP-format skill bundle containing the runtime skill directory.

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

If a capability is missing, the skill must degrade explicitly and must not claim research, rendering, accessibility, or performance evidence that was not actually collected.

## North star

**The page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.**
