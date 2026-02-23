# Real Estate Investment Analyzer

Adaptive multi-agent system for real estate investment analysis — deal screening, underwriting, pro forma, financing, tax strategy, stress testing, and more.

## How It Works

An **orchestrator agent** classifies each deal by property type, strategy, geography, and complexity, then deploys the right combination of specialist agents. Describe your deal and the system handles the routing.

See the [orchestrator](./agents/orchestrator.md) for classification logic and routing rules.

## Skills

| Skill | Description |
| :--- | :--- |
| [Real Estate Analyzer](./skills/real-estate-analyzer/SKILL.md) | Entry point for the multi-agent analysis system. Covers domestic and international deals, direct ownership and syndications, all property types including hospitality. |

## Agents

12 specialist agents — see [`agents/README.md`](./agents/README.md) for the full registry.

## Commands

11 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **real-estate-investment**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/real-estate-investment
```
