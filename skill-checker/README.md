# Skill Checker Plugin

> Validate, review, and improve Claude skills against Anthropic's official best practices from "The Complete Guide to Building Skills for Claude."

---

## Install

```bash
npx skills add LauraFlorentin/skills-marketplace/skill-checker
```

---

## Commands

| Command | Description |
| :--- | :--- |
| `/skill-checker:check` | Run a full audit on a skill folder or SKILL.md |

---

## What It Does

The review runs in three phases:

1. **Structural validation** — file naming, folder layout, YAML correctness
2. **Content quality audit** — description effectiveness, instruction clarity, progressive disclosure, patterns used
3. **Scorecard & recommendations** — graded rubric across 7 dimensions with prioritized fixes

### Scoring Dimensions

| Dimension | What It Checks |
|---|---|
| Structure | File/folder naming, YAML validity, conventions |
| Description | Trigger phrases, WHAT + WHEN, scope clarity |
| Progressive Disclosure | 3-level loading, SKILL.md line count, reference usage |
| Instruction Clarity | Imperative form, examples, explains WHY |
| Error Handling | Troubleshooting, rollback, common issues |
| Composability | Works alongside other skills, no conflicts |
| Testing Readiness | Clear success criteria, verifiable outputs |

### Automated Validator

```bash
python scripts/validate_skill.py <path-to-skill-folder>
python scripts/validate_skill.py <path-to-skill-folder> --json    # Machine-readable
python scripts/validate_skill.py <path-to-skill-folder> --fix     # With fix suggestions
```

---

## Skills

| Skill | Description |
| :--- | :--- |
| `skill-checker` | Multi-dimensional audit and scorecard for any Claude skill |

---

## References

- `references/quick-reference.md` — Condensed rules from Anthropic's official guide
