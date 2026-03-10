---
name: monitoring
description: Status reporting, burndown analysis, risk reviews, dependency tracking, and project health checks for software and general PMs Use when user asks to "write a status report", "check project health", "track progress", or mentions burndown, RAG status, risk review, or earned value.
triggers:
  - status report
  - project status
  - rag status
  - burndown
  - burn down
  - velocity
  - risk review
  - dependency
  - health check
  - project health
  - earned value
  - spi
  - cpi
  - dora metrics
---

# Monitoring

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

---

## Status Reporting

Status reports exist for one reason: to surface the information that enables good decisions. A status report that does not lead to a decision, an escalation, or an action item is wasted effort. Every element in the report should answer one of three questions: "Are we on track?", "What needs attention?", or "What do we need from you?"

### RAG Status Framework

RAG (Red/Amber/Green) is the universal shorthand for project health. The problem is that most teams apply RAG subjectively -- "it feels green" -- which renders it meaningless. Define explicit, measurable criteria for each color across every dimension so that two different people reviewing the same data would assign the same color.

**RAG Criteria Table:**

| Dimension | Green | Amber | Red |
|-----------|-------|-------|-----|
| **Schedule** | On track or ahead. All milestones within 5% of planned dates. No critical path items slipping. | 1-2 milestones at risk of slipping by 1-2 weeks. Critical path has less than 1 week of float remaining. Recovery plan exists and is being executed. | Critical path milestone missed by >2 weeks. No credible recovery plan. End date at risk of moving. |
| **Scope** | Scope stable. Change requests processed through formal change control. No uncontrolled additions. | Minor scope creep detected (1-3 unapproved items in progress). Change request backlog growing. Scope boundary needs reinforcement. | Significant scope changes without approval. Team working on items not in the plan. Original objectives at risk of being displaced. |
| **Budget** | Spend within 5% of plan. Forecast to complete within approved budget. No unplanned expenditures. | Spend 5-10% over plan, or forecast to exceed budget by 5-10%. Contingency being consumed faster than planned. Corrective action identified. | Spend >10% over plan. Forecast exceeds approved budget. Contingency exhausted. Additional funding required. |
| **Risk** | All identified risks have owners, mitigations, and acceptable residual risk levels. No High-probability/High-impact risks without active mitigation. | 1-2 High risks with mitigations in progress but not yet effective. New risks emerging faster than being resolved. Risk register growing. | Multiple unmitigated High risks. Risk has materialized into an issue with no resolution plan. Project viability threatened. |
| **Team Health** | Team morale stable. Attrition at or below normal. Capacity matches demand. No overtime trend. Skills aligned to work. | Some team members working sustained overtime (>2 weeks). One key person at flight risk. Skills gap identified but not yet filled. | Key person has left or is leaving. Team burnout evident (quality dropping, absenteeism rising). Capacity insufficient for remaining scope. |

**How to use the table:** Score each dimension independently every reporting period. The overall project RAG is the worst single dimension -- a project that is Green on everything except Red on Risk is a Red project. Do not average. The weakest link defines the status.

### Software Mode: Sprint-Level Status

For software teams running sprints (Scrum, Kanban with cadence, or any time-boxed iteration), the sprint-level status report focuses on delivery throughput, quality, and operational health.

**Sprint Status Elements:**

- **Velocity vs. Plan:** Planned story points for the sprint vs. completed story points. Track the 4-sprint rolling average. If current sprint is tracking >20% below the rolling average at the midpoint, flag it Amber.
- **Burndown Shape:** Is the burndown following the ideal line, flat (blocked), or hockey-stick shaped (back-loaded)? See the Burndown section for shape analysis.
- **Blockers:** List every item that is blocked, who is blocking it, and when the block will be resolved. Blockers older than 2 business days should be escalated.
- **Deployment Status:** What has been deployed to production this sprint? What is queued for deployment? Any rollbacks?

**DORA Metrics:**

DORA (DevOps Research and Assessment) metrics measure software delivery performance. They are the industry standard for assessing engineering team effectiveness. Track these four metrics and compare against the benchmark table below.

