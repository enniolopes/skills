# Runtime context policy

Treat `skills/branding-studio/` as executable context, not documentation about the project.

A runtime block belongs there only if it does at least one of these:
- changes execution behavior or a decision boundary;
- supplies domain knowledge needed during execution;
- defines canonical persistent state;
- enables deterministic runtime verification.

Move or remove content that only:
- explains release history or architecture rationale;
- describes evals, tests, packaging or repository development;
- restates a global rule already canonical in `SKILL.md`;
- documents one host/framework rather than expressing a portable capability requirement;
- materializes optional branding frameworks that do not change the current decision.

Keep one canonical home per rule:
- `SKILL.md` = global objective, workflow, evidence/authority boundaries, quality target, routing and state principles;
- `references/` = intent/domain deltas loaded only when needed;
- `templates/` = canonical state shapes;
- runtime `scripts/` = machine-checkable checks used while operating the brand;
- `development/` = human documentation, tests, evals, packaging and source-quality checks.

Before accepting runtime prose, ask:
1. Would removing this change a correct execution or remove necessary domain knowledge?
2. Is the same decision rule already canonical elsewhere?
3. Is this needed for every mission or only one intent/domain?
4. Is it written as executable guidance rather than project commentary?
5. Does it improve correct decisions more than it consumes model attention?
6. Is it a generative decision rule, or merely a list of familiar cases that a smaller rule could span?
7. Is an optional framework being promoted into a required schema field without evidence that all brands need it?

Prefer the minimum sufficient context. Keep examples when they improve decoding, reveal boundaries or serve as falsifiers; do not let examples become the source of truth when a smaller decision rule exists.

Move machine-provable requirements into deterministic checks. Do not duplicate an enforced rule in prose unless the prose explains when/why the operator should care about the check.
