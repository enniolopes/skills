# Knowledge base — what is solid, what is contested, what is myth

Use this reference to calibrate claims. The skill never presents contested knowledge as consensus. When any of these topics appears in conversation, flag its status.

## Solid consensus (use with confidence)

- **Strategic derivation**: every identity decision derives from strategy and justifies itself ("because"); decisions without a rationale tend to fail (Fielding, Malinic — independent convergence).
- **Negative specification**: defining who the customer is NOT, what the voice does NOT say, what the visual avoids — this is what makes the system decidable.
- **Design tokens (W3C DTCG)**: $value/$type, three layers (primitive → semantic → component), versionable, diffable. Stable standard since Oct/2025, adopted by Figma, Adobe, Salesforce, etc.
- **WCAG 2.2** as the legal contrast floor (4.5:1 body, 3:1 large/UI); **APCA/Lc** as the superior perceptual metric (Lc 60 ≈ body, 45 ≈ large) — but APCA is a WCAG 3 candidate, NOT an adopted standard. Report both, with that status.
- **Perceptually uniform spaces (OKLCH/OKLab)** for generating and comparing colors; contrast is monotonic in L for fixed hue/chroma (the basis of binary-search generation).
- **Empirical hierarchy of distinctive assets** (Ehrenberg-Bass/Romaniuk, 1,162-asset benchmark across 21 categories): shape/logo strongest (~40% fame / 71% uniqueness); **color weakest** (~12% / 39%; only ~4% of colors uniquely identify a brand). Differentiation anchors on shape and name; color reinforces.
- **Distinctive Asset Grid** (Fame × Uniqueness): new assets are born at fame ~0 — a new brand's goal is high uniqueness + consistent repetition. Measuring real fame/uniqueness requires field research; without it, treat values as hypotheses.
- **Optical adjustments** (overshoot of curves/apexes beyond baseline/cap-height; nudging centered elements): real and necessary — perfect geometry looks wrong.
- **Phonosemantics**: real, replicated effect (Yorkston & Menon 2004), but modest — a signal, not a decider.
- **Voice vs tone** (Podmajersky): voice constant, tone varies by moment; auditing tone requires knowing the moment.
- **Color as property**: legally, a color becomes a trademark only through secondary meaning and decades of consistent use (Qualitex, Louboutin, Cadbury); empirically coherent with color's weakness in the grid. Never promise a new brand it will "own a color".

## Contested (use with the explicit caveat)

- **Brand archetypes** (Mark & Pearson): no falsifiable empirical base; the Jung link is tenuous. Real value: a consistency heuristic for personality. If the user asks, use it — saying what it is.
- **Universal color psychology** ("blue = trust"): weak, context- and category-dependent effects. What is real: category base rates (≈30% of the world's logos are blue; retail is dominated by reds) — useful as a convention map to break, not as an emotion table.
- **How Brands Grow laws** (double jeopardy, penetration > loyalty): derived from mature mass-consumer brands; do not transfer directly to small-base deep-tech B2B. What transfers: mental availability, category entry points, distinctive assets.
- **Category design / Play Bigger** ("category kings take ~70–80% of the category's economics"): influential thesis for deep tech, but critics point to oversimplification; rely on case evidence, not the promise.

## Myth (never use as an argument; correct it if the user brings it)

- **Golden ratio in logos**: no scientific basis (the reputation traces to Zeising, 19th century). The real things are optical adjustments and consistent grids.
- **"Blanding" as good practice**: the geometric-sans + minimalism + friendly tone + -ify name formula is not neutral, it is active convergence — it erases distinctiveness. The defensible part is functional (legibility at small sizes); the rest is inertia. Simplification that removes recognized assets destroys brand memory.

## Register-specific notes

- **Research institute (ICT) / academic spin-off**: scientific credibility > emotional appeal; multiple stakeholders (funding agencies, government, academia, industry); longevity and sobriety; names lean acronym-with-meaning or institutional-descriptive; INPI class 42 (scientific research) almost always present; the "manifesto" becomes the institutional mission.
- **Deep-tech B2B startup**: Dunford-style positioning (real competitive alternatives, not "slide competitors"); frequently category creation (onliness mandatory); dual audience (technical customer + investor); the brand must survive pivots — avoid names that lock product scope.

## Declared limits of the skill (say them when relevant)

1. **Organic/illustrative/expressive marks**: outside the constructible domain — the skill writes the brief and acceptance criteria, and audits the external designer's delivery.
2. **Definitive legal clearance**: a lawyer's opinion; the skill triages.
3. **Real fame/uniqueness**: require field research; the skill treats them as hypotheses.
4. **Final aesthetic verdict**: the user's — informed by the skill, never usurped by it.
5. **Raster image generation**: not a brand asset (no vector, no construction, no reproducibility, similarity risk with existing marks). The skill produces declarative geometric construction (parameterized SVG).
