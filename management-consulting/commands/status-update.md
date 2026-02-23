---
description: Generate an engagement status update or steering committee report
argument-hint: "<client or engagement name>"
---

# Engagement Status Update

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a status update for a consulting engagement — either a weekly team update or a steering committee report.

## Usage

```
/status-update <engagement>
```

### Arguments

- `engagement` — Client or engagement name/identifier

## Workflow

### 1. Gather Status Information

If ~~project tracker or ~~documents is connected:
- Pull current task status, milestone progress, and open items
- Review RAID log for active risks, issues, and pending decisions

If no data source is connected:
> Provide: accomplishments this period, planned activities next period, risks/issues, decisions needed, and milestone status.

### 2. Generate Update

**Weekly Status Update:**
- Overall RAG status (Red/Amber/Green) with justification
- Key accomplishments this period
- Planned activities for next period
- Risks and issues requiring attention
- Decisions needed from client or leadership
- Milestone tracker (on track / at risk / behind)

**Steering Committee Report:**
- Executive summary of engagement progress
- Workstream-by-workstream status with RAG
- Key findings or deliverables completed
- Critical path items and dependencies
- Budget/timeline status vs. plan
- Decisions and approvals requested

### 3. Output

Provide the formatted status update ready for distribution, with any items flagged for escalation or follow-up.
