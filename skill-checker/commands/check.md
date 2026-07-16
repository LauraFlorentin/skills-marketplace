---
description: Validate and review a Claude Code skill for structural errors, triggering, progressive disclosure, portability, safety, and testability
---

# /skill-checker:check

Validate, review, and score a Claude skill.

## Usage

```
/skill-checker:check [path-to-skill-folder]
```

## What it does

1. **Structural validation** — file naming, folder layout, YAML correctness
2. **Content quality audit** — triggering, instruction clarity, progressive disclosure, portability, and safety
3. **Evidence-backed recommendations** — blocking errors, warnings, and prioritized fixes

## Quick-check mode

For a fast pass, say "quick check my skill" — runs only YAML validation, description quality, and top 3 issues.

## Automated validator

```bash
python "${CLAUDE_PLUGIN_ROOT}/skills/skill-checker/scripts/validate_skill.py" <path-to-skill-folder>
python "${CLAUDE_PLUGIN_ROOT}/skills/skill-checker/scripts/validate_skill.py" <path-to-skill-folder> --json
python "${CLAUDE_PLUGIN_ROOT}/skills/skill-checker/scripts/validate_skill.py" <path-to-skill-folder> --check-scripts
```
