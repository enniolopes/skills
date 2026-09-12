# Landing Page evaluation rubric

Use this rubric to compare the current experiment against v3.1 or another baseline. Keep reliability and creative quality separate so process compliance cannot hide weaker work.

## Evidence levels for the evaluation itself

Do not overclaim what a test establishes.

- **L0 — structural:** repository/CI checks, file contracts, token budgets, JSON validity.
- **L1 — instruction audit:** whether the runtime actually encodes a behavior without contradiction or excessive duplication.
- **L2 — proxy execution:** one model/session simulates or grades behavior. Useful for finding obvious flaws, but not independent evidence of model improvement.
- **L3 — independent A/B:** separate model runs on identical briefs, version identity hidden from the reviewer. Required before claiming the new skill is behaviorally better.
- **L4 — real project:** repeated performance on actual landing-page work with rendered/browser evidence.

A version should not merge merely because it passes L0–L2.

## Evaluation rule

Judge the **rendered/resulting page and the trajectory**, not prose that repeats the skill vocabulary. The evaluator should not require terms such as TRUTH, INTENT, DIRECTION or RE-DIVERGE to appear. Credit the behavior, not the taxonomy.

Do not collapse the dimensions into one fake-precision score. Prefer dimension-level judgments and blind pairwise comparison.

## A. Reliability / control

### Truth and authority

Pass when factual claims, proof and business commitments stay within available evidence/authority. Fail on invented customers, metrics, capabilities, integrations, guarantees or strategy.

### Continuity of purpose

Pass when local decisions remain governed by the page job, proposition, proof and current creative idea across a long run. Fail when later regions drift into unrelated defaults without a reason.

### Causal diagnosis

Pass when the agent fixes the smallest level that explains a problem. Fail when it redesigns everything for a local defect or keeps polishing execution when the idea itself is wrong.

### Pivot quality

Pass when a material falsifier reopens enough of the solution to solve the real problem while preserving valid work. Fail when sunk cost protects a bad idea or every new possibility causes a restart.

### Upstream learning

Pass when making/prototyping can reveal a stronger truthful proposition or framing, which is then checked against evidence before adoption. Fail when earlier synthesis becomes dogma, or when creative intuition silently rewrites factual truth.

### Convergence

Pass when the agent commits long enough to make the page coherent, resolves material defects and stops when remaining changes are preference-level. Fail on endless churn or first-render shipping.

## B. Creative performance

Evaluate independently of A.

### Specificity

Does the page feel causally related to this product, audience, evidence and domain? Would a logo swap materially break the design logic?

### Governing idea

Is there a strong point of view that generates multiple coherent decisions beyond one decorative hero trick?

### Distinction

Is there a memorable signature for the right reason, rather than a recombination of current landing-page fashions?

### Composition and rhythm

Does the full page control hierarchy, mass, density, contrast, transitions and quiet/intense moments? Do later regions retain authorship?

### Appropriate expression

Do typography, imagery, color, motion and spatial behavior fit the brief's cultural/domain needs rather than a house aesthetic?

### Inventiveness under constraint

Does the agent discover non-obvious but relevant solutions when useful? Can it explore a wildcard without confusing unusualness with quality?

### Creative adaptability

Can a better late idea or rendered failure lead to a genuinely stronger concept without losing valid truth and purpose?

### Craft

At macro, meso and micro scale, does the work improve under inspection? Are type, crops, alignment, states, responsive behavior and section joins resolved rather than approximate?

## C. Anti-rigidity / creative freedom

Fail the experimental version if control improvements cause any of the following:

- unrelated outputs converge on one recurring aesthetic;
- internal state/control concepts become visible page templates;
- every idea must be fully rationalized before it can be tried;
- the first committed direction becomes immutable;
- strong late discoveries are rejected because implementation started;
- qualitative judgment is replaced by arbitrary numerical scoring;
- process compliance receives more attention than the rendered work;
- creative exploration is only allowed downstream of a fixed strategy, preventing making from revealing a stronger truthful framing.

## D. Cross-run mode-collapse test

Run the briefs in `creative-benchmark.json` as a batch. A blind reviewer should ask:

1. Are the governing ideas materially different where the briefs warrant it?
2. Do composition, type, imagery and motion derive from each domain rather than one skill-induced visual lineage?
3. Are recurring structures explained by usability needs or by fallback habit?
4. Could several outputs become variants of one template after swapping logo/copy/palette?

Individually polished but repetitively authored outputs fail creative generalization.

## E. Blind comparison protocol

For a real v3.1 vs experimental comparison:

- snapshot v3.1 and the experimental runtime separately;
- run the same prompt, files, tools and capability envelope independently;
- hide version identity and process transcript from the reviewer when possible;
- inspect desktop and mobile rendered output when available;
- judge Reliability and Creative Performance before stating a preference;
- name the largest advantage and largest regression of each output;
- repeat enough cases to detect variance rather than trusting a single win.

Prefer the experiment only when control improves **without material loss of specificity, conceptual strength, expressive range or craft**.

## F. Eval-quality checks

Before trusting a benchmark, inspect the benchmark itself:

- criteria should describe observable outcomes, not quote the new skill's taxonomy;
- a criterion that both versions trivially pass adds little evidence;
- a scenario written directly from a new instruction can overfit the experiment;
- subjective design quality should be judged qualitatively/blind, not converted into pseudo-objective assertions;
- long-horizon continuity requires actual multi-step execution when a runner is available; a setup paragraph is only a proxy.

The success condition is not “more compliant.” It is:

**more coherent across long execution, more capable of productive change, and at least as surprising, specific and art-directed as the strongest baseline run.**
