# Skill Checker

Validate and review Claude Code skills for structural correctness, trigger quality, progressive disclosure, portability, safety, and testability.

## Command

Use `/skill-checker:check [path]` for a full review. The deterministic validator can also run directly:

```bash
python skills/skill-checker/scripts/validate_skill.py <skill-directory>
python skills/skill-checker/scripts/validate_skill.py <skill-directory> --json
python skills/skill-checker/scripts/validate_skill.py <skill-directory> --check-scripts
```

The validator reports contract errors separately from maintainability warnings. The review workflow adds trigger tests and editorial feedback; it does not treat every heuristic as a platform requirement.

## Installation

```bash
npx skills add LauraFlorentin/skills-marketplace/skill-checker
```
