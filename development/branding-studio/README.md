# Branding Studio v2 — creative-engine consolidation

Branding Studio is an autonomous brand steward for creating, applying, auditing and evolving brand systems. Version 2 shifts the runtime center of gravity from governance machinery to the actual work of making a strong brand while preserving the evidence/authority safeguards learned in v1.

## Problem being solved

The previous architecture was strong at answering:

> Can this decision be committed responsibly?

It was weaker at answering:

> Is this actually a specific, coherent, generative and well-resolved brand?

`SEARCH → PROVE → COMMIT → ADAPT`, V1–V4, commitment radii, gates and persistent evidence state formed a sophisticated control plane, but much of research, strategy, creative exploration and design lived inside one broad SEARCH phase. A structurally excellent `brand-spec.json` could therefore coexist with mediocre identity work.

v2 keeps the valid epistemic boundaries but makes the creative process primary.

## Runtime model

Material creation/change now follows:

```text
GROUND
  ↓
FRAME
  ↓
DIVERGE
  ↓
COMMIT DIRECTION
  ↓
BUILD SYSTEM
  ↓
TEST IN USE
  ↓
REFINE or RE-DIVERGE
  ↓
PACKAGE
```

Evidence, authority and consequence operate across this workflow instead of forming a second workflow the model must constantly classify.

The evidence resolver is intentionally small:

```text
inspectable/current fact       → source / authoritative evidence
private/future org truth       → owning source / user authority
creative/perceptual quality    → professional judgment
artifact/system performance    → make / render / inspect / trial
market perception/behavior     → real external evidence
consequential legal claim      → current sources + specialist when needed
```

The key invariant is that evidence of one type cannot impersonate another.

## Quality target

The runtime now uses one shared quality model across creation, identity craft, audit and brand-book work:

- truth;
- relevance to the brand job;
- specificity;
- distinction;
- coherence;
- generativity;
- flexibility;
- craft;
- real-world performance;
- durability.

The model is qualitative. It exists to focus critique, not to manufacture a brand score.

## Counterfeit quality

v2 adds causal negative control rather than an aesthetic blacklist.

The runtime explicitly rejects these substitutions:

```text
spec completeness ≠ brand resolution
symbolism ≠ meaning
style signal ≠ specificity / distinction / premium / timelessness
repetition ≠ coherence / recognizability
mockup polish ≠ system performance
research volume ≠ insight
```

A mechanism remains available when the brief independently earns it. The goal is to prune bad reasoning, not legitimate aesthetic territory.

## Contextual attractor

Before committing a direction, the agent identifies the most available competent-but-generic answer to the current brief/category and asks what in this brand actually earns the proposed choices. This gives the runtime a brief-specific anti-default mechanism without a static “AI slop” blacklist or impossible cross-run self-awareness.

Cross-run mode collapse belongs in evaluation, not runtime.

## Creative exploration and commitment

A central v2 distinction is:

> Exploration may be intuitive; commitment must become defensible.

The runtime no longer requires every emerging idea to arrive with a complete rationale. It may sketch/prototype first, then retain only directions that demonstrate strategic fit, specificity and generative force.

Direction remains a working hypothesis until representative use proves it can generate a coherent system. Repeated genericity, exceptions or range failures can re-open direction even without new market evidence. This is creative/artifact learning, not a claim about market perception.

## Brand job

Strategy now has a canonical `brand_job`: the business/organizational transition the brand must help produce. This separates the task from optional frameworks such as manifesto, archetype, onliness or category-entry-point models.

The required strategic core is deliberately small:

```text
brand job
primary audience
relevant offer truth
alternatives/context
position
right to win
intended meaning
```

Optional frameworks are used only when they change a decision.

## Sparse canonical state

The v4 brand spec is a durable operating contract, not a project database.

It persists only information whose absence would materially increase future drift. Rejected routes, routine trial applications, research dumps, prompts and empty framework/media blocks do not belong in canonical state.

The template contains only the core contract. Optional blocks such as naming, architecture, portfolio, tokens, motion and production structures are added only when materially active.

Legacy v3 specs remain operable. Migration happens during a meaningful CREATE/EVOLVE operation by compressing valid state into the sparse v4 contract; migration itself never justifies redesign.

## Deterministic boundary

`validate_structure.py` was narrowed to properties code can actually establish:

- JSON/required structural shape;
- enums/types;
- evidence ID/reference consistency;
- token references;
- declared color contrast;
- declared modular-scale math;
- production-state coherence;
- optional architecture/naming/portfolio field validity.

It no longer treats rationale length, negative examples or the presence of conventional brand sections as evidence of semantic quality.

`portfolio_collision.py` is now advisory. It reports transparent lexical/tag/color comparison signals plus architecture context, but no universal distance score, severity threshold, pass/fail verdict or legal/confusion conclusion.

## Brand books

`references/brand-book.md` is a runtime module for guideline and handoff work. A brand book is treated as a designed teaching artifact, not a pretty serialization of the spec.

It must teach the causal chain from brand job to creative thesis to system behavior, show range through real/representative applications, distinguish principles from exact production specifications and itself demonstrate the identity at a high level of craft.

## Verbal identity

`references/verbal-identity.md` is loaded only when proposition, messaging, voice/tone or a broader verbal system is materially in scope. It keeps proposition, proof, message and expression distinct; converts generic voice adjectives into observable writing behavior; supports contextual modulation; and tests whether the guidance can generate new communication instead of only describing a few examples.

Naming remains separate because semantic, phonetic, linguistic, operational and legal consequences require their own decision logic.

## Runtime layout

```text
skills/branding-studio/
├── SKILL.md
├── references/
│   ├── apply.md
│   ├── audit.md
│   ├── brand-book.md
│   ├── create.md
│   ├── creative-direction.md
│   ├── evolve.md
│   ├── identity-craft.md
│   ├── knowledge.md
│   ├── naming.md
│   ├── spec-schema.md
│   └── verbal-identity.md
├── templates/
└── scripts/
```

Development assets remain outside runtime. `package_skill.py` uses an explicit manifest and fails on unexpected runtime files.

## Evaluation strategy

The prior suite over-indexed on governance behavior. v2 keeps the highest-value regression cases but adds creative-performance coverage.

`evals/behavioral-evals.json` checks behavior such as:
- brand-job framing;
- existing-equity reconstruction;
- evidence fit without taxonomy ceremony;
- category-default challenge without anti-style inversion;
- intuitive divergence followed by defensible commitment;
- re-divergence when a governing idea fails in use;
- sparse state rather than schema completion;
- brand-book usability;
- counterfeit-quality rejection;
- artifact vs system vs strategy correction scope.

`evals/creative-benchmark.json` contains deliberately different briefs for blind creative comparison and cross-run mode-collapse detection.

`evals/corpus-promotion-evals.json` contains targeted regressions and benchmark oracles for deciding whether corpus-derived knowledge actually changes behavior before it is promoted into runtime.

`evals/rubric.md` evaluates both decision behavior and brand quality. `evals/evaluation-protocol.md` defines same-prompt baseline/candidate runs, blind review and evidence levels.

Structural tests/CI can establish runtime/package/tool integrity. They do **not** establish that v2 creates better brands. Creative superiority requires independent runs and blind comparison; real-world effectiveness requires actual project/market evidence.

## Core principle

**Ground in truth, frame the brand job, explore real alternatives, commit a generative direction, test it in use, and persist only what future work must not lose.**
