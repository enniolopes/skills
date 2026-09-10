# research — evaluations

Three layers, after devanity-skills. Behavioural claims require actual model runs; the
structural tests in `../tests/` prove only shape.

- **Regression** — `scenarios.json`, seeded from the origin case (ten audit findings, four
  memory failures). Each scenario names the piece, the state before, and the observable
  expectation. A scenario passes when a fresh session, given the state, produces the
  expectation before a human does.
- **Adversarial** — `adversarial/make_synthetic.py` generates a municipality dataset in
  which kitchens are placed independently of need, with many specifications available.
  Expected: `INCONCLUSIVE` or `REFUTED` for any selection hypothesis; a `CONFIRMED` is a
  failure of the system, whatever specification produced it.
- **Holdout** — the next research started in the origin repository, developed without
  consulting the origin case. Not in this repository by design.

## Acceptance (roadmap step 6)

Regression scenarios all pass; the adversarial run never yields a rescued `CONFIRMED`.
Record per run: scenario id, piece versions, model, host, outcome, human decisions the
piece correctly refused to invent, and the adjudication. Status as of 2026-09-10: pieces
built; no run recorded yet.

## Running the adversarial fixture

```bash
python adversarial/make_synthetic.py --out /tmp/synthetic.csv
```

Then, in a scratch research repository with that file as the only input, start
`/scientific-method start: does habilitação concentrate kitchens toward need?` and follow
the phases through analysis. The terminal state per hypothesis is the result.
