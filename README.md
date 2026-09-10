# skills

Agent skills, agents and the systems that compose them, by Ennio Politi Lopes. Built for
Claude Code following the [Agent Skills](https://agentskills.io) standard. Every unit
installs on its own:

```bash
npx skills add enniolopes/skills --skill <name> --agent claude-code
```

Hosts that take a directory: copy `skills/<name>/`. Hosts that take a `.skill` or ZIP
upload: build it from `development/<name>/` when a packager exists there.

## Catalog

| Unit | Kind | Status | Docs |
|---|---|---|---|
| [branding-studio](skills/branding-studio/) | skill | shipped | [README](development/branding-studio/README.md) |
| [landing-page](skills/landing-page/) | skill | shipped | [README](development/landing-page/README.md) |
| [explorer](skills/explorer/) | skill | shipped | — |
| [research](systems/research/) | system | design | [design](development/research/design/) |

CI checks this table against the filesystem: it lists exactly the units that exist.

## Model

Three concepts, one rule each.

- **Unit** — a skill, an agent or a system. It has a name, a version, an owner and a reason
  to change that is its own. The name is the same everywhere the unit appears.
- **Runtime** — what a unit ships. Its location is fixed by the standard and by installers
  that copy it wholesale: `skills/<name>/` (with `SKILL.md` at the root) and
  `agents/<name>.md`. Runtime carries exactly what the agent needs while operating, no
  more, and never refers back to this repository; it must work installed alone.
- **System** — a composition of skills and agents that work together. It has no runtime
  of its own: `systems/<name>/system.json` names the pieces and their status, and CI
  checks that against what exists. Pieces install independently; a system may depend on
  a standalone skill.

Everything a unit needs that is not runtime — tests, evals, packaging, source policy,
design records, its human README — lives in one place, `development/<name>/`, so a unit
occupies at most two regions of the tree and deleting it means deleting two directories.

```text
skills/<name>/            runtime skill
agents/<name>.md          runtime agent
systems/<name>/           system.json + README.md
development/<name>/       everything else about the unit — never shipped
development/validate.py   the model above as executable checks
```

Design decisions and their rationale:

| Decision | Because | Revise when |
|---|---|---|
| Top level is the *role* (runtime, composition, development), unit name second | the runtime path is dictated by installers; given that, the only choice is where the rest goes, and one companion directory per unit keeps change local | an installer accepts a nested runtime directory, which would allow unit-first layout |
| Runtime contains no README, tests or evals | installers and packagers copy the directory as-is; every file becomes context or payload | never — this is the contract with the host |
| Systems are manifests, not containers | pieces version and install separately, and a system may include a skill that exists on its own | a host offers a real multi-piece install unit (e.g. a plugin marketplace); then `system.json` gains a projection to it |
| One validator, one workflow, discovery by convention | adding a unit must not require touching CI; `development/<name>/tests/` is found and run | a unit needs a toolchain other than Python |
| Version and license in each `SKILL.md` frontmatter | the installed artifact is the whole unit; identity and terms travel with it | — |

New top-level directories and new roles are architecture decisions: the validator lists
the allowed set and fails on anything else, so the change and the rule land together.

## Development

```bash
python development/validate.py
```

That is also what CI runs on every pull request. It checks the topology, each unit's
frontmatter contract, each `SKILL.md` against the 5,000-token budget (Claude Code's
auto-compaction re-attaches only that much of an invoked skill; depth beyond it goes into
`references/`), each system's manifest against the filesystem, the catalog above, relative
links, then compiles the Python and runs every `development/<name>/tests/`.

Per-unit tooling lives with the unit, e.g. `python development/branding-studio/package_skill.py`
builds `dist/branding-studio.zip`.

## License

[CC BY-NC 4.0](LICENCE). Each runtime unit repeats the license in its frontmatter.
