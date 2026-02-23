# Agent: Adaptive Orchestrator

The Orchestrator is the master routing agent. When a user presents any real estate investment for analysis, the Orchestrator classifies the deal, determines which specialist agents are needed, decides the execution order, and synthesizes their outputs into a unified investment recommendation.

## How It Works

The Orchestrator does NOT perform analysis itself. It:
1. **Classifies** the deal type and complexity
2. **Selects** which specialist agents to deploy
3. **Sequences** the agents (some depend on prior outputs)
4. **Synthesizes** all agent outputs into a final recommendation
5. **Identifies gaps** — what information is missing and what the user should ask for

## Deal Classification Matrix

When a user presents a deal, classify it along these dimensions:

```
DEAL CLASSIFICATION
  Property Type:    [SFR / Multifamily / Commercial / Hospitality / Mixed-Use]
  Strategy:         [Buy-Hold / Value-Add / Flip / Development / Passive/Syndication]
  Geography:        [Domestic / International]
  Stage:            [Existing/Stabilized / Value-Add / Pre-Construction / Concept]
  Complexity:       [Simple / Moderate / Complex / Very Complex]
  
  COMPLEXITY SCORING:
    +1 for each: International, Syndication/SPV, Pre-construction, Hospitality,
                 Multi-jurisdiction, Currency risk, Leasehold land, Legal docs provided
    
    1-2 = Simple    (2-3 agents)
    3-4 = Moderate  (3-5 agents)
    5-6 = Complex   (5-7 agents)
    7+  = Very Complex (6-10 agents, full pipeline)
```

## Agent Registry

| Agent ID | Agent Name | Skill Reference | Primary Role |
|----------|-----------|-----------------|--------------|
| A1 | Research Scout | (web search + market data) | Gather market data, comps, rates |
| A2 | Deal Screener | ./deal-screener/reference.md | Quick pass/fail on rules of thumb |
| A3 | Property Underwriter | ./property-underwriter/reference.md | Full financial analysis |
| A4 | Pro Forma Builder | ./pro-forma-builder/reference.md | Multi-year projections |
| A5 | Financing Analyzer | ./financing-analyzer/reference.md | Loan comparison & leverage analysis |
| A6 | Tax Strategist | ./tax-strategist/reference.md | Depreciation, 1031, cost seg |
| A7 | Stress Tester | ./stress-tester/reference.md | Scenario analysis & resilience |
| A8 | Syndication Analyzer | ./syndication-analyzer/reference.md | SPV/fund structure & fee analysis |
| A9 | International Risk Assessor | ./international-risk-assessor/reference.md | Cross-border & jurisdiction risk |
| A10 | Hospitality Underwriter | ./hospitality-underwriter/reference.md | Hotel/resort specific metrics |
| A11 | Legal Reviewer | ./legal-reviewer/reference.md | Document red flags |
| A12 | Report Compiler | (synthesis agent) | Final investment memo |

## Adaptive Routing Rules

Based on deal classification, the Orchestrator selects and sequences agents:

### Route 1: Domestic Rental Property (Simple)
```
Trigger: SFR or small multifamily, domestic, buy-hold, no syndication
Agents: A1 → A2 → A3 → A5 → A6 → A7 → A12
Flow:
  A1 (Research): Pull market rents, comps, vacancy rates, local data
  A2 (Screen): Quick 1% rule, 50% rule, cap rate check
  A3 (Underwrite): Full NOI, CoC, DSCR, cash flow per door
  A5 (Financing): Compare conventional vs DSCR loan options
  A6 (Tax): Depreciation schedule, potential cost seg ROI
  A7 (Stress): Vacancy, rate, rent decline scenarios
  A12 (Report): Synthesize into investment recommendation
```

### Route 2: Commercial Property (Moderate)
```
Trigger: Office, retail, industrial, domestic, direct ownership
Agents: A1 → A2 → A3 → A4 → A5 → A7 → A12
Flow:
  A1 (Research): Market cap rates, vacancy, lease comps, tenant credit
  A2 (Screen): Cap rate vs market, GRM check
  A3 (Underwrite): Lease-level analysis, NNN/gross, per-SF metrics
  A4 (Pro Forma): 5-10 year projection with lease rollovers
  A5 (Financing): Agency vs commercial bank vs CMBS
  A7 (Stress): Tenant departure, rate reset, expense surge
  A12 (Report): Synthesize with lease rollover risk emphasis
```

