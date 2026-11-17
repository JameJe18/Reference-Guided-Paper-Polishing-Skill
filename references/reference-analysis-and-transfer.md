# Reference Analysis and Transfer

Use this reference when building reference cards, expanding the corpus, or
deciding what can be imitated.

## 1. Source coverage

Label each paper:

- `full-text`: methods, results, figures/tables and discussion are available;
- `abstract/metadata`: only the abstract and verified bibliographic record are
  reliable;
- `partial`: some sections or supplements are unavailable.

Never infer unseen experiments, limitations or numeric results from the title
or abstract. Record whether citations were verified through Crossref, PubMed,
Europe PMC, PMC or another stable source.

## 2. Deep-reference card

When `nature-paper-card` is available, use its full Sections 01–16 contract. If
not, produce an equivalent compact card with:

1. bibliographic record and source coverage;
2. one-sentence result;
3. research question and clinical/scientific stake;
4. background route and exact gap;
5. core insight and study design;
6. methods and evidence order;
7. results as a claim-evidence chain;
8. author-acknowledged limitations;
9. independent critical analysis;
10. language and paragraph mechanics;
11. semantic boundaries;
12. transferable writing mechanisms;
13. non-transferable claims;
14. relevance to the target manuscript.

## 3. Language and structure analysis

For each reference, inspect how it:

- opens with relevance before technical detail;
- states the exact unresolved question;
- orders evidence rather than experiments;
- distinguishes observation from interpretation;
- positions limitations near the claims they constrain;
- moves from local findings to field implications;
- calibrates verbs, quantifiers and novelty language;
- uses citations for positioning rather than breadth display.

Record sentence-level observations as mechanisms, not phrases to copy. For
example: “separates clinical problem and assay design into separate paragraphs”
is transferable; a copied sentence is not.

## 4. External expansion

Search by evidence axes, not only topic keywords:

- same disease and molecular compartment;
- same origin-tracing problem in another disease;
- same tissue-to-biofluid or longitudinal design;
- same multi-omics integration route;
- same clinical comparison but different assay;
- methods that expose a boundary or alternative interpretation;
- clinical validation studies that show what the present project has not done.

Create:

- a reproducible search log;
- a candidate table with DOI, PMID, PMCID, access status and relevance;
- full cards for the closest papers;
- a citation-verification record.

Candidate table minimum columns:

```text
id  title  first_author  year  journal  doi  pmid  pmcid  oa
relevance  evidence_level  planned_use
```

## 5. Transfer matrix

Create one row per manuscript function:

| Target function | Reference mechanism | Target location | Safe adaptation | Non-transferable conclusion |
|---|---|---|---|---|
| Title | | | | |
| Abstract background | | | | |
| Abstract result | | | | |
| Introduction gap | | | | |
| Results unit 1 | | | | |
| Results unit 2 | | | | |
| Discussion synthesis | | | | |
| Methods motivation | | | | |
| Figure legends | | | | |
| Conclusion | | | | |

## 6. Semantic-boundary ladder

Do not move upward without direct evidence:

```text
detected difference
→ association
→ directional concordance or compatibility
→ possible source / possible mechanism
→ experimentally supported source / mechanism
→ causal or clinical utility claim
```

Examples of forbidden upgrades:

| Available evidence | Forbidden stronger claim |
|---|---|
| case-control difference | tumour-derived molecule |
| expression association in a reference atlas | confirmed cellular origin |
| magnitude difference between compartments | selective loading efficiency |
| same-direction change | causal transport |
| same-cohort discrimination | externally validated diagnosis |
| prediction model fit | demonstrated mechanism |

When a stronger claim is central to the user's desired narrative, surface it as
an evidence blocker rather than writing around it.

## 7. Reference synthesis

After the cards, write a cross-paper synthesis covering:

- shared argument chain;
- useful section-specific writing mechanisms;
- language posture;
- boundary patterns;
- differences in study design that prohibit conclusion transfer;
- final recommended narrative architecture.

This synthesis, not the raw cards, governs the rewrite.
