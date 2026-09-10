# Research skills system — consolidated design

Status: design, 2026-09-10. Language of the skills: English, with bilingual (en/pt-BR)
examples where the origin case supplies them.

## 1. Diagnosis the design answers

Working through a full observational study with an agent showed two failure classes:

- **Procedure was the value.** What made the work sound was listing model assumptions
  before fitting, separating exploratory from confirmatory analysis, logging each
  decision with a revision condition, and verifying every citation at its source. None
  of this is knowledge the model lacks; it is discipline the model applies only when a
  procedure demands it at the right moment.
- **Memory was the risk.** Numbers carried from an earlier session were wrong
  (4,618 kitchens → actually 5,913; 566/133 → 299/137) and survived until executed code
  replaced them. Nothing the agent "learned" persists past the session unless it is
  written where the next session reads first.

The system therefore has a method piece (procedure with gates), a memory piece (an
index read first and validated mechanically), and a review piece (an adversary that does
not inherit the author's reasoning).

## 2. `skills/scientific-method`

### Ownership

Owns the lifecycle of an empirical research project and the quality of its artifacts.
Does **not** own domain judgement (what question matters, which institution to call,
what a field term means in practice), authorship decisions, ethics approval, or the
choice of venue. Those are human-owned and are never invented.

### Form

Follows the devanity-skills shape: frontmatter with `name`, `description`, `license`,
`metadata.version`, `argument-hint`; sections **Ownership**, **Invariants**
(numbered), **Phases** (each with entry condition, procedure, exit gate, terminal
states), **Delegation**, **Reference**. Kept under ~2,500 words; everything longer lives
in `reference/<phase>.md`. The model may invoke it on its own when it recognises a phase
trigger (about to fit a model, about to cite, about to write results).

### Invariants (draft)

1. The protocol is the source of truth; paper, abstract, pre-registration, e-mails and
   slides are projections of it and are regenerated from it, never edited into
   disagreement with it.
2. Evidence is something read or run against an identified target. A number that did not
   come out of executed code in the current repository state is a claim, not a result.
3. Every hypothesis carries a prediction **and** a refutation condition before any
   confirmatory analysis runs. One primary test per hypothesis.
4. Exploratory and confirmatory are separated by an artifact, not by intent: a public
   registration, and confirmatory code that runs only with the outcome permuted until
   registration exists (`DRY_RUN`).
5. Every model lists its assumptions, the check for each, and the fallback if the check
   fails — before fitting. A fallback chosen after seeing residuals is a forking path.
6. Bounds for any claim of "no effect" (equivalence) are fixed before the test.
7. Every analytic choice that could reasonably have gone another way is a dimension of a
   specification curve, not a footnote.
8. Every linkage step reports match rates and errors (GUILD). Every aggregate that leaves
   the analysis environment respects the disclosure floor the repository sets.
9. Every citation is verified at its DOI record or landing page before it is written;
   findings read only from excerpts are marked as such.
10. Every methodological decision is logged with date, rationale and revision condition;
    the log is append-only.
11. Terminal states are named: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`
    (missing human decision or data), `NOT_VERIFIED` (check could not run). Silence is
    not a state.
12. A missing capability degrades explicitly (`NOT_VERIFIED`, `BLOCKED`), never to a
    guess.

### Phases and gates

| Phase | Procedure | Exit gate | Reference knowledge (to be distilled, source-verified) |
|---|---|---|---|
| 1 Problem | invoke `explorer`; fix unit of analysis, what would invalidate the question, conventional answers, non-goals | question written with its refutation; the "obvious reviewer objection" named | King, Keohane & Verba *Designing Social Inquiry*; Booth et al. *The Craft of Research* |
| 2 Literature | search; verify each source at DOI/landing page; classify findings as established / silent / what this study adds | verification log complete; gap stated in one paragraph | PRISMA principles for narrative review; Crossref API as verifier |
| 3 Protocol | hypotheses with prediction and refutation; primary test each; floor vs additive blocks; gates with exit criteria; assumptions→check→fallback per model; equivalence bounds; specification-curve dimensions | protocol frozen; registration text derived from it | Nosek et al. 2018; Lakens 2017; Simonsohn et al. 2020; Hernán & Robins for identification in observational designs |
| 4 Data | reconcile sources by stable key; linkage table per step; disclosure floor; PII dropped at first step; provenance file per input | linkage report exists; no identifiable row outside the cache | Gilbert et al. 2018 (GUILD); Gebru et al. *Datasheets for Datasets*; FAIR |
| 5 Analysis | `DRY_RUN` until registration; assumption checks executed and reported; dependence (spatial/cluster) asked explicitly; sensitivity to unmeasured confounding | every pre-specified check has a result; terminal state assigned per hypothesis | VanderWeele & Ding 2017; Wagstaff et al. 1991 / O'Donnell et al. 2008; Anselin 1995; Cameron & Trivedi for count models |
| 6 Writing | argument structure before prose; one finding per paragraph; every number with interval and source table; limitations stated, not discovered | manuscript renders from committed aggregates only; no number without a file | Gopen & Swan 1990; Schimel *Writing Science*; Heard *The Scientist's Guide to Writing* |
| 7 Review | hand to `reviewer-2`; fix or rebut every finding; re-run affected checks | reviewer verdict `PASS` or every `FAIL` has a logged response | STROBE, RECORD; Munafò et al. 2017 |
| 8 Publication | preprint with versioning; code and aggregates deposited with DOI; data management plan; AI-use declaration | DOIs recorded in the protocol; PII exposure resolved | venue and funder policies (Elsevier, SciELO, FAPESP) |

### Delegation

- `explorer` — phase 1, hypothesis portfolio with bridge certificates.
- `research-map` — read at every session start (`resume`), written at every session end
  (`update`), validated before any commit (`validate`).
- `reviewer-2` — phase 7, and on demand after any confirmatory run.

### What it is not

Not a statistics textbook (the model knows the methods; it fails at applying them at the
right time). Not a substitute for domain judgement. Not a monolith: method, memory and
review are versioned separately.

## 3. `skills/research-map`

Inspired by aicp's operational map: an index that points to truth and is validated
against it, never a second copy of the truth.

### `RESEARCH.map` content (one per research)

- Question and hypotheses, one line each, with pointers to protocol sections.
- State per gate: reached / pending / blocked (by whom).
- **Facts that were once wrong** — corrected numbers with the notebook that now produces
  them. The single most valuable block.
- Provenance: each input, its location in the cache, the notebook that reads it.
- Verification commands: re-run the notebooks in order, render the paper, run hooks,
  verify citations.
- Open decisions and who unblocks each.
- "What changed last session" in five lines.

### Modes

- `init` — build the map from an existing protocol and decision log.
- `resume` — session start: read the map, restate state in one screen (the i-have-adhd
  rule: the reader cannot hold "step 3 of 5" between messages — the agent is that
  reader).
- `update` — session end: obligatory; records what changed and what is next.
- `validate` — mechanical, runnable as a pre-commit hook: every number quoted in a `.md`
  exists in a committed aggregate; every decision has a revision condition; every
  citation resolves at Crossref or a landing page; no committed notebook has outputs;
  the map's pointers resolve to existing files.

### Session ritual

Open by reading; close by writing; lead every report with the next action and end with
one concrete next step; no closing pleasantries.

## 4. `agents/reviewer-2`

Follows the devanity `verifier` contract, adapted to manuscripts.

- **Mandate:** judge whether the manuscript's claims are supported by the protocol, the
  committed aggregates and the code, without adopting the author's reasoning.
- **May:** read protocol, decision log, manuscript, aggregates, notebooks; run permitted
  read-only checks (render, citation verification, number-to-file matching).
- **May not:** edit, commit, re-run analyses that change state, accept risk, or treat the
  author's summaries as evidence.
- **Procedure:** enumerate claims → for each, look for the falsifying observation first
  (forking path, number without interval, causal language in an ecological design,
  hypothesis decided on a statistic that was not its pre-specified primary, figure that
  does not match its code or data, citation that does not say what it is cited for) →
  then confirming evidence → verdict.
- **Output:** fixed headings — `VERDICT` (`PASS` / `FAIL` / `NOT VERIFIED`), `CLAIMS`,
  `FINDINGS` (claim → location → why a reviewer rejects → what resolves), `CHECKS RUN`,
  `NOT VERIFIED`, `BASIS`.
- Adds the Claude Science check the origin case lacked: figure ↔ code ↔ data agreement.

## 5. Evaluation

Three layers, after devanity-skills:

- **Regression** — the origin case (`origin-case.md`): the ten audit findings and the
  memory failures, each as a scenario with an observable expectation ("the skill asks for
  the bootstrap's dependence structure before reporting an interval").
- **Adversarial** — a synthetic research whose data do not support the hypothesis, where
  the temptation is to find a specification that does; the expectation is
  `INCONCLUSIVE` or `REFUTED`, never a rescued `CONFIRMED`.
- **Holdout** — the next real research in the origin repository, not used during
  development.

Metric: first-pass yield of artifacts that `reviewer-2` passes without material rework,
and the count of human decisions the skill correctly refused to invent.

## 6. Decisions taken

| Decision | Choice | Rationale |
|---|---|---|
| Language | English | matches sibling skills and the target venues; examples may be bilingual |
| Hosting | `enniolopes/skills`, installed via `npx skills add` and pinned in each research repo's `skills-lock.json` | reusable across researches; same mechanism as devanity-skills |
| Granularity | three pieces, separately versioned | they change at different rates |
| `explorer` | dependency, not content | it already does phase 1 well |
| Form | devanity shape (ownership, numbered invariants, phases, terminal states, reference files) | proven in the house; keeps `SKILL.md` short |

## 7. Decisions open

- Scope of v1: observational quantitative research with administrative data only
  (recommended — the only scope with a retro-test available), or also qualitative and
  experimental phases.
- License for the skills (devanity uses CC-BY-NC-4.0).
- Whether `research-map validate` ships as a pre-commit hook in the consuming repository
  or as a command the skill runs.
