---
description: Map and track cross-team or cross-project dependencies
argument-hint: "<project name>"
---

# Dependency Tracker

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map and track dependencies between teams, projects, or external parties.

## Usage

```
/dependency-tracker <project name>
```

### Arguments

- `project name` — The project to track dependencies for

## Workflow

### 1. Gather Dependencies

Ask about: what does this project depend on from others? What do others depend on from this project? Check ~~project-tracker for linked issues and blocking items.

### 2. Map & Assess

Use the **Monitoring** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/monitoring/SKILL.md` and create:
- Dependency map with status for each dependency
- Critical path impact for blocked dependencies
- Escalation recommendations for at-risk dependencies

### 3. Output

Deliver the dependency map and status report. Flag any blocked or at-risk dependencies with recommended actions.
