---
name: research-map
description: Memory and navigation across sessions for a research project. Keeps one RESEARCH.map per research — question, registration status, hypotheses, gate states, facts that were once wrong, provenance, verification commands, open decisions, deferred ideas — read before the first action of a session (resume), written after any gate, state or number changes (update), built once (init) and checked mechanically before every commit (validate). Use /research:research-map <init|resume|update|validate>.
when_to_use: Triggers include the start of any session in a repository that has a RESEARCH.map, "onde parei", "resume", "o que mudou", "antes de commitar", "validate", "esse número está certo?", "de onde veio esse número", "atualiza o mapa".
license: CC-BY-NC-4.0
metadata:
  version: 0.5.0
argument-hint: 'init|resume|update|validate [path to RESEARCH.map]'
---

# Research map

Nothing an agent learns persists past the session unless it is written where the next
session reads first. `RESEARCH.map` is that place: an operational index of one research,
pointing at the protocol, notebooks and aggregates that are the truth, never a second copy
of them. The repository stays the source of truth; the map says where it is and what state
it is in.

## The map

One file per research, Markdown, fixed sections in this order. The grammar and an example
are in `reference/map-schema.md`; a blank one is in `templates/RESEARCH.map`.

| Section | Holds |
|---|---|
| `## Layout` | where things are: `protocol`, `decisions`, `aggregates`, `documents`, `notebooks`, `references` |
| `## Question` | one line with a pointer to the protocol's problem statement (seven required fields, checked); `Problem: PENDING \| SHOWN \| NOT_SHOWN \| INCONCLUSIVE → \`<problem-brief.md>\`` (the brief's seven fields and its Verdict are checked; no gate ≥ 3 is reached before `SHOWN`); `Registration: none \| <URL or DOI, date>` — while `none`, confirmatory code is `DRY_RUN` |
| `## Hypotheses` | one row each: prediction, refutation, terminal state, pointer |
| `## Gates` | one row per phase, all eight: `reached` / `pending` / `blocked` and by whom |
| `## Facts that were once wrong` | the wrong value, the right value, the notebook that now produces it — the most valuable block |
| `## Provenance` | each input, its location in the cache, the notebook that reads it |
| `## Verification` | the commands that re-run the notebooks in order, render the paper, run hooks, verify citations |
| `## Open decisions` | what is undecided and who unblocks it |
| `## Deferred` | ideas, methods and fronts that appeared after the freeze and were not admitted: `- YYYY-MM-DD: <idea> — enters when: <condition>`; the destination for "we should also test X" |
| `## Last session` | a dated line per change and one `Next:` line |

Backticks in the map are reserved for pointers: repository-relative paths, optionally with
`#anchor`; `validate` resolves every one of them.

## Modes

### `init`

Build the map from an existing protocol and decision log. Read them; fill every section
from what they say, never from memory; leave `Facts that were once wrong` empty rather than
inventing history. Write `Layout` first — everything else depends on it. Copy the validator
into the repository so pre-commit does not depend on where this capability is installed:

```bash
cp "${CLAUDE_SKILL_DIR}/scripts/validate.py" tools/research_map_validate.py
```

Finish by running `validate`.

### `resume` — before the first action of a session

Read the map. Restate the state in one screen, in this order: the next action; gates and
their states; the problem's state (`SHOWN` or not, and why); registration status; hypotheses with terminal states, and the count without
one (more than three is reported as a scope finding); facts that were once wrong; open
decisions and who unblocks each; deferred items, as a count and the one whose entry
condition is closest; what changed last session. The reader cannot
hold "step 3 of 5" between messages — the agent is that reader. Then run `validate` and
report its result before any other work; a `FAIL` is the first item of the session.

### `update` — after any change of state

Nothing signals "the end of the session", so `update` is bound to observable events: a gate
changed, a hypothesis changed terminal state, a number was corrected, registration
happened, a commit is about to be made. On each: add a dated line to `Last session` and
rewrite its `Next:`; make `Gates`, `Hypotheses`, `Open decisions` and `Registration` match
what the protocol and decision log now say; add any corrected number to `Facts that were
once wrong` with the notebook that now produces it. Run `validate`; a `FAIL` that cannot be
fixed now is recorded under `Open decisions`. A `resume` that finds `Last session` older
than the last commit reports the missed `update` as its first finding.

### `validate` — mechanical, before any commit

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/validate.py" RESEARCH.map        # from the installed capability
python3 tools/research_map_validate.py RESEARCH.map                   # the copy `init` placed in the repository
```

Five checks, each `PASS`, `FAIL` or `NOT_VERIFIED` with the offending lines; the rules are
in `reference/map-schema.md`: `map` (structure, pointers, gates, registration, problem statement and problem brief fields, the problem-before-protocol rule), `numbers`
(a number quoted in a document that no aggregate contains at the quoted precision is
reported — a match is presence, not provenance; the source table is still required),
`decisions` (revision condition per `D-<n>`, ids unique and increasing), `citations`
(resolution; `NOT_VERIFIED` with `--offline`), `notebooks` (no outputs). A check with
nothing to examine reports `NOT_VERIFIED`, never `PASS`.

Exit code is non-zero on any `FAIL`; `--strict` also fails on `NOT_VERIFIED`. As a
pre-commit hook in the consuming repository:

```yaml
repos:
  - repo: local
    hooks:
      - id: research-map-validate
        name: research-map validate
        entry: python3 tools/research_map_validate.py RESEARCH.map --offline
        language: system
        pass_filenames: false
```

A number the checker cannot find is reported, not silently accepted. A line that
legitimately carries a number with no aggregate is marked `<!-- rm:ignore -->` on the same
line; the marker is a decision and is visible in the diff.

## What this is not

Not a copy of the protocol, not a changelog, not a place for results. A number belongs in
an aggregate; a decision in the decision log; the map points at both.
