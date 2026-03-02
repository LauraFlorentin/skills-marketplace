---
description: Analyze sprint or project burndown and forecast completion
argument-hint: "<project or sprint> [sprint|release|project]"
---

# Burndown

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Analyze burndown data and forecast completion for a sprint, release, or project.

## Usage

```
/burndown <project or sprint> [sprint|release|project]
```

### Arguments

- `project or sprint` — The sprint, release, or project to analyze
- `sprint|release|project` — (Optional) Burndown scope:
  - `sprint` — Sprint burndown: story points remaining vs. ideal line
  - `release` — Release burndown: features remaining across sprints
  - `project` — Project burndown: milestones or earned value over time
  - If not specified, ask about the scope

## Workflow

### 1. Gather Data

Ask about: remaining work, completed work, time elapsed, team velocity. Check ~~project-tracker for burndown data.

### 2. Analyze & Forecast

Use the **Monitoring** skill. Read `../skills/monitoring/SKILL.md` and:
- Analyze current burndown shape
- Forecast completion date
- Identify warning signs

### 3. Output

Deliver the burndown analysis with forecast and recommendations. Flag if the current trajectory won't meet the target date.
