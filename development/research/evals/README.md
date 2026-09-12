# research — evaluation

Behavioral claims require model runs; unit tests prove only deterministic contracts.

Use `scenarios.json` as the minimal regression set: one scenario per distinct failure mechanism across `scientific-method`, `research-map` and `reviewer-2`. Judge the observable decision, not exact phase wording, headings or historical case details.

`adversarial/make_synthetic.py` is the single adversarial fixture. It creates data with no target relation but many plausible specifications. The system fails if specification search manufactures a confirmatory result.

For a targeted change, run only scenarios that can distinguish it. For a broad method change, run the full set plus the adversarial fixture. A baseline/candidate difference is useful only when it changes the research decision or evidence boundary; matching preferred vocabulary is not improvement.

Independent real-project use remains stronger evidence than these regressions.
