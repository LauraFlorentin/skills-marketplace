---
description: Run a full audit on a skill folder or SKILL.md against Anthropic's official best practices
---

# /skill-checker:check

Validate, review, and score a Claude skill.

## Usage

```
/skill-checker:check [path-to-skill-folder]
```

## What it does

1. **Structural validation** — file naming, folder layout, YAML correctness
2. **Content quality audit** — description effectiveness, instruction clarity, progressive disclosure, patterns used
3. **Scorecard & recommendations** — graded rubric across 7 dimensions with prioritized fixes

## Quick-check mode

For a fast pass, say "quick check my skill" — runs only YAML validation, description quality, and top 3 issues.

## Automated validator

```bash
python scripts/validate_skill.py <path-to-skill-folder>
python scripts/validate_skill.py <path-to-skill-folder> --json
python scripts/validate_skill.py <path-to-skill-folder> --fix
```
