# Branding Studio

**Branding Studio** turns a tool-enabled AI into an autonomous brand steward: it can create, apply, audit and evolve a brand system with high autonomy while keeping evidence, production limits and real-world uncertainty explicit.

It is designed to do the branding work, not merely advise the user how to do it.

## What it does

Use it to:

- create a brand from zero: strategy, positioning, naming, verbal identity, creative direction, visual identity and representative applications;
- formalize an existing identity into a canonical brand system;
- produce new branded touchpoints such as websites, decks, reports, campaigns, social assets, documents, UI surfaces and signage;
- audit whether an artifact is on-brand and explain exactly what is structural evidence, professional judgment or missing real-world evidence;
- evolve an existing brand when strategy, market reality, touchpoints or constraints materially change;
- triage naming, portfolio collisions, production constraints and trademark-related risk without pretending to provide legal clearance.

The output is not just a logo, palette or guideline document. The canonical result is a **brand system** whose persistent source of truth is `brand-spec.json`.

## How it behaves

Every mission runs the same control plane:

```text
SEARCH → PROVE → COMMIT → ADAPT
```

**SEARCH** inspects available files, assets, repositories, product/site context, current sources and available tools before interrupting the user. It researches, forms hypotheses, explores strategic and creative lineages, prototypes and prunes.

**PROVE** verifies only what can actually be supported. Rigor scales with the consequence of the decision.

**COMMIT** separates cheap candidates from decisions that enter the brand system or the market. The AI should converge and recommend rather than outsource routine professional judgment to the user.

**ADAPT** incorporates new evidence conservatively. Beliefs can change quickly; the brand contract changes only when a material rationale is invalidated or a recurring system failure is demonstrated.

## Intents

| Intent | Use when | Typical result |
|---|---|---|
| **CREATE** | no canonical brand spec exists | new or reconstructed brand system |
| **APPLY** | a spec exists and a new touchpoint is needed | branded artifact without redesigning the brand |
| **AUDIT** | an existing artifact must be evaluated | evidence-based diagnosis and prioritized fixes |
| **EVOLVE** | the current system may no longer serve | minimum justified, versioned brand-system change |

Standalone naming uses the same control plane with the naming reference.

## Autonomy model

The skill is intentionally more autonomous than a traditional client-service workflow.

The AI should inspect and decide first. It should not ask the user to choose routine reversible design decisions such as serif vs sans, palette preference, layout direction or arbitrary style menus when the strategy and available evidence are sufficient.

It interrupts only when one of three gates is material:

- **Truth** — private, future or organizational truth cannot be responsibly discovered or inferred;
- **Authority** — a consequential commitment requires the legitimate decision owner;
- **Reality** — the decision depends on customer, market, legal or other external evidence that does not yet exist or is not accessible.

The goal is not “never ask.” The goal is to spend human attention only where it adds unique value.

## Commitment radius

Not every branding decision deserves the same rigor.

| Radius | Example | Default behavior |
|---|---|---|
| **LOCAL** | crop, layout, headline, one application choice | decide autonomously |
| **SYSTEM** | reusable type rule, signature device, recurring guidance | decide when derived; test downstream |
| **MARKET** | positioning, central identity direction, public naming | stronger evidence + appropriate authority |
| **HIGH-COST** | established renaming, architecture change, retirement of meaningful equity | strong proof + explicit human authority |

This is qualitative professional judgment, not a numeric risk score.

## Verification ladder

The skill keeps four evidence levels separate:

| Level | What it can establish |
|---|---|
| **V1 Structural** | schemas, exact values, file integrity, contrast, machine-checkable constraints |
| **V2 Semantic** | coherence, derivation, specificity, rationale quality, brand fit |
| **V3 Contextual** | whether the system works in representative real touchpoints |
| **V4 Reality** | actual perception, behavior, recall, stakeholder truth, legal/specialist evidence |

A lower level must never impersonate a higher one. Model critique is not customer research. Desk research is not measured audience perception. A structurally valid spec is not proof that the strategy or identity is good.

## Brand state

`brand-spec.json` is persistent memory and the canonical semantic contract. It contains three kinds of state:

- **contract** — committed strategy, creative direction, verbal/visual system and constraints;
- **beliefs/evidence** — findings, hypotheses, provenance, confidence and lifecycle state;
- **history** — changelog and material outcomes that explain future decisions.

The spec is intentionally compressed. It should not store every prompt, rejected candidate or internal exploration trace.

Readable guidelines, CSS variables, decks, documents and other outputs are compiled views of the spec, not competing sources of truth.

## Best way to use it

Give the AI a **mission and access to reality**, not a step-by-step design recipe.

Good requests:

```text
Create the complete branding for this startup. Inspect the repo, site and attached material first. Work autonomously and involve me only when a material truth or high-consequence decision genuinely requires my authority.
```

```text
Use the current brand spec to create our sales deck. Make the professional application decisions yourself, verify the result and do not change the brand system unless the work exposes a recurring system failure.
```

```text
Audit this homepage against the current brand. Prefer the native source over screenshots, separate structural findings from semantic judgment, and tell me whether any issue is local or system-level.
```

```text
The team wants to modernize the identity. Determine whether there is a real reason to evolve it, preserve valid equity, and change only what the evidence justifies.
```

For best results, provide or expose the current spec, existing assets, product/site/repository, relevant business material, portfolio context and any real constraints. Do not summarize information the AI can inspect directly.

## What it is not

Branding Studio is **not**:

- a logo generator;
- a moodboard or style-preset generator;
- a simulated human agency org chart;
- a framework that creates its own fixed swarm of strategist/designer/copywriter agents;
- an aesthetic preference poll;
- a universal design-rule engine;
- a customer-research simulator;
- an oracle for market perception;
- a trademark attorney;
- a rebrand machine that changes assets because a stakeholder is bored;
- a short-term metric optimizer;
- a system that calls generated raster concepts “final masters” when production craft cannot be verified.

The skill can create and operate the **designed brand system**. The brand as actual market perception only exists through repeated real-world experience and must be evidenced externally.

## Production behavior

The host AI may have web access, files, image generation, code execution, SVG tooling, presentation/document tools, analytics or other capabilities. Branding Studio does not hardcode a specific tool stack.

It uses the strongest trustworthy path available and degrades production claims honestly:

```text
final master → tested prototype → concept → recommendation
```

Concept authority can be broad. Final production authority depends on whether the available tools can create and verify a reproducible master.

## Package for ChatGPT or Claude

From `skills/branding-studio/`, run:

```bash
python scripts/package_skill.py
```

This creates `dist/branding-studio.zip` with the required top-level `branding-studio/` folder while excluding generated/cache files. Upload that ZIP through the host's Skills interface. Keep this repository as the source of truth; do not maintain separate ChatGPT and Claude copies.

## Repository map

```text
branding-studio/
├── SKILL.md                  # operating constitution
├── references/               # domain knowledge by intent/craft area
├── templates/                # canonical brand + portfolio state
├── scripts/                  # deterministic verification + packaging tools
├── evals/                    # behavioral contract and regression cases
└── tests/                    # script-level tests
```

Start with `SKILL.md`. The references are progressively loaded only when the mission requires them.

## Core principle

**Explore broadly, verify proportionally, commit narrowly, adapt conservatively.**

The skill should close as many professional branding decisions as possible before consuming human attention — without claiming evidence, authority or production quality it does not actually have.
