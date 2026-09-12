# AGENTS.md

This repository is an **Agent-Skills-first monorepo** for reusable AI capabilities. Treat this file as the operating guide for creating, maintaining, reviewing, and evolving repository units.

The repository should stay easy to understand, easy to extend, and difficult to drift. Prefer a small number of durable semantic boundaries over platform-specific copies, framework ceremony, or speculative abstractions.

## Core model

The repository has four semantic classes:

| Class | Purpose | Canonical runtime location |
|---|---|---|
| **Skill** | Reusable expertise or workflow invoked when a task requires it | `skills/<name>/` |
| **Agent** | A role that needs its own context, tool, authority, or evidence boundary | `agents/<name>.md` |
| **System** | Several capabilities that need to be installed or operated as one unit | `systems/<name>/` |
| **Development** | Tests, evals, fixtures, design evidence, packaging/release support, and other non-runtime material | `development/<name>/` |

These are responsibilities, not size tiers. A large workflow can still be one Skill. A small component can justify an Agent if it needs a real independent boundary. A System exists because composition itself is a product boundary, not because a directory became large.

## First decision: what should this become?

Before creating files, classify the responsibility.

### Create a Skill when

Use a Skill for reusable expertise, procedure, judgment, or task behavior that can operate as an on-demand capability.

Typical signs:

- the user asks the model to perform a kind of work;
- the capability can be described by an objective, decision rules, evidence requirements, workflow, and outputs;
- it should work across more than one project or context;
- it does not require an independently isolated role to be meaningful;
- it can degrade honestly when a host lacks a tool.

A Skill is the default choice for new reusable behavior.

Do **not** create an Agent merely because the Skill is sophisticated, long, multi-phase, or expert-level.

### Create an Agent when

Use an Agent only when an independent execution boundary is materially useful.

At least one of these should be true:

- it needs its own fresh or isolated context;
- it uses materially different tools or permissions;
- it owns a distinct authority boundary;
- independence of evidence is part of correctness, such as adversarial verification;
- it must execute or reason separately so another capability cannot contaminate its role;
- it has a stable contract and meaningful use independent of one particular caller.

Examples of justified agent roles include an evidence collector that does not decide, or an independent verifier that tries to falsify a candidate without editing it.

If none of these boundaries is real, prefer a Skill or a reference inside a Skill.

### Create a System when

Use a System when several Skills and/or Agents only make sense when installed or operated together as one capability.

A System should have:

- one user-facing job;
- an explicit composition boundary;
- multiple pieces with distinct responsibilities;
- a reason to install/use them together;
- a stable ownership model for exclusive versus reusable pieces.

Exclusive pieces live inside the System. Pieces that are useful independently stay top-level and the System depends on them instead of copying them.

Use this test:

```text
Is this piece useful and meaningful by itself?
  yes -> standalone Skill or Agent
  no  -> keep it inside the System
```

Do not create a System just because a Skill has many references, scripts, phases, or files.

### Use Development for everything that should not ship

Tests, evals, research notes, source studies, design records, packaging logic, fixture generators, migration notes, and repository-specific documentation belong in `development/<name>/` unless a runtime genuinely needs them while operating.

Runtime must stay independently installable and repository-independent.

## Source-of-truth rules

One meaning should have one owner.

1. **Runtime behavior has one canonical home.** Never maintain ChatGPT-, Claude-, Gemini-, DeepSeek-, or other host-specific copies of a Skill.
2. **Installed runtime must stand alone.** It must not depend on `development/`, repository-relative design notes, or files outside its installable unit.
3. **Distribution is a projection.** Marketplaces, manifests, ZIPs, host paths, and release metadata distribute runtime; they do not own behavior.
4. **Generated artifacts are outputs.** Do not commit generated release archives back to `main`.
5. **Do not duplicate rules between prose, schemas, tests, and scripts without one explicit authority.** Derive or verify where possible.
6. **Prefer one canonical rule per decision.** Supporting examples can decode the rule; they must not become alternate truth.

When two places say the same thing, decide which one owns the meaning and make the other derive, reference, or disappear.

## Agent Skills is the portability boundary

Standalone Skills should follow the Agent Skills convention:

```text
skills/<name>/
├── SKILL.md
├── references/        # optional, on-demand depth
├── scripts/           # optional, deterministic runtime tools
├── assets/            # optional
├── templates/         # optional
└── other runtime-only resources when genuinely needed
```

`SKILL.md` is the capability entry point. Keep the main file focused on global behavior and routing; move specialized depth to references that are loaded only when relevant.