| Metric | Definition | Elite | High | Medium | Low |
|--------|-----------|-------|------|--------|-----|
| **Deployment Frequency** | How often code is deployed to production | On-demand (multiple times per day) | Between once per day and once per week | Between once per week and once per month | Between once per month and once per six months |
| **Lead Time for Changes** | Time from code commit to running in production | Less than one hour | Between one day and one week | Between one week and one month | Between one month and six months |
| **Change Failure Rate** | Percentage of deployments that cause a failure in production | 0-15% | 16-30% | 31-45% | 46-60% |
| **Time to Restore Service** | Time to recover from a production failure | Less than one hour | Less than one day | Between one day and one week | More than one week |

**How to use DORA metrics in status reports:** Report current period values alongside the target tier your team is aiming for. Example: "Deployment Frequency: 3x/week (High tier -- target: daily by Q3)." Do not try to improve all four simultaneously. Pick the weakest metric and focus improvement efforts there. Improving deployment frequency without improving change failure rate creates more problems, not fewer.

**Sprint Status Template:**

```
SPRINT STATUS REPORT
======================
Sprint: [Sprint Name/Number]  |  Dates: [Start] - [End]
Team: [Team Name]             |  Report Date: [Date]

VELOCITY:
  Planned: [X] story points
  Completed: [Y] story points (as of report date)
  4-Sprint Rolling Average: [Z] points/sprint
  Variance: [+/-] [%] from plan

BURNDOWN: [On track / Flat / Hockey stick / Ahead]
  Notes: [Brief description of burndown shape and cause]

SPRINT GOAL: [The sprint goal statement]
  Status: [On track / At risk / Missed]

COMPLETED THIS SPRINT:
  - [Story/feature] ([X] points) -- deployed [yes/no]
  - [Story/feature] ([X] points) -- deployed [yes/no]
  - [Story/feature] ([X] points) -- deployed [yes/no]

IN PROGRESS:
  - [Story/feature] ([X] points) -- [% complete] -- [on track / blocked]
  - [Story/feature] ([X] points) -- [% complete] -- [on track / blocked]

BLOCKERS:
  | Item | Blocked By | Days Blocked | Resolution Owner | ETA |
  |------|-----------|-------------|-----------------|-----|
  |      |           |             |                 |     |

DEPLOYMENTS THIS SPRINT:
  - [Date]: [What was deployed] -- [Status: successful / rolled back]
  - [Date]: [What was deployed] -- [Status: successful / rolled back]

DORA METRICS (this period):
  Deployment Frequency: [value] ([tier])
  Lead Time for Changes: [value] ([tier])
  Change Failure Rate: [value] ([tier])
  Time to Restore Service: [value] ([tier])

RISKS/ISSUES:
  1. [Description] -- [Impact] -- [Mitigation/Owner]
  2. [Description] -- [Impact] -- [Mitigation/Owner]
  3. [Description] -- [Impact] -- [Mitigation/Owner]

DECISIONS NEEDED:
  - [Decision] -- needed by [date] -- from [person/group]
```

### General Mode: Project-Level Status

For non-software projects (business transformation, process improvement, facility build-out, marketing campaigns, consulting engagements), status reporting focuses on milestone progress, budget management, and resource utilization.

**Project-Level Status Elements:**

- **Milestone Progress:** Percentage complete for each milestone. Use a consistent methodology (see Percent Complete methods in the Burndown section). Show planned vs. actual completion dates.
- **Budget Burn Rate:** Planned expenditure vs. actual expenditure over time. Express as a percentage and as absolute dollars/hours. A project that has consumed 60% of its budget but completed only 40% of its scope is in trouble.
- **Resource Utilization:** Planned hours vs. actual hours by resource or resource category. Utilization above 90% for sustained periods signals overallocation and risk.
- **Critical Path Status:** Identify the longest chain of dependent tasks. Any delay on the critical path directly delays the project end date. Report critical path float (how much slack remains before the end date slips).

**Earned Value Metrics:**

Earned Value Management (EVM) is the most rigorous method for measuring project performance. It integrates scope, schedule, and cost into a single analytical framework. Use these formulas and the interpretation guide below.

**Core Earned Value Formulas:**

