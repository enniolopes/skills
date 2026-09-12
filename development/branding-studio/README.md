# Branding Studio — development

`branding-studio` is an autonomous brand steward for creating, applying, auditing and evolving brand systems. Runtime lives in `skills/branding-studio/`; everything here is development evidence or tooling and never ships with the skill.

## Runtime model

Material creation/change follows:

`GROUND → FRAME → DIVERGE → COMMIT DIRECTION → BUILD SYSTEM → TEST IN USE → REFINE OR RE-DIVERGE → PACKAGE`

The durable principles are small:
- protect business truth and earned equity;
- use evidence capable of answering the actual question;
- explore materially different ideas before commitment;
- build the smallest grammar that can generate new work;
- judge systems in representative use, not by completeness or mockup polish;
- fix the lowest layer that explains a defect;
- persist only decisions future operators need.

Specialized depth belongs in on-demand references. The v2.1 addition is `references/verbal-identity.md`, loaded only when proposition, messaging, voice/tone or a broader verbal system is materially in scope.

## Deterministic boundary

Scripts establish only machine-checkable properties. Structural validity, color calculations, SVG checks and portfolio comparison signals never become proof of strategy, creativity, perception or legal status.

`package_skill.py` builds the installable runtime from an explicit manifest and fails when runtime files are missing or unexpected.

## Evaluation

`evals/` has two canonical files:
- `cases.json` — seven orthogonal behavioral regressions, four diverse creative briefs and one decision-transfer test;
- `evaluation.md` — evidence levels, blind-comparison method, six judgment dimensions and the promotion rule.

Cases represent failure mechanisms, not runtime rules. For a targeted change, run only cases that can distinguish it. If baseline and candidate behave materially the same, extra runtime context is not earned.

CI and unit tests establish mechanical integrity only. A claim that branding behavior improved requires independent blind comparison; market/perception claims require real external evidence.
