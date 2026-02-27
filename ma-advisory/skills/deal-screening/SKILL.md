---
name: "Deal Screening"
description: >
  Rapid target evaluation through CIM extraction and IOI drafting. Strips
  sell-side marketing rhetoric from Confidential Information Memorandums to
  isolate core financials (EBITDA, margins, churn, CAC/LTV). Enables buy-side
  teams to screen dozens of targets daily and generate customized Indications
  of Interest.
version: "1.0"
author: "LauraFlorentin"
---

# Deal Screening

Buy-side consultants, PE associates, and corporate development teams waste critical evaluation hours manually stripping corporate jargon from CIMs to find core data. This skill automates target screening and IOI generation.

## When to Use

- Evaluating an inbound CIM or teaser from a sell-side bank
- Screening multiple targets simultaneously for a buy-side mandate
- Generating a customized IOI for an attractive target
- Building a rapid valuation view before investment committee review

## The /cim-extract Protocol

### How It Works

Deliberately bypasses CIM formatting entirely. Instructs the AI to ignore narrative prose and extract only:
- **Quantitative assertions**: Revenue, EBITDA, margins, growth rates, customer metrics
- **Explicit strategic claims**: Market position, competitive moats, expansion vectors
- **Management adjustments**: Proposed EBITDA add-backs with stated rationale
- **Key risk indicators**: Customer concentration, churn rates, capex requirements

### Output Format

```
## CIM Extraction Summary — [Target Name]

### Financial Snapshot
| Metric | FY-2 | FY-1 | LTM | Mgmt Projection |
|--------|------|------|-----|-----------------|
| Revenue | | | | |
| Gross Margin | | | | |
| Adj. EBITDA | | | | |
| EBITDA Margin | | | | |
| Free Cash Flow | | | | |

### Proposed EBITDA Adjustments
| Add-Back | Amount | Rationale | Defensibility |
|----------|--------|-----------|---------------|
| | | | High / Medium / Low |

### Key Metrics
- **Customer concentration**: Top 10 = [X]% of revenue
- **Churn rate**: [X]%
- **CAC / LTV ratio**: [X]
- **Organic growth rate**: [X]%

### Investment Highlights (seller's claims)
1. [Claim] — [Supporting data point or "UNSUBSTANTIATED"]

### Red Flags
- [Identified concerns from the data]

### Verdict
[Quick BUY-SIDE assessment: Advance / Further Diligence / Pass]
```

## IOI Memorandum Generation

### Key Sections

| Section | Focus |
|---------|-------|
| Purchase Price Range | Enterprise valuation estimate, expressed as EBITDA multiple |
| Transaction Structure | Asset vs. stock, cash/equity/rollover/earn-out mix |
| Sources of Financing | Proof of funds, committed equity, anticipated leverage |
| Key Assumptions | Metrics the valuation relies upon |
| Due Diligence Scope | Remaining access required to reach definitive agreement |
| Timing & Approvals | Timeline to LOI and investment committee requirements |

### AI-Assisted IOI Workflow

1. Ingest the target's CIM and the buyer's investment committee memos
2. Map buyer's strategic rationale to seller's growth pillars
3. Generate bespoke IOI that feels tailored (not a form letter)
4. Align the offer structure directly with CIM's identified opportunities

## Operating Guidelines

- Never trust sell-side EBITDA at face value — always flag adjustments for validation
- Distinguish between organic and inorganic (M&A-driven) revenue growth
- Flag customer concentration above 20% for any single customer
- For IOIs, ensure the valuation range is defensible with stated methodology
- Time saved: **3-5 hours per CIM** screening; IOI drafting gives massive competitive advantage in auctions
