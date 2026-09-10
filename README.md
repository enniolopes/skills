# skills

Agent skills, agents and the systems that compose them, by Ennio Politi Lopes. Built for
Claude Code following the Agent Skills standard; each skill is installable on its own:

```bash
npx skills add enniolopes/skills --skill <name> --agent claude-code
```

For hosts that take a directory, copy `skills/<name>/`. For hosts that take a `.skill` or
ZIP upload, build it from `development/<name>/` when a packager exists there.

## Catalog

| Unit | Kind | Status | Docs |
|---|---|---|---|
| [branding-studio](skills/branding-studio/) | skill | shipped | [docs](docs/branding-studio/README.md) |
| [landing-page](skills/landing-page/) | skill | shipped | [docs](docs/landing-page/README.md) |
| [explorer](skills/explorer/) | skill | shipped | — |
| [research](systems/research/) | system | design | [design](docs/research/design/) |

A **system** is a set of skills and agents built to work together and versioned
separately. `research` composes `scientific-method`, `research-map` (skills, to be built),
`reviewer-2` (agent, to be built) and `explorer`.

## Topology

The first level is the *role* a file plays; the second level is the *unit* it belongs to.

```text
skills/<name>/          runtime skill — SKILL.md + references/, templates/, scripts/; nothing else
agents/<name>.md        runtime agent — one file, frontmatter name == file name
systems/<name>/         composition — README.md naming the pieces, their status and dependencies
development/<unit>/     tests, evals, packaging, source policy — never shipped
docs/<unit>/            human documentation and design records
development/check_structure.py   mechanical check of the rules above (runs in CI)
```

The rule that holds it together: **runtime may be tested by development assets; runtime
never contains its tests, evals, build tooling or human documentation.** An installer that
copies `skills/<name>/` ships exactly what the skill needs to run.

Consequences:

- A unit's name is the same in every directory it appears in.
- A skill that belongs to a system still lives in `skills/`; the system directory only
  names it. Pieces install independently and a system can depend on a standalone skill.
- Design-stage pieces have no runtime directory yet. Their contract lives in
  `docs/<system>/`, their status in `systems/<system>/README.md`.
- Anything under `development/` or `docs/` must be named after an existing unit.

## Development

```bash
python development/check_structure.py                                  # topology
python -m unittest discover -s development/branding-studio/tests -v    # branding-studio
python development/branding-studio/package_skill.py                    # dist/branding-studio.zip
```

CI runs the structure check on every pull request and unit-specific checks when that
unit's paths change (`.github/workflows/`).

## License

See [LICENCE](LICENCE).
