# Skill 1: Deal Screener

Rapidly filter investment properties using rule-of-thumb tests. This is the first step in any analysis — it takes 30 seconds and tells the investor whether a deal deserves deeper underwriting.

## When to Use

- User shares a property listing with price and rent
- User asks "is this worth looking at?" or "quick analysis"
- User wants to compare multiple properties side by side
- Before diving into full underwriting (always screen first)

## Required Inputs

| Input | Required? | Notes |
|---|---|---|
| Purchase price | Yes | Ask price or target offer |
| Monthly rent (or rent estimate) | Yes | Per unit if multifamily |
| Number of units | Yes | Default: 1 for SFR |
| Property type | Helpful | SFR, duplex, MF, commercial |
| Market/location | Helpful | For context on benchmark expectations |

## Screening Tests to Run

### Test 1: The 1% Rule
```
Monthly Rent ÷ Purchase Price ≥ 1.0%
```
- **Pass** (≥1.0%): Likely positive cash flow, proceed to underwriting
- **Marginal** (0.7–0.99%): May work with low expenses, favorable financing, or strong appreciation market
- **Fail** (<0.7%): Unlikely to cash flow; only viable in high-appreciation markets with tax benefits

Context: The 1% rule is achievable in Midwest markets (Cleveland, Indianapolis, Memphis, Kansas City) but rarely in coastal/Sun Belt metros. Failing the 1% rule doesn't kill a deal — it means the investment thesis must rely on appreciation, tax benefits, or below-market acquisition.

### Test 2: The 2% Rule
```
Monthly Rent ÷ Purchase Price ≥ 2.0%
```
- **Pass**: Exceptional cash flow — but verify the neighborhood, tenant quality, and condition
- Properties meeting the 2% rule often come with elevated vacancy, turnover, and maintenance costs

### Test 3: Gross Rent Multiplier (GRM)
```
GRM = Purchase Price ÷ Annual Gross Rent
```
- **Excellent**: 4–5
- **Good**: 5–7
- **Acceptable**: 8–10
- **Expensive**: 12+ (appreciation market, minimal cash flow)

### Test 4: The 50% Rule (Quick Cash Flow Estimate)
```
Estimated Monthly Cash Flow = (Monthly Rent × 0.50) − Monthly Mortgage Payment
```
- Positive result → likely cash flows after expenses and debt service
- Negative result → needs careful expense analysis; may still work if actual expenses are below 50%

### Test 5: Cap Rate Quick Check (if NOI known or estimable)
```
Estimated NOI = Annual Rent × (1 − vacancy) × (1 − expense ratio)
Cap Rate = Estimated NOI ÷ Purchase Price
```
Compare to current benchmarks:
- Multifamily: 3.9–7.6% (avg 5.9%)
- Industrial: 5.2–7.7% (avg 6.4%)
- Retail: 5.0–9.1% (avg 6.7%)
- Office: 4.6–10.5% (avg 7.4%)

Flag if cap rate < current borrowing cost (~6.1–6.5%) → negative leverage situation.

### Test 6: 70% Rule (Flips Only)
```
Max Purchase = (ARV × 70%) − Repair Costs
```
If the asking price exceeds this, the flip margin is too thin unless you're very experienced.

## Output Format

Present results as a clear scorecard:

```
DEAL SCREENING SCORECARD
═══════════════════════════════════════
Property: [address or description]
Price: $XXX,XXX | Rent: $X,XXX/mo | Units: X

TEST                  RESULT    VERDICT
──────────────────────────────────────
1% Rule               X.XX%    ✓ PASS / ✗ FAIL
2% Rule               X.XX%    ✓ PASS / ✗ FAIL
GRM                   X.X      Good / Acceptable / Expensive
50% Rule Cash Flow    $XXX/mo  Positive / Negative
Est. Cap Rate         X.X%     vs. X.X% benchmark
Cap Rate vs Debt      +/-Xbps  Positive / Negative leverage

OVERALL: PROCEED TO UNDERWRITING / MARGINAL — DIG DEEPER / PASS
```

## Interpretation Guidance

- **3+ tests pass**: Strong candidate, proceed to full underwriting
- **1–2 tests pass**: Marginal deal; could work with value-add strategy, creative financing, or strong appreciation thesis
- **0 tests pass**: Almost certainly a bad deal at this price — either negotiate significantly or walk away
- **All tests pass with flying colors**: Be skeptical — very high returns often indicate hidden risk (deferred maintenance, bad location, tenant problems). Investigate before celebrating.

## For Multi-Property Comparison

When comparing multiple deals, create a side-by-side table:

```
PROPERTY COMPARISON
                    Property A    Property B    Property C
Price               $XXX,XXX      $XXX,XXX      $XXX,XXX
Rent/mo             $X,XXX        $X,XXX        $X,XXX
Units               X             X             X
1% Rule             X.XX%         X.XX%         X.XX%
GRM                 X.X           X.X           X.X
50% Est. CF/mo      $XXX          $XXX          $XXX
Est. Cap Rate       X.X%          X.X%          X.X%
VERDICT             ✓/✗           ✓/✗           ✓/✗
```

## Quick Calculator Code Templates

When users want spreadsheet-ready or programmable calculations:

### JavaScript Quick Screen Calculator

```javascript
function screenDeal(price, monthlyRent, units = 1) {
  const annualRent = monthlyRent * 12;
  const pctRule = monthlyRent / price;
  const grm = price / annualRent;
  const estExpenses = annualRent * 0.50;  // 50% rule
  const estNOI = annualRent - estExpenses;
  const estCapRate = estNOI / price;
  const cashFlowPerDoor = (estNOI / 12) / units;
  
  return {
    price, monthlyRent, units,
    pctRule: (pctRule * 100).toFixed(2) + "%",
    passes1Pct: pctRule >= 0.01,
    grm: grm.toFixed(1),
    passesGRM: grm <= 8.33,
    estNOI: estNOI.toFixed(0),
    estCapRate: (estCapRate * 100).toFixed(1) + "%",
    cashFlowPerDoor: "$" + cashFlowPerDoor.toFixed(0) + "/mo",
    verdict: pctRule >= 0.01 && grm <= 8.33 ? "PASS" : "FAIL"
  };
}

// Example: 4-unit building, $320K, each unit rents for $900/mo
console.table(screenDeal(320000, 3600, 4));
```

### Python Quick Analysis

```python
def quick_screen(price, monthly_rent, units=1):
    """Quick screen a property using 1%, 50%, GRM rules"""
    annual_rent = monthly_rent * 12
    pct_rule = monthly_rent / price
    grm = price / annual_rent
    est_noi = annual_rent * 0.50
    est_cap_rate = est_noi / price
    cf_per_door = (est_noi / 12) / units
    
    print(f"{'='*40}")
    print(f"Price: ${price:,.0f} | Rent: ${monthly_rent:,.0f}/mo | Units: {units}")
    print(f"1% Rule: {pct_rule:.2%} {'✓' if pct_rule >= 0.01 else '✗'}")
    print(f"GRM: {grm:.1f} {'✓' if grm <= 8.33 else '✗'}")
    print(f"Est. Cap Rate: {est_cap_rate:.1%}")
    print(f"CF/Door: ${cf_per_door:,.0f}/mo")
    print(f"VERDICT: {'PASS ✓' if pct_rule >= 0.01 and grm <= 8.33 else 'FAIL ✗'}")
    return {"pct_rule": pct_rule, "grm": grm, "cap_rate": est_cap_rate, "cf_per_door": cf_per_door}
```
