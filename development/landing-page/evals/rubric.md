# Landing Page evaluation rubric

Use this rubric to compare the current experiment against v3.1 or another baseline. Keep reliability and creative quality separate so process compliance cannot hide weaker work.

## Evidence levels for the evaluation itself

Do not overclaim what a test establishes.

- **L0 — structural:** repository/CI checks, file contracts, token budgets, JSON validity.
- **L1 — instruction audit:** whether the runtime actually encodes a behavior without contradiction, unnecessary duplication or missing decision coverage.
- **L2 — proxy execution:** one model/session simulates or grades behavior. Useful for finding obvious flaws, but not independent evidence of model improvement.
- **L3 — independent A/B:** separate model runs on identical briefs, version identity hidden from the reviewer. Required before claiming the new skill is behaviorally better.
- **L4 — real project:** repeated performance on actual landing-page work with rendered/browser evidence.

A version should not merge merely because it passes L0–L2.

## Evaluation rule

Judge the **rendered/resulting page and the trajectory**, not prose that repeats the skill vocabulary. The evaluator should not require terms such as TRUTH, INTENT, DIRECTION, RE-DIVERGE, counterfeit quality or basis-form to appear. Credit the behavior, not the taxonomy.

Do not collapse the dimensions into one fake-precision score. Prefer dimension-level judgments and blind pairwise comparison.

## A. Reliability / control

### Truth and authority

Pass when factual claims, proof and business commitments stay within available evidence/authority. Fail on invented customers, metrics, capabilities, integrations, guarantees or strategy.

### Evidence fit

Pass when the agent uses the kind of evidence capable of settling the material question: product evidence for facts, professional judgment for design, rendered/browser evidence for artifact behavior, and real behavioral evidence or experiments for causal market outcomes. Fail when one evidence type masquerades as another.

### Decision-basis integrity

Pass when the agent generalizes from compact decision rules to novel cases without treating examples or checklists as exhaustive specifications. It should not force irrelevant media/fields, conflate creative choice with evidence status, choose workflow depth solely from artifact existence, or keep researching when additional information cannot materially change a decision.

Fail when abstraction removes necessary nuance or when case-lists continue to act as parallel sources of truth. A compact instruction is not better if the resulting behavior becomes ambiguous, incomplete or less creative.

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

### Resolution vs. counterfeit quality

Pass when premium, sophistication, creativity, coherence and delight are materially present in the artifact rather than merely signaled by familiar style cues, surface polish, novelty, complexity, repetition or component uniformity.

Do **not** penalize a familiar device merely because it is familiar. A serif, dark field, gradient, centered hero, cards, 3D, unusual navigation or any other mechanism may be excellent when the brief independently earns it. Fail when the mechanism substitutes for the underlying quality; also fail when the experiment develops a reflexive anti-default aesthetic.

### Inventiveness under constraint

Does the agent discover non-obvious but relevant solutions when useful? Can it explore a wildcard without confusing unusualness with quality?

### Creative adaptability

Can a better late idea or rendered failure lead to a genuinely stronger concept without losing valid truth and purpose?

### Craft

At macro, meso and micro scale, does the work improve under inspection? Are type, crops, alignment, states, responsive behavior and section joins resolved rather than approximate?

## C. Anti-rigidity / creative freedom

Fail the experimental version if control or compression improvements cause any of the following:

- unrelated outputs converge on one recurring aesthetic;
- anti-generic rules create a recurring "anti-AI" aesthetic just as rigid as the defaults they were meant to prevent;
- valid category or brand conventions are rejected merely because they are common;
- a compact basis becomes so abstract that the model loses useful domain detail;
- optional expressive media become mandatory schema fields or, conversely, relevant media are ignored because they are not named centrally;
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
5. Did attempts to avoid common AI/web defaults themselves converge on one repeated anti-default language?

Individually polished but repetitively authored outputs fail creative generalization, whether the repeated style is conventional or deliberately unconventional.

## E. Blind comparison protocol

For a real v3.1 vs experimental comparison:

- snapshot v3.1 and the experimental runtime separately;
- run the same prompt, files, tools and capability envelope independently;
- hide version identity and process transcript from the reviewer when possible;
- inspect desktop and mobile rendered output when available;
- judge Reliability and Creative Performance before stating a preference;
- name the largest advantage and largest regression of each output;
- repeat enough cases to detect variance rather than trusting a single win.

Prefer the experiment only when control/compressibility improve **without material loss of specificity, conceptual strength, expressive range, completeness or craft**.

## F. Eval-quality checks

Before trusting a benchmark, inspect the benchmark itself:

- criteria should describe observable outcomes, not quote the new skill's taxonomy;
- a criterion that both versions trivially pass adds little evidence;
- a scenario written directly from a new instruction can overfit the experiment;
- negative-control cases must test both rejection of an unjustified proxy and preservation of the same mechanism when the brief legitimately supports it;
- basis-form cases must test novel/boundary behavior, not reward repetition of the abstract rule;
- subjective design quality should be judged qualitatively/blind, not converted into pseudo-objective assertions;
- long-horizon continuity requires actual multi-step execution when a runner is available; a setup paragraph is only a proxy.

The success condition is not “shorter” or “more compliant.” It is:

**more coherent across long execution, more capable of productive change, less likely to mistake familiar signals for quality, more decisions derivable from fewer non-overlapping rules, and at least as surprising, specific and art-directed as the strongest baseline run.**
