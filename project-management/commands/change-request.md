---
description: Draft a formal change request with impact analysis
argument-hint: "<change description>"
---

# Change Request

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Draft a formal change request documenting the proposed change, justification, and impact on scope, schedule, and cost.

## Usage

```
/change-request <change description>
```

### Arguments

- `change description` — A brief description of the proposed change

## Workflow

### 1. Gather Context

Ask about: what's changing, why, who requested it, what's the urgency. Check ~~project-tracker for affected work items and ~~docs for the current project plan.

### 2. Analyze Impact

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and create:
- Change request with full description
- Impact analysis (scope, schedule, cost, risk)
- Recommendation (approve, defer, reject)

### 3. Output

Deliver the change request document. Flag if this change would affect the critical path or trigger a re-plan.
