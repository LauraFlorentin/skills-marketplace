---
name: "Synergy Analysis"
description: >
  Synergy identification, quantification, and validation for M&A transactions.
  Maps overlapping headcount, vendor relationships, and infrastructure across
  buyer and target organizations. Generates cost-takeout plans with
  costs-to-achieve estimates for lender validation and integration planning.
version: "1.0"
author: "LauraFlorentin"
---

# Synergy Analysis

Synergy underwriting provides the mathematical and strategic justification for paying an acquisition premium. Cost synergies — headcount rationalization, facility closures, vendor consolidation — are the most reliable forms of value creation, but identifying them requires mapping two complex organizations.

## When to Use

- Quantifying cost synergies to justify an acquisition premium
- Mapping organizational overlaps between buyer and target
- Identifying vendor consolidation and contract renegotiation opportunities
- Building a cost-takeout plan for lender validation
- Generating the Synergy and Cost Savings Analysis Report

## The /synergy-map Protocol

### How It Works

1. **Ingest** the target's employee census, benefits data, and third-party spend
2. **Compare** against the acquirer's operating model and vendor lists
3. **Identify** overlapping functions:
   - Duplicate back-office roles (dual ERP teams, redundant HR, overlapping finance)
   - Redundant regional sales coverage
   - Duplicated vendor relationships (same cloud provider, same audit firm)
4. **Quantify** savings with confidence ratings
5. **Estimate** costs to achieve (severance, lease breaks, migration costs)

**Time saved**: 15+ hours per synergy model.

### Output Format

```
## Synergy Map — [Target] + [Acquirer]

### Summary
| Category | Identified Run-Rate Savings | Costs to Achieve | Net Year 1 Impact |
|----------|---------------------------|-------------------|-------------------|
| Headcount | $[X]M | $[X]M | $[X]M |
| Third-Party Spend | $[X]M | $[X]M | $[X]M |
| Facilities | $[X]M | $[X]M | $[X]M |
| Technology | $[X]M | $[X]M | $[X]M |
| **Total** | **$[X]M** | **$[X]M** | **$[X]M** |

### Headcount Overlap
| Function | Target FTEs | Acquirer FTEs | Redundant | Savings | Confidence |
|----------|-------------|---------------|-----------|---------|------------|
| Finance & Accounting | [N] | [N] | [N] | $[X]K | High |
| IT Operations | [N] | [N] | [N] | $[X]K | Medium |
| Sales (Regional) | [N] | [N] | [N] | $[X]K | Low |

### Vendor Consolidation
| Vendor/Category | Target Spend | Acquirer Spend | Estimated Saving | Mechanism |
|----------------|-------------|----------------|-----------------|-----------|
| Cloud hosting | $[X]K | $[X]K | $[X]K | Volume renegotiation |
| Audit/Tax | $[X]K | $[X]K | $[X]K | Consolidate to single firm |

### Costs to Achieve
| Item | Estimate | Timing |
|------|----------|--------|
| Severance (redundant FTEs) | $[X]M | Months 1-6 |
| Lease termination penalties | $[X]K | Months 3-9 |
| IT migration costs | $[X]K | Months 1-12 |
| Retention bonuses (key talent) | $[X]K | Months 1-24 |
```

## Synergy and Cost Savings Report

The formal deliverable that moves beyond the mapping to a validated, defended analysis:

| Section | Focus |
|---------|-------|
| Synergy Thesis & Strategy | Strategic rationale and integration philosophy |
| Headcount & Organizational Overlap | Quantified role-level redundancies |
| Third-Party Spend Rationalization | Vendor pricing leverage and consolidation |
| Technology & Infrastructure | ERP migration, license elimination, real estate |
| Costs to Achieve | One-time expenditures: severance, lease breaks, IT migration |

## Operating Guidelines

- Synergies are notoriously overestimated — apply conservative assumptions
- Distinguish between **run-rate savings** (annual) and **one-time gains**
- Always include costs to achieve — synergies without execution costs are misleading
- Confidence ratings: **High** (contractual/observable), **Medium** (benchmarked), **Low** (estimated)
- Lenders demand third-party validation — ensure the analysis is independently defensible
- Revenue synergies are speculative and should be separated from cost synergies
- Flag any synergy that depends on retaining key personnel who may have flight risk
