# Skill Review Quick Reference

## Structure

```text
skill-name/
├── SKILL.md
├── scripts/       optional deterministic helpers
├── references/    optional on-demand guidance
└── assets/        optional reusable inputs
```

- `SKILL.md` uses exact case.
- Frontmatter begins on line 1 and has `name` and `description`.
- Use a lowercase kebab-case name matching the folder.
- Keep the description within the platform limit and make it identify both capability and trigger context.

## Progressive disclosure

- Description: enough information to decide whether to load the skill.
- Body: core workflow, constraints, routing, and output contract.
- Resources: variants, long examples, schemas, scripts, and templates loaded only when needed.

Keep the body under roughly 500 lines when practical. Length is a maintainability warning, not a substitute for content review.

## Quality questions

1. Does the description distinguish this skill from nearby skills?
2. Are critical safety and permission boundaries near the top?
3. Can the model identify inputs, steps, outputs, and stopping conditions?
4. Are paths portable and references valid?
5. Are volatile facts looked up at execution time?
6. Does the workflow require only tools that exist in the target runtime?
7. Are scripts deterministic and safe with user data and credentials?
8. Is success verified proportionately to risk?

## Trigger tests

- obvious positive;
- two paraphrased positives;
- adjacent negative;
- competing-skill case.

## Severity

- **Error:** violates the runtime contract or prevents loading or execution.
- **Warning:** likely trigger, portability, safety, or maintainability problem.
- **Suggestion:** optional editorial improvement.

Confirm current platform-specific rules in official documentation before calling a heuristic an error.
