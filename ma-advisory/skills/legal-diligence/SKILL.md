---
name: legal-diligence
description: >
  Legal due diligence automation — NDA redlining against firm playbooks,
  change-of-control clause scanning across material contracts, disclosure
  schedule drafting for purchase agreements, and red flag report generation.
  Covers the full spectrum of legal risk identification in M&A transactions.
  Use when user asks to "run legal due diligence", "review contracts", "legal risk assessment", or mentions legal DD, contract review, or compliance diligence.
version: "1.0"
author: "LauraFlorentin"
---

# Legal Diligence

Legal due diligence is where hidden liabilities surface — or slip through. This skill automates the most labor-intensive legal DD tasks: NDA management, contract scanning, disclosure drafting, and red flag identification.

## When to Use

- Redlining counterparty NDA markups in a sell-side auction
- Scanning material contracts for change-of-control triggers
- Drafting disclosure schedules for a purchase agreement
- Compiling a red flag due diligence report

## The /redline-nda Protocol

### How It Works

Relies on a strict, pre-programmed negotiation playbook:
1. **Ingests** the counterparty's marked-up NDA
2. **Compares** semantic differences against the firm's standard positions
3. **Accepts** benign formatting changes
4. **Reverts** substantive deviations requiring senior partner review
5. **Generates** a redlined counter-draft with commentary

### Common NDA Negotiation Points

| Clause | Standard Position | Common Counterparty Push |
|--------|------------------|-------------------------|
| Confidentiality term | 24 months | Reduce to 12 months |
| Non-solicitation | 18-24 months | Eliminate or shorten |
| Permitted disclosure | Named advisors only | Expand to financing sources |
| Residuals clause | Exclude | Include |
| Standstill | Include | Remove or sunset |

**Time saved**: 1-2 hours per bidder in high-volume auction processes.

## The /flag-coc Protocol

### How It Works

Deploys a **cumulative risk synthesis model** — not simple keyword matching:
1. **Semantic understanding** of assignment restrictions and transferability clauses
2. **Identifies** clauses triggered by equity ownership changes
3. **Flags** financial penalties, consent requirements, and termination rights
4. **Compiles** an actionable risk register

### Output Format

```
## Change-of-Control Risk Register

**Contracts Scanned**: [N]
**CoC Provisions Found**: [N]
**Critical (deal-threatening)**: [N]
**Moderate (consent required)**: [N]
**Low (notification only)**: [N]

### Critical Findings
| Contract | Counterparty | Provision | Impact | Required Action |
|----------|--------------|-----------|--------|-----------------|
| | | | Revenue at risk: $X | Third-party consent required |

### Consent Request Priority
1. [Highest-value contract requiring consent]
2. [Second priority]
...
```

**Time saved**: 20+ hours during legal DD. Identifies hidden liabilities that could threaten revenue continuity post-close.

## The /schedule-disclosure Protocol

### How It Works

1. **Extracts** data from VDR to populate initial schedule drafts
2. **Maps** disclosures to specific SPA/APA sections (e.g., Section 3.14 Material Contracts)
3. **Cross-references** for internal consistency against the operative agreement
4. **Flags** potential omissions

### Common Disclosure Schedules

| Schedule | Source Data | Threshold |
|----------|-----------|-----------|
| Material Contracts | All contracts | >$250K annual value |
| Capitalization | Equity grants, warrants, options | All outstanding |
| Litigation | Pending/threatened claims | All |
| Employee Benefits | Plan documents | All plans |
| Real Property | Leases, owned property | All |
| IP Registrations | Patents, trademarks, copyrights | All registered |

> **⚠️ AI Limitations**: LLMs cannot independently verify the economic substance of related-party transactions or interpret subjective legal standards like "Material Adverse Effect." AI outputs in definitive legal agreements must remain strictly advisory, requiring rigorous human validation.

**Time saved**: 12+ hours of manual drafting per transaction.

## Red Flag Due Diligence Report

### Key Sections

| Section | Focus |
|---------|-------|
| Executive Risk Summary | Prioritized dashboard by severity and valuation impact |
| Corporate Governance & Capitalization | Unresolved equity claims, missing consents, invalid 409A valuations |
| Material Contracts | Onerous CoC provisions, exclusivity, single-supplier concentration |
| Intellectual Property | Unsecured chain of title, open-source contamination, infringement |
| Regulatory & Compliance | Pending investigations, data privacy exposure, environmental liabilities |
| Labor & Employment | Contractor misclassification, unfunded pensions, key-person flight risk |

### AI-Assisted Workflow

The AI continually scans the VDR as documents are uploaded, comparing against a predefined database of critical transactional risks. When anomalies are detected — missing IP assignment clauses, undocumented equity issuances, broken cap tables — they immediately populate the Red Flag Report template.

## Operating Guidelines

- NDA redlining: always escalate novel or bespoke clauses to senior counsel
- CoC scanning: go beyond keywords — use semantic understanding for bespoke legal phrasing
- Disclosure schedules: err on the side of over-disclosure to minimize post-close indemnification risk
- Red flag reports: focus on exceptions, not comprehensive cataloguing
- All legal outputs are advisory — always require qualified legal review


## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Change-of-control clauses missed | Buried in schedules | Run keyword scan on full contract corpus, not just main body |
| NDA redline rejected by counterparty | Overly aggressive positions | Use tiered playbook: "must-haves" vs. "nice-to-haves"; escalate only on must-haves |
| Disclosure schedules incomplete | Seller's counsel rushed | Provide a disclosure schedule checklist at LOI stage; allow 2-week cure period |
| Material contracts not provided | VDR gaps | Cross-reference audited financials for material contract obligations; request missing items |
