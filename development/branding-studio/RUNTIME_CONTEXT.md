# Runtime context policy

Treat `skills/branding-studio/` as executable context, not documentation about the project.

A runtime block belongs there only if it does at least one of these:
- changes execution behavior or a decision boundary;
- supplies domain knowledge needed during execution;
- defines canonical persistent state;
- enables deterministic runtime verification.

Move or remove content that only:
- explains what the skill is or why its architecture was chosen;
- describes development history, versions, evals, tests or packaging;
- restates a global rule already canonical in `SKILL.md`;
- documents a host/framework rather than expressing a portable capability requirement.

Keep one canonical home per rule:
- `SKILL.md` = global kernel, routing, gates, state and invariants;
- `references/` = intent/domain deltas loaded only when needed;
- `templates/` = canonical state shapes;
- runtime `scripts/` = deterministic checks used while operating the brand;
- `development/` = tests, evals, build tooling, source-quality checks and the human
  README (explanation, installation, use).

Before accepting runtime prose, ask:
1. Would removing this change a correct execution or remove necessary domain knowledge?
2. Is the same rule already stated canonically elsewhere?
3. Is this needed for every mission or only one intent/domain?
4. Is it written as executable instruction/constraint rather than project commentary?
5. Does it preserve uncertainty and verification boundaries without adding explanatory ceremony?

Prefer the minimum sufficient context. Runtime should be dense because each token earns its place, not because it repeats the architecture in multiple forms.
