# Identity Craft — designing and judging the visual/verbal system

Identity craft turns creative direction into repeatable expression. The goal is not uniformity; it is coherent recognizability across different applications.

## 1. Identity grammar

Define a small set of rules that explain how the system behaves:
- dominant forms and counterforms;
- typographic behavior;
- color relationships;
- image behavior;
- spacing/density tendencies;
- composition;
- recurring devices;
- interaction/motion if relevant.

A strong grammar should generate new work without requiring imitation of old layouts.

## 2. Logo, wordmark and signature

Treat the mark as one distinctive asset within the broader identity.

Evaluate:
- relevance to the central idea;
- memorability/simplicity appropriate to the use case;
- distinctiveness from category/portfolio collisions;
- optical balance;
- counterform and silhouette;
- scalability;
- monochrome behavior;
- reproduction constraints;
- lockups/variants required by touchpoints.

### Concept vs production

The skill can ideate and art-direct:
- wordmarks;
- monograms;
- letterforms;
- geometric symbols;
- abstract marks;
- organic marks;
- illustrative/expressive marks.

But production status must be explicit:
- `final`;
- `concept`;
- `external_craft_required`.

A raster concept is not a production master. A final SVG master should pass `asset_checks.py`.

Optical correction is legitimate; geometry is a construction aid, not the aesthetic authority.

## 3. Typography

Choose typography by:
- meaning/personality;
- legibility;
- range of weights/widths/scripts;
- licensing;
- available character set;
- touchpoints;
- hierarchy needs;
- relationship to the mark and other distinctive assets.

Do not assume two families.

Define roles rather than arbitrary family count:
- display;
- text;
- interface/data;
- institutional/office fallback;
- mono/special-purpose where needed.

Hierarchy may be:
- modular;
- custom;
- responsive/fluid.

If modular, declare and validate the scale. If custom, document the intended hierarchy and relationships instead of forcing a ratio.

## 4. Color

Color is both expressive and functional.

Decide it from:
- creative direction;
- category context;
- cultural/market context;
- medium;
- accessibility/contrast needs;
- production constraints.

Use OKLCH/OKLab for technical manipulation and comparison when useful.

Do not:
- derive strategy from universal color-emotion tables;
- assume a color alone creates distinctiveness;
- equate a technically accessible palette with a good identity.

For digital/text contexts, declare the actual foreground/background pairs that need contrast verification.

## 5. Imagery and illustration

Specify:
- subject matter;
- perspective;
- crop;
- light;
- color treatment;
- realism/abstraction;
- composition;
- relationship to typography;
- what is explicitly excluded.

If generative image tools are used, distinguish art direction from final rights/production review and avoid claiming uniqueness.

## 6. Iconography

Define:
- visual construction logic;
- stroke/fill behavior;
- corner logic;
- optical size;
- grid only when it improves consistency;
- semantic clarity;
- accessibility where relevant.

Icons do not need to mimic the logo; they need to belong to the same visual language.

## 7. Composition and grid

A grid is a tool for repeatable relationships, not a universal 4/8pt law.

Specify what matters:
- alignment;
- margin behavior;
- density;
- asymmetry/symmetry;
- image/type relationship;
- recurring spatial device;
- responsive behavior where applicable.

## 8. Motion, sound and sensory expression

Add only when touchpoints justify them.

For motion:
- timing;
- easing character;
- entry/exit behavior;
- transformation rules;
- reduced-motion fallback.

For sound/sensory elements:
- define the intended role and production constraints;
- avoid decorative additions that do not reinforce recognition or experience.

## 9. Trial applications

Identity decisions are provisional until tested in real contexts.

Use applications that stress different conditions. The purpose is to discover system problems early:
- mark disappears at small size;
- type hierarchy collapses in dense data;
- imagery rules cannot generate enough variety;
- color pair fails contrast;
- graphic device overwhelms content;
- voice breaks in error/institutional moments.

Fix the rule that caused the failure, then re-test.

## 10. Craft review

A semantic craft review asks:
- Is the system specific to this strategy?
- Does it remain recognizable without always showing the logo?
- Are expressive and functional choices coherent?
- Does it create enough variation without losing identity?
- Does it survive declared touchpoints?
- Are production decisions actually reproducible?

This is expert judgment, not deterministic validation.
