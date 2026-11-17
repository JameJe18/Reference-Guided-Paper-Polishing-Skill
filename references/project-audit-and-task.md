# Project Audit and Task Brief

Use this reference before rewriting any manuscript.

## 1. Source inventory

Scan the project in this order:

1. handoff documents and validation reports;
2. current manuscript files;
3. result summary tables and statistical outputs;
4. figure and legend manifests;
5. data-availability and code records;
6. historical drafts, only as revision evidence.

Exclude vendored runtimes, package caches, archives and exploratory outputs from
evidence collection unless the project explicitly names them as authoritative.
Large repositories often contain hundreds of thousands of irrelevant files; use
targeted file discovery rather than a root-wide deep read.

## 2. Source-of-truth table

Record:

| Artifact | Authoritative path | Authority basis | Current status |
|---|---|---|---|
| Main manuscript | | Handoff, validation, or user designation | |
| Figure legends | | Project manifest or current main draft | |
| Figure files | | Formal output directory | |
| Result tables | | Validated/corrected outputs | |
| Methods | | Reproducible analysis record | |
| Reference list | | Current manuscript | |

Do not use modification time as the sole authority signal. A later-generated
file can be a derived copy, an abandoned experiment, or a weaker summary.

## 3. Project audit report

Write a standalone artifact containing:

1. authoritative versions and version drift;
2. one-sentence North Star;
3. central scientific question;
4. main claim and contribution type;
5. evidence route from input data to final candidate/output;
6. purpose, methods and core results with exact denominators;
7. figure/table/legend inventory and argumentative role;
8. Claim-Evidence Map;
9. confirmed / assumed / unresolved items;
10. severe scientific, structural, terminology and figure-text problems;
11. safe revision scope;
12. evidence gaps that wording cannot repair;
13. recommended task-brief content.

Use these evidence states:

- `fully supported` — directly supported by supplied results;
- `partial` — supported only under a narrower scope;
- `unsupported` — contradicts or exceeds the supplied evidence;
- `hypothesis` — plausible interpretation requiring future testing.

## 4. Claim-Evidence Map

Build at least one row for every substantive claim in:

- title;
- abstract;
- introduction gap and contribution;
- Results section headings and topic sentences;
- Discussion synthesis;
- conclusion;
- Figure legends.

Template:

| Location / claim | Evidence | Status | Required action |
|---|---|---|---|
| | | | keep / narrow / move to hypothesis / add evidence / delete |

Never repair an unsupported claim by adding several defensive qualifiers. Either
narrow the claim, supply evidence, relabel it as a hypothesis, or stop.

## 5. Invariant extraction

Create a compact list of values that must remain stable:

- cohort sizes and comparisons;
- inclusion, exclusion and missing-data denominators;
- candidate and validation counts;
- statistical thresholds, estimates, intervals and multiplicity values;
- category totals and arithmetic relationships;
- gene, RNA biotype and figure-panel identifiers;
- canonical abbreviations.

Store the result in a validation manifest for
`scripts/check_manuscript_package.py`.

## 6. Task brief template

```markdown
# [Project] Manuscript Revision Task

## Goal
## Current authoritative inputs
## Central claim
## Scope
## Out of scope
## Canonical terms
## Numerical invariants
## Required structural changes
## Reference corpus
## Deliverables
## Acceptance criteria
## Known blockers and unresolved issues
```

The acceptance criteria must include evidence preservation, claim strength,
figure-text correspondence, citation verification and output-version rules.

## 7. Parallel work

When subagents are available, independent work can run in parallel:

- project truth and Claim-Evidence Map;
- supplied-reference Paper Cards;
- external literature discovery and metadata verification;
- numerical-package checks.

Assign separate artifacts and avoid concurrent edits to the same manuscript.
The parent agent must integrate the results and retain final responsibility for
scientific judgement.
