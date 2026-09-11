---
name: research-map
description: Memory and navigation across sessions for a research project. Keeps one RESEARCH.map per research — question, registration status, hypotheses, gate states with their evidence, deferred ideas, last session — read before the first action of a session (resume), written after any gate, state or number changes (update), built once (init) and checked mechanically before every commit (validate). Use /research:research-map <init|resume|update|validate>.
when_to_use: Triggers include the start of any session in a repository that has a RESEARCH.map, "onde parei", "resume", "o que mudou", "antes de commitar", "validate", "esse número está certo?", "de onde veio esse número", "atualiza o mapa", "como organizo a pasta da pesquisa".
license: CC-BY-NC-4.0
metadata:
  version: 0.6.0
argument-hint: 'init|resume|update|validate [path to RESEARCH.map]'
---

# Research map

Nothing an agent learns persists past the session unless it is written where the next
session reads first. `RESEARCH.map` is that place: an operational index of one research,
pointing at the protocol, notebooks and aggregates that are the truth, never a second copy
of them. The repository stays the source of truth; the map says where it is and what state
it is in.

## The map

One file per research, Markdown, fixed sections in this order. Six are required — the
state no other file holds; four are optional and hold only what no file in `Layout`
already says (if the README or the protocol says it, point, never copy). The grammar and
an example are in `reference/map-schema.md`; a blank one is in `templates/RESEARCH.map`.

| Section | Holds |
|---|---|
| `## Layout` | where things are: `protocol`, `decisions`, `aggregates`, `documents`, `notebooks`, `references`; `floor`, the minimum cell size for anything under `documents` |
| `## Question` | one line with a pointer to the protocol's problem statement (seven required fields, checked); `Problem: PENDING \| SHOWN \| NOT_SHOWN \| INCONCLUSIVE → \`<problem-brief.md>\`` (the brief's seven fields, its Verdict and the decision its Reference names are checked; no gate ≥ 3 is reached before `SHOWN`); `Registration: none \| <URL or DOI, date>` — while `none`, confirmatory code is `DRY_RUN` |
| `## Hypotheses` | one row each: prediction, refutation, terminal state, pointer; at most three without a terminal state |
| `## Gates` | one row per phase, all eight: `reached` / `pending` / `blocked`; a `blocked` row names who unblocks it, a `reached` row names its **evidence** — the artifact the gate produced, as a pointer or DOI |
| `## Facts that were once wrong` (optional) | the wrong value, the right value, the notebook that now produces it |
| `## Provenance` (optional) | inputs the README or protocol do not already list |
| `## Verification` (optional) | the commands, when no Makefile or README holds them |
| `## Open decisions` (optional) | what is undecided and not already a `blocked` gate row |
| `## Deferred` | ideas, methods and fronts that appeared after the freeze and were not admitted: `- YYYY-MM-DD: <idea> — enters when: <condition>`; the destination for "we should also test X" |
| `## Last session` | a dated line per change and one `Next:` line |

Backticks in the map are reserved for pointers: repository-relative paths, optionally with
`#anchor`; `validate` resolves every one of them.

## Modes

### `init`

Build the map from an existing protocol and decision log. Read them; fill every section
from what they say, never from memory. Write `Layout` first — everything else depends on
it, and it is the whole answer to "how should this research be organised": six paths and a
floor, nothing about packages, tests or build systems. Every gate starts `pending`; a gate
becomes `reached` only when its evidence artifact exists and is pointed to — a research
that already has a protocol has the protocol, not a certified past. Leave optional
sections out rather than copying what the README already says; leave `Facts that were once
wrong` empty rather than inventing history. Finish by running `validate`.

### `resume` — before the first action of a session

Read the map. Restate the state in one screen, in this order: the next action; gates and
their states; the problem's state (`SHOWN` or not, and why); registration status;
hypotheses with terminal states, and the count without one (more than three is a scope
finding); open decisions and who unblocks each; deferred items, as a count and the one
whose entry condition is closest; what changed last session. The reader cannot hold "step
3 of 5" between messages — the agent is that reader. Then run `validate` and report its
result before any other work; a `FAIL` is the first item of the session.

### `update` — after any change of state

Nothing signals "the end of the session", so `update` is bound to observable events: a gate
changed, a hypothesis changed terminal state, a number was corrected, registration
happened, a commit is about to be made. On each: add a dated line to `Last session` and
rewrite its `Next:`; make `Gates` (state and evidence), `Hypotheses` and `Registration`
match what the protocol and decision log now say; add any corrected number to `Facts that
were once wrong` with the notebook that now produces it. Run `validate`; a `FAIL` that
cannot be fixed now is recorded under `Open decisions`. A `resume` that finds `Last
session` older than the last commit reports the missed `update` as its first finding.

### `validate` — mechanical, before any commit

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/validate.py" RESEARCH.map --offline
```

The script lives with this capability and runs from where it is installed; the consuming
repository carries no copy. `${CLAUDE_SKILL_DIR}` resolves when the skill is invoked; if
the path is not resolved, the skill was read, not invoked — invoke it. A repository that
wants a pre-commit hook points the hook at that installed path; the hook is the
repository's business, `validate` before every commit is this skill's.

Six checks, each `PASS`, `FAIL` or `NOT_VERIFIED` with the offending lines; the rules are
in `reference/map-schema.md`: `map` (structure, pointers, gates with evidence, the
hypotheses cap, registration, problem statement and problem brief fields, the
problem-before-protocol rule), `numbers` (a number quoted in a document that no aggregate
contains at the quoted precision is reported — a match is presence, not provenance; the
source table is still required), `decisions` (title, non-empty revision condition and
`Supersedes` per `D-<n>` block; ids unique and increasing; decision ids in table rows
counted and reported as not checked), `disclosure` (no count cell under `documents` below
`floor`), `citations` (resolution; `NOT_VERIFIED` with `--offline`), `notebooks` (no
outputs). A check with nothing to examine reports `NOT_VERIFIED`, never `PASS`. Exit code
is non-zero on any `FAIL`; `--strict` also fails on `NOT_VERIFIED`.

A number the checker cannot find is reported, not silently accepted. A line that
legitimately carries a number with no aggregate is marked `<!-- rm:ignore: <reason> -->`
on the same line; the reason is required, the summary counts the markers, and the marker
is visible in the diff. Deleting the number instead is a change to what the document
claims, and is said in the report line.

## What this is not

Not a copy of the protocol, not a changelog, not a place for results, not a build system.
A number belongs in an aggregate; a decision in the decision log; the map points at both.
