---
name: scientific-method
description: Run an empirical research project as a lifecycle with gates — problem, literature, protocol, data, analysis, writing, review, publication — for observational quantitative studies on administrative data. Use it to start a research, to check which gate you are at, to review a manuscript, and whenever you are about to fit a model, cite a source, report a number or write results. Delegates hypothesis generation to explorer, session memory to research-map, and review to the reviewer-2 agent.
when_to_use: Triggers include "vou ajustar/rodar o modelo", "let me fit", "vou citar", "escrever os resultados", "deu/não deu efeito", "no effect", "qual o intervalo", "definir a amostra/população", "o raio de 500 m", "os dois resultados discordam", "pré-registro", "protocolo", "hipótese", "revisar o manuscrito", "submeter o artigo", "a gente devia testar também", "apareceu um método novo", "abrir mais uma frente", "qual é a pergunta", "definir o problema", "estimando", "para quem isso importa", "o problema é óbvio", "mostrar que o problema existe", "qual o tamanho do problema", "isso já não está resolvido?".
license: CC-BY-NC-4.0
metadata:
  version: 0.6.0
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
- anything else → match it against the phase table below; a match fires that phase; no
  match is answered as asked, without a phase.

Every response ends with one report line. If a phase trigger fired this turn:

```text
Phase <n> <name> · Gate: PASS | FAIL — <unmet criterion> · states changed: <H1 → INCONCLUSIVE, …> · decisions: <D-n, …> · next: <one concrete step>
```

Otherwise: `Phase: none · no gate touched · next: <one concrete step>`.

## Ownership

Owns: phases, gates, terminal states, the quality of protocol, data, analysis, manuscript
and deposit. Does **not** own domain judgement (which question matters, which institution
to call, what a field term means in practice), authorship, ethics approval, or the choice
of venue. Those belong to humans and are never invented; when one is missing the state is
`BLOCKED`, named, with who unblocks it.

Does **not** own software engineering. The topology of a research is the map's `Layout`:
protocol, decisions, aggregates, documents, notebooks, references. "Structure this
research" means making those six keys true — `research-map init` — and nothing more.
Packages, test suites, build systems, CI, hooks and code architecture are the analyst's
engineering, not this method; when asked for them, say so in one line and stop.

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
8. **Every linkage step reports match rates and errors. Every table written under the
   map's `documents` respects its `floor`** — whoever writes it, this method included.
9. **Every citation is verified at its DOI record or landing page before it is written**;
   a finding read only from an excerpt is marked as such.
10. **Every methodological decision is logged** with date, rationale and revision
    condition. Methodological means: a reviewer, or the supplementary material, would need
    it to judge the results. Anything else — tooling, file layout, wording — is a commit
    message. The log is append-only from the commit onward.
11. **Terminal states are named**: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`
    (missing human decision or data), `NOT_VERIFIED` (a check could not run). Silence is
    not a state.
12. **A missing capability degrades explicitly** to `NOT_VERIFIED` or `BLOCKED`, never to a
    guess.

## The problem first: formulated, then shown

"Understanding the problem" is not time spent; it is two artifacts, complete and checked by
`validate`. Gate 1A: the **problem statement** (`reference/problem-statement.md`) —
what is claimed, for whom, with what estimand, what would refute it. Gate 1B: the **problem
brief** (`reference/problem-brief.md`) — a descriptive study that shows the problem exists,
how large against a reference set by a logged decision, for whom, how it is handled today,
and what was tried to make it disappear. Its verdict lives in the map: `Problem: SHOWN |
NOT_SHOWN | INCONCLUSIVE`. The protocol does not freeze before `SHOWN`; `NOT_SHOWN` ends or
reformulates the research and is the cheapest good result a research can have. Every later
gate re-reads both; a change is a logged decision, never a silent rewrite. The error this
prevents has a name — the error of the third kind, a precise answer to the wrong problem.

## Scope: open wide once, then pay to reopen

Divergence is a phase with a budget, not a disposition. In phase 1 the exploration budget
(lineages, time, stopping rule) is logged as a decision **before** `explorer` runs; the
default is three to five structurally different lineages and stop at revised saturation.
After the protocol freezes, a new method, concept, test or front has exactly four
destinations, and "open it" is the most expensive:

1. a **specification-curve dimension**, when it is an alternative way of doing something
   already in the protocol — absorbed, no new front;
2. an **exploratory analysis**, labelled as such, hypothesis-generating, never confirmatory;
3. the map's **`## Deferred`** section, dated, with the condition under which it would enter
   — the default destination for "we should also test X";
4. **reopening phase 3**, only by a logged decision that says what leaves the protocol for
   this to enter; a research carries at most three hypotheses without a terminal state, and a
   fourth requires that trade in the same decision.

`resume` reports the count of open hypotheses and of deferred items every session, so
growth is seen, not felt.

## Memory across sessions

`research:research-map` owns it. Run its `resume` before the first action of a session,
its `validate` before any commit, and its `update` after any gate change, terminal-state
change or corrected number — not "at the end", which nothing signals. Never narrate a
resume, update or validate you did not perform.

## Phases

