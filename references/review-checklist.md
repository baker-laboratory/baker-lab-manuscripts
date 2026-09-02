# Baker/IPD manuscript review checklist

Use this checklist only for the full-manuscript or structural route after revision. Do not load or apply it for a lightweight few-sentence edit or a formatting-only task unless the user separately requests a full compliance audit. Record `Pass`, `Needs author confirmation`, `Not applicable`, or a severity-ranked finding.

## Intake and integrity

- Source manuscript preserved; revision created as a separate artifact.
- Target journal and article type identified or explicitly marked unknown.
- Scientific values, units, sample sizes, thresholds, statistics, citations, and cross-references preserved.
- No facts, citations, funding, authorship, experiments, vendors, or availability statements invented.
- All factual placeholders and author questions collected.
- A revised DOCX or native Google Doc delivered from the full-manuscript or structural route passed full-document page-by-page visual QA. Lightweight and formatting-only tasks use the task-specific localized QA scope defined in `SKILL.md` and do not use this checklist.

## Story

- One-sentence problem, gap, approach, main evidence, and significance can each be stated.
- Conceptual opening-challenge-action-resolution arc is coherent.
- Main-text order follows the scientific story rather than experimental chronology.
- Each figure has a clear narrative job and appears in a logical sequence.

## Corpus routing

- Two to five comparators match the manuscript's scientific genre and target journal.
- Every section-level corpus recommendation comes from a `FULL_TEXT_READ` record.
- Preprints and author manuscripts are identified and are not used to infer final journal formatting.
- Review articles are used for field framing, not primary-research Results structure.
- Corpus patterns are described as recommendations, not Baker/IPD requirements.

## Abstract

- Broad context, specific gap, problem, main result, key evidence, and significance are all present.
- Quantitative results are used where informative.
- No claim exceeds the evidence in the manuscript.
- Length and structure fit the target journal.

## Introduction

- Paragraph 1 narrows to a clearly stated unsolved problem.
- Paragraph 2 gives the protein-design rationale.
- Optional paragraph 3 explains only essential design logic.
- The opening paragraphs do not recap the study's results.
- Citations support every nontrivial field statement.

## Results

- Headers communicate findings or questions rather than procedures alone.
- Each result unit presents data before inference and distinguishes interpretation.
- Every discussed dataset was introduced in Results.
- Claims point to the correct figure, table, statistic, or citation.
- Negative results and limitations relevant to interpretation are not hidden.
- Every success rate has an explicit denominator and stage label.
- Computational pass rate, expression, binding, structural validation, and functional success are not conflated.

## Computational method comparisons, when applicable

- Baselines receive comparable inputs, sampling budgets, evaluation regions, filters, and prediction protocols.
- Best-of-budget performance is distinguished from per-sample efficiency.
- Model/checkpoint versions, random-seed policy, sampling steps, recycle settings, templates, MSA policy, and thresholds are reported when relevant.
- Hyperparameter selection and development targets are separated from final evaluation targets.
- Ablations isolate the contribution of each proposed component.
- Training/test overlap, structure-date cutoffs, homolog leakage, and benchmark exclusions are disclosed.
- Failed generations and filter attrition remain in the appropriate denominator.

## Enzyme and multistate design, when applicable

- Theozyme, catalytic motif, transition state, intermediates, cofactors, and relevant atomic constraints are defined.
- Motif geometry, foldability, sequence compatibility, predicted structure, experimental structure, and catalytic activity are treated as distinct evidence levels.
- Each modeled state or reaction intermediate and its evaluation criterion are stated.
- RMSD reports define aligned atoms/residues, reference structure, mapping, and aggregation rule.
- Kinetic claims distinguish `kcat`, `KM`, and `kcat/KM`.

## Discussion

- Opens with the main advance in field context.
- Does not replay the Results section.
- Compares fairly with prior work.
- States strengths, limitations, and boundaries of generality.
- Ends with specific significance and defensible future directions.
- Length is proportionate; two or three paragraphs are preferred when sufficient.

## Baker-specific language

- Final predicted structure is defined as the design model when applicable.
- Experimental structure is compared with the design, not framed as prediction success.
- Synthetic genes are described as obtained, not ordered.
- Gene vendor appears in Methods when applicable.

## Figures and captions

- Figure dimensions, fonts, and file formats match the journal.
- Colors are consistent, accessible, and semantically stable.
- Axes, units, ticks, sample sizes, and statistical notation are complete.
- Captions define panels, abbreviations, encodings, and tests.
- Molecular views use purposeful orientation and zoom.
- Final-size inspection reveals no unreadable text, excess whitespace, clipping, or overlap.

## End matter

- Author list, affiliations, contributions, and competing interests are present and consistent.
- Funding is relevant and attributed to recipients.
- David is attached to his awards and HHMI is acknowledged when he is an author.
- No internal UW identifiers beginning `GF`, `GR`, `PG`, or `AWD` appear.
- Every author is asked to confirm funding.
- Data, code, model, structure, and accession availability statements are complete.
- CC BY open access is planned; NIH-funded work has a PubMed Central plan.
- Authorized internal manuscript-record and communication steps are recorded as administrative actions, not silently assumed complete.

## Compliance report format

### Blocker

Use for submission-invalid formatting, missing required sections, unsupported central claims, unresolved authorship/funding/licensing, corrupt cross-references, or missing essential data/code availability.

### Major

Use for story architecture, Introduction/Discussion structure, claim-evidence mismatch, major figure problems, or substantial Baker-specific noncompliance.

### Minor

Use for local clarity, terminology, caption completeness, citation placement, or formatting inconsistencies.

### Style

Use for optional improvements that do not affect correctness or compliance.

For every finding, include:

- location;
- current issue;
- governing source: `Journal`, `Explicit IPD/Baker`, `Corpus pattern`, or `General writing`;
- proposed fix;
- whether author confirmation is required.

End with:

1. `Ready for David review: Yes/No`.
2. Remaining blockers.
3. Author decisions needed.
4. Corpus and guidance actually inspected.
