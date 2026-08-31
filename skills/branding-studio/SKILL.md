---
name: branding-studio
description: "Creates, audits and evolves branding and visual identity with technical rigor and objective verification, for a venture studio that continuously launches startups and research institutes (ICTs). Use this skill WHENEVER the user mentions: creating a brand, branding, visual identity, naming, a name for a company/product/startup/ICT, logo, brand color palette, brand typography, tone of voice, brand guidelines, brand manual, rebrand/identity refresh, or asks to review/audit whether a graphic asset, website, deck or interface 'is on brand'. Also for positioning questions, portfolio brand architecture, and trademark registration (INPI). Trigger it even for informal or Portuguese requests ('me ajuda com um nome', 'cria a marca da nova empresa', 'revisa esse banner', 'dá uma olhada nesse deck')."
---

# Branding Studio

A derivation-and-verification system for creating and maintaining brand identities across a venture studio's portfolio. Not a logo generator: the full method — strategy → naming → verbal system → visual system — operating on a central versioned artifact (the **brand spec**), with objective validation via scripts and portfolio memory against convergence between sister brands. Respond in the language of the conversation.

## Routing — pick the mode by the state of the spec

First ask/verify: **does a brand spec exist for this brand?** (attached file, in the project, or request it from the user)

| Situation | Mode | Read |
|---|---|---|
| No spec (new brand, or existing identity without a spec) | **CREATE** | `references/create.md` |
| Spec exists + new material to review | **AUDIT** | `references/audit.md` |
| Spec exists + no longer serves (customer/competition/context/offering changed) | **EVOLVE** | `references/evolve.md` |

Standalone naming ("I need a name") → `references/naming.md`, but it requires minimum strategy: if there is none, run create.md's essential interrogation first. Existing identity without a spec → offer reverse-engineering into the template (a CREATE fed by the existing material). New thesis, early stage → default to the **provisional tier** (see create.md): most studio theses die before identity becomes an asset; invest the full package only when the thesis survives.

In every mode, also read `references/spec-schema.md` (spec structure) and consult `references/knowledge.md` whenever you need to calibrate claims (consensus vs contested vs myth) or handle register specifics (startup vs research institute).

## Invariants — hold in every mode, no exceptions

1. **Mandatory derivation.** No element enters the spec or a deliverable without `$rationale`: the chain "exists because [lever/brief]". The plausible default does not survive having to justify itself — this is the anti-generic mechanism.
2. **Negative specification.** Every relevant dimension declares the excluded case (who the customer is NOT, what the voice does NOT say, avoided morphologies/hues). Without the negative, audits become opinion.
3. **Epistemic honesty.** Always separate: deterministic checks (numbers, pass/fail, via scripts) from heuristic judgment (0–10 score + cited spec rule) from opinion (declared as such). Never dress opinion as measurement. Flag contested knowledge as contested (knowledge.md).
4. **Memory lives in files.** The environment resets between conversations. The spec and the portfolio registry live in the user's files: request them at the start, deliver them updated at the end (as presented files). Never operate "from memory".
5. **Portfolio consultation before creating.** A new brand is born with negative constraints from its sisters; validate with `portfolio_distance.py`. Differentiation anchors on **shape and name** (strong assets), never on color (the weakest asset).
6. **One delivery, not a menu.** Explore routes internally, deliver ONE, with discarded routes attached as justification. Only present options if the user asks.
7. **Declared boundary.** Out of reach — and said plainly: organic/illustrative/expressive marks (the skill writes the external-designer brief + acceptance criteria, and audits the delivery), definitive legal clearance (lawyer; the skill triages), real fame/uniqueness (field research; treat as hypothesis), the final aesthetic verdict (the user's). Logos only as **parameterized geometric construction** (grid, primitives, coordinates in SVG) — never freehand drawing or raster images.
8. **Touchpoints drive deliverables.** At creation, ask where the brand will live (`meta.touchpoints`) and compile the token definitions into exactly those formats (web → plain CSS variables; deck → templated pptx; print/institutional → CMYK + document template). Never assume tools (Tailwind, Figma...) the user hasn't named. Definition is branding; the delivery format belongs to the touchpoint.
9. **Web search when external facts matter**: INPI/registration fees and rules, current competitors, live category conventions. Never quote fee values from memory.

## Scripts (execute them, never simulate their output)

All in `scripts/`, pure Python 3 (no dependencies):

- `color_tools.py contrast '#fg' '#bg' [body|large|ui]` — WCAG 2.2 (legal floor, pass/fail) + APCA/Lc (perceptual quality; WCAG 3 candidate, not adopted — say so when reporting).
- `color_tools.py scale '#seed' --bg '#background'` — OKLCH tonal scale preserving hue, steps targeting contrast ratios (1.1→13:1). Use it to generate every palette.
- `color_tools.py inspect '#hex'` — L, C, H in OKLCH.
- `validate_spec.py spec.json` — validates the spec's structural invariants (rationales, negatives, DTCG, contrast pairs, modular scale, clear space, voice chart, tier rules). Exit 0 = valid. **Run before any spec delivery.**
- `portfolio_distance.py portfolio.json spec.json` — candidate distance against each sister (shape 0.40, name 0.30, color 0.15, personality 0.15 — weights per the empirical distinctiveness hierarchy). Convergence flags = go back and redo the colliding element.

Canonical templates in `templates/` (brand-spec and portfolio). Copy them; do not invent structure.

## Delivery format per mode

- **CREATE** → validated brand-spec.json + logo construction SVG(s) + updated portfolio registry + formats compiled from touchpoints (CSS variables, deck template, print kit — only what was declared) + application mini-kit (full tier) + readable guidelines (derived from the spec, never a parallel source of truth) + explicit list of human pendencies (lawyer, external designer if any, final aesthetic decision).
- **AUDIT** → report with verdict (COMPLIANT / WITH RESERVATIONS / NON-COMPLIANT), separated blocks (deterministic / heuristic / opinion) and prioritized fixes with the spec's correct value. Ask for the structured source (URL/CSS, deck file, design file) before accepting screenshots.
- **EVOLVE** → spec with bumped version + changelog + explicit diff (before → after → new rationale) + touchpoint migration plan + re-compiled formats. Also the path for promoting provisional → full.

## Anti-patterns (refuse, citing the rule)

Generating without a brief; presenting 3 unrequested options; "blue because it conveys trust" (universal color psychology is weak — derive from theme/convention); golden ratio as an argument (myth — the real thing is optical adjustment); archetypes as science (a heuristic, and say so); *blanding* by inertia (default geometric sans + minimalism = active convergence); rebranding without the admission gate (change only if customer/competition/context/offering changed); promising to "own a color" (legally takes decades of use; empirically the weakest asset); delivering full-tier investment to an unvalidated thesis (offer provisional).
