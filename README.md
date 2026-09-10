# skills

Agent skills, agents and the systems that compose them, by Ennio Politi Lopes. Built for
Claude Code following the [Agent Skills](https://agentskills.io) standard. The repository
is also a Claude Code plugin marketplace: every unit is one install.

```text
/plugin marketplace add enniolopes/skills
/plugin install <name>@enniolopes
```

A standalone skill can also be installed on its own, without the marketplace:

```bash
npx skills add enniolopes/skills --skill <name> --agent claude-code
```

Hosts that take a directory: copy `skills/<name>/`. Hosts that take a `.skill` or ZIP
upload: build it from `development/<name>/` when a packager exists there.

## Quick start

```text
/plugin marketplace add enniolopes/skills          # once per machine
/plugin install research@enniolopes                 # a system: skills + agent + dependencies
/plugin install branding-studio@enniolopes          # a standalone skill, when needed
```

Then, inside a research repository: `/research:research-map init` builds the map from the
protocol and decision log, and `/research:scientific-method start: <question>` begins at
phase 1. Each unit's README says how it is used; the research one is
[`systems/research/README.md`](systems/research/README.md).

## Catalog

| Unit | Kind | Status | Docs |
|---|---|---|---|
| [branding-studio](skills/branding-studio/) | skill | shipped | [README](development/branding-studio/README.md) |
| [landing-page](skills/landing-page/) | skill | shipped | [README](development/landing-page/README.md) |
| [explorer](skills/explorer/) | skill | shipped | — |
| [research](systems/research/) | system | built · acceptance pending | [README](systems/research/README.md) · [design](development/research/design/) |

CI checks this table and `.claude-plugin/marketplace.json` against the filesystem: both
list exactly the units that exist.

## Model

Three concepts, one rule each.

- **Unit** — a skill, an agent or a system. It has a name, a version, an owner and a reason
  to change that is its own. Names are unique across the repository.
- **Runtime** — what a unit ships. `skills/<name>/` (with `SKILL.md` at the root) and
  `agents/<name>.md`, the locations installers copy wholesale. Runtime carries exactly
  what the agent needs while operating, no more, and never refers back to this repository;
  it must work installed alone.
- **System** — several skills and agents that only make sense together, installed as one
  unit. A system is a Claude Code plugin: `systems/<name>/` holds its manifest, its README
  (how to install, how to use) and the pieces exclusive to it under `skills/` and
  `agents/`. A piece that is also useful alone is a standalone unit the system declares in
  `dependencies`; the host installs it transitively.

Everything a unit needs that is not runtime — tests, evals, packaging, source policy,
design records, its human README — lives in one place, `development/<name>/`, so a unit
occupies at most two regions of the tree and deleting it means deleting two directories.

```text
skills/<name>/                     standalone runtime skill; also a single-skill plugin
agents/<name>.md                   standalone runtime agent
systems/<name>/                    a plugin: .claude-plugin/plugin.json, README.md, skills/, agents/
development/<name>/                everything else about the unit — never shipped
.claude-plugin/marketplace.json    the catalog as the host reads it: one plugin per unit
development/validate.py            the model above as executable checks
```

Design decisions and their rationale:

| Decision | Because | Revise when |
|---|---|---|
| Top level is the *role* (runtime, composition, development), unit name second | the runtime path is dictated by installers; given that, the only choice is where the rest goes, and one companion directory per unit keeps change local | an installer accepts a nested runtime directory, which would allow unit-first layout |
| Runtime contains no README, tests or evals | installers and packagers copy the directory as-is; every file becomes context or payload | never — this is the contract with the host |
| A system is a plugin, its exclusive pieces live inside it | the host's install unit is the plugin, and a plugin cannot reference files outside its own directory; "install one thing" is the requirement | a host installs a multi-piece unit from a manifest that may point anywhere in the repository — then pieces return to the flat catalog and the system becomes a manifest again (the layout this superseded) |
| Standalone skills are single-skill plugins with `strict: false` | a `SKILL.md` at the plugin root is a plugin; `strict: false` keeps the manifest in the marketplace entry, so nothing non-runtime enters `skills/<name>/` | — |
| One validator, one workflow, discovery by convention | adding a unit must not require touching CI; `development/<name>/tests/` is found and run | a unit needs a toolchain other than Python |
| Version and license in each `SKILL.md` frontmatter and each `plugin.json` | the installed artifact is the whole unit; identity and terms travel with it | — |
| `SKILL.md` under 5,000 estimated tokens | Claude Code's auto-compaction re-attaches only that much of an invoked skill; depth beyond it goes to `references/` | the platform changes the mechanic |

New top-level directories and new roles are architecture decisions: the validator lists
the allowed set and fails on anything else, so the change and the rule land together.

## Development

```bash
python development/validate.py
```

That is also what CI runs on every pull request. It checks the topology, each runtime
piece's frontmatter contract and token budget (standalone or inside a system), each
system's `plugin.json` and its dependencies, the marketplace and the catalog above against
the filesystem, relative links, then compiles the Python, runs `claude plugin validate`
when the CLI is present, and runs every `development/<name>/tests/`.

Per-unit tooling lives with the unit, e.g. `python development/branding-studio/package_skill.py`
builds `dist/branding-studio.zip`.

## License

[CC BY-NC 4.0](LICENCE). Each runtime unit repeats the license in its frontmatter.
