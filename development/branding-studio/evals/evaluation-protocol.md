# Branding Studio v2 — evaluation protocol

Use this protocol to distinguish structural correctness from actual creative improvement.

## Baseline and candidate

Run the same prompt, source materials and tool capabilities against:
- **baseline** — current main/runtime before the v2 change;
- **candidate** — the v2 runtime under test.

Do not let the candidate see baseline outputs or vice versa. Do not repair one side manually.

## Evidence levels

### L0 — structural
Repository validation, unit tests, package boundary, JSON/script correctness and runtime-size constraints.

L0 can establish that the implementation is internally coherent. It cannot establish that branding behavior improved.

### L1 — instruction audit
Review whether runtime instructions encode the intended decision rules without contradiction, duplicate sources of truth, impossible preconditions or gratuitous case lists.

L1 is still not behavioral proof.

### L2 — same-model proxy execution
Use the same model/session setup to answer selected behavioral cases or creative briefs with baseline and candidate instructions separately. Useful for catching obvious regressions, but not independent evidence.

### L3 — independent blind A/B
Run baseline and candidate independently, randomize/obscure which is which, and have reviewers score the outputs using `rubric.md` without seeing implementation labels.

This is the minimum useful level for claiming that the candidate tends to produce better branding artifacts.

### L4 — real project
Use the candidate on real branding work with genuine constraints, operators and stakeholder/market contact. Evaluate whether the system is usable and whether predicted advantages survive reality.

Market/perception claims require their own real evidence; even a successful creative A/B is not customer research.

## Behavioral regression set

Run `behavioral-evals.json` across the cases most relevant to the code change. For a major release, cover the full set.

Score each case as:
- **PASS** — all material musts are present and must-nots absent;
- **PARTIAL** — behavior is directionally correct but a material requirement is weak/missing;
- **FAIL** — core behavior contradicts the case.

Do not reward the agent for printing runtime terminology. Evaluate behavior, not labels.

## Corpus-promotion gate

For changes derived from the branding corpus, run the targeted cases in `corpus-promotion-evals.json` before treating a new rule or reference as earned.

Use the file to test four distinct claims:
- failure-mode-aware test selection improves the information value of representative applications;
- that improvement does not inflate testing beyond the requested scope;
- specialized craft knowledge changes diagnosis or verification where the baseline is genuinely weak;
- verbal-system and brand-book knowledge improves downstream artifacts, not merely process vocabulary or document completeness.

A targeted case can justify promotion only for the decision it distinguishes. If baseline and candidate behave materially the same, do not promote the extra instruction merely because it is well supported by the literature.

## Creative benchmark

Use `creative-benchmark.json` for major changes to CREATE/creative-direction/identity-craft/brand-book behavior.

For each brief:
1. run baseline and candidate independently;
2. require comparable deliverables;
3. hide runtime identity from reviewers;
4. review artifacts before reading rationales;
5. score against the shared rubric;
6. record material reasons, not only numeric preference;
7. after individual scoring, compare all briefs for recurring aesthetic solutions.

## Cross-run mode collapse

Look across unrelated briefs for repeated solutions that are not independently earned, such as the same:
- palette family;
- typography pairing archetype;
- logo morphology;
- composition pattern;
- signature device;
- verbal attitude;
- anti-default aesthetic posture.

Recurrence is not automatically a failure; it becomes evidence when the mechanism has weak causal dependence on the briefs.

The runtime should not be asked to detect its own cross-run distribution. This is an evaluation responsibility.

## Acceptance criteria for v2

A candidate should not be considered behaviorally superior on L0/L1 evidence alone.

For L3 acceptance, require:
- no systematic regression in truth/evidence/authority boundaries;
- no increase in unnecessary user questioning;
- no systematic production-status overclaim;
- creative output preferred or non-inferior overall;
- improved or non-inferior specificity and generativity;
- no new recurring anti-AI/anti-category style mode;
- sparse state behavior without loss of necessary operating guidance;
- brand-book outputs more useful than spec serialization;
- correction scope remains local/systemic/strategic as appropriate.

A targeted regression case can falsify one behavior; it cannot by itself prove the whole runtime better.

## Reporting

For every evaluation report, record:
- baseline commit;
- candidate commit;
- model/host/tool conditions;
- prompts/brief IDs used;
- reviewer/blinding method;
- results by case/brief;
- observed regressions;
- uncertainty and evidence level.

Do not collapse L0 structural success into L3 creative superiority.
