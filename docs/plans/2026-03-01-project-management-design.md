# Project Management Plugin — Design Document

**Date**: 2026-03-01
**Status**: Approved
**Plugin**: `project-management`

---

## Overview

A comprehensive project management plugin for the AI Skills Marketplace, organized around the project lifecycle: Initiation, Planning, Execution, Monitoring, and Closing. Covers both software/tech PM and general PM workflows with a mode switch within each skill.

This is the second of two plugins (the first being product-management, already implemented).

## Architecture

**Hybrid**: Skills + commands for most workflows, with an orchestrator agent for complex cross-cutting tasks.

- **5 skills** organized by lifecycle stage
- **20 commands** as user entry points
- **1 orchestrator agent** for multi-stage workflows
- **MCP connectors** with placeholder syntax + pre-configured servers

## Plugin Structure

```
project-management/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── orchestrator.md
│   └── README.md
├── commands/
│   ├── project-charter.md
│   ├── stakeholder-map.md
│   ├── kickoff.md
│   ├── wbs.md
│   ├── schedule.md
│   ├── resource-plan.md
│   ├── risk-register.md
│   ├── communication-plan.md
│   ├── standup.md
│   ├── sprint-plan.md
│   ├── decision-log.md
│   ├── change-request.md
│   ├── status-report.md
│   ├── burndown.md
│   ├── risk-review.md
│   ├── dependency-tracker.md
│   ├── health-check.md
│   ├── retro.md
│   ├── lessons-learned.md
│   ├── project-closeout.md
│   └── README.md
├── skills/
│   ├── initiation/SKILL.md
│   ├── planning/SKILL.md
│   ├── execution/SKILL.md
│   ├── monitoring/SKILL.md
│   └── closing/SKILL.md
├── .mcp.json
├── CONNECTORS.md
└── README.md
```

## Mode Switch: Software vs. General PM

Every skill supports both modes. Commands accept an optional `[software|general]` hint. When no mode is specified, the command asks about the project context and recommends the appropriate approach.

- **Software/Tech PM**: Agile/Scrum/Kanban workflows, sprint planning, CI/CD awareness, velocity-based estimation, deployment planning, engineering-team-focused delivery
- **General PM**: Cross-industry PM — construction, marketing, consulting, ops. Waterfall, hybrid, Agile. PMP/PRINCE2 frameworks, Gantt charts, critical path, earned value management

## Skills

### Skill 1: Initiation (3 commands)

| Command | Description |
|---------|-------------|
| `/project-charter` | Define project scope, objectives, stakeholders, and success criteria |
| `/stakeholder-map` | Map stakeholders by influence/interest, define communication needs |
| `/kickoff` | Generate a kickoff meeting agenda and deck outline |

**Software mode**: Technical feasibility, architecture dependencies, team capacity, tech stack decisions
**General mode**: Business case, sponsor alignment, governance structure, procurement needs

### Skill 2: Planning (5 commands)

| Command | Description |
|---------|-------------|
| `/wbs` | Create a work breakdown structure |
| `/schedule` | Build a project schedule with milestones and dependencies |
| `/resource-plan` | Plan team allocation, roles, and capacity |
| `/risk-register` | Create a risk register with mitigation strategies |
| `/communication-plan` | Define stakeholder communication cadence and channels |

**Software mode**: Sprint planning, story mapping, CI/CD milestones, velocity-based estimation, definition of done
**General mode**: Gantt charts, critical path method, resource leveling, PERT estimates, phase gates

### Skill 3: Execution (4 commands)

| Command | Description |
|---------|-------------|
| `/standup` | Generate daily standup summaries or async standup templates |
| `/sprint-plan` | Plan a sprint or iteration (scope, capacity, commitments) |
| `/decision-log` | Record and track project decisions with context and rationale |
| `/change-request` | Draft a formal change request with impact analysis |

**Software mode**: Sprint ceremonies, kanban flow, deployment planning, code review coordination
**General mode**: Work authorization, procurement management, vendor coordination, phase transitions

### Skill 4: Monitoring (5 commands)

| Command | Description |
|---------|-------------|
| `/status-report` | Generate a project status report (RAG format) |
| `/burndown` | Analyze sprint/project burndown and forecast completion |
| `/risk-review` | Review and update the risk register |
| `/dependency-tracker` | Map and track cross-team or cross-project dependencies |
| `/health-check` | Run a project health assessment across multiple dimensions |

