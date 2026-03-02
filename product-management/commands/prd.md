---
description: Write a product requirements document
argument-hint: "<feature or project> [lean|full]"
---

# PRD

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Write a Product Requirements Document for a feature or project.

## Usage

```
/prd <feature or project> [lean|full]
```

### Arguments

- `feature or project` — The feature or project to write requirements for
- `lean|full` — (Optional) PRD depth:
  - `lean` — 1-page PRD: problem, solution, metrics, scope, risks
  - `full` — Complete PRD: user stories, acceptance criteria, edge cases, technical considerations, rollout plan
  - If not specified, ask about the feature complexity and team size

## Workflow

### 1. Gather Context

Ask the user about: the problem being solved, target user, desired outcome, constraints, and any existing research. Check ~~docs for prior PRDs or specs.

### 2. Write PRD

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and apply the appropriate PRD template.

### 3. Output

Deliver the PRD in markdown. Run through the PRD quality checklist. Offer to save to ~~docs if connected.