| Metric | Abbreviation | Formula | What It Tells You |
|--------|-------------|---------|-------------------|
| Planned Value | PV | Budget allocated for work scheduled to date | How much work should be done by now |
| Earned Value | EV | Budget allocated for work actually completed to date | How much work is actually done |
| Actual Cost | AC | Total cost incurred for work completed to date | How much you have spent |
| Schedule Variance | SV | EV - PV | Are you ahead or behind schedule? (positive = ahead) |
| Cost Variance | CV | EV - AC | Are you under or over budget? (positive = under budget) |
| Schedule Performance Index | SPI | EV / PV | Efficiency of schedule execution (1.0 = on plan) |
| Cost Performance Index | CPI | EV / AC | Efficiency of cost execution (1.0 = on budget) |
| Estimate at Completion | EAC | BAC / CPI | Projected total cost based on current efficiency |
| Estimate to Complete | ETC | EAC - AC | How much more will it cost to finish |

**Interpretation Guide:**

| SPI Value | Meaning | Action |
|-----------|---------|--------|
| > 1.1 | Significantly ahead of schedule | Verify accuracy. Consider redeploying resources to other projects. |
| 1.0 - 1.1 | On track | Continue current execution plan. |
| 0.9 - 1.0 | Slightly behind | Monitor closely. Identify specific tasks causing delay. |
| 0.8 - 0.9 | Behind schedule | Activate recovery plan. May need to add resources or reduce scope. |
| < 0.8 | Seriously behind | Escalate immediately. Re-baseline the project plan. |

| CPI Value | Meaning | Action |
|-----------|---------|--------|
| > 1.1 | Significantly under budget | Verify accuracy. May indicate under-scoped work or quality shortcuts. |
| 1.0 - 1.1 | On budget | Continue current execution plan. |
| 0.9 - 1.0 | Slightly over budget | Identify cost drivers. Look for efficiency gains. |
| 0.8 - 0.9 | Over budget | Formal cost review. May need to reduce scope or find savings. |
| < 0.8 | Seriously over budget | Escalate immediately. Project economics are failing. |

**Worked Example:**

```
Project: Office Relocation
Budget at Completion (BAC): $500,000
Report Date: End of Month 3 (of 6)

Planned Value (PV):  $250,000  (50% of work was scheduled to be done by now)
Earned Value (EV):   $200,000  (40% of work is actually complete)
Actual Cost (AC):    $230,000  (actual spend to date)

Schedule Variance (SV):  $200,000 - $250,000 = -$50,000  (behind schedule)
Cost Variance (CV):      $200,000 - $230,000 = -$30,000  (over budget)

SPI:  $200,000 / $250,000 = 0.80  (delivering 80 cents of work per planned dollar)
CPI:  $200,000 / $230,000 = 0.87  (getting 87 cents of value per dollar spent)

EAC:  $500,000 / 0.87 = $574,713  (projected total cost at current efficiency)
ETC:  $574,713 - $230,000 = $344,713  (still need to spend this much)

Interpretation: The project is behind schedule (SPI 0.80) AND over budget
(CPI 0.87). At current rates, it will cost $574,713 instead of $500,000 --
a $74,713 overrun. The PM should escalate to the steering committee, present
recovery options (reduce scope, add resources, extend timeline), and get a
decision within 1 week.
```

### Status Report Template (1-Page)

This template works for both software and general PMs. Tailor the metrics section to your mode.

```
PROJECT STATUS REPORT
=======================
Project: _______________
Report Date: _______________  |  Reporting Period: [dates]
PM: _______________           |  Sponsor: _______________

RAG SUMMARY:
| Dimension     | Status | Trend     | Notes                          |
|---------------|--------|-----------|--------------------------------|
| Schedule      | [R/A/G]| [up/down/flat] | [one-line explanation]    |
| Scope         | [R/A/G]| [up/down/flat] | [one-line explanation]    |
| Budget        | [R/A/G]| [up/down/flat] | [one-line explanation]    |
| Risk          | [R/A/G]| [up/down/flat] | [one-line explanation]    |
| Team Health   | [R/A/G]| [up/down/flat] | [one-line explanation]    |
| OVERALL       | [R/A/G]| [up/down/flat] |                            |

KEY ACCOMPLISHMENTS (this period):
1. [Accomplishment with measurable impact]
2. [Accomplishment with measurable impact]
3. [Accomplishment with measurable impact]
4. [Accomplishment with measurable impact] (optional)
5. [Accomplishment with measurable impact] (optional)

UPCOMING MILESTONES:
| Milestone | Planned Date | Forecast Date | Status | Owner |
|-----------|-------------|---------------|--------|-------|
|           |             |               |        |       |
|           |             |               |        |       |
|           |             |               |        |       |

RISKS & ISSUES (Top 3):
| # | Type      | Description | Impact | Probability | Mitigation         | Owner |
|---|-----------|-------------|--------|-------------|--------------------|-------|
| 1 | [Risk/Issue] |          | [H/M/L]| [H/M/L]    | [Action + ETA]     |       |
| 2 | [Risk/Issue] |          | [H/M/L]| [H/M/L]    | [Action + ETA]     |       |
| 3 | [Risk/Issue] |          | [H/M/L]| [H/M/L]    | [Action + ETA]     |       |

DECISIONS NEEDED:
- [Decision description] -- Needed by [date] -- From [person/group]
- [Decision description] -- Needed by [date] -- From [person/group]

HELP NEEDED:
- [What you need] -- From [person/team] -- By [date]
- [What you need] -- From [person/team] -- By [date]
```