**Software mode**: Velocity trends, cycle time, deployment frequency, incident rate, tech debt tracking
**General mode**: Earned value (EV/PV/AC), SPI/CPI, milestone slip analysis, budget variance

### Skill 5: Closing (3 commands)

| Command | Description |
|---------|-------------|
| `/retro` | Facilitate a retrospective (multiple formats) |
| `/lessons-learned` | Compile lessons learned into a structured document |
| `/project-closeout` | Generate a project closeout report with handoff checklist |

**Software mode**: Release notes, runbook handoff, tech debt register, on-call transition, monitoring setup
**General mode**: Formal acceptance, contract closure, benefits realization review, archive procedures

---

## Orchestrator Agent

**Location**: `agents/orchestrator.md`

**Activation**: Triggered by `/health-check`, stakeholder update requests, or multi-stage requests that span lifecycle stages.

**Execution model**: Single-pass synthesis. The orchestrator fires each skill in sequence, collects outputs, and synthesizes in one pass. It produces a snapshot, not a live loop. Re-entry is a separate invocation triggered by the user or a downstream finding.

### Forward Routing

```
INPUT CLASSIFICATION:
├── "Project health check" or "project assessment"
│   → Planning (scope/schedule check) → Execution (team velocity) → Monitoring (metrics pull) → Report
│
├── "Stakeholder update" or "status report request"
│   → Monitoring (current metrics + status) → Synthesis (formatted for audience)
│
├── "New project setup"
│   → Initiation (charter + stakeholders) → Planning (WBS + schedule + risks) → Execution (first sprint/phase)
│
├── "Project recovery"
│   → Monitoring (diagnose what's wrong) → Planning (re-plan/re-scope) → Execution (revised plan)
│
├── "Project closeout"
│   → Monitoring (final metrics) → Closing (retro + lessons + closeout report)
│
└── Single-stage request
    → Route directly to the appropriate skill (no orchestration needed)
```

### Bidirectional Re-entry Routing

**Backward re-entry** (downstream gaps trigger return to earlier stages):

```
RE-ENTRY PATHS (BACKWARD):
├── Schedule slip → Planning (re-scope or re-estimate)
├── Resource conflict → Planning (resource re-allocation)
├── Risk materialized → Planning (mitigation plan) or Execution (immediate response)
├── Scope creep detected → Initiation (charter review) or Planning (change request)
├── Stakeholder misalignment → Initiation (stakeholder re-mapping)
└── Any stage → Previous stage (explicit user request)
```

**Forward re-entry** (resolved issues trigger resumption of downstream stages):

```
RE-ENTRY PATHS (FORWARD):
├── Replanning complete → resume Execution at revised scope
├── Risk resolved → resume Execution with updated risk register
├── Charter amended → resume Planning with new constraints
├── Change request approved → resume Execution with updated scope
└── Resource conflict resolved → resume Execution with updated allocation
```

The orchestrator tracks which stage triggered re-entry and why, carrying that context forward so work doesn't get repeated.

### Conflict Escalation

When the orchestrator detects divergence between the project plan and execution reality, it surfaces the tension with an **Alignment Flag**.

**Severity thresholds** — not every variance triggers a flag:

| Severity | Threshold | Behavior |
|----------|-----------|----------|
| Low | < 10% schedule slip, 1 minor resource shift | Noted in report, no Alignment Flag |
| Medium | 10-25% slip, scope change without change request | Alignment Flag raised |
| High | > 25% slip, critical risk materialized, sponsor misalignment | Alignment Flag with "requires immediate decision" marker |

**Flag format**:
- Surfaces the tension explicitly
- Describes the gap: what was planned vs. what's happening
- Does **not** silently resolve it — flags it for human decision
- Suggests 2-3 resolution options but makes no choice

### Partial Data Protocol

If a downstream skill returns incomplete data or errors, the orchestrator:
1. Flags the gap explicitly
2. Proceeds with available data
3. Marks the affected section with a confidence level (High / Moderate / Low)
4. Surfaces a "Data Gap" callout in the synthesis

### Synthesis Template

