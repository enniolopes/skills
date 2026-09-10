# research

Agent skills for scientific research: method, memory across sessions, and adversarial
review. A **system**: one install, several pieces that work together and are versioned
separately.

## Status

**Design stage.** The plugin installs today but carries no piece yet, only its dependency
on `explorer`. The consolidated design, the references it draws on, the origin case that
motivated it and the build order live in `development/research/design/`. Each piece's
contract is written there in prose; its runtime files appear in `skills/` and `agents/`
of this directory as they are built (`development/research/design/roadmap.md`). This
README states how the system is meant to be used; the build must honor it.

## Install

One command, in Claude Code:

```text
/plugin marketplace add enniolopes/skills
/plugin install research@enniolopes
```

That installs `scientific-method`, `research-map`, the `reviewer-2` agent and, through the
plugin's `dependencies`, the standalone `explorer` skill. Later, `/plugin update research`
brings new pieces as they ship.

## How to use

There is one entry point: **`scientific-method`**. You talk to it; it decides which other
piece owns the next step. You normally do not invoke `explorer`, `research-map` or
`reviewer-2` yourself.

```text
/scientific-method <what you want to do with this research>
```

The skill also fires on its own when it recognises a phase trigger: you are about to fit
a model, about to cite, about to write a results paragraph, about to compute a number that
will leave the analysis environment.

### A research from the start

```text
/scientific-method start: does state habilitação correct or amplify the geography of
community kitchens relative to municipal food insecurity?
```

Phase 1 delegates to `explorer`: a portfolio of hypothesis lineages, each with a bridge
certificate. Each surviving lineage becomes a hypothesis; its discriminating test becomes
the primary test, its failure condition the refutation clause. The phase closes when the
question is written with its refutation and the obvious reviewer objection is named.
Then literature (every source verified at its DOI), protocol (prediction and refutation
per hypothesis, one primary test each, assumptions → check → fallback per model,
equivalence bounds fixed before any test), and so on. Every phase ends with a gate that
can fail; every hypothesis ends in a named state: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`,
`BLOCKED`, `NOT_VERIFIED`.

### Every session

`research-map` keeps one `RESEARCH.map` per research: question and hypotheses, state per
gate, **facts that were once wrong** with the notebook that now produces them, provenance
of every input, verification commands, open decisions and who unblocks each.

```text
/research-map resume     # session start: restate the state in one screen
/research-map update     # session end: what changed, what is next — obligatory
/research-map validate   # before any commit; also runnable as a pre-commit hook
```

`validate` is mechanical: every number quoted in a `.md` exists in a committed aggregate,
every decision has a revision condition, every citation resolves, no committed notebook
has outputs, every pointer in the map resolves.

`/research-map init` builds the map once from an existing protocol and decision log.

### The moment before a mistake

```text
Vou ajustar um modelo hurdle para o número de cozinhas por município.
```

`scientific-method` recognises a phase-5 trigger and, before any fit, requires the list of
assumptions, the check for each and the fallback if a check fails (invariant 5). It asks
the dependence structure of the outcome before any interval is reported. It refuses a
number that did not come out of executed code in the current repository state.

### Review

```text
/scientific-method review paper/manuscript.qmd
```

Phase 7 hands the manuscript to `reviewer-2`, an independent, non-editing agent that
treats the author's text as untrusted narrative and looks for the falsifying observation
first: forking paths, a number without interval or source table, causal language in an
ecological design, a figure that does not match its code or data, a citation that does not
say what it is cited for. It returns fixed headings: `VERDICT` (`PASS` / `FAIL` /
`NOT VERIFIED`), `CLAIMS`, `FINDINGS`, `CHECKS RUN`, `NOT VERIFIED`, `BASIS`. The gate
passes when every `FAIL` has a logged response.

### What it never does

Invent a human-owned decision: what question matters, which institution to call, what a
field term means in practice, authorship, ethics approval, venue. A missing capability or
decision degrades to `BLOCKED` or `NOT_VERIFIED`, never to a guess.

## Pieces

| Piece | Kind | Owns |
|---|---|---|
| scientific-method | skill, entry point | the research lifecycle: problem → literature → protocol → data → analysis → writing → review → publication, each phase with an exit gate; distilled, source-verified method knowledge in `reference/` (`research-skills-system.md` §2) |
| research-map | skill | memory and navigation across sessions: `RESEARCH.map`, modes `init`, `resume`, `update`, `validate` (§3) |
| reviewer-2 | agent | independent, non-editing review of a manuscript against its own protocol and reporting checklists (§4) |
| explorer | skill, dependency | phase 1: hypothesis portfolio with bridge certificates; a standalone unit at `skills/explorer/`, pulled in by `dependencies` |

## Where things live

| What | Path |
|---|---|
| plugin manifest (name, version, dependencies) | `systems/research/.claude-plugin/plugin.json` |
| runtime pieces, as built | `systems/research/skills/<piece>/`, `systems/research/agents/<piece>.md` |
| design, references studied, origin case, roadmap | `development/research/design/` |
| evaluation scenarios (regression, adversarial, holdout) | `development/research/evals/scenarios.json` |

## Principles

1. The research repository is the source of truth; skills say *how to decide* and *where
   to record*, never *what was decided*.
2. Evidence is something read or run against an identified target; confidence is not
   evidence. A number that did not come out of executed code is not a result.
3. Phases end with gates that can fail. What cannot fail is not a gate.
4. Mechanical checks before judgement: if a script can verify it, the script does.
5. Method knowledge is distilled, source-verified and dated. Nothing enters `reference/`
   from memory.
6. Inconclusive is a legitimate terminal state and has a name.
7. Acceptance is by retro-test: a skill is ready when, applied to the origin case as it
   stood before the audit, it produces the audit's findings before a human does.

## Origin

Designed during the `delbem-research/cozsolidarias-research` project (September 2026),
where a method audit found ten defects in an already-careful pipeline and a session
boundary let wrong numbers survive. Both are recorded in
`development/research/design/origin-case.md` as the first evaluation scenarios.
