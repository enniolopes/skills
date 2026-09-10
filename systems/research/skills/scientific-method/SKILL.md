---
name: scientific-method
description: Run an empirical research project as a lifecycle with gates — problem, literature, protocol, data, analysis, writing, review, publication — for observational quantitative studies on administrative data. Use it to start a research, to check which gate you are at, to review a manuscript, and whenever you are about to fit a model, cite a source, report a number or write results. Delegates hypothesis generation to explorer, session memory to research-map, and review to the reviewer-2 agent.
when_to_use: Triggers include "vou ajustar/rodar o modelo", "let me fit", "vou citar", "escrever os resultados", "deu/não deu efeito", "no effect", "qual o intervalo", "definir a amostra/população", "o raio de 500 m", "os dois resultados discordam", "pré-registro", "protocolo", "hipótese", "revisar o manuscrito", "submeter o artigo".
license: CC-BY-NC-4.0
metadata:
  version: 0.2.0
argument-hint: '<start | phase | review <manuscript> | what you are about to do>'
---

# Scientific method

Own the lifecycle of an empirical research project and the quality of its artifacts. The
model already knows the statistics; what fails is applying the right discipline at the
right moment. This capability supplies the moment.

Scope of this version: observational quantitative research with administrative data. Other
designs may use the invariants; the phase references are written for this scope.

## Arguments

- `start <question>` → phase 1, then onward.
- `phase` → report the current phase and gate from the research map, nothing else.
- `review <path>` → phase 7 on that manuscript.
- anything else → match it against the phase table below; if it matches no trigger, say so
  and ask which phase is meant.

Every response ends with one report line, always this shape:

```text
Phase <n> <name> · Gate: PASS | FAIL — <unmet criterion> · states changed: <H1 → INCONCLUSIVE, …> · decisions: <D-n, …> · next: <one concrete step>
```

## Ownership

Owns: phases, gates, terminal states, the quality of protocol, data, analysis, manuscript
and deposit. Does **not** own domain judgement (which question matters, which institution
to call, what a field term means in practice), authorship, ethics approval, or the choice
of venue. Those belong to humans and are never invented; when one is missing the state is
`BLOCKED`, named, with who unblocks it.

## Invariants

1. **The protocol is the source of truth.** Paper, abstract, registration text, slides and
   e-mails are projections of it, regenerated from it, never edited into disagreement.
2. **Evidence is something read or run against an identified target.** A number that did
   not come out of executed code in the current repository state is a claim, not a result.
3. **Every hypothesis carries a prediction and a refutation condition** before any
   confirmatory analysis runs. One primary test per hypothesis.
4. **Exploratory and confirmatory are separated by an artifact, not by intent**: a public
   registration recorded in the research map, and confirmatory code that runs only with
   the outcome permuted (`DRY_RUN`) while `Registration: none`.
5. **Every model lists assumptions → check → fallback before fitting.** A fallback chosen
   after seeing residuals is a forking path.
6. **Bounds for any "no effect" claim are fixed before the test.**
7. **Every analytic choice that could reasonably have gone another way is a
   specification-curve dimension**, not a footnote.
8. **Every linkage step reports match rates and errors. Every aggregate that leaves the
   analysis environment respects the disclosure floor** the repository sets.
9. **Every citation is verified at its DOI record or landing page before it is written**;
   a finding read only from an excerpt is marked as such.
10. **Every methodological decision is logged** with date, rationale and revision
    condition; the log is append-only.