Do not create platform forks by default. Host-specific mechanics should remain at the distribution edge unless a real semantic incompatibility proves that the canonical Skill cannot express the required behavior.

Runtime instructions should describe **capabilities**, not vendor tool names, unless the runtime truly depends on a specific host feature.

Prefer:

```text
inspect the strongest available source
search current authoritative information when it can change the decision
generate or edit imagery when material exploration benefits from it
run deterministic validation when execution is available
```

over:

```text
call vendor_tool_x
use provider_y_feature
```

If a host lacks a capability, degrade the result honestly rather than pretending the capability ran.

## Designing a Skill

Start from behavior, not document structure.

A useful Skill normally needs only the information that materially changes correct execution:

- purpose and scope;
- activation conditions;
- important truths, constraints, and authority boundaries;
- decision rules;
- workflow or state transitions when ordering matters;
- evidence rules;
- quality criteria;
- routing to specialized references;
- durable outputs or state, if any;
- honest degradation when tools or evidence are unavailable.

Do not manufacture sections because another Skill has them.

### Progressive disclosure

Keep universal behavior in `SKILL.md`. Move detail out when it is conditional.

Good candidates for references:

- domain-specific craft knowledge;
- optional sub-workflows;
- specialized evaluation criteria;
- schemas explained in depth;
- naming, legal, research, or production guidance needed only for some missions;
- examples that help decode a subtle boundary.

A reference should exist because loading it conditionally improves decisions or reduces permanent context pressure, not because a large file feels tidier when split.

### Preserve autonomy without inventing truth

Skills should usually inspect before asking.

Ask the user only when the missing answer belongs to:

- private or future truth;
- legitimate authority;
- an irreversible or consequential choice the agent cannot own;
- external reality that cannot be observed with available evidence.

Do not ask users to perform routine expert work the Skill is supposed to own.

At the same time, never invent product truth, business rules, research facts, legal status, perception, or organizational authority.

### Use the right evidence for the question

Evidence types are not interchangeable.

- inspectable fact -> inspect the source or authoritative evidence;
- private/future fact -> owning source or user authority;
- artifact behavior -> build, render, execute, inspect, or measure;
- creative/perceptual judgment -> explicit professional criteria and artifact inspection;
- market or behavioral claim -> real external evidence;
- legal or high-consequence claim -> current authoritative evidence and specialist input when warranted.

Do not use polish, model agreement, spec completeness, research volume, or validator output as proof of a different property.

### Build generative rules, not case lists

Prefer a basis that spans the decision space over enumerating familiar examples.

A good rule helps with new cases. A brittle rule protects only the examples that inspired it.

Watch both failure directions:

- **under-abstraction**: many repeated cases express one visible axis;
- **over-abstraction**: a framework or layer exists before real consumers justify it.

Promote repeated cases into a shared rule only when the axis is genuinely visible and doing so reduces ambiguity or change cost. Collapse empty abstractions when they have no real span.

## Designing an Agent

An Agent must earn its independence.

Define:

- its responsibility;
- what it may decide;
- what it must not decide;
- what evidence it receives;
- what evidence or artifact it returns;
- whether it may edit or only observe;
- what independence property would be lost if it were folded back into the caller.

Do not duplicate a Skill's full methodology inside an Agent. Keep shared reusable knowledge in Skills when possible, and let the Agent own the distinct execution role.

If an Agent's only justification is a different persona, tone, or name, it probably should not exist.

## Designing a System

A System is composition with one user-facing job.

The current repository convention is:

```text
systems/<name>/
├── .claude-plugin/
│   └── plugin.json
├── README.md
├── skills/             # exclusive runtime skills
└── agents/             # exclusive runtime agents
```

This physical shape reflects current install/runtime constraints; do not generalize it into a universal system standard without evidence from another real composition surface.

When adding a System:

- keep exclusive pieces inside the System;
- depend on standalone reusable pieces instead of copying them;
- keep dependency direction obvious;
- avoid parallel versions of the same capability;
- keep the System README focused on installation, composition, and user operation;
- keep tests/evals/design evidence under `development/<system>/`.

A System may use host-specific composition metadata at the edge while its component Skills remain platform-neutral.

## Repository topology principles

Physical structure is an architectural projection, not decoration.

A good topology should pass these tests:

- **Tree decode** — a shallow tree gives a mostly correct mental model;
- **Placement** — new behavior has one predominantly obvious home;
- **Change locality** — conceptually local changes stay mostly local;
- **Deletion** — removing a capability removes a coherent region;
- **Dependency** — dependency direction is understandable and enforceable where useful.

