# Landing Page — development

`landing-page` is a high-autonomy skill for researching, directing, designing, implementing and refining marketing landing pages and homepages. Runtime lives in `skills/landing-page/`; development assets never ship with it.

## Runtime model

The stable workflow is:

`ORIENT → DISCOVER → SYNTHESIZE → DIRECT → COMPOSE → SYSTEMIZE → REALIZE → REFINE → CRITIQUE`

The control model is:

`TRUTH → INTENT → DIRECTION → EXPRESSION → EXECUTION`

Facts and authority have high inertia. Creative direction is a revisable hypothesis. Rendered artifacts can reveal better solutions, but creative discovery cannot invent product truth.

Core behavior:
- inspect before asking;
- research only while it can change a material decision;
- distinguish evidence status from creative choice;
- challenge competent-but-generic defaults without mechanically opposing familiar forms;
- treat polish, novelty, style signals and component repetition as possible proxies, never proof of quality;
- fix the lowest layer that explains a defect;
- let rendered reality outrank plan fidelity.

## Evaluation

`evals/` has two canonical files:
- `cases.json` — six orthogonal regressions and four deliberately different creative briefs;
- `evaluation.md` — evidence levels, blind comparison, five judgment dimensions and the promotion rule.

Cases represent failure mechanisms rather than runtime rules. Targeted changes should run only cases that can distinguish them; material creative/composition changes should also run the creative briefs. Cross-run recurrence matters only when a repeated solution lacks brief-specific causality.

CI establishes mechanical integrity only. Claims of behavioral or creative improvement require independent comparison; real project performance remains stronger evidence.
