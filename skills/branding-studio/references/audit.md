# AUDIT mode — evaluate a branded artifact against the current spec

AUDIT requires a current brand spec. Without one, there is no standards-based audit; there is only critique. If no spec exists, either:
- reverse-engineer/create the spec first; or
- provide an explicitly opinion-based critique with no false precision.

## Prefer the richest source

Use structured/native source when available:
- URL/HTML/CSS;
- PPTX;
- SVG;
- design source;
- document file.

Screenshots are acceptable when that is all that exists, but measurements from them are degraded. State what could and could not be verified.

## Four evidence classes

Keep these separate.

### 1. Deterministic
What code or exact source inspection can establish, for example:
- token/value use where the artifact exposes exact values;
- declared foreground/background contrast;
- declared font family/size rules;
- logo master integrity and clear-space/minimum-size rules when measurable;
- SVG structural checks;
- required file/variant presence.

Only call something deterministic if the input actually makes it measurable.

### 2. Semantic judgment
Grounded professional judgment against explicit spec rules:
- hierarchy supports the artifact's job;
- creative territory is preserved;
- imagery/composition belong to the identity grammar;
- voice and tone fit the moment;
- distinctive devices are used coherently;
- the result remains recognizably from the same system.

Do not hide judgment behind pseudo-objective decimal scores. If a score is useful for workflow consistency, label it explicitly as a rubric score, not measurement.

### 3. Evidence gap
When a claim cannot be decided from the available medium/source:
- mark `INSUFFICIENT EVIDENCE`;
- say what source would resolve it.

Unknown is not pass.

### 4. Opinion
Observations not grounded in a spec rule or measurable requirement. Label them as opinion and keep them out of compliance verdicts unless the user explicitly asks for an aesthetic critique.

## Flow

1. Load the spec and identify the artifact's job, audience, medium and tone/moment.
2. Load the native source if available.
3. Run applicable deterministic checks only.
4. Review semantically against the smallest relevant subset of the spec.
5. Identify evidence gaps.
6. Separate optional aesthetic opinion.
7. Prioritize fixes by effect on the artifact's job and brand-system integrity.

## Verdict

Use:
- **COMPLIANT** — no material violations found and evidence is sufficient for the important checks.
- **COMPLIANT WITH RESERVATIONS** — usable, but material improvements or evidence gaps remain.
- **NON-COMPLIANT** — clear violations of important spec rules or production constraints.
- **INSUFFICIENT EVIDENCE** — the requested compliance judgment cannot responsibly be made from the available source.

## Report format

```text
# Audit: [artifact] vs [brand] v[spec version]
## Verdict
## Artifact job and evidence available
## Deterministic checks
## Semantic review
## Evidence gaps
## Prioritized fixes
## Optional opinion
```

For each semantic finding cite the relevant spec rule/field.

## Third-party creative deliveries

For a specialist-produced logo, illustration, lettering or other craft output:
- audit against the approved creative direction and production brief;
- verify required variants and reproduction behavior;
- inspect portfolio/category collision signals;
- distinguish "meets brief" from "I prefer it aesthetically."

If the delivery exposes a missing or broken system rule, do not silently rewrite the spec. Route a system-level change through EVOLVE.
