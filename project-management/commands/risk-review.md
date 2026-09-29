---
description: Review and update the project risk register
argument-hint: "<project name>"
---

# Risk Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Review and update the risk register — re-score existing risks, identify new ones, and close resolved risks.

## Usage

```
/risk-review <project name>
```

### Arguments

- `project name` — The project to review risks for

## Workflow

### 1. Gather Current State

Ask about: current project status, recent issues, upcoming concerns. Check ~~docs for the existing risk register.

### 2. Review Risks

Use the **Monitoring** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/monitoring/SKILL.md` and:
- Re-score existing risks based on current information
- Identify new risks
- Close risks that have been resolved or are no longer relevant
- Check if any risk triggers have fired

### 3. Output

Deliver the updated risk register with changes highlighted. Flag any risks that have escalated to issues.
