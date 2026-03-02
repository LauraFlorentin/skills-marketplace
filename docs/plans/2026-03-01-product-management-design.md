# Product Management Plugin — Design Document

**Date**: 2026-03-01
**Status**: Approved
**Plugin**: `product-management`

---

## Overview

A comprehensive product management plugin for the AI Skills Marketplace, organized around the product lifecycle: Strategy, Discovery, Planning, Launch & Growth, and Analytics. Covers both startup and enterprise PM workflows with clear separation within each skill.

This is the first of two plugins (the second being project-management, designed separately).

## Architecture

**Hybrid**: Skills + commands for most workflows, with an orchestrator agent for complex cross-cutting tasks.

- **5 skills** organized by lifecycle stage
- **19 commands** as user entry points
- **1 orchestrator agent** for multi-stage workflows
- **MCP connectors** with placeholder syntax + pre-configured servers

## Plugin Structure

```
product-management/
├── .claude-plugin/
│   └── plugin.json
├── agents/
│   ├── orchestrator.md
│   └── README.md
├── commands/
│   ├── vision.md
│   ├── okrs.md
│   ├── competitive-analysis.md
│   ├── user-research.md
│   ├── persona.md
│   ├── jtbd.md
│   ├── opportunity-score.md
│   ├── roadmap.md
│   ├── prd.md
│   ├── feature-spec.md
│   ├── prioritize.md
│   ├── backlog-groom.md
│   ├── sprint-review.md
│   ├── gtm-plan.md
│   ├── launch-checklist.md
│   ├── ab-test.md
│   ├── metrics-dashboard.md
│   ├── growth-experiment.md
│   ├── product-review.md
│   └── README.md
├── skills/
│   ├── strategy/
│   │   └── SKILL.md
│   ├── discovery/
│   │   └── SKILL.md
│   ├── planning/
│   │   └── SKILL.md
│   ├── launch-growth/
│   │   └── SKILL.md
│   └── product-analytics/
│       └── SKILL.md
├── CONNECTORS.md
├── .mcp.json
└── README.md
```

## Plugin Metadata

**`.claude-plugin/plugin.json`**:

```json
{
  "name": "product-management",
  "version": "1.0.0",
  "description": "Product management workflows from strategy to growth — vision docs, PRDs, roadmaps, user research, prioritization, GTM, analytics, and product reviews for startup and enterprise PMs.",
  "author": {
    "name": "Laura Florentine"
  },
  "repository": "https://github.com/LauraFlorentin/skills-marketplace",
  "license": "MIT",
  "skills": "./skills/",
  "commands": "./commands/",
  "keywords": ["product", "pm", "roadmap", "prd", "discovery", "okr", "prioritization", "gtm", "analytics", "user-research"]
}
```

---

## Skills

### Skill 1: Strategy (`skills/strategy/SKILL.md`)

Covers product vision, strategic positioning, and goal-setting.

| Aspect | Startup PM | Enterprise PM |
|--------|-----------|---------------|
| Vision | Lean canvas, elevator pitch | Full vision doc with stakeholder alignment |
| OKRs | Team-level, quarterly | Multi-team, cascading OKRs with dependencies |
| Competitive | Quick landscape scan | Full competitive matrix with feature parity analysis |

**Commands**:
- `/vision` — Generate a product vision document (lean or full)
- `/okrs` — Draft OKRs with measurable key results
- `/competitive-analysis` — Map competitive landscape and positioning

### Skill 2: Discovery (`skills/discovery/SKILL.md`)

Covers user research, persona development, and opportunity identification.

| Aspect | Startup PM | Enterprise PM |
|--------|-----------|---------------|
| Research | Guerrilla interviews, surveys | Formal research plans with recruiting criteria |
| Personas | Lightweight proto-personas | Data-backed personas with segmentation |
| JTBD | Quick job stories | Full jobs-to-be-done framework with outcome mapping |

**Commands**:
- `/user-research` — Design a user research plan with interview guides
- `/persona` — Create user personas from research data
- `/jtbd` — Map jobs-to-be-done and desired outcomes
- `/opportunity-score` — Score opportunities using Opportunity Solution Trees or similar frameworks

### Skill 3: Planning (`skills/planning/SKILL.md`)

Covers roadmapping, requirements, prioritization, and backlog management.

| Aspect | Startup PM | Enterprise PM |
|--------|-----------|---------------|
| Roadmap | Now/Next/Later, theme-based | Timeline roadmap with dependencies and milestones |
| PRD | 1-pager, lean spec | Full PRD with acceptance criteria, edge cases, technical considerations |
| Prioritization | ICE, gut + data | RICE, weighted scoring, stakeholder input matrix |

**Commands**:
- `/roadmap` — Build a product roadmap (lean or detailed)
- `/prd` — Write a product requirements document
- `/feature-spec` — Write a detailed feature specification
- `/prioritize` — Run a prioritization exercise (RICE, ICE, MoSCoW, weighted scoring)
- `/backlog-groom` — Structure and refine a product backlog

### Skill 4: Launch & Growth (`skills/launch-growth/SKILL.md`)

Covers go-to-market, launches, experimentation, and growth loops.

| Aspect | Startup PM | Enterprise PM |
|--------|-----------|---------------|
| GTM | Lean launch, Product Hunt, early adopters | Cross-functional GTM with sales enablement, marketing, CS |
| Launch | Simple checklist | Phased rollout with feature flags, rollback plan |
| Experiments | Quick A/B tests, fake door tests | Structured experimentation with statistical rigor |

