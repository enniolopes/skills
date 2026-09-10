# research

Agent skills for scientific research: method, memory across sessions, and adversarial
review. A **system**: several pieces, installed separately, designed to work together.
`system.json` is the composition; CI checks it against the repository.

## Status

**Design stage.** No piece of this system is installable yet. The consolidated design, the
references it draws on, the origin case that motivated it and the build order live in
`development/research/design/`. Each piece's contract is written there in prose; its
runtime files appear in `skills/` or `agents/` when built (see
`development/research/design/roadmap.md`).

## Pieces

Versioned separately because they change at different rates.

| Piece | Kind | Owns |
|---|---|---|
| scientific-method | skill | the research lifecycle: problem → literature → protocol → data → analysis → writing → review → publication, each phase with an exit gate; distilled, source-verified method knowledge in `reference/` (`research-skills-system.md` §2) |
| research-map | skill | memory and navigation across sessions: an operational index per research (`RESEARCH.map`), read at session start, updated at session end, validated mechanically (`init`, `resume`, `update`, `validate`) (§3) |
| reviewer-2 | agent | independent, non-editing review of a manuscript against its own protocol and reporting checklists; treats the author's text as untrusted narrative; fixed output headings (`VERDICT`, `CLAIMS`, `FINDINGS`, `CHECKS RUN`, `NOT VERIFIED`, `BASIS`) (§4) |
| explorer | skill, dependency | phase 1: hypothesis portfolio with bridge certificates; shipped standalone in `skills/explorer/` |

`scientific-method` declares `explorer` as a dependency for its first phase and does not
reimplement it.

## Where things live

| What | Path |
|---|---|
| composition and status per piece | `systems/research/system.json` |
| design, references studied, origin case, roadmap | `development/research/design/` |
| evaluation scenarios (regression, adversarial, holdout) | `development/research/evals/scenarios.json` |
| runtime pieces, once built | `skills/<piece>/`, `agents/<piece>.md` |

## Install (once built)

```bash
npx skills add enniolopes/skills --skill scientific-method --agent claude-code
npx skills add enniolopes/skills --skill research-map --agent claude-code
npx skills add enniolopes/skills --skill explorer --agent claude-code
```

Consuming research repositories pin versions in their `skills-lock.json`.

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
