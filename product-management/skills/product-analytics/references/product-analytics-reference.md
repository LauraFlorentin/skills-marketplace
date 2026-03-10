# Product Analytics — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Dashboard Design

Dashboards translate your metrics framework into something the team can actually use. A good dashboard tells a story in 30 seconds. A bad dashboard is a graveyard of charts nobody looks at.

### Startup Mode: Single-Page Scorecard

For early-stage teams, one page is enough. If your dashboard does not fit on one screen, it has too much on it. Update it weekly. Make it the first thing the team sees in the Monday standup.

**Single-Page Scorecard Template:**

```
PRODUCT SCORECARD — Week of _______________
=============================================

NORTH STAR: [Metric Name]
  Current: ______    Last Week: ______    4-Week Trend: ______
  Target:  ______    Status: [On Track / At Risk / Off Track]

  4-Week Trend:
  |         *
  |       *
  |     *   *
  |   *
  +---+---+---+---
   W-3  W-2  W-1  Now

INPUT METRICS:
  Metric                Current   Prev    Trend   Status
  -----------------------------------------------------------
  New signups           ______    ______  [^ v -] [G/Y/R]
  Activation rate       ______%   ______% [^ v -] [G/Y/R]
  Day-7 retention       ______%   ______% [^ v -] [G/Y/R]
  Reactivated users     ______    ______  [^ v -] [G/Y/R]

ACQUISITION FUNNEL (this week):
  Visitors:     ______ (100%)
  Signups:      ______ (__%)    <-- Visitor-to-signup rate
  Activated:    ______ (__%)    <-- Signup-to-activation rate
  Retained W1:  ______ (__%)    <-- Activation-to-retention rate

RETENTION CURVE (current cohort):
  Week 1:  ____%
  Week 2:  ____%
  Week 4:  ____%
  Week 8:  ____%
  Week 12: ____%

NOTES / CONTEXT:
  [1-2 sentences: Anything unusual this week? Launches,
   outages, press coverage, seasonality?]
```

**Rules for the startup scorecard:**

- One page, no scrolling.
- Updated every Monday morning.
- Visible to the entire team (pinned in Slack, projected on a wall, bookmarked in the browser).
- Color-coded: Green = on track, Yellow = needs attention, Red = off track.
- Trend arrows: Up, down, or flat compared to last week.
- Context section is mandatory. Numbers without context are dangerous.

### Enterprise Mode: Multi-Level Dashboards

Mature organizations need dashboards at multiple levels. Each level serves a different audience with different cadences and different levels of detail.

#### Executive Dashboard

**Audience:** C-suite, board members, investors.
**Cadence:** Monthly refresh.
**Purpose:** Answer "Is the business healthy?" in under 60 seconds.
**Rule:** No feature-level detail. Executives do not need to know the click-through rate on the onboarding tooltip. They need to know if the business is growing, healthy, and on track.

**Contents:**

| Metric | Current | vs. Last Month | vs. Target | Trend (3-month) |
|---|---|---|---|---|
| North Star Metric | ______ | ______ | ______ | [chart] |
| Revenue (MRR/ARR) | $______ | ______ | ______ | [chart] |
| Growth rate (MoM) | ______% | ______ | ______ | [chart] |
| Customer count | ______ | ______ | ______ | [chart] |
| NPS | ______ | ______ | ______ | [chart] |

Plus: 3-bullet executive summary at the top. One paragraph of context. List of top 3 risks.

#### Team Dashboard

**Audience:** Product managers, engineering leads, designers.
**Cadence:** Weekly refresh.
**Purpose:** Answer "Are our current initiatives moving the right metrics?"

**Contents:**

| Metric | Current | vs. Last Week | Target | Owner |
|---|---|---|---|---|
| Feature adoption rate (core feature) | ______% | ______ | ______ | PM |
| Funnel conversion by step | ______% | ______ | ______ | Growth |
| NPS by segment | ______ | ______ | ______ | Product |
| Sprint velocity (story points) | ______ | ______ | ______ | Eng Lead |
| Defect rate (bugs per release) | ______ | ______ | ______ | Eng Lead |

#### Feature Dashboard

**Audience:** Engineers, individual PMs, QA.
**Cadence:** Real-time or daily.
**Purpose:** Answer "Is this feature working correctly and being used as expected?"

