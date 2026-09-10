# research

Agent skills for scientific research: method, memory across sessions, and adversarial
review. A **system**: one install, several pieces that work together and are versioned
separately.

## Status

**Built, acceptance pending** (plugin 0.5.0, pieces 0.4.0, 2026-09-10). All three pieces
exist and pass the repository's structural checks and unit tests. Two things are not yet
done, and the pieces say so themselves:

- the method sources behind `reference/` were *located* (publisher landing page or DOI
  found with matching metadata) but not *read* at source, because the build environment
  blocked scholarly domains; `development/research/design/sources-verified.md` records the
  level per source and is the first thing to upgrade in a session with network access;
- no behavioural run has been recorded against `development/research/evals/`; acceptance
  is by retro-test on the origin case (roadmap step 7).

The consolidated design, the references it draws on, the origin case and the roadmap live
in `development/research/design/`.

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

There is one entry point for the method: **`scientific-method`**. You talk to it; it
decides which other piece owns the next step and calls `explorer` and `reviewer-2` for you.
The one piece you also call yourself is `research-map`, the session ritual below. Plugin
skills are namespaced; the short form works when no other skill has the same name.

```text
/research:scientific-method <what you want to do with this research>
```

The skill also fires on its own when it recognises a phase trigger: you are about to fit
a model, about to cite, about to write a results paragraph, about to compute a number that
will leave the analysis environment.

### A research from the start

```text
/research:scientific-method start: does state habilitação correct or amplify the geography of
community kitchens relative to municipal food insecurity?
```

Phase 1 writes the problem statement first — claim kind, unit of analysis, estimand,
refutation, the obvious objection, who cares, non-goals — as a section of the protocol that
`validate` checks field by field; then it delegates to `explorer`: a portfolio of hypothesis
lineages, each with a bridge certificate. Each surviving lineage becomes a hypothesis; its discriminating test becomes
the primary test, its failure condition the refutation clause. The phase closes when the
question is written with its refutation and the obvious reviewer objection is named.
Then literature (every source verified at its DOI), protocol (prediction and refutation
per hypothesis, one primary test each, assumptions → check → fallback per model,
equivalence bounds fixed before any test), and so on. Every phase ends with a gate that
can fail; every hypothesis ends in a named state: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`,
`BLOCKED`, `NOT_VERIFIED`.

### Every session

`research-map` keeps one `RESEARCH.map` per research: question and registration status,
hypotheses, state per gate, **facts that were once wrong** with the notebook that now
produces them, provenance of every input, verification commands, open decisions and who
unblocks each.

```text
/research:research-map resume     # before the first action: restate the state in one screen
/research:research-map update     # after any gate, state or number changes, and before a commit
/research:research-map validate   # before any commit; also runnable as a pre-commit hook
```

`validate` is mechanical: a number quoted in a document that no committed aggregate
contains is reported (presence, not provenance — the source table is still required),
every decision has a revision condition, every citation resolves, no committed notebook
has outputs, every pointer in the map resolves, registration status is declared. A check
with nothing to examine says `NOT_VERIFIED`, never `PASS`.

`/research:research-map init` builds the map once from an existing protocol and decision
log and copies the validator into the repository for pre-commit.

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
/research:scientific-method review paper/manuscript.qmd
```

Phase 7 hands the manuscript to `reviewer-2`, an independent, non-editing agent that
treats the author's text as untrusted narrative and looks for the falsifying observation
first: forking paths, a number without interval or source table, causal language in an
ecological design, a figure that does not match its code or data, a citation that does not
say what it is cited for. It returns fixed headings: `VERDICT` (`PASS` / `FAIL` /
`NOT_VERIFIED`), `CLAIMS`, `FINDINGS`, `CHECKS RUN`, `NOT_VERIFIED`, `BASIS`. The gate
passes when every `FAIL` has a logged response.

### When a new idea appears mid-way

```text
Apareceu um método novo, acho que a gente devia testar também.
```

Opening is cheap only before the protocol freezes; phase 1 opens wide, on a logged budget,
and converges to at most three hypotheses. After the freeze, "we should also test X" has
four destinations and the skill routes it: a specification-curve dimension (absorbed), a
labelled exploratory analysis, the map's `## Deferred` with the condition under which it
would enter (the default), or reopening phase 3 by a decision that names what leaves.
`resume` shows the count of open hypotheses and deferred items every session.

### What it never does

Invent a human-owned decision: what question matters, which institution to call, what a
field term means in practice, authorship, ethics approval, venue. A missing capability or
decision degrades to `BLOCKED` or `NOT_VERIFIED`, never to a guess.

## Pieces

| Piece | Kind | Owns |
|---|---|---|
| scientific-method | skill, entry point | the research lifecycle: problem → literature → protocol → data → analysis → writing → review → publication, each phase with an exit gate; distilled, source-verified method knowledge in `reference/` (design record §2, in `development/research/design/`) |
| research-map | skill | memory and navigation across sessions: `RESEARCH.map`, modes `init`, `resume`, `update`, `validate` (design record §3) |
| reviewer-2 | agent | independent, non-editing review of a manuscript against its own protocol and reporting checklists (design record §4) |
| explorer | skill, dependency | phase 1: hypothesis portfolio with bridge certificates; a standalone unit at `skills/explorer/`, pulled in by `dependencies` |

## Where things live

| What | Path |
|---|---|
| plugin manifest (name, version, dependencies) | `systems/research/.claude-plugin/plugin.json` |
| `scientific-method` kernel and one reference per phase | `systems/research/skills/scientific-method/` |
| `research-map` kernel, map grammar, blank map, `validate` script | `systems/research/skills/research-map/` |
| `reviewer-2` agent | `systems/research/agents/reviewer-2.md` |
| design, references studied, sources verified, origin case, roadmap | `development/research/design/` |
| evaluation scenarios and the adversarial fixture generator | `development/research/evals/` |
| unit tests (`validate` script; reference shape) | `development/research/tests/` |

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
