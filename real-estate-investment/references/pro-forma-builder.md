# Skill 3: Pro Forma Builder

Build multi-year cash flow projections (typically 5–10 years) with exit modeling and sensitivity analysis. This is the tool for answering "what will this investment look like over time?"

## When to Use

- User asks about future cash flow or long-term returns
- User wants IRR or equity multiple calculations
- User is comparing hold periods (3 vs 5 vs 10 years)
- User needs to present projections to partners or lenders
- After initial underwriting, to model the full investment lifecycle

## Required Inputs

| Input | Required? | Default if Missing |
|---|---|---|
| Year 1 Gross Potential Rent | Yes | From underwriting |
| Year 1 Operating Expenses | Yes | From underwriting |
| Purchase Price | Yes | — |
| Down Payment % | No | 25% |
| Interest Rate | No | 6.5% |
| Amortization (years) | No | 30 |
| Vacancy Rate | No | 7% |
| Other Income (Year 1) | No | $0 |
| Annual Rent Growth | No | 2.5% |
| Annual Expense Growth | No | 2.5% |
| Hold Period (years) | No | 5 years |
| Exit Cap Rate | No | Entry cap + 0.50% |
| Selling Costs % | No | 5% |
| Marginal Tax Rate | No | 32% |

## Projection Methodology

### Year-over-Year Projections

For each year (1 through N):

```
Gross Potential Rent[Y] = GPR[Y-1] × (1 + Rent Growth)
Vacancy Loss[Y] = GPR[Y] × Vacancy Rate
Other Income[Y] = Other Income[Y-1] × (1 + Rent Growth)
Effective Gross Income[Y] = GPR[Y] − Vacancy[Y] + Other Income[Y]
Operating Expenses[Y] = OpEx[Y-1] × (1 + Expense Growth)
NOI[Y] = EGI[Y] − OpEx[Y]
Cash Flow[Y] = NOI[Y] − Annual Debt Service (constant for fixed-rate)
DSCR[Y] = NOI[Y] ÷ Annual Debt Service
```

### Debt Service Calculation

```
Loan Amount = Purchase Price × (1 − Down Payment %)
Monthly Payment = PMT(rate/12, amort_years×12, -loan_amount)
Annual Debt Service = Monthly Payment × 12
```

For each year, calculate:
```
Interest Paid[Y] = remaining balance × rate (summed monthly)
Principal Paid[Y] = Annual Debt Service − Interest Paid[Y]
Remaining Balance[Y] = Balance[Y-1] − Principal Paid[Y]
```

### Exit / Sale Modeling

At the end of the hold period:

```
Exit NOI = NOI of the year following sale (projected)
Property Value at Sale = Exit NOI ÷ Exit Cap Rate
Selling Costs = Property Value × Selling Cost %
Remaining Loan Balance = calculated from amortization schedule
Net Sale Proceeds = Property Value − Selling Costs − Remaining Balance
```

### Return Calculations

**Cash-on-Cash Return** (each year):
```
CoC[Y] = Cash Flow[Y] ÷ Total Cash Invested
```

**Equity Multiple**:
```
Total Distributions = Sum of all Cash Flows + Net Sale Proceeds
Equity Multiple = Total Distributions ÷ Total Cash Invested
```

**IRR**:
```
Cash flows = [-Total Cash Invested, CF Year 1, CF Year 2, ..., CF Year N + Net Sale Proceeds]
IRR = rate that makes NPV of these cash flows = 0
```

Use Excel's IRR function or numpy's irr/npv functions.

**Total ROI Components** (for each year):
```
Cash Flow Return = Cash Flow ÷ Total Cash Invested
Appreciation Return = (Property Value × Appreciation Rate) ÷ Total Cash Invested
Principal Paydown Return = Principal Paid ÷ Total Cash Invested
Tax Benefit Return = Depreciation Tax Savings ÷ Total Cash Invested
Total ROI = sum of all four components
```

## Output Format

### Summary Dashboard

```
10-YEAR PRO FORMA SUMMARY
═══════════════════════════════════════
Entry Price: $XXX,XXX | Exit Value: $X,XXX,XXX | Hold: X years

RETURN METRICS
  IRR:                    XX.X%
  Equity Multiple:        X.Xx
  Avg Annual CoC:         X.X%
  Total Profit:           $XXX,XXX
```

### Year-by-Year Table

Create a table with these rows for each year (columns = years):

```
                    Year 1    Year 2    Year 3    ...    Year N    Sale
Gross Potential Rent
Less: Vacancy
Other Income
Effective Gross Income
Operating Expenses
NET OPERATING INCOME
Debt Service
PRE-TAX CASH FLOW
DSCR
Cash-on-Cash Return
Cumulative Cash Flow
```

### Exit Analysis

