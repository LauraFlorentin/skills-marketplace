# Skill 6: Stress Tester

Model adverse scenarios to determine whether a deal can survive what could go wrong. This skill shifts the analysis from "how much can I make?" to "can I withstand a downturn?" Every deal should be stress-tested before committing capital.

## When to Use

- After underwriting, before making an offer
- User asks "what could go wrong?" or "what are the risks?"
- User asks "what if vacancy increases?" or "what if rates go up?"
- User wants to know break-even points
- User asks about red flags or due diligence concerns
- When evaluating deals in volatile markets or with thin margins

## Stress Test Categories

Run all four stress tests on every deal. Present results clearly.

### 1. Vacancy Stress Test

```
For each vacancy scenario, recalculate:
  Adjusted GPR = Original GPR × (1 − Vacancy Rate)
  Adjusted NOI = Adjusted EGI − Operating Expenses
  Cash Flow = Adjusted NOI − Debt Service
  DSCR = Adjusted NOI ÷ Debt Service
  CoC = Cash Flow ÷ Total Cash Invested

SCENARIOS:
  Base Case:    X% vacancy (market rate)
  Moderate:     10% vacancy
  Stressed:     15% vacancy
  Severe:       20% vacancy
  Crisis:       25% vacancy

BREAK-EVEN VACANCY:
  The vacancy rate at which Cash Flow = $0
  Formula: Break-Even Vacancy = 1 − [(OpEx + Debt Service) ÷ (GPR + Other Income)]
  
  INTERPRETATION:
    Break-Even < 75%  → Excellent cushion
    Break-Even 75-85% → Adequate
    Break-Even 85-90% → Thin margin, concerning
    Break-Even > 90%  → Dangerously tight, avoid unless strong thesis
```

### 2. Interest Rate Stress Test

For variable-rate loans or anticipated refinances:

```
For each rate scenario, recalculate:
  New Monthly Payment = PMT(new_rate/12, remaining_term, -balance)
  New Annual Debt Service = New Payment × 12
  Cash Flow = NOI − New Debt Service
  DSCR = NOI ÷ New Debt Service

SCENARIOS:
  Current:    X.XX% (today's rate)
  +0.5%:      X.XX%
  +1.0%:      X.XX%
  +1.5%:      X.XX%
  +2.0%:      X.XX%

BREAK-EVEN RATE:
  The interest rate at which Cash Flow = $0
  Solve for: PMT(rate/12, term, -loan) × 12 = NOI
  
  CUSHION = Break-Even Rate − Current Rate
  If cushion < 1.5%, flag as rate-sensitive
```

### 3. Rent Decline Stress Test

```
For each rent scenario, recalculate NOI and downstream metrics:

SCENARIOS:
  Base:       0% change (current rents)
  Soft:       −5% rent decline
  Moderate:   −10% rent decline
  Severe:     −15% rent decline
  
ALSO TEST:
  0% rent growth over hold period (flat rents vs. projected 2-3% growth)
  This shows what happens if the pro forma's rent growth assumptions don't materialize.

BREAK-EVEN RENT:
  The rent level at which Cash Flow = $0
  Formula: Break-Even Rent = (OpEx + Debt Service − Other Income) ÷ (Units × 12 × (1 − Vacancy))
```

### 4. Expense Stress Test

```
SCENARIOS:
  Base:           Current projected expenses
  Insurance +20%: Common in FL, TX, coastal markets (surging 10-25%/year)
  Tax Reassess:   Property taxes at purchase price (can increase 15-30%+)
  OpEx +10%:      General expense inflation
  OpEx +15%:      Major maintenance surprise
  Combined:       Insurance +20% AND tax reassessment AND +5% other expenses

For each scenario: recalculate NOI, Cash Flow, DSCR, CoC
```

## Combined Stress Test

The most important test: combine multiple adverse conditions simultaneously.

```
COMBINED WORST-CASE SCENARIOS

Mild Stress:    10% vacancy + 0% rent growth + OpEx +5%
Moderate Stress: 12% vacancy + rates +1% + OpEx +10%
Severe Stress:  15% vacancy + rates +1.5% + rents -5% + OpEx +10%
Crisis:         20% vacancy + rates +2% + rents -10% + OpEx +15%

For each: NOI, Cash Flow, DSCR, CoC, monthly out-of-pocket required

SURVIVAL QUESTION: How many months of reserves does the investor need
to survive each scenario?
  Monthly deficit × 12 months = annual reserve requirement
```

## Output Format

### Stress Test Dashboard

