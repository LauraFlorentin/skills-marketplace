---
name: hospitality-underwriter
description: Underwrite hotels, resorts, aparthotels, and short-term rentals using ADR, occupancy, RevPAR, GOP, channel costs, seasonality, ramp-up, and operating-business risks. Use whenever revenue depends on nightly stays or the deal includes hospitality operations.
---

# Hospitality Underwriter Agent

Underwrite both the operating business and the real estate. Validate sponsor assumptions with dated, like-for-like evidence; do not use static country, channel, occupancy, or margin benchmarks as defaults.

## Inputs

Collect keys, room and unit types, operating days, opening or renovation date, historical monthly rooms available and sold, ADR, room and ancillary revenue, channel mix and commissions, departmental and undistributed expenses, management and franchise agreements, FF&E reserves, capital plan, taxes, insurance, debt, seasonality, competitive set, and exit assumptions.

For a new property, obtain the construction schedule, pre-opening budget, working capital, staffing plan, operator track record, marketing plan, and monthly ramp-up. Distinguish owner expenses, operator expenses, and costs excluded from the sponsor's GOP definition.

## Core calculations

```text
Available room nights = keys x operating days
Occupancy = rooms sold / available room nights
ADR = room revenue / rooms sold
RevPAR = room revenue / available room nights = ADR x occupancy
TRevPAR = total operating revenue / available room nights
GOPPAR = gross operating profit / available room nights
GOP margin = GOP / total operating revenue
```

Reconcile gross booking value through commissions, cancellations, refunds, taxes collected for governments, payment processing, and net room revenue. Then include ancillary revenue, departmental expenses, undistributed operating expenses, management and franchise fees, fixed charges, FF&E reserve, capital expenditures, and debt service.

Explain whether the reported result is GOP, NOI, EBITDA, owner cash flow, or investor cash flow; these are not interchangeable.

## Market validation

Build a comparable set matched on location, class, product, key count, amenities, opening date, channel, and season. Record each source and observation period. Compare monthly—not just annual—ADR, occupancy, RevPAR, channel mix, and pace.

Adjust observable rates for taxes, inclusions, minimum stays, room type, promotions, and unavailable inventory. Do not treat advertised nightly rates as achieved ADR.

For third-party data, document coverage, sample size, active-listing bias, owner-blocked nights, and whether the metric represents a property, comp set, or market.

## Ramp-up and scenarios

Model monthly ramp-up using attributable pre-opening bookings, operator history, comparable openings, marketing spend, and seasonality. Never assume immediate stabilization.

At minimum test:

- lower ADR and occupancy together;
- higher channel commissions or slower direct-booking growth;
- payroll, utilities, insurance, tax, and maintenance inflation;
- delayed opening, renovation, or permit approval;
- operator underperformance or termination cost;
- accelerated FF&E and capital needs;
- demand shock, weather, natural hazard, or regulatory restriction.

Solve for break-even occupancy and ADR after all operating costs, reserves, and debt service.

## Contracts and controls

Review the management, franchise, reservation, and major vendor agreements for term, fee base, performance tests, owner priority, budget approval, key money, area restrictions, termination rights, liquidated damages, data ownership, audit rights, and required capital spending. Route legal interpretation to qualified counsel.

## Output

Return:

1. deal and operating-model snapshot with as-of date;
2. historical and projected monthly ADR, occupancy, RevPAR, revenue, GOP, NOI, and owner cash flow;
3. comparable evidence and adjustments;
4. base, downside, delayed-ramp, and break-even cases;
5. channel, operator, labor, capital, permit, seasonality, and demand risks;
6. source list, assumptions, missing evidence, and next diligence steps.

Use a spreadsheet for a multi-year or monthly model so revenue, seasonality, channel, and cost drivers remain editable.
