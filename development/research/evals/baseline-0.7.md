# Behavioral baseline — research 0.7.0

This file preserves the first adjudicated control/treatment behavioral evidence for
`research`. It is historical baseline evidence for 0.8; it is **not** evidence that 0.8
passes the same mechanisms.

## Provenance

- date: 2026-09-14
- runtime under test: research 0.7.0
- source commit containing the adjudicated finding: `466b9081024952e787121ed1cebf1a231590ce0a`
- source branch at the time of preservation: `claude/blissful-pascal-hpbgbt`
- design: 8 mechanisms × control/treatment × 3 runs, plus one corrected
  `adversarial-null` rerun
- runner/judge environment recorded by the source finding: Claude Code 2.1.270,
  `claude plugin eval --ablation with-without`, judge `sonnet`
- raw result file from that run was gitignored and is not claimed to be preserved here;
  this file preserves the adjudicated summary and its limitations

## Result

| mechanism | control | research 0.7 | delta |
|---|---:|---:|---:|
| stale-memory | 0/3 | 2/3 | +67pp |
| missing-input | 0/3 | 2/3 | +67pp |
| adversarial-null | 1/3 | 3/3 | +67pp |
| independent-review | 2/3 | 3/3 | +33pp |
| missing-inferential-requirement | 2/3 | 3/3 | +33pp |
| assumptions-before-fit | 0/3 | 0/3 | 0pp |
| contradictory-specification | 0/3 | 0/3 | 0pp |
| post-freeze-change | 0/3 | 0/3 | 0pp |

`adversarial-null` uses the corrected-fixture rerun. The original fixture mixed in a
protocol/code contradiction and was not used for the table above.

## Finding that motivated 0.8

The effect concentrated where a rule already had durable state/artifact support. The three
zero-delta mechanisms often showed the model reasoning correctly in prose while failing to
leave the required scientific state behind:

- `assumptions-before-fit`: the session recognized that the model was not ready but left no
  assumption → check → fallback artifact for a later session;
- `post-freeze-change`: the session recognized the freeze and refused a second primary test
  but left the proposed route unrecorded;
- `contradictory-specification`: the session read remembered/narrative artifacts but did not
  inspect the current executable/aggregate evidence before committing the stale
  specification to the manuscript.

A separate observation was that the treatment arm invoked `reviewer-2` 0/3 times in the
`independent-review` case. Review happened inline, so outcome quality and procedural
independence were not the same property.

These findings are inputs to the 0.8 design: `analysis-plan`, action preflights, temporal run
provenance, durable CHANGE_PLAN routing, claim lineage and explicit independent-review
evidence. They do not establish that those mechanisms work until 0.8 is rerun.

## Experimental limitations

- `n = 3` per arm; the result is diagnostic rather than a precise effect estimate.
- control behavior varied materially across repeated runs.
- the host used for the run could not grant a shell, so execution-order-only criteria were
  vacuous and excluded from interpretation.
- `explorer` was absent from both arms; phase-1 exploration was not tested.
- the judge was an LLM correlated with the runner.
- fixtures were synthetic; the historical origin repository retro-test was not run.

## Use of this baseline

For 0.8, compare the same failure mechanisms plus liveness cases under the new isolated
harness. Do not tune only the three failures above, and do not treat a baseline pass as a
0.8 pass. Where a property is machine-observable, prefer deterministic observation over an
LLM judgment; reserve semantic judgment for the residual that cannot be decided from
artifacts, order or tool events.
