# Real Estate Investment Analyzer

Adaptive multi-agent system for real estate investment analysis — deal screening, underwriting, pro forma, financing, tax strategy, stress testing, and more.

> **Important**: This plugin assists with investment analysis but does not provide financial, legal, or tax advice. All outputs should be reviewed by qualified professionals before making investment decisions.

## How It Works

An **orchestrator agent** classifies each deal by property type, strategy, geography, and complexity, then deploys the right combination of specialist agents. Describe your deal and the system handles the routing.

See the [orchestrator](./agents/orchestrator.md) for classification logic and routing rules.

## Skills

| Skill | Description |
| :--- | :--- |
| [Real Estate Analyzer](./skills/real-estate-analyzer/SKILL.md) | Entry point for the multi-agent analysis system. Covers domestic and international deals, direct ownership and syndications, all property types including hospitality. |

## Commands

11 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Agents

1 orchestrator + 10 specialist agents — see [`agents/README.md`](./agents/README.md) for the full registry.

| Agent | Role |
| :--- | :--- |
| Orchestrator | Classifies deals and routes to the right specialists |
| A2 Deal Screener | Quick pass/fail on rules of thumb |
| A3 Property Underwriter | Full financial analysis |
| A4 Pro Forma Builder | Multi-year projections |
| A5 Financing Analyzer | Loan comparison and leverage |
| A6 Tax Strategist | Depreciation, 1031, cost segregation |
| A7 Stress Tester | Scenario analysis and resilience |
| A8 Syndication Analyzer | SPV/fund structure and fee analysis |
| A9 Int'l Risk Assessor | Cross-border and jurisdiction risk |
| A10 Hospitality Underwriter | Hotel/resort specific metrics |
| A11 Legal Reviewer | Document red flags |

## Hooks

None.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **real-estate-investment**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/real-estate-investment
```
