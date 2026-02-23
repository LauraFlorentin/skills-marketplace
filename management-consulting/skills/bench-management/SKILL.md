---
name: "Bench Management & Activity Tracker"
description: >
  Track and optimize consulting bench utilization. Captures consultant
  availability, activity types (RFP/proposal work, POV development, internal
  engagement, thought leadership, training, business development, practice
  development, mentoring), and generates structured bench status reports with
  idle-time alerts, pipeline alignment, and staffing recommendations.
version: "1.0"
author: "LauraFlorentin"
---

# Bench Management & Activity Tracker

In consulting firms, "the bench" refers to consultants not currently assigned to billable client projects. Bench time should be tracked and optimized — consultants on the bench are not idle; they work on internal activities that drive future revenue and firm capability.

## When to Use

- Generating a bench status report for leadership
- Tracking which consultants are available and what they're working on
- Identifying idle consultants who need immediate activity assignment
- Aligning bench work with upcoming pipeline opportunities
- Optimizing utilization rates across the practice

## Consultant Activity Types

For each consultant on the bench, capture and maintain:

1. **Availability status**: Available now, partially available, ramping off a project, on planned leave
2. **Current activity type** (one or more):
   - RFP/Proposal work — responding to Requests for Proposals
   - POV development — building Proof of Value / Proof of Concept demos
   - Internal engagement — supporting internal firm initiatives (e.g., recruiting, L&D, DE&I)
   - Thought leadership — writing whitepapers, blog posts, presenting at events
   - Training & certification — upskilling, completing certifications
   - Business development — supporting sales pursuits, client relationship building
   - Practice development — building accelerators, templates, methodologies, reusable assets
   - Mentoring/coaching — supporting junior consultants
   - Bench idle — no active assignment (flag for immediate action)
3. **Activity details**: Brief description, expected duration, deliverable, sponsoring partner/lead
4. **Skills & interests**: Relevant for matching to upcoming opportunities

## Report Format

When generating a bench status report, use this structure:

```
## Bench Status Report — [Date]
**Total on bench**: [N] | **Avg. bench duration**: [X days] | **Utilization target gap**: [Y%]

### 🔴 Immediate Action (Idle > 5 days)
| Consultant | Days on Bench | Skills | Last Project |
|---|---|---|---|

### By Activity Type
**RFP/Proposal Work** ([N] consultants)
- [Name] — [RFP name], [expected submission date], [staffing lead]

**POV Development** ([N] consultants)
- [Name] — [POV topic], [client/target], [expected completion]

[...repeat for each activity type...]

### Pipeline Alignment Opportunities
- [Consultant] skills match → [Upcoming opportunity]

### Recommendations
- [Actionable recommendations based on the data]
```

## Escalation Rules

- **Idle > 5 business days** — Urgent: flag for immediate action
- **Bench activities misaligned with pipeline** — Flag for realignment
- **Approaching 3+ weeks on bench** — Escalation to leadership needed

## Operating Guidelines

- Always ask for the time period if not specified
- If a consultant has no activity logged, flag them as "bench idle" — never assume they are busy
- Distinguish between billable bench (e.g., waiting for SOW signature) and non-billable bench
- Keep descriptions concise — one line per consultant per activity
- When suggesting activity assignments, prioritize: (1) pipeline-aligned work, (2) skills development for high-demand areas, (3) thought leadership
- If activity type is ambiguous, ask the user to clarify
- If data is incomplete, produce what you can and clearly list what information is missing
