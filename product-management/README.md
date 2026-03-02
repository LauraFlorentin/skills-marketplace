# Product Management

Product management workflows from strategy to growth — vision docs, PRDs, roadmaps, user research, prioritization, GTM, analytics, and product reviews for startup and enterprise PMs.

> **Important**: This plugin assists with product management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and users before making product decisions.

## Skills

| Skill | Description |
| :--- | :--- |
| [Strategy](./skills/strategy/SKILL.md) | Product vision, OKRs, and competitive analysis — lean canvas or full strategic docs |
| [Discovery](./skills/discovery/SKILL.md) | User research, personas, jobs-to-be-done, and opportunity scoring |
| [Planning](./skills/planning/SKILL.md) | Roadmaps, PRDs, feature specs, prioritization frameworks, and backlog grooming |
| [Launch & Growth](./skills/launch-growth/SKILL.md) | Go-to-market plans, launch checklists, A/B testing, and growth experiments |
| [Product Analytics](./skills/product-analytics/SKILL.md) | Metrics frameworks, dashboards, sprint reviews, and product reviews |

## Commands

19 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Agents

| Agent | Description |
| :--- | :--- |
| [Orchestrator](./agents/orchestrator.md) | Routes multi-stage requests across lifecycle skills, supports bidirectional re-entry and conflict escalation |

## Hooks

None.

## Startup vs. Enterprise

Every skill supports both modes. Commands accept an optional mode hint (e.g., `/prd my-feature lean` or `/prd my-feature full`). When no mode is specified, the command asks about your team context and recommends the appropriate depth.

## MCP Integration

Connect your product tools via MCP servers for the richest experience. See [CONNECTORS.md](./CONNECTORS.md) for details.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **product-management**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/product-management
```
