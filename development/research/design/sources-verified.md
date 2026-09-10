# Sources verified — roadmap step 1

Date of verification: 2026-09-10. Verifier: this repository's build session.

**Verification level reached: `located`, not `read`.** In the build environment the
network policy blocked `api.crossref.org`, `doi.org` and every publisher domain, so no DOI
record or landing page was fetched. Each source below was located through a web-search
index that returned the publisher's landing page (or the DOI URL) with matching title,
authors, venue and year; the "what it says" column is taken from the abstract or
publisher summary returned in the index. Before any `reference/` line is treated as
`read`, re-run this table in an environment with scholarly network access and upgrade the
level per row. Nothing below entered `reference/` from memory alone; nothing below has yet
been read at its source in this build.

Levels: `read` — DOI record or landing page fetched and read; `located` — index returned
the landing page/DOI with matching metadata; `unresolved` — could not be located.

| # | Source | DOI / URL | Phase | What it says (one sentence) | Level |
|---|---|---|---|---|---|
| S01 | King, Keohane & Verba (1994). *Designing Social Inquiry*. Princeton UP. | press.princeton.edu/books/hardcover/9780691224633 | 1 | One logic of inference underlies qualitative and quantitative research: frame the question, state uncertainty of every inference, guard against selection bias and measurement error. | located |
| S02 | Booth, Colomb, Williams, Bizup & FitzGerald (2016). *The Craft of Research*, 4th ed. U. Chicago Press. | press.uchicago.edu (bo215874008) | 1, 6 | A research argument is built from claims, reasons, evidence, and answers to anticipated reader objections. | located |
| S03 | Page et al. (2021). The PRISMA 2020 statement. *BMJ* 372:n71. | 10.1136/bmj.n71 | 2 | Reporting a review requires a documented search, explicit selection, appraisal and synthesis of sources (27-item checklist). | located |
| S04 | Crossref REST API (verifier tool). | api.crossref.org | 2 | Returns the metadata record registered for a DOI; the check that a citation exists and says what it is cited for starts here. | tool — blocked in this build |
| S05 | Nosek, Ebersole, DeHaven & Mellor (2018). The preregistration revolution. *PNAS* 115(11):2600–2606. | 10.1073/pnas.1708274114 | 3 | Mistaking postdiction for prediction reduces credibility; preregistering hypotheses, methods and analyses before data keeps the two distinct. | located |
| S06 | Lakens (2017). Equivalence tests: a practical primer. *SPPS* 8(4):355–362. | 10.1177/1948550617697177 | 3, 5 | A claim of "no meaningful effect" is testable only against equivalence bounds fixed in advance (TOST). | located |
| S07 | Simonsohn, Simmons & Nelson (2020). Specification curve analysis. *Nat Hum Behav* 4:1208–1214. | 10.1038/s41562-020-0912-z | 3, 5 | Enumerate all theoretically justified, statistically valid, non-redundant specifications; display them; infer jointly across them. | located |
| S08 | Hernán & Robins (2020). *Causal Inference: What If*. Chapman & Hall/CRC. | miguelhernan.org/whatifbook | 3, 5 | Causal effects from observational data require explicit identification assumptions (exchangeability, positivity, consistency); the target trial makes them inspectable. | located |
| S09 | Simmons, Nelson & Simonsohn (2011). False-positive psychology. *Psychol Sci* 22(11):1359–1366. | 10.1177/0956797611417632 | 3 | Undisclosed flexibility in data collection and analysis makes anything significant; disclosure rules for authors and reviewers are the remedy. | located |
| S10 | Gelman & Loken (2014). The statistical crisis in science. *Am Sci* 102(6):460. | americanscientist.org/article/the-statistical-crisis-in-science | 3, 5 | Data-dependent analysis choices form a garden of forking paths even without intent to fish; the remedy is to fix the path before seeing the data. | located |
| S11 | Gilbert et al. (2018). GUILD: GUidance for Information about Linking Data sets. *J Public Health* 40(1):191–198. | 10.1093/pubmed/fdx037 | 4 | Report, at each step of a linkage, the information needed to assess linkage error and its impact on results. | located |
| S12 | Gebru et al. (2021). Datasheets for datasets. *CACM* 64(12):86–92. | 10.1145/3458723 | 4 | Every dataset should ship a datasheet: motivation, composition, collection, preprocessing, uses, distribution, maintenance. | located |
| S13 | Wilkinson et al. (2016). The FAIR Guiding Principles. *Sci Data* 3:160018. | 10.1038/sdata.2016.18 | 4, 8 | Data and metadata should be Findable, Accessible, Interoperable and Reusable, by machines as well as people. | located |
| S14 | Hundepool et al. (2012). *Statistical Disclosure Control*. Wiley. | 10.1002/9781118348239 | 4 | Publishing statistics requires controlling the disclosure risk of small cells and identifiable units; thresholds and suppression are the standard tools. | located |
| S15 | VanderWeele & Ding (2017). Sensitivity analysis in observational research: the E-value. *Ann Intern Med* 167:268–274. | 10.7326/M16-2607 | 5 | The E-value is the minimum strength of unmeasured confounding, on the risk-ratio scale, that would explain away an observed association. | located |
| S16 | Wagstaff, Paci & van Doorslaer (1991). On the measurement of inequalities in health. *Soc Sci Med* 33(5):545–557. | 10.1016/0277-9536(91)90212-U | 5 | Of the inequality measures in use, only the slope index and the concentration index reflect socioeconomic inequality faithfully. | located |
| S17 | O'Donnell, van Doorslaer, Wagstaff & Lindelow (2008). *Analyzing Health Equity Using Household Survey Data*. World Bank. | openknowledge.worldbank.org (6896) | 5 | Concentration index, its decomposition and related equity measures, with implementation guidance. | located |
| S18 | Anselin (1995). Local indicators of spatial association—LISA. *Geogr Anal* 27(2):93–115. | 10.1111/j.1538-4632.1995.tb00338.x | 5 | Global spatial autocorrelation (Moran's I) decomposes into local indicators that expose hot spots and influential locations. | located |
| S19 | Moran (1950). Notes on continuous stochastic phenomena. *Biometrika* 37(1–2):17–23. | 10.1093/biomet/37.1-2.17 | 5 | Defines the statistic later called Moran's I for spatial autocorrelation. | located |
| S20 | Cameron & Trivedi (2013). *Regression Analysis of Count Data*, 2nd ed. Cambridge UP. | cambridge.org (2AB83B406C5798030F7C91ECC99B1BE4) | 5 | Count models — Poisson, negative binomial, hurdle, zero-inflated — with their assumptions, diagnostics and bootstrap methods. | located |
| S21 | Cameron, Gelbach & Miller (2008). Bootstrap-based improvements for inference with clustered errors. *REStat* 90(3):414–427. | 10.1162/rest.90.3.414 | 5 | With few clusters, cluster-robust standard errors over-reject; cluster bootstrap-t procedures correct this. | located |
| S22 | Gopen & Swan (1990). The science of scientific writing. *Am Sci* 78(6):550–558. | americanscientist.org | 6 | Readers interpret prose through structural expectations (topic/stress positions, subject–verb proximity); meet them and complexity becomes legible. | located |
| S23 | Schimel (2012). *Writing Science*. Oxford UP. | ISBN 9780199760244 | 6 | A paper is a story with a structure; clarity follows from choosing and holding that structure. | located |
| S24 | Heard (2016). *The Scientist's Guide to Writing*. Princeton UP. | press.princeton.edu/books/paperback/9780691170220 | 6 | Absolute clarity is the goal; structure, revision, citation handling and responding to review are learnable practice. | located |
| S25 | von Elm et al. (2007). STROBE statement. *PLoS Med* 4(10):e296. | 10.1371/journal.pmed.0040296 | 7 | 22-item checklist for reporting observational studies (cohort, case-control, cross-sectional). | located |
| S26 | Benchimol et al. (2015). RECORD statement. *PLoS Med* 12(10):e1001885. | 10.1371/journal.pmed.1001885 | 7 | Extends STROBE for routinely collected data: codes, linkage, data cleaning and access must be reported. | located |
| S27 | Munafò et al. (2017). A manifesto for reproducible science. *Nat Hum Behav* 1:0021. | 10.1038/s41562-016-0021 | 7 | Measures across methods, reporting, reproducibility, evaluation and incentives improve reliability; adoption requires iterative evaluation. | located |
| S28 | FAPESP. Gestão de dados — Plano de Gestão de Dados (mandatory since 2020-09-01). | fapesp.br/gestaodedados | 8 | Proposals carry a ≤2-page data management plan: data and metadata produced, legal/ethical restrictions, privacy, preservation and sharing policy and embargo. | located |
| S29 | Elsevier. Generative AI policies for authors. | elsevier.com/about/policies-and-standards | 8 | AI use in manuscript preparation is allowed with oversight and must be declared in a fixed section before the references; AI cannot be an author. | located |
| S30 | SciELO (2023). Guide for the use of AI tools in research communication. | blog.scielo.org (2023-08-30) | 8 | Declare tool and version, purpose, limits of AI contribution, impact on writing/analysis, ethical compliance; AI is not an author. | located |