**Contents:**

| Metric | Value | Threshold | Status |
|---|---|---|---|
| DAU (feature-specific) | ______ | ______ | [G/Y/R] |
| Sessions per user per day | ______ | ______ | [G/Y/R] |
| Key actions per session | ______ | ______ | [G/Y/R] |
| Error rate | ______% | < 0.1% | [G/Y/R] |
| Latency p50 | ______ ms | < 200 ms | [G/Y/R] |
| Latency p95 | ______ ms | < 500 ms | [G/Y/R] |
| Latency p99 | ______ ms | < 1000 ms | [G/Y/R] |
| Support tickets (this feature) | ______ | ______ | [G/Y/R] |

### Dashboard Spec Template

For each metric on any dashboard, document the specification before building the visualization. Ambiguous definitions are the number-one cause of teams arguing about metrics instead of acting on them.

**Per-metric spec:**

```
METRIC SPECIFICATION
=====================
Name:           [Human-readable name, e.g., "Weekly Active Users"]
Definition:     [Exact calculation, e.g., "Count of unique users who
                 performed at least one core action in the past 7 days.
                 Core actions: create project, complete task, comment.
                 Excludes: admin users, internal test accounts."]
Data source:    [Where the data comes from, e.g., "events.user_action
                 table in Snowflake, filtered by action_type IN
                 ('create_project','complete_task','comment')"]
Refresh cadence:[How often the metric updates, e.g., "Daily at 06:00 UTC"]
Owner:          [Person responsible for the metric's accuracy and
                 for investigating anomalies]
Alert threshold:[When to page someone, e.g., "Alert if WAU drops >15%
                 week-over-week or if data pipeline is >4 hours stale"]
Visualization:  [Chart type, e.g., "Line chart, 12-week trend,
                 with target line overlay"]
```

**Why this matters:** Without a spec, two dashboards will show different numbers for the "same" metric because they use different definitions, filters, or time windows. This destroys trust in data. Write the spec once and treat it as the source of truth.

### Visualization Best Practices

**Choose chart type by data type:**

| Data Question | Chart Type | Example |
|---|---|---|
| How does this change over time? | **Line chart** | WAU over 12 weeks |
| How do things compare? | **Bar chart** | Conversion rate by acquisition channel |
| What is the composition? | **Stacked bar chart** | Revenue by plan tier over time |
| What is the distribution? | **Histogram** | Session duration distribution |
| What is the current value? | **Big number / KPI card** | Current MRR |
| What is the relationship? | **Scatter plot** | Feature usage vs. retention |

**Avoid these charts:**

- **Pie charts:** Human eyes are bad at comparing angles. A bar chart conveys the same information more accurately. The only acceptable use of a pie chart is when you have 2-3 segments and the exact percentages matter less than the rough proportions.
- **3D charts:** They distort proportions and add no information. Never use them.
- **Dual-axis charts:** Two Y-axes on the same chart are misleading because the scales can be manipulated to imply false correlations. Use two separate charts side by side instead.

**General principles:**

- **Show trends, not snapshots.** A single number without context is meaningless. Always show the current value plus its trend over time (at minimum, vs. last period).
- **Include comparison.** Show the metric vs. last period and vs. target. This gives immediate context: Are we improving? Are we on track?
- **Use color sparingly.** Reserve red and green for status indicators (off track / on track). If everything is colorful, nothing stands out. Default to neutral colors (grays, blues) for data series.
- **Label axes and include units.** Every chart should have a title, labeled axes, and units. "Revenue" is incomplete. "$MRR (thousands)" is clear.
- **Start Y-axis at zero for bar charts.** Truncating the Y-axis on bar charts exaggerates differences and misleads viewers. Line charts may start at a non-zero value when showing small changes in a large base, but label this clearly.

---

## Sprint Review

A sprint review is the team's regular checkpoint to assess what shipped, what impact it had, and what the team learned. It is not a status update. It is a feedback loop that connects execution to outcomes.

### What to Cover

Every sprint review should address three questions, in this order:

**1. What shipped?**

List features, fixes, and improvements that were released to users this sprint. For each, include:
- Brief description (1 sentence).
- Link to PRD, ticket, or design doc.
- Whether it shipped to 100% of users or is behind a feature flag / in limited rollout.

**2. What didn't ship, and why?**

