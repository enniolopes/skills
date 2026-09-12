# Proxy audit — 2026-09-11

This is **L2 proxy evidence**, not an independent model benchmark. The current environment had no `claude`/`codex` executable and no Anthropic/OpenAI API credentials, so separate A/B agent runs could not be spawned. Do not treat this document as proof that v3.3 outperforms v3.1.

The audit was still useful for finding design flaws in the experiment itself.

## What was actually tested

1. Repository/CI structural validation.
2. Instruction audit against v3.1 and the experimental branch.
3. Proxy execution of the natural-language cases in `behavioral-evals.json`, judging expected behavior rather than taxonomy recall.
4. Cross-domain concept stress using `creative-benchmark.json` to detect obvious house-style/mode-collapse pressure.
5. Eval-quality audit against Anthropic skill-creator guidance: avoid non-discriminating assertions, distinguish subjective evaluation, and use blind comparison when a real runner is available.

## Findings that changed the skill

### 1. v3.2 control reference was too large

The first `control.md` was about 10 KB and was routed for every CREATE/major REFINE. That risked making process salience compete with discovery, marketing and design judgment.

Change: compress the control reference and load it at DIRECT / pivot points instead of as an early always-needed procedure.

### 2. v3.2 was too top-down

The first model allowed browser evidence to reopen a direction, but did not clearly state that making itself can reveal a stronger proposition or page framing.

Change: add bidirectional learning. Creative work may generate an upstream hypothesis; it must then be checked against product evidence and authority. Creativity may discover strategy; it may not invent truth.

### 3. the first behavioral evals were overfit

Several criteria explicitly required terms such as FOUNDATION, INTENT, DIRECTION and RE-DIVERGE. That primarily tested recall of the new taxonomy.

Change: rewrite behavioral evals around observable outcomes, with no requirement to use internal control vocabulary.

### 4. repeated local patches need escalation logic

A design can fail without one dramatic falsifier: many individually reasonable exceptions can accumulate because the shared system or governing idea is wrong.

Change: repeated downstream exceptions now count as evidence to question the next upstream decision instead of continuing to patch locally.

## Proxy behavioral comparison

Legend: PASS = runtime directly supports the desired behavior; PARTIAL = behavior is plausible but under-specified; FAIL = important mechanism is absent or pushes the opposite way. This is an instruction-level proxy, not measured model success.

| Case | v3.1 proxy | v3.3 proxy | Main difference |
|---|---|---|---|
| local mobile fix | PASS | PASS | both already protect local repair |
| wrong category meaning | PARTIAL | PASS | v3.3 explicitly abandons a governing idea that creates wrong meaning |
| repetitive middle page | PASS | PASS | both support composition-level correction |
| conversion model changes | PARTIAL | PASS | v3.3 propagates a changed page decision downstream |
| claim becomes false | PASS | PASS | truth invariant already strong |
| late better idea | PARTIAL | PASS | v3.3 compares against intent rather than sunk cost |
| novelty/3D is not progress | PASS | PASS | technical ambition already had to earn cost |
| generic but polished | PASS | PASS | v3.1 already has strong anti-generic review; v3.3 makes conceptual re-divergence clearer |
| creative discovery improves proposition | FAIL/PARTIAL | PASS | new bidirectional-learning rule is the main v3.3 gain |
| too many local exceptions | PARTIAL | PASS | v3.3 treats recurring patch pressure as upstream evidence |
| expressive fashion brief | PASS | PASS | v3.3 must not reduce domain-specific freedom |
| premium request on resolved page | PASS | PASS | convergence/stop rules already strong |
| mobile needs different expression | PASS | PASS | mobile-as-composition already strong |
| render beats plan | PASS | PASS | rendered output was already visual truth |

The experiment therefore appears additive mainly around **productive change**, not routine QA.

## Cross-domain creative stress

The proxy generated materially different governing territories for the eight benchmark briefs:

- experimental fashion — cut/reassembled editorial proof-sheet logic driven by garment photography and construction notes;
- industrial robotics — spatial choreography of the robot cell, CAD/collision proof and cycle-time movement;
- children astronomy — night-expedition/mission-log progression balancing wonder with parent trust;
- luxury fragrance — olfactory score and material sequence, sparse and sensory rather than explanatory UI;
- litigation intelligence — evidentiary chronology with source attachment and documentary trust;
- grid battery hardware — physical scale and thermodynamic flow from module to site to grid;
- neighborhood arts festival — poster/program/wayfinding grammar unfolding into map and schedule;
- developer runtime — code-to-trace-to-replay narrative using actual execution evidence.

At concept level there was no obvious single visual lineage. Some structural ideas recur where the domain justifies them (chronology/trace), which should not itself count as mode collapse.

This does **not** establish rendered design quality. Independent A/B runs remain required.

## Current verdict

v3.3 is a better experimental hypothesis than the original v3.2 because it is:

- lighter in runtime context;
- less schema-like;
- explicitly bidirectional rather than purely top-down;
- more tolerant of intuitive exploration;
- better at detecting when repeated local failure points upstream;
- tested with less taxonomy-overfit evals.

Do not merge based on this proxy audit alone. The next evidence threshold is L3: independent, blinded v3.1 vs v3.3 runs on the behavioral cases plus rendered outputs for the creative benchmark.
