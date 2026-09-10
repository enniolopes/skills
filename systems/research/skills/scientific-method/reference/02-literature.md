# Phase 2 — Literature

Sources located 2026-09-10, not yet read at source.

**When this applies.** Before the protocol is frozen, and again whenever a new claim about
the state of knowledge enters the manuscript.

**What it requires.**

- A documented search: where, with which terms, on which date. Narrative reviews borrow
  this discipline from PRISMA without the full systematic-review apparatus.
- Every source verified at its DOI record (Crossref) or landing page *before* it is
  written into the text. Record: DOI, what it actually says in one sentence, the date.
- A finding read only from an abstract or excerpt is marked as such in the verification
  log and cited with that qualifier.
- Classify each finding: **established** (the literature settles it), **silent** (nobody
  has asked), **what this study adds**. The gap statement is one paragraph built from the
  "silent" column.
- No citation from memory. If the DOI cannot be resolved, the citation is `NOT_VERIFIED`
  and does not enter the manuscript until it is.

**The error it prevents.** A citation that does not say what it is cited for; a "gap" that
a known paper already filled; a reference list that cannot be reproduced because the
search was never recorded.

**Exit gate.** The verification log is complete (one row per source, none `NOT_VERIFIED`
in the text); the gap is stated in one paragraph.

**Sources.** Page et al. 2021, PRISMA 2020 (documented search, selection and appraisal).
Crossref REST API as the verifier (`https://api.crossref.org/works/<doi>`).
