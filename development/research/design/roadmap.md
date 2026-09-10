# Roadmap

Ordered so that each step's output is the next step's input. Nothing enters `reference/`
from memory.

Status as of 2026-09-10: steps 1–6 executed in the build session; step 7 pending (lives
in the origin repository). Acceptance (step 6) is not yet met: the pieces exist, no
behavioural run has been recorded.

## 1. Deep research of the method sources — done 2026-09-10, level `located`

For each phase in `research-skills-system.md` §2, locate the canonical sources named
there plus what the search adds; verify each at its DOI record (Crossref) or landing page;
record the verification. Output: `sources-verified.md` — one row per source with DOI, what
it actually says (one sentence), and the phase it serves. This is the same discipline the
origin case used for its literature review (its decision D-21).

*Result.* Thirty sources located through a search index that returned the publisher's
landing page or DOI with matching metadata. Crossref, doi.org and publisher domains were
blocked by the build environment's network policy, so no record was read at source. The
table marks every row `located`; upgrading to `read` is the first task of any session with
scholarly network access, and no reference line should be treated as read until then.

## 2. Distil `reference/` files — done 2026-09-10

One file per phase, short, in the shape "when this applies / what it requires / the error
it prevents / source". No file longer than a screen. Each carries the date of its last
verification.

*Result.* `systems/research/skills/scientific-method/reference/01-problem.md` …
`08-publication.md`, 40–60 lines each; a structural test enforces the shape.

## 3. Write `systems/research/skills/scientific-method/SKILL.md` — done 2026-09-10

Frontmatter; ownership; the twelve invariants; the eight phases with gates and terminal
states; delegation to `explorer`, `research-map`, `reviewer-2`; pointers to `reference/`.
Target ≤ 2,500 words.

*Result.* ~1,240 words, ~2,200 estimated tokens. Adds an explicit "phase triggers when
invoked implicitly" section so the skill fires on "vou ajustar o modelo" as designed.

## 4. Write `systems/research/skills/research-map/SKILL.md` and its `validate` script — done 2026-09-10

The map schema; the four modes; the session ritual; `scripts/validate.py` covering
number-to-aggregate matching, decision revision conditions, citation resolution, notebook
outputs, pointer integrity. Shipped so a consuming repository can call it from
pre-commit.

*Result.* Grammar in `reference/map-schema.md`, blank map in `templates/RESEARCH.map`,
`scripts/validate.py` standard-library only with `--offline` and `--strict`; twelve unit
tests in `development/research/tests/`. Decision: `init` copies the script into the
consuming repository so pre-commit does not depend on the plugin's install path.

## 5. Write `systems/research/agents/reviewer-2.md` — done 2026-09-10

The verifier contract adapted to manuscripts, with the fixed output headings and the
figure ↔ code ↔ data check.

## 6. Evals — fixture built 2026-09-10; acceptance pending

`development/research/evals/scenarios.json` seeded from `origin-case.md` (plus two
`reviewer-2` scenarios); the adversarial synthetic dataset generator
(`evals/adversarial/make_synthetic.py`); the holdout reserved. Acceptance: regression
scenarios all pass; adversarial never yields a rescued `CONFIRMED`.

*Pending.* A recorded run per scenario, per `evals/README.md`.

## 7. Install in the origin repository — pending

In `delbem-research/cozsolidarias-research`, `/plugin marketplace add enniolopes/skills` and
`/plugin install research@enniolopes` at project scope; run `research-map init`
on `research/2026-kitchens-hunger-macro`; confirm `resume` restates the state correctly.
This is also the first retro-test: applied to the origin case as it stood before the
audit, the skill should produce the audit's findings.

## Decisions closed before step 3 (2026-09-10)

- v1 scope: observational quantitative research with administrative data — the only scope
  with a retro-test available.
- License: CC-BY-NC-4.0, the repository's license, carried in every piece's frontmatter.
- `validate` is a command shipped with the skill; `init` places a copy in the consuming
  repository for pre-commit.