11. **Terminal states are named**: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`
    (missing human decision or data), `NOT_VERIFIED` (a check could not run). Silence is
    not a state.
12. **A missing capability degrades explicitly** to `NOT_VERIFIED` or `BLOCKED`, never to a
    guess.

## Memory across sessions

`research:research-map` owns it. Run its `resume` before the first action of a session,
its `validate` before any commit, and its `update` after any gate change, terminal-state
change or corrected number — not "at the end", which nothing signals. If the skill is not
listed, run its script directly; never narrate a resume or update you did not perform.

## Phases

Each phase has an entry trigger, a procedure (in `reference/`), an exit gate that can fail,
and terminal states. Read the phase file when the phase is entered or when its trigger
fires; do not read all eight at once. When a trigger fires implicitly, say which phase
fired and apply its requirements **before** doing the thing.

| # | Phase | Trigger (what the conversation shows) | Exit gate | Read |
|---|---|---|---|---|
| 1 | Problem | a research starts, restarts or gains a hypothesis | question written with its refutation; unit of analysis fixed; obvious reviewer objection named | `reference/01-problem.md` |
| 2 | Literature | a citation is about to be typed; a claim about the state of knowledge | verification log complete (each source at DOI, or `NOT_VERIFIED` and not in the text); gap in one paragraph | `reference/02-literature.md` |
| 3 | Protocol | hypotheses, tests, populations or thresholds set or changed; a round-number threshold or radius proposed; "no effect" planned | protocol frozen; registration text derived; assumption tables, bounds and dimensions listed | `reference/03-protocol.md` |
| 4 | Data | an input enters; sources are joined; a population or pool is named for the first time; an aggregate leaves | linkage report per join; provenance per input; no identifiable row outside the cache | `reference/04-data.md` |
| 5 | Analysis | "vou ajustar / rodar o modelo", "let me fit"; an interval or statistic about to be reported; two results disagree | assumptions → check → fallback listed before fitting; dependence structure asked; `DRY_RUN` status confirmed; every pre-specified check has a result; terminal state per hypothesis; discordance reported and the primary test decides | `reference/05-analysis.md` |
| 6 | Writing | a number is about to be written into prose; any prose that will leave the repository | every number exists in a committed aggregate with interval and source table; figure provenance; definitions with misreadings | `reference/06-writing.md` |
| 7 | Review | before submission; after any confirmatory run on demand; `review <path>` | reviewer verdict `PASS`, or every `FAIL` has a logged response and re-run checks | `reference/07-review.md` |
| 8 | Publication | anything leaves for a venue, funder or repository of record | DOIs recorded in the protocol; DMP and AI declaration in the venue's shape; PII check passed | `reference/08-publication.md` |

Phases are ordered by dependency, not ceremony. A later phase may send work back to an
earlier one (a review finding that changes a number reopens phase 6; a new hypothesis
reopens phases 1 and 3). Skipping a phase is a logged decision with a revision condition,
never silence.

## Delegation

- **`explorer`** (skill; `explorer:explorer` when installed from the marketplace, pulled in
  as a dependency) — phase 1: hypothesis portfolio with bridge certificates. Each surviving
  lineage's discriminating test becomes the primary test; its failure condition becomes
  the refutation clause.
- **`research:research-map`** (skill) — memory across sessions, above. Its `validate` is
  the mechanical half of invariants 2, 9 and 10.
- **`research:reviewer-2`** (agent) — phase 7 and on demand. Supply the brief exactly as its
  "Required brief" section lists it, checklist included. It does not edit and does not
  inherit your reasoning.

If a delegate is not installed, do not simulate it: mark the step `NOT_VERIFIED` and name
what is missing.

## Decision log entry

Every methodological decision, appended to the repository's decision log, in this shape
(the map's `validate` requires the heading and the revision condition):

```text
### D-<n> · <YYYY-MM-DD>
Decision: <what was decided>
Rationale: <why; evidence or source>
Revision condition: <what observation would reopen this>
```

## Human gates

Stop and ask only when the missing answer belongs to a human authority (domain judgement,
authorship, ethics, venue, a scoping decision on unobtainable data). Ask the smallest
decision-changing question, with the consequence stated in plain language and a
recommended default; record the answer as a decision. Everything else is inspected,
computed or degraded explicitly — never asked.

## Completion

A phase is complete when its report line reads `Gate: PASS`. A research is complete when
every hypothesis has a terminal state, phase 8's gate passed, and the research map's
`update` recorded it.