Be honest about what was planned but not delivered. For each item:
- What was the blocker? (Technical complexity underestimated, dependency on another team, scope change, unexpected bug.)
- Is it rolling into next sprint, or is the approach being reconsidered?

**3. Demo of key features.**

Show the product, not slides. Demo the most significant shipped feature in the actual product (or staging environment). Let stakeholders see and interact with real output.

### Metrics Impact

After covering what shipped, connect execution to outcomes:

**What moved:**

| Metric | Before | After | Change | Why |
|---|---|---|---|---|
| Activation rate | 28% | 33% | +5 pp | New onboarding flow launched to 100% |
| Day-7 retention | 42% | 41% | -1 pp | No change expected this sprint |

**What didn't move (but was expected to):**

| Metric | Expected Change | Actual | Hypothesis for Gap |
|---|---|---|---|
| Feature adoption (export) | +10% | +2% | Export button is discoverable but export format doesn't meet user needs -- need user research |

**Unexpected changes:**

Flag any metric that moved significantly without a clear cause. These are the most important signals to investigate because they may indicate user behavior changes, data pipeline issues, or external factors (competitor launch, press coverage, seasonality).

### User Feedback

Quantitative data tells you what happened. Qualitative data tells you why. Every sprint review should include a brief summary of user signals:

- **Support tickets:** Volume trend, top categories, any emerging themes.
- **User interviews:** Summary of any interviews conducted this sprint. What did you learn?
- **NPS comments:** Notable verbatims from detractors and promoters.
- **Social media / community:** Any notable mentions, complaints, or praise.

**Synthesize into top 3 themes.** Do not dump a list of 30 support tickets into the review. Identify the 3 most important themes and explain what action (if any) the team is taking.

### Startup Mode: Weekly Standup Format

For small teams, the sprint review should be a 5-minute async-friendly update. Do not schedule a 60-minute meeting for a team of 5. Post a Loom video or a structured Slack message instead.

**Startup Sprint Review Template:**

```
WEEKLY UPDATE — Week of _______________
========================================
Team: _______________

SHIPPED:
  - [Feature/fix]: [1-sentence description] [link]
  - [Feature/fix]: [1-sentence description] [link]

DID NOT SHIP:
  - [Item]: [Why] [New ETA or dropped]

METRIC CHECK:
  North Star ([metric name]): [value] ([trend: up/down/flat])
  Key input:  [metric]: [value] ([trend])
  Key input:  [metric]: [value] ([trend])

USER SIGNAL:
  [1-2 sentences: Top theme from support/feedback this week]

NEXT WEEK:
  - [Planned item 1]
  - [Planned item 2]

BLOCKER:
  [If any — otherwise "None"]
```

**Delivery:** Post this in Slack every Monday. Record a 3-minute Loom video if a demo is warranted. Reply in thread with questions. No meeting required unless a blocker needs real-time discussion.

### Enterprise Mode: Formal Sprint Review

For larger teams with multiple stakeholders, a structured 60-minute meeting ensures alignment and gives stakeholders a voice.

**Enterprise Sprint Review Agenda (60 min):**

```
SPRINT REVIEW — Sprint [#] ([dates])
======================================
Product: _______________
PM: _______________
Attendees: [list]

1. DEMO (20 min)
   Show the most significant features shipped this sprint.
   Use the actual product or staging environment.
   - Feature A: [demo + context]
   - Feature B: [demo + context]
   - Feature C: [demo + context]

2. METRICS READOUT (15 min)
   North Star: [value] vs. [target] — [trend]

   Metrics that moved:
   | Metric | Before | After | Cause |
   |--------|--------|-------|-------|
   |        |        |       |       |

   Metrics that didn't move (expected):
   | Metric | Expected | Actual | Hypothesis |
   |--------|----------|--------|------------|
   |        |          |        |            |

   Unexpected changes:
   | Metric | Change | Investigation Status |
   |--------|--------|----------------------|
   |        |        |                      |

3. USER FEEDBACK (10 min)
   Support ticket volume: [#] ([trend])
   Top 3 themes:
     1. [Theme]: [summary + action]
     2. [Theme]: [summary + action]
     3. [Theme]: [summary + action]

   Notable user quotes:
     - "[verbatim]" — [user segment]
     - "[verbatim]" — [user segment]

4. STAKEHOLDER Q&A (10 min)
   Open floor for questions, concerns, and feedback.
   [Capture questions and answers in notes]

5. ACTION ITEMS (5 min)
   | Action | Owner | Due Date |
   |--------|-------|----------|
   |        |       |          |
```