```
PROJECT MANAGEMENT REPORT
═══════════════════════════════════════════════════════
Project:          [Name]
Assessment Type:  [Health Check / Stakeholder Update / Recovery / Closeout / New Setup]
Context:          [Software / General PM]
Skills Deployed:  [S1, S2, S3, etc.]
Date:             [Date]
Execution Model:  Single-pass snapshot

EXECUTIVE SUMMARY
  [2-3 sentences: headline finding, key risk, recommended action]

INITIATION ASSESSMENT (from S1)
  [Charter alignment, stakeholder status, governance health]

PLANNING STATUS (from S2)
  [Schedule status, resource allocation, risk register state, WBS completeness]

EXECUTION STATUS (from S3)
  [Sprint/phase progress, team velocity, blockers, decisions pending]

MONITORING METRICS (from S4)
  [RAG status, burndown trajectory, dependency health, key metrics]

CLOSING STATUS (from S5)
  [Retro findings, lessons captured, handoff readiness]

─── Include only sections for skills that were deployed ───

ALIGNMENT FLAGS (if any)
  [Severity, gap description, resolution options — see Conflict Escalation]

DATA GAPS (if any)
  [Which skills returned incomplete data, confidence impact, what's missing]

RECOMMENDATIONS
  1. [Top priority action with owner]
  2. [Second priority]
  3. [Third priority]

NEXT STEPS
  [Specific actions, who does what, when to review again]

ASSUMPTIONS & GAPS
  [All assumptions made, data gaps, limitations of analysis]
═══════════════════════════════════════════════════════
```

---

## MCP Connectors

### Placeholder Syntax (`CONNECTORS.md`)

Commands use `~~placeholder` syntax so they work without any tool configuration:

| Placeholder | Category | Example Tools |
|-------------|----------|---------------|
| `~~project-tracker` | Issue tracking & sprints | Jira, Linear, Asana, Monday, Shortcut |
| `~~docs` | Documentation & wikis | Notion, Confluence, Google Docs |
| `~~time-tracker` | Time tracking & capacity | Harvest, Toggl, Clockify |
| `~~messaging` | Team communication | Slack, Teams |
| `~~calendar` | Scheduling & availability | Google Calendar, Outlook |
| `~~ci-cd` | Build & deploy pipelines | GitHub Actions, Jenkins, CircleCI |
| `~~repo` | Source code & PRs | GitHub, GitLab, Bitbucket |

**Notes**:
- `~~ci-cd` and `~~repo` are software-mode-only connectors — general PM mode doesn't reference them
- `~~docs` can serve as a project wiki, meeting notes repo, and decision log — same tool, multiple uses
- Commands work without any connectors; they produce richer output when tools are available

### Pre-configured MCP Servers (`.mcp.json`)

```json
{
  "mcpServers": {
    "jira": {
      "type": "npm",
      "package": "@anthropic/jira-mcp",
      "description": "Issue tracking, sprint management, backlog, boards"
    },
    "linear": {
      "type": "npm",
      "package": "@anthropic/linear-mcp",
      "description": "Lightweight project tracking, cycles, triage"
    },
    "asana": {
      "type": "npm",
      "package": "@anthropic/asana-mcp",
      "description": "Task management, timelines, portfolios"
    },
    "notion": {
      "type": "npm",
      "package": "@anthropic/notion-mcp",
      "description": "Docs, wikis, meeting notes, knowledge base"
    },
    "slack": {
      "type": "npm",
      "package": "@anthropic/slack-mcp",
      "description": "Team messaging, standups, status updates"
    }
  }
}
```

Users opt in to whichever tools they use. Commands work without any connectors.

---

## Relationship to Product Management Plugin

The project-management plugin is **independent and self-contained**. Where topics overlap with product-management (e.g., sprint planning, backlog), each plugin covers the topic from its own lens:

- **Product-management**: The product lens — what to build and why, user value, product metrics
- **Project-management**: The delivery lens — how to deliver on time, within scope, with the right resources

No cross-plugin references. Users can install one or both.

---

## Summary

| Component | Count |
|-----------|-------|
| Skills | 5 (initiation, planning, execution, monitoring, closing) |
| Commands | 20 |
| Agents | 1 (orchestrator) |
| MCP Servers | 5 (Jira, Linear, Asana, Notion, Slack) |
| Connector Placeholders | 7 |
