# Landing Page Evaluation

Use this file to compare an experimental landing-page runtime against a baseline. It is the single evaluation protocol; behavior cases live in `behavioral-evals.json`, creative briefs in `creative-benchmark.json`.

## Evidence levels

- **L0 structural** — CI, file contracts, token budgets, JSON validity.
- **L1 instruction audit** — whether the runtime encodes the intended behavior without contradiction or unnecessary duplication.
- **L2 proxy execution** — one model/session simulates or grades behavior. Useful for finding obvious regressions, not for proving improvement.
- **L3 independent A/B** — separate executor contexts on identical inputs, with version identity hidden from a reviewer.
- **L4 real project** — repeated performance on actual landing-page work with rendered/browser evidence.

Do not claim behavioral superiority from L0-L2.

## Fixed comparison

- **Baseline A:** `d3b73f3911246ac7dfe7704e7abb5b86cda0eea0` — landing-page v3.1.0.
- **Candidate B:** `9487feea1e9ae5a78684a071988d71ec3161e658` — landing-page v3.5.1 runtime.

Pin the commits. Give both executors the same prompt, files, tools and capability envelope. Do not let either see the other runtime or comparison rationale.

Reviewer C receives anonymized outputs (`X`/`Y`) and, when possible, no executor reasoning transcript. For rendered tasks, desktop/mobile artifacts outrank prose claims.

## What to judge

Judge behavior and output, never use of skill vocabulary.

### Reliability

- **Truth / evidence fit** — claims and commitments stay within evidence and authority; the agent uses evidence capable of settling the question.
- **Continuity / causal scope** — local defects get local fixes; upstream failures reopen enough of the solution without destroying valid work.
- **Pivot / learning** — stronger truthful ideas can replace weaker ones despite sunk cost; creative discovery cannot silently rewrite facts.
- **Decision-rule integrity** — novel cases are handled without forcing irrelevant fields, confusing creative choice with evidence status, choosing workflow depth from artifact existence, or researching after decision value is exhausted.
- **Convergence** — material defects are resolved; the agent neither ships the first plausible render nor churns indefinitely.

### Creative performance

- **Specificity / governing idea** — the page is causally tied to the product/domain and has a strong idea beyond a decorative hero trick.
- **Composition / expression / distinction** — hierarchy, rhythm, typography, imagery, motion and spatial behavior serve the brief rather than a recurring house style.
- **Resolution vs counterfeit quality** — polish, trend signals, novelty, complexity or component repetition do not substitute for the quality they imply; familiar devices remain valid when earned.
- **Craft / reality** — desktop and mobile, type, crops, alignment, states, responsive behavior, interaction and technical execution survive close inspection.

Fail the candidate if compression causes missing relevant work, if control becomes process theater, or if anti-generic guidance creates a recurring anti-default aesthetic.

## Batteries

### A — behavioral regressions

Run every case in `behavioral-evals.json`. These are targeted guardrails, not standalone proof of broad superiority.

For each case record: pass/fail, largest correct decision, largest regression, and whether the result over-changed, under-changed or preserved the right work.

### B — full creative builds

Run all briefs in `creative-benchmark.json` with isolated fixtures and identical capabilities. Require a complete implementation, representative desktop/mobile renders, real supplied assets/evidence, no invented proof, and a concise list of checks actually performed.

For each pair, Reviewer C reports preferred result (`X`, `Y`, or tie), reliability, creative performance, largest advantage/weakness of each, and confidence.

After the batch, review each anonymous system as a set. Fail a system whose unrelated pages repeatedly share the same governing idea, composition grammar, type/imagery/motion language, or anti-default aesthetic without brief-driven reasons. Also fail systematic loss of relevant richness or mobile quality.

## Decision rule

Prefer the candidate only when all are true:

1. no severe truth, authority or evidence-fit regression;
2. behavioral regressions show no systematic loss of continuity, pivot discipline, decision coverage or anti-template balance;
3. blind creative preference is at least non-inferior overall;
4. no material mode-collapse, completeness or mobile regression appears across the creative batch;
5. any added or saved runtime cost is proportionate to outcome quality.

A practical minimum bar is: no severe behavioral failure; at least 12 of 14 behavioral cases pass, including `category-default-is-earned`, `existing-page-needs-create-depth`, `inactive-medium-does-not-need-a-plan-field`, and `research-value-has-ended`; creative builds win more pairs than they lose; and CI passes.

These are experiment policy, not statistical significance claims.

## Iteration rule

When the candidate loses, identify the failure mechanism first: missing guidance, excessive guidance, salience/context competition, false proxy, anti-template overcorrection, over-compression, missing decision coverage, or flawed eval. Change the smallest relevant runtime surface and rerun the failed case plus neighboring regressions. Changes to creative direction/composition require diverse creative-build reruns before acceptance.

Do not add rules because one output is aesthetically disliked. Require a recurring failure mechanism or a clear missing decision.