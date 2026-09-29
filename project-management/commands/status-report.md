---
description: Generate a project status report in RAG format
argument-hint: "<project name> [executive|team|steering]"
---

# Status Report

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a project status report with RAG (Red/Amber/Green) indicators across key dimensions.

## Usage

```
/status-report <project name> [executive|team|steering]
```

### Arguments

- `project name` — The project to report on
- `executive|team|steering` — (Optional) Audience level:
  - `executive` — 3-bullet summary with RAG, key risks, decisions needed
  - `team` — Full detail: progress, metrics, blockers, upcoming work
  - `steering` — Steering committee format: RAG dashboard, decisions required, budget status
  - If not specified, ask about the audience

## Workflow

### 1. Gather Data

Ask about: what happened this period, blockers, upcoming milestones. Check ~~project-tracker for progress data and ~~docs for previous status reports.

### 2. Compile Report

Use the **Monitoring** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/monitoring/SKILL.md` and generate the status report.

### 3. Output

Deliver the status report formatted for the target audience. Offer to post to ~~messaging or save to ~~docs if connected.
