# Project Management

Project management workflows from initiation to closing — charters, WBS, scheduling, risk registers, sprint planning, status reports, retrospectives, and project closeout for software and general PMs.

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

## Skills

| Skill | Description |
| :--- | :--- |
| [Initiation](./skills/initiation/SKILL.md) | Project charters, stakeholder mapping, and kickoff planning |
| [Planning](./skills/planning/SKILL.md) | WBS, scheduling, resource planning, risk management, and communication planning |
| [Execution](./skills/execution/SKILL.md) | Standups, sprint planning, decision tracking, and change management |
| [Monitoring](./skills/monitoring/SKILL.md) | Status reporting, burndown analysis, risk reviews, dependency tracking, and health checks |
| [Closing](./skills/closing/SKILL.md) | Retrospectives, lessons learned, and project closeout |

## Commands

20 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Agents

| Agent | Description |
| :--- | :--- |
| [Orchestrator](./agents/orchestrator.md) | Routes multi-stage requests across lifecycle skills, supports bidirectional re-entry and conflict escalation |

## Hooks

None.

## Software vs. General PM

Every skill supports both modes. Commands accept an optional mode hint (e.g., `/project-charter my-project software` or `/project-closeout my-project general`). When no mode is specified, the command asks about your project context and recommends the appropriate depth.

## MCP Integration

Connect your project tools via MCP servers for the richest experience. See [CONNECTORS.md](./CONNECTORS.md) for details.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **project-management**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/project-management
```
