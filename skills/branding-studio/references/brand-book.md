# Brand book — a served touchpoint that teaches the system

Use when guidelines, a brand book or an equivalent handoff is a deliverable. Build it after the identity has survived the declared touchpoints. It is written for people who did not participate in the project, so they can make correct new work and recognize drift.

The brand book is a touchpoint of the brand: it is designed, rendered, looked at and refined like any other application. It is not a serialized contract and it is not written in the process's vocabulary.

## 1. Readers decide language, medium and register

Name the actual readers before writing, from the audience and the owner's operation rather than from a template: typically a designer or agency, a supplier or printer, and the person who operates the brand day to day without design training. Add leadership or partners only when they will genuinely read it.

- **Language** is the audience's language (`strategy.audience.language`). Repository or host conventions govern code and commits, never a touchpoint.
- **Medium** is one self-contained HTML document unless the owner requires another medium that can render the system. Type, color and composition must demonstrate themselves; a format that cannot render the system is never the medium. Print is a stylesheet, not a second artifact: A4 pages come from the browser, never from the agent typesetting a PDF.
- **Register** is instruction. The reader obeys the book and puts it down; persuasion belongs to the brand's own touchpoints.

## 2. Three layers with different owners

**Reference** — exact values, inventories, lockup variants, minimum sizes, contrast pairs, downloads. Derived from the contract and from the asset folder, never retyped, and never invented: a number appears only where reproduction depends on it and the contract holds it, not to make the book feel authoritative. An inventory or download grid is generated from the folder; the readable name of an asset comes from the asset itself (its title), not from a second list. Every enumeration in the book matches the folder it describes.

**How-to** — one imperative rule per task, with the reason in a visually secondary layer and the optional variation last. Titles predict content: someone who has read nothing else knows what a section holds. Every term is defined at first use or replaced by a plain one; design jargon is glossed where it first appears; no coined term appears in a title, and no coined term collides with a standard name in this skill (voice, signature, thesis).

**Explanation** — the causal chain `brand job → position → thesis → principles → behavior`, compact, separable from the rules. This is the only layer where the brand's voice may lead the prose, and only if the organization genuinely uses one.

Cover only the dimensions the system actually has; no empty section exists to resemble a conventional table of contents. Process vocabulary never reaches any layer: contract, specification, schema, version of a file, evidence, unresolved, open questions, route names. Pending matters go to the delivery report, never into the book.

## 3. The document is a showpiece

The design layer demonstrates the system at the level of the best work in adjacent categories: a cover with the signature at full force, type specimens at display scale, full-bleed color fields, illustration and imagery at the size they were made for, range pages that show two very different applications sharing one logic, and a failure page that explains the mechanism of a wrong use rather than banning a placement.

Do not sacrifice clarity to self-expression, and do not deliver a generic corporate document that contradicts the identity it describes. Use `visual-artifact-production.md` to build, render and refine the actual pages.

## 4. Package shape

One folder the host already serves statically (for example the public directory of a site), containing:
- the book at the folder root, self-contained: fonts embedded with their license notice, no scripts, no external requests;
- assets in subfolders by kind (logo, illustration, pattern, imagery, applications), every file downloadable;
- relative references only, so the folder survives download, offline use and a change of host;
- a print stylesheet for A4;
- a short stable route that resolves inside the folder, so relative references keep working; the redirect or rewrite is the host's mechanism.

Folder and path names follow the audience's language or the host's convention. The contract lives outside the served folder unless the owner decides the strategy is public. If the host needs a README, it is a one-line pointer to the book; every rule has exactly one address.

## 5. Verify by looking

Render the book on desktop, on a phone and as print, and look at each capture as each named reader: can the supplier find the file they need, can the operator apply a rule without asking, would the designer make a materially different correct application from it? Check the contrast of every text role on every background it appears on with `color_tools.py` when the eye suspects; check every count against the folder; check that nothing from the process is visible. Fix, re-render, look again.

If a guideline repeatedly needs exceptions, fix the system or rewrite the rule instead of documenting more cases.

## Delivery

Deliver the folder: book and assets. Deliver the contract separately, as an operating file. Report pending matters in the conversation, never in the book.
