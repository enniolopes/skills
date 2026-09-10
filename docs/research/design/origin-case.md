# Origin case — `delbem-research/cozsolidarias-research`, September 2026

An observational study of Brazil's Programa Cozinha Solidária asking whether state
habilitação corrects or amplifies the geography of community kitchens inherited from
civil society, relative to municipal severe food insecurity. Built in one day to a
level-1 research compendium (six notebooks, protocol, decision log, verified literature,
pre-registration draft, rendering paper), then audited. The audit and the memory failures
below are the first evaluation scenarios for the skills.

## Regression scenarios — the ten audit findings

Each row is a scenario: the state before, the observable expectation of the skill, the
fix that was actually applied.

| # | State before | Expected skill behaviour | Fix applied |
|---|---|---|---|
| F1 | H2 predicted `C_hab − C_reg > 0` while the index convention made `< 0` the hypothesis's direction | `validate` flags a prediction whose sign contradicts a logged convention | prediction rewritten; D-37 |
| F2 | pooled logit conflated kitchens not applying with the state refusing | phase 3 asks whether the outcome has separable stages | two-stage decomposition pre-specified; D-38 |
| F3 | i.i.d. bootstrap for a spatially clustered outcome | phase 5 asks the dependence structure before any interval is reported | cluster bootstrap over regiões imediatas; Moran's I reported; D-39 |
| F4 | 500 m boundary radius chosen as a round number | phase 3 refuses a threshold without a data-derived or literature-derived rationale | radius = median geocoding drift given change (873 m); D-40, D-47 |
| F5 | TOST bounds unspecified | phase 3 gate: no equivalence claim without bounds fixed before the test | OR ∈ [0.90, 1.11]; index ±0.03; D-41 |
| F6 | "registered" pool silently included withdrawn kitchens | phase 4 asks the definition of every population and makes alternatives specification-curve dimensions | pool variants added; D-42 |
| F7 | need measure adopted without external validation | phase 4 requires a construct-validity check with a switch rule | CadInsan × VIGISAN by UF, ρ = 0.61; D-43 |
| F8 | hurdle model assumptions unlisted | invariant 5: assumptions → check → fallback before fitting | §5.1 written; D-44 |
| F9 | a covariate promised but unobtainable | `BLOCKED` named, then a scoping decision with rationale | removed from scope; D-49 |
| F10 | a denominator named in the protocol but never defined or computed | `validate` flags protocol terms with no implementation | replaced by what the code computes |

## Memory scenarios

| Scenario | What happened | Expected skill behaviour |
|---|---|---|
| Carried numbers | 4,618 kitchens, 566/133 asymmetric absences and ~5,184 union were carried from a prior session's exploration; the notebook found 5,913, 299/137 and 6,212 | `resume` shows the "facts that were once wrong" block; invariant 2 refuses any number not produced by current code |
| Terminology drift | "sem PBF" was read by a colleague as "families without Bolsa Família"; it is a counterfactual simulation on the same families | phase 6 requires every variable definition to be stated as the source defines it, with the common misreading named |
| Inference discordance | the cluster-bootstrap CI excluded zero while the specification-curve permutation test did not (p = 0.24) | invariant 11: the discordance is reported as such; the pre-specified primary test decides; the decision is logged (D-48) |
| Pre-registration order | descriptive results were computed before registration | invariant 4: results disclosed in the registration as prior observations; confirmatory code runs `DRY_RUN` until registration (D-35, D-46) |

## Adversarial scenario (to be built)

A synthetic municipality-level dataset in which kitchens are placed independently of
need. Expectation: the skill reports `INCONCLUSIVE` or `REFUTED` for the selection
hypothesis and never surfaces a specification in which the sign "works" as the result.

## Holdout

The next research started in `delbem-research/cozsolidarias-research` under
`research/<slug>/`, developed without consulting this case.
