# Skill 7: Syndication & Fund Analyzer

Evaluate passive real estate investment structures including SPVs, syndications, private equity funds, DSTs, and fractional ownership deals. These investments are fundamentally different from direct property ownership — the investor is buying into a **structure** managed by others, so the analysis shifts from property metrics to **sponsor quality, fee drag, alignment of interests, and structural protections**.

## When to Use

- User receives a Private Placement Memorandum (PPM), prospectus, or investment deck
- User is evaluating a syndication, SPV, fund, or fractional ownership deal
- User asks about GP/LP structures, waterfall distributions, preferred returns
- User mentions Class A/B shares, carried interest, management fees in a fund context
- Deal involves a sponsor/operator managing the asset on behalf of passive investors
- Any deal where the investor does NOT directly control the property

## Analysis Framework

### 1. Structure & Entity Analysis

Map the legal structure — who owns what, and how many layers exist between the investor and the asset:

```
ENTITY STRUCTURE MAP
  Investor (you) → [Entity 1] → [Entity 2] → ... → Physical Asset

  Key questions:
  - How many legal entities between investor and asset?
  - What jurisdictions are involved?
  - What entity type holds the asset? (LLC, LP, SPV, PMA, trust)
  - Is the investor's interest in the asset-holding entity or a parent?
  - What happens if an intermediate entity fails?
```

**Red flags:**
- More than 2 entities between investor and asset (complexity = opacity)
- Multiple jurisdictions with different legal systems
- Investor holds interest in a parent company, not the asset entity
- Unclear or missing organizational chart

### 2. Share Class & Rights Analysis

For deals with multiple share classes (common in SPVs and funds):

```
SHARE CLASS COMPARISON
                        Class A (GP/Founder)    Class B (Investor)
  Voting Rights         [Yes/No/Limited]        [Yes/No/Limited]
  Dividend Rights       [% or priority]         [% or priority]
  Liquidation Priority  [Senior/Junior/Pari]    [Senior/Junior/Pari]
  Management Control    [Yes/No]                [Yes/No]
  Transfer Rights       [Free/Restricted]       [Free/Restricted]
  Information Rights    [Full]                  [Limited/Full]
  Tag-Along Rights      [Yes/No]                [Yes/No]
  Anti-Dilution         [Yes/No]                [Yes/No]
```

**Critical investor protections to look for:**
- Preferential liquidation rights (get your money back first)
- Pro-rata dividend rights
- Information and audit rights
- Consent rights on major decisions (sale, refinance, additional debt)
- Tag-along / drag-along provisions
- Anti-dilution protection
- Right of first refusal on share transfers

**Red flags:**
- No voting rights AND no consent rights on major decisions
- GP can make unilateral decisions about the asset
- No preferential liquidation (investor and GP share losses equally)
- Unclaimed dividend forfeiture clauses
- Forced repurchase without investor consent
- Transfer restrictions that effectively trap capital

### 3. Fee Structure Analysis

Fees are the single biggest drag on passive investment returns. Analyze every fee layer:

```
FEE ANALYSIS
  Fee Type                  Amount          Benchmark       Assessment
  ─────────────────────────────────────────────────────────────────
  Acquisition Fee           X%              1–2%            Normal/High
  Management Fee            X% of [base]    1–2% of rev     Normal/High
  Asset Management Fee      X%              1–2%            Normal/High
  Construction Mgmt Fee     X%              3–5%            Normal/High
  Disposition Fee           X%              1–2%            Normal/High
  Performance Fee/Carry     X% above pref   15–20%          Normal/High
  Financing Fee             X%              0.5–1%          Normal/High

  TOTAL ANNUAL FEE DRAG:    X% of gross revenue
  
  BENCHMARK COMPARISON:
    Typical syndication total fees: 2–4% of revenue annually + 20% carry
    Typical PE fund: 1.5–2% mgmt + 20% carry above 8% pref
    
  THIS DEAL: X% total annual fees
  ASSESSMENT: [In-line / Above market / Significantly above market]
```

**Key fee questions:**
- What is the fee calculated ON? (Gross revenue, net revenue, NAV, committed capital, invested capital — each produces very different dollar amounts)
- Are fees charged during construction/pre-revenue period?
- Does the management fee include or exclude staff salaries and OpEx?
- Is there a preferred return hurdle before performance fees kick in?
- Are fees paid before or after investor distributions?

**Red flags:**
- Management fee > 2% of revenue (or > 20% of net revenue in hospitality)
- Fees calculated on gross revenue rather than net income
- No preferred return hurdle for performance fees
- Stacked fees that collectively exceed 5% of revenue
- Fees charged during construction before any revenue is generated
- Fee structures where GP profits even if investors lose money

### 4. Return Projection Validation

Scrutinize the sponsor's projected returns:

```
RETURN PROJECTION AUDIT
  Sponsor's Projections:
    Projected Annual Yield:     X%
    Projected IRR:              X%
    Projected Equity Multiple:  X.Xx
    Hold Period:                X years
    
  Reality Check:
    - Are revenue assumptions supported by market comps?
    - What occupancy rate is assumed? Is it achievable for this market/property type?
    - What ADR/rent growth rate is projected? Is it consistent with market history?
    - What expense ratio is assumed? Does it include ALL expenses?
    - Is there a "pessimistic" scenario, and does it actually show losses?
    - What exit assumptions are made (cap rate, appreciation)?
    
  SCENARIO VALIDATION:
    Sponsor's "Pessimistic":    X% return  ← Is this truly pessimistic?
    Sponsor's "Realistic":      X% return  ← Does this match market data?
    Sponsor's "Optimistic":     X% return  ← Is this within reason?
    
    True Pessimistic (our est):  X% return  ← What if occupancy is 50%?
    True Break-Even:             X% occupancy needed to cover all costs
```

