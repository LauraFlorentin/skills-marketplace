---
description: Build a financial business case or ROI analysis for a recommendation
argument-hint: "<recommendation or initiative>"
---

# Business Case / Financial Model

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

**Important**: All financial analyses should be reviewed by qualified financial professionals before use in investment decisions.

Build a business case or ROI analysis to justify a consulting recommendation or client investment.

## Usage

```
/business-case <initiative>
```

### Arguments

- `initiative` — The investment or recommendation to justify:
  - `cost-reduction` — Cost takeout or efficiency improvement
  - `technology` — Technology investment or platform migration
  - `restructuring` — Organizational restructuring savings
  - `market-entry` — New market or product launch
  - `custom` — Any other initiative requiring financial justification

## Workflow

### 1. Gather Financial Inputs

If ~~data warehouse or ~~documents is connected:
- Pull baseline financial data, historical costs, and revenue figures
- Access budget documents and prior business cases

If no data source is connected:
> Provide: current costs, projected savings or revenue, investment required, timeline, discount rate, and key assumptions.

### 2. Build the Model

Construct a financial analysis including:
- **Cost-benefit analysis** — All direct costs, indirect costs, one-time investments, and ongoing costs vs. quantified benefits (hard savings, revenue uplift, soft benefits)
- **NPV calculation** — Net present value using appropriate discount rate (typically 8-12% for corporate investments)
- **IRR** — Internal rate of return compared to hurdle rate
- **Payback period** — Time to recover initial investment
- **Scenario analysis** — Best case, base case, worst case with probability weighting

### 3. Sensitivity Analysis

Test the model against key assumption changes:
- What happens if benefits are 20% lower than projected?
- What if implementation takes 6 months longer?
- What if costs exceed estimates by 15%?

Identify the 3-5 assumptions that most influence the outcome.

### 4. Executive Summary

Distill the analysis into a one-page business case summary:
- Investment required
- Expected return (NPV, IRR, payback)
- Key assumptions and risks
- Recommendation with confidence level

### 5. Output

Provide:
1. One-page business case summary for executive review
2. Detailed financial model with calculations and assumptions
3. Sensitivity analysis showing key risk factors
4. Scenario comparison (best/base/worst)
5. Recommendation with go/no-go criteria
