# Skill 4: Financing Analyzer

Compare loan structures, optimize leverage, and understand how financing decisions reshape investment returns. This skill answers "how should I finance this deal?" and "what happens if I change my loan terms?"

## When to Use

- User asks which loan type to use
- User wants to compare financing scenarios (e.g., 20% vs 25% down)
- User asks about DSCR loans, hard money, seller financing, etc.
- User wants to understand leverage impact on returns
- User is deciding between amortization periods (15 vs 25 vs 30 year)
- User asks about refinancing or BRRRR strategy

## Loan Product Reference

### Product Overview

| Loan Type | Rate Range | LTV | Term | Best For |
|---|---|---|---|---|
| Conventional (30yr fixed) | ~6.11% | 75–85% | 30 yr | First 1–10 investment properties |
| DSCR Loan | 5.99–7.50% | 75–80% | 30 yr | Scaling portfolios, self-employed |
| Agency (Fannie/Freddie MF) | ~5.18%+ | Up to 80% | Up to 30 yr | Stabilized multifamily 5+ units |
| Hard Money | 8–14% | 65–80% | 6–24 mo | Fix-and-flip, bridge |
| Private Money | 6–12% | Varies | 1–5 yr | Relationship-based, flexible |
| Seller Financing | 5–7% | 80–90% | 3–10 yr | Motivated sellers, creative deals |
| Commercial Bank | 5.5–7.5% | 60–75% | 5–10 yr (25yr amort) | Commercial properties |
| Bridge Loan | 7–12% | 65–80% | 12–36 mo | Transitional properties |
| FHA 203(k) | ~6.5%+ | 96.5% | 30 yr | Owner-occ rehab (house hack) |
| VA Loan | ~5.8%+ | 100% | 30 yr | Veterans, owner-occupied |
| Portfolio Loan | 6–8% | 70–80% | 5–30 yr | Non-conforming, unique properties |

### Key Qualifications

**Conventional**: 620+ credit, DTI <45%, 2 years tax returns, max 10 financed properties (Fannie)
**DSCR**: Property DSCR ≥1.0–1.25x, 680+ credit typical, no income verification, closes in LLC
**Agency**: 2+ years multifamily experience (5+ units), stabilized occupancy (90%+), non-recourse
**Hard Money**: Asset-based (property is collateral), ARV-focused, minimal borrower qualification

## Analysis Procedures

### Scenario Comparison Framework

For any financing comparison, calculate these metrics for each scenario:

```
For each loan scenario:
  1. Monthly Payment = PMT(rate/12, term_months, -loan_amount)
  2. Annual Debt Service = Monthly Payment × 12
  3. Total Cash Invested = Down Payment + Closing Costs + Loan Fees
  4. Annual Cash Flow = NOI − Annual Debt Service
  5. Cash-on-Cash Return = Cash Flow ÷ Total Cash Invested
  6. DSCR = NOI ÷ Annual Debt Service
  7. Break-Even Occupancy = (OpEx + Debt Service) ÷ Gross Income
  8. Year 1 Principal Paydown = from amortization schedule
  9. Total Interest Paid = (Monthly Payment × Total Months) − Loan Amount
  10. Loan Constant = Annual Debt Service ÷ Loan Amount
```

### Leverage Analysis

Compare all-cash vs. leveraged returns:

```
ALL-CASH SCENARIO
  Total Invested: Purchase Price + Closing Costs
  Annual Return: NOI
  CoC Return: NOI ÷ Total Invested
  No debt risk

LEVERAGED SCENARIO
  Total Invested: Down Payment + Closing Costs + Points
  Annual Return: NOI − Debt Service
  CoC Return: Cash Flow ÷ Total Invested
  
LEVERAGE IMPACT
  Cap Rate: NOI ÷ Purchase Price
  Loan Constant: Debt Service ÷ Loan Amount
  
  If Cap Rate > Loan Constant → POSITIVE leverage (debt boosts returns)
  If Cap Rate < Loan Constant → NEGATIVE leverage (debt drags returns)
  If Cap Rate = Loan Constant → NEUTRAL leverage
```