Do not add a new top-level directory just to anticipate future products or hosts. A new top-level role is an architecture decision and must represent a real irreducible responsibility.

Avoid generic dumping grounds such as `common/`, `shared/`, `utils/`, `platforms/`, or `misc/` unless repeated real cases demonstrate a coherent responsibility that belongs there.

## Runtime versus development

The runtime boundary is strict.

Runtime contains only what the installed capability needs while operating.

Development contains material needed to create, evaluate, verify, package, or understand the capability as a repository project.

Ask of every file:

```text
Would the installed agent need this file to perform the task correctly?
```

If no, it probably belongs in `development/` or does not need to exist.

README files for human contributors should normally stay outside standalone Skill runtime. Runtime guidance belongs in `SKILL.md` or references.

## Deterministic scripts

Use code when code can establish a property more precisely, cheaply, or reproducibly than model judgment.

Good script targets include:

- schema/type validation;
- exact numeric calculations;
- structural checks;
- deterministic asset validation;
- reference resolution;
- reproducible transformations;
- fixture generation.

Do not turn a subjective quality into a fake deterministic score merely because code can output a number.

Every deterministic tool should state what it proves and, just as importantly, what it does **not** prove.

## Tests, evals, and field evidence

Use the smallest evidence layer capable of answering the question.

### Unit tests and CI

Use them for machine-decidable contracts only.

Examples:

- parser behavior;
- schema constraints;
- required references exist;
- deterministic script contracts;
- runtime/package boundaries;
- dependency integrity;
- syntax/compilation.

Avoid tests that freeze:

- exact prose;
- heading names without semantic need;
- source lists;
- author names;
- arbitrary counts;
- historical implementation details;
- framework vocabulary;
- approximate proxies treated as truth.

A test should protect a durable semantic or mechanical contract, not preserve how today's prompt happens to be written.

### Evals

Use evals for behavior and artifact quality.

Canonical principle:

```text
one distinct recurring causal failure -> one durable regression case
```

Do not create one eval per runtime sentence.

For a targeted behavioral change, run only cases capable of distinguishing that change. For a broad method or creative-system change, add the smallest representative benchmark that can expose regression outside the motivating case.

Judge observable routes, actions, questions, decisions, artifacts, evidence, and terminal state. Do not require private chain-of-thought.

When comparing revisions:

- define the failure or hypothesis first;
- define the observable that would distinguish improvement;
- compare baseline and candidate on the same case when practical;
- use blinded/pairwise judgment when quality is subjective;
- include holdout or representative cases for broad changes;
- record regressions and cost, not only wins;
- do not claim improvement when outputs are materially equivalent.

If the eval rewards exact wording, a template, or historical implementation rather than the desired behavior, fix the eval instead of bending runtime to pass it.

### Field evidence

Real use is stronger than synthetic confidence.

Use field evidence to detect:

- recurrence;
- false positives/blocks;
- host differences;
- context pressure;
- latency and operational cost;
- missing capabilities;
- unexpected environments;
- real failure modes not represented in synthetic evals.

Do not commit sensitive user traces. Preserve only deliberately curated, non-sensitive evidence.

## CI philosophy

Blocking CI should remain narrow and deterministic.

The repository contract is:

```bash
python development/validate.py
```

CI should prove only properties it can actually falsify with acceptable precision.

Do not add a CI check because a sentence says something is important. Add one when:

- the property is machine-decidable;
- failure would represent a real defect;
- the check has low false-positive risk;
- the maintenance/runtime cost is justified.

Do not make normal PR CI depend on volatile external `latest` platform behavior.

Compatibility monitoring belongs outside the core blocking loop and should be added only when an official or sufficiently stable external check produces useful signal.

## Distribution and releases

Source stays in Git. Generated transport artifacts leave Git.

Standalone Skills are distributed from the canonical `skills/<name>/` directory. When a downloadable bundle is useful, use the repository release workflow to archive that directory as-is.

Do not maintain a second explicit list of runtime files for packaging when the canonical directory already defines the runtime boundary.

Do not add per-Skill packagers unless a real Skill requires a transformation that cannot be expressed by the generic archive path.

Do not let release automation commit generated ZIPs, manifests, or derived metadata back to `main`.

## Platform changes

Platform surfaces change faster than capability semantics. Treat that volatility as an edge concern.

When ChatGPT, Claude, Gemini, DeepSeek, or another host changes:

