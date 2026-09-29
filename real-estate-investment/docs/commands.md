# Real Estate Investment Commands

Slash commands for Claude Code. The `.md` files in `commands/` become `/real-estate-investment:command-name` commands. This catalog is kept outside that directory so it is not interpreted as a command.

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
| `/real-estate-investment:screen-deal` | A2 Deal Screener | Preliminary triage with deal-appropriate metrics and evidence gaps |
| `/real-estate-investment:underwrite` | A3 Property Underwriter | Full financial underwriting (NOI, CoC, DSCR) |
| `/real-estate-investment:pro-forma` | A4 Pro Forma Builder | Multi-year financial projections |
| `/real-estate-investment:compare-financing` | A5 Financing Analyzer | Compare loan options and leverage impact |
| `/real-estate-investment:tax-strategy` | A6 Tax Strategist | Depreciation, 1031, cost segregation |
| `/real-estate-investment:stress-test` | A7 Stress Tester | Scenario analysis across adverse conditions |
| `/real-estate-investment:analyze-syndication` | A8 Syndication Analyzer | SPV/fund structure, fees, investor protections |
| `/real-estate-investment:assess-international` | A9 Int'l Risk Assessor | Cross-border, FX, jurisdiction, leasehold risks |
| `/real-estate-investment:analyze-hospitality` | A10 Hospitality Underwriter | Hotel/resort metrics (ADR, RevPAR, GOP) |
| `/real-estate-investment:review-legal` | A11 Legal Reviewer | Document issue spotting and next steps |

## Adding a Command

Create a new `.md` file in `commands/` with YAML frontmatter and operating instructions. The filename becomes the command name (for example, `analyze-deal.md` becomes `/real-estate-investment:analyze-deal`).
