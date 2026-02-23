# Skill 2: Property Underwriter

Perform comprehensive financial analysis on a specific investment property. This is the core analytical skill — it calculates every metric an investor needs to make a buy/pass decision.

## When to Use

- After a deal passes initial screening
- User says "analyze this property" or "underwrite this deal"
- User uploads a property listing, rent roll, or T-12 statement
- User provides detailed property financials

## Analysis Modes

Route to the correct sub-analysis based on property type:

| Property Type | Analysis Mode | Key Differences |
|---|---|---|
| Single-family rental | Residential | Per-unit metrics, 1% rule emphasis |
| Small multifamily (2-4) | Residential | Per-door cash flow, unit-level rents |
| Large multifamily (5+) | Multifamily | NOI-driven, expense ratios, DSCR focus |
| Commercial (retail, office, industrial) | Commercial | Lease analysis, NNN vs gross, per-SF metrics |
| Fix-and-flip | Flip | ARV, 70% rule, holding costs, profit margin |

## Required Inputs by Mode

### Residential / Multifamily
| Input | Required? | Default if Missing |
|---|---|---|
| Purchase price | Yes | — |
| Monthly rent (per unit) | Yes | — |
| Number of units | Yes | — |
| Down payment % | No | 25% |
| Interest rate | No | 6.5% |
| Loan term | No | 30 years |
| Vacancy rate | No | 7% |
| Property taxes (annual) | Helpful | 1.2% of purchase price |
| Insurance (annual) | Helpful | 0.5% of purchase price |
| Property management % | No | 8% (SFR), 6% (MF) |
| Other monthly income | No | $0 |
| Immediate rehab costs | No | $0 |

### Commercial
All residential inputs PLUS:
| Input | Required? | Default if Missing |
|---|---|---|
| Rentable square feet | Helpful | Derive from rent/SF |
| Lease type (NNN, Gross, Modified) | Helpful | Gross |
| Annual base rent per SF | Yes (or total rent) | — |
| NNN reimbursements | If NNN | $0 |
| WALT (weighted avg lease term) | Helpful | — |
| Amortization period | No | 25 years |

### Fix-and-Flip
| Input | Required? | Default if Missing |
|---|---|---|
| Purchase price | Yes | — |
| After Repair Value (ARV) | Yes | — |
| Estimated repair costs | Yes | — |
| Contingency % | No | 15% |
| Holding period (months) | No | 5 months |
| Financing (rate, LTV, points) | No | 12% hard money, 80% LTV, 2 pts |
| Agent commission % | No | 5% |
| Selling closing costs % | No | 2% |

## Calculation Procedures

### Residential / Multifamily Underwriting

**Step 1: Calculate Gross Income**
```
Gross Potential Rent = Monthly Rent × Units × 12
Vacancy Loss = GPR × Vacancy Rate
Other Income = Other Monthly Income × 12
Effective Gross Income = GPR − Vacancy Loss + Other Income
```

**Step 2: Calculate Operating Expenses**
Line-item each expense:
- Property Taxes: actual or estimate at 1.0–1.5% of purchase price
- Insurance: actual or estimate at 0.3–0.6% of purchase price
- Property Management: % of Effective Gross Income
- Repairs & Maintenance: 5–10% of gross rent (use 8% if unknown)
- CapEx Reserves: 8–10% of gross rent (SFR) or $250–600/unit/year (MF)
- Utilities (if landlord-paid): actual or $100–200/unit/month
- Landscaping: actual or $50–150/month
- Administrative: 1–2% of EGI
- Marketing/Turnover: 1–2% of EGI

```
Total Operating Expenses = sum of all above
Operating Expense Ratio = Total OpEx ÷ EGI
```

Reality-check: residential expense ratios should fall between 35–55%. If outside this range, investigate.

**Step 3: Calculate NOI**
```
NOI = EGI − Total Operating Expenses
```

**Step 4: Calculate Financing**
```
Loan Amount = Purchase Price × (1 − Down Payment %)
Monthly Payment = standard amortization formula (PMT function)
Annual Debt Service = Monthly Payment × 12
```

**Step 5: Calculate All Returns**
```
Annual Pre-Tax Cash Flow = NOI − Annual Debt Service
Cash-on-Cash Return = Cash Flow ÷ Total Cash Invested
  where Total Cash Invested = Down Payment + Closing Costs + Rehab Costs

Cap Rate = NOI ÷ Purchase Price
DSCR = NOI ÷ Annual Debt Service
GRM = Purchase Price ÷ Annual Gross Rent
Cash Flow per Door = Monthly Cash Flow ÷ Number of Units
Break-Even Occupancy = (OpEx + Debt Service) ÷ Gross Operating Income
```

**Step 6: Calculate Total ROI (Year 1)**
```
Appreciation = Purchase Price × 3% (or user-specified growth rate)
Principal Paydown = Year 1 principal portion of mortgage payments
Depreciation Tax Savings = (Purchase Price × 80% ÷ 27.5) × Marginal Tax Rate
Total ROI = (Cash Flow + Appreciation + Principal Paydown + Tax Savings) ÷ Total Cash Invested
```

