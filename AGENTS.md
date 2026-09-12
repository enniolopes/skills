# AGENTS.md

This repository is an **Agent-Skills-first monorepo** for reusable AI capabilities. This file is the operating contract for AI sessions that create, maintain, review, or evolve it.

The goal is **better observable behavior with the smallest durable structure that can produce it**.

## Operating kernel

1. **Understand first, synthesize second, implement last.** Inspect the current runtime, evidence, failures, constraints, and host surface before changing anything.
2. **Improve behavior, not architecture.** A rule, file, Agent, System, script, test, or layer must solve a concrete problem, enable a needed capability, or reduce real risk/change cost.
3. **Context is expensive.** Permanent runtime text competes for model attention. Keep only guidance that materially changes decisions; load conditional depth progressively.
4. **One decision, one source of truth.** Choose one semantic owner; derive or verify projections instead of maintaining independent copies.
5. **Use basis-form.** Prefer generative axes over lists of remembered cases.
6. **Avoid both abstraction failures.** Promote a repeated real axis; collapse an abstraction that has no demonstrated consumers.
7. **Preserve the problem; keep the solution revisable.** Truths, objectives, constraints, authority, and critical properties are stable. Workflows, prompts, templates, taxonomies, and topology are hypotheses.
8. **Use evidence that can answer the question.** Source inspection, execution, professional judgment, field evidence, user authority, and legal evidence are not interchangeable.
9. **Do not confuse proxies with quality.** Completeness, polish, complexity, repetition, research volume, validator output, or model agreement do not prove real quality or performance.
10. **Mechanize only machine-decidable properties.** Use code for exact contracts; do not manufacture deterministic scores for judgment.
11. **Fix the lowest responsible layer.** Local defect -> local fix. Repeated grammar failure -> system rule. Broken governing idea -> reopen the governing idea.
12. **Do not claim improvement without observed behavior.** Permanent complexity must be earned by evidence or a necessary contract change.

## Basis-form

Use four tests for instructions, code, topology, schemas, and workflows:

- **Irreducible** — removing it loses a distinct capability or decision.
- **Orthogonal** — it has one owner and one primary reason to change.
- **Spanning** — it covers novel relevant cases, not only examples already seen.
- **Decodable** — a capable model can apply it without hidden conventions.

Examples are decoding aids or falsifiers, never the source of truth.

## Choose the smallest correct owner

| Class | Create when | Canonical location |
|---|---|---|
| **Skill** | reusable expertise, judgment, or workflow for a kind of work | `skills/<name>/` |
| **Agent** | correctness needs an independent context/tool/authority/evidence boundary | `agents/<name>.md` |
| **System** | multiple Skills/Agents form one installable/operated product | `systems/<name>/` |
| **Development** | tests, evals, fixtures, source evidence, or tooling that must not ship | `development/<name>/` |

Prefer a **Skill** by default. Size or multiple phases do not justify an Agent or System.

An **Agent** must earn independence through isolated context, different permissions/tools, distinct authority, independent evidence/adversarial review, or another stable execution boundary. Persona or prompt length is not enough.

A **System** exists because composition is the product. Reusable pieces stay standalone; pieces meaningful only inside the System stay under `systems/<system>/`.

## Build effective Skills

Standalone Skills follow Agent Skills:

```text
skills/<name>/
├── SKILL.md
├── references/     # conditional depth
├── scripts/        # deterministic runtime tools
├── assets/         # optional runtime assets
├── templates/      # optional runtime shapes
└── other runtime-only resources only when needed
```

`SKILL.md` contains the minimum global context required for correct activation and decisions. Keep specialized depth in references loaded only when relevant.

A runtime should contain only what materially governs behavior: purpose/activation, truths and constraints, authority boundaries, generative decision rules, required ordering/state, evidence rules, quality criteria, routing, durable state, and honest degradation when evidence or tools are unavailable.

Do not copy another Skill's section structure mechanically. Structure follows the capability.

### Autonomy and truth

Inspect before asking. Own routine reversible professional decisions when evidence is sufficient. Interrupt only for missing private/future truth, legitimate authority, consequential commitment outside the agent's remit, or unavailable external reality that materially changes the work.

Never invent product facts, organizational rules, legal status, market perception, scientific facts, or user authority.

Runtime should describe semantic capabilities (`inspect`, `search`, `render`, `generate/edit`, `execute`, `measure`) rather than vendor tool names unless the capability genuinely depends on that host.

## Evidence discipline