```
EXIT ANALYSIS (Year X Sale)
  Projected NOI:              $XX,XXX
  Exit Cap Rate:              X.XX%
  Implied Sale Price:         $X,XXX,XXX
  Appreciation (total):       XX.X%
  Less: Selling Costs (X%):   ($XX,XXX)
  Less: Remaining Mortgage:   ($XXX,XXX)
  NET SALE PROCEEDS:          $XXX,XXX
```

## Sensitivity Analysis (Always Include)

Run the pro forma under stressed assumptions and present a sensitivity matrix:

### Rent Growth Sensitivity
Test at: 0%, 1%, 2% (base), 3%, 4%
Show: IRR and Equity Multiple at each rate

### Exit Cap Rate Sensitivity
Test at: Base −0.25%, Base, Base +0.25%, Base +0.50%, Base +0.75%
Show: Sale Price, Net Proceeds, IRR at each rate

### Combined Sensitivity Matrix (IRR)
Rows = rent growth rates, Columns = exit cap rates
Each cell = resulting IRR

```
IRR SENSITIVITY (Rent Growth vs Exit Cap Rate)
              6.5%     7.0%     7.5%     8.0%
  1.0%        X.X%     X.X%     X.X%     X.X%
  2.0%        X.X%     X.X%     X.X%     X.X%
  3.0%        X.X%     X.X%     X.X%     X.X%
  4.0%        X.X%     X.X%     X.X%     X.X%
```

## Hold Period Comparison

If the user hasn't committed to a hold period, compare 3, 5, 7, and 10-year holds:

```
HOLD PERIOD COMPARISON
              3-Year    5-Year    7-Year    10-Year
IRR           XX.X%     XX.X%     XX.X%     XX.X%
Eq Multiple   X.Xx      X.Xx      X.Xx      X.Xx
Total Profit  $XXX,XXX  $XXX,XXX  $XXX,XXX  $XXX,XXX
Avg CoC       X.X%      X.X%      X.X%      X.X%
```

## When Building Spreadsheets

If creating an Excel pro forma, follow these conventions:
- Input cells with blue font (hardcoded assumptions)
- Formula cells with black font
- Yellow background on key assumption cells
- Include a dashboard/summary sheet and a detailed projections sheet
- All formulas should reference input cells (no hardcoded numbers in formulas)
- Include sensitivity tables using Excel DATA TABLES or manual scenario columns

## Development & Pre-Construction Pro Forma Adjustments

For ground-up development, pre-construction syndications, and major value-add projects, standard stabilized pro forma assumptions don't apply. Use the following modifications:

### The J-Curve Pattern

Development deals exhibit a characteristic "J-Curve" in IRR calculation:
- **Phase 1 (Negative)**: Capital is deployed for land acquisition, permits, and construction. No revenue. IRR is deeply negative.
- **Phase 2 (Recovery)**: Property completes, lease-up or ramp-up begins. Initial revenue is below stabilized levels. IRR climbs toward zero.
- **Phase 3 (Positive)**: Revenue stabilizes and/or exit event occurs. IRR turns positive and accelerates as profits are realized against the time-weighted investment.

```
J-CURVE CASH FLOW PATTERN (Development/Pre-Construction)

Year:        -2        -1        0         1         2         3        4+
Phase:       Design    Build     Complete  Ramp-Up   Ramp-Up   Stabil.  Stabilized
Cash Flow:   -$XXX     -$XXX     -$XXX     -$XX      +$XX      +$XXX    +$XXX
Cumulative:  -$XXX     -$XXX     -$XXX     -$XXX     -$XX      +$XX     +$XXX
IRR (if sold):  n/a    neg       neg       low       moderate  target   target+
```

**Key implication**: Do not evaluate development deals using Year 1 CoC or stabilized cap rates. Use IRR and Equity Multiple over the full cycle, including the construction/ramp-up period.

### Ramp-Up Schedule for Hospitality & New Construction

New properties do NOT achieve stabilized revenue immediately. Apply ramp-up discounts:

| Property Type | Year 1 | Year 2 | Year 3 | Year 4+ |
|---|---|---|---|---|
| Hotel/Resort | 50-65% of stabilized RevPAR | 70-85% | 85-95% | Stabilized |
| Multifamily (new) | 70-80% occupancy during lease-up | 85-90% | 90-95% | Stabilized |
| Commercial (new) | 40-60% leased | 60-80% | 80-90% | Stabilized |
| STR / Vacation Rental | 40-55% occupancy | 55-70% | 65-75% | Stabilized (market-dependent) |

**Red flag**: Any sponsor projecting stabilized performance from Day 1 of a new property is being unrealistic. Always model the ramp-up period explicitly in the pro forma.

### Construction Period Modeling

