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
- documents: research/2026-kitchens/paper/, research/2026-kitchens/protocol.md
- notebooks: research/2026-kitchens/notebooks/
- references: research/2026-kitchens/references.bib

## Question
Does state habilitação correct or amplify the geography of community kitchens inherited
from civil society, relative to municipal severe food insecurity? → `research/2026-kitchens/protocol.md#question`

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

## Last session
- 2026-09-09: reconciled registry; 5,913 kitchens (was 4,618); D-37..D-42 logged.
- Next: run 03_models in DRY_RUN; list hurdle assumptions before fitting (phase 5).
```

## Rules `validate` applies

- `Layout` keys are exactly `protocol`, `decisions`, `aggregates`, `documents`,
  `notebooks`, `references`; values are comma-separated paths that must exist.
- `Gates` states are `reached`, `pending` or `blocked`; a `blocked` row names who or what
  blocks it in the third column.
- `Hypotheses` states are `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`,
  `NOT_VERIFIED`, or `—` before analysis.
- Every row in `Facts that were once wrong` has a `Produced by` pointer that resolves.
- `Last session` has at least one dated line and one `Next:` line.

## Decision log grammar (`decisions`)

Each decision is a block starting with a heading or bold id, containing a date, the
decision, a rationale and a revision condition:

```markdown
### D-39 · 2026-09-08
Decision: cluster bootstrap over regiões imediatas; report Moran's I.
Rationale: outcome is spatially clustered (Moran's I = 0.31, p < 0.001, notebook 03).
Revision condition: a dependence check on the final sample shows Moran's I within the null band.
```

`validate` requires `Revision condition:` (or `Revise when:`) in every block, and ids
unique and increasing in file order. The log is append-only by convention; git history is
the check.

## Numbers rule (`documents` ↔ `aggregates`)

A number in a document matches when some numeric value in an aggregate file (`.csv`,
`.tsv`, `.json`) rounds to it at the quoted precision. Thousands separators (`5,913`,
`5.913`) and decimal commas (`0,61`) are normalised; a token ambiguous between pt-BR
thousands and three decimals (`5.913`) matches on either reading, and a leading zero
(`0.125`) is never read as thousands. Ignored by default: integers below 20, four-digit
years 1900–2100, confidence levels (`95% CI`, `95% IC`), numbers inside code fences,
numbers on a line carrying `<!-- rm:ignore -->`, and lines containing `doi` or `http`.
Aggregate files are read cell by cell (`, ; tab |` delimiters), JSON by value. Everything
else must have a source or is reported with file and line.
