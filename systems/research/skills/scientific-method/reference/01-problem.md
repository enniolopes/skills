# Phase 1 — Problem

Sources located 2026-09-10, not yet read at source.

**When this applies.** A research is being started, restarted, or its question is being
changed. Also whenever a hypothesis is added after the protocol exists (that addition is a
phase-1 act and goes through the same gate).

**What it requires.**

- **Budget before exploring.** Log a decision with the exploration budget: how many
  structurally different lineages (default three to five), how much time, and the stopping
  rule (revised saturation: no new lineage after the search ontology was revised once). Wide
  and fast is the goal; "as much as possible" is not a stopping rule.
- Invoke the `explorer` skill (`explorer:explorer` when installed from the marketplace) on
  the problem as stated, with that budget. Its output is a portfolio of lineages with
  bridge certificates. Each surviving lineage is a candidate hypothesis: its
  *discriminating test* becomes the hypothesis's primary test, its *failure condition*
  becomes the refutation clause.
- Write the **problem statement** (`reference/problem-statement.md`): claim kind and
  identification assumptions, unit of analysis, estimand, refutation, the obvious reviewer
  objection and the phase that answers it, how it is done today, what is new, who cares,
  non-goals, feasibility, success checks. It lives in the protocol, at the anchor the map's
  `## Question` points to; `validate` checks its seven required fields.
- State the uncertainty of every inference you intend to make, not only its direction.
- **Converge explicitly.** Adopt at most three hypotheses. Every surviving lineage not
  adopted goes to the map's `## Deferred` with the condition under which it would enter;
  nothing is silently dropped, nothing is silently kept open.

**The error it prevents.** A question that cannot fail; a hypothesis whose direction is a
matter of interpretation after the fact (a predicted sign that contradicts an index
convention already logged); a unit of analysis that shifts between the protocol and the
code; a term the protocol names and no code computes.

**Exit gate.** The exploration budget was logged before exploring; the problem statement
is complete and `validate` passes on it; lineages not adopted are in `## Deferred`.
Otherwise the phase is not closed.

**Sources.** King, Keohane & Verba, *Designing Social Inquiry* (one logic of inference;
state uncertainty; guard selection and measurement bias). Booth et al., *The Craft of
Research* (a claim needs reasons, evidence and an answer to the reader's objection).