```
CONSTRUCTION PERIOD PRO FORMA
  Land Acquisition:             $XXX,XXX   (Month 0)
  Soft Costs (design, permits): $XXX,XXX   (Months 0-6)
  Hard Costs (construction):    $XXX,XXX   (Months 3-18, draw schedule)
  FF&E / Fit-Out:               $XXX,XXX   (Months 15-20)
  Contingency (10-20%):         $XXX,XXX
  Financing Carry (interest):   $XXX,XXX   (Interest-only during construction)
  Pre-Opening Costs:            $XXX,XXX   (Staff hiring, marketing, soft launch)
  
  TOTAL DEVELOPMENT BUDGET:     $X,XXX,XXX
  
  DELAY SCENARIO:
    Each month of delay costs:  $XX,XXX (carrying costs)
    6-month delay total impact: $XXX,XXX additional capital required
    Impact on IRR:              -X.X% per 3-month delay (approximate)
```

## Pro Forma Code Templates

### Python: Full Multi-Year DCF Pro Forma

```python
"""
Multi-Year DCF Pro Forma Generator
Produces year-by-year projections with IRR and Equity Multiple.
"""
import numpy as np

def build_pro_forma(
    purchase_price, year1_noi, hold_years=5,
    rent_growth=0.025, expense_growth=0.025,
    entry_cap_rate=None, exit_cap_premium=0.005,
    down_pct=0.25, closing_pct=0.03, selling_cost_pct=0.05,
    interest_rate=0.065, loan_term=30, expense_ratio=0.45
):
    """Build a complete DCF pro forma with IRR calculation."""
    
    if entry_cap_rate is None:
        entry_cap_rate = year1_noi / purchase_price
    
    exit_cap = entry_cap_rate + exit_cap_premium
    loan = purchase_price * (1 - down_pct)
    total_cash_in = purchase_price * (down_pct + closing_pct)
    
    # Monthly mortgage
    mr = interest_rate / 12
    n = loan_term * 12
    monthly_pmt = loan * (mr * (1 + mr)**n) / ((1 + mr)**n - 1)
    annual_ds = monthly_pmt * 12
    
    # Year-by-year projection
    cash_flows = [-total_cash_in]
    balance = loan
    noi = year1_noi
    
    print(f"{'Year':<6} {'NOI':>10} {'Debt Svc':>10} {'Cash Flow':>10} {'Balance':>12}")
    print("-" * 52)
    
    for yr in range(1, hold_years + 1):
        if yr > 1:
            gross = noi / (1 - expense_ratio)
            new_gross = gross * (1 + rent_growth)
            new_exp = (gross * expense_ratio) * (1 + expense_growth)
            noi = new_gross - new_exp
        
        cf = noi - annual_ds
        interest = balance * interest_rate
        principal = annual_ds - interest
        balance -= principal
        
        cash_flows.append(cf)
        print(f"{yr:<6} ${noi:>9,.0f} ${annual_ds:>9,.0f} ${cf:>9,.0f} ${balance:>11,.0f}")
    
    # Exit
    exit_noi = noi * (1 + rent_growth)  # forward NOI
    sale_price = exit_noi / exit_cap
    net_sale = sale_price * (1 - selling_cost_pct) - balance
    cash_flows[-1] += net_sale
    
    # IRR & Equity Multiple
    irr = np.irr(cash_flows)
    total_distributions = sum(cf for cf in cash_flows if cf > 0)
    equity_multiple = total_distributions / total_cash_in
    
    print(f"\n{'='*52}")
    print(f"Sale Price (Yr {hold_years}):  ${sale_price:>12,.0f}")
    print(f"Net Sale Proceeds:    ${net_sale:>12,.0f}")
    print(f"IRR:                  {irr:>12.2%}")
    print(f"Equity Multiple:      {equity_multiple:>12.2f}x")
    print(f"Total Cash Invested:  ${total_cash_in:>12,.0f}")
    
    return {"irr": irr, "equity_multiple": equity_multiple, 
            "sale_price": sale_price, "cash_flows": cash_flows}

# Example: 20-unit apartment building
build_pro_forma(
    purchase_price=2000000, year1_noi=140000, hold_years=5,
    rent_growth=0.03, expense_growth=0.025, exit_cap_premium=0.005
)
```

### JavaScript: Quick IRR Calculator (for React/HTML artifacts)

```javascript
function calcIRR(cashFlows, guess = 0.1) {
  const maxIter = 1000;
  const tolerance = 1e-7;
  let rate = guess;
  
  for (let i = 0; i < maxIter; i++) {
    let npv = 0, dnpv = 0;
    for (let t = 0; t < cashFlows.length; t++) {
      npv += cashFlows[t] / Math.pow(1 + rate, t);
      dnpv -= t * cashFlows[t] / Math.pow(1 + rate, t + 1);
    }
    const newRate = rate - npv / dnpv;
    if (Math.abs(newRate - rate) < tolerance) return newRate;
    rate = newRate;
  }
  return rate;
}

// Example: $100K invested, $12K/yr for 5 years, sell for $120K in year 5
const flows = [-100000, 12000, 12000, 12000, 12000, 12000 + 120000];
console.log(`IRR: ${(calcIRR(flows) * 100).toFixed(2)}%`);
```
