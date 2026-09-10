# References studied and what was taken from each

Read on 2026-09-10. Each entry: what it is, what transfers to research skills, what does
not.

## devanity-skills — `TriangulosTecnologia/devanity-skills`

Skills *maestro* (software-change lifecycle), *archer* (architecture), *guardian*
(repository quality); agents *worker* (collects evidence, does not decide) and *verifier*
(independently tries to falsify a change, does not edit). Installed with
`npx skills add TriangulosTecnologia/devanity-skills --skill <name> --agent claude-code`.

**Transfers.**
- Form of `SKILL.md`: frontmatter, ownership and explicit non-ownership, numbered
  invariants, phases with gates, delegation, `reference/` files for the long material.
- "One evolving Change is the lifecycle source of truth; plans, matrices, summaries, PR
  text … are projections." → the protocol is the source of truth; every other document is
  a projection.
- "Evidence is something read or run against an identified target; confidence is not
  evidence." → invariant 2 of `scientific-method`, verbatim in spirit.
- Named terminal states beyond success (`NO_CHANGE`, `BLOCKED`, `NOT_VERIFIED`,
  `INVALID_TARGET`) → research needs `INCONCLUSIVE` as a first-class outcome.
- The *verifier* contract: independent, non-editing, treats the implementer's reasoning
  as untrusted narrative, looks for the falsifying observation first, fixed output
  headings → the whole shape of `reviewer-2`.
- Evals in three layers (regression, adversarial, holdout) measuring first-pass yield.

**Does not transfer.** Software vocabulary (Change Contract, delta, target identity);
`disable-model-invocation: true` — research skills must fire when the model recognises a
phase trigger.

## aicp — `tomieiro/aicp-skill`

A semantic map (`AICP.aicp`) as "an operational index of the repository": pointers to
architecture, contracts, invariants, evidence and verification commands, with the code as
source of truth; modes `init`, `review`, `validate`, `update`; "the skill does not replace
code, tests or specialised documentation".

**Transfers.** The map-as-index concept and the `validate` mode → `research-map`. The map
points to the protocol, notebooks and aggregates; `validate` checks that quoted numbers
exist in committed files, decisions have revision conditions, citations resolve, and
notebooks carry no outputs.

**Does not transfer.** The ACS compact syntax and the software-oriented record types.

## i-have-adhd — `ayghri/i-have-adhd`

Ten output rules for coding assistants: lead with the next action, number steps, end with
one concrete next step, suppress tangents, **restate state every turn** ("the reader
cannot hold 'we are on step 3 of 5' between messages"), concrete estimates, visible wins,
matter-of-fact errors, ranked short lists, no preamble or closers.

**Transfers.** Rule 5 describes the agent across sessions, not the user: it becomes the
`research-map` session ritual (restate state at start, record state at end). Rules 1 and 3
fix the agent's long-report habit. Rule 10 as house style.

**Does not transfer.** The rest is output formatting for a different audience.

## explorer — local skill (Ennio Politi Lopes)

Structural exploration agent: admit the problem; model before proposing; plan coverage;
diverge in independent branches; require a **bridge certificate** (source structure,
target correspondences, preserved relations, limits, insight, marginal gain, evidence,
failure condition and discriminating test); evaluate with non-compensatory gates; keep
lineages; close the loop; deliver for decision; stop explicitly.

**Transfers.** Used as-is for phase 1. Each surviving lineage becomes a hypothesis; its
"discriminating test" becomes the hypothesis's primary test; its "failure condition"
becomes the refutation clause.

**Does not transfer.** Nothing is rewritten; the skill is declared a dependency.

## Claude Science — Anthropic, beta 2026-06-30

An AI workbench for life sciences: 60+ skills and connectors for genomics, single-cell,
proteomics, structural biology, cheminformatics; persistent kernels; session forking;
provenance per artifact ("the exact code and environment that produced it, a
plain-language description of how it was created, and the full message history"); a
reviewer agent that "checks citations and calculations, flagging incorrect citations,
untraceable numbers, and figures that don't match their underlying code".
Sources: anthropic.com/news/claude-science-ai-workbench; hpcwire.com (2026-06-30).

**Transfers.** Two principles: provenance per artifact (the origin case has it per commit,
not per figure — add figure-level provenance to phase 6) and the reviewer's figure ↔ code
↔ data check (added to `reviewer-2`).

**Does not transfer.** Its skills are domain packages for biology; none applies to social
research with administrative data.
