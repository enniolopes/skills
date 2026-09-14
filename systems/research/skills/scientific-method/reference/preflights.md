# Epistemic preflights

Phases describe where the research is. Preflights govern the action about to happen. Run the smallest applicable preflight before the action, regardless of phase.

## FIT

Before a confirmatory analysis can expose its result, require:

- hypothesis and estimand IDs;
- one recorded primary test;
- an `analysis-plan.md` block with assumptions, checks, failure actions, dependence and interpretation boundary;
- protocol and analysis-plan freezes that predate the run;
- registration/DRY_RUN state consistent with the protocol;
- data exposure compatible with confirmatory use.

A missing material condition blocks the fit. Do not satisfy a failed preflight with an explanation of what the missing artifact probably would have contained.

## CHANGE_PLAN

A post-freeze change is classified before editing the confirmatory plan:

- `SPECIFICATION` when it is a defensible alternative that preserves the same estimand and was admitted prospectively;
- `EXPLORATORY` when it is result-driven or hypothesis-generating;
- `DEFERRED` when it does not enter the current research;
- `REOPEN` when it changes the confirmatory scientific commitment. `REOPEN` requires a logged decision and a new freeze.

Silent rewrite is not a state.

## CLAIM

Before a material claim enters prose, require an executed result, a valid run, the relevant planned test and checks, an interpretation boundary that permits the wording, and no unresolved supersession or material contradictory result. Give the claim a stable ID and lineage annotation.

A hypothesis-deciding claim must use that hypothesis's primary test unless the protocol was explicitly reopened before the deciding run.

## CITE

A source may suggest a search while merely discovered. It supports a scientific or methodological proposition only after the relevant source content has been retrieved and read. DOI/URL resolution proves identity/reachability, not semantic support.

## PUBLISH

Before release, require material claims to have complete lineage and adversarial review; no unresolved `FAIL`; material `NOT_VERIFIED` explicitly disclosed or resolved; reporting/disclosure requirements satisfied; and human-owned publication/ethics decisions present.

## Forbidden transitions

The following transitions are invalid:

```text
RESULT_SEEN -> RETROACTIVE_FALLBACK
DISCOVERY_DATA -> INDEPENDENT_CONFIRMATION_OF_DERIVED_HYPOTHESIS
SOURCE_DISCOVERED -> SUPPORTS_CLAIM
UNEXECUTED_NUMBER -> RESULT
SECONDARY_TEST -> DECIDES_HYPOTHESIS_AGAINST_PRIMARY
FROZEN_PROTOCOL -> SILENT_REWRITE
VALIDATOR_PASS -> SCIENTIFICALLY_TRUE
```

Route invalid transitions to a legitimate state: prospective fallback, `EXPLORATORY`, `DEFERRED`, `REOPEN`, `BLOCKED` or `NOT_VERIFIED`.