### Sprint Health Metrics

Beyond product metrics, track the health of the sprint process itself. These metrics help engineering leads and PMs identify systemic execution issues.

| Metric | Definition | Healthy Range | Warning Sign |
|---|---|---|---|
| **Velocity trend** | Story points completed per sprint (3-sprint rolling average) | Stable +/- 15% | Declining over 3+ sprints = capacity issue, technical debt, or unclear requirements |
| **Commitment accuracy** | % of planned stories that were actually delivered | 80-90% | Below 70% = chronic over-commitment or too many mid-sprint interruptions |
| **Defect escape rate** | Bugs found in production per release | Trending down or stable | Trending up = quality process gaps; review testing and code review practices |
| **Cycle time by story size** | Calendar days from "In Progress" to "Done" by story point size | Small (1-3 pts): 1-3 days, Medium (5-8 pts): 3-7 days, Large (13+ pts): break it down | Stories consistently exceeding expected cycle time = estimation or scoping problems |

**How to use sprint health metrics:** Review these at the sprint retrospective, not the sprint review. The review is about product outcomes. The retrospective is about process improvement. Do not conflate them.

---

## Product Review

A product review is a cross-cutting assessment of the entire product, not just the last sprint. It steps back from the execution details and asks: Is this product healthy? Are we building the right things? Are we winning?

Product reviews trigger the orchestrator agent for multi-stage analysis, pulling together signals from strategy, discovery, execution, and growth into a unified assessment.

### Strategy Alignment

**Are we building toward the vision?**

- Review the product vision statement. Has anything changed in the market or company strategy that makes the vision need updating?
- List the top 3 initiatives currently in progress. For each, explain how it connects to the vision. If the connection is weak or indirect, flag it.

**Are OKRs on track?**

Score each objective's key results on a 0.0-1.0 scale:

```
Objective 1: [Name]
  KR 1.1: [Description] — Score: __/1.0
  KR 1.2: [Description] — Score: __/1.0
  KR 1.3: [Description] — Score: __/1.0
  Objective Score: __/1.0

Objective 2: [Name]
  KR 2.1: [Description] — Score: __/1.0
  KR 2.2: [Description] — Score: __/1.0
  KR 2.3: [Description] — Score: __/1.0
  Objective Score: __/1.0

Overall OKR Score: __/1.0
```

**Has the competitive landscape changed?**

Summarize any material competitive moves since the last review: new entrants, funding rounds, major feature launches, pricing changes, acquisitions. Assess whether any of these require a strategic response (refer to the competitive response framework in the Product Strategy skill).

### Discovery Health

Discovery health measures whether the team is staying connected to users and feeding those insights into the product.

| Signal | This Period | Last Period | Target | Status |
|---|---|---|---|---|
| User conversations conducted | ______ | ______ | 10+ per quarter | [G/Y/R] |
| Insights added to research repository | ______ | ______ | ______ | [G/Y/R] |
| % of roadmap items with user evidence | ______% | ______% | 80%+ | [G/Y/R] |
| Last persona refresh | ______ | -- | Within 6 months | [G/Y/R] |
| Last jobs-to-be-done update | ______ | -- | Within 6 months | [G/Y/R] |

**Red flags:**

- Zero user conversations in the past month means the team is building blind.
- Less than 50% of roadmap items supported by user evidence means the roadmap is driven by opinion, not insight.
- Personas or JTBD documents older than 12 months are stale and may be misleading the team.

### Execution Quality

| Metric | Current | Trend (3-period) | Target | Status |
|---|---|---|---|---|
| Sprint velocity (3-sprint avg) | ______ | [chart/arrows] | Stable | [G/Y/R] |
| Defect rate (bugs/release) | ______ | [chart/arrows] | Declining | [G/Y/R] |
| Cycle time — small stories (1-3 pts) | ______ days | [chart/arrows] | 1-3 days | [G/Y/R] |
| Cycle time — medium stories (5-8 pts) | ______ days | [chart/arrows] | 3-7 days | [G/Y/R] |
| Definition of Done compliance | ______% | [chart/arrows] | 95%+ | [G/Y/R] |
| Tech debt ratio (% of sprint on debt) | ______% | [chart/arrows] | 15-25% | [G/Y/R] |

