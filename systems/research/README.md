# research

Scientific research system for Claude Code. Version 0.8 turns the plugin from a lifecycle prompt into an **epistemic control system**: creative exploration remains available, while consequential commitments, executions, inferences and claims leave inspectable artifacts and mechanical provenance.

Scope: observational quantitative research, especially administrative data.

## Install

```text
/plugin marketplace add enniolopes/skills
/plugin install research@enniolopes
```

The plugin depends on `explorer` and installs the rest as one system.

## One public entry point

Use:

```text
/research:scientific-method start <idea or question>
/research:scientific-method status
/research:scientific-method review [manuscript]
/research:scientific-method <normal research request>
```

Talk normally after `start`. The method invokes `research-map`, `statistical-analysis`, `research-graph`, `explorer` and `reviewer-2` internally. Direct component commands remain available for debugging/power use; normal users do not need a resume/update/validate ritual.

## Kernel

Five operations:

```text
EXPLORE → COMMIT → EXECUTE → JUSTIFY → CHALLENGE
```

Five laws:

1. **Evidence outranks narrative.** Read/executed evidence beats memory, confidence and explanation.
2. **Commitment precedes exposure.** Choices a result could influence are recorded/frozen before that exposure.
3. **Discovery is not confirmation.** Data that materially generated a hypothesis do not independently confirm it.
4. **Claims require lineage.** A material claim traces through an explicit inference to identified result/source evidence and design.
5. **Material claims face an adversary.** The process that built the claim is not sufficient to release it.

The existing eight phases remain the research lifecycle: problem, literature, protocol, data, analysis, writing, review, publication. Preflights govern the action immediately before a consequential step.

## Problem first

Phase 1 remains the highest-leverage gate. It does not demand that the initial story be true. It frames the question, explores structurally distinct explanations/hypotheses under a budget, then tries to make the empirical premise disappear.

The problem state is:

```text
SHOWN | NOT_SHOWN | INCONCLUSIVE
```

`NOT_SHOWN` closes or reformulates before expensive modelling; it is a useful result. The system prevents the third-kind error: a precise answer to the wrong problem.

## Preflights

The method automatically runs the relevant boundary check:

- **FIT** — before a confirmatory result is exposed: estimand, primary test, assumptions/checks/failure actions, dependence, interpretation boundary, freezes, registration and data exposure must be coherent.
- **CHANGE_PLAN** — a post-freeze idea becomes `SPECIFICATION`, `EXPLORATORY`, `DEFERRED` or explicit `REOPEN`; never a silent rewrite.
- **CLAIM** — result/run/test/checks and interpretation boundary must support the material claim; hypothesis-deciding claims use the frozen primary test.
- **CITE** — DOI/URL identity is not semantic support; the relevant source content must be retrieved/read before supporting a proposition.
- **PUBLISH** — material claim lineage, review, disclosure/reporting and human-owned publication/ethics requirements must be complete.

## Authoritative artifacts

Each artifact has one job:

| Artifact | Owns |
|---|---|
| `protocol.md` | question, hypotheses, estimands and scientific commitments |
| `analysis-plan.md` | analytic commitments, decision rules and interpretation boundaries |
| `decisions.md` | methodological choices and revision conditions |
| code/notebooks | executable procedures |
| `.research/runs/RUN-*.json` | what ran, against what, under which frozen commits |
| `aggregates/` | computed results |
| `references.bib` + inspected source content | bibliographic identity/evidence |
| `RESEARCH.map` | one-screen operational state/navigation |
| `.research/graph.json` | disposable derived index of relations (rebuildable) |
| manuscript | scientific communication |
| reviewer output | adversarial challenge/adjudication evidence |

`RESEARCH.map` remains deliberately small. It never becomes a second protocol, result store or graph database.

## Analysis plan

Before confirmatory analysis, the method creates/reviews `analysis-plan.md`. Each hypothesis block carries stable IDs:

```text
H1 hypothesis
E1 estimand
T1 primary test
A1 assumption
K1 check
```

and records `Generated from:`, dependence, decision rules, `A → K → failure action`, sensitivity/specification dimensions and `May claim` / `May not claim`.

`statistical-analysis` starts from:

```text
QUESTION → CLAIM TYPE → ESTIMAND → IDENTIFICATION/DESIGN → DATA STRUCTURE
→ DEPENDENCE → ESTIMATOR → INFERENCE → DIAGNOSTICS → SENSITIVITY → INTERPRETATION
```

It does not route `binary → logistic` or `count → Poisson` by reflex. Method-specific policy is added only from primary sources that have actually been read for the condition encoded.

The initial 0.8 statistical references cover estimands, exploratory-analysis boundaries, dependence and missingness. Families of estimators are added only when real research/evals justify them.

## Temporal provenance

A prose statement that something was pre-specified is insufficient. Every material run records:

```json
{
  "id": "RUN-001",
  "mode": "confirmatory",
  "analysis_role": "primary",
  "commit": "<execution commit containing the result artifact>",
  "protocol_freeze": "<earlier commit>",
  "analysis_plan_freeze": "<earlier commit>",
  "hypothesis": "H1",
  "estimand": "E1",
  "test": "T1",
  "registration": "https://registry.example/record",
  "inputs": [
    {"id": "DATA2", "path": "data.csv", "role": "confirmatory"}
  ],
  "outputs": [
    {"result": "R1", "artifact": "aggregates/h1-primary.csv"}
  ]
}
```

