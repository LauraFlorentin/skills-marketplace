---
name: "Real Estate Investment Analyzer"
description: >
  ALWAYS USE THIS SKILL when the user mentions ANY of: real estate investing,
  rental property, commercial property, multifamily, fix-and-flip, BRRRR,
  cap rate, NOI, cash-on-cash, DSCR, pro forma, 1% rule, 1031 exchange,
  depreciation, cost segregation, syndication, SPV, PPM, shareholders agreement,
  hotel investment, resort investment, Bali property, international real estate,
  property analysis, deal analysis, underwriting, investment package, prospectus,
  investment deck, passive income from real estate, REIT analysis, preferred return,
  waterfall distribution, management fee analysis, ADR, RevPAR, occupancy rate,
  leasehold risk, currency risk, Tulum property, Mexico real estate, fideicomiso,
  ejido, PT PMA, HGB, cross-border financing, HELOC for overseas, repatriation,
  withholding tax, DTAA, developer financing, pre-construction investment,
  J-curve, ramp-up period, or ANY request to analyze an investment document.
  Also triggers on: Zillow API, Redfin data, AirDNA, Census data, CoStar,
  batch deal screening, Monte Carlo simulation, Python calculator, JavaScript
  calculator, investment code, automated analysis pipeline, property API,
  rental data API, market data, comp data, or any request for code/scripts
  to analyze real estate investments.
  This skill provides comprehensive real estate investment analysis using an
  adaptive multi-agent system that automatically selects the right specialist
  agents based on deal type and complexity. Covers domestic and international
  deals (with country-specific profiles for Indonesia/Bali and Mexico/Tulum),
  direct ownership and passive syndications, all property types including
  hospitality, cross-border financing strategies, and full legal document review.
version: "2.1"
author: "User"
---

# Real Estate Investment Analyzer v2.1
## Adaptive Multi-Agent Analysis System

This skill uses an **adaptive orchestrator** that classifies each deal and deploys the right combination of specialist agents. You don't need to pick which skill to use — describe the deal and the orchestrator handles routing.

## Quick Start

**User says anything about a real estate investment → Read the Orchestrator first:**
```
view → ../../agents/orchestrator.md
```

The Orchestrator will tell you which specialist reference files to read based on the deal type.

## Architecture

```
                        ┌─────────────────────┐
                        │    ORCHESTRATOR      │
                        │  (../../agents/orchestrator.md) │
                        │                     │
                        │  1. Classify deal    │
                        │  2. Select agents    │
                        │  3. Sequence work    │
                        │  4. Synthesize output│
                        └──────────┬──────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
              ┌─────▼─────┐ ┌─────▼─────┐ ┌─────▼─────┐
              │  CORE      │ │ EXPANDED   │ │ SYNTHESIS  │
              │  AGENTS    │ │ AGENTS     │ │ AGENTS     │
              │            │ │            │ │            │
              │ A1 Research│ │ A8 Syndic. │ │ A12 Report │
              │ A2 Screen  │ │ A9 Int'l   │ │   Compiler │
              │ A3 Underwr.│ │ A10 Hospit.│ └────────────┘
              │ A4 ProForma│ │ A11 Legal  │
              │ A5 Finance │ └────────────┘
              │ A6 Tax     │
              │ A7 Stress  │
              └────────────┘
```

## Agent → Reference File Map

| Agent | Reference File | Use When |
|-------|---------------|----------|
| A1 Research Scout | *(uses web search tools)* | Always — gather market data first |
| A2 Deal Screener | `../../agents/deal-screener/reference.md` | Quick pass/fail filtering |
| A3 Property Underwriter | `../../agents/property-underwriter/reference.md` | Full financial analysis |
| A4 Pro Forma Builder | `../../agents/pro-forma-builder/reference.md` | Multi-year projections |
| A5 Financing Analyzer | `../../agents/financing-analyzer/reference.md` | Loan comparison & leverage |
| A6 Tax Strategist | `../../agents/tax-strategist/reference.md` | Depreciation, 1031, cost seg |
| A7 Stress Tester | `../../agents/stress-tester/reference.md` | Scenario analysis |
| A8 Syndication Analyzer | `../../agents/syndication-analyzer/reference.md` | SPV, fund, passive deals |
| A9 Int'l Risk Assessor | `../../agents/international-risk-assessor/reference.md` | Cross-border investments |
| A10 Hospitality Underwriter | `../../agents/hospitality-underwriter/reference.md` | Hotels, resorts, STRs |
| A11 Legal Reviewer | `../../agents/legal-reviewer/reference.md` | Document red flags |
| A12 Report Compiler | `../../agents/orchestrator.md` (synthesis section) | Final recommendation |
| — Data Sources | `../../agents/data-sources/reference.md` | API lookups, batch screening, market data |

