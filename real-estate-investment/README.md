# Real Estate Investment Analyzer

Evidence-based real estate investment analysis for deal screening, underwriting,
pro formas, financing, tax issue spotting, stress testing, and specialist risk
review. It includes a dependency-free calculation tool and reusable templates
for consistent, auditable analysis.

> **Important:** This plugin assists with investment analysis but does not
> provide financial, legal, tax, accounting, or lending advice. Qualified
> professionals must review outputs before an investment decision.

## How it works

The [orchestrator](./agents/orchestrator.md) classifies a deal by property type,
strategy, geography, stage, and complexity, then routes only the relevant work
to specialist agents. A full analysis reconciles evidence, calculations, and
assumptions before producing an investment memo.

## Components

| Component | Purpose |
|---|---|
| [Real Estate Analyzer](./skills/real-estate-analyzer/SKILL.md) | Entry point for mixed-scope analysis and workflow controls |
| [Commands](./docs/commands.md) | Eleven namespaced commands for full or focused analysis |
| [Agents](./docs/agents.md) | Orchestrator plus ten underwriting, finance, legal, and risk specialists |
| [Templates](./templates/README.md) | Structured intake, source register, workbook, and decision-output templates |
| [Tests](./tests/README.md) | Synthetic regression tests for the bundled calculator |

## Reproducible toolkit

The specialist agents remain the decision workflow; these assets make a result
easier to review and reproduce:

- `scripts/real_estate_calculations.py` calculates a transparent, fixed-rate,
  single-property underwriting summary from a completed JSON intake.
- [`templates/`](./templates/) includes a deal-intake contract, source register,
  financing comparison, risk and legal logs, diligence checklist, investment
  memo, and an editable Excel underwriting model.
- [`tests/`](./tests/) contains synthetic regression cases for the calculator.

Example use from the plugin root:

```bash
python3 scripts/real_estate_calculations.py path/to/completed-deal-intake.json
python3 -m unittest discover -s tests -p 'test_*.py'
```

The calculator uses only values supplied in the intake. It does not source
market data, validate loan eligibility, or give legal, tax, accounting, or
investment advice.

## Confidentiality

Do not commit or upload completed deal intakes, rent rolls, investor lists,
bank information, tax records, credentials, or other confidential materials to
this repository. Use an authorized private working location, minimize personal
data, and confirm authorization before sending materials to an external
provider. See [data handling guidance](./skills/real-estate-analyzer/references/data-handling.md).

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then
install **real-estate-investment**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/real-estate-investment
```
