# Contributing

This repository is Agent-Skills-first. Keep the reusable capability stable and platform-neutral; treat host-specific installation and packaging as thin distribution concerns.

## Classify the change first

Choose the smallest durable owner for the behavior.

- **Skill** — reusable expertise or workflow that can operate as an on-demand capability. Put its runtime in `skills/<name>/` and follow the Agent Skills `SKILL.md` contract.
- **Agent** — an execution role that needs its own context, tool, authority, or evidence boundary. Add `agents/<name>.md` only when that boundary is real; do not use an agent as a larger skill.
- **System** — several skills or agents that only make sense as one installed/operated unit. Put exclusive pieces inside `systems/<name>/`; keep independently useful capabilities standalone and declare them as dependencies.
- **Development** — tests, evals, design evidence, fixtures, and development tooling. Put it in `development/<name>/`; it never ships as runtime.

Do not add a new top-level role for a platform or hypothetical future need. Add a structural axis only when an irreducible responsibility has appeared in real cases and has no clear existing home.

## Source-of-truth rules

1. Runtime behavior has one canonical home. Never fork a skill into ChatGPT-, Claude-, Gemini-, or DeepSeek-specific copies.
2. A runtime must work when installed independently of this repository. It must not depend on `development/` or repository-only paths.
3. Platform manifests and marketplaces are projections. They may point at canonical runtime, but they do not own capability behavior.
4. Generated archives and other release artifacts are build outputs. Do not commit them back to `main`.
5. Prefer capabilities over vendor tool names in runtime instructions. Describe the needed operation (`inspect`, `search`, `render`, `execute`, `generate`) and degrade honestly when the host cannot provide it.

## Change workflow

For a normal change:

1. Start from an observed need, failure, or explicit hypothesis.
2. Change the smallest canonical surface capable of fixing it.
3. Add or update deterministic tests only for machine-decidable contracts.
4. Run only eval cases that can distinguish the behavioral hypothesis; use broader benchmarks for broad method or creative-system changes.
5. Run `python development/validate.py`.
6. Open a PR with the intended behavioral/contract delta and the evidence actually obtained.
7. After merge, publish a release artifact only when a stable downloadable bundle is useful. Release workflows never rewrite source.
8. Use field evidence to decide whether another revision is warranted.

Do not add permanent prompt surface merely because a test can assert its wording. Test behavior and contracts, not prose shape.

## Tests and evals

Use the evidence type that can answer the question.

- **Unit tests / CI**: deterministic structure, schemas, references, scripts, package contracts, or other properties code can actually falsify.
- **Evals**: behavior or artifact quality where model judgment or human judgment is necessary.
- **Field evidence**: real use, recurrence, latency, context pressure, host differences, and other external reality.

One distinct recurring causal failure should normally map to one regression case. Do not create one test per runtime sentence or framework label.

## Platform compatibility

Agent Skills is the canonical portability contract for skills. Use native host support first.

When a platform changes:

1. determine whether the canonical skill still works;
2. if only installation, path, manifest, or packaging changed, fix that projection only;
3. add host-specific code or structure only when a real incompatibility cannot be expressed by the existing standard/runtime;
4. never change capability semantics merely to satisfy a distribution surface.

Compatibility automation should be added only when an official or sufficiently stable external check provides useful signal. Do not make normal PR CI depend on volatile `latest` host behavior.

## Release policy

Standalone skills can be published as archives of the canonical `skills/<name>/` directory. The archive is a transport format, not another source tree.

Use the `release skill` GitHub Action. It validates the repository, reads the version from the skill frontmatter, archives the canonical runtime, and creates a GitHub Release tagged `<skill>-v<version>` at the reviewed commit.

Systems remain host-composition artifacts until a second concrete composition standard earns a neutral abstraction. Do not invent a universal system manifest in advance.

## Definition of done

A change is done when:

- ownership and placement are unambiguous;
- there is no parallel source of truth;
- runtime remains independently installable;
- relevant deterministic checks pass;
- behavioral claims are no stronger than the evidence obtained;
- no generated artifact or platform projection has become the owner of capability behavior;
- any remaining assumption or compatibility limitation is explicit.