**Definition of Done compliance:** Measure how often stories meet all DoD criteria (code reviewed, tests passing, documentation updated, product sign-off) before being marked complete. Low compliance means the team is cutting corners and quality will degrade over time.

### Growth Metrics

#### Funnel Performance

Track conversion at each stage of the user journey. The funnel should be reviewed at every product review to identify where users are dropping off.

```
ACQUISITION FUNNEL — [Period]
===============================
Stage              Count     Rate      vs. Last    Trend
------------------------------------------------------------
Visitors           ______    100%      ______      [^ v -]
Signups            ______    ____%     ______      [^ v -]
Activated          ______    ____%     ______      [^ v -]
Engaged (Week 1)   ______    ____%     ______      [^ v -]
Retained (Month 1) ______    ____%     ______      [^ v -]
Paying             ______    ____%     ______      [^ v -]

Biggest drop-off: [Stage] to [Stage] at ____%
Hypothesis:
Action:
```

#### Retention Cohorts

Retention is the most important growth metric. Acquisition without retention is a leaky bucket. Track retention by monthly cohort to see whether the product is improving for new users over time.

**Cohort Retention Table:**

```
RETENTION COHORTS (% of users active)
=======================================
Cohort     Day 1   Day 7   Day 30   Day 90
-------------------------------------------
Jan 2026   85%     42%     28%      18%
Feb 2026   87%     45%     30%      --
Mar 2026   89%     48%     --       --
Apr 2026   90%     --      --       --

Trend: Day-7 retention improving month-over-month (+2-3 pp/month)
Target: Day-30 retention > 35% by Q3
```

**How to read cohort tables:** Read down a column to see if the product is improving for new users. If the January cohort has 42% Day-7 retention and the April cohort has 50%, the product is getting better. Read across a row to see how a specific cohort degrades over time -- this is the retention curve for that group.

#### Revenue Trends

| Metric | Current | vs. Last Month | vs. Last Quarter | Target |
|---|---|---|---|---|
| MRR (Monthly Recurring Revenue) | $______ | ______ | ______ | $______ |
| ARPU (Average Revenue Per User) | $______ | ______ | ______ | $______ |
| Churn rate (monthly) | ______% | ______ | ______ | < ____% |
| Net revenue retention | ______% | ______ | ______ | > 100% |
| Expansion revenue (upsell + cross-sell) | $______ | ______ | ______ | $______ |

**Net revenue retention (NRR)** is the single best metric for SaaS health. NRR above 100% means that revenue from existing customers is growing even before new customers are added. Below 100% means the bucket is leaking faster than it fills.

### Startup Mode: Monthly Lightweight Review

For early-stage teams, a full product review every month keeps the team honest without becoming burdensome. Focus on "Are we learning and growing?" rather than exhaustive analysis.

**Monthly Product Review Template (Startup):**

```
MONTHLY PRODUCT REVIEW — [Month Year]
=======================================
Product: _______________
Author: _______________
Date: _______________

1. NORTH STAR CHECK (5 min)
   Metric: [name]
   Current: ______    Target: ______    Status: [On/Off Track]
   Trend: [4-week summary]
   Why: [1-2 sentences explaining the trend]

2. TOP 3 WINS THIS MONTH
   1. [Win]: [Impact on metrics or users]
   2. [Win]: [Impact on metrics or users]
   3. [Win]: [Impact on metrics or users]

3. TOP 3 MISSES OR LEARNINGS
   1. [Miss/Learning]: [What happened + what we'll do differently]
   2. [Miss/Learning]: [What happened + what we'll do differently]
   3. [Miss/Learning]: [What happened + what we'll do differently]

4. USER PULSE
   Conversations this month: [#]
   Top insight: [1-2 sentences]
   NPS (if tracked): [score] ([trend])

5. GROWTH SNAPSHOT
   Signups:          ______ ([trend])
   Activation rate:  ______% ([trend])
   Day-30 retention: ______% ([trend])
   MRR:              $______ ([trend])

6. NEXT MONTH FOCUS
   - [Priority 1]: [Why this, what we expect to learn/achieve]
   - [Priority 2]: [Why this, what we expect to learn/achieve]

7. OPEN QUESTIONS / RISKS
   - [Question or risk]: [Mitigation or investigation plan]

Total time to complete: ~30 minutes
Delivery: Async (Notion doc, Google Doc, or Slack post)
```

