# Journal formatting and DOCX conversion

Use this reference for every lightweight local edit under this skill and whenever the user asks to format, reformat, template, or convert a manuscript DOCX or native Google Doc. The target journal and submission stage control the result.

## Contents

- [Do not conflate the journals](#do-not-conflate-the-journals)
- [Optional Nature Communications template](#optional-nature-communications-template)
- [Reusable formatter](#reusable-formatter)
- [Nature Article rules](#nature-article-rules)
- [Nature Methods rules](#nature-methods-rules)
- [Conversion workflow and QA](#conversion-workflow-and-qa)

## Do not conflate the journals

Nature, Nature Methods, and Nature Communications are separate journals. The referenced AJE Word template is specifically a **Nature Communications** template. Do not claim that its typography or section furniture is an official Nature or Nature Methods template.

Nature and Nature Methods both allow flexible formatting at initial submission. At the user's direction, the formatter applies the **Nature visual format to both Nature and Nature Methods**. This means the same typography, spacing, page geometry, line numbering, page numbering, heading treatment, legends, and table formatting. Keep their compliance audits separate: Nature Methods still uses its own article-type, structure, abstract, word-count, display-item, and submission-stage rules. Report that the visual treatment is a review convention rather than a mandatory Nature Methods initial-submission template.

## Optional Nature Communications template

- Official source: `https://authorservices.springernature.com/wp-content/uploads/2025/01/AJE-Nature-Communications-Submission-Template_changed_Dec2025.docx`
- SHA-256: `4618c48d7781d2a51d519e4a3c1e37a0b1ba2052a0fb3fa4ac2bd2832b6a101b`
- Inspected: 2026-08-25

The third-party DOCX is not redistributed in this public repository. The formatter works without it by using deterministic layout tokens derived from the inspected template. If exact page geometry from the source file is required, download an authorized copy from the official source, verify its checksum, and pass its local path with `--template`.

The template uses US Letter portrait pages, one-inch margins, continuous line numbers, right-aligned footer page numbers, Times New Roman text, and double spacing for most manuscript content. Its model hierarchy uses a 16-point bold title, 14-point bold top-level section headings, 14-point subheadings, 11-point figure/table legends and table text, and explicit section rules under major headings.

The template states an Article main-text limit of 6,000 words, up to 10 display items, a title of no more than 15 words, an unreferenced abstract of no more than 150 words, Results and Methods subheadings, and no Discussion subheadings. Treat these as template-derived requirements and verify the live journal page before an actual submission if current access is available.

## Reusable formatter

Run with the primary runtime Python:

```bash
python scripts/format_manuscript.py input.docx \
  --journal nature-communications \
  --output output.docx \
  --report output.audit.json
```

Other supported profiles:

```bash
python scripts/format_manuscript.py input.docx \
  --journal nature \
  --article-type article \
  --stage initial \
  --output output.docx \
  --report output.audit.json

python scripts/format_manuscript.py input.docx \
  --journal nature-methods \
  --article-type article \
  --stage initial \
  --output output.docx \
  --report output.audit.json
```

For Nature Methods, `article`, `resource`, `analysis`, and `brief-communication` are supported. Every Nature Methods article type uses the Nature visual format while retaining its Nature Methods audit profile. The JSON report records `"visual_format": "nature"` so this mapping is explicit. Use `--audit-only` when the user asks only for a format report. The script refuses to overwrite the input.

The formatter preserves document content, equations, images, tables, hyperlinks, citations, and existing OOXML parts to the extent supported by `python-docx`. It applies page geometry, typography, line numbering, page numbering, semantic paragraph styles, table formatting, and an audit. It does not rewrite prose, invent missing content, update reference-manager databases, or silently reorder top-level sections.

## Nature Article rules

The current official Nature formatting guide says:

- Manuscripts should be double-spaced, include line numbers, and preferably use 12-point Times New Roman.
- The order is title, authors, affiliations, bold first/summary paragraph, main text, main references, tables, figure legends, Methods, Methods references, end notes and availability/declaration material, then Extended Data legends.
- The title should normally fit within 75 characters including spaces.
- The fully referenced summary paragraph is ideally no more than 200 words and is aimed at readers outside the discipline.
- A typical six-page Article has about 2,500 words and four modest display items; a typical eight-page Article has about 4,300 words and five to six modest display items.
- Articles typically have no more than 50 main-text references.
- Methods are normally no more than 3,000 words, use short bold subheadings, and cannot contain figures or tables.
- Figure legends should be under 300 words each.

Nature is flexible about initial-submission formatting. Do not represent the script's named Word styles as required Nature house style. Official sources, checked 2026-08-25:

- `https://www.nature.com/nature/for-authors/formatting-guide`
- `https://www.nature.com/nature/for-authors/initial-submission`

## Nature Methods rules

Nature Methods explicitly says that initial submissions do not require special formatting, provided they are suitable for editorial assessment and peer review. More detailed formatting applies after acceptance in principle. For this skill, nevertheless apply the Nature visual format because the user has selected it as the shared house format; do not replace the Nature Methods compliance rules with Nature rules.

For an Article, the current content-type guidance specifies:

- An unreferenced abstract of up to 150 words.
- Main text of 3,000 words, with up to 5,000 at editorial discretion, excluding abstract, Methods, references and figure legends.
- Up to six figures and/or tables.
- Introduction without a visible heading, followed by Results, Discussion and Online Methods.
- Topical subheadings in Results and Methods; no Discussion subheadings.
- Typically up to 50 references.

Brief Communications instead use an abstract of up to 70 words, 1,200 words total with up to 1,600 at editorial discretion, no main-text sections or subheadings, no more than two display items unless editorial discretion allows three, a subheaded Online Methods section, and typically up to 20 references.

At AIP, Word or TeX/LaTeX is accepted, tables belong at the end of the text document, figures are cited in sequence, Methods use short bold subheadings, references are numbered sequentially, and acknowledgements and funding are separate sections. Official sources, checked 2026-08-25:

- `https://www.nature.com/nmeth/submission-guidelines/initial-formatting`
- `https://www.nature.com/nmeth/content`
- `https://www.nature.com/nmeth/submission-guidelines/preparing-your-submission`
- `https://www.nature.com/nmeth/submission-guidelines/aip-and-formatting`

## Conversion workflow and QA

1. Preserve the original DOCX and choose a new output path.
2. Confirm the target journal, article type, and submission stage.
3. Run `scripts/format_manuscript.py` and inspect the JSON audit.
4. Resolve semantic ambiguities manually when the script cannot reliably identify title, front matter, headings, captions, or reference boundaries.
5. Use the route selected in `SKILL.md` to determine review and visual-QA scope. This task-specific routing replaces a generic requirement to inspect every page solely because a final DOCX or Google Doc will be delivered.
6. For a lightweight local edit or formatting-only route, inspect the edited location, its rendered page when available, directly affected adjacent pages, and nearby layout details. Do not inspect unaffected pages unless an escalation trigger in `SKILL.md` applies. Routine document-wide style application by the formatter is not itself an escalation trigger.
7. For the full-manuscript or structural route, render the DOCX to page PNGs and inspect every page for clipping, overlap, table reflow, missing glyphs, displaced figures, broken equations, and unexpected page breaks before delivering a revised artifact.
8. Correct defects and repeat the same localized or full-document scope as needed.
9. Deliver one formatted artifact and report findings at the selected route's scope.

Do not describe the output as submission-ready solely because the script completed. A lightweight or formatting-only task passes its localized review and JSON audit but does not establish whole-manuscript readiness. Only the full route can produce a Baker-ready or submission-ready determination after the complete checklist and applicable full-document visual QA pass.