Each phase has an entry trigger, a procedure (in `reference/`), an exit gate that can fail,
and terminal states; phase 1 has two gates. Read the phase file when the phase is entered or
when its trigger fires; do not read all of them at once. When a trigger fires implicitly, say which phase
fired and apply its requirements **before** doing the thing.

| # | Phase | Trigger (what the conversation shows) | Exit gate | Read |
|---|---|---|---|---|
| 1A | Problem — formulate | a research starts, restarts, gains a hypothesis or comes under the method; the question is stated in one sentence and someone wants to start analysing | exploration budget logged, then `explorer` invoked on it; problem statement complete (claim, unit, estimand, refutation, objection, who cares, non-goals); lineages not adopted in `## Deferred` | `reference/01-problem.md`, `reference/problem-statement.md` |
| 1B | Problem — demonstrate | the statement exists; "the problem is obvious"; anyone reaches for a solution or a model before the problem is shown | problem brief complete (construct validated, population, measure, reference named by its decision, magnitude from executed code, falsification attempted, verdict); `Problem: SHOWN` in the map, or the research reformulates or closes | `reference/problem-brief.md` |
| 2 | Literature | a citation is about to be typed; a claim about the state of knowledge | verification log complete (each source at DOI, or `NOT_VERIFIED` and not in the text); gap in one paragraph | `reference/02-literature.md` |
| 3 | Protocol | hypotheses, tests, populations or thresholds set or changed; a round-number threshold or radius proposed; "no effect" planned; "we should also test X" after the freeze | protocol frozen; registration text derived; assumption tables, bounds and dimensions listed; anything admitted after the freeze has its trade logged | `reference/03-protocol.md` |
| 4 | Data | an input enters; sources are joined; a population or pool is named for the first time; a table is written under `documents` | linkage report per join; provenance per input; no identifiable row outside the cache; no cell under `documents` below `floor` | `reference/04-data.md` |
| 5 | Analysis | "vou ajustar / rodar o modelo", "let me fit"; an interval or statistic about to be reported; two results disagree | assumptions → check → fallback listed before fitting; dependence structure asked; `DRY_RUN` status confirmed; every pre-specified check has a result; terminal state per hypothesis; discordance reported and the primary test decides | `reference/05-analysis.md` |
| 6 | Writing | a number is about to be written into prose; any prose that will leave the repository | every number exists in a committed aggregate with interval and source table; figure provenance; definitions with misreadings | `reference/06-writing.md` |
| 7 | Review | before submission; after any confirmatory run on demand; `review <path>` | reviewer verdict `PASS`, or every `FAIL` has a logged response and re-run checks | `reference/07-review.md` |
| 8 | Publication | anything leaves for a venue, funder or repository of record | DOIs recorded in the protocol; DMP and AI declaration in the venue's shape; PII check passed | `reference/08-publication.md` |

Phases are ordered by dependency, not ceremony. A later phase may send work back to an
earlier one (a review finding that changes a number reopens phase 6; a new hypothesis
reopens phases 1 and 3). Skipping a phase is a logged decision with a revision condition,
never silence. A gate is `reached` when the artifact it produces exists and the map's
`Gates` row points to it; until then it is `pending`, whatever the history says. This is
also how a research that already exists comes under the method: every gate `pending`, each
earned by its artifact.

## Delegation

- **`explorer`** (skill; `explorer:explorer` when installed from the marketplace, pulled in
  as a dependency) — phase 1: hypothesis portfolio with bridge certificates. Each surviving
  lineage's discriminating test becomes the primary test; its failure condition becomes
  the refutation clause.
- **`research:research-map`** (skill) — memory across sessions, above. Its `validate` is
  the mechanical half of invariants 2, 8, 9 and 10.
- **`research:reviewer-2`** (agent) — phase 7 and on demand. Supply the brief exactly as its
  "Required brief" section lists it, checklist included. It does not edit and does not
  inherit your reasoning.

Delegating is invoking: the Skill tool for a skill, the Agent tool for the agent. Reading a
skill's file with `cat` is not invoking it. A delegate that is not installed or cannot be
invoked is not simulated: the step is `NOT_VERIFIED` with what is missing named.

## Decision log entry

A methodological decision (invariant 10: a reviewer would need it) goes to the repository's
decision log in this shape; the map's `validate` requires the heading and a non-empty
revision condition:

```text
### D-<n> · <YYYY-MM-DD> · <title, five words>
<what was decided, one or two sentences>
Rationale: <why; evidence or source>
Revision condition: <the observation that would reopen this; or "not revisable: <why>">
```

Before its commit a block is a draft and is rewritten in place; after, only a new block with
`Supersedes: D-<k>` changes it.

## Human gates

Stop and ask only when the missing answer belongs to a human authority (domain judgement,
authorship, ethics, venue, a scoping decision on unobtainable data). Ask the smallest
decision-changing question, with the consequence stated in plain language and a
recommended default — always the option that changes the least; record the answer as a
decision. Everything else is inspected, computed or degraded explicitly — never asked.

## Completion

A phase is complete when its report line reads `Gate: PASS`. A research is complete when
every hypothesis has a terminal state, phase 8's gate passed, and the research map's
`update` recorded it.
