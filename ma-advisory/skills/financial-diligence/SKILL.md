---
name: "Financial Diligence"
description: >
  Financial due diligence and Quality of Earnings (QoE) reporting. Automates
  trial balance tie-outs, EBITDA adjustment validation, working capital analysis,
  and debt-like item identification. Detects anomalies in general ledgers and
  accelerates the reconciliation process that traditionally consumes weeks.
version: "1.0"
author: "LauraFlorentin"
---

# Financial Diligence

The Quality of Earnings report directly dictates final purchase price adjustments and protects buyers from overpaying for inflated performance. This skill automates the foundational labor of financial due diligence.

## When to Use

- Performing a Quality of Earnings analysis on a target
- Validating management-proposed EBITDA adjustments
- Reconciling trial balances against audited financials and tax returns
- Identifying off-balance-sheet liabilities and debt-like items
- Analyzing net working capital for purchase agreement peg negotiations

## Quality of Earnings Report Structure

| Section | Focus |
|---------|-------|
| Quality of Earnings Summary | Bridge between reported and run-rate adjusted EBITDA |
| Revenue & Margin Analysis | Customer concentration, product mix, volume vs. price trends |
| EBITDA Adjustments | Validate or refute each management add-back |
| Net Working Capital (NWC) | Historical peg calculation, seasonality, aged receivables, obsolete inventory |
| Debt and Debt-Like Items | Off-balance-sheet liabilities, deferred revenue, unpaid bonuses, unfunded capex |

## AI-Assisted Workflow

### Trial Balance Reconciliation

1. **Ingest** trial balances, audited financials, bank statements, and tax returns (3-5 year lookback)
2. **Map** granular account codes to standard FDD analytical groupings
3. **Reconcile** across data sources, flagging discrepancies
4. **Detect anomalies** — sudden expense spikes, unusual journal entries near deal launch

### EBITDA Adjustment Analysis

For each proposed management add-back:

```
## EBITDA Bridge

### Reported EBITDA: $[X]M

| # | Adjustment | Amount | Category | Defensibility | Notes |
|---|-----------|--------|----------|---------------|-------|
| 1 | Owner excess compensation | $[X]K | Recurring normalization | HIGH | Benchmarked against market rate |
| 2 | One-time litigation | $[X]K | Non-recurring | HIGH | Settlement confirmed, no ongoing exposure |
| 3 | "COVID impact" | $[X]K | Disputed | LOW | Revenue decline appears structural |
| ... | ... | ... | ... | ... | ... |

### Adjusted EBITDA: $[X]M
### Buy-Side Recommended EBITDA: $[X]M (variance: $[X]K)
```

### Net Working Capital Analysis

```
## NWC Peg Analysis

### Trailing 12-Month Average NWC: $[X]M

| Component | Avg Balance | Seasonality | Flags |
|-----------|------------|-------------|-------|
| Accounts Receivable | $[X]M | [Pattern] | [Aged AR > 90 days: $X] |
| Inventory | $[X]M | [Pattern] | [Obsolete: $X] |
| Prepaid Expenses | $[X]M | | |
| Accounts Payable | ($[X]M) | | [Stretched beyond terms?] |
| Accrued Liabilities | ($[X]M) | | |

### Recommended NWC Target: $[X]M
### Mechanism: [Dollar-for-dollar adjustment / collar]
```

## Operating Guidelines

- Always validate management's reported EBITDA independently — never accept at face value
- Distinguish between truly non-recurring items and items management wishes were non-recurring
- Flag revenue recognition policy changes during the lookback period
- Identify related-party transactions and verify arm's-length pricing
- For NWC, exclude cash and debt from the calculation unless specified in the purchase agreement
- AI outputs are analytical aids — the subjective debate over valid add-backs requires human judgment
- Time saved: automates tie-out process that traditionally takes **40+ hours**