## Routing Quick Reference

| Deal Type | Route | Agents |
|-----------|-------|--------|
| Domestic rental (SFR/MF) | Route 1 | A1→A2→A3→A5→A6→A7→A12 |
| Commercial property | Route 2 | A1→A2→A3→A4→A5→A7→A12 |
| Fix-and-flip | Route 3 | A1→A2→A3→A5→A12 |
| Domestic syndication | Route 4 | A1→A8→A3→A4→A7→A6→(A11)→A12 |
| International direct | Route 5 | A1→A9→A2→A3→A4→A5→A7→A12 |
| Int'l hospitality syndication | Route 6 | A1→A9→A10→A8→A11→A3→A4→A7→A12 |
| REIT / public market | Route 7 | A1→A8(partial)→A12 |

## Execution Instructions

### Step 1: Read the Orchestrator
Always start by reading `../../agents/orchestrator.md`. It contains the classification logic and routing rules.

### Step 2: Classify the Deal
Use the Orchestrator's classification matrix to determine:
- Property type, strategy, geography, stage, complexity
- Which route (1-7) applies, or create a custom route

### Step 3: Read Required Reference Files
Read ONLY the reference files for agents selected by the Orchestrator. Don't read all files for a simple rental analysis.

### Step 4: Execute Each Agent's Analysis
Follow each reference file's framework. Pass outputs forward where agents depend on prior results (e.g., A10 Hospitality outputs feed into A3 Underwriter).

### Step 5: Compile the Report
Use the Orchestrator's synthesis template to produce the final Investment Analysis Memo.

## Default Assumptions (When User Doesn't Specify)

### Domestic (US) Defaults
| Parameter | Default | Source |
|-----------|---------|--------|
| 30-yr fixed rate | 6.11% | Freddie Mac, Feb 2026 |
| Vacancy (residential) | 7% | National average |
| Vacancy (office) | 18% | National average |
| Expense ratio (residential) | 45% | Industry standard |
| Expense ratio (NNN commercial) | 15% | Industry standard |
| Rent growth | 2.5%/year | Long-term average |
| Expense growth | 2.5%/year | Inflation proxy |
| Exit cap premium | +0.50% over entry | Conservative |
| Closing costs | 3% of purchase | Investment property avg |
| CapEx reserve | $400/unit/year (MF), 8% gross (SFR) | Industry standard |
| Management fee | 8% SFR, 6% small MF, 5% large MF | Market rates |
| Land allocation | 20% (for depreciation) | Standard |
| Conforming limit | $832,750 | 2026 FHFA |
| Depreciation | 27.5yr residential, 39yr commercial | IRS |
| Bonus depreciation | 100% (OBBBA, July 2025) | Current law |

### International / Hospitality Defaults
| Parameter | Default | Notes |
|-----------|---------|-------|
| OTA commission | 20% | Booking.com/Expedia average |
| Hospitality management fee | 3-5% base + 10-15% incentive | Standard; >20% of net rev is high |
| Hospitality OpEx ratio | 50-60% of revenue | Luxury resort |
| Ramp-up Year 1 | 55% of stabilized RevPAR | New property |
| Ramp-up Year 2 | 75% of stabilized RevPAR | Building reputation |
| Ramp-up Year 3 | 90% of stabilized RevPAR | Approaching stabilization |
| FF&E reserve | 4% of revenue | Hospitality standard |
| Leasehold discount | See int'l risk assessor | Varies by years remaining |
| FX risk premium | +3-5% required return | Emerging market |
| International risk premium | +2-5% required return | Jurisdiction dependent |