```
STRESS TEST RESULTS
═══════════════════════════════════════
Property: [description] | Base NOI: $XX,XXX | Debt Service: $XX,XXX

VACANCY STRESS
Scenario     Vacancy   NOI        Cash Flow   DSCR     CoC
Base         X%        $XX,XXX    $XX,XXX     X.XXx    X.X%
Moderate     10%       $XX,XXX    $XX,XXX     X.XXx    X.X%
Stressed     15%       $XX,XXX    $XX,XXX     X.XXx    X.X%
Severe       20%       $XX,XXX    $X,XXX      X.XXx    X.X%
Crisis       25%       $XX,XXX    ($X,XXX)    0.XXx    -X.X%
→ Break-Even Vacancy: XX%  [Rating]

INTEREST RATE STRESS
Scenario     Rate      Debt Svc   Cash Flow   DSCR     CoC
Current      X.XX%     $XX,XXX    $XX,XXX     X.XXx    X.X%
+0.5%        X.XX%     $XX,XXX    $XX,XXX     X.XXx    X.X%
+1.0%        X.XX%     $XX,XXX    $XX,XXX     X.XXx    X.X%
+1.5%        X.XX%     $XX,XXX    $X,XXX      X.XXx    X.X%
+2.0%        X.XX%     $XX,XXX    ($X,XXX)    0.XXx    -X.X%
→ Break-Even Rate: X.XX%  [Rating]

RENT DECLINE STRESS
Scenario     Change    NOI        Cash Flow   DSCR     CoC
Base         0%        $XX,XXX    $XX,XXX     X.XXx    X.X%
Soft         -5%       $XX,XXX    $XX,XXX     X.XXx    X.X%
Moderate     -10%      $XX,XXX    $X,XXX      X.XXx    X.X%
Severe       -15%      $XX,XXX    ($X,XXX)    0.XXx    -X.X%

COMBINED WORST CASE
Scenario     Details                          Cash Flow   DSCR
Mild         10% vac + flat rent + OpEx +5%   $X,XXX      X.XXx
Moderate     12% vac + rate +1% + OpEx +10%   $X,XXX      X.XXx
Severe       15% vac + rate +1.5% + rent -5%  ($X,XXX)    0.XXx

RESILIENCE RATING: STRONG / ADEQUATE / WEAK / FRAGILE
[2-3 sentence summary of stress test findings and recommended reserves]
```

## Red Flag Detection Checklist

When analyzing any deal, check for these red flags and report findings:

### Financial Red Flags
- [ ] **Inflated rent roll**: In-place rents exceed market by >10%
- [ ] **Recent lease clustering**: Most leases started within last 3-6 months
- [ ] **High month-to-month**: >20% of units on month-to-month leases
- [ ] **Chronic late payments**: Late payment pattern across 10+ units
- [ ] **Income/deposit mismatch**: Bank deposits don't match reported rent roll
- [ ] **Below-market expenses**: Expense ratio significantly below benchmarks (deferred maintenance)
- [ ] **Cap rate outlier**: Cap rate far above market average (hidden risk)
- [ ] **Declining occupancy trend**: Occupancy dropping over last 12-24 months

### Physical Red Flags
- [ ] **Deferred maintenance**: Peeling paint, water stains, overgrown landscaping
- [ ] **Cosmetic masking**: Fresh paint/carpet hiding structural issues
- [ ] **Roof age**: >15 years old without replacement plan
- [ ] **HVAC age**: >12 years old, especially in extreme climate
- [ ] **Environmental**: Pre-1978 (lead paint), asbestos, mold indicators, radon
- [ ] **Foundation**: Cracks, settling, water intrusion signs
- [ ] **Unpermitted work**: Additions or modifications without building permits

### Market Red Flags
- [ ] **Pro forma rent growth >3%**: Aggressive unless market data supports it
- [ ] **Declining population/employment**: Market fundamentals weakening
- [ ] **Construction pipeline**: Large supply coming online in submarket
- [ ] **Single employer dependency**: Economy depends on one major employer
- [ ] **Flood zone / disaster risk**: Insurance costs may surge
- [ ] **Rent control risk**: Pending or likely rent regulation

### Due Diligence Document Checklist
- [ ] T-12 (trailing 12 months income/expenses) — cross-reference with bank statements
- [ ] Rent roll with lease terms, expiration dates, concessions
- [ ] Estoppel certificates from tenants
- [ ] Property Condition Assessment
- [ ] Phase I Environmental Site Assessment ($2,000–$5,000)
- [ ] Zoning verification and permit history
- [ ] Property tax reassessment modeling
- [ ] Certificate of occupancy (current)
- [ ] Insurance loss history (CLUE report)
- [ ] Utility bills (12+ months)

## Market Cycle Context

Real estate follows ~18-year cycles through four phases. Understanding where the market stands affects risk tolerance:

```
CYCLE PHASE     CHARACTERISTICS                  STRATEGY IMPLICATION
Recovery        Low occupancy, no new            Buy distressed, value-add
                construction, distressed prices
Expansion       Rising rents, falling vacancy,   Buy with moderate leverage,
                new construction starting        focus on cash flow
Hyper-Supply    Construction completing,          Be cautious, reduce leverage,
                vacancy rising, rent slowing      stress test aggressively
Recession       High vacancy, falling values,    Cash is king, buy distressed
                distressed sales                  with low/no leverage
```

Current (early 2026):
- **Office**: Recession (record vacancy ~20.5%)
- **Retail**: Expansion (near historic low vacancy)
- **Multifamily**: Late expansion / early hyper-supply (new supply delivering)
- **Industrial**: Late expansion (moderating after strong run)
- **CRE maturity wall**: ~$600B/year through 2028 → potential distressed opportunities

## Resilience Rating System

Based on combined stress test results, assign a resilience rating:

| Rating | Criteria |
|---|---|
| **STRONG** | Survives moderate stress with positive cash flow; DSCR stays >1.15x; break-even vacancy <75% |
| **ADEQUATE** | Survives mild stress; goes negative under moderate combined stress; break-even vacancy 75-82% |
| **WEAK** | Goes negative under mild-to-moderate stress; break-even vacancy 82-88%; thin DSCR cushion |
| **FRAGILE** | Goes negative under any stress scenario; break-even vacancy >88%; DSCR cushion <5% |

**Recommendation by rating:**
- STRONG → Proceed with confidence; standard reserves
- ADEQUATE → Proceed with caution; larger reserve fund (6+ months expenses + debt service)
- WEAK → Negotiate significant price reduction or improve terms; or walk away
- FRAGILE → Walk away unless you can restructure the deal fundamentally

## Monte Carlo Simulation (Advanced Stress Testing)

For sophisticated analysis — especially syndications, development deals, and high-value investments — discrete scenarios aren't enough. Monte Carlo simulation runs thousands of randomized trials across probability distributions to produce a return distribution with confidence intervals.

### When to Use Monte Carlo

- Investment exceeds $500K equity or involves passive investors
- Multiple uncertain variables interact (rent, vacancy, expenses, FX, cap rate)
- Sponsor projections need independent probabilistic validation
- User requests confidence intervals or probability of loss

### Methodology

Instead of testing fixed scenarios (vacancy at 5%, 10%, 15%), Monte Carlo assigns each variable a probability distribution and randomly samples from all distributions simultaneously for thousands of iterations.

```
MONTE CARLO VARIABLE SETUP

For each uncertain input, define:
  Variable:         [Name]
  Distribution:     [Normal / Triangular / Uniform]
  Base case:        [Most likely value]
  Min (optimistic):  [Best case]
  Max (pessimistic): [Worst case]
  
TYPICAL VARIABLE DISTRIBUTIONS:
  Occupancy:        Triangular(min=50%, mode=75%, max=92%)
  ADR Growth:       Normal(mean=2.5%, std=2.0%)
  Expense Growth:   Normal(mean=3.0%, std=1.5%)
  Exit Cap Rate:    Triangular(min=5.5%, mode=7.0%, max=9.0%)
  Rent Growth:      Normal(mean=2.5%, std=1.5%)
  Interest Rate:    Triangular(min=5.5%, mode=6.5%, max=8.5%)
  FX Change (intl): Normal(mean=-2.0%, std=5.0%)  # neg = local depreciation
```

### Python Monte Carlo Template

