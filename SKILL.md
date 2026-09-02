---
name: baker-lab-manuscript
description: Audit, locally revise, and format scientific manuscripts to match Baker Lab and Institute for Protein Design manuscript expectations and Nature-family submission formats. Use for a few-sentence wording edit, a full Baker-ready review, preparation for David Baker's review, Nature-family DOCX or Google Docs formatting, corpus comparison, or checks of manuscript structure, claims, funding, open access, and submission readiness.
---

# Baker Lab Manuscript

Align a manuscript with explicit Baker Lab/IPD requirements and evidence-backed patterns from recent Baker Lab-led papers. Preserve scientific meaning and make the provenance of every recommendation clear.

## Route the task before loading references

Choose exactly one route. Do not silently expand a local request into a full-manuscript audit.

### Lightweight local edit

Use this route only when all of the following are true:

- the requested substantive change is limited to a few sentences within one existing paragraph;
- the target paragraph or exact sentences are identified;
- the request does not add, remove, reorder, or substantially reinterpret manuscript sections, headings, figures, tables, equations, captions, references, or end matter; and
- the user did not request a full audit, Baker-ready assessment, David-review preparation, paper-corpus comparison, or submission-readiness review of the whole manuscript.

If the requested substantive edits span more than one paragraph, the target is not localized, or the change is structural, use the full-manuscript route. Do not upgrade solely because the supplied source is a long manuscript or because deterministic formatting touches styles throughout a DOCX.

For a lightweight local edit:

1. Read `references/ipd-baker-requirements.md` and `references/journal-formatting.md` only. Do not read the corpus synthesis, corpus manifest, or full review checklist unless a separate trigger below applies.
2. Inspect only the target paragraph and the minimum neighboring context needed to understand it.
3. Apply the five local passes in [Lightweight local review](#lightweight-local-review).
4. Revise only the requested sentences and any immediately necessary transition. Preserve all unrelated manuscript content.
5. For a DOCX or a native Google Doc with a DOCX working copy, run the journal-matched formatter, inspect its JSON audit, correct semantic misidentification, and rerun when needed.
6. Apply the artifact workflow and the task-specific visual-QA override below.

### Formatting-only

Use this route when the user requests deterministic formatting or template conversion without substantive prose revision. Read only `references/journal-formatting.md`, run the formatter and JSON audit, resolve semantic mapping problems, and apply the artifact workflow and visual-QA override. Do not load the corpus, choose comparators, run the full five-pass content review, or use the full review checklist unless the user separately requests them.

### Full-manuscript or structural review

Use the full route when any of the following applies:

- substantive edits span more than one paragraph, including multiple disconnected local edits;
- a paragraph is added, removed, or moved, or a section, heading, figure sequence, claim architecture, or other manuscript structure is added, removed, reordered, or substantially rewritten;
- the user requests a complete audit, a Baker-ready determination, preparation for David Baker's review, a clean or annotated full revision, or whole-manuscript submission readiness;
- paper-level comparators, corpus-derived organization, current corpus research, or a complete journal-compliance review is requested; or
- localized review reveals that the requested correction cannot be made responsibly without broader restructuring.

Before a full review or revision, read:

1. `references/ipd-baker-requirements.md` for explicit lab requirements.
2. `references/corpus-2022-2026.md` for the verified five-year corpus synthesis, genre routing, access policy, and writing patterns.
3. `references/review-checklist.md` for the final audit and deliverable format.

Also read `references/journal-formatting.md` when the task includes Word formatting, template conversion, or preparation for Nature, Nature Methods, or Nature Communications.

Read `references/corpus-manifest.tsv` only when selecting or citing paper-level comparators, checking access or version provenance, or refreshing the corpus. Search it by DOI, slug, year, access, or version rather than loading unrelated records.

Treat `ipd-baker-requirements.md` as normative. Treat corpus-derived patterns as descriptive unless multiple relevant recent papers support them.

## Establish the task

Identify only the information that changes the selected route or output:

- the manuscript, paragraph, or section in scope;
- the target journal and article type;
- the submission stage: initial submission or acceptance in principle/final formatting;
- the requested output: audit, annotated revision, clean revision, or deterministic formatting; and
- the desired artifact type: pasted text, DOCX, or native Google Doc.

Ask only for missing information that materially changes the work. A full manuscript with no localized target or output mode defaults to a revised copy plus a concise compliance report. If the target journal is unknown and a formatter run is required, ask for it rather than guessing a formatter profile.

Never overwrite the source manuscript. Preserve citations, cross-references, equations, tables, figures, and reference-manager fields whenever possible.

## Lightweight local review

Run all five passes, but confine every pass to the target sentences, their paragraph, and only the directly needed neighboring context:

1. **Story:** determine the paragraph's local narrative job, logical transition, and whether the edited sentences support that job. Do not map or restructure the full manuscript.
2. **Claims and evidence:** check only claims in the edited sentences against nearby data, figures, tables, or citations. Do not inventory claims elsewhere in the manuscript.
3. **Baker/IPD compliance:** apply only explicit requirements relevant to the edited wording or its immediate context. Do not audit unrelated sections, funding, acknowledgements, or administrative items.
4. **Language and presentation:** improve clarity, precision, transitions, terminology, and quantitative wording while preserving author intent and reported values.
5. **Submission readiness:** check only local journal limits, terminology, citation placement, cross-references, and directly affected layout. Do not issue a whole-manuscript readiness determination.

Do not select comparator papers, refresh the corpus, produce a full `Blocker`/`Major`/`Minor`/`Style` report, or declare the manuscript Baker-ready in this route.

## Format DOCX manuscripts

For a DOCX local edit, formatting-only request, or full template conversion:

1. Preserve the source and write to a new `.docx` path.
2. Confirm the exact journal, article type, and submission stage. Use the Nature visual format for both Nature and Nature Methods while retaining their separate structural and compliance rules. Do not apply the Nature Communications template to either journal.
3. Run `scripts/format_manuscript.py` with matching `--journal`, `--article-type`, `--stage`, `--output`, and `--report` arguments. For `nature-communications`, the formatter uses deterministic built-in layout tokens; pass an authorized local copy with `--template` when exact template page geometry is required.
4. Inspect the JSON audit. Resolve misidentified title, front matter, headings, captions, or reference boundaries and rerun when needed. The script formats but does not silently reorder, rewrite, or invent manuscript content.
5. Use the Documents workflow for safe DOCX handling, preserving all of its requirements except the full-document visual-QA scope explicitly replaced below.

The optional Nature Communications template is available from the official source recorded in `references/journal-formatting.md`; this public repository does not redistribute the third-party DOCX. Treat it as a Nature Communications asset only. Nature and Nature Methods initial submissions permit flexible formatting, so describe the applied layout as review-ready formatting rather than mandatory publisher typography.

## Handle native Google Docs

Use the Google Docs workflow for document identity, target confirmation, trusted reads, native copying, preservation, writes, readback, and post-import repair.

- Never edit the source manuscript in place; create or use a clearly identified working copy.
- Export or download a DOCX working copy when the selected route requires `scripts/format_manuscript.py`.
- Apply local prose edits only to the identified paragraph and verify the edited native range after writing.
- Return a native Google Doc only when requested. When returning a deterministically formatted native document, import the QA-passed DOCX through the Google Docs workflow, then perform required connector readback and repair.
- Preserve native tabs, structure, links, controls, and supported smart-chip semantics. Do not replace a native document through DOCX import when the user only asked for a native text edit and did not request deterministic native reformatting; in that case use the formatter output as the required format audit and keep the edit native.

All Google Docs safety and preservation rules remain in force except the full-document PDF visual-QA scope explicitly replaced below.

## Task-specific visual-QA override

This section is a deliberate, task-specific exception to generic Documents and Google Docs skill instructions that otherwise require full-document rendering or inspection for every final deliverable. When those generic skills are active together with this specialized skill, use this section to resolve the QA-scope conflict: the localized scope below supersedes their generic full-document shipping gate for the lightweight and formatting-only routes. A direct system, developer, or user instruction outside those generic skill defaults still controls.

For a lightweight local edit or formatting-only route:

- do not render, rasterize, or inspect every unaffected page solely because the artifact is a final DOCX or Google Doc;
- inspect the edited location, its rendered page when available, directly affected adjacent pages, and nearby equations, figures, tables, captions, headers, footers, line numbers, page numbers, or page breaks;
- when the renderer or PDF export produces all pages, inspect only this localized set unless an escalation trigger applies;
- routine document-wide style application by `format_manuscript.py` does not by itself trigger full-document inspection; and
- report localized QA accurately and do not claim that the whole document was visually inspected.

Escalate to full-document page-by-page visual QA only when:

- the user explicitly requests it;
- the selected route is the full-manuscript or structural route and a revised DOCX or native Google Doc will be delivered;
- the requested change, beyond the formatter's routine normalization already exempted above, affects figures, tables, equations, headers, footers, section breaks, page setup, or other layout-sensitive structures outside the localized area; or
- localized inspection or the JSON audit identifies a plausible document-wide defect.

Do not treat the generic Documents or Google Docs wording alone as a reason to ignore this task-specific exception. Preserve all of their non-conflicting safety, target-confirmation, source-preservation, and readback requirements, and do not modify those generic skills.

## Apply the source hierarchy

Resolve conflicts in this order:

1. Target-journal requirements that determine submission validity.
2. Explicit Baker Lab/IPD requirements.
3. Repeated patterns in recent Baker Lab Lab-Led papers.
4. General scientific-writing conventions.

Do not force a Nature-style section structure onto a journal that requires a different format. Explain each meaningful conflict and state which rule controlled the decision.

## Refresh or use the paper corpus

Use the bundled corpus only in the full route when corpus evidence is relevant. Route a full manuscript to two to five comparators matching both scientific genre and target journal. For mixed papers, combine the applicable genre playbooks.

When the user requests a current corpus comparison:

1. Retrieve the official Lab-Led list for the rolling five-year window: the current calendar year plus the preceding four years.
2. De-duplicate preprint and journal versions and resolve each DOI to the version of record or latest authoritative preprint.
3. Label access as `FULL_TEXT_READ`, `ABSTRACT_ONLY`, `METADATA_ONLY`, or `UNVERIFIED`.
4. Extract structure and style only from inspected text and prefer papers matching both genre and target journal.

If the official list is inaccessible, use the bundled snapshot, disclose that it was not refreshed, and describe it as complete only for the user-supplied 2026-08-25 export. Never use unauthorized mirrors.

## Full review in five passes

Apply these passes only in the full-manuscript or structural route:

1. **Story and structure:** map opening, challenge, action, and resolution; check section jobs and figure-driven Results order; select two to five relevant comparators when corpus routing is in scope.
2. **Claims and evidence:** link every major claim to its result, figure, table, or citation and separate observation, inference, and interpretation.
3. **Baker/IPD compliance:** apply every relevant hard rule in `ipd-baker-requirements.md`.
4. **Language and presentation:** improve topic sentences, transitions, verbs, quantitative wording, repetition, chronology, and terminology while preserving scientific meaning.
5. **Submission readiness:** check figures and captions, abbreviations, references, availability statements, competing interests, contributions, funding, licensing, and internal administrative steps.

Use `references/review-checklist.md` before finalizing the full route. A manuscript is not Baker-ready while a blocker remains unresolved.

## Revise safely

- Preserve all reported values, units, sample sizes, thresholds, accession codes, and statistical statements unless correcting an obvious formatting error.
- Never invent experiments, citations, funding, author contributions, vendors, data availability, or submission status.
- Mark factual gaps as `[AUTHOR TO CONFIRM: ...]` in an annotated version; do not leave such markers in a clean version unless requested.
- Distinguish a required correction from an optional stylistic preference.
- Keep hedging proportional to evidence.
- Transfer organization and rhetorical function from prior papers, never distinctive wording.

## Deliver by route

For a lightweight local edit, provide the revised artifact or replacement text plus a concise note limited to material local issues and any unresolved author decision. Do not add a full compliance report or comparator/source survey.

For formatting-only, provide one separately named formatted artifact plus the relevant JSON-audit findings and unresolved semantic mappings. Do not also create a second content-revised manuscript unless requested.

For the full route, unless the user requests another output, provide:

1. a revised manuscript copy;
2. when formatting was requested, one separately named formatted artifact;
3. a Baker/IPD and journal compliance report organized as `Blocker`, `Major`, `Minor`, and `Style`;
4. unresolved author decisions; and
5. a source note stating which guidance, journal requirements, templates, and corpus materials were inspected.