| Claim | Evidence capable of answering it |
|---|---|
| inspectable/current fact | source inspection or current authoritative evidence |
| private/future/org truth | owning source or user authority |
| artifact/runtime behavior | build, execute, render, inspect, or measure |
| creative/perceptual quality | explicit professional judgment against the artifact |
| market/behavioral effect | real audience/stakeholder/behavioral evidence |
| consequential legal claim | current authoritative sources and specialist input when stakes require it |

Do not coerce evidence types. Structural validity is not creative quality; mockup polish is not system performance; model agreement is not market validation; a passing test is not behavioral improvement.

## Change protocol

```text
UNDERSTAND
-> inspect canonical runtime + relevant development evidence
-> identify the concrete need/failure/hypothesis
-> separate truth/constraint from current solution

DESIGN
-> choose Skill / Agent / System / Development ownership
-> find the lowest responsible layer
-> derive the smallest generative rule or contract
-> choose evidence that could falsify the change

IMPLEMENT
-> change the canonical source only
-> keep runtime portable and repository-independent
-> mechanize only decidable properties

VERIFY
-> run targeted unit tests for mechanical contracts
-> run the smallest relevant evals for behavior changes
-> compare baseline/candidate when claiming improvement
-> use field evidence when external reality matters
-> run `python development/validate.py`

DELIVER
-> claim only what obtained evidence supports
-> state unresolved truth/authority/reality/compatibility limits
-> keep generated transport artifacts outside source Git
```

Do not broaden the change because adjacent improvements are available.

## Tests, evals, and CI

**Unit tests / CI** protect durable machine-decidable contracts: syntax, parsers, schemas, calculations, references, runtime boundaries, dependencies, and deterministic scripts. Do not freeze prose, headings, arbitrary counts, framework vocabulary, or historical implementation shape unless contractual.

Blocking CI stays deliberately narrow:

```bash
python development/validate.py
```

Add a CI check only when failure is a real decidable defect, false positives are low, and maintenance cost is justified.

**Evals** judge model behavior and artifact quality. Canonical rule:

```text
one distinct recurring causal failure -> one durable regression case
```

Run only cases capable of distinguishing a targeted change. For broad changes, add the smallest representative coverage needed to expose collateral regressions. Judge observable decisions/actions/artifacts, not private reasoning or wording similarity. If an eval rewards historical wording instead of desired behavior, fix the eval.

**Field evidence** calibrates host differences, recurrence, false positives/blocks, context pressure, latency, and missing capabilities. Preserve only curated non-sensitive evidence.

## Runtime and development boundaries

Runtime contains only what the installed capability needs to perform correctly. It must not depend on `development/` or repository-only paths.

`development/<name>/` should contain only durable evidence or machinery whose absence would impair future maintenance: tests, evals, necessary fixtures, source-verification evidence, and unit-specific tooling. Avoid narrative READMEs when the files are self-explanatory. Delete completed roadmaps, design transcripts, duplicated runtime explanations, and historical notes once their useful behavior/evidence is canonical elsewhere.

Repository topology should preserve tree decode, obvious placement, change locality, coherent deletion, and clear dependency direction. Do not create speculative top-level axes or generic dumping grounds.

## Distribution and versioning

Capability semantics live in runtime. Marketplaces, manifests, archives, install paths, and host bindings are projections.

When a host changes, first distinguish semantic incompatibility from discovery/install/package change. If only the edge changed, change only the edge. Prefer native Agent Skills support. Create platform-specific structure only after a real incompatibility earns it.

Generated release artifacts never commit back to `main`. Standalone Skill releases archive `skills/<name>/` directly.

Version user-visible/runtime contract changes intentionally. Do not bump runtime versions for repository-only docs, tests, eval fixtures, or release plumbing. Any duplicated version required by a host projection must be mechanically checked against its canonical runtime version.

Do not make normal PR CI depend on volatile external `latest` behavior. Use manual/field compatibility checks until a stable automated check has enough signal to justify permanent maintenance.

## Documentation authority

- runtime files own capability behavior;
- executable mechanisms own mechanical truth;
- `AGENTS.md` owns repository-wide AI maintenance policy;
- `README.md` is the consumer entry point.

Do not duplicate policy across them.

## Definition of done

A change is done when the smallest correct owner changed; runtime remains portable and independent; no parallel source of truth was introduced; relevant deterministic checks pass; behavioral claims have appropriate evidence; context growth is justified; generated artifacts remain outside source Git; and unresolved truth, authority, external reality, or compatibility limits are explicit.