When negative leverage exists, explain that total returns can still be positive through appreciation, principal paydown, and tax benefits — but Day 1 cash flow will be thin or negative.

### Amortization Comparison

Compare 15-year, 20-year, 25-year, and 30-year amortization:

```
For a $XXX,XXX loan at X.XX%:
                    15-yr     20-yr     25-yr     30-yr
Monthly Payment     $X,XXX    $X,XXX    $X,XXX    $X,XXX
Annual Debt Svc     $XX,XXX   $XX,XXX   $XX,XXX   $XX,XXX
Total Interest      $XXX,XXX  $XXX,XXX  $XXX,XXX  $XXX,XXX
Year 1 Principal    $XX,XXX   $XX,XXX   $XX,XXX   $XX,XXX
Cash Flow Impact    $X,XXX    $X,XXX    $X,XXX    $X,XXX
DSCR               X.XXx     X.XXx     X.XXx     X.XXx
```

### Interest-Only Analysis

```
I/O Payment = Loan Amount × Annual Rate ÷ 12
Fully Amortizing = PMT(rate/12, term_months, -loan_amount)
Monthly Savings = Fully Amortizing − I/O Payment
Cash Flow Boost = Monthly Savings × 12 per year

TRADEOFF:
  ✓ Lower payments during I/O period
  ✓ Higher cash-on-cash during renovation/lease-up
  ✗ Zero principal paydown (no equity buildup)
  ✗ Full balance due at maturity
  ✗ Higher total interest cost over life of loan
```

### Refinance / BRRRR Analysis

```
BRRRR ANALYSIS
  Original Investment:
    Purchase:           $XXX,XXX
    Rehab:              $XX,XXX
    Closing + Holding:  $XX,XXX
    Total Basis:        $XXX,XXX

  After Renovation:
    Appraised Value:    $XXX,XXX
    Max LTV (75%):      $XXX,XXX
    New Loan Amount:    $XXX,XXX
    
  Cash Recaptured:
    New Loan:           $XXX,XXX
    Less: Original Loan: ($XXX,XXX)
    Cash Back:          $XX,XXX
    
  Money Left in Deal:
    Total Invested:     $XXX,XXX
    Cash Recaptured:    ($XX,XXX)
    Net Equity Trapped: $XX,XXX
    
  New Cash Flow (post-refi):
    NOI:                $XX,XXX
    New Debt Service:   ($XX,XXX)
    Annual Cash Flow:   $XX,XXX
    CoC on Trapped Equity: XX.X%
    
  INFINITE RETURN? If Cash Recaptured ≥ Total Invested → Yes
```

## Output Format

### Side-by-Side Comparison

```
FINANCING COMPARISON
═══════════════════════════════════════
Property NOI: $XX,XXX | Purchase Price: $XXX,XXX

                        Option A          Option B          Option C
Loan Type               Conventional      DSCR              Seller Finance
Rate                    X.XX%             X.XX%             X.XX%
LTV / Down              XX% / $XX,XXX     XX% / $XX,XXX     XX% / $XX,XXX
Term / Amort            30/30             30/30             10/25
Monthly Payment         $X,XXX            $X,XXX            $X,XXX
Points/Fees             $X,XXX            $X,XXX            $X,XXX
Total Cash Required     $XX,XXX           $XX,XXX           $XX,XXX

RETURNS
Cash-on-Cash            X.XX%             X.XX%             X.XX%
DSCR                    X.XXx             X.XXx             X.XXx
Break-Even Occ.         XX%               XX%               XX%
Yr 1 Principal Paydown  $X,XXX            $X,XXX            $X,XXX
Total Interest (life)   $XXX,XXX          $XXX,XXX          $XXX,XXX

VERDICT                 [analysis]        [analysis]        [analysis]

RECOMMENDATION: [Which option and why]
```

## Optimal Leverage Guidelines

| Strategy | Recommended LTV | Rationale |
|---|---|---|
| Buy-and-hold rental | 70–80% | Balance cash flow with leverage benefits |
| Value-add | 65–75% | Room for cost overruns, renovation period |
| Fix-and-flip | 65–70% of ARV | Hard money based on exit value |
| Commercial stabilized | 60–70% | Conservative; balloon risk mitigation |
| Development | 60–65% of total cost | High risk requires more equity |

