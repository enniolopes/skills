# AUDIT — evaluate an existing artifact

Use AUDIT when a current brand spec exists and an existing artifact must be evaluated against it.

Without a current spec, do not present a standards-based compliance audit. Reconstruct/create the spec first, or provide an explicitly opinion-based critique without false precision.

## 1. Inspect the richest available source

Prefer native/structured source over screenshots when available:
- URL/HTML/CSS;
- PPTX;
- SVG;
- design source;
- document file;
- code/components.

Use screenshots only for what they can establish. State when exact measurement is impossible.

Compile the smallest spec subset relevant to the artifact's job, audience, medium and moment.

## 2. Separate evidence classes

Apply the verification ladder from `SKILL.md` and keep findings distinct.

**V1 Structural** — only what exact source or deterministic tooling can establish, such as token/value usage, declared contrast pairs, measurable type rules, SVG/master integrity, file/variant presence, dimensions and production constraints.

**V2 Semantic** — grounded professional judgment against explicit spec rules, including hierarchy, strategy/creative territory, imagery/composition, voice/tone, distinctive devices and recognizability of the system.

**V3 Contextual** — behavior in the environment where the artifact must operate: viewport/device, print/packaging scale, presentation sequence, shelf/category context, signage distance or actual content density.

**V4 Reality** — external claims about perception, behavior, recall, stakeholder response, legal status or other outcomes. If required evidence is missing, report `INSUFFICIENT EVIDENCE` for that claim.

Do not hide judgment behind pseudo-objective decimal scores. Label any rubric score as a rubric score.

## 3. Issue a verdict

Use one:
- **COMPLIANT** — no material violations found and evidence is sufficient for important checks;
- **COMPLIANT WITH RESERVATIONS** — usable, but material improvements or evidence gaps remain;
- **NON-COMPLIANT** — clear violations of important spec/production constraints;
- **INSUFFICIENT EVIDENCE** — the requested judgment cannot responsibly be made from available evidence.

Prioritize fixes by:
1. artifact-job failure;
2. accessibility/legal/production risk;
3. brand-system integrity;
4. distinctiveness/recognition cues;
5. refinement.

Do not mutate the spec merely because an artifact is weak.

## 4. Classify system consequence

- one-off artifact error → fix artifact;
- repeated execution ambiguity → guidance-patch candidate;
- repeated failure across legitimate touchpoints → EVOLVE candidate;
- new external evidence contradicting a belief → update evidence state/confidence before changing contract.

## Report

```text
# Audit: [artifact] vs [brand] v[spec version]
## Verdict
## Artifact job + evidence available
## V1 Structural
## V2 Semantic
## V3 Contextual
## V4 / evidence gaps
## Prioritized fixes
## System consequence: none | patch candidate | EVOLVE candidate
## Optional aesthetic opinion
```

For semantic findings, cite the governing spec field/rule.

For specialist-produced logos, illustration, lettering or other craft, audit against approved creative direction/production brief, required variants, reproduction behavior and relevant category/portfolio collision. Keep “meets brief”, aesthetic preference and production validity separate.
