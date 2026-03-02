---
description: Build a project schedule with milestones and dependencies
argument-hint: "<project name> [sprint-based|timeline]"
---

# Schedule

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Build a project schedule with milestones, dependencies, and time estimates.

## Usage

```
/schedule <project name> [sprint-based|timeline]
```

### Arguments

- `project name` — The project to schedule
- `sprint-based|timeline` — (Optional) Schedule style:
  - `sprint-based` — Agile: sprint cadence, velocity estimation, release mapping
  - `timeline` — Traditional: Gantt-style milestones, critical path, PERT estimates
  - If not specified, ask about the team's methodology

## Workflow

### 1. Gather Inputs

Ask about: WBS or scope, team size, target dates, known dependencies, constraints. Check ~~project-tracker for existing work items and ~~calendar for key dates.

### 2. Build Schedule

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create the schedule.

### 3. Output

Deliver the schedule with milestones, dependencies, and critical path (or sprint plan). Flag any scheduling risks. Offer to sync with ~~project-tracker if connected.
