---
name: "Q&A Management"
description: >
  Diligence Q&A process acceleration. Synthesizes approved VDR documents,
  disclosure schedules, and prior responses to auto-draft defensible answers
  to buyer diligence questions. Routes drafts for expert approval while
  maintaining consistency across a multi-bidder auction process.
version: "1.0"
author: "LauraFlorentin"
---

# Q&A Management

As transactions enter confirmatory diligence, the Q&A process can devolve into a logistical nightmare. Multiple bidders submit hundreds of granular questions about tax liabilities, employee benefits, and IT infrastructure. Junior deal team members become administrative traffic cops, routing questions, chasing answers, and formatting responses.

## When to Use

- Responding to buyer diligence question trackers
- Managing multi-bidder Q&A in a sell-side auction
- Ensuring consistency in seller representations across bidders
- Drafting responses using approved VDR documents and disclosure schedules

## The /draft-qna Protocol

### How It Works

1. **Connect** to approved VDR documents, existing disclosure schedules, and prior Q&A
2. **Analyze** each buyer question to identify the relevant data source
3. **Draft** a preliminary response synthesizing approved materials
4. **Cross-reference** against previously answered questions for consistency
5. **Flag** for expert approval with routing recommendations
6. **Track** response status across all bidders

### Output Format

```
## Q&A Response Draft

### Question [#]
**From**: [Bidder name]
**Category**: [Financial / Legal / HR / Operations / IT / Tax]
**Question**: [Full question text]

**Draft Response**:
[Response synthesized from approved materials]

**Sources Used**:
- [VDR document reference and folder path]
- [Prior Q&A reference if applicable]

**Routing**: → [CFO / General Counsel / CTO] for approval
**Sensitivity**: [Standard / Restricted / Highly Confidential]
**Consistency Check**: [Aligned with prior responses / POTENTIAL CONFLICT with Q#X]
```

### Multi-Bidder Consistency Tracking

```
## Q&A Consistency Matrix

| Topic | Bidder A Response | Bidder B Response | Consistent? |
|-------|------------------|------------------|-------------|
| EBITDA adjustments | Referenced QoE §3.2 | Referenced QoE §3.2 | ✅ |
| Customer concentration | Disclosed top 10 = 45% | Disclosed top 5 = 38% | ⚠️ REVIEW |
| Pending litigation | Full disclosure | Full disclosure | ✅ |
```

## Operating Guidelines

- Never disclose information beyond what's been approved for the current diligence phase
- Maintain strict information barriers between bidders in a competitive auction
- Flag any question that could require disclosure of material non-public information
- Cross-reference every response against prior answers to prevent contradictions
- Route tax questions to tax counsel, employment questions to labor counsel
- Track response turnaround time — delays signal deal fatigue to bidders
- Preserve the Q&A log as it becomes part of the deal's legal record

**Time saved**: 30 minutes per query, preventing coordination bottlenecks and ensuring consistency.
