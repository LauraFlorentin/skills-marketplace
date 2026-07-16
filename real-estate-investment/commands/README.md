# Real Estate Investment — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/real-estate-investment:command-name` you can invoke directly.

## Usage

In Claude Code, type `/real-estate-investment:` to see available commands from this plugin.

## Available Commands

### Full Analysis
| Command | Agent | Description |
|---------|-------|-------------|
| `/real-estate-investment:analyze-deal` | Orchestrator | Full multi-agent analysis — classifies deal and deploys the right agents |

### Individual Agents
| Command | Agent | Description |
|---------|-------|-------------|
| `/real-estate-investment:screen-deal` | A2 Deal Screener | Quick pass/fail on rules of thumb (1%, 50%, 70%) |
| `/real-estate-investment:underwrite` | A3 Property Underwriter | Full financial underwriting (NOI, CoC, DSCR) |
| `/real-estate-investment:pro-forma` | A4 Pro Forma Builder | Multi-year financial projections |
| `/real-estate-investment:compare-financing` | A5 Financing Analyzer | Compare loan options and leverage impact |
| `/real-estate-investment:tax-strategy` | A6 Tax Strategist | Depreciation, 1031, cost segregation |
| `/real-estate-investment:stress-test` | A7 Stress Tester | Scenario analysis across adverse conditions |
| `/real-estate-investment:analyze-syndication` | A8 Syndication Analyzer | SPV/fund structure, fees, investor protections |
| `/real-estate-investment:assess-international` | A9 Int'l Risk Assessor | Cross-border, FX, jurisdiction, leasehold risks |
| `/real-estate-investment:analyze-hospitality` | A10 Hospitality Underwriter | Hotel/resort metrics (ADR, RevPAR, GOP) |
| `/real-estate-investment:review-legal` | A11 Legal Reviewer | Red flags in PPMs, SHAs, operating agreements |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `analyze-deal.md` → `/real-estate-investment:analyze-deal`).
