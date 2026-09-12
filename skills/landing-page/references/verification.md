# Verification and Refinement

Load this before completion of any material CREATE or REFINE task when browser/rendering tools are available. Use the relevant subset for REPAIR.

The core rule is:

**Code is implementation evidence. Pixels and interaction are experience evidence.**

For award-caliber, animation-heavy, WebGL/3D/canvas, or technically ambitious work, also load `technical-excellence.md`; passing generic build/visual QA is not sufficient for creative-development excellence.

A build can pass while the page is visually poor. A screenshot can look excellent while interaction is broken. Verify both.

## Build a QA inventory

Before final handoff, list internally the claims you intend to make about completion and map each to evidence.

Examples:

| Claim | Evidence |
|---|---|
| page renders | browser load / server response |
| primary CTA works | actual click + resulting navigation/state |
| no horizontal overflow | browser inspection at target viewports |
| mobile composition works | rendered mobile viewport screenshot/inspection |
| build is valid | repository build/typecheck/lint command actually run |
| visual direction is coherent | perceptual review of full page and screenshots |
| WCAG contrast checked | actual accessibility/audit/manual contrast evidence |
| performance is good | measured evidence, not code inspection |

Never claim evidence that was not collected.

## Deterministic QA

Prefer tools for falsifiable properties.

Run repository-declared checks when available and relevant:

- build;
- typecheck;
- lint;
- tests;
- framework-specific validation.

In the browser inspect for:

- console errors;
- failed network assets relevant to the page;
- broken internal/external destinations on primary actions;
- accidental horizontal scroll;
- clipped or overlapping content;
- missing fonts/images;
- broken sticky/fixed elements;
- invalid interactive states;
- focus visibility and basic keyboard flow;
- obvious accessibility violations through available tooling.

Do not invent ad-hoc destructive commands. Respect repository conventions.

## Viewport QA

At minimum for material pages, inspect:

- a representative desktop viewport;
- a representative mobile viewport.

Add tablet/intermediate widths when layout transitions are complex or when defects appear between the extremes.

Do not test mobile only by narrowing until the page technically fits. Look for intended recomposition:

- hierarchy preserved;
- copy measures and line breaks remain controlled;
- imagery crop still communicates;
- tap targets remain usable;
- navigation remains clear;
- no meaningful interaction relies only on hover;
- dense desktop compositions simplify or resequence appropriately.

## Perceptual QA

Review the rendered page as a hostile design critic rather than its author.

### First-viewport test

Without scrolling, ask:

- What receives attention first?
- Can I identify the product/page job quickly?
- Is the primary action evident?
- Does this feel specific to the product?
- Is there one dominant visual idea?
- Is any element competing with the thesis?

### Full-page test

Scroll at normal reading speed. Ask:

- Does the page accumulate meaning or restart every section?
- Does visual intensity vary intentionally?
- Are sections mechanically repetitive?
- Is there a weak middle after a strong hero?
- Does imagery remain meaningful?
- Does the CTA architecture stay coherent?
- Does the footer feel like part of the same system?

### Craft sweep

Inspect high-risk details:

- headline line breaks;
- paragraph measures;
- image crops;
- icon consistency;
- optical alignment;
- buttons/controls typography;
- hover/focus/pressed states;
- section edges/transitions;
- sticky content;
- forms and error/empty states when present;
- mobile spacing and wrapping.

### Anti-generic / counterfeit-quality test

Ask:

- Could most of this design survive an unrelated product/logo swap?
- Which important decision is merely **signaling** premium, creativity, sophistication or technical authority instead of producing the underlying quality?
- Did surface polish make an unresolved proposition, hierarchy, composition or interaction look finished?
- Which visual decision has weak causal dependence on this brief and is present mainly because it is a familiar category or trend default?
- Did component convenience replace composition, or did repeated geometry replace coherent variation?
- Is novelty or technical complexity adding cognitive/runtime cost without adding meaning, identity, proof or a useful experience job?
- Is imagery doing narrative/evidentiary work rather than acting as decoration?
- Are structural devices encoding information rather than simulating sophistication?
- Did reference research broaden the solution or make it imitate the category?
- Is there one memorable idea or many weak attempts at interest?

When a false proxy appears, repair the **underlying quality** rather than banning the surface form or adding another decorative layer. Keep any form that the brief genuinely earns. If genericity is conceptual, revise the governing decision rather than ornamenting it.

## Concept fidelity

When a visual concept/reference was accepted before implementation:

1. capture the concept/reference and current implementation in the same QA pass;
2. compare composition, typography, scale, crop, palette, spacing, imagery, containers, and motion intent;
3. list the largest mismatches;
4. fix mismatches in descending perceptual impact;
5. re-render after each meaningful correction set.

Do not silently reinterpret the accepted design into a generic component system.

A reference is not permission to ship screenshot-as-UI. Keep real UI, text, controls, and interactions code-native where appropriate.

## Build in visual slices

For material CREATE work, do not write the whole page blindly and review only at the end:

1. implement the first viewport and the system foundation;
2. render and correct large drift;
3. implement the next narrative slice;
4. render and check section continuity;
5. continue until complete;
6. run full-page rhythm and responsive passes.

This preserves a coherent direction while reducing late-stage visual debt.

## Render loop

The first successful render begins QA. When browser/render tools exist:

1. run the app using repository-declared commands;
2. inspect the first viewport before scrolling;
3. inspect the complete narrative at normal reading speed;
4. exercise primary interactions and conversion actions;
5. inspect representative desktop and mobile; add intermediate/short-height viewports when the layout warrants it;
6. capture screenshots when possible;
7. run the deterministic checks available in the environment;
8. run the perceptual critiques and the multi-lens review below, as separate passes;
9. identify the largest remaining defect;
10. make a targeted correction and render again;
11. repeat until no material defect remains or a concrete blocker prevents improvement.