### Audience-Specific Formatting

The same underlying data should be packaged differently depending on who is reading it. Sending the engineering team a three-bullet executive summary wastes their time. Sending the CEO a five-page sprint report wastes theirs.

**Executive Audience (CEO, VP, C-Suite):**

Format: 3 bullets, 1 paragraph max. Delivered via email or Slack message, not a deck.

- Overall RAG status with one-sentence explanation of any non-Green dimensions
- The single most important risk or decision that needs their attention
- One key metric showing trajectory (velocity trend, budget burn rate, milestone completion %)

Example: "Project Aurora: Amber overall. Schedule slipped 1 week due to vendor delay on API integration (recovery plan in place, back on track by March 15). Budget on track. Decision needed: approve $12K additional spend for temporary contractor to parallelize the blocked workstream. Current velocity: 34 points/sprint (target: 38)."

**Team Audience (Engineers, Designers, Analysts):**

Format: Full detail. Sprint status report or project status report as templated above. Shared in a team wiki or project channel.

Include: Every metric, every blocker, every action item. The team needs granular visibility to do their work. Do not summarize away the details they need to self-organize and unblock each other.

**Steering Committee Audience:**

Format: RAG summary table + decisions needed + budget snapshot. Delivered as a 2-3 slide deck or 1-page document.

Content:
- RAG table with trend arrows (is each dimension improving or worsening?)
- Budget: planned vs. actual spend, forecast to complete, variance explanation
- Top 3 risks with mitigation status and any escalation requests
- Decisions needed with options and PM recommendation
- No sprint-level detail. No individual task status. No blockers unless they require steering committee intervention.

### Status Report Anti-Patterns

**All-Green Syndrome:**

The project reports Green across all dimensions for weeks or months, then suddenly flips to Red. This means the status was not being assessed honestly -- problems were growing beneath a veneer of optimism. Causes: PM fears delivering bad news; stakeholders punish Amber/Red status; criteria are too vague ("it feels okay"). Fix: Define explicit, measurable RAG criteria (use the table above). Reward early Amber reports that come with recovery plans. A team that reports Amber early and recovers is performing better than a team that hides problems until they become unrecoverable.

**Burying Bad News:**

The report is technically accurate but buries concerning information in the middle of a wall of text, or frames serious issues with minimizing language ("slight delay" when the delay is 3 weeks; "minor budget pressure" when you have exceeded contingency). Fix: Lead with the worst news. Put the most concerning item at the top. Use direct language. "We are 3 weeks behind schedule on the critical path. Here is our recovery plan." Stakeholders respect directness. They do not respect discovering bad news that was hidden from them.

**Report as CYA (Cover Your Actions):**

The status report exists primarily to create a paper trail protecting the PM, not to communicate useful information. Symptoms: excessive detail about what the PM did (rather than what the project achieved), defensive language pre-emptively blaming other teams, and no actionable decisions or asks. Fix: Every status report should contain at least one decision request or action item for someone other than the PM. If the report does not ask for anything, it is not driving the project forward -- it is just documentation theater.

---

## Burndown & Forecasting

---

## References

For detailed burndown analysis and forecasting guidance: [references/monitoring-reference.md](references/monitoring-reference.md)

- Sprint Burndown (Software Mode)
- Milestone Burndown (General Mode)
- Forecast Accuracy Tracking
- Warning Signs in Burndown Shapes
- Forecasting Anti-Patterns