### Commercial Underwriting

Same as multifamily but with these additions:
- Calculate Price per SF = Purchase Price ÷ Rentable SF
- Compare rent per SF to market comps
- For NNN leases: add reimbursement income, reduce landlord expenses accordingly
- Calculate WALT if lease data available
- Note lease expiration concentration risk
- Apply commercial amortization (typically 25 years, not 30)
- Note balloon payment risk at loan maturity

### Fix-and-Flip Underwriting

**Step 1: 70% Rule Check**
```
Max Purchase = (ARV × 0.70) − Total Repair Budget
Total Repair Budget = Repair Estimate × (1 + Contingency %)
Over/Under = Max Purchase − Actual Purchase Price
```

**Step 2: Total Project Cost**
```
Acquisition Costs = Purchase Price + Buying Closing Costs (1–2%)
Repair Costs = Estimate + Contingency
Financing Costs = Points + (Monthly Interest × Hold Period)
Holding Costs = (Monthly Taxes + Insurance + Utilities) × Hold Period
Total Project Cost = Acquisition + Repairs + Financing + Holding
```

**Step 3: Sale Proceeds**
```
Gross Sale Price = ARV
Agent Commission = ARV × Commission %
Selling Closing = ARV × Closing %
Net Sale Proceeds = ARV − Commission − Closing Costs
```

**Step 4: Profit Analysis**
```
Total Profit = Net Sale Proceeds − Total Project Cost
Profit as % of ARV = Profit ÷ ARV
ROI = Profit ÷ Cash Invested
Annualized ROI = (1 + ROI)^(12/Hold Months) − 1
```

Target: $20K–$30K minimum profit (under $250K ARV) or 10–15% of ARV.

## Output Format

Present a structured analysis report:

```
PROPERTY INVESTMENT ANALYSIS
═══════════════════════════════════════
[Property description / address]

PURCHASE & FINANCING
  Purchase Price:          $XXX,XXX
  Down Payment (XX%):      $XX,XXX
  Loan Amount:             $XXX,XXX
  Rate / Term:             X.XX% / XX years
  Monthly Payment:         $X,XXX
  Total Cash Invested:     $XX,XXX

INCOME & EXPENSES (Annual)
  Gross Potential Rent:    $XX,XXX
  Less Vacancy (X%):       ($X,XXX)
  Other Income:            $X,XXX
  Effective Gross Income:  $XX,XXX
  Operating Expenses:      ($XX,XXX)  [XX% ratio]
  NET OPERATING INCOME:    $XX,XXX

KEY METRICS                VALUE      BENCHMARK    RATING
  Cap Rate                 X.XX%      X.X% avg     Good
  Cash-on-Cash Return      X.XX%      8–12%        Acceptable
  DSCR                     X.XXx      1.25x min    ✓ / ✗
  Cash Flow/Door           $XXX/mo    $150–200     Good
  GRM                      X.X        5–7          Acceptable
  Break-Even Occupancy     XX%        <85%         ✓ / ✗
  Total ROI (Year 1)       XX.X%      —            —

LEVERAGE ANALYSIS
  Cap Rate vs. Debt Cost:  +/- XX bps → Positive / Negative leverage
  [If negative leverage, explain total return thesis]

RECOMMENDATION: BUY / NEGOTIATE / PASS
[2-3 sentence explanation of the verdict with key factors]
```

## Red Flags to Check

