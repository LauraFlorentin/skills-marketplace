# Financial Modeling — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

## Contents

- [Sensitivity Analysis](#sensitivity-analysis)
- [Common Financial Models for Consulting](#common-financial-models-for-consulting)
- [Model Quality Standards](#model-quality-standards)
- [Presenting Financial Analysis](#presenting-financial-analysis)
- [Financial Modeling Deliverables](#financial-modeling-deliverables)

---

## Sensitivity Analysis

**Goal:** Understand which assumptions have the biggest impact on financial results. Pressure-test the model.

### One-Way Sensitivity Table

Vary one assumption at a time; see how NPV changes.

**Example: System Order Processing ROI Model**

Base case assumptions:
- Implementation cost: $520K
- Discount rate: 10%
- Labor savings: $350K/year (Year 2+)
- Volume growth impact: 20% additional orders, $100/order margin

**One-way sensitivity: Vary discount rate**

| Discount Rate | NPV |
|---|---|
| 5% | $2,847K |
| 8% | $2,456K |
| **10% (base)** | **$2,123K** |
| 12% | $1,823K |
| 15% | $1,451K |

**Interpretation:** NPV decreases as discount rate increases, but remains positive even at 15%. Investment is robust to discount rate assumptions.

**One-way sensitivity: Vary implementation cost**

| Implementation Cost | NPV |
|---|---|
| $400K | $2,343K |
| $460K | $2,233K |
| **$520K (base)** | **$2,123K** |
| $600K | $1,973K |
| $700K | $1,773K |

**One-way sensitivity: Vary Year 2+ labor savings**

| Annual Labor Savings | NPV |
|---|---|
| $250K | $1,456K |
| $300K | $1,789K |
| **$350K (base)** | **$2,123K** |
| $400K | $2,456K |
| $450K | $2,789K |

**Key insight:** NPV is most sensitive to labor savings assumption. If labor savings < $300K, NPV drops significantly.

### Tornado Diagram

Visualize which assumptions have largest impact on NPV.

1. Calculate one-way sensitivity for all key assumptions
2. Rank by impact size (largest to smallest)
3. Plot as horizontal bars (wider bar = larger impact)

```
Impact on NPV (from base case of $2,123K)

Volume growth impact ████████████████████ ±$890K
Labor savings ███████████████ ±$667K
Discount rate ██████████ ±$672K
Implementation cost ███████ ±$370K
System ongoing costs ███ ±$185K
```

**Interpretation:**
- Top 3 assumptions drive most of NPV variation
- Focus financial due diligence on these (labor savings, volume growth, discount rate)
- Less critical to refine bottom assumptions

### Scenario Analysis

Define 3 scenarios: Best, Base, Worst case. Assign probability to each.

**Scenario: System implementation delays by 6 months**

| Scenario | Probability | Impact | NPV |
|---|---|---|---|
| **Best Case** | 20% | Implementation on time; full benefits Year 2 | $2,500K |
| **Base Case** | 60% | Implementation 2-month delay; benefits from mid-Year 2 | $2,123K |
| **Worst Case** | 20% | Implementation 6-month delay + lower adoption (80% vs. 100%) | $1,400K |

**Expected Value = (0.20 × $2,500K) + (0.60 × $2,123K) + (0.20 × $1,400K) = $2,029K**

**Scenario: Volume growth assumptions don't materialize**

| Scenario | Probability | Assumption | NPV |
|---|---|---|---|
| **Base** | 60% | 20% volume growth enabled by faster processing | $2,123K |
| **Conservative** | 30% | 10% volume growth | $1,600K |
| **Aggressive** | 10% | 30% volume growth | $2,800K |

**Expected Value = (0.30 × $1,600K) + (0.60 × $2,123K) + (0.10 × $2,800K) = $1,994K**

**3-scenario approach for decision-making:**
- Present all 3 scenarios to leadership
- Clearly state probability and assumptions
- Use base case for primary decision
- Call out worst-case (can we live with it?)
- Mention upside without relying on it

---

## Common Financial Models for Consulting

### 1. Cost Reduction Business Case

**Scenario:** Company wants to consolidate suppliers, reduce overhead, or improve process efficiency.

**Structure:**

| Benefit | Mechanism | Year 1 | Year 2+ |
|---------|-----------|--------|---------|
| **Head Count Reduction** | Eliminate 3 FTE through attrition/retraining | $50K (partial) | $300K (full 3 × $100K loaded) |
| **Supplier Consolidation** | Reduce supplier count 20→5; leverage volume discounts | $100K | $200K |
| **Process Efficiency** | Reduce cycle time; eliminate manual steps | $80K | $150K |
| **System Consolidation** | Eliminate 2 legacy systems | $0 | $100K |
| **Total Benefits** | | $230K | $750K |
| **Implementation Cost** | Project management, training, systems | ($200K) | — |
| **Ongoing Cost** | New system license/support | ($50K) | ($50K) |
| **Net Benefit** | | ($20K) | $700K |

**Key risks:**
- Head count reduction takes longer than planned
- Supplier won't agree to consolidation terms
- System implementation delays benefit realization

### 2. Technology Investment ROI

**Scenario:** Company invests in new system, tool, or platform.

**Structure:**

| Metric | Year 1 | Year 2 | Year 3+ |
|--------|--------|--------|---------|
| **Software Cost** | ($300K) | ($120K) | ($120K) |
| **Implementation/Services** | ($250K) | — | — |
| **Training/Change Mgmt** | ($100K) | ($20K) | ($20K) |
| **Labor Efficiency Savings** | $50K | $200K | $200K |
| **Data Quality Improvement** | $0 | $150K | $150K |
| **Decision Speed (revenue)** | $0 | $100K | $200K |
| **Total Cost** | ($650K) | ($140K) | ($140K) |
| **Total Benefit** | $50K | $450K | $550K |
| **Net** | ($600K) | $310K | $410K |

**Key assumptions to validate:**
- Labor efficiency: How many hours saved per day? What's loaded cost?
- Data quality: How does it translate to economic benefit?
- Decision speed: How much revenue uplift from faster insights?

### 3. Organizational Restructuring Savings

**Scenario:** Company wants to flatten org, reduce spans of control, consolidate functions.

**Structure:**

| Impact | Calculation | Benefit |
|--------|-----------|---------|
| **Eliminate layer** | Remove 1 director + 1 manager level = 2 FTE | $200K (loaded cost) |
| **Increase span of control** | Manager supervises 8 instead of 6; eliminate 3 supervisors | $180K (3 × $60K) |
| **Consolidate functions** | Consolidate HR into shared services; save 2 FTE | $150K |
| **Reduce centralized overhead** | Finance consolidation, shared IT support | $100K |
| **Total Annual Savings** | | $630K |
| **Implementation cost** | Severance, consulting, systems changes | ($200K) |
| **Ongoing cost** | No additional cost | — |
| **Net Year 1** | | $430K |
| **Payback** | < 4 months | |

**Key risks:**
- Severance costs higher than estimated
- Consolidation takes longer (benefit delayed)
- Employee attrition/morale impacts (hard to quantify)
- Manager effectiveness lower with larger spans

### 4. Market Entry Financial Model

**Scenario:** Company enters new market, launches new product, or enters new geography.

**Structure:**

| Year | Revenue | Cost of Goods | Gross Profit | OpEx | EBIT | Cumulative |
|------|---------|---------------|--------------|------|------|-----------|
| **Year 1** | $2M | ($800K) | $1.2M | ($1.5M) | ($300K) | ($300K) |
| **Year 2** | $4M | ($1.2M) | $2.8M | ($1.8M) | $1.0M | $700K |
| **Year 3** | $7M | ($2.1M) | $4.9M | ($2.0M) | $2.9M | $3.6M |
| **Year 4** | $10M | ($3.0M) | $7.0M | ($2.2M) | $4.8M | $8.4M |
| **Year 5** | $12M | ($3.6M) | $8.4M | ($2.4M) | $6.0M | $14.4M |

**Key assumptions:**
- Revenue ramp (Year 1: build market awareness; Year 2-3: growth; Year 4+: mature)
- Margin profile (gross margin improves with scale)
- OpEx (fixed + variable; invest upfront, then leverage)
- Break-even point (when do you turn EBIT positive?)

**NPV with 12% discount rate: $8.2M**

### 5. M&A Synergy Model

**Scenario:** Company acquires another company; realizes cost synergies and revenue synergies.

**Structure:**

| Synergy Type | Mechanism | Year 1 | Year 2 | Year 3+ |
|---|---|---|---|---|
| **Cost of Goods Savings** | Procurement leverage, manufacturing consolidation | $2M | $4M | $5M |
| **Overhead Consolidation** | Eliminate duplicate functions (finance, HR, IT) | $1M | $3M | $3M |
| **Revenue Synergies** | Cross-sell, broader customer base | $0 | $2M | $5M |
| **One-time Costs** | Integration, severance, systems | ($5M) | ($1M) | — |
| **Net Synergy** | | ($2M) | $8M | $13M |

**Key risks:**
- Integration takes longer than planned
- Cost synergies don't materialize (retention, complexity)
- Revenue synergies overstated (customers don't cross-buy)
- Cultural integration issues

---

## Model Quality Standards

### Documentation

Every model should include:

1. **Cover page/summary:**
   - Business case title
   - Key outputs (NPV, IRR, Payback)
   - Scenario summary (best/base/worst)
   - Executive summary (2-3 paragraphs)

2. **Assumption log:**
   - Every assumption used in model
   - Source/justification for assumption
   - What was validated with client/market data?
   - What was estimated/judgment call?

   **Example assumption log:**

   | Category | Assumption | Value | Source | Confidence |
   |---|---|---|---|---|
   | Implementation | Project duration | 6 months | Client feedback + historical data | High |
   | Implementation | Implementation cost | $520K | Vendor quote + 15% contingency | High |
   | Labor | Loaded labor cost | $100K/FTE | HR provided | High |
   | Labor | FTE reduction | 3 FTE | Process analysis | Medium |
   | Revenue | Volume growth %age | 20% | Sales forecast | Medium |
   | Revenue | Margin per order | $100 | Historical data | High |
   | Discount | Discount rate | 10% | Company standard | High |

3. **Calculation detail:**
   - Show formulas, not just results
   - Break complex calculations into steps
   - Call out any simplifications

4. **Audit trail:**
   - Version history (who, when, what changed)
   - For complex models, track input changes
   - Comments on key cells explaining logic

### Error Checking

Before presenting model:

1. **Sanity checks:**
   - Does NPV pass the smell test? (Is it reasonable given investment size?)
   - Do costs/benefits make sense? (Compare to budget, revenue size)
   - Is payback reasonable? (2-3 years typical for corporate projects)

2. **Sensitivity validation:**
   - If you change an assumption 10%, does NPV change reasonably?
   - If sensitivity changes are wildly off, there's likely a model error

3. **Formula audit:**
   - Spot-check 5-10 key formulas
   - Check for circular references
   - Ensure consistent discount rate application

4. **Scenario validation:**
   - Run best/base/worst scenarios
   - Do the results make intuitive sense?
   - Is the range realistic?

### Version Control

- Use file naming: "OrderSystem_BusinessCase_v3.0_Final.xlsx"
- Track version in model cover page
- Comment on what changed in each version
- Archive old versions

---

## Presenting Financial Analysis

### Simplifying for Executives

**Don't do this:**
- Dump 50-sheet Excel model on executives
- Explain NPV calculation formula
- Show all sensitivity tables

**Do this:**
- One-page executive summary with key numbers
- 3-5 key financial charts
- Scenario summary (best/base/worst)
- Top 3 risks + mitigations

**Key metrics to present:**
- Total Net Benefit (3-5 year period)
- Payback period (in months)
- NPV (or IRR)
- Best/base/worst scenario range

### Handling Uncertainty Honestly

**Avoid:**
- False precision: "NPV is $2,123,456" (looks overly confident)
- Hiding assumptions: Present assumptions clearly
- Over-relying on soft benefits: "This will improve employee morale, which will drive 10% productivity gain" (hard to substantiate)

**Better:**
- Round to meaningful precision: "NPV is approximately $2.1M"
- Transparent assumptions: "This model assumes 20% volume growth enabled by faster processing; sensitivity shows NPV ranges $1.6M-$2.8M depending on growth realization"
- Scenario ranges: "Base case NPV is $2.1M; in worst-case scenario (delayed implementation + lower adoption), NPV is $1.4M. We believe this investment is justified across scenarios."

### Addressing Skepticism

**If executive challenges cost savings:**
- "We estimated 3 FTE savings based on process analysis and benchmarking. We're assuming phased reduction through attrition over 18 months. If savings take longer to realize, payback extends to 2.5 years instead of 1.8 years."

**If executive questions revenue assumptions:**
- "Volume growth assumption is conservative vs. sales forecast. If sales achieves even 10% of their 30% growth projection through faster order processing, NPV improves to $2.5M. We're using 20% (two-thirds of their projection) as a middle ground."

**If executive focuses on worst case:**
- "Worst-case NPV is $1.4M with 15% payback period. Even if key assumptions don't materialize, investment remains positive. Key risk mitigation: detailed project governance, phased implementation allowing adjustment, and conservative benefit assumptions."

---

## Financial Modeling Deliverables

### Template 1: One-Page Business Case Summary

```
BUSINESS CASE SUMMARY: Order-to-Cash System Implementation
Date: March 25, 2024
Prepared by: [Consulting firm]

EXECUTIVE SUMMARY

Problem Statement:
Current order processing takes 3 days and costs $200K annually in manual labor and exception handling.
Growth plans (25% volume increase) are constrained by manual process. We need to reduce cycle time
to <4 hours and automate exception handling while supporting growth.

Recommended Option:
Implement cloud-native order management system (Salesforce OMS) to automate order-to-cash process,
eliminate manual exceptions, and enable faster processing and scalability.

Financial Summary (5-year NPV at 10% discount rate):
- Total Net Benefit: $2.1M
- Payback Period: 1.8 years
- Internal Rate of Return: 68%
- Initial Investment: $520K (Year 1)

KEY METRICS
Total Investment (Year 1): $520K
Ongoing Annual Costs (Year 2+): $205K
Annual Benefits (steady state): $1M+

SCENARIO ANALYSIS
Scenario | Probability | 5-Yr NPV | Key Assumptions
Base Case | 60% | $2.1M | 20% volume growth, $350K labor savings, 6-month implementation
Aggressive | 20% | $2.8M | 30% volume growth, $450K labor savings
Conservative | 20% | $1.4M | 10% volume growth, 8-month implementation delay

PAYBACK ANALYSIS
Year 1: Investment ($620K)
Year 2: Benefits exceed cumulative costs; payback achieved by mid-year 2
Time to payback: 18 months (strong payoff for most organizations)

KEY BENEFITS (Steady State, Year 2+)
1. Labor Efficiency (40% → 15% time on exceptions): $350K/year
2. System Consolidation (eliminate 2 legacy systems): $90K/year
3. Operational Efficiency (cycle time reduction): $200K/year
4. Revenue Growth (20% volume enabled by faster processing): $300K+/year
Total: $940K+/year

KEY COSTS (Steady State, Year 2+)
Software/License: $120K/year
Infrastructure: $40K/year
Maintenance: $30K/year
Training (new hires): $15K/year
Total: $205K/year

TOP RISKS & MITIGATIONS
Risk | Impact | Probability | Mitigation
Implementation delay | 6-month slip → 12-month payback | 30% | Detailed project governance; experienced implementation partner; phased approach
Lower labor savings realization | Savings $250K vs. $350K → NPV drops | 25% | Detailed process redesign; change management investment; performance tracking
Adoption below 100% | Benefits flow more slowly | 20% | Executive sponsorship; training investment; change communication; incentive alignment
Lower volume growth | Revenue benefit doesn't materialize | 30% | Monitor actual growth; decision gate at Year 2 to adjust roadmap

RECOMMENDATION
Proceed with implementation. Strong financial case across scenarios. Payback within 2 years supports investment decision.
Key success factors: Executive sponsorship, change management, benefit realization tracking.

NEXT STEPS
1. Approve investment ($520K Year 1 budget)
2. Issue RFP to system vendors (target selection by April 30)
3. Establish program governance and benefit realization team
4. Begin change management and stakeholder engagement
5. Monthly steering committee reviews (tracking to plan, risk management)
```

### Template 2: Detailed NPV Model (Excel structure)

```
SHEET 1: SUMMARY

Key Outputs:
- NPV (10% discount rate): $2,123K
- IRR: 68%
- Payback Period: 1.84 years

Scenario Comparison:
Base Case NPV: $2,123K
Best Case NPV: $2,500K
Worst Case NPV: $1,400K

SHEET 2: ASSUMPTIONS

[Table showing all assumptions with sources]
Category | Assumption | Value | Source | Confidence | Notes
Implementation | Duration (months) | 6 | Client project plan | High |
Implementation | Total cost | $520K | Vendor quotes + internal estimate | High | Includes 15% contingency
Personnel | Loaded labor cost/FTE | $100K | HR data | High | Includes salary + benefits + overhead
Personnel | FTE reduction target | 3 | Process analysis | Medium | Through attrition, 18-month timeline
Personnel | Implementation start | Q2 2024 | Project plan | High |
Revenue | Volume growth % | 20% | Sales forecast | Medium | Conservative vs. sales ask (30%)
Revenue | Margin per order | $100 | Historical data | High |
Financial | Discount rate | 10% | Corporate standard | High |
Financial | Analysis period | 5 years | Standard for IT investments | High |

SHEET 3: DETAILED FINANCIALS (5-year projection)

Year | Year 1 | Year 2 | Year 3 | Year 4 | Year 5
---|---|---|---|---|---
COSTS:
Software/License | ($300K) | ($120K) | ($120K) | ($120K) | ($120K)
Implementation | ($250K) | — | — | — | —
Infrastructure | ($80K) | ($40K) | ($40K) | ($40K) | ($40K)
Data migration | ($40K) | — | — | — | —
Training delivery | ($50K) | ($15K) | ($15K) | ($15K) | ($15K)
Change management | ($70K) | — | — | — | —
Contingency (15%) | ($78K) | — | — | — | —
Total Costs | ($868K) | ($175K) | ($175K) | ($175K) | ($175K)

BENEFITS:
Labor efficiency | $50K | $350K | $350K | $350K | $350K
System consolidation | — | $90K | $90K | $90K | $90K
Process efficiency | — | $200K | $200K | $200K | $200K
Revenue (volume growth) | — | $300K | $600K | $600K | $600K
Total Benefits | $50K | $940K | $1,240K | $1,240K | $1,240K

NET CASH FLOW | ($818K) | $765K | $1,065K | $1,065K | $1,065K

Discount Factor (10%) | 1.000 | 0.909 | 0.826 | 0.751 | 0.683
Present Value | ($818K) | $695K | $880K | $801K | $728K

CUMULATIVE (undiscounted) | ($818K) | ($53K) | $1,012K | $2,077K | $3,142K
CUMULATIVE (discounted) | ($818K) | ($123K) | $757K | $1,558K | $2,286K

NPV = $2,286K (rounded to $2,123K after final calculations)
Payback Period = 1.84 years (early Year 2)

SHEET 4: SENSITIVITY ANALYSIS

One-way sensitivity (NPV impact):
[Table showing NPV for ±10%, ±20% changes to key assumptions]

Discount Rate Sensitivity:
5% → NPV $2.8M
10% → NPV $2.1M (base)
15% → NPV $1.5M

Labor Savings Sensitivity:
$250K → NPV $1.5M
$350K → NPV $2.1M (base)
$450K → NPV $2.8M

Volume Growth Impact Sensitivity:
10% growth → NPV $1.6M
20% growth → NPV $2.1M (base)
30% growth → NPV $2.8M

Implementation Cost Sensitivity:
$400K → NPV $2.3M
$520K → NPV $2.1M (base)
$650K → NPV $2.0M

SHEET 5: SCENARIO ANALYSIS

Best Case (20% probability):
- Implementation on schedule
- Full 3 FTE labor savings realized
- 30% volume growth achieves
- 5-Year NPV: $2.8M

Base Case (60% probability):
- 2-month implementation delay
- 3 FTE labor savings, delayed by 6 months
- 20% volume growth
- 5-Year NPV: $2.1M

Worst Case (20% probability):
- 6-month implementation delay
- 2 FTE labor savings realized
- 10% volume growth
- 5-Year NPV: $1.4M

Expected Value: (0.20 × $2.8M) + (0.60 × $2.1M) + (0.20 × $1.4M) = $2.0M
```

### Template 3: Sensitivity Chart (for presentations)

```
NPV Sensitivity to Key Assumptions
(Base Case: $2,123K)

TORNADO DIAGRAM

Revenue Growth Impact ████████████ ±$850K
Labor Savings Assumption ██████████ ±$667K
Discount Rate ██████████ ±$672K
Implementation Cost ███████ ±$370K
System Ongoing Costs ████ ±$185K

Interpretation:
- Top 3 assumptions account for ~85% of NPV variation
- Revenue growth and labor savings are most critical
- Model is relatively robust to cost assumptions
- Recommend detailed validation of labor/revenue assumptions
```

---

**Key Principles for Financial Modeling:**
- **Start with the business case, not the spreadsheet:** Understand problem, options, and recommendation first; model validates it
- **Build in transparency:** Document assumptions; show calculation logic; acknowledge uncertainty
- **Validate with reality:** Pressure-test assumptions with client data, benchmarks, or expert input
- **Focus on drivers:** Identify which assumptions matter most; spend analysis effort there
- **Present with confidence but humility:** This model is your best estimate, not a forecast; acknowledge what could be wrong
- **Use scenarios, not point estimates:** Range of outcomes better than single "expected" number
- **Payback matters for credibility:** Even strong NPV is more believable with reasonable payback period
