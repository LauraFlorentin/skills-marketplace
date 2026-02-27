---
name: "Regulatory Screening"
description: >
  Cross-border regulatory risk assessment for M&A transactions. Screens target
  revenue footprints against global antitrust and Foreign Direct Investment (FDI)
  thresholds. Flags jurisdictions requiring mandatory pre-close filings to
  prevent deal delays, fines, or forced unwinding.
version: "1.0"
author: "LauraFlorentin"
---

# Regulatory Screening

Cross-border M&A is fraught with overlapping regulatory regimes. Failing to file for antitrust clearance or FDI approval in a tertiary jurisdiction can lead to massive fines, mandated divestitures, or forced deal unwinding.

## When to Use

- Evaluating a cross-border acquisition for regulatory hurdles
- Initial assessment of antitrust filing requirements across jurisdictions
- FDI screening for foreign acquirers
- Timeline forecasting for regulatory approvals
- Risk allocation planning in definitive agreements

## The /screen-fdi Protocol

### How It Works

1. **Ingest** the target's geographic revenue breakdown, physical asset locations, and customer distribution
2. **Cross-reference** against the latest global thresholds for:
   - Mandatory merger control filings (HSR in US, CMA in UK, EC in EU, SAMR in China, etc.)
   - FDI notification requirements (CFIUS, EU FDI Screening Regulation, etc.)
   - Sector-specific reviews (defense, critical infrastructure, healthcare, telecoms)
3. **Flag** jurisdictions requiring mandatory pre-close filings
4. **Estimate** review timelines and potential remedies

### Output Format

```
## Regulatory Screening Report

### Deal Parameters
- **Acquirer jurisdiction**: [Country]
- **Target jurisdictions**: [List]
- **Combined revenue**: $[X]M
- **Sector(s)**: [Industry classification]

### Filing Requirements

| Jurisdiction | Regime | Threshold | Status | Est. Timeline | Risk Level |
|-------------|--------|-----------|--------|---------------|------------|
| United States | HSR Act | Size-of-transaction >$[X]M | FILING REQUIRED | 30-60 days | 🟡 |
| European Union | EC Merger Reg | Combined turnover >€5B | FILING REQUIRED | 25-90 working days | 🟡 |
| United Kingdom | CMA | UK turnover >£70M or >25% share | REVIEW LIKELY | 40-60 working days | 🟡 |
| China | SAMR | [Thresholds] | TO BE ASSESSED | 30-180 days | 🔴 |

### FDI-Specific Risks
| Jurisdiction | Trigger | Required Action |
|-------------|---------|-----------------|
| [Country] | [Critical infrastructure / national security] | Mandatory pre-close notification |

### Structural Recommendations
- [Strategies to avoid/mitigate regulatory triggers]
- [Suggested risk allocation in purchase agreement]

### Timeline Impact
- **Earliest possible close**: [Date estimate]
- **Critical path**: [Longest regulatory review]
```

> **⚠️ Explicit Limitation**: This tool provides preliminary screening only and does **not** replace formal antitrust legal counsel. Thresholds change annually. Always verify current filing requirements with qualified competition lawyers.

## Operating Guidelines

- This is a preliminary screening tool — always verify with qualified legal counsel
- Thresholds are jurisdiction and year-specific — flag if data may be outdated
- Consider both target-side and acquirer-side revenue for combined thresholds
- Sector-specific reviews (defense, telecoms, critical infrastructure) have lower thresholds
- For Chinese (SAMR) filings, timeline can extend to 180+ days — plan accordingly
- FDI screening is increasingly aggressive globally post-2020 — err on the side of filing
- Include regulatory risk allocation in the SPA (who bears risk of non-approval, break fees)

**Time saved**: 8+ hours of preliminary legal research per transaction.
