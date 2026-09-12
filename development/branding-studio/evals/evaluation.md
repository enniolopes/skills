# Branding Studio — evaluation

Evaluate behavior and artifacts, not whether the model repeats runtime terminology. `cases.json` is intentionally small: each case represents a different failure mechanism, not a rule in the skill.

## Evidence levels

- **L0 — structural:** CI, packaging, syntax and deterministic-tool contracts.
- **L2 — proxy:** same-model or simulated comparison; useful for falsifying obvious regressions, not proving superiority.
- **L3 — blind A/B:** independent baseline/candidate runs on identical inputs, with runtime identity hidden from reviewers. Minimum useful level for a claim of better branding behavior.
- **L4 — real work:** genuine constraints, operators and external outcomes. Market/perception claims require their own evidence.

## Run

For a targeted change, run only the regression cases that can distinguish it. For a material creative-system change, also run the four creative briefs. Use the transfer test when guidelines or system handoff are affected.

Keep baseline and candidate isolated. Give them the same prompt, evidence and tools. Review artifacts before rationales whenever an artifact exists.

## Judge

Use six dimensions:

1. **Truth and evidence fit** — no invented reality; each claim uses evidence capable of settling it.
2. **Decision quality** — autonomy is appropriate; exploration, commitment and correction happen at the right level.
3. **Specificity** — consequential choices depend on this brand rather than category autocomplete or arbitrary novelty.
4. **Generativity** — the system can make materially different new work without copying one layout, phrase or device.
5. **Craft and reality** — representative artifacts survive perceptual, functional and production constraints relevant to the brief.
6. **Context efficiency** — extra process, rules or state must earn their cost; completeness and polish are not quality proxies.

Across creative briefs, flag repeated aesthetic or verbal solutions only when recurrence lacks brief-specific causality. Recurrence itself is not a failure.

## Decision rule

Promote a candidate only when the intended behavior difference is observable, no severe truth/authority/production regression appears, and creative quality is non-inferior overall. If baseline and candidate behave materially the same, do not add context. If a case rewards wording, a fixed template or one historical implementation rather than the underlying decision, fix the eval instead of the runtime.
