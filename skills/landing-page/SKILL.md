---
name: landing-page
description: Research, design, build, redesign, or refine high-end marketing landing pages and homepages where conversion, creative direction, visual distinction, and production-grade web craft matter.
license: CC-BY-NC-4.0
metadata:
  version: 3.1.0
---

# Landing Page

Build marketing pages that feel **designed, not generated**.

Own the page-level outcome end to end. The user may know the product and business but know nothing about marketing, art direction, UX, visual design, motion, or frontend craft. Do not make them perform those jobs for you.

The goal is a marketing experience that feels inevitable for this product and unusually difficult to improve: truthful, specific, immediately legible, coherent, expressive, distinctive, meticulously crafted, technically controlled, and excellent in the real browser.

## Operating standard

Quality is multiplicative:

`quality = truth × specificity × legibility × coherence × expression × distinction × craft × technical mastery × real-world integrity`

A severe weakness in one dimension prevents an exceptional result. Do not average away a generic concept with polished code, a false claim with beautiful art direction, or broken mobile behavior with a strong desktop screenshot. The specification is the floor, not the finish line.

## Expert-default operating model

Default to ownership, not interrogation. Whenever information is incomplete:

`DISCOVER → INFER SAFELY → DECIDE AS EXPERT → ASK ONLY IF BLOCKING`

- **Discover** facts that are economically obtainable from the repo, current site, product, docs, supplied material, or public web.
- **Infer safely** when a reversible assumption is strongly supported and creates no false factual claim.
- **Decide as expert** for design, layout, typography, palette, imagery, narrative form, motion, responsive composition, and implementation.
- **Ask** only when the missing answer belongs to the user's truth/authority or creates a material, non-reversible commercial/brand fork. Then: research first; batch the smallest set of questions; explain the consequence in plain language; recommend a default; continue without another approval round once resolved.

Never ask the user to choose fonts, colors, page patterns, section counts, animation styles, or aesthetic labels because the brief is incomplete. Those are design decisions.

## Load references progressively

- `references/discovery.md` — CREATE, major REFINE, weak briefs, external research, competitive/category study, reference study, evidence classification, question protocol.
- `references/marketing.md` — creating or materially changing proposition, narrative, proof, CTA, or page structure.
- `references/design-quality.md` — CREATE, major REFINE, art direction, divergence and selection, visual grammar, any premium/award-caliber request.
- `references/technical-excellence.md` — award-caliber, animation-heavy, 3D/WebGL/canvas, cinematic, or creative-development work.
- `references/verification.md` — before completing any material CREATE/REFINE when browser/rendering tools are available: build-render loop, QA, critique lenses, severity, stop rule.

## Choose the smallest sufficient mode

- **CREATE** — new landing page, launch/campaign page, marketing homepage, or a page whose concept is effectively undefined. Run the full method.
- **REFINE** — a real page exists but is materially below the standard. Diagnose first; render before major edits when possible. Preserve strong decisions and change the limiting layer.
- **REPAIR** — a bounded defect (broken mobile composition, clipping, weak hierarchy in one region, malfunctioning CTA, local visual mismatch). Fix the defect and its direct causes without reopening strategy or art direction.

Escalate depth only when evidence shows the problem is broader than first observed.

## Invariants

1. **Ground before inventing.** Inspect reality before major decisions.
2. **Never fabricate truth.** No invented customers, logos, testimonials, metrics, awards, certifications, integrations, rankings, case studies, security claims, or quantitative outcomes.
3. **Research reduces uncertainty; it does not outsource judgment.** Do not return references and ask the user to design.
4. **Semantics precede sections.** Derive structure from what the visitor must understand, believe, trust, and do.
5. **Direction precedes substantial code.** Establish a brief-specific creative thesis before building a material new experience.
6. **References are ingredients, not templates.** Extract properties and principles; never imitate another site's identity or composition wholesale.
7. **One dominant signature.** At least one memorable idea tied to the brief, with supporting decisions disciplined enough for it to land.
8. **System, not collage.** Typography, color, spacing, shape, imagery, layout, motion, and interaction behave like one visual language.
9. **Composition before components.** Hierarchy, mass, rhythm, and relationships before cards, pills, badges, grids, or generic containers.
10. **Rendered output is visual truth.** Source code cannot prove visual quality.
11. **Deterministic evidence where possible.** Build, console, overflow, links, accessibility and similar properties are checked by tools, not guessed.
12. **Technical ambition must earn its cost.** Advanced motion/graphics are media, not prestige signals.
13. **Mobile is a composition, not a shrink operation.** Preserve thesis and conversion path across device constraints.
14. **Do not stop at plausible.** A successful first render begins refinement.
15. **Do not finish with known material defects.**

# Method

Each phase names its output; the procedure lives in the reference that owns it.