### Enterprise Mode: Quarterly Business Review (QBR)

The QBR is the most comprehensive product review format. It is designed for a 90-minute meeting with executive stakeholders and should be board-ready in its quality and structure.

**QBR Agenda (90 min):**

```
QUARTERLY BUSINESS REVIEW — Q_ 20__
=====================================
Product: _______________
Presenter: _______________
Date: _______________
Attendees: _______________

0. EXECUTIVE SUMMARY (5 min)
   3 bullets that capture the quarter:
   - [Bullet 1: Biggest win]
   - [Bullet 2: Biggest challenge or learning]
   - [Bullet 3: Key decision or priority for next quarter]

1. STRATEGY UPDATE (15 min)
   Vision reaffirmation or update:
   [Is the vision still correct? Any market changes?]

   OKR scorecard:
   | Objective | Score | Commentary |
   |-----------|-------|------------|
   |           |       |            |

   Competitive landscape changes:
   [2-3 sentences on any material competitive moves]

2. PRODUCT METRICS DEEP DIVE (20 min)
   North Star:
   [Value, trend, vs. target, with 12-week chart]

   Funnel performance:
   [Conversion by stage, trend, biggest drop-off]

   Retention cohorts:
   [Cohort table, trend analysis, comparison vs. target]

   Revenue:
   | Metric   | Q Start | Q End  | Change  | Target |
   |----------|---------|--------|---------|--------|
   | MRR      |         |        |         |        |
   | ARPU     |         |        |         |        |
   | Churn    |         |        |         |        |
   | NRR      |         |        |         |        |
   | Expansion|         |        |         |        |

3. CUSTOMER INSIGHTS (15 min)
   User research conducted:
   [# conversations, # surveys, key methods]

   Top 3 customer insights:
   1. [Insight]: [Evidence] [Action taken or planned]
   2. [Insight]: [Evidence] [Action taken or planned]
   3. [Insight]: [Evidence] [Action taken or planned]

   NPS:
   [Score, trend, top promoter theme, top detractor theme]

   Customer success signals:
   [Churn reasons, expansion triggers, support volume trend]

4. COMPETITIVE UPDATE (10 min)
   | Competitor | Notable Move | Our Response |
   |------------|--------------|--------------|
   |            |              |              |

   Positioning map: [Updated if changed]
   Win/loss trend: [Win rate, trend, top win reasons, top loss reasons]

5. RISKS AND MITIGATIONS (10 min)
   | Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation | Owner |
   |------|---------------------|-----------------|------------|-------|
   |      |                     |                 |            |       |

6. NEXT QUARTER PRIORITIES (10 min)
   | Priority | Expected Impact | Key Metric | Target |
   |----------|-----------------|------------|--------|
   |          |                 |            |        |

   Resource requests:
   [Any headcount, tooling, or budget needs]

   Key dependencies:
   [Cross-team or external dependencies]

7. Q&A AND DECISIONS (5 min)
   [Capture questions, decisions, and follow-ups]

   | Decision | Rationale | Owner | Deadline |
   |----------|-----------|-------|----------|
   |          |           |       |          |
```

### Product Review Output Template

This is the unified output format that the orchestrator agent uses to synthesize inputs from strategy, discovery, execution, and growth into a single product health assessment.

