---
name: research-map
description: Memory and navigation across sessions for a research project. Keeps one RESEARCH.map per research — question, hypotheses, gate states, facts that were once wrong, provenance, verification commands, open decisions — read at session start (resume), written at session end (update), built once (init) and checked mechanically (validate). Use /research-map <init|resume|update|validate>.
license: CC-BY-NC-4.0
metadata:
  version: 0.1.0
argument-hint: 'init|resume|update|validate [path to RESEARCH.map]'
---

# Research map

Nothing an agent learns persists past the session unless it is written where the next
session reads first. `RESEARCH.map` is that place: an operational index of one research,
pointing at the protocol, notebooks and aggregates that are the truth, never a second copy
of them. The repository stays the source of truth; the map says where it is and what state
it is in.

## The map

One file per research, Markdown, fixed sections in this order. The full grammar and an
example are in `reference/map-schema.md`; a blank one is in `templates/RESEARCH.map`.

| Section | Holds |
|---|---|
| `## Layout` | where things are: `protocol`, `decisions`, `aggregates`, `documents`, `notebooks`, `references` |
| `## Question` | one line, with a pointer into the protocol |
| `## Hypotheses` | one line each, prediction and refutation, terminal state, pointer |
| `## Gates` | one row per phase: `reached` / `pending` / `blocked` and by whom |
| `## Facts that were once wrong` | the wrong value, the right value, the notebook that now produces it — the most valuable block |
| `## Provenance` | each input, its location in the cache, the notebook that reads it |
| `## Verification` | the commands that re-run the notebooks in order, render the paper, run hooks, verify citations |
| `## Open decisions` | what is undecided and who unblocks it |
| `## Last session` | what changed, in five lines |

Pointers are backticked paths relative to the repository root, optionally with `#anchor`.
`validate` resolves every one of them.

## Modes

### `init`

Build the map from an existing protocol and decision log. Read them; fill every section
from what they say, never from memory; leave `Facts that were once wrong` empty rather than
inventing history. Write `Layout` first — everything else depends on it. Copy
`scripts/validate.py` into the repository (suggested: `tools/research_map_validate.py`) so
the repository can run it from pre-commit without depending on where this capability is
installed. Finish by running `validate`.

### `resume` — session start

Read the map. Restate the state in one screen, in this order: the next action; gates and
their states; hypotheses with terminal states; facts that were once wrong; open decisions
and who unblocks each; what changed last session. The reader cannot hold "step 3 of 5"
between messages — the agent is that reader. Then run `validate` and report its result
before any other work; a `FAIL` is the first item of the session.

### `update` — session end, obligatory

Rewrite `Last session` (five lines: what changed, what is next). Update `Gates`,
`Hypotheses` and `Open decisions` to match what the protocol and decision log now say. Add
to `Facts that were once wrong` any number this session corrected, with the notebook that
now produces it. Run `validate`; do not end the session on a `FAIL` without recording it
under `Open decisions`.

### `validate` — mechanical, before any commit

```bash
python scripts/validate.py RESEARCH.map            # from the installed capability
python tools/research_map_validate.py RESEARCH.map # the copy `init` placed in the repository
```

Checks, each reported `PASS`, `FAIL` or `NOT_VERIFIED` with the offending lines:

| Check | Rule |
|---|---|
| `map` | required sections present and in order; every pointer resolves; gate states valid; every fact-once-wrong has a producing notebook |
| `numbers` | every number quoted in the `documents` exists in a committed aggregate under `aggregates`, at the quoted precision |
| `decisions` | every `D-<n>` in `decisions` has a `Revision condition:`; ids unique and increasing |
| `citations` | every DOI or URL in `references` resolves (`NOT_VERIFIED` with `--offline`) |
| `notebooks` | no committed notebook under `notebooks` carries outputs or execution counts |

Exit code is non-zero on any `FAIL`; `--strict` also fails on `NOT_VERIFIED`. As a
pre-commit hook in the consuming repository:

```yaml
repos:
  - repo: local
    hooks:
      - id: research-map-validate
        name: research-map validate
        entry: python tools/research_map_validate.py RESEARCH.map --offline
        language: system
        pass_filenames: false
```

A number the checker cannot find is reported, not silently accepted. A line that
legitimately carries a number with no aggregate (a year in a citation, a page number) is
marked `<!-- rm:ignore -->` on the same line; the marker is a decision and is visible in
the diff.

## Session ritual

Open by reading; close by writing; lead every report with the next action and end with one
concrete next step; no closing pleasantries. `resume` without a following `update` in the
same session is a defect the next `resume` reports (`Last session` will be stale).

## What this is not

Not a copy of the protocol, not a changelog, not a place for results. A number belongs in
an aggregate; a decision in the decision log; the map points at both.
