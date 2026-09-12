# Independent A/B protocol — landing-page v3.1 vs v3.4

Purpose: test whether v3.4 improves long-horizon coherence, productive pivot behavior, evidence fit and resistance to counterfeit quality without reducing creative strength or producing a new anti-default house style.

This protocol requires genuinely separate executor contexts and a blind reviewer. Do not use one conversation to role-play all three roles and call that independent evidence.

## Fixed versions

- **Baseline A:** repository `enniolopes/skills` at commit `d3b73f3911246ac7dfe7704e7abb5b86cda0eea0` (`main`, landing-page v3.1.0).
- **Candidate B:** repository `enniolopes/skills` at commit `67375954742ed3137451dfb2ee93b611380e445b` (`landing-page-v3.2-control-plane`, landing-page v3.4.0 experimental runtime).

Pin the commits. Do not let either executor see the other version or this comparison rationale.

## Agent roles

### Executor A — baseline

Use only `skills/landing-page/` from Baseline A. For every assigned task:
- inspect all supplied evidence;
- execute the landing-page task end-to-end using the skill;
- when a runnable project is supplied, build and render desktop/mobile;
- save implementation, screenshots, concise handoff, and any material unresolved gap;
- do not mention the skill version.

### Executor B — candidate

Same instructions and same inputs, but use only `skills/landing-page/` from Candidate B. Do not mention the skill version.

### Reviewer C — blind judge

Receive outputs as `X` and `Y`, with ordering randomized independently per task. Do not receive skill text, version identity, executor reasoning transcript, commit names, or branch names.

Judge the actual result and observable trajectory evidence. For rendered tasks, desktop/mobile output outranks prose claims.

For every pair report:
- preferred result: X / Y / tie;
- reliability: truth, evidence fit, continuity, correct scope of change, convergence;
- creative performance: specificity, governing idea, distinction, composition/rhythm, appropriate expression, resolution vs superficial quality signals, inventiveness, adaptability, craft;
- largest advantage of X;
- largest weakness of X;
- largest advantage of Y;
- largest weakness of Y;
- whether either result feels templated, like a recurring house style, or like a recurring anti-default style;
- confidence: low / medium / high.

Do not reward use of internal vocabulary such as `TRUTH`, `DIRECTION`, `RE-DIVERGE`, `counterfeit quality`, etc. Reward outcomes only.

## Battery A — behavioral continuation / pivot

Use the natural-language cases in `behavioral-evals.json`. Prioritize these six continuity/control cases first:

1. `wrong-category-meaning`
2. `conversion-model-changes`
3. `late-better-idea`
4. `creative-discovery-improves-proposition`
5. `too-many-local-exceptions`
6. `mobile-needs-different-expression`

Each executor receives identical setup material and prompt. For these tests, compare the proposed action/change and, when a fixture is runnable, the changed artifact.

Primary questions:
- Did the executor change enough to solve the real problem?
- Did it avoid changing more than evidence justified?
- Did it preserve valid solved work?
- Could it discover a better upstream hypothesis without inventing truth?

## Battery A2 — targeted negative-control regressions

Run these four cases after the continuity/control battery:

1. `premium-style-proxy`
2. `category-default-is-earned`
3. `component-uniformity-is-not-coherence`
4. `motion-is-not-delight`

These are targeted regression cases written close to the v3.4 hypothesis, so treat them as **guardrails**, not standalone evidence that v3.4 is broadly superior.

Check both directions:
- does the candidate reject a superficial proxy when it is substituting for the underlying quality?
- does it preserve the same mechanism when authoritative brand/product context genuinely earns it?

Fail the negative-control hypothesis if the candidate merely swaps common defaults for a repeated anti-default aesthetic, bans legitimate mechanisms, or becomes more process-heavy than the design problem warrants.

## Battery B — full creative builds

Use `creative-benchmark.json`. Minimum strong batch: all eight briefs.

For each brief, each executor gets an isolated copy of the same starter fixture/assets and the same capability envelope. Require:
- complete landing page implementation;
- representative desktop render;
- representative mobile render;
- real supplied assets/evidence where provided;
- no invented proof;
- concise handoff listing checks actually performed.

Reviewer C evaluates each pair blindly, then performs a batch-level mode-collapse review.

## Batch-level creative diversity review

After all eight briefs, Reviewer C examines all outputs from one anonymous system as a set, then the other set.

Ask:
- Do unrelated briefs produce materially different governing ideas?
- Do composition grammars vary for reasons tied to the domain/content?
- Are typography, imagery, motion and density repeatedly falling into one house style?
- Could three or more pages become each other through logo/copy/color replacement?
- Are recurring structures justified by usability/evidence, or are they defaults?
- Did attempts to avoid familiar AI/web patterns themselves converge on a repeated anti-default language?

A candidate fails this dimension if reliability improves but unrelated pages visibly converge, regardless of whether that recurring style is conventional or deliberately unconventional.

## Decision rule

Do not merge v3.4 because it wins process/compliance metrics or targeted negative-control cases alone.

Prefer v3.4 only when all are true:
1. it wins or ties the majority of the six continuity/control cases;
2. it shows no material truth/authority/evidence-fit regression;
3. the targeted negative-control battery shows no systematic proxy substitution or anti-template regression;
4. blind creative preference is at least non-inferior overall;
5. no material mode-collapse regression appears across the eight creative briefs;
6. any added time/token/runtime cost is proportionate to the quality gain.

A useful minimum bar before merge is:
- continuity/control: candidate wins >= 4 of 6 high-signal cases, with no severe regression;
- targeted negative-control: no severe failure and at least 3 of 4 cases satisfy the intended behavior, including `category-default-is-earned`;
- creative builds: candidate wins more pairs than it loses, ties allowed;
- diversity: no reviewer-detected house-style or anti-house-style regression;
- mobile: no systemic regression;
- CI/runtime validation passes.

These thresholds are experiment policy, not claims of statistical significance.

## Iteration rule

When v3.4 loses a case:
1. identify whether the failure is missing guidance, excessive guidance, salience/context competition, a false proxy, anti-template overcorrection, or a flawed eval;
2. change the smallest relevant skill surface;
3. rerun the losing case plus two neighboring regression cases;
4. after local recovery, rerun the full six-case continuity/control battery and the relevant negative-control guardrail;
5. after any change touching creative direction/composition, rerun at least four diverse creative briefs;
6. before merge, rerun the full eight-brief blind set.

Do not add rules merely because one output was aesthetically disliked. Require a recurring failure mechanism or a clear causal gap in the skill.