### Bali-Specific Defaults
| Parameter | Default | Notes |
|-----------|---------|-------|
| Ownership structure | PT PMA with HGB title | Most secure for foreigners |
| Min. investment plan (PMA) | IDR 10 billion (~$600K) | Per KBLI, BKPM Reg 5/2025 |
| Min. paid-up capital (PMA) | IDR 2.5 billion (~$150K) | New 2025 reduced threshold |
| Market-wide ADR (Bali STR) | $178/night | 2025 average; luxury top 10% = $539+ |
| Occupancy (Bali average) | 66% | Higher in Seminyak/Canggu, lower in emerging |
| WHT on dividends (standard) | 20% | Reducible to 5-15% via DTAA |
| Corporate income tax | 22% | Standard PT PMA rate |
| IDR long-term depreciation | ~3%/year vs EUR/USD | 10-year historical average |
| Active-use deadline (HGB) | 2 years | PP 18/2021; idle land reverts to state |

### Mexico/Tulum-Specific Defaults
| Parameter | Default | Notes |
|-----------|---------|-------|
| Ownership structure | Fideicomiso (bank trust) | Required in Restricted Zone (coastal) |
| Fideicomiso setup cost | $1,500-2,500 USD | One-time |
| Annual trust fee | $500-1,000 USD | Ongoing |
| ISABI (acquisition tax) | ~3.0% | Municipality-dependent |
| Lodging tax | 6.0% | Remitted via Airbnb or directly |
| ISR (non-resident income tax) | 25% gross or 35% net | 35% net preferred with legal rep |
| Capital gains (non-resident) | 25% gross or 35% net | Mexico has primary taxing right |
| Tulum resale discount | 3-15% below asking | 2026 buyer's market |
| Ejido land risk | VERIFY ALWAYS | #1 cause of investment loss in region |

## Benchmark Targets (Quick Reference)

| Metric | Acceptable | Good | Excellent |
|--------|-----------|------|-----------|
| Cash-on-Cash Return | 6–8% | 8–12% | 12%+ |
| Cash Flow per Door | $100/mo | $150–200/mo | $300+/mo |
| DSCR | 1.20x | 1.25–1.35x | 1.50x+ |
| Break-Even Occupancy | <85% | <80% | <75% |
| Equity Multiple (5-yr) | 1.5x | 1.7–2.0x | 2.0x+ |
| IRR (Value-Add) | 12% | 15% | 18%+ |
| GRM | 8–10 | 5–7 | 4–5 |
| GOP Margin (Luxury Hotel) | 35% | 40-45% | 50%+ |
| RevPAR Index | 90 | 100-110 | 120+ |

## Cap Rate Benchmarks (2025-2026)

| Property Type | Average | Range |
|---------------|---------|-------|
| Multifamily | 5.9% | 3.9–7.6% |
| Industrial | 6.4% | 5.2–7.7% |
| Retail | 6.7% | 5.0–9.1% |
| Self-Storage | 6.2% | 5.3–7.6% |
| Office | 7.4% | 4.6–10.5% |

## Output Principles

1. **Show all math** — every number should be traceable to inputs and formulas
2. **Flag issues prominently** — red flags get their own section, not buried in text
3. **Compare to benchmarks** — every metric compared to industry standards
4. **Recommend next steps** — don't just analyze, tell the user what to DO
5. **State assumptions** — every assumption clearly labeled and justified
6. **Provide ranges** — when uncertain, give best/base/worst estimates
7. **Caveat legal content** — always note that legal review is not legal advice
8. **Integrate with tools** — use xlsx skill for calculators, docx for reports, web search for market data
9. **Generate code when asked** — provide Python/JS calculators, batch scripts, or API integration code; reference `../../agents/data-sources/reference.md` for API patterns and `../../agents/stress-tester/reference.md` for Monte Carlo templates
10. **Match output format to need** — narrative for reports, tables for comparisons, code for automation, spreadsheets for interactive analysis

## Integration with Other Skills

- **xlsx skill**: Create downloadable calculator spreadsheets with the analysis
- **docx skill**: Generate formatted investment memos and due diligence reports
- **pptx skill**: Create investor presentation summaries
- **web search**: Research market data, sponsor track records, comparable properties
- **pdf skill**: Extract and analyze uploaded prospectuses and legal documents
