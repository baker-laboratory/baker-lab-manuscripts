# Baker Lab Manuscript Skill Development

This document records the local validation workflow for the
`baker-lab-manuscript` skill.

## Modify the skill

Edit the canonical skill directory inside the `remote-skills` repository. Keep
changes scoped to this skill and do not stage sibling-skill work.

## Install the skill

Install or update the skill through the repository workflow used by the target
Codex environment. Do not copy development-only test outputs into the skill
package.

## Test the skill

Run the skill validator and formatter regression tests with the primary runtime:

```bash
PYTHONDONTWRITEBYTECODE=1 "$CODEX_PRIMARY_RUNTIME_PYTHON" \
  /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
PYTHONDONTWRITEBYTECODE=1 "$CODEX_PRIMARY_RUNTIME_PYTHON" \
  -m unittest discover -s tests -v
```

For formatter performance work, compare representative paragraph counts before
and after the change. Keep generated DOCX files in a temporary directory rather
than the repository.
