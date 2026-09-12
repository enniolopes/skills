# AGENTS.md

This repository is an **Agent-Skills-first monorepo** for reusable AI capabilities. This file is the operating contract for AI sessions that create, maintain, review, or evolve the repository.

The goal is not more framework. The goal is **better observable behavior with the smallest durable structure that can produce it**.

## Operating kernel

Apply these rules before adding instructions, files, tests, abstractions, or platform-specific machinery.

1. **Understand first, synthesize second, implement last.** Inspect the current runtime, evidence, failures, and constraints before changing anything. When studying sources, do not modify the Skill merely because useful material was found; first decide what behavior, if any, deserves promotion.
2. **Improve behavior, not architecture.** A rule, file, Agent, System, script, or layer must improve a decision, prevent a demonstrated failure, enable a needed capability, or reduce real change/risk cost.
3. **Context is expensive.** Permanent runtime text competes for model attention. Keep only guidance that materially changes decisions; load conditional depth progressively.
4. **One decision, one source of truth.** Do not maintain independent copies of the same meaning in prose, manifests, schemas, tests, scripts, or host variants. Choose the owner; derive or verify the rest.
5. **Use basis-form.** Describe the generative axes of a decision space, not a list of remembered cases.
6. **Avoid both abstraction failures.** Do not leave a visible repeated axis scattered across cases; do not create an abstraction before real consumers justify it.
7. **Preserve the problem, keep the solution revisable.** Objectives, truths, constraints, authority, and critical properties deserve stability. Workflows, templates, taxonomies, prompts, and topology are hypotheses and may change.
8. **Use the evidence that can answer the question.** Source inspection, execution, expert judgment, field evidence, user authority, and legal evidence are not interchangeable.
9. **Do not confuse proxies with quality.** Completeness, polish, complexity, repetition, research volume, validator output, or model agreement do not prove strategy, creativity, correctness, perception, or real-world performance.
10. **Mechanize only machine-decidable properties.** Use code for exact contracts. Do not manufacture deterministic scores for subjective quality.
11. **Fix the lowest responsible layer.** Local defect -> local fix. Repeated grammar failure -> system rule. Broken governing idea -> reopen the governing idea. Do not promote every failure into global prompt surface.
12. **Do not claim improvement without observed behavior.** A change earns permanent complexity only when evidence shows a material improvement or a necessary contract change.

## Basis-form

Use these four tests for instructions, code, topology, schemas, and workflows:

- **Irreducible** — removing the element shrinks what the system can correctly decide or do. If another element already owns the same meaning, remove or derive the duplicate.
- **Orthogonal** — each concern has one owner and one reason to change. If one change requires editing unrelated regions, the boundary is probably wrong.
- **Spanning** — the rules cover the relevant decision space, including novel cases, rather than only enumerated examples.
- **Decodable** — a capable model or maintainer can expand the rule correctly without clever hidden conventions.

Watch the two opposite failures:

```text
case-enumeration: repeated points reveal a real axis
    -> promote to a shared rule only when the axis is evidenced and reduces ambiguity/blast radius

empty axis: abstraction/framework exists before real consumers
    -> collapse it until the need is demonstrated
```

Examples are decoding aids and falsifiers, never the source of truth.

## Classify ownership before creating files

Use the smallest durable owner.

| Class | Use when | Canonical location |
|---|---|---|
| **Skill** | reusable expertise, judgment, or workflow invoked for a kind of work | `skills/<name>/` |
| **Agent** | correctness benefits from an independent context/tool/authority/evidence boundary | `agents/<name>.md` |
| **System** | multiple Skills/Agents form one installable/operated capability | `systems/<name>/` |
| **Development** | tests, evals, fixtures, design evidence, source studies, packaging/release support | `development/<name>/` |

These are responsibilities, not size tiers.

### Prefer a Skill by default

Create a Skill when the capability can be expressed as an objective, decision rules, evidence/authority boundaries, workflow, and outputs. A Skill may be sophisticated or multi-phase; size alone never justifies an Agent or System.

### An Agent must earn independence

Create an Agent only when folding it into the caller would materially weaken correctness because it needs one or more of:

- fresh or isolated context;
- different tools or permissions;
- a distinct authority boundary;
- independent evidence or adversarial verification;
- a stable execution role that is meaningful separately from one caller.

Persona, tone, specialization, or prompt length alone are not reasons for an Agent.

An Agent contract should make explicit: responsibility, allowed decisions, forbidden decisions, inputs/evidence, outputs, edit authority, and the independence property it preserves.

### A System exists because composition is the product

Create a System when multiple pieces have distinct responsibilities and need to be installed or operated together for one user-facing job.

