---
name: reference-guided-paper-polishing
description: >-
  Audit a research project and use supplied or externally verified papers as
  structural and rhetorical references to rewrite a scientific manuscript and
  its figure legends. Use for 论文仿写、论文润色、参考论文风格迁移、论文结构重构、图注重写,
  especially when current evidence, numbers, terminology and semantic boundaries
  must remain synchronized. Do not use for isolated grammar fixes, figure-only
  redesign, or citation-free copyediting.
---

# Reference-Guided Paper Polishing

Use this skill as an orchestrated manuscript workflow: establish the current
scientific truth, learn transferable reasoning from reference papers, rebuild
the claim architecture, rewrite prose and legends, then verify the result.

## Operating contract

1. Preserve every supplied number, denominator, sample definition, comparison,
   uncertainty statement and negative result. Never fill a scientific gap with
   more persuasive language.
2. Identify the authoritative manuscript, figures, legends, result summaries,
   validation records and project handoffs before editing. Newest modification
   time alone does not establish authority.
3. Keep confirmed observations, interpretations and hypotheses distinct. Match
   verbs to evidence: `detected`, `was associated with`, `supports`,
   `is consistent with`, `suggests`, `could reflect`, `proved`.
4. Treat reference papers as evidence for writing mechanisms, not as material
   to paraphrase. Transfer paragraph jobs, argument order, claim calibration
   and boundary placement. Do not reproduce sentences or distinctive wording.
5. Do not upgrade association to origin, loading, causality, mechanism,
   diagnostic performance or clinical utility without matching evidence.
6. Create versioned outputs. Do not overwrite the authoritative source unless
   the user explicitly asks for in-place editing.
7. If the target journal or language is unspecified, use a field-appropriate
   high-impact scientific structure and state that choice. Do not invent
   journal rules.

## Workflow

### 1. Intake and source boundary

Identify the project root, current manuscript, figures, legends, claims/results
records, validation reports, reference papers and requested deliverable language.
When a supplied path is missing, locate reasonable in-workspace equivalents and
state the substitution. Do not stop for information that can be recovered from
the project.

Read [references/project-audit-and-task.md](references/project-audit-and-task.md)
before the project audit. Stop the rewrite if the central claim is unsupported
or two authoritative records contradict each other in a way that changes the
claim.

### 2. Project truth, current report and task brief

Build:

- a source-of-truth table;
- a one-sentence North Star;
- a claim-evidence architecture;
- confirmed, assumed and unresolved facts;
- a manuscript/figure/legend inventory;
- a severity-ordered issue list.

Record these in a project report and derive a separate task brief with scope,
required terms, numerical invariants, deliverables, acceptance criteria and
non-goals. Use the templates in
[references/project-audit-and-task.md](references/project-audit-and-task.md).

### 3. Reference corpus

Start with every paper the user supplies. Deep-read the papers that most closely
match the project's evidence structure. Search externally when the user permits
or asks for more references, prioritizing primary studies with traceable DOI,
PMID or stable publisher links.

Use the available `nature-paper-card` workflow for full cards and
`nature-academic-search` for discovery/export when installed. If a skill is
unavailable, follow the equivalent contracts in
[references/reference-analysis-and-transfer.md](references/reference-analysis-and-transfer.md).

For every reference, identify:

- question, purpose and gap;
- study route and evidence order;
- claim-evidence chain;
- language posture and paragraph functions;
- semantic boundaries;
- transferable mechanisms and non-transferable conclusions.

### 4. Reference synthesis

Create a cross-paper transfer matrix keyed by manuscript function: title,
abstract, introduction, each Results unit, discussion, methods and legends.
Separate:

- structure worth imitating;
- language behavior worth calibrating;
- claims that cannot be transferred because the evidence design differs.

Read [references/reference-analysis-and-transfer.md](references/reference-analysis-and-transfer.md)
for the required cards, source labels and transfer matrix.

### 5. Claim architecture and rewrite

Stabilize the claim hierarchy before polishing. Then run the writing layers in
order, adapting to available installed skills:

1. `manuscript-optimizer` for claim architecture, paragraph function and
   figure-text alignment;
2. `scientific-writing` for section drafting and full paragraphs;
3. `write-scientific-manuscript` for paragraph logic and reader guidance;
4. `anti-defensive-writing` after limitations and scope have been fixed;
5. `scientific-prose-style` for sentence rhythm and punctuation;
6. `humanizer-zh` for Chinese prose that is formulaic, repetitive or padded;
7. `figure-planner` for panel roles and legends.

Read [references/rewrite-and-validation.md](references/rewrite-and-validation.md)
for the rewrite order, boundary-preservation rules, bilingual synchronization
and legend contract.

### 6. Validation

Build a machine-checkable package manifest containing:

- files to validate;
- required key numbers and phrases;
- forbidden stale phrases;
- expected reference count and DOI policy;
- arithmetic sums and category totals;
- required boundary concepts.

Run:

```bash
python scripts/check_manuscript_package.py package-check.json
```

Then manually verify citation-to-claim fit, reference metadata, terminology,
figure-text correspondence and unresolved scientific risks. A passing syntax
check is not a scientific audit.

### 7. Delivery

Return the polished manuscript, synchronized legends and translation when
requested, plus a concise revision report. The report must list:

- structural changes;
- claim-strength changes;
- defensive language removed;
- load-bearing limitations retained;
- citations added or corrected;
- numerical and citation verification;
- unresolved factual, visual or submission-readiness issues.

## Hard boundaries

- Do not infer a cell of origin, mechanism, direction of effect, diagnostic
  utility or novelty from association alone.
- Do not remove a limitation because it sounds cautious. First decide whether
  it protects validity, scope, reproducibility, ethics or reporting.
- Do not move conclusion-changing evidence into Supplementary Information to
  create a cleaner narrative.
- Do not claim a figure was visually checked when only its legend was reviewed.
- Do not call a draft submission-ready when journal formatting, rendered DOCX,
  figure legibility or external validation remains open.
