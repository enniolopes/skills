# RESEARCH.map — grammar

Markdown. Sections are `## ` headings in this exact order; `validate` fails on a missing or
misordered section. Pointers are backticked repository-relative paths, optionally with
`#anchor`; every pointer must resolve. Tables are GitHub-flavoured Markdown.

```markdown
# RESEARCH.map — <research slug>

## Layout
- protocol: research/2026-kitchens/protocol.md
- decisions: research/2026-kitchens/decisions.md
- aggregates: research/2026-kitchens/aggregates/
- documents: research/2026-kitchens/paper/
- notebooks: research/2026-kitchens/notebooks/
- references: research/2026-kitchens/references.bib

## Question
Does state habilitação correct or amplify the geography of community kitchens inherited
from civil society, relative to municipal severe food insecurity? → `research/2026-kitchens/protocol.md#question`
Registration: https://osf.io/xxxxx, 2026-09-08

## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | C_hab − C_reg < 0 (habilitação concentrates toward need) | interval includes 0 or sign > 0 under the primary test | INCONCLUSIVE | `research/2026-kitchens/protocol.md#h1` |

## Gates
| Phase | State | Blocked by |
|---|---|---|
| 1 Problem | reached | |
| 2 Literature | reached | |
| 3 Protocol | reached | |
| 4 Data | reached | |
| 5 Analysis | pending | |
| 6 Writing | pending | |
| 7 Review | pending | |
| 8 Publication | blocked | ethics approval — PI |

## Facts that were once wrong
| Was | Is | Produced by |
|---|---|---|
| 4,618 kitchens | 5,913 | `research/2026-kitchens/notebooks/01_reconcile.ipynb` |
| 566/133 asymmetric absences | 299/137 | `research/2026-kitchens/notebooks/01_reconcile.ipynb` |

## Provenance
| Input | Location | Read by |
|---|---|---|
| MDS kitchens registry, 2026-08-30 | `data/cache/mds_kitchens_2026-08-30.csv` | `research/2026-kitchens/notebooks/01_reconcile.ipynb` |

## Verification
```bash
make notebooks          # runs notebooks in order, DRY_RUN unless REGISTERED=1
make paper              # renders the manuscript from committed aggregates
python tools/research_map_validate.py RESEARCH.map --offline
```

## Open decisions
- D-?: include withdrawn kitchens in the "registered" pool? — unblocked by: PI, after D-42 alternatives are computed

## Deferred
- 2026-09-09: spatial lag model as an alternative to the cluster bootstrap — enters when: H1 has a terminal state and Moran's I is reported
- 2026-09-09: qualitative interviews with state coordinators — enters when: the next research is scoped (out of this study's design)

## Last session
- 2026-09-09: reconciled registry; 5,913 kitchens (was 4,618); D-37..D-42 logged.
- Next: run 03_models in DRY_RUN; list hurdle assumptions before fitting (phase 5).
```

## Rules `validate` applies

- `Layout` keys are exactly `protocol`, `decisions`, `aggregates`, `documents`,
  `notebooks`, `references`; values are comma-separated paths that must exist. Keep the
  protocol out of `documents`: its design parameters (bounds, alpha, power) exist before any
  aggregate by construction.
- `Question` carries `Registration: none` or `Registration: <URL or DOI>, <date>`; while it
  is `none`, confirmatory code is `DRY_RUN`.
- Backticks are reserved for pointers: a repository-relative path (with `/` or a known
  suffix), optionally with `#anchor`. A backticked number or symbol is not a pointer.
- `Gates` has one row per phase, all eight; states are `reached`, `pending` or `blocked`;
  a `blocked` row names who or what blocks it in the third column.
- `Hypotheses` states are `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`,
  `NOT_VERIFIED`, or `—` before analysis.
- Every row in `Facts that were once wrong` has a `Produced by` pointer that resolves.
- `Deferred` holds what appeared after the protocol froze and was not admitted: each item
  `- YYYY-MM-DD: <idea> — enters when: <condition>`. It is the destination for a new method,
  concept or front that would otherwise open a parallel line of work; nothing leaves it
  except by a logged decision that reopens phase 3 or by becoming the next research.
- `Last session` has at least one dated line (`- YYYY-MM-DD: …`) and one `Next:` line.

## Decision log grammar (`decisions`)

Each decision is a block starting with a heading or bold id, containing a date, the
decision, a rationale and a revision condition:

```markdown
### D-39 · 2026-09-08
Decision: cluster bootstrap over regiões imediatas; report Moran's I.
Rationale: outcome is spatially clustered (Moran's I = 0.31, p < 0.001, notebook 03).
Revision condition: a dependence check on the final sample shows Moran's I within the null band.
```

A block starts only at a heading (`### D-<n>`) or a bold id (`**D-<n>**`, `- **D-<n>**`);
a bare `D-<n>` in running text is a cross-reference. `validate` requires `Revision
condition:` (or `Revise when:`) in every block, and ids unique and increasing in file
order. The log is append-only by convention; git history is the check.

## Numbers rule (`documents` ↔ `aggregates`)

A number in a document is *present* when some numeric value in an aggregate file (`.csv`,
`.tsv`, `.json`) rounds to it at the quoted precision. Presence is not provenance: the check
reports what is absent from every aggregate; a number that is present still needs its
source table in the text (phase 6). Signs are compared both ways (`-0.31` and `0.31` match
each other). Thousands separators (`5,913`, `5.913`) and decimal commas (`0,61`) are
normalised; a token ambiguous between pt-BR thousands and three decimals (`5.913`) matches
on either reading, and a leading zero (`0.125`) is never read as thousands.

Ignored by default: integers below 20; four-digit years 1900–2100; identifiers glued to a
letter (`D-37`, `H1`, `F10`); thresholds after `p`, `alpha` or `α` and an inequality
(`p < 0.001`); labels after Section/Seção/§, Table/Tabela, Figure/Fig./Figura, Eq., p./pp.;
confidence levels (`95% CI`, `95% IC`); numbers inside ``` or ~~~ fences; numbers on a line
carrying `<!-- rm:ignore -->`; the span of a URL or DOI (the rest of the line is still
checked). Aggregate files are read cell by cell (`, ; tab |` delimiters), JSON by value.
Everything else must be present or is reported with file and line. Manuscripts in
`.docx`/`.pdf` are out of scope; render to Markdown or `.qmd` first.
