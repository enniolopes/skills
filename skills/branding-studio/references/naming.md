# Naming — a pipeline with gates

A name is a strategy decision, not a brainstorm. It comes AFTER the levers and the theme. Changing a name early is cheap; late is expensive — the pipeline exists to get it right before reputation accumulates.

## Two-axis taxonomy (agency standard)

Every candidate is classified on:
- **Approach**: descriptive (says what it does: PayPal) → suggestive (association: Spotify, Uber) → abstract (no semantic link: Apple, Kodak).
- **Construct**: real-word | compound (Facebook) | coined (Zapier, Cisco).

Central trade-off: descriptive communicates instantly but is legally weak (hard to register) and locks scope; abstract/coined is legally strong and flexible but requires investment to mean anything. **Research institutes lean descriptive/institutional (an acronym with buildable meaning); category-creating startups lean suggestive/coined.**

## Pipeline

### 1. Forced generation across the types
Generate candidates in ALL relevant cells of the taxonomy (do not let sampling converge to the default type). Sources: theme metaphors, evocative real words, Latin/other languages, invention by blending/truncation, acronym with meaning. Consult the portfolio: types and prefixes/suffixes already used by sisters go into `$excludes`.

### 2. Phonosemantic score (real but modest effect)
Empirical base (Yorkston & Menon 2004; Klink): front vowels (/i/, /e/) evoke small-light-fast-near; back vowels (/o/, /u/) evoke large-robust-heavy; plosives (k, t, p) → angular/technical; sonorants (l, m, n) → soft/organic (bouba/kiki). Compare the sound profile with the theme's target attributes. **Record as a signal, never as the decider** — the effect is modest and depends on semantic congruence.

### 3. Language disaster check
Pronunciation and connotation in pt-BR + English + declared target markets. Say it out loud. Slang and double meanings (history is cruel: Pajero, Fitta, Mondelez). Spellable over the phone.

### 4. Clearance triage (the skill triages; the final opinion is a lawyer's)
- **INPI (Brazil)**: search e-Marcas per Nice class. Fees are PER CLASS. Typical tech classes: **42** (SaaS, development, scientific research — the natural class for research institutes too), **9** (downloadable software, hardware), **35** (commerce/management), **41** (education/training). Relevant collision = identical/confusable name in the same or an adjacent class. Typical registration timeline: 12–24+ months. Identical marks in distinct classes can coexist.
- **Domains**: .com.br and .com (or a declared viable variation). **Handles** on the relevant networks.
- **International**: with global ambition, plan via the Madrid System (single filing from the INPI base registration). Mind the **5-year dependency** (central attack): if the base mark falls, the international registration falls with it — coined names are safer base marks (lower refusal risk).
- Always web-search: fees and rules change; confirm current values before quoting numbers to the user.

### 5. Final gate
Shortlist of up to 3 survivors → SINGLE choice with written rationale ($rationale: why this name expresses the theme) + record of what was excluded ($excludes). Explicit recommendation to the user: full legal search by a lawyer BEFORE investing in the mark, and buy the domains immediately after deciding.

Provisional tier: steps 1–3 + a quick look at INPI/domains, with `human_legal_clearance: PENDING` and `inpi_status: not_searched` explicitly kept — full clearance happens at promotion.

## Recording in the spec
Fill the spec's `naming` block completely, including clearance status. A name without triaged clearance does NOT leave full-tier CREATE.
