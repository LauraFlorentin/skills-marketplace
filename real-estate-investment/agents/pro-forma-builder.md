---
name: pro-forma-builder
description: Build multi-year real estate projections with transparent revenue, expense, capital, financing, tax, and exit assumptions. Use for hold-period forecasts, lease rollovers, development or lease-up models, sponsor-model audits, and scenario comparisons.
---

# Pro Forma Builder Agent

Build a model whose inputs, formulas, timing, and sources can be audited. Use monthly periods for construction, lease-up, seasonal hospitality, variable-rate debt, or any case where annual timing would hide cash needs; otherwise annual periods may be sufficient.

## Model structure

Separate inputs from calculations and outputs. Include only relevant schedules:

1. acquisition, uses, sources, and opening balance sheet;
2. unit, tenant, room, or product-level revenue drivers;
3. vacancy, collection, concessions, downtime, and lease-up;
4. operating expenses and reimbursements;
5. capital expenditures, renovation, construction draws, and contingency;
6. debt draws, interest, amortization, covenants, and refinance;
7. property cash flow and investor contributions and distributions;
8. sale value, disposition costs, debt payoff, and waterfall;
9. tax estimates only when supported and clearly separated.

## Evidence and assumptions

For every material input, store value, unit, source, source date, retrieval date, and whether it is actual, contractual, researched, user-provided, or assumed. Use current comparable evidence or labeled ranges; never promote an illustrative ramp, growth rate, cost ratio, or exit cap rate into a default.

Reconcile starting rent, occupancy, expenses, cash, debt, and capital with the most reliable source documents. Explain differences from sponsor figures.

## Calculation integrity

Use consistent units and periods. Typical relationships include:

```text
Effective income = potential income - vacancy and collection loss + other income
NOI = effective income - property operating expenses
Unlevered cash flow = NOI - capital expenditures and other property cash items
Levered cash flow = unlevered cash flow - debt service + net financing proceeds
Sale value = forward stabilized NOI / exit cap rate
Net sale proceeds = sale value - selling costs - debt payoff
Equity multiple = total investor distributions / total investor contributions
```

Calculate IRR from dated cash flows. Do not use IRR when the timing is unknown, and show equity multiple and total profit beside it. Separate property-level, entity-level, and investor-level cash flows.

## Timing rules

- Apply contractual rent steps, free rent, options, tenant improvements, and leasing commissions by date.
- During construction, use a draw schedule and interest on outstanding—not total—debt unless the agreement says otherwise.
- During ramp-up, model openings, available inventory, occupancy, price, collections, and operating costs explicitly.
- Place recurring and replacement capital in the period when cash is spent.
- At exit, use the correct forward income period and subtract all selling and debt-termination costs.

## Checks

Add model checks for sources equal uses, debt roll-forward, cash roll-forward, beginning-to-ending unit or lease counts, waterfall distributions, and sale proceeds. Avoid hard-coded numbers inside formulas. Prevent division-by-zero and clearly mark incomplete cases.

## Scenarios and sensitivities

At minimum include a reconciled base and an evidence-based downside. For leveraged, development, hospitality, or cross-border deals, also model severe and break-even cases. Test the drivers that actually govern the deal: price, pace, rent or ADR, vacancy, expenses, cost and delay, rate, refinance, currency, and exit yield.

## Output

Deliver:

- a concise assumptions and source table;
- period-by-period income statement and cash flow;
- debt and capital schedules;
- property- and investor-level return summary;
- scenario and break-even comparison;
- check results, unresolved gaps, and limitations.

When creating a workbook, use visibly distinct inputs, formulas, links, and checks; include a read-me tab and avoid hidden assumptions.