```
PRODUCT HEALTH ASSESSMENT
==========================
Product: _______________
Period: _______________
Author: _______________
Date: _______________

OVERALL HEALTH: [Healthy / Needs Attention / At Risk]

DIMENSION SCORES:
  Strategy Alignment:   [1-5] — [1-sentence summary]
  Discovery Health:     [1-5] — [1-sentence summary]
  Execution Quality:    [1-5] — [1-sentence summary]
  Growth Metrics:       [1-5] — [1-sentence summary]
  Customer Satisfaction:[1-5] — [1-sentence summary]

SCORING GUIDE:
  5 = Excellent — exceeding targets, no concerns
  4 = Good — on track, minor issues being addressed
  3 = Adequate — meeting minimum bar, improvement needed
  2 = Concerning — below targets, action plan required
  1 = Critical — significantly off track, immediate intervention

TOP 3 STRENGTHS:
  1. [Strength]: [Evidence]
  2. [Strength]: [Evidence]
  3. [Strength]: [Evidence]

TOP 3 RISKS:
  1. [Risk]: [Impact if unaddressed] [Mitigation]
  2. [Risk]: [Impact if unaddressed] [Mitigation]
  3. [Risk]: [Impact if unaddressed] [Mitigation]

RECOMMENDED ACTIONS:
  | Action | Priority (P0-P3) | Owner | Timeline |
  |--------|------------------|-------|----------|
  |        |                  |       |          |

KEY METRICS SNAPSHOT:
  North Star:        [value] ([trend])
  Activation:        [value] ([trend])
  Retention (Day-30):[value] ([trend])
  NPS:               [value] ([trend])
  MRR:               [value] ([trend])
  Churn:             [value] ([trend])

NEXT REVIEW DATE: _______________
```

---

## Output Formats

### Metrics Framework Template

```
METRICS FRAMEWORK
==================
Product: _______________
Date: _______________
Owner: _______________

NORTH STAR METRIC:
  Name:       _______________
  Definition: [Exact calculation]
  Current:    ______
  Target:     ______
  Cadence:    [Daily / Weekly / Monthly]

INPUT METRICS:
  | # | Metric | Definition | Current | Target | Owner | How It Drives North Star |
  |---|--------|------------|---------|--------|-------|--------------------------|
  | 1 |        |            |         |        |       |                          |
  | 2 |        |            |         |        |       |                          |
  | 3 |        |            |         |        |       |                          |
  | 4 |        |            |         |        |       |                          |
  | 5 |        |            |         |        |       |                          |

NORTH STAR FORMULA:
  [North Star] = [Input 1] x [Input 2] + [Input 3] x [Input 4] + ...
  (Express the mathematical relationship if possible)

COUNTER-METRICS (GUARDRAILS):
  | Primary Metric | Counter-Metric | Threshold (don't exceed) |
  |----------------|----------------|--------------------------|
  |                |                |                          |

METRIC QUALITY CHECK:
  [ ] All metrics are measurable with current instrumentation
  [ ] All metrics are actionable by the owning team
  [ ] All metrics are understandable (team can explain them)
  [ ] All metrics are comparable over time (normalized)
  [ ] No vanity metrics included
```

### Single-Page Scorecard Template

```
PRODUCT SCORECARD — Week of _______________
=============================================
Product: _______________

NORTH STAR: [Metric Name]
  Current: ______    Target: ______    Status: [On/At Risk/Off Track]
  4-Week: [W-3] --> [W-2] --> [W-1] --> [Now]

INPUT METRICS:
  | Metric          | Current | Previous | Trend | Status |
  |-----------------|---------|----------|-------|--------|
  |                 |         |          |       |        |
  |                 |         |          |       |        |
  |                 |         |          |       |        |

FUNNEL:
  Visitors --> Signups --> Activated --> Retained
  [#] (100%)  [#] (__%)   [#] (__%)    [#] (__%)

RETENTION:
  Wk 1: ____%  |  Wk 2: ____%  |  Wk 4: ____%  |  Wk 8: ____%

CONTEXT: _______________________________________________
```

### Executive Dashboard Spec

```
EXECUTIVE DASHBOARD SPECIFICATION
===================================
Product: _______________
Audience: C-suite, board, investors
Refresh: Monthly on the [1st/last] business day

METRICS:
  | Metric | Definition | Source | Visualization | Alert |
  |--------|------------|--------|---------------|-------|
  | North Star | [exact calc] | [table/API] | Line (12-wk) | >15% drop WoW |
  | MRR | [exact calc] | [billing system] | Line (12-mo) | Miss plan >10% |
  | Growth Rate | [MoM %] | [derived] | Bar (6-mo) | <X% for 2 months |
  | Customer Count | [active paying] | [CRM] | Line (12-mo) | Net negative |
  | NPS | [survey score] | [survey tool] | Line (quarterly) | Drop >10 pts |

EXECUTIVE SUMMARY FORMAT:
  - 3 bullets: top win, top challenge, key decision
  - 1 paragraph of context
  - Top 3 risks with mitigation status

DISTRIBUTION:
  Delivered via: [email / Slack / dashboard link]
  Review meeting: [Monthly, 30 min, first Monday]
```

