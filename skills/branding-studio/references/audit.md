# AUDIT intent — prove what an artifact does and does not satisfy

AUDIT evaluates an existing branded artifact against the current brand state. It uses the global **SEARCH → PROVE → COMMIT → ADAPT** loop, with most work concentrated in SEARCH and PROVE.

Without a current spec there is no standards-based compliance audit. Either reconstruct/create the spec first or provide an explicitly opinion-based critique with no false precision.

## SEARCH

### Prefer the richest source

Inspect native/structured source when available:
- URL/HTML/CSS;
- PPTX;
- SVG;
- design source;
- document file;
- code/components.

A screenshot is a degraded source when native structure exists. State what cannot be measured exactly.

Compile the smallest relevant spec subset for the artifact's job, audience, medium and moment.

Search for:
- machine-checkable violations;
- semantic/creative mismatches;
- contextual failures;
- missing evidence;
- recurring failures that may indicate a system problem.

## PROVE

Keep the verification ladder explicit.

### V1 Structural

What exact source or deterministic tooling can establish, for example:
- token/value usage;
- declared foreground/background contrast;
- font/size rules when measurable;
- SVG/master integrity;
- required file/variant presence;
- dimensions and production constraints.

Only call a finding deterministic if the available source makes it measurable.

### V2 Semantic

Grounded professional judgment against explicit spec rules:
- hierarchy serves the artifact's job;
- strategy/creative territory is preserved;
- imagery/composition belongs to the identity grammar;
- voice/tone fits the moment;
- distinctive devices are coherent;
- the artifact remains recognizably from the same system.

Do not hide judgment behind pseudo-objective decimal scores. A rubric score, if used, must be labeled as a rubric score.

### V3 Contextual

When possible, inspect the artifact in the environment where it must operate:
- viewport/device;
- print/packaging scale;
- presentation sequence;
- shelf/category context;
- signage distance;
- actual content density.

A source can be V1-valid and still fail V3.

### V4 Reality

Use only for claims about real perception, behavior, recall, stakeholder response, legal status or other external outcomes.

When V4 evidence is missing, report `INSUFFICIENT EVIDENCE` for that claim. Model critique, simulated personas and desk research do not upgrade the evidence level.

## COMMIT

AUDIT normally commits a **diagnosis**, not a brand-system change.

Verdicts:
- **COMPLIANT** — no material violations found and evidence is sufficient for the important checks;
- **COMPLIANT WITH RESERVATIONS** — usable, but material improvements or evidence gaps remain;
- **NON-COMPLIANT** — clear violations of important spec/production constraints;
- **INSUFFICIENT EVIDENCE** — the requested judgment cannot responsibly be made from available evidence.

Prioritize fixes by:
1. artifact job failure;
2. accessibility/legal/production risk;
3. brand-system integrity;
4. distinctiveness/recognition cues;
5. refinement.

Do not silently mutate the spec because an artifact is weak.

## ADAPT

After diagnosis classify the cause:
- one-off artifact error → fix artifact;
- repeated execution ambiguity → small guidance patch candidate;
- repeated failure across legitimate touchpoints → EVOLVE candidate;
- new external evidence contradicting a belief → update evidence state/confidence before changing contract.

This is where AUDIT can improve the system without turning every critique into a redesign.

## Report format

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

For semantic findings, cite the relevant spec field/rule.

## Third-party creative deliveries

For specialist-produced logos, illustration, lettering or other craft:
- audit against approved creative direction and production brief;
- verify required variants/reproduction behavior;
- inspect portfolio/category collision where relevant;
- distinguish "meets brief" from personal aesthetic preference;
- never label concept quality as production validity without the appropriate evidence level.
