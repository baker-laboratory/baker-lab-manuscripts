# Baker Lab Manuscript Skill

`baker-lab-manuscript` audits, revises, and formats scientific manuscripts to align them with Baker Lab and Institute for Protein Design (IPD) manuscript expectations. It also draws on recurring structural, rhetorical, and evidentiary patterns identified across recent Baker Lab Lab-Led publications.

## Capabilities

- Route a few-sentence edit within one paragraph through a lightweight local review without loading the paper corpus, selecting comparators, or running the full manuscript checklist.
- Review a complete manuscript or individual sections, including the Abstract, Introduction, Results, Discussion, Methods, figure captions, and acknowledgements.
- Provide an explanatory editorial review, an annotated revision, or a clean revised manuscript.
- Distinguish explicit Baker Lab/IPD requirements, target-journal requirements, and descriptive patterns inferred from prior publications.
- Check whether each major claim is supported by an experiment, figure, table, or citation, and prevent predictions from being presented as experimental validation.
- Select the most relevant Baker Lab papers as comparators based on both scientific genre and target journal.
- Check funding, HHMI acknowledgement, open-access, data availability, code availability, and other submission-readiness requirements.
- Convert an existing DOCX using deterministic layout tokens derived from the December 2025 Nature Communications submission template, with an optional locally supplied template file.
- Apply the Nature visual format to both Nature and Nature Methods while keeping their journal-specific structure and compliance audits separate from each other and from Nature Communications.
- Preserve figures, tables, equations, hyperlinks, citations, and other manuscript content while applying deterministic page layout, typography, line numbers, page numbers, headings, legends, and table formatting.

## Recommended Invocation Prompts

For the most reliable routing, start the request with the explicit skill invocation
`$baker-lab-manuscript`. When known, include the target journal, article type,
submission stage, requested scope, and desired output.

### Full Manuscript Review

Use this prompt for a complete Baker-ready assessment, preparation for David
Baker's review, structural revision, or whole-manuscript submission-readiness
review.

```text
$baker-lab-manuscript

Perform a full Baker Lab/IPD review of the manuscript I uploaded.

Target journal: [Nature / Nature Methods / Nature Communications / other]
Article type: [Article / Brief Communication / other]
Submission stage: [initial submission / acceptance in principle or final formatting]

Review the manuscript for:
1. Scientific story, section structure, and figure-driven Results order.
2. Whether each major claim is supported by data, a figure, a table, or a citation.
3. Baker Lab/IPD requirements for wording, acknowledgements, open access, and submission.
4. Clarity, precision, logical transitions, terminology, and quantitative reporting.
5. Figure legends, references, data and code availability, author contributions,
   competing interests, funding, licensing, and overall submission readiness.

When relevant, select two to five recent Baker Lab papers that match both the
scientific genre and target journal as structural and rhetorical comparators.
Transfer writing strategies only; do not imitate distinctive wording.

Preserve all reported values, units, statistics, citations, figures, tables,
equations, cross-references, and reference-manager fields whenever possible.
Do not overwrite the source manuscript.

Deliver:
- A revised manuscript copy.
- A Baker/IPD and journal compliance report organized as Blocker, Major, Minor,
  and Style.
- A list of unresolved author decisions.
- A source note identifying the requirements, corpus materials, and comparator
  papers actually inspected.
```

### Formatting-Only

Use this prompt when the manuscript text is already settled and the requested
work is deterministic DOCX formatting rather than substantive revision.

```text
$baker-lab-manuscript

Format the uploaded DOCX without making substantive prose revisions or running
a full content review.

Target journal: [Nature / Nature Methods / Nature Communications]
Article type: [Article / other]
Submission stage: [initial submission / acceptance in principle or final formatting]

Please:
1. Preserve the source file and create one separately named formatted DOCX.
2. Apply the matching journal profile for page layout, typography, headings,
   legends, tables, line numbers, and page numbers.
3. Preserve citations, figures, tables, equations, hyperlinks, cross-references,
   and reference-manager fields whenever possible.
4. Inspect the formatter's JSON audit, correct semantic mapping errors involving
   the title, front matter, headings, captions, or reference boundaries, and rerun
   the formatter when needed.
5. Perform the formatting-only visual QA required by the skill and report its
   scope accurately.

Return:
- The separately named formatted DOCX.
- A concise summary of the JSON-audit findings and any unresolved semantic mappings.
```

For Nature Methods, the skill uses the Nature visual format while applying the
selected Nature Methods article-type and submission-stage requirements. It does
not apply the Nature Communications format to Nature or Nature Methods.

### Optional Add-ons

#### Full-Document Visual QA

Formatting-only work uses localized visual QA by default. Add the following
sentence when every page of the finished document must be inspected:

```text
Perform full-document, page-by-page visual QA on the final DOCX and correct any
layout defects you find.
```

#### Authorized Nature Communications Template

The public skill does not redistribute the third-party Nature Communications
DOCX template. If an authorized local copy is supplied and exact template page
geometry is required, add:

```text
Use the authorized Nature Communications template I uploaded for exact template
conversion.
```

