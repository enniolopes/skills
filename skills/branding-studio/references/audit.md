# AUDIT mode — checking material against the spec

Requires the brand's spec. Without a spec there is no audit — only opinion. If the user asks for a review without one, offer: (a) creating the spec first (CREATE mode, or reverse-engineering an existing identity into the template), or (b) an explicitly opinion-based critique, with no numbers.

## Ask for the structured source before accepting a screenshot

Auditing a screenshot is degraded by nature: compression shifts colors, sizes are estimates. Whenever a structured source exists — the live URL/CSS, the deck file (pptx/XML), the design file, the HTML — request and audit **that**; measurements become exact. Accept images only when no source exists, and declare in the report which checks were degraded by the medium.

## Core principle: two natures of check, always separated

**Deterministic (pass/fail with a number)** — what a machine verifies:
- Colors used ∈ spec tokens (no hex outside the palette).
- Text/background contrast pairs: WCAG 2.2 AA mandatory; Lc/APCA as quality score (`scripts/color_tools.py contrast`).
- Font sizes ∈ declared modular scale.
- Spacing ∈ the spec's 4/8pt scale.
- Logo clear space and minimum size respected.
- Typography = declared families.

**Heuristic (0–10 score with a comment citing the spec rule)** — what requires judgment:
- Visual hierarchy: does the reading order serve the piece's goal?
- Gestalt: does grouping (proximity/similarity) match the information?
- Territory: does the piece inhabit the spec's territory and respect `$excludes`?
- Voice: does the copy pass the 6 voice-chart dimensions?
- **Tone vs moment**: identify the piece's moment (error? celebration? institutional?) and compare against THAT moment's tone. Correct tone variation is not a voice violation.

Never present heuristic judgment with the authority of measurement. In the report the two blocks are visually separate.

## Flow

1. Load the spec. Prefer the structured source (above). For images, extract what is extractable (dominant colors, copy, apparent sizes) and declare what could not be measured.
2. Run the deterministic checks. For colors extracted from images, tolerate small ΔL/ΔC from compression, but a divergent hue is a failure.
3. Do the heuristic judgment item by item, **always citing the spec rule** grounding each score (Podmajersky format: comment + 0–10). Without a citable rule, the observation goes under "opinion" — never into the scorecard.
4. Check copy against the voice chart dimension by dimension (forbidden vocabulary? verbosity off? capitalization?) and against the "not_like_this" counter-examples.

## Report format

```
# Audit: [piece] vs [brand] v[spec version]
## Verdict: COMPLIANT | COMPLIANT WITH RESERVATIONS | NON-COMPLIANT
## Deterministic checks  → table: check | measured | expected | pass/fail
## Heuristic judgment    → item | score 0-10 | spec rule cited | comment
## Prioritized fixes     → what to change, by impact, with the spec's correct value
## Outside the spec (opinion) → observations without a citable rule, declared as opinion
```

Prioritize fixes by impact: deterministic accessibility violations first (the only ones with legal consequence), then territory/distinctiveness violations, then refinements.

## Auditing third-party deliveries (external designer)
When the piece comes from a brief this skill wrote (expressive marks), audit against the brief's acceptance criteria: derivation from the territory, behavior across required variants (monochrome, reduced, favicon), clear space, and portfolio distance (`portfolio_distance.py` with the delivery's morphology tags).