## Refinement strategy

Converge rather than churn.

After each render:

1. identify the single largest remaining defect or mismatch;
2. diagnose its root layer: semantics, hierarchy, composition, system, asset, implementation, responsive behavior, or micro-craft;
3. make the smallest change that addresses the root cause;
4. render again;
5. keep improvements that survive comparison.

Do not regenerate a solved page because of a local defect.

## Accessibility floor

Follow WCAG 2.2 AA where applicable and reasonably testable. In particular, protect:

- keyboard access and visible focus;
- semantic headings/landmarks/controls;
- accessible names for interactive controls;
- text contrast (generally at least 4.5:1 for normal text and 3:1 for large text, subject to WCAG exceptions);
- reflow/resizing;
- non-color-only communication;
- reduced-motion preferences;
- target size/spacing (WCAG 2.2 AA specifies at least 24×24 CSS px or qualifying spacing/equivalent exceptions).

Do not claim full WCAG conformance from a cursory automated audit.

## Performance integrity

Performance affects perceived design quality.

Avoid obvious sources of preventable degradation:

- enormous unoptimized hero media;
- unnecessary client-side JavaScript;
- layout-shifting media without dimensions;
- gratuitous animation work on the main thread;
- excessive web-font payloads;
- dependencies added for trivial effects.

When actual performance measurement is in scope and tools permit, use current Core Web Vitals as reference targets: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 at the 75th percentile. Local synthetic measurement is not equivalent to field percentiles; describe evidence accurately.

## Hard-stop defects

Do not sign off while any applicable defect remains:

- runtime/build failure;
- blank/partially broken render;
- primary action broken;
- missing central image/font;
- clipped primary content;
- accidental wrapping that damages hierarchy;
- unreadable text;
- horizontal mobile overflow;
- unusable mobile navigation or CTA;
- obvious contrast/focus defect;
- placeholder boxes or rough temporary assets in a premium result;
- large concept-to-browser mismatch;
- central section that looks prototype-grade;
- unsupported marketing proof represented as real;
- known materially weaker viewport or page region.

If the environment prevents verification, state exactly what remains unverified.

## Final internal questions

Before handoff:

- **Truth:** Did I introduce any unsupported factual claim?
- **Meaning:** Can the intended visitor identify proposition and action?
- **Specificity:** Could this plausibly belong to an unrelated product?
- **Hierarchy:** Is attention ordered rather than contested?
- **Coherence:** Does everything speak one visual language without collapsing into mechanical uniformity?
- **Signature:** What will be remembered?
- **Counterfeit quality:** Is any major quality being implied mainly by polish, style cues, novelty, complexity or repetition instead of being materially present?
- **Craft:** Where is the weakest-looking 10%? Did I fix it?
- **Responsive:** Was mobile composed intentionally?
- **Function:** Did I actually exercise the important actions?
- **Evidence:** Which checks did I truly run?
- **Resolution:** Is any visible part merely acceptable rather than resolved?

A material page is ready when the last question is `no`, or when further improvement is blocked by a concrete external constraint that is explicitly reported.

## Multi-lens review for premium work

Do not collapse all critique into one aesthetic impression. Run separate passes because each lens catches different failures.

### Lens 1 — first-time visitor

Temporarily ignore implementation intent and inspect only what a new visitor can perceive:

- What is this?
- Who is it for?
- What is the primary promise?
- What makes it credible?
- What action is expected?
- What context is missing because the builder already knows the product?

### Lens 2 — creative director

Inspect concept strength:

- Is the governing idea defensible and brief-specific?
- What makes the page memorable after the browser is closed?
- Which section feels derivative of current web trends or category autocomplete?
- Does the signature express the product or merely demonstrate technique?
- Is any familiar premium/creative signal standing in for a weaker underlying idea?
- Is there enough contrast between quiet/supporting regions and the dominant moment?

### Lens 3 — craft reviewer

Inspect the weakest 10%, not the strongest 10%:

- where does quality drop?
- which line break/crop/alignment/spacing relation feels approximate?
- which state or section edge would receive a design-review comment?
- which mobile decision looks like a fallback rather than a composition?

### Lens 4 — creative developer / technical jury

For ambitious work inspect:

- loading and perceived performance;
- responsive/device behavior;
- markup/document structure;
- semantics/discoverability/metadata;
- motion/frame behavior;
- accessibility and graceful degradation.

A technically impressive page that fails one of these materially is not award-caliber.

## Finding severity

Classify findings internally:

- `BLOCKER` — breaks truth, primary function, accessibility/safety, core rendering, or makes the experience materially unusable/misleading;
- `MATERIAL` — clearly prevents premium/agency-signoff quality, including generic composition, counterfeit quality masking an unresolved decision, weak section, broken responsive hierarchy, significant fidelity drift, or visible jank;
- `POLISH` — real improvement whose absence does not undermine the page's concept or professional integrity.

Do not hand off with known BLOCKER or MATERIAL findings that are fixable in the current environment.

## Diminishing-returns stop rule

Premium work requires iteration but not endless churn. Stop refinement when:

1. all applicable hard gates pass;
2. no BLOCKER/MATERIAL finding remains;
3. the weakest important region is still professional and coherent with the whole;
4. another change would be preference-level, conflict with a constraint, or risk destabilizing a stronger solved decision.

This is stronger than “looks good” and more practical than pretending perfection is measurable.
