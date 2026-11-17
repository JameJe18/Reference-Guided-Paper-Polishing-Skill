# Rewrite and Validation

Use this reference after the project truth and reference synthesis are stable.

## 1. Rewrite order

Apply these layers in order:

1. **Claim architecture**: answer the central question with the strongest
   evidence-supported claim.
2. **Section jobs**: title, abstract, introduction, Results, Discussion, Methods,
   conclusion, legends.
3. **Paragraph jobs**: one main function per paragraph.
4. **Evidence order**: question → why the analysis is needed → design → finding
   → bounded inference.
5. **Terminology**: one canonical term per concept.
6. **Rhetorical posture**: remove defensive scaffolding after the scope is fixed.
7. **Sentence quality**: rhythm, punctuation, repeated openers and hedge stacking.
8. **Language naturalization**: remove template-like Chinese or jargon without
   changing facts or certainty.

## 2. Section contracts

### Title

Use the highest evidence-supported concept. Prefer object + evidence/action +
scope. Do not place an unverified mechanism in the title.

### Abstract

Use one evidence chain:

```text
problem and exact gap
→ approach needed to answer it
→ one main result
→ one or two decisive supports or boundaries
→ bounded implication
```

Do not compress the abstract by deleting the evidence boundary.

### Introduction

Use:

```text
field problem
→ why current measurements/approaches are insufficient
→ what prior work establishes
→ exact unresolved question
→ study route
```

Do not list methods or report all Results numbers in the introduction.

### Results

Organize by evidence questions, not file or script chronology. Each subsection
should contain:

```text
question / result-led opening
→ decisive numbers
→ relationship to the previous evidence
→ interpretation licensed by this analysis
→ necessary boundary
```

Use a result-allocation table when the manuscript is long:

| Result | Function | Main text / caption / SI | Reason |
|---|---|---|---|

### Discussion

Use:

```text
main advance
→ explanation of the joint findings
→ competing or non-exclusive interpretations
→ comparison with prior work
→ specific limitations
→ validation path
```

Do not replay every figure. Do not use a new result in the Discussion.

### Methods

Favor reproducibility. For each major module, record motivation, exact input,
operation, output, statistical assumptions and interpretive boundary.

### Conclusion

Use contribution → decisive evidence → implication → scope. Keep it shorter
than the Discussion.

## 3. Defensive-writing boundary

Remove sentences that exist only to negotiate with an imagined critic. Preserve
limitations that affect:

- validity;
- evidence interpretation;
- application scope;
- study design;
- reproducibility;
- ethics, law or safety.

Preferred repair:

```text
old: These data cannot distinguish X from Y.
new: Distinguishing X from Y requires [specific additional evidence].
```

Do not repeat the same limitation in the abstract, every Results section, the
Discussion, conclusion and all legends. State it once where it first affects
interpretation, then synthesize it once in the Discussion.

## 4. Figure legends

For every figure:

1. state the figure or panel's role;
2. define samples, comparisons, units and visual encodings;
3. preserve key denominators needed to read the plot;
4. define statistics and abbreviations;
5. keep claim interpretation no stronger than the plotted evidence;
6. keep complete numerical reporting in one authoritative location.

Do not make the legend a duplicate Results section. Do not claim visual QA when
only the text was changed.

## 5. Translation and bilingual synchronization

When producing multiple languages:

- freeze the fact chain and terminology before translating;
- translate intent and evidence order, not sentence syntax;
- run numerical and citation checks on every language;
- make legends correspond panel by panel;
- record any unavoidable wording difference that changes scope.

For Chinese, use `humanizer-zh` when installed. Preserve formal scientific
register and always keep numbers, uncertainty, negation and attribution.

## 6. Validation manifest

Create a JSON file for `scripts/check_manuscript_package.py`:

```json
{
  "files": [
    "manuscript.md",
    "figure-legends.md"
  ],
  "required_phrases": [
    "1,007",
    "980",
    "72.0%"
  ],
  "forbidden_phrases": [
    "913"
  ],
  "reference_count": 31,
  "require_reference_doi": true,
  "citation_range": [1, 31],
  "sums": [
    {"total": 980, "parts": [54, 13, 607, 306]}
  ],
  "required_concepts": [
    "non-paired",
    "cell-type expression association",
    "validation"
  ]
}
```

The checker only validates declared invariants. It does not verify that a source
supports a citation or that a statistical test is appropriate.

## 7. Final gate

Before delivery, confirm:

- authoritative source preserved;
- new output versioned;
- claim hierarchy stable;
- major numbers and sums unchanged;
- citations cover the reference list and avoid stale numbering;
- every added reference has verifiable metadata;
- terms are consistent across abstract, Results, Discussion and legends;
- all load-bearing limitations remain;
- figure-text references and panel letters match;
- visual figures and rendered documents have been inspected separately when
  those formats are part of the deliverable;
- unresolved evidence gaps are reported rather than hidden in polished prose.
