# Phase 5 — Analysis

Verified 2026-09-10 (sources located, not yet read at source).

**When this applies.** You are about to fit a model, compute an interval, report a
statistic, or compare two results.

**What it requires.**

- **`DRY_RUN` until registration.** Confirmatory code runs with the outcome permuted until
  the registration exists; the switch is a repository flag, not a comment.
- **Dependence before intervals.** Ask the dependence structure of the outcome — spatial,
  cluster, temporal — before any interval is reported. Spatially clustered outcomes get a
  cluster bootstrap over the relevant region and a reported Moran's I; with few clusters,
  a bootstrap-t (origin case F3).
- **Assumption checks executed and reported**, one row per model: assumption, check,
  result, fallback taken or not.
- **Count models**: overdispersion, zero process (hurdle vs zero-inflated), exposure
  offset — decided and written before fitting, tested after.
- **Sensitivity to unmeasured confounding** for any causal-leaning estimate (E-value or
  equivalent), reported next to the estimate.
- **Inequality measures** (concentration index, slope index) computed with their standard
  errors and the ranking variable stated.
- **Discordance is reported as such.** When two frameworks disagree (an interval excludes
  zero, a permutation test does not), the pre-specified primary test decides and the
  decision is logged with both results.
- **Terminal state per hypothesis**: `CONFIRMED`, `REFUTED`, `INCONCLUSIVE`, `BLOCKED`,
  `NOT_VERIFIED`. Silence is not a state.

**The error it prevents.** An i.i.d. interval on a clustered outcome; a fallback chosen
after seeing residuals; a discordance resolved by choosing the flattering result; a
number reported that no executed code produced.

**Exit gate.** Every pre-specified check has a result; every hypothesis has a terminal
state; every reported number exists in a committed aggregate.

**Sources.** VanderWeele & Ding 2017 (E-value). Wagstaff, Paci & van Doorslaer 1991 and
O'Donnell et al. 2008 (concentration index). Anselin 1995 and Moran 1950 (spatial
autocorrelation, LISA). Cameron & Trivedi 2013 (count models). Cameron, Gelbach & Miller
2008 (cluster bootstrap-t with few clusters). Lakens 2017 (equivalence testing).
Simonsohn et al. 2020 (joint inference across specifications).
