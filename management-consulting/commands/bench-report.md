---
description: Generate a bench and utilization report
argument-hint: "<period or team>"
---

# Bench & Utilization Report

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a bench management report showing consultant availability, utilization trends, and staffing outlook.

## Usage

```
/bench-report <period>
```

### Arguments

- `period` — Reporting period or scope:
  - `weekly` — Current week snapshot
  - `monthly` — Monthly utilization summary
  - `quarterly` — Quarterly trends and forecast
  - A specific team or practice name

## Workflow

### 1. Gather Data

If ~~project tracker or ~~data warehouse is connected:
- Pull current staffing assignments and end dates
- Pull time/billing data for utilization calculations
- Pull pipeline data for demand forecasting

If no data source is connected:
> Provide: current bench list (names, levels, skills, days on bench), active engagements with expected end dates, and upcoming staffing needs.

### 2. Generate Report

Include:
- **Current bench roster** — Who's available, for how long, key skills
- **Utilization summary** — Rates by level vs. target, trending over last 3 periods
- **Upcoming availability** — Consultants rolling off engagements in the next 30/60/90 days
- **Demand pipeline** — Staffing needs from proposals in progress or won engagements
- **Skill gap analysis** — Demand that can't be met with current bench
- **Recommended actions** — Staffing decisions, training investments, contractor needs

### 3. Output

Provide the formatted bench report with key metrics highlighted and action items for leadership.