**Commands**:
- `/gtm-plan` — Create a go-to-market plan
- `/launch-checklist` — Generate a launch readiness checklist
- `/ab-test` — Design an A/B test with hypothesis, variants, and success metrics
- `/growth-experiment` — Design a growth experiment (acquisition, activation, retention loops)

### Skill 5: Product Analytics (`skills/product-analytics/SKILL.md`)

Covers metrics frameworks, dashboards, and product reviews.

| Aspect | Startup PM | Enterprise PM |
|--------|-----------|---------------|
| Metrics | North star + 3-5 key metrics | Metrics hierarchy with leading/lagging indicators per team |
| Dashboard | Single-page scorecard | Multi-level dashboards (exec, team, feature) |
| Reviews | Weekly standup format | Quarterly business review with deep dives |

**Commands**:
- `/metrics-dashboard` — Define a metrics framework and dashboard spec
- `/sprint-review` — Generate a sprint/iteration review summary
- `/product-review` — Run a comprehensive product review (cross-cutting, triggers orchestrator)

---

## Orchestrator Agent

**Location**: `agents/orchestrator.md`

**Activation**: Triggered by `/product-review` or multi-stage requests that span lifecycle stages.

### Forward Routing

```
INPUT CLASSIFICATION:
├── "Product review" or "quarterly review"
│   → Strategy (vision check) → Analytics (metrics pull) → Planning (roadmap assessment) → Report
│
├── "New product/feature from scratch"
│   → Strategy (vision) → Discovery (research + personas) → Planning (PRD + roadmap) → Launch (GTM)
│
├── "Pivot assessment"
│   → Analytics (current metrics) → Discovery (new research) → Strategy (repositioning) → Planning (new roadmap)
│
├── "Launch readiness review"
│   → Planning (spec completeness) → Analytics (baseline metrics) → Launch (checklist + GTM)
│
└── Single-stage request
    → Route directly to the appropriate skill (no orchestration needed)
```

### Bidirectional Re-entry Routing

The orchestrator supports looping back to earlier stages when downstream work reveals gaps:

```
RE-ENTRY PATHS:
├── Build blocker → Discovery (need more user signal)
├── Build blocker → Planning (spec gaps or scope change)
├── Launch metrics miss → Discovery (wrong assumptions)
├── Launch metrics miss → Strategy (positioning problem)
├── Growth stall → Discovery (new research) → Strategy (pivot assessment)
└── Any stage → Previous stage (explicit user request)
```

The orchestrator tracks which stage triggered re-entry and why, carrying that context forward so work doesn't get repeated.

### Conflict Escalation

When the orchestrator detects divergence between strategic intent (roadmap, vision, OKRs) and execution reality (sprint scope, velocity, blockers), it:

- Surfaces the tension explicitly in its output with an **"Alignment Flag"** section
- Describes the gap: what was planned vs. what's happening
- Does **not** silently resolve it — flags it for human decision
- Suggests 2-3 resolution options but makes no choice

### Behavior

- Classifies the request by complexity and scope
- For single-stage requests, routes directly without overhead
- For multi-stage workflows, sequences skills and passes context between them
- Produces a unified output document at the end

---

## MCP Connectors

### Placeholder Syntax (`CONNECTORS.md`)

Commands use `~~placeholder` syntax so they work without any tool configuration:

| Placeholder | Category | Example Tools |
|-------------|----------|---------------|
| `~~roadmap-tool` | Roadmap & planning | Productboard, Aha!, Linear, Notion |
| `~~analytics` | Product analytics | Amplitude, Mixpanel, PostHog, Heap |
| `~~project-tracker` | Tickets & sprints | Jira, Linear, Shortcut, Asana |
| `~~docs` | Documentation | Notion, Confluence, Google Docs |
| `~~research-repo` | Research repository | Dovetail, EnjoyHQ, Notion |
| `~~messaging` | Team communication | Slack, Teams |
| `~~design` | Design files | Figma |

**Note**: `~~research-repo` and `~~docs` can point to the same tool (e.g., Notion). Users should configure the tool once and reference it in both placeholders — no duplicate configuration needed.

### Pre-configured MCP Servers (`.mcp.json`)

```json
{
  "mcpServers": {
    "linear": {
      "type": "npm",
      "package": "@anthropic/linear-mcp",
      "description": "Project tracking, sprint management, backlog"
    },
    "notion": {
      "type": "npm",
      "package": "@anthropic/notion-mcp",
      "description": "Docs, roadmaps, research repos, wikis"
    },
    "posthog": {
      "type": "npm",
      "package": "@anthropic/posthog-mcp",
      "description": "Product analytics, event tracking, feature flags, A/B tests"
    },
    "slack": {
      "type": "npm",
      "package": "@anthropic/slack-mcp",
      "description": "Team messaging, stakeholder updates"
    },
    "figma": {
      "type": "npm",
      "package": "@anthropic/figma-mcp",
      "description": "Design file references and specs"
    }
  }
}
```

Users opt in to whichever tools they use. Commands work without any connectors — they produce richer output when tools are available.

---

## Summary

| Component | Count |
|-----------|-------|
| Skills | 5 (strategy, discovery, planning, launch-growth, product-analytics) |
| Commands | 19 |
| Agents | 1 (orchestrator) |
| MCP Servers | 5 (Linear, Notion, PostHog, Slack, Figma) |
| Connector Placeholders | 7 |