**Red flags:**
- "Pessimistic" scenario still shows strong positive returns (real pessimism includes losses)
- No scenario showing negative returns or principal loss
- Revenue projections significantly above market comparables
- Expense ratio below industry norms for the property type
- Exit assumptions more favorable than entry (lower cap rate at exit)
- IRR projections above 15% for core/stabilized assets
- No sensitivity analysis provided

### 5. Sponsor/GP Due Diligence

The sponsor is the most important factor in any passive investment:

```
SPONSOR EVALUATION
  Track Record:
    - Number of prior projects completed: ___
    - Years of experience: ___
    - Performance through downturns (2008-2010, 2020): ___
    - Any projects with losses? Details: ___
    - References from prior investors: ___
    
  Alignment of Interests:
    - GP co-investment amount: $___  (___% of total equity)
    - GP co-invest benchmark: 5–20% signals strong alignment
    - Does GP invest pari passu with LPs?
    - Is GP compensation primarily from fees or performance?
    
  Operational Capability:
    - In-house management or third-party?
    - Team size and relevant expertise
    - Geographic focus and market knowledge
    - Construction/development capability (if applicable)
    
  Legal/Regulatory:
    - Any litigation history?
    - Regulatory actions or sanctions?
    - Proper licensing for securities offerings?
```

**Red flags:**
- No verifiable track record (first-time sponsor on a large project)
- No GP co-investment ("skin in the game")
- GP earns more from fees than from project success
- Track record only in bull markets (no downturn experience)
- Sponsor has no direct experience in this asset class or market
- Unable to provide references from prior investors

### 6. Capital Call & Liquidity Analysis

```
CAPITAL COMMITMENT STRUCTURE
  Total Commitment:              €/$ ___
  Call Schedule:
    Call 1:    X% due by [date]
    Call 2:    X% due by [date]
    ...
    
  Default Penalties:
    [Describe penalty for missed calls]
    SEVERITY ASSESSMENT: [Standard / Harsh / Punitive]
    Industry standard: Dilution or forced sale at discount (10-20%)
    
  LIQUIDITY ANALYSIS:
    Lock-up period:              X years
    Transfer restrictions:       [Describe]
    Secondary market available?  [Yes/No]
    Redemption rights:           [Yes/No/Limited]
    Estimated time to exit:      X years
    
  LIQUIDITY RATING: [Liquid / Semi-Liquid / Illiquid / Highly Illiquid]
```

**Red flags:**
- Forfeiture of 50%+ of investment for missed capital calls (punitive)
- No ability to transfer shares or very high transfer fees
- No secondary market and no redemption mechanism
- Lock-up period > 7 years with no interim liquidity options
- Capital calls with very short notice periods (<30 days)

### 7. Investor Protection Mechanisms

```
PROTECTION CHECKLIST
  □ Preferential liquidation rights (get your money back first)
  □ Quarterly or annual financial reporting
  □ Independent audit requirement  
  □ Investor advisory committee or similar oversight
  □ Major decision consent rights (sale, refi, new debt)
  □ Removal rights for underperforming GP/manager
  □ Key-person clause (what happens if founder leaves)
  □ Insurance requirements specified
  □ Reserve requirements for CapEx/maintenance
  □ Cooling-off period after commitment
  □ Clear dispute resolution mechanism
  □ Limited liability confirmation
  □ Force majeure provisions
  
  PROTECTION SCORE: ___/13
  
  RATING:
    10-13: Well-protected investor
    7-9:   Adequate but gaps exist
    4-6:   Concerning — significant protections missing
    0-3:   Avoid — investor has minimal protection
```

## Output Format

```
SYNDICATION / FUND ANALYSIS
═══════════════════════════════════════
Deal: [Name]
Sponsor: [Name/Entity]
Structure: [SPV / Fund / DST / Other]
Jurisdiction: [Where]
Minimum Investment: $___

STRUCTURE ASSESSMENT
  Entity layers: X (Investor → ... → Asset)
  Jurisdictions: X
  Investor class: [Class B Preferred / LP / etc.]
  Voting rights: [Yes/No]
  Complexity: [Simple / Moderate / Complex / Very Complex]

FEE ANALYSIS
  Total annual fee drag: X% of revenue
  Assessment: [In-line / Above market / Significantly above]
  
RETURN PROJECTIONS
  Sponsor's realistic case: X% annual yield
  Our adjusted estimate: X% (after fee drag, realistic assumptions)
  Break-even occupancy/revenue: X%
  
SPONSOR ASSESSMENT
  Track record: [Strong / Moderate / Limited / Unverifiable]
  Co-investment: X% of equity
  Alignment: [Strong / Moderate / Weak]

INVESTOR PROTECTIONS
  Protection score: X/13
  Key gaps: [list missing protections]
  
LIQUIDITY
  Estimated hold: X years
  Exit options: [list]
  Liquidity rating: [Liquid → Highly Illiquid]

RED FLAGS IDENTIFIED
  1. [Flag + explanation]
  2. [Flag + explanation]
  ...

OVERALL ASSESSMENT: [INVEST / NEGOTIATE TERMS / PASS]
[Detailed reasoning — what would need to change to make this investable]
```
