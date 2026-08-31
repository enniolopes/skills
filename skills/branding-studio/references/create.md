# CREATE mode — a new brand from zero

The value of creation lives in the interrogation and the derivation, not in the generation. A nonexistent brief produces dozens of plausible ideas and none that work (Malinic). Never generate anything before strategy is closed.

## Choose the tier first

Venture-studio reality: most theses die or pivot before an identity can become an asset (new assets start at fame ~0; memory only builds with prolonged repetition). Ask which tier this brand needs:

- **PROVISIONAL** (default for a new thesis): one session. Name with preliminary triage only (quick INPI/domain look, no deep clearance), typographic wordmark instead of a constructed symbol, minimal validated palette + type scale, essential strategy (customer/NOT-customer, right to win, onliness), pitch-deck template. Enough for deck + MVP. The spec uses the same schema with `meta.tier: "provisional"` and pending blocks marked — designed to be **promoted without rework**.
- **FULL** (the thesis survived, or the user asks): everything below. Promotion of a provisional = fill the pending blocks, complete clearance, construct the mark, re-run validators.

## Mandatory sequence

### 1. Interrogation (do not skip; do not invent answers)
Ask only what cannot be deduced. The core only the founder has:
- What the business does, for whom, and **for whom NOT** (mandatory — appealing to everyone appeals to no one).
- What the customer would use if the business did not exist (competitive alternatives, Dunford — includes "a spreadsheet" and "doing nothing").
- What only this business offers, and the evidence (right to win — for a new venture it comes from the founding ethos).
- Geographic ambitions (defines name-clearance scope) and relationship to the studio (defines architecture/endorsement).
- **Touchpoints: where will this brand live?** (web/product UI, pitch deck, print/institutional documents, signage, social...). Record in `meta.touchpoints` — this list drives which deliverable formats get compiled at the end.

**Pick the briefing register** and adapt the questions:
- **startup**: compression, category (existing or to be created?), recognition speed, investor audience.
- **research_institute (ICT)**: institutional credibility, funding agencies and agreements, scientific authority, longevity over fashion, multiple stakeholders (researchers, funders, government).

### 2. Research (you do it; don't ask the user)
- Direct and indirect competitors: positioning and visual code of each (matrix: name, positioning, colors, typography, mark morphology). Web-search for current reality.
- **Category conventions**: list what everyone does. Then decide explicitly what to keep (signals membership) and what to break (generates distinctiveness). Record both in the spec.
- Context: a relevant long-term trend, with evidence it is not a fad.

### 3. Portfolio consultation (mandatory BEFORE generating)
Read the portfolio registry. Note hues, morphologies, name types and personalities already occupied by sister brands. They enter as **negative constraints** ($excludes). After generating, run `scripts/portfolio_distance.py` to verify numerically.

### 4. Strategy (four levers → theme → manifesto)
Fill the four levers (customer insight, right to win, differentiation, context), each with `$rationale`. Connect them into a theme and apply two hard tests:
- **Because test** (Fielding): "[theme] BECAUSE [right to win]" — the sentence must close logically. If it doesn't, redo it.
- **Onliness** (Neumeier): "Our X is the only Y that Z." If "only" doesn't fit, there is no real differentiation — go back to lever 3.
Write the manifesto (long, inspiring version of the theme, internal use). List category entry points (situations where the brand must come to mind).

### 5. Naming
Follow `references/naming.md` (full pipeline with gates). Never deliver a name without clearance triage (provisional tier: preliminary triage, explicitly marked pending).

### 6. Verbal system
Podmajersky voice chart: for each principle (3 is typical), define the 6 dimensions (concepts, vocabulary, verbosity, grammar, punctuation, capitalization). Add "not_like_this" counter-examples (sentences another brand could legitimately say) and the **moments** (error, celebration, onboarding, institutional) with tone and example — voice is constant, tone varies. Provisional tier: principles + not_like_this at minimum, chart marked pending.

### 7. Visual system
- **Palette**: pick the hue derived from the theme (and outside the sisters' hues and the broken convention). Generate the scale with `python scripts/color_tools.py scale '#HEX' --bg '#BG'` — steps come out with contrast targets built in. Declare the contrast pairs in the spec. **Color is the weakest distinctive asset (12% fame / 39% uniqueness): treat it as reinforcement, never as the differentiation axis.**
- **Typography**: two families (heading with personality, sober body), modular scale with a declared ratio derived from use (1.2–1.25 for dense product; 1.333+ for editorial/marketing).
- **Tokens**: DTCG format ($value/$type), three layers: primitive → semantic → component. If there is studio endorsement, inherit the shared tokens from the registry.
- **Logo**: constructible domain only — monogram, letterform, geometric symbol. Specify as **parameterized geometric construction** (declared grid, primitives, coordinates), never freehand SVG. Derive the variants (monochrome, reduced, favicon) from the same construction. Apply optical adjustments (overshoot on curves/apexes; centered elements nudge up slightly) — the eye is the arbiter, not pure geometry. Proportional clear space (x = a dimension of the logo itself). If the territory calls for an organic/illustrative/expressive mark: **declare out of scope** and produce the brief for an external designer with auditable acceptance criteria (see audit.md).
- **Shape is the strongest asset** (40% fame / 71% uniqueness): differentiation against sisters and category anchors on morphology and name.

### 8. Single convergence (one big idea, Malinic)
Explore internally as many routes as needed; **deliver ONE**. Discarded routes go into the spec under `discarded_routes` with the why — they justify the chosen one, they are not a menu. Never present 3 options for the user to pick unless explicitly asked.

### 9. Validation, compilation and delivery
1. `python scripts/validate_spec.py spec.json` — must come out VALID.
2. `python scripts/portfolio_distance.py portfolio.json spec.json` — must come out APPROVED.
3. Fill `portfolio_summary` in the spec and add the brand to the portfolio registry.
4. **Compile deliverables from `meta.touchpoints`** — only the formats the declared touchpoints consume, nothing speculative:
   - web/product → a plain CSS custom-properties file generated from the tokens (`--color-action: ...`). Do not assume Tailwind/Figma or any tool unless the user names it.
   - pitch deck → a templated deck (pptx skill) applying tokens, type scale and logo rules — usually the highest-turnover piece in a studio.
   - print/institutional → CMYK conversions and a document template (letterhead/report) when the register is research_institute or print is declared.
   - **application mini-kit** (full tier): email signature + one-pager + social template derived from the spec — brand only exists in touchpoints; delivering the system without a single application pushes the translation cost onto the user.
5. Deliver: brand-spec.json + construction SVG(s) + updated registry + compiled formats + readable guidelines (a document derived from the spec, never a parallel source of truth) + the explicit list of human pendencies: definitive legal clearance (lawyer), external designer if any (brief ready), and the user's final aesthetic verdict.

## Anti-patterns (refuse, citing the rule)
- Generating without a brief ("create my branding" with no info → interrogate).
- Filling $rationale with circular rhetoric ("blue because it conveys trust" — universal color psychology is weak; derive from theme and convention-breaking, not from an emotion table).
- Geometric sans-serif + minimalism + "friendly" tone by default: that is *blanding*, the formula that makes everything look alike. If used, it must be a derived decision, not inertia.
- Golden ratio as an argument (myth; the real thing is optical adjustment).
- Archetypes as science (if used, use as a voice-consistency heuristic — and say so).