This template option is for Nature Communications only.

### Short Invocation Examples

```text
$baker-lab-manuscript Review this complete manuscript against Baker Lab/IPD and
the target journal requirements. Return a revised copy, a categorized compliance
report, and unresolved author decisions.
```

```text
$baker-lab-manuscript Format this DOCX only; do not revise the manuscript text.
Preserve the source and return one journal-matched formatted copy with a concise
format-audit summary.
```

### Information to Provide

When available, include:

1. The target journal and article type.
2. The submission stage: initial submission or acceptance in principle/final
   formatting.
3. The manuscript, paragraph, or sections in scope.
4. The desired output: audit, annotated revision, clean revision, or formatting
   only.
5. The desired artifact type: pasted text, DOCX, or native Google Doc.
6. Whether figures, supplementary information, captions, methods, references,
   and acknowledgements are in scope.

If a full manuscript is supplied without a localized target or output mode, the
skill defaults to a revised manuscript, a Baker/IPD compliance report, unresolved
author decisions, and a note identifying the sources actually used.

## Review routes

- **Lightweight local edit:** a few sentences within one identified paragraph. Reads only the explicit IPD/Baker requirements and journal-formatting reference, applies five locally scoped review passes, runs the DOCX formatter and JSON audit when a DOCX working copy is available, and avoids corpus/comparator/full-checklist work.
- **Formatting-only:** deterministic formatting and JSON audit without a full content review.
- **Full manuscript or structural review:** edits spanning more than one paragraph, structural rewrites, Baker-ready or David-review preparation, complete submission readiness, or corpus comparison. This route loads the corpus and full checklist and runs the full five-pass review.

The selected route is not upgraded merely because the supplied manuscript is long.

## Review Standard

The skill resolves conflicting requirements in the following order:

1. Target-journal requirements that determine submission validity.
2. Explicit Baker Lab/IPD requirements.
3. Repeated patterns in recent Baker Lab Lab-Led papers.
4. General scientific-writing conventions.

Findings are classified as:

- `Blocker`: must be resolved before the manuscript can be considered Baker-ready.
- `Major`: affects the scientific story, evidence, or an important compliance requirement.
- `Minor`: affects local clarity, completeness, or consistency.
- `Style`: an optional improvement to wording or presentation.

## Baker Lab Publication Corpus

The bundled corpus currently covers the user-specified 2022-2026 Lab-Led publications and contains 87 de-duplicated records:

- 86 are labeled `FULL_TEXT_READ`.
- 1 is labeled `ABSTRACT_ONLY`.
- No unauthorized paper mirrors are used.

`FULL_TEXT_READ` means that obtaining the PDF was not sufficient by itself. The paper's opening, main evidentiary sequence, Discussion or conclusion, Methods, and figures/captions were also inspected. Corpus-derived writing patterns are descriptive rather than mandatory: a convention observed in one paper is not treated as a Baker Lab rule.

## Method-Development and Protein-Design Manuscripts

For computational methods, enzyme design, or manuscripts combining both, the skill pays particular attention to whether:

- Method comparisons use fair sampling budgets, inputs, filtering procedures, and evaluation criteria.
- Total generation counts, passing counts, and failed samples are reported instead of showing only successful examples.
- Random seeds, model versions, recycles, diffusion steps, and template/MSA settings are sufficiently documented for reproducibility.
- Ablations support claims about the contribution of individual method components.
- Structure prediction, experimentally determined structure, and functional validation are clearly distinguished.
- Claims accurately represent the evidentiary relationships among the theozyme, motif geometry, cofactors, and catalytic activity.

## Output and Safety Boundaries

The skill does not invent experiments, numerical results, citations, funding, author contributions, or submission status. It does not overwrite the source manuscript. Missing factual information is marked for author confirmation. A manuscript is described as `Baker-ready` only after all `Blocker` findings have been resolved.

For lightweight local edits and formatting-only tasks, the skill defines a task-specific exception to the generic Documents and Google Docs full-document inspection gate: inspect the edited location, affected page, directly affected adjacent pages, and nearby layout details, but not unaffected pages. Full-document page-by-page inspection is used for the full/structural route, an explicit user request, broader layout-sensitive changes, or a plausible document-wide defect. A localized pass is reported as localized and never presented as proof that the whole manuscript is Baker-ready.

## File Structure

- `SKILL.md`: core review and revision workflow.
- `references/ipd-baker-requirements.md`: explicit Baker Lab/IPD requirements.
- `references/corpus-2022-2026.md`: synthesis of the five-year full-text corpus.
- `references/corpus-manifest.tsv`: source, version, and access status for each paper.
- `references/review-checklist.md`: final review checklist.
- `references/journal-formatting.md`: Nature-family formatting rules plus the official download location and provenance for the optional Nature Communications template; the third-party DOCX is not redistributed in this public repository.
- `scripts/fetch_corpus.py`: helper script for refreshing the corpus from authorized sources.
- `scripts/format_manuscript.py`: reusable DOCX formatter and journal-compliance auditor.
- `tests/test_format_manuscript.py`: regression test for formatter correctness and linear paragraph-list access.
