---
name: workflow-chains
description: >
  End-to-end M&A pipeline orchestration — chains individual slash commands
  and report generators into continuous operational pipelines. Three core
  Use when user asks to "chain M&A workflows", "end-to-end deal process", "deal lifecycle", or mentions workflow automation, multi-phase deals, or deal coordination.
  chains: Origination-to-IOI (7 days → 4 hours), VDR Drop-to-Red Flag
  (5 days → 6 hours), and Synergy-to-Day 1 Integration (3 weeks → 3 days).
version: "1.0"
author: "LauraFlorentin"
---

# Workflow Chains

The highest evolution of AI in M&A advisory: strategic sequencing of individual commands and report generators into continuous, end-to-end operational pipelines. Chains compress multi-week processes into single-day turnarounds.

## When to Use

- Running a full origination-to-bid pipeline on a new target
- Processing a fresh VDR drop into actionable diligence intelligence
- Transitioning from signed purchase agreement to Day 1 integration readiness
- Any scenario requiring sequential execution of multiple M&A commands

---

## Chain 1: "Origination to IOI" Pipeline

**Time compressed**: 7 days → 4 hours

When an attractive asset hits the market, speed-to-bid dictates survival in the auction. Late followers get outbid or excluded entirely.

### Sequence

```
Step 1: /cim-extract
  ↓ Output: Sanitized financial metrics, growth assumptions, concentration data
Step 2: Financial Model Integration
  ↓ Feed extracted data into standardized DCF/LBO models for baseline valuation
Step 3: /draft-ioi
  ↓ Generate customized IOI mapping buyer's advantages to CIM's growth pillars
  → Deliverable: Bespoke IOI letter ready for investment committee
```

### Result

The entire origination-to-bid cycle completes before competing firms have scheduled their initial review meetings.

---

## Chain 2: "VDR Drop to Initial Red Flag Report" Pipeline

**Time compressed**: 5 days → 6 hours

When a buyer gains VDR access, the race to uncover liabilities begins. Delays cause severe deal fatigue.

### Sequence

```
Step 1: /vdr-classify
  ↓ Ingest 5,000+ file document dump → auto-categorize into Legal/Financial/HR/Ops
Step 2: /flag-coc + /schedule-disclosure (parallel)
  ↓ Simultaneously scan for CoC risks AND extract core representations
Step 3: Red Flag Report Generation
  ↓ Route outputs into Red Flag template → populate Executive Risk Summary
  → Deliverable: Pre-populated Red Flag Report for consultant review
```

### Result

Consultant reviews the pre-populated report the next morning, refines legal interpretations, and delivers actionable intelligence to the investment committee days ahead of schedule.

---

## Chain 3: "Synergy Underwriting to Day 1 Integration Readiness"

**Time compressed**: 3 weeks → 3 days

After the Purchase Agreement is signed and price is locked, focus shifts to value capture. Failure to execute rapidly means synergy leakage and talent attrition.

### Sequence

```
Step 1: /synergy-map
  ↓ Model overlapping operational footprints, redundant licenses, duplicate vendors
Step 2: Synergy Report Generation
  ↓ Compile into validated Synergy & Cost Savings Analysis for lenders/board
Step 3: PMI Target Operating Model Generation
  ↓ Feed synergy data into integration planning:
    - Headcount redundancies → HR workstream 30-day severance/retention checklist
    - Duplicate vendors → IT/Procurement workstream with termination dates & penalties
    - Facility overlaps → Real estate workstream with lease break timeline
  → Deliverable: Executable Day 1 roadmap
```

### Result

Seamless transition from theoretical valuation modeling to a concrete, executable integration plan — rigorous and instantaneous.

---

## Chain Execution Guidelines

- Each chain step should complete before the next begins — outputs are inputs
- At each transition point, the consultant should **review and validate** before proceeding
- Chains are templates — adapt the sequence based on deal-specific requirements
- Document the chain execution log for audit trail and post-deal review
- If any step produces unexpected results, halt the chain and investigate
- The consultant's role shifts from execution to **validation and strategic interpretation**


## Examples

**Input**: "Run the full sell-side process chain for a $120M transaction."

**Workflow chain output**:
```
[Week 1]  VDR Setup        → /vdr-setup completed, 847 docs indexed
[Week 2]  Deal Marketing   → Teaser + CIM drafted, distributed to 12 strategic + 8 PE buyers
[Week 3]  Screening        → 9 IOIs received, 6 qualify; management presentation scheduled
[Week 5]  Diligence Open   → Q&A log active: 47 questions received, 41 answered
[Week 7]  Final Bids       → 3 LOIs received, best at $127M (10.6x EBITDA)
[Week 9]  Docs + Close     → Regulatory filing submitted, SPA negotiation underway
```


## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Workflow chain stalls at one stage | Missing prerequisite output | Check each stage's output schema; ensure data is passed completely |
| Parallel workstreams fall out of sync | No shared status tracker | Use a deal management tracker with stage gates and owner assignments |
| Chain runs wrong skill | Ambiguous trigger | Explicitly name each skill step in the chain rather than relying on auto-trigger |
