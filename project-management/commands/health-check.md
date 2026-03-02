---
description: Run a multi-dimensional project health assessment — triggers the orchestrator
argument-hint: "<project name>"
---

# Health Check

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a comprehensive project health check assessing schedule, scope, budget, team, risk, and stakeholder dimensions.

**This command triggers the orchestrator agent** for cross-stage assessment.

## Usage

```
/health-check <project name>
```

### Arguments

- `project name` — The project to assess

## Workflow

### 1. Activate Orchestrator

Read the orchestrator at `../agents/orchestrator.md`. This command triggers the "Project health check" routing path.

### 2. Cross-Stage Assessment

The orchestrator sequences:
1. **Planning check** — Scope/schedule alignment, WBS completeness
2. **Execution check** — Team velocity, sprint health, blockers
3. **Monitoring pull** — RAG status, burndown trajectory, risk state
4. **Synthesis** — Unified health report with alignment flags

### 3. Output

Deliver the health check report with scores per dimension. If any plan-vs-reality divergence is detected, include an **Alignment Flag** section with resolution options.