```text
Is a piece useful and meaningful by itself?
  yes -> keep it standalone and make the System depend on it
  no  -> keep it inside systems/<system>/
```

Do not create a System merely because a Skill has many files, phases, references, or scripts.

## Design effective Skills

Agent Skills is the portability boundary for standalone Skills:

```text
skills/<name>/
├── SKILL.md
├── references/     # conditional depth
├── scripts/        # deterministic runtime tools
├── assets/         # optional runtime assets
├── templates/      # optional canonical runtime shapes
└── other runtime-only resources only when needed
```

`SKILL.md` should contain the minimum global context required for correct routing and decisions. Specialized depth belongs in references loaded only when relevant.

A strong runtime usually defines only what materially governs behavior:

- purpose and activation;
- truths, constraints, and non-goals;
- authority boundaries;
- generative decision rules;
- ordering/state transitions when order matters;
- evidence rules;
- quality criteria and counterfeit-quality guards;
- routing to conditional references;
- durable outputs/state when needed;
- honest degradation when evidence or tools are unavailable.

Do not copy another Skill's section structure mechanically. Structure follows the capability.

### Progressive disclosure

Move material to a reference when it is conditional, not merely because the main file is long. Keep a rule in `SKILL.md` when most correct executions need it.

A reference earns existence when loading it only in relevant cases improves decisions or reduces permanent context pressure.

### Autonomy without invented truth

Inspect before asking. The Skill should own routine professional decisions that are reversible and supported by available evidence.

Interrupt the user only for missing information that materially changes the work and belongs to:

- private or future truth;
- legitimate authority;
- consequential/irreversible commitment outside the agent's remit;
- unavailable external reality.

Never invent product facts, organizational rules, legal status, market perception, scientific facts, or user authority.

### Speak in capabilities, not vendors

Runtime should prefer semantic capabilities such as `inspect`, `search`, `render`, `generate/edit`, `execute`, and `measure` over provider-specific tool names. If a host lacks the capability, degrade honestly.

Only bind runtime to a vendor feature when the capability genuinely cannot exist without it.

## Evidence discipline

Match the evidence to the claim:

| Question | Evidence capable of answering it |
|---|---|
| inspectable/current fact | source inspection or current authoritative evidence |
| private/future/org truth | owning source or user authority |
| artifact/runtime behavior | build, execute, render, inspect, or measure |
| creative/perceptual quality | explicit professional judgment against the artifact |
| market/behavioral effect | real audience, stakeholder, or behavioral evidence |
| consequential legal claim | current authoritative sources and specialist input when stakes require it |

Do not coerce evidence types. In particular:

- model agreement != market validation;
- desk research != measured perception;
- structural validity != strategic/aesthetic quality;
- mockup polish != system performance;
- test pass != behavioral improvement.

## Change protocol

For material work, follow this sequence:

```text
UNDERSTAND
-> inspect canonical runtime and development evidence
-> identify the concrete need/failure/hypothesis
-> distinguish truth/constraint from current solution

DESIGN
-> classify Skill / Agent / System / Development ownership
-> find the lowest responsible layer
-> derive the smallest generative rule or contract
-> choose evidence that could falsify the change

IMPLEMENT
-> change the canonical source only
-> keep runtime portable and repository-independent
-> add deterministic enforcement only for decidable properties

VERIFY
-> run targeted unit tests for mechanical contracts
-> run the smallest relevant evals for behavioral changes
-> compare baseline/candidate when claiming improvement
-> use field evidence when external reality matters
-> run `python development/validate.py`

DELIVER
-> state only claims supported by the evidence obtained
-> keep unresolved truth/authority/reality dependencies explicit
-> publish generated transport artifacts outside source Git
```

Do not broaden the change merely because adjacent improvements are possible.

## Tests, evals, and field evidence

Use the cheapest valid evidence layer.

### Unit tests and CI

Protect durable machine-decidable contracts: parsers, schemas, exact calculations, deterministic scripts, references, runtime boundaries, dependency integrity, syntax, and packaging mechanics.

Do not freeze exact prose, headings, author/source lists, arbitrary counts, framework vocabulary, or historical implementation shape unless they are themselves contractual.

Blocking CI remains deliberately narrow:

```bash
python development/validate.py
```

Do not add a CI check unless the property is decidable, a failure is a real defect, false positives are low, and the maintenance cost is justified.

### Evals

Use evals for model behavior and artifact quality.

Canonical rule:

```text
one distinct recurring causal failure -> one durable regression case
```

A targeted change runs only cases capable of distinguishing it. A broad method/system change adds the smallest representative coverage needed to expose collateral regressions.

