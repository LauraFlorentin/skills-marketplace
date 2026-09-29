---
description: Plan team allocation, roles, and capacity
argument-hint: "<project name>"
---

# Resource Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Plan team allocation, roles, capacity, and identify resource risks.

## Usage

```
/resource-plan <project name>
```

### Arguments

- `project name` — The project to plan resources for

## Workflow

### 1. Gather Context

Ask about: team members available, their roles and skills, allocation percentage, project duration, known constraints (leave, other projects). Check ~~time-tracker for current utilization.

### 2. Build Plan

Use the **Planning** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/planning/SKILL.md` and create:
- Resource allocation matrix (person × week)
- Skills gap analysis
- Capacity calculation

### 3. Output

Deliver the resource plan with allocation matrix, capacity summary, and risk flags (over-allocation, single points of failure, skills gaps).