Flag when proposed leverage exceeds these ranges and explain the increased risk.

## Cross-Border & International Financing

When the investment property is outside the investor's home country, traditional financing becomes significantly more constrained. In most international markets (Bali, Mexico, Southeast Asia), 90-99% of foreign acquisitions are completed as cash transactions. However, several strategies exist to access capital:

### Funding Sources for International Purchases

| Strategy | Mechanism | Typical Terms | Best For |
|---|---|---|---|
| Home Country HELOC | Draw equity from primary residence to become "cash" buyer abroad | Variable rate, 10-20yr draw | US/Canadian investors with home equity; better negotiation power |
| Developer Financing | Developer acts as lender for pre-construction purchases | 5-10yr, higher rates (8-12%), 40-60% down | Pre-construction in markets with limited bank financing |
| Cross-Border Lenders | Specialized lenders (MoXi, Global Mortgage Group) using home-country credit | 30-40% down, 700+ credit, USD-denominated | US/Canadian citizens buying in Mexico |
| Self-Directed IRA/SDIRA | Purchase foreign real estate through self-directed retirement account | Complex compliance, no personal use | Tax-advantaged investors with retirement funds |
| Cash-Out Refinance | Refinance existing domestic properties to extract capital | Domestic rates, 75-80% LTV | Investors with domestic portfolio equity |

### Indonesia-Specific Financing

| Product | Provider Type | Requirements | Terms |
|---|---|---|---|
| KPR (Property Loan) for foreigners | Banks (Commonwealth, Permata) | KITAS/KITAP residency permit, min net income IDR 25M/month | 30-50% down, 10-15yr, IDR-denominated (8-12%) |
| PT PMA Corporate Loan | Indonesian banks under OJK regulation | Established PT PMA with operating history | Corporate rates, requires collateral + business plan |
| Fintech Solutions | Platforms (e.g., Briix) | Varies; digital processing, more streamlined | Higher rates but faster approval and transparency |

**Key constraints in Indonesia**: No mortgage interest deduction for foreign investors. IDR-denominated loans carry currency risk (if revenue is also IDR, this provides a natural hedge). Bank appraisals in Indonesia are typically conservative (60-70% of market value).

### Mexico-Specific Financing

| Product | Provider Type | Requirements | Terms |
|---|---|---|---|
| Cross-Border Mortgage (USD) | MoXi, Global Mortgage Group | US/Canadian citizen, 700+ credit, US income docs | 30-40% down, 15-30yr, USD-denominated |
| Developer Financing | Direct from developer | Purchase agreement + down payment | 5-10yr, 8-12%, often interest-only during construction |
| Mexican Bank Mortgage | Scotiabank, HSBC Mexico | Mexican residency (temporary or permanent), credit history in Mexico | 20-30% down, 15-20yr, MXN-denominated (10-14%) |

**Key constraints in Mexico**: Fideicomiso properties can be used as collateral for cross-border lenders but not all Mexican banks accept them. No mortgage interest deduction for non-residents. Approximately 99% of foreign acquisitions are cash.

### International Financing Decision Framework

```
CROSS-BORDER FINANCING ANALYSIS
  Property Location:        [Country]
  Investor Home Country:    [Country]
  
  LOCAL FINANCING AVAILABLE?
    Bank mortgage for foreigners:    [Yes/No] → Terms: ___
    Developer financing available:   [Yes/No] → Terms: ___
    Cross-border lender available:   [Yes/No] → Terms: ___
    
  HOME COUNTRY OPTIONS:
    HELOC available on domestic property: [Yes/No] → Amount: ___
    Cash-out refi on domestic portfolio:  [Yes/No] → Amount: ___
    SDIRA eligible:                       [Yes/No]
    
  CURRENCY MISMATCH:
    Loan currency:           [USD/EUR/local]
    Revenue currency:        [USD/EUR/local]
    Mismatch risk:           [Low if matched / High if different]
    
  RECOMMENDATION: [All-cash / Home-country leverage / Local financing / Developer terms]
  RATIONALE: [Based on rate differential, FX risk, tax implications]
```