During underwriting, flag any of these issues:
- DSCR below 1.20x (won't qualify for most financing)
- Break-even occupancy above 85% (too thin a margin)
- Expense ratio below 30% (likely deferred maintenance or missing costs)
- Expense ratio above 60% (operational problems or old property)
- Cap rate far above market average (hidden risk — investigate)
- Negative cash flow with no clear appreciation thesis
- Property taxes likely to be reassessed significantly higher at purchase price

## Full Underwriting Calculator (Code Template)

When users need a programmable underwriting tool:

```python
"""
Full Property Underwriting Calculator
Input a deal's parameters, get a complete investment analysis.
"""

def underwrite_deal(
    purchase_price, monthly_rent, units=1,
    vacancy_pct=0.07, expense_ratio=0.45,
    down_payment_pct=0.25, interest_rate=0.065, loan_term=30,
    closing_cost_pct=0.03, capex_per_unit_year=400,
    appreciation_rate=0.03, rent_growth=0.025, tax_rate=0.32,
    land_pct=0.20
):
    """Complete property underwriting with all key metrics."""
    
    # === INCOME ===
    gross_rent = monthly_rent * 12
    vacancy_loss = gross_rent * vacancy_pct
    effective_income = gross_rent - vacancy_loss
    
    # === EXPENSES ===
    operating_expenses = gross_rent * expense_ratio
    capex_reserves = capex_per_unit_year * units
    total_expenses = operating_expenses + capex_reserves
    
    # === NOI ===
    noi = effective_income - total_expenses
    cap_rate = noi / purchase_price
    
    # === FINANCING ===
    loan_amount = purchase_price * (1 - down_payment_pct)
    monthly_rate = interest_rate / 12
    n_payments = loan_term * 12
    monthly_pmt = loan_amount * (monthly_rate * (1 + monthly_rate)**n_payments) / \
                  ((1 + monthly_rate)**n_payments - 1)
    annual_debt_service = monthly_pmt * 12
    
    # Year 1 principal paydown (approximate)
    yr1_interest = loan_amount * interest_rate
    yr1_principal = annual_debt_service - yr1_interest
    
    # === CASH FLOW ===
    annual_cash_flow = noi - annual_debt_service
    total_cash_invested = purchase_price * (down_payment_pct + closing_cost_pct)
    cash_on_cash = annual_cash_flow / total_cash_invested
    dscr = noi / annual_debt_service
    cash_flow_per_door = annual_cash_flow / units / 12
    
    # === BREAK-EVEN ===
    break_even_occ = (total_expenses + annual_debt_service) / gross_rent
    
    # === TAX BENEFITS ===
    building_value = purchase_price * (1 - land_pct)
    annual_depreciation = building_value / 27.5
    taxable_income = noi - yr1_interest - annual_depreciation
    tax_benefit = -taxable_income * tax_rate if taxable_income < 0 else 0
    
    # === TOTAL ROI ===
    appreciation = purchase_price * appreciation_rate
    total_return = annual_cash_flow + appreciation + yr1_principal + tax_benefit
    total_roi = total_return / total_cash_invested
    
    # === LEVERAGE CHECK ===
    leverage_spread = cap_rate - interest_rate
    leverage_type = "POSITIVE" if leverage_spread > 0 else "NEGATIVE"
    
    # === PRINT RESULTS ===
    print(f"""
PROPERTY UNDERWRITING REPORT
{'='*50}
Purchase Price:      ${purchase_price:>12,.0f}
Monthly Rent:        ${monthly_rent:>12,.0f}    ({units} unit{'s' if units > 1 else ''})
Annual Gross Rent:   ${gross_rent:>12,.0f}

INCOME
  Gross Rent:        ${gross_rent:>12,.0f}
  Vacancy ({vacancy_pct:.0%}):      $({vacancy_loss:>11,.0f})
  Effective Income:  ${effective_income:>12,.0f}

EXPENSES
  Operating ({expense_ratio:.0%}):   $({operating_expenses:>11,.0f})
  CapEx Reserves:    $({capex_reserves:>11,.0f})
  Total Expenses:    $({total_expenses:>11,.0f})

NOI:                 ${noi:>12,.0f}
Cap Rate:            {cap_rate:>12.2%}

FINANCING
  Loan Amount:       ${loan_amount:>12,.0f}
  Monthly Payment:   ${monthly_pmt:>12,.0f}
  Annual Debt Svc:   ${annual_debt_service:>12,.0f}
  Yr 1 Principal:    ${yr1_principal:>12,.0f}

RETURNS
  Annual Cash Flow:  ${annual_cash_flow:>12,.0f}
  Cash-on-Cash:      {cash_on_cash:>12.2%}   {'✓' if cash_on_cash >= 0.08 else '✗ (below 8%)'}
  DSCR:              {dscr:>12.2f}x  {'✓' if dscr >= 1.25 else '✗ (below 1.25x)'}
  CF/Door:           ${cash_flow_per_door:>12,.0f}/mo {'✓' if cash_flow_per_door >= 100 else '✗ (below $100)'}
  Break-Even Occ:    {break_even_occ:>12.1%}   {'✓' if break_even_occ < 0.85 else '✗ (above 85%)'}
  Leverage:          {leverage_type:>12}  ({leverage_spread:+.2%} spread)

TAX BENEFITS (Yr 1)
  Depreciation:      ${annual_depreciation:>12,.0f}
  Taxable Income:    ${taxable_income:>12,.0f}
  Tax Benefit:       ${tax_benefit:>12,.0f}

TOTAL RETURN (Yr 1)
  Cash Flow:         ${annual_cash_flow:>12,.0f}
  Appreciation:      ${appreciation:>12,.0f}
  Principal Paydown: ${yr1_principal:>12,.0f}
  Tax Benefit:       ${tax_benefit:>12,.0f}
  TOTAL:             ${total_return:>12,.0f}
  Total ROI:         {total_roi:>12.2%}
""")
    
    return {
        "noi": noi, "cap_rate": cap_rate, "cash_on_cash": cash_on_cash,
        "dscr": dscr, "cash_flow_per_door": cash_flow_per_door,
        "break_even_occ": break_even_occ, "total_roi": total_roi,
        "leverage_type": leverage_type
    }

# Example usage:
underwrite_deal(
    purchase_price=400000, monthly_rent=4000, units=4,
    vacancy_pct=0.07, expense_ratio=0.42
)
```