```python
"""
Monte Carlo Simulation for Real Estate Investment Returns
Produces: IRR distribution, probability of loss, confidence intervals
"""
import numpy as np

def monte_carlo_re(n_simulations=10000, hold_years=5):
    """Run Monte Carlo simulation on a real estate investment."""
    
    # ═══ DEAL INPUTS (modify per deal) ═══
    purchase_price = 500000
    down_payment_pct = 0.25
    closing_cost_pct = 0.03
    loan_rate = 0.065
    loan_term = 30  # amortization
    initial_noi = 40000
    
    total_cash_invested = purchase_price * (down_payment_pct + closing_cost_pct)
    loan_amount = purchase_price * (1 - down_payment_pct)
    
    # Monthly mortgage payment
    monthly_rate = loan_rate / 12
    n_payments = loan_term * 12
    monthly_pmt = loan_amount * (monthly_rate * (1 + monthly_rate)**n_payments) / \
                  ((1 + monthly_rate)**n_payments - 1)
    annual_debt_service = monthly_pmt * 12
    
    # ═══ PROBABILITY DISTRIBUTIONS ═══
    # Each simulation draws random values from these distributions
    rent_growth = np.random.normal(0.025, 0.015, (n_simulations, hold_years))
    expense_growth = np.random.normal(0.030, 0.010, (n_simulations, hold_years))
    vacancy_rates = np.random.triangular(0.03, 0.07, 0.15, (n_simulations, hold_years))
    exit_cap_rates = np.random.triangular(0.055, 0.070, 0.090, n_simulations)
    
    # ═══ RUN SIMULATIONS ═══
    irrs = []
    equity_multiples = []
    total_cash_flows = []
    
    for sim in range(n_simulations):
        cash_flows = [-total_cash_invested]  # Year 0: invest
        
        noi = initial_noi
        remaining_balance = loan_amount
        total_distributions = 0
        
        for year in range(hold_years):
            # Revenue grows by random rent growth, adjusted for random vacancy
            revenue_growth = 1 + rent_growth[sim, year]
            effective_vacancy = vacancy_rates[sim, year]
            
            # Grow NOI (revenue portion grows, expenses grow separately)
            gross_revenue = (noi / 0.55) * revenue_growth  # reverse 45% expense ratio
            expenses = (noi / 0.55 * 0.45) * (1 + expense_growth[sim, year])
            noi = gross_revenue * (1 - effective_vacancy) - expenses
            
            # Cash flow after debt service
            annual_cf = max(noi - annual_debt_service, 0)
            cash_flows.append(annual_cf)
            total_distributions += annual_cf
            
            # Amortization (simplified)
            interest_paid = remaining_balance * loan_rate
            principal_paid = annual_debt_service - interest_paid
            remaining_balance -= principal_paid
        
        # Exit: sell at exit cap rate
        sale_price = noi / exit_cap_rates[sim]
        selling_costs = sale_price * 0.05  # 5% transaction costs
        net_proceeds = sale_price - selling_costs - remaining_balance
        cash_flows[-1] += net_proceeds  # Add sale proceeds to final year
        total_distributions += net_proceeds
        
        # Calculate IRR
        try:
            irr = np.irr(cash_flows)
            if not np.isnan(irr) and -1 < irr < 2:  # filter outliers
                irrs.append(irr)
                equity_multiples.append(total_distributions / total_cash_invested)
        except:
            pass
    
    irrs = np.array(irrs)
    equity_multiples = np.array(equity_multiples)
    
    # ═══ RESULTS ═══
    results = {
        "n_valid_simulations": len(irrs),
        "irr_mean": np.mean(irrs),
        "irr_median": np.median(irrs),
        "irr_std": np.std(irrs),
        "irr_5th_percentile": np.percentile(irrs, 5),
        "irr_25th_percentile": np.percentile(irrs, 25),
        "irr_75th_percentile": np.percentile(irrs, 75),
        "irr_95th_percentile": np.percentile(irrs, 95),
        "probability_of_loss": np.mean(irrs < 0),
        "probability_below_8pct": np.mean(irrs < 0.08),
        "equity_multiple_median": np.median(equity_multiples),
        "equity_multiple_5th": np.percentile(equity_multiples, 5),
    }
    return results

# Run and display
results = monte_carlo_re(n_simulations=10000, hold_years=5)
print(f"""
MONTE CARLO RESULTS ({results['n_valid_simulations']:,} valid simulations)
═══════════════════════════════════════════════════════
IRR Distribution:
  Mean:             {results['irr_mean']:.1%}
  Median:           {results['irr_median']:.1%}
  Std Deviation:    {results['irr_std']:.1%}
  5th Percentile:   {results['irr_5th_percentile']:.1%}  (worst 5% of outcomes)
  25th Percentile:  {results['irr_25th_percentile']:.1%}
  75th Percentile:  {results['irr_75th_percentile']:.1%}
  95th Percentile:  {results['irr_95th_percentile']:.1%}  (best 5% of outcomes)

Risk Metrics:
  Probability of loss (IRR < 0%):     {results['probability_of_loss']:.1%}
  Probability below target (IRR < 8%): {results['probability_below_8pct']:.1%}

Equity Multiple:
  Median:           {results['equity_multiple_median']:.2f}x
  5th Percentile:   {results['equity_multiple_5th']:.2f}x  (worst case)
""")
```

### Interpreting Monte Carlo Results

| Metric | Good | Acceptable | Concerning |
|---|---|---|---|
| Probability of loss (IRR < 0%) | <5% | 5-15% | >15% |
| Probability below target | <25% | 25-40% | >40% |
| IRR Std Deviation | <5% | 5-10% | >10% (high uncertainty) |
| 5th Percentile IRR | >0% | -5% to 0% | < -5% |
| Median vs. Sponsor Projection | Within 2% | 2-5% below | >5% below |

### Monte Carlo for International Deals

Add FX as an additional random variable:

```python
# Add to distributions section:
fx_annual_change = np.random.normal(-0.03, 0.05, (n_simulations, hold_years))
# mean=-3% (local currency depreciation trend), std=5% (volatility)

# Apply to cash flows:
for year in range(hold_years):
    fx_factor = np.prod(1 + fx_annual_change[sim, :year+1])
    cash_flows_in_home_currency = annual_cf * fx_factor
```
