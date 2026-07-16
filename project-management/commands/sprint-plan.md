---
description: Plan a sprint or iteration with scope, capacity, and commitments
argument-hint: "<team or project> [sprint-number]"
---

# Sprint Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Plan a sprint or iteration — calculate capacity, select scope, set a sprint goal, and define commitments.

## Usage

```
/sprint-plan <team or project> [sprint-number]
```

### Arguments

- `team or project` — The team or project to plan the sprint for
- `sprint-number` — (Optional) The sprint number or iteration name

## Workflow

### 1. Gather Inputs

Ask about: team members and availability, sprint length, backlog priorities, carry-over items, dependencies. Check ~~project-tracker for backlog and velocity data.

### 2. Plan Sprint

Use the **Execution** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/execution/SKILL.md` and:
- Calculate team capacity
- Select stories/tasks from backlog
- Set sprint goal
- Identify risks and dependencies for this sprint

### 3. Output

Deliver the sprint plan: goal, committed items with estimates, capacity breakdown, risks. Offer to update ~~project-tracker with sprint assignments.
