# Roadmap

Ordered so that each step's output is the next step's input. Nothing enters `reference/`
from memory.

## 1. Deep research of the method sources

For each phase in `research-skills-system.md` §2, locate the canonical sources named
there plus what the search adds; verify each at its DOI record (Crossref) or landing page;
record the verification. Output: `development/research/design/sources-verified.md` — one
row per source
with DOI, what it actually says (one sentence), and the phase it serves. This is the same
discipline the origin case used for its literature review (its decision D-21).

## 2. Distil `reference/` files

One file per phase, short, in the shape "when this applies / what it requires / the error
it prevents / source". No file longer than a screen. Each carries the date of its last
verification.

## 3. Write `skills/scientific-method/SKILL.md`

Frontmatter; ownership; the twelve invariants; the eight phases with gates and terminal
states; delegation to `explorer`, `research-map`, `reviewer-2`; pointers to `reference/`.
Target ≤ 2,500 words.

## 4. Write `skills/research-map/SKILL.md` and its `validate` script

The map schema; the four modes; the session ritual; `scripts/validate.py` covering
number-to-aggregate matching, decision revision conditions, citation resolution, notebook
outputs, pointer integrity. Shipped so a consuming repository can call it from
pre-commit.

## 5. Write `agents/reviewer-2.md`

The verifier contract adapted to manuscripts, with the fixed output headings and the
figure ↔ code ↔ data check.

## 6. Evals

`development/research/evals/scenarios.json` seeded from `origin-case.md`; the adversarial synthetic dataset;
the holdout reserved. Acceptance: regression scenarios all pass; adversarial never yields
a rescued `CONFIRMED`.

## 7. Install in the origin repository

Add to `delbem-research/cozsolidarias-research/skills-lock.json`; run `research-map init`
on `research/2026-kitchens-hunger-macro`; confirm `resume` restates the state correctly.

## Open decisions to close before step 3

- v1 scope (recommended: observational quantitative research with administrative data).
- License.
- Whether `validate` is a hook or a command.