Judge observable decisions, routes, questions, actions, evidence, artifacts, and terminal state — not private chain-of-thought or wording similarity.

When claiming improvement:

1. state the observed failure or hypothesis;
2. define the observable bar;
3. compare released baseline and candidate on the same case when practical;
4. use blinded/pairwise judgment for subjective quality;
5. check representative/holdout cases when the change is broad;
6. record regressions, false blocks, and cost;
7. reject permanent context growth when behavior is materially equivalent.

If an eval rewards exact wording or historical structure instead of desired behavior, fix the eval, not the runtime.

### Field evidence

Real use calibrates recurrence, false positives/blocks, host differences, context pressure, latency, missing capabilities, and unanticipated environments. Do not commit sensitive user traces; preserve only curated non-sensitive evidence.

## Runtime and repository boundaries

Runtime contains only what the installed capability needs to operate correctly. Everything else belongs in `development/` or should not exist.

Ask of every file:

```text
Would the installed capability need this to perform the task correctly?
```

If no, keep it out of runtime.

Installed runtime must not depend on `development/`, repository design notes, or paths outside its installable unit.

Repository topology should satisfy:

- **tree decode** — a shallow tree gives a correct mental model;
- **placement** — new behavior has one obvious home;
- **change locality** — local concepts change locally;
- **deletion** — removing a capability removes a coherent region;
- **dependency clarity** — dependency direction is understandable.

Do not create generic top-level dumping grounds or speculative platform axes. A new top-level responsibility must be irreducible and evidenced by real cases.

## Systems and composition

Current System runtime convention:

```text
systems/<name>/
├── .claude-plugin/plugin.json
├── README.md
├── skills/      # exclusive pieces
└── agents/      # exclusive pieces
```

Treat host-specific system metadata as a distribution/composition edge, not a universal semantic standard. Do not invent a neutral System manifest until multiple real composition surfaces demonstrate a common axis worth extracting.

Reusable pieces stay standalone; exclusive pieces stay inside the System. Never maintain parallel copies.

## Distribution and platform evolution

Canonical capability semantics live in runtime. Marketplaces, manifests, ZIPs, release metadata, install paths, and host bindings are projections.

Generated transport artifacts leave Git; automation must not commit them back to `main`.

Standalone Skill releases should archive `skills/<name>/` directly. Do not maintain per-Skill file manifests or packagers unless a demonstrated transformation cannot be expressed by the generic archive path.

Platform surfaces change faster than capability semantics. When ChatGPT, Claude, Gemini, DeepSeek, or another host changes:

1. test whether the canonical runtime is still valid;
2. distinguish semantic incompatibility from discovery/install/manifest/package change;
3. if only the edge changed, change only the edge;
4. prefer native Agent Skills support;
5. create platform-specific structure only after a real incompatibility earns it;
6. never rewrite capability semantics to satisfy a transient host surface.

Do not make normal PR CI depend on volatile external `latest` behavior. Add compatibility monitoring only when a stable external check has enough signal to justify permanent maintenance.

## Documentation and drift

`README.md` is the public human entry point. `AGENTS.md` is the repository operating contract for AI sessions. Unit-specific development READMEs exist only for information unique to that unit's development.

Executable mechanisms own mechanical truth. Runtime owns capability behavior. This file owns repository-wide decision policy. Avoid prose duplication across them.

When prose and executable behavior disagree, identify the intended authority and remove the drift; do not silently preserve both.

## Versioning

Version user-visible/runtime contract changes intentionally. Do not bump versions for repository-only documentation, tests, eval fixtures, or release plumbing that leaves installed behavior unchanged.

When a System contains independently versioned pieces, do not force lockstep versions unless the install/runtime contract requires it.

## Review before finishing

Ask:

- What observable problem does this change solve?
- Is the owner the smallest correct one?
- Did we add a case-list where a generative rule exists?
- Did we add an abstraction before its span exists?
- Did permanent runtime context grow? If so, what behavior earned that cost?
- Is one meaning now owned in more than one place?
- Are we using a proxy as proof of another property?
- Did we mechanize something that actually requires judgment?
- Could the fix live at a lower layer?
- Does installed runtime still work independently?
- Did platform volatility leak into canonical capability semantics?
- What evidence actually supports the claim that this is better?

## Definition of done

A change is done when ownership is clear; the smallest responsible canonical surface changed; runtime remains portable and independent; no parallel source of truth was introduced; relevant deterministic checks pass; relevant behavioral claims have appropriate evidence; context growth is justified by observed behavior; generated artifacts remain outside source Git; and unresolved truth, authority, external reality, or compatibility limitations are explicit.
