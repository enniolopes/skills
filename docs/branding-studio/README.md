# Branding Studio

**Branding Studio** turns a tool-enabled AI into an autonomous brand steward. It can create, apply, audit and evolve a brand system with high autonomy while keeping evidence, production limits and real-world uncertainty explicit.

It is designed to do the branding work, not merely advise the user how to do it.

## What it does

Use it to:

- create a brand from zero: strategy, positioning, naming, verbal identity, creative direction, visual identity and representative applications;
- formalize an existing identity into a canonical brand system;
- produce branded touchpoints such as websites, decks, reports, campaigns, social assets, documents, UI surfaces and signage;
- audit whether an artifact is on-brand while separating structural evidence, professional judgment and missing real-world evidence;
- evolve a brand when strategy, market reality, touchpoints or constraints materially change;
- triage naming, portfolio collisions, production constraints and trademark-related risk without pretending to provide legal clearance.

The canonical result is a **brand system** whose persistent source of truth is `brand-spec.json`, not a loose collection of logo, palette and guideline files.

## Operating model

Every mission runs the same control plane:

```text
SEARCH → PROVE → COMMIT → ADAPT
```

**SEARCH** inspects available files, assets, repositories, product/site context, current sources and tools before interrupting the user. It researches, forms hypotheses, explores materially different strategic/creative lineages, prototypes and prunes.

**PROVE** verifies only what can actually be supported. Rigor scales with the consequence of the decision.

**COMMIT** separates candidates from decisions that enter the brand system or market. The AI should converge and recommend rather than outsource routine professional judgment to the user.

**ADAPT** incorporates genuinely new evidence conservatively. Beliefs can change quickly; the brand contract changes only when a material rationale is invalidated or recurring system failure is demonstrated.

## Intents

| Intent | Use when | Typical result |
|---|---|---|
| **CREATE** | no canonical brand spec exists | new or reconstructed brand system |
| **APPLY** | a spec exists and a new touchpoint is needed | branded artifact without redesigning the brand |
| **AUDIT** | an existing artifact must be evaluated | evidence-based diagnosis and prioritized fixes |
| **EVOLVE** | the current system may no longer serve | minimum justified, versioned brand-system change |

Standalone naming uses the same control plane with the naming reference.

## Autonomy and verification

The skill is intentionally more autonomous than a traditional client-service workflow. It should inspect and decide first, not ask the user to choose routine reversible design decisions when strategy and evidence are sufficient.

Human interruption is reserved for three material gates:

- **Truth** — private, future or organizational truth cannot be responsibly discovered or inferred;
- **Authority** — a consequential commitment requires the legitimate decision owner;
- **Reality** — the decision depends on customer, market, legal or other external evidence that does not yet exist or is inaccessible.

Commitment scales qualitatively:

```text
LOCAL → SYSTEM → MARKET → HIGH-COST
```

Verification scales independently:

```text
V1 Structural → V2 Semantic → V3 Contextual → V4 Reality
```

A lower verification level must never impersonate a higher one. Model critique is not customer research. Desk research is not measured audience perception. A structurally valid spec is not proof that the strategy or identity is good.

## Brand state

`brand-spec.json` contains three semantic kinds of persistent state:

- **contract** — committed strategy, creative direction, verbal/visual system and constraints;
- **beliefs/evidence** — findings, hypotheses, provenance, confidence and lifecycle state;
- **history** — changelog and material outcomes that explain future decisions.

It is intentionally compressed. It should not store every prompt, rejected candidate or internal exploration trace.

## Best way to use it

Give the AI a **mission and access to reality**, not a step-by-step design recipe.

```text
Create the complete branding for this startup. Inspect the repo, site and attached material first. Work autonomously and involve me only when a material truth or high-consequence decision genuinely requires my authority.
```

```text
Use the current brand spec to create our sales deck. Make the professional application decisions yourself, verify the result and do not change the brand system unless the work exposes a recurring system failure.
```

```text
Audit this homepage against the current brand. Prefer native source over screenshots, separate structural findings from semantic judgment, and tell me whether any issue is local or system-level.
```

For best results, expose the current spec, existing assets, product/site/repository, business material, portfolio context and real constraints. Do not manually summarize information the AI can inspect directly.

## What it is not

Branding Studio is not a logo generator, moodboard preset, simulated agency org chart, aesthetic preference poll, customer-research simulator, market-perception oracle, trademark attorney, rebrand machine or short-term metric optimizer.

It can create and operate the **designed brand system**. Actual market perception must be evidenced through real-world experience.

## Production behavior

The host may have web access, files, image generation, code execution, SVG tooling, presentation/document tools, analytics or other capabilities. Branding Studio does not hardcode a host-specific tool stack.

Production claims degrade honestly:

```text
final master → tested prototype → concept → recommendation
```

Concept authority can be broad. Final production authority depends on whether available tools can create and verify a reproducible master.

## Runtime vs development

The repository deliberately separates the installable skill from the files used to develop it.

```text
skills/branding-studio/                 # runtime source only
├── SKILL.md
├── references/
├── templates/
└── scripts/                            # runtime deterministic tools only

development/branding-studio/            # never shipped
├── RUNTIME_CONTEXT.md                  # semantic source policy
├── evals/
├── tests/
└── package_skill.py

docs/branding-studio/README.md           # human documentation
```

The rule is strict:

> **runtime may be tested by development assets; runtime must not contain or observe its tests, evals, build tooling or human documentation.**

The same boundary applies inside runtime prose: it should change execution, provide necessary on-demand domain knowledge, define canonical state or enable runtime verification. Project explanation, architecture rationale and development history belong outside runtime.

The runtime directory is intentionally limited to the kernel, on-demand domain references, canonical templates and deterministic tools used while operating the brand.

## Build the installable package

From the repository root:

```bash
python development/branding-studio/package_skill.py
```

This writes:

```text
dist/branding-studio.zip
```

The packager uses an **explicit runtime manifest**, not “zip everything under the skill folder”. It fails if a required runtime file is missing or if an unexpected source file appears inside `skills/branding-studio/`.

The generated ZIP contains exactly:

```text
branding-studio/
├── SKILL.md
├── references/
├── templates/
└── scripts/
```

It does **not** contain:

```text
README / docs
evals
tests
packaging code
deprecated compatibility wrappers
repository/CI files
```

Use the generated ZIP for ChatGPT/Claude uploads. For hosts that consume a local skill directory directly, copy `skills/branding-studio/`.

## Core principle

**Explore broadly, verify proportionally, commit narrowly, adapt conservatively.**

The skill should close as many professional branding decisions as possible before consuming human attention — without claiming evidence, authority or production quality it does not actually have.