### Sprint Review Template (Startup)

```
WEEKLY UPDATE — Week of _______________
========================================
Team: _______________

SHIPPED:
  - [Item]: [Description] [link]
  - [Item]: [Description] [link]

DID NOT SHIP:
  - [Item]: [Reason] [New ETA or dropped]

METRIC CHECK:
  North Star ([name]): [value] ([trend])
  [Input metric 1]:    [value] ([trend])
  [Input metric 2]:    [value] ([trend])

USER SIGNAL:
  [Top theme from support/feedback this week]

NEXT WEEK:
  - [Item 1]
  - [Item 2]

BLOCKER: [Description or "None"]
```

### Sprint Review Template (Enterprise)

```
SPRINT REVIEW — Sprint [#] ([dates])
======================================
Product: _______________
PM: _______________

1. DEMO (20 min)
   [Feature demos with context]

2. METRICS READOUT (15 min)
   North Star: [value] vs. [target]

   Moved:
   | Metric | Before | After | Cause |
   |--------|--------|-------|-------|
   |        |        |       |       |

   Didn't move:
   | Metric | Expected | Actual | Hypothesis |
   |--------|----------|--------|------------|
   |        |          |        |            |

   Unexpected:
   | Metric | Change | Status |
   |--------|--------|--------|
   |        |        |        |

3. USER FEEDBACK (10 min)
   Tickets: [#] ([trend])
   Top themes:
     1. [Theme]: [action]
     2. [Theme]: [action]
     3. [Theme]: [action]

4. Q&A (10 min)
   [Notes]

5. ACTIONS (5 min)
   | Action | Owner | Due |
   |--------|-------|-----|
   |        |       |     |
```

### Monthly Product Review Template

```
MONTHLY PRODUCT REVIEW — [Month Year]
=======================================
Product: _______________

1. NORTH STAR CHECK
   [Metric]: [value] vs. [target] — [trend + why]

2. WINS (Top 3)
   1. [Win]: [metric impact]
   2. [Win]: [metric impact]
   3. [Win]: [metric impact]

3. MISSES / LEARNINGS (Top 3)
   1. [Item]: [what happened + what changes]
   2. [Item]: [what happened + what changes]
   3. [Item]: [what happened + what changes]

4. USER PULSE
   Conversations: [#] | Top insight: [summary]
   NPS: [score] ([trend])

5. GROWTH SNAPSHOT
   Signups: ______ | Activation: ______%
   Day-30 Retention: ______% | MRR: $______

6. NEXT MONTH FOCUS
   - [Priority 1]: [expected outcome]
   - [Priority 2]: [expected outcome]

7. RISKS
   - [Risk]: [mitigation]
```

### QBR Template

```
QUARTERLY BUSINESS REVIEW — Q_ 20__
=====================================
Product: _______________
Presenter: _______________

EXECUTIVE SUMMARY:
  - [Biggest win]
  - [Biggest challenge]
  - [Key priority for next quarter]

1. STRATEGY
   Vision: [Reaffirm or update]
   OKRs:
   | Objective | Score | Notes |
   |-----------|-------|-------|
   |           |       |       |
   Competitive: [Key changes]

2. METRICS
   North Star: [value, trend, chart]
   Funnel: [conversion by stage]
   Retention: [cohort table]
   Revenue:
   | Metric | Q Start | Q End | Change | Target |
   |--------|---------|-------|--------|--------|
   |        |         |       |        |        |

3. CUSTOMERS
   Research: [# conversations, methods]
   Top insights: [3 bullets]
   NPS: [score, trend]

4. COMPETITIVE
   | Competitor | Move | Our Response |
   |------------|------|--------------|
   |            |      |              |
   Win/loss: [rate, trend, reasons]

5. RISKS
   | Risk | Likelihood | Impact | Mitigation | Owner |
   |------|------------|--------|------------|-------|
   |      |            |        |            |       |

6. NEXT QUARTER
   | Priority | Impact | Metric | Target |
   |----------|--------|--------|--------|
   |          |        |        |        |
   Resources: [needs]
   Dependencies: [list]

7. DECISIONS
   | Decision | Owner | Deadline |
   |----------|-------|----------|
   |          |       |          |
```