0. **ORIENT** — classify the mode; inspect the repo/page and declared project commands; identify framework, primitives, tokens, assets, fonts, routing, existing patterns; identify available web/search, browser, screenshot, image-generation/design-canvas, accessibility and performance tools; establish whether a design/brand system exists and is authoritative. Preserve project architecture unless the outcome truly requires changing it.
1. **DISCOVER** (`discovery.md`) — for CREATE and major REFINE, reconstruct the brief from internal evidence, then the desk-research lanes and reference pools that resolve real uncertainty. Every research action answers an uncertainty or widens the creative search space; none exists to collect names.
2. **SYNTHESIZE** (`discovery.md`) — compress evidence into the working brief; tag every item `KNOWN`, `INFERRED`, `CREATIVE` or `UNKNOWN`; resolve the first three yourself; ask only about an `UNKNOWN` that blocks truth, authority or an irreversible fork.
3. **DIRECT** (`design-quality.md`) — form a point of view before substantial implementation: visual thesis, emotional target, visual world, signature, content thesis, interaction thesis, restraint; technical thesis for ambitious work. Under material creative uncertainty, diverge into 2–3 structurally different directions and select the strongest yourself.
4. **COMPOSE** (`marketing.md`) — design in visitor-state transitions, not section names: `arrival → understanding → belief → evidence → reduced friction → action`. Every region has one job, an incoming and desired state, a dominant message, its strongest evidence, a dominant visual relationship and a transition. The first viewport is a thesis; the whole page has rhythm.
5. **SYSTEMIZE** (`design-quality.md`) — stabilize the visual grammar as roles and relationships, extending an existing system deliberately rather than creating a second language.
6. **REALIZE** — build production-oriented code in the existing environment: semantic HTML and native browser behavior; the project's framework, routing, component and dependency conventions unless change is justified; primitives reused where they fit, never forced onto a composition that needs another model; dependencies only for meaningful capability; understandable component ownership; real supplied assets, and central assets created or obtained through available tools rather than rough placeholders; visible text code-native unless it intrinsically belongs inside an image; primary actions real when destinations exist. Build in visual slices (`verification.md`), rendering between slices. Type, imagery, motion and responsive recomposition follow `design-quality.md`; animation-heavy or 3D work follows `technical-excellence.md`.
7. **REFINE** (`verification.md`) — the first successful render begins QA. Run the render loop: deterministic checks, viewport QA, perceptual QA; find the largest remaining defect, correct it, render again. Prefer targeted corrections to wholesale regeneration once a direction is established.
8. **CRITIQUE** (`verification.md`) — for premium work, run separate lenses: first-time visitor, creative director, craft reviewer, creative developer/technical jury. Fix every `BLOCKER` and `MATERIAL` finding before completion; polish until further change no longer produces meaningful improvement.

# Quality gates

A material CREATE/REFINE result is exceptional only when all applicable gates pass:

- **Truth** — no unsupported claim or fabricated credibility device appears as real.
- **Meaning** — a relevant visitor understands what this is, why it matters, and the primary next action without reconstructing intent.
- **Specificity** — the concept is causally tied to this product, audience, brand, content or domain; a logo swap would break the design logic.
- **Hierarchy** — attention has an intentional order.
- **Coherence** — typography, color, imagery, shape, motion, spacing and layout behave as one system.
- **Expression** — appropriate emotional character without sacrificing comprehension or familiar interaction where familiarity matters.
- **Distinction** — one memorable signature; novelty concentrated where it adds meaning, emotion or recall.
- **Craft** — no important region looks approximate, templated, unfinished or weaker than the rest, at macro, meso and micro scale.
- **Technical mastery** — meaningful semantics, disciplined runtime behavior, intentional responsive adaptation, purposeful motion, accessible interaction, graceful degradation.
- **Reality** — functional, free of material rendering/runtime defects, strong outside the ideal screenshot.

Before completing CREATE or major REFINE, run the anti-generic test in `verification.md`; if genericity appears, revise the underlying decision rather than adding decoration.

# Hard stops

Do not declare completion while any applicable material issue remains: broken build/runtime or console failure; primary CTA or required interaction not functioning; clipped/unreadable primary content or accidental horizontal overflow; inferior or broken mobile composition; fabricated or unsupported proof; missing central font/image/asset; major contrast/focus/keyboard defect when testable; uncontrolled type/spacing/system drift; a central composition or major section still generic or prototype-grade for a premium task; a known large mismatch against an accepted concept; preventable jank, resource waste or broken reduced-motion behavior; advanced canvas/WebGL hiding essential content or action; a research-dependent factual claim with no adequate source; an unresolved authority question that would make publication unsafe or misleading. The full defect list is in `verification.md`.

If blocked by missing capability or external authority, report the blocker precisely instead of pretending the result was verified.

# Completion behavior

Do the work; do not narrate every design decision. A non-expert should be able to give a weak brief and receive a resolved page, not a questionnaire.

At handoff, report concisely: what was created or materially changed; the core direction/signature when useful; checks actually performed; any unresolved blocker or evidence gap. Never claim browser inspection, accessibility, performance, research, or other evidence that was not collected.

**North star:** the page should feel inevitable for the product, memorable for the right reason, technically effortless, and unusually difficult to improve.
