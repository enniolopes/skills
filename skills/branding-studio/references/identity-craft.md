# Identity craft — build and judge the expression system

Turn creative direction into repeatable expression. Optimize for coherent recognizability across different applications, not uniformity.

## 1. Identity grammar

Define the smallest ruleset that can generate new work without imitating old layouts:
- dominant forms/counterforms;
- typographic behavior;
- color relationships;
- imagery behavior;
- spacing/density tendencies;
- composition;
- recurring devices;
- interaction/motion when relevant.

## 2. Logo, wordmark and signature

Treat the mark as one distinctive asset within the broader system.

Evaluate:
- relationship to the central idea;
- memorability/simplicity appropriate to use;
- category/portfolio distinctiveness;
- optical balance;
- counterform/silhouette;
- scalability;
- monochrome behavior;
- reproduction constraints;
- lockups/variants required by touchpoints.

### Concept vs production

Ideate and art-direct wordmarks, monograms, letterforms, geometric/abstract/organic/illustrative marks as needed, but keep production status explicit:
- `final`;
- `concept`;
- `external_craft_required`.

A raster concept is not a production master. A final SVG master should pass `scripts/asset_checks.py`. Use geometry as a construction aid, not aesthetic authority; apply optical correction where needed.

## 3. Typography

Choose typography from meaning/personality, legibility, range, licensing, character set, touchpoints, hierarchy needs and relationship to other distinctive assets.

Do not assume a fixed family count. Define roles only when needed:
- display;
- text;
- interface/data;
- institutional/office fallback;
- mono/special-purpose.

Hierarchy may be `modular`, `custom` or `fluid`. If modular, declare/validate the scale. If custom/fluid, document explicit relationships instead of forcing a ratio.

## 4. Color

Derive color from creative direction, category/cultural context, medium, accessibility and production constraints.

Use OKLCH/OKLab for technical manipulation/comparison when useful.

Do not:
- derive strategy from universal color-emotion tables;
- assume color alone creates distinctiveness;
- equate technical accessibility with identity quality.

For digital/text contexts, declare actual foreground/background pairs requiring contrast verification.

## 5. Imagery and illustration

Specify only behavior that constrains production:
- subject matter;
- perspective/crop;
- light;
- color treatment;
- realism/abstraction;
- composition;
- relationship to typography;
- explicit exclusions.

When generative image tools are used, keep art direction separate from final rights/production review and do not claim uniqueness without evidence.

## 6. Iconography

Define construction logic, stroke/fill behavior, corner logic, optical size, semantic clarity and accessibility. Use a grid only when it improves consistency. Icons need to belong to the same visual language; they do not need to mimic the logo.

## 7. Composition and grid

Specify meaningful relationships such as alignment, margin behavior, density, asymmetry/symmetry, image/type relationship, recurring spatial devices and responsive behavior.

Do not impose a universal 4/8pt system.

## 8. Motion, sound and sensory expression

Add only when touchpoints justify them.

For motion define timing, easing character, entry/exit behavior, transformation rules and reduced-motion fallback. For sound/sensory elements define intended role and production constraints; avoid decorative additions that do not reinforce recognition/experience.

## 9. Trial applications

Treat material identity decisions as provisional until they survive representative use. Choose applications that expose different stresses, such as:
- mark at small scale;
- dense information hierarchy;
- imagery variety;
- contrast-dependent color use;
- expressive device vs content;
- voice in institutional/error moments.

Fix recurring system causes, then re-test. Keep one-off failures local.

## 10. Craft review

At V2 ask:
- Is expression specific to this strategy?
- Is it recognizable without always showing the logo?
- Are expressive and functional choices coherent?
- Is there enough variation without loss of identity?
- Does it survive declared touchpoints?
- Are production decisions reproducible?

Treat these as professional judgments, not deterministic validation.