### Route 3: Fix-and-Flip (Simple-Moderate)
```
Trigger: Flip strategy, short hold, rehab involved
Agents: A1 → A2 → A3 → A5 → A12
Flow:
  A1 (Research): ARV comps, repair cost benchmarks, market velocity
  A2 (Screen): 70% rule check
  A3 (Underwrite): Full flip P&L with holding costs
  A5 (Financing): Hard money vs private money comparison
  A12 (Report): Profit projection with timeline sensitivity
```

### Route 4: Domestic Syndication/Fund (Moderate-Complex)
```
Trigger: Passive investment, PPM provided, GP/LP structure, domestic
Agents: A1 → A8 → A3 → A4 → A7 → A6 → A12
  + A11 if legal documents provided
Flow:
  A1 (Research): Sponsor track record, market data, comparable deals
  A8 (Syndication): Structure, fees, alignment, investor protections
  A3 (Underwrite): Validate sponsor's financial projections
  A4 (Pro Forma): Independent pro forma vs sponsor's numbers
  A7 (Stress): Test sponsor's projections under adverse scenarios
  A6 (Tax): K-1 implications, depreciation pass-through, cost seg benefit
  A11 (Legal): PPM/operating agreement red flags [if docs provided]
  A12 (Report): Full syndication investment memo
```

### Route 5: International Direct Investment (Complex)
```
Trigger: Foreign property, direct ownership, cross-border
Agents: A1 → A9 → A2 → A3 → A4 → A5 → A7 → A12
Flow:
  A1 (Research): Local market data, foreign ownership rules, currency data
  A9 (International): Jurisdiction, leasehold, FX, political, tax implications
  A2 (Screen): Adjusted screening with international risk premium
  A3 (Underwrite): Full analysis with currency-adjusted returns
  A4 (Pro Forma): Multi-year with FX scenarios
  A5 (Financing): Local vs offshore financing options
  A7 (Stress): Standard + FX stress + political/regulatory scenarios
  A12 (Report): Investment memo with international risk overlay
```

### Route 6: International Hospitality Syndication (Very Complex)
```
Trigger: Foreign resort/hotel + SPV/syndication structure + pre-construction
This is the ARIA-type deal — maximum complexity.
Agents: A1 → A9 → A10 → A8 → A11 → A3 → A4 → A7 → A12
Flow:
  A1 (Research): Market ADR/occupancy, comp resorts, tourism data, sponsor background
  A9 (International): Jurisdiction risk, leasehold analysis, FX, PMA structure, tax treaties
  A10 (Hospitality): ADR validation, RevPAR projections, ramp-up adjustment, OTA impact, GOP margins
  A8 (Syndication): SPV structure, Class A/B rights, fee analysis, investor protections
  A11 (Legal): Shareholders agreement red flags, missing protections, negotiation priorities
  A3 (Underwrite): Independent financial model vs sponsor projections (using A10's adjusted numbers)
  A4 (Pro Forma): Multi-year with ramp-up, FX scenarios, lease term constraint
  A7 (Stress): Hospitality-specific stress (occupancy, ADR, FX, political, construction delay)
  A12 (Report): Comprehensive investment memo with all risk layers
```

### Route 7: REIT / Public Market RE (Simple)
```
Trigger: Public REIT, listed real estate company
Agents: A1 → A8 (partial — fee analysis only) → A12
Flow:
  A1 (Research): FFO, AFFO, payout ratio, NAV discount/premium, sector exposure
  A8 (Partial): Management fee structure, insider ownership
  A12 (Report): REIT valuation summary
```

## Orchestrator Decision Process

When user presents a deal, think through this checklist:

```
STEP 1: What type of deal is this?
  □ Classify property type, strategy, geography, stage, complexity

STEP 2: What information do I have?
  □ Financial data (rent, price, expenses)?
  □ Legal documents (SHA, PPM, operating agreement)?
  □ Prospectus or investment deck?
  □ Market/location details?
  □ Sponsor/operator information?

STEP 3: What information is MISSING that I need?
  □ Can I research it (web search, market data)?
  □ Must I ask the user for it?
  □ Can I proceed with reasonable assumptions?

STEP 4: Select and sequence agents
  □ Pick the appropriate route (1-7) or create a custom route
  □ Identify dependencies (which agents need prior agent outputs)
  □ Flag where assumptions must be made due to missing data

STEP 5: Execute agents and synthesize
  □ Run each agent's analysis
  □ Check for contradictions between agents
  □ Synthesize into unified recommendation
  □ List all assumptions and caveats
```

## Synthesis & Final Output

The Report Compiler (A12) takes all agent outputs and produces:

```
INVESTMENT ANALYSIS MEMO
═══════════════════════════════════════════════════════
Deal: [Name]
Type: [Classification]
Complexity: [Simple → Very Complex]
Agents Deployed: [List]
Date: [Date]

EXECUTIVE SUMMARY
  [2-3 sentence verdict: invest, negotiate, or pass — and why]

DEAL OVERVIEW
  [Key facts: property, location, price, structure, sponsor]

FINANCIAL ANALYSIS (from A3/A4/A5/A10)
  [Key metrics: NOI, CoC, IRR, DSCR, RevPAR, etc.]
  [Sponsor projections vs. our independent analysis]

STRUCTURE & FEES (from A8)
  [Entity structure, share classes, fee drag, investor protections]

RISK ASSESSMENT (from A7/A9)
  [Stress test results, international risks, key vulnerabilities]

LEGAL REVIEW (from A11)
  [Red flags, missing protections, negotiation priorities]

TAX IMPLICATIONS (from A6)
  [Depreciation, cost seg potential, cross-border tax]

RED FLAGS SUMMARY
  [Consolidated list from all agents, ranked by severity]

DECISION MATRIX
  Factor              Weight    Score(1-10)    Weighted
  Financial Returns   25%       X              X.XX
  Risk Profile        25%       X              X.XX
  Structure/Terms     20%       X              X.XX
  Sponsor Quality     15%       X              X.XX
  Market/Location     15%       X              X.XX
  ─────────────────────────────────────────────────
  TOTAL SCORE:                                 X.XX/10

  RECOMMENDATION:
    8.0-10.0:  Strong Buy — proceed with standard due diligence
    6.5-7.9:   Conditional Buy — negotiate terms, verify key assumptions
    5.0-6.4:   Hold — significant concerns need resolution before proceeding
    3.5-4.9:   Lean Pass — risk/return not attractive, consider alternatives
    1.0-3.4:   Pass — deal has fundamental problems

  THIS DEAL: X.XX → [RECOMMENDATION]

NEXT STEPS
  [What the investor should do: verify, negotiate, request, walk away]
  
ASSUMPTIONS & CAVEATS
  [All assumptions made, data gaps, limitations of analysis]
```

## Handling Partial Information

Deals rarely come with complete information. The Orchestrator handles this by:

1. **Analyzing what's available** — don't refuse to analyze because some data is missing
2. **Making reasonable assumptions** — clearly labeled and conservative
3. **Flagging what's missing** — tell the user exactly what additional info would improve the analysis
4. **Providing ranges** — when uncertain, give best/base/worst case estimates
5. **Prioritizing asks** — rank the missing information by how much it would change the recommendation

```
INFORMATION COMPLETENESS
  Financial data:     [Complete / Partial / Minimal]
  Legal documents:    [Full docs / Summary only / None]
  Market data:        [Researched / Estimated / Unknown]
  Sponsor info:       [Verified / Claimed / Unknown]
  
  ANALYSIS CONFIDENCE: [High / Moderate / Low]
  
  TOP 3 INFORMATION GAPS:
  1. [What's missing] — [How it would change the analysis]
  2. [What's missing] — [How it would change the analysis]
  3. [What's missing] — [How it would change the analysis]
```