`analysis_role` is one of `primary | sensitivity | specification | diagnostic`. A confirmatory `primary` run must use the frozen primary test. Other confirmatory roles are allowed only when their test ID was already named in the frozen analysis plan and cannot decide the hypothesis.

The validator checks Git ancestry and verifies that input/output paths existed at the run commit. A result artifact is anchored to its run commit: silently changing the current aggregate under the same R<n> fails validation. A changed result needs a new run/result identity (or restoration of the committed artifact).

Historical analyses with no trustworthy temporal evidence remain `NOT_VERIFIED` on that property; the system never fabricates a historical freeze.

## Discovery exposure

Datasets use stable `DATA<n>` IDs and run input roles:

```text
discovery | confirmatory | validation
```

If H1 was materially generated from DATA1, a confirmatory run of H1 using DATA1 as independent confirmatory evidence is rejected. Registration after exposure does not erase exposure. The work can remain exploratory, use defensible held-out/independent evidence, or reopen the design.

## Claim lineage and graph

Material claims are annotated near the prose:

```text
<!-- claim:C1 inference:I1 result:R1 -->
<!-- claim:C2 inference:I2 result:R2 decides:H1 -->
```

`research-graph` derives a disposable graph from authoritative artifacts. Its core nodes are hypotheses, estimands, tests, assumptions/checks, decisions, datasets, runs, results, inference/warrants, claims and sources.

A claim path is approximately:

```text
H/E ← T → RUN → R → I → C
```

`I` is important: a result does not magically imply a sentence. The inference/warrant is the public bridge from result + design/checks to wording. Mechanical validation proves lineage structure; `reviewer-2` attacks whether that bridge is scientifically adequate.

Graph views (`trace`, `argument`, `why`, `changed`) are navigation/mind-map/argument-map projections, never sources of truth. `.research/graph.json` is rebuildable.

## Validation

`research-map validate` composes the original 0.7 checks with four 0.8 checks.

Existing:

```text
map · numbers · decisions · disclosure · citations · notebooks
```

Added:

```text
plan · runs · lineage · exposure
```

Run directly when debugging:

```text
python3 <installed research-map>/scripts/validate_all.py RESEARCH.map --offline
```

`PASS` means only that coded invariants passed. It does **not** mean the design, estimator, source interpretation or claim is scientifically true.

## Adversarial review

`reviewer-2` is independent and non-editing. It starts from material claim lineage rather than author explanation, looks for the falsifying observation first, inspects temporal provenance, data exposure, primary-test use, estimator/estimand fit, checks, aggregates/code, source entailment and reporting checklists.

Its fixed output remains:

```text
VERDICT
CLAIMS
FINDINGS
CHECKS RUN
NOT_VERIFIED
BASIS
```

The same agent that built a claim is not sufficient evidence for accepting it.

## Behavioral efficacy is measured, not assumed

`development/research/evals/scenarios.json` contains eight safety mechanisms plus three liveness mechanisms. The harness generates reproducible Git-backed repository fixtures and runs the same prompt/model under isolated conditions:

```text
CONTROL   Claude Code bare mode, no research/explorer plugin
TREATMENT Claude Code bare mode, local research + explorer loaded explicitly
```

Bare mode prevents globally installed plugins, hooks, memory, CLAUDE.md and other host configuration from contaminating the comparison. The harness verifies the `system/init` plugin list before adjudication; an invalid/missing treatment plugin or contaminated control becomes an eval-infrastructure `NOT_VERIFIED`, not a research result.

The runner never receives `expect`. A separate **condition-hidden** judge receives the completed transcript/diff/validator output and criterion only after the run. The transcript can reveal plugin/tool names, so this is not claimed as perfect perceptual blinding; the judge is explicitly instructed not to reward plugin vocabulary. Repetitions are required because model behavior is nondeterministic.

Dry-run harness:

```text
python development/research/evals/run.py --scenario assumptions-before-fit --condition both
```

Execute and judge (incurs Claude/API usage):

```text
ANTHROPIC_API_KEY=... python development/research/evals/run.py \
  --scenario assumptions-before-fit --condition both --repetitions 3 --execute --judge
```

The scripted harness uses Claude Code `--bare`; for Anthropic API execution that means provider credentials rather than subscription OAuth. Raw eval run artifacts are ignored by Git. Adjudicated summaries can be committed separately. The existence of scenario specifications is not evidence that the plugin passes them.

## Release discipline

A new runtime rule needs a distinct failure mechanism. Prefer the smallest artifact/check/state that prevents the mechanism; otherwise leave it to adversarial judgement or drop it. Do not accumulate good-practice prose.

0.8 is mechanically releasable only when repository validation/unit tests pass. Claims of behavioral uplift additionally require adjudicated control/treatment runs with no material liveness regression.

## Pieces

| Piece | Role |
|---|---|
| `scientific-method` | single public orchestrator; lifecycle + five laws + preflights |
| `research-map` | operational memory + composed mechanical validation |
| `statistical-analysis` | estimand-first analysis planning and EDA boundary |
| `research-graph` | derived epistemic lineage and query views |
| `reviewer-2` | independent non-editing adversarial review |
| `explorer` | structural divergence/hypothesis generation dependency |

## Non-goals

0.8 is not an autonomous scientist, automatic truth verifier, complete statistical library, universal knowledge graph, GUI graph editor, multi-agent society or automatic paper author. Those capabilities enter only when an observed failure mechanism demonstrates that the additional complexity is necessary.
