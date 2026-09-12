# skills

Portable Agent Skills, agents, and systems by Ennio Politi Lopes.

The repository is **Agent-Skills-first**: capability behavior lives in one canonical runtime, while host-specific installation and packaging stay thin and disposable. A skill should not need a ChatGPT, Claude, Gemini, or DeepSeek fork.

## Use

### ChatGPT

Where Skills are enabled, upload a released skill archive from **Plugins → Skills → Create → Upload from your computer**.

Workspace admins can import `https://github.com/enniolopes/skills` as a plugin marketplace from **Workspace settings → Plugins → Add → Import marketplace**. ChatGPT currently accepts Claude-compatible `.claude-plugin/marketplace.json` manifests and can keep them synced from the repository.

### Claude Code

Add the marketplace once, then install the unit you need:

```text
/plugin marketplace add enniolopes/skills
/plugin install <name>@enniolopes
```

A standalone skill can also be installed directly with an Agent Skills client such as:

```bash
npx skills add enniolopes/skills --skill <name> --agent claude-code
```

### Gemini CLI

Gemini CLI supports the Agent Skills standard directly and can install a skill from this repository:

```bash
gemini skills install https://github.com/enniolopes/skills.git --path skills/<name>
```

### Deep Code and other Agent Skills hosts

Install or copy `skills/<name>/` into the host's Agent Skills location. Deep Code, for example, discovers user skills under `~/.agents/skills/<name>/` and project skills under `.deepcode/skills/<name>/`.

For hosts that accept uploaded skills, use the GitHub Release archive for the skill. The archive is only a transport form of the same canonical runtime.

## Repository model

Four concepts cover the repository.

- **Skill** — reusable on-demand expertise or workflow. Runtime lives in `skills/<name>/` and follows the Agent Skills `SKILL.md` contract.
- **Agent** — a role with a real independent context, tool, authority, or evidence boundary. Standalone agents live in `agents/` when such a role actually exists.
- **System** — a composition of skills/agents that only makes sense as one installed or operated unit. Runtime lives in `systems/<name>/`; exclusive pieces stay inside the system and reusable pieces remain standalone dependencies.
- **Development** — tests, evals, fixtures, design evidence, packaging/release support, and other material that must never ship. It lives in `development/<name>/`.

The physical rule is simple:

```text
skills/<name>/                     canonical standalone skill runtime
agents/<name>.md                   standalone agent, only when independently justified
systems/<name>/                    composed runtime unit
development/<name>/                tests, evals and development evidence
.claude-plugin/marketplace.json    distribution projection for installable units
.github/workflows/                 repository validation and release automation
```

A unit should normally occupy one runtime region and, when needed, one `development/<name>/` companion region. Deleting a capability should delete a coherent part of the tree rather than leave copies across platform folders.

## Architectural rules

1. **One behavioral source of truth.** Never maintain platform-specific copies of a skill.
2. **Runtime is repository-independent.** Installed runtime cannot depend on `development/` or other repository-only paths.
3. **Topology follows ownership.** Add a new directory axis only when a real irreducible responsibility has appeared; do not pre-build abstractions for hypothetical consumers.
4. **Distribution is a projection.** Marketplace manifests, upload archives, and host paths distribute runtime; they do not own its semantics.
5. **Use host capabilities, not host vocabulary.** Runtime instructions describe operations such as inspect, search, render, generate, or execute and degrade honestly when a host lacks them.
6. **Mechanize only decidable properties.** CI proves installability and deterministic contracts; evals and field evidence judge behavior and quality.
7. **Generated artifacts leave Git.** Release archives are produced from reviewed source and published as artifacts/releases; automation never commits them back to `main`.

These rules keep maintenance closer to `skills + platforms` rather than `skills × platforms`: adding a host should not require editing every capability, and adding a capability should not require four host-specific implementations.

## Systems

Systems exist for composition, not because a workflow is large. Create one when several pieces need to be installed and operated as a single unit.

A system keeps pieces that are exclusive to it under its own `skills/` and `agents/`. If a piece becomes useful independently, promote it to the top-level catalog and make the system depend on it instead of copying it.

The current `research` system uses a Claude-compatible plugin manifest. That format is also consumable by ChatGPT marketplace import today. We do not invent a universal system manifest until another concrete composition surface makes that abstraction necessary.

## Development

Run the repository's deterministic contract locally with:

```bash
python development/validate.py
```

The same command runs in blocking CI. It is intentionally narrow: CI checks mechanically provable runtime integrity, manifests, syntax, and unit contracts. It does not grade prompt wording, creative quality, research quality, or architecture by proxy.

Behavior-changing revisions use the smallest relevant eval set under `development/<name>/evals/`. A targeted change should run cases capable of distinguishing that change; broad method or creative-system changes warrant broader representative evaluation. A passing structure check is never evidence that model behavior improved.

For all future AI-assisted creation, maintenance, review, and evolution work, follow [AGENTS.md](AGENTS.md). It is the repository-wide operating contract.

## Releases

Stable downloadable bundles are created from canonical standalone skill directories with the **release skill** GitHub Action.

The workflow:

```text
reviewed skills/<name>/
        ↓
repository validation
        ↓
archive the directory as-is
        ↓
GitHub Release: <name>-v<version>
```

It does not create a second manifest of runtime files and does not push generated output back to the repository.

## Evolving platform support

Agent Skills is the portability boundary for skills. Platform surfaces are expected to change faster than capability semantics.

When a host changes, first determine whether the canonical Agent Skill still works. If the change is only discovery, installation, manifest, or packaging, keep the fix at that edge. Introduce a new platform-specific surface only after a real incompatibility demonstrates that the existing standard cannot express what is required.

Volatile external compatibility checks should not block normal PRs. Add periodic compatibility automation only when an official or sufficiently stable check gives useful signal; otherwise rely on native host validation and field evidence.

## License

[CC BY-NC 4.0](LICENCE). Runtime units repeat the license in their own metadata where the host contract supports it.
