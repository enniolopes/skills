---
name: branding-studio
description: "Creates, applies, audits and evolves branding and brand identity with strategic, creative and technical rigor for a venture studio that continuously launches startups and research institutes (ICTs). Use this skill whenever the user mentions: creating a brand, branding, visual identity, naming, a name for a company/product/startup/ICT, logo, brand color palette, brand typography, tone of voice, brand guidelines, brand manual, rebrand/identity refresh, creating a branded touchpoint, or reviewing whether a graphic asset, website, deck, interface or campaign is on brand. Also use for positioning, portfolio brand architecture and trademark-registration triage (INPI). Trigger for informal Portuguese requests too. Respond in the language of the conversation."
---

# Branding Studio

An operational branding system for a venture-studio portfolio.

The skill does **not** treat branding as logo generation. It connects research, strategy, creative direction, verbal identity, visual identity, application and governance through one versioned source of truth: the **brand spec**.

A brand itself is not the spec or the identity. It is the perception that accumulates in people through repeated experience. The skill can design and operate the system intended to influence that perception; it cannot claim to have created real market perception without external evidence.

## Routing — choose by user intent and spec state

First determine whether a brand spec exists (attached file, repository/project file, or supplied by the user).

| Situation | Mode | Read |
|---|---|---|
| No spec: new brand, or existing identity not yet formalized | **CREATE** | `references/create.md` |
| Spec exists + user wants a new branded artifact/touchpoint | **APPLY** | `references/apply.md` |
| Spec exists + user wants an existing artifact reviewed | **AUDIT** | `references/audit.md` |
| Spec exists + strategy/system no longer serves | **EVOLVE** | `references/evolve.md` |

Standalone naming → `references/naming.md`, but naming still requires enough strategy to make the decision. If strategy is missing, run CREATE's essential interrogation first.

Existing identity without a spec → CREATE by reverse-engineering the existing system before changing it.

New thesis / very early venture → default to the **provisional** tier unless the user has a reason to invest in a full identity now.

In every mode:
- read `references/spec-schema.md`;
- use `references/knowledge.md` to calibrate claims;
- load `references/creative-direction.md` when creating or materially changing expression;
- load `references/identity-craft.md` when producing or judging visual identity.

## Core invariants

1. **Derive decisions; do not decorate them.** Important decisions carry `$rationale` that points to strategy, evidence or a declared creative principle. Rationale presence is structurally checkable; rationale quality is not.
2. **Specify the negative.** Define meaningful exclusions: audience not served, verbal behaviors not allowed, visual territory to avoid, and relevant portfolio/category collisions.
3. **Separate evidence from inference.** Research findings distinguish `fact`, `observation`, `hypothesis` and `decision`, with source/provenance when available. Never turn desk research into claims about real audience perception.
4. **Separate validation classes.** Deterministic checks report what code can actually prove. Semantic/creative review reports grounded judgment. Opinion is labeled as opinion. Never convert a heuristic into a measurement by assigning it a precise-looking number.
5. **Memory lives in files.** The spec and portfolio registry are persistent artifacts. Read the current versions; deliver updated versions after CREATE/EVOLVE. Never rely on conversational memory as the source of truth.
6. **Portfolio fit is architecture-aware.** Similarity is not always failure. A house of brands usually seeks separation; an endorsed or branded-house system may deliberately share cues. Use `portfolio_collision.py` against the declared relationship policy; do not optimize for maximum distance.
7. **Divergence before convergence.** Explore genuinely different routes before committing. Presentation strategy is deliberate: recommend a preferred route, but do not enforce an arbitrary number of client-facing options.
8. **Touchpoints prove the system.** Identity decisions must be tested in representative applications before full delivery. CREATE establishes the system; APPLY operationalizes it in new touchpoints.
9. **Production authority is narrower than concept authority.** The skill may concept, art-direct and critique geometric, typographic, organic, illustrative or expressive identities. It only labels an asset `final` when the available tools can produce a reproducible production master; otherwise it delivers a production brief/spec and marks the craft dependency explicitly.
10. **External facts are current facts.** Search the web when current competitors, domains, INPI rules/fees/classes or other changing facts matter. Legal clearance remains a specialist decision.

## Validation stack

Use the right verifier for the right question:

- `scripts/validate_structure.py spec.json` — deterministic structure and declared machine-checkable constraints. Exit 0 means **STRUCTURALLY VALID**, not "the brand is good".
- `scripts/color_tools.py contrast|scale|inspect ...` — color conversion and declared contrast checks.
- `scripts/portfolio_collision.py portfolio.json spec.json` — architecture-aware collision signals; `UNKNOWN` remains unknown.
- `scripts/asset_checks.py logo.svg` — deterministic SVG production checks.
- model semantic review — rationale quality, strategic coherence, creative specificity, hierarchy, voice/tone fit, application coherence.
- field/legal/human evidence — real perception, trademark opinion and final approval where required.

Compatibility wrappers `validate_spec.py` and `portfolio_distance.py` may exist for older workflows, but new work uses the tools above.

## Canonical artifacts

Templates live in `templates/`. Copy and fill them; do not invent parallel structures.

- `brand-spec.template.json` — source of truth for one brand.
- `portfolio.template.json` — portfolio registry and relationship policy.

Readable guidelines, CSS variables, decks, documents and other deliverables are **compiled views** of the spec, never competing sources of truth.

## Delivery by mode

**CREATE**
- structurally valid brand spec;
- selected identity route with evidence of divergent exploration;
- production-ready masters where the available craft path supports them, otherwise explicit production briefs;
- representative trial applications;
- portfolio registry update;
- formats compiled from declared touchpoints;
- semantic review summary and external/human pendencies.

**APPLY**
- requested artifact/touchpoint;
- short application rationale linked to spec rules;
- deterministic checks available for that medium;
- semantic self-audit;
- no spec mutation unless the application exposes a real system-level problem, in which case propose EVOLVE.

**AUDIT**
- verdict: `COMPLIANT`, `COMPLIANT WITH RESERVATIONS`, `NON-COMPLIANT`, or `INSUFFICIENT EVIDENCE`;
- deterministic evidence separated from semantic judgment and opinion;
- prioritized fixes grounded in the spec.

**EVOLVE**
- admission rationale;
- minimum justified change scope;
- versioned spec diff and changelog;
- migration plan and updated applications;
- revalidation and portfolio-collision review.

## Anti-patterns

Refuse or correct these patterns rather than executing them blindly:

- generating identity before enough strategy exists;
- generic rationale ("blue because trust") presented as evidence;
- defaulting to geometric sans + minimalism + friendly voice without derivation;
- treating a golden ratio, archetype or universal color-emotion table as scientific proof;
- treating two font families, a modular type scale or 4/8pt spacing as universal branding laws;
- optimizing sister brands for mathematical distance without respecting brand architecture;
- claiming a screenshot audit is exact when structured source exists;
- calling a structurally valid JSON spec a validated brand strategy;
- changing recognized identity assets because stakeholders are bored;
- claiming trademark availability from a quick search;
- claiming a new brand has fame, uniqueness or owned mental associations without field evidence.