1. determine whether the canonical Skill itself is still valid;
2. distinguish semantic incompatibility from installation/discovery/manifest/package change;
3. if only the edge changed, change only the edge;
4. prefer official/native Agent Skills support before creating custom adapters;
5. add platform-specific structure only after a real incompatibility demonstrates that the existing format cannot express the requirement;
6. never rewrite Skill semantics merely to satisfy a transient distribution surface.

The desired maintenance shape is closer to:

```text
number of capabilities + number of platforms
```

not:

```text
number of capabilities × number of platforms
```

## Documentation discipline

Documentation should help a human or agent make a decision that cannot be recovered cheaply from executable truth.

Do not maintain prose copies of facts already obvious from code or validation unless the explanation materially improves use.

The root README is the human entry point. `CONTRIBUTING.md` explains contributor workflow. This file instructs coding/maintenance agents. Unit-specific development READMEs should contain only information unique to that unit's development process.

When executable behavior and prose disagree, do not silently choose one. Identify the intended authority, fix the drift, and remove duplicate claims when possible.

## Working method for repository changes

For material work in this repository:

```text
UNDERSTAND
-> classify responsibility
-> inspect canonical runtime and existing evidence
-> define the concrete failure / need / hypothesis

DESIGN
-> choose the smallest responsible owner
-> preserve source-of-truth and dependency direction
-> avoid speculative axes
-> decide what evidence can actually validate the change

IMPLEMENT
-> change canonical source first
-> add deterministic enforcement only where justified
-> keep runtime portable and repository-independent

VERIFY
-> run targeted unit tests
-> run relevant evals when behavior changed
-> run python development/validate.py
-> inspect the diff for duplicated truth, accidental runtime payload, and platform coupling

DELIVER
-> state what changed
-> state what was actually verified
-> separate mechanical validation from behavioral claims
-> keep unresolved assumptions and revision conditions explicit
```

Do not use implementation as a substitute for understanding the problem.

## Review questions

Before declaring a change complete, ask:

### Ownership

- Is there exactly one canonical owner for each new meaning?
- Is the change in Skill, Agent, System, or Development for a reason rather than convenience?
- Did we create a new axis before enough real cases justify it?

### Runtime

- Can the runtime operate when installed without this repository?
- Did development material leak into runtime?
- Did host-specific vocabulary enter the core unnecessarily?
- Did permanent context grow without a demonstrated behavioral need?

### Evidence

- Are claims no stronger than the evidence?
- Does each deterministic test prove only what it can falsify?
- Did a behavioral change receive an eval capable of distinguishing it?
- Are we preserving an implementation detail merely because a test already exists?

### Architecture

- Is placement obvious?
- Does a local change remain local?
- Would deleting the capability remove a coherent region?
- Are dependency directions understandable?
- Is any abstraction empty or duplicated?

### Maintenance

- Will adding the next Skill require changing platform-specific code?
- Will adding the next platform require editing every existing Skill?
- Is any generated file becoming a second source of truth?
- Could a simpler structure preserve the same properties?

If the answer exposes unnecessary coupling or duplication, simplify before merging.

## Versioning

Version meaningful runtime contract changes in the owning runtime metadata.

Do not bump versions for development-only notes, eval reorganizations, or repository documentation unless they change the shipped behavior or installable contract.

A release version should describe the runtime being shipped, not repository activity around it.

## Change significance and restraint

Not every cleanup is an architecture change.

Prefer the smallest sufficient intervention:

- local defect -> local fix;
- repeated runtime defect -> repair the governing rule or reference;
- repeated deterministic defect -> strengthen executable enforcement;
- repeated placement/ownership confusion -> reconsider topology;
- real cross-platform incompatibility -> introduce the smallest edge adaptation;
- new irreducible responsibility -> only then introduce a new structural axis.

Do not turn every lesson into permanent instruction. Context is expensive. A new rule must earn its presence by changing decisions, preventing recurrence, or supplying knowledge that cannot be recovered cheaply at execution time.

## Definition of done

A repository change is complete when:

- the responsibility and placement are unambiguous;
- the canonical source of truth is singular;
- runtime remains independently installable;
- no unnecessary platform coupling was introduced;
- deterministic contracts that matter are enforced at the strongest reasonable layer;
- relevant unit tests pass;
- relevant behavioral evals were run when warranted;
- `python development/validate.py` passes;
- documentation does not contradict executable behavior;
- claims are bounded by the evidence actually obtained;
- remaining assumptions, limitations, or revision triggers are explicit.

The goal is not maximal structure, maximal documentation, maximal testing, or maximal portability machinery. The goal is a repository whose capabilities remain **clear, portable, generative, verifiable, easy to change, and hard to accidentally fork or drift** as the ecosystem evolves.
