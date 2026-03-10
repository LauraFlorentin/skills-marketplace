---
name: product-analytics
description: Metrics frameworks, dashboard design, sprint reviews, and comprehensive product reviews for startup and enterprise PMs — North Star metrics, input metrics, funnel analysis, retention cohorts, and cross-cutting product health assessments. Use when user asks to "define product metrics", "build a dashboard", "product review", or mentions north star metric, funnel analysis, retention cohorts, or QBR.
triggers:
  - metrics
  - north star metric
  - KPI
  - dashboard
  - analytics
  - product analytics
  - sprint review
  - iteration review
  - product review
  - QBR
  - quarterly business review
  - funnel
  - retention
  - cohort analysis
  - NPS
  - product health
---

# Product Analytics

## Disclaimer

Metrics inform decisions but don't make them. Always pair quantitative data with qualitative understanding of user behavior and context.

## Metrics Frameworks

A metrics framework is the foundation of product analytics. Without a clear framework, teams drown in data -- tracking hundreds of events and charts that nobody acts on. The goal of a framework is to connect a small number of meaningful metrics to the product strategy so that every team member knows what success looks like and which levers to pull.

### North Star Metric

The North Star Metric is the single metric that best captures the core value your product delivers to customers. It is the one number that, if it grows sustainably, means the product is succeeding. Everything else -- revenue, retention, engagement -- should correlate with the North Star over time.

**Properties of a good North Star Metric:**

1. **Measures value delivered, not vanity.** It reflects something the customer cares about, not something that merely makes the company look good. Page views are vanity. Tasks completed is value.
2. **Is a leading indicator.** It predicts future business success rather than reflecting past performance. Weekly active users predicts future revenue better than last month's revenue predicts next month's revenue.
3. **Is actionable.** The product team can directly influence it through their work. Total addressable market is important but not actionable by a product team. Activation rate is.

**North Star Metric Examples by Product Type:**

| Product Type | North Star Metric | Why It Works |
|---|---|---|
| **Marketplace** | GMV (Gross Merchandise Volume) or Transactions Completed | Captures both sides of the marketplace -- buyers finding value and sellers making sales. Growth means the marketplace is working. |
| **SaaS** | Weekly Active Users or Features Used per Week | Measures habitual engagement with core product value. A user who returns weekly and uses multiple features is getting real value. |
| **Media / Content** | Total Time Spent or Articles Read | Reflects that content is engaging and relevant enough to keep users coming back and consuming more. |
| **E-commerce** | Purchases per Active Customer | Measures repeat buying behavior, which indicates the product is delivering enough value to earn repeat business. |
| **Social** | Daily Active Users with a Social Interaction | Ensures the metric captures the social value (not just lurking). A user who interacts socially is both getting and creating value for others. |

**How to Find Your North Star Metric:**

Ask two questions:

1. **What action means a customer got value?** Think about the moment a user says "this was worth it." For a project management tool, it might be "completing a task." For a marketplace, it might be "making a purchase." For a communication tool, it might be "sending a message that gets a reply."
2. **How often should that action happen?** If the core value should be delivered daily, measure daily. If weekly is the natural cadence, measure weekly. A fitness app might measure weekly workouts completed. A tax tool might measure annual returns filed.

The intersection of the value-delivering action and the natural frequency is your North Star candidate. Test it by asking: "If this metric doubles, would we be confident the product is succeeding?" If yes, you have a strong candidate.

### Input Metrics

Input metrics are the 3-5 levers that drive the North Star. They are the actionable, team-level metrics that break the North Star into components the team can directly influence.

**The relationship:**

```
Input Metrics  -->  North Star Metric  -->  Business Outcomes
(team controls)     (product health)        (revenue, growth, valuation)
```

**Worked Example:**

If your North Star Metric is **Weekly Active Users (WAU)**, your input metrics might be:

| Input Metric | How It Drives WAU | Who Owns It |
|---|---|---|
| New user signups | More users entering the top of the funnel | Growth / Marketing |
| Activation rate | Higher % of signups become active users | Product / Onboarding |
| Day-7 retention | More new users return after the first week | Product / Core experience |
| Reactivated users | Dormant users come back | Lifecycle / Marketing |

**The math should connect.** In the best case, you can express the North Star as a formula of its inputs:

```
WAU = New signups x Activation rate
    + Existing users x Retention rate
    + Dormant users x Reactivation rate
```

This makes it immediately clear where growth comes from and which lever offers the most opportunity. If activation rate is 20% and retention is 80%, improving activation will have a larger impact per percentage point.

### Startup Mode: Keep It Simple

For early-stage products, resist the urge to instrument everything. Over-instrumentation wastes engineering time and creates dashboards nobody reads.

**The startup metrics stack:**

- **North Star Metric** -- the one number everyone knows.
- **3-5 Key Input Metrics** -- the levers the team is actively pulling this quarter.
- **Single Dashboard** -- one page, updated weekly, visible to the whole team.
- **Weekly Review** -- 15 minutes in the team standup to check the numbers and discuss.

Do not over-instrument. Focus on the critical path first: Can users find your product? Can they sign up? Do they experience the core value? Do they come back? Can you charge them? Track those steps and nothing else until you have product-market fit. You can always add instrumentation later. You cannot easily remove the organizational complexity of 50 dashboards nobody trusts.

### Enterprise Mode: Metrics Hierarchy

For mature products with multiple teams, metrics must cascade across organizational levels, just like OKRs. Each level has a distinct purpose and audience.

**Metrics Hierarchy:**

```
Company-level North Star
    |
    +-- Department-level Input Metrics
    |       |
    |       +-- Team-level Feature Metrics
    |               |
    |               +-- Feature-level Instrumentation
```

- **Company-level:** The North Star plus 2-3 business outcomes (revenue, customer count, NPS). Reviewed by executives monthly.
- **Department-level:** The input metrics that drive the North Star. Each department owns 2-4 input metrics. Reviewed by department leads weekly.
- **Team-level:** Feature-specific metrics that drive the department input metrics. Each team owns 1-3 feature metrics. Reviewed by the team daily or weekly.
- **Feature-level:** Granular instrumentation (click-through rates, error rates, latency) used for debugging and optimization. Reviewed by engineers as needed.

**Leading vs. Lagging Indicators:**

| Type | Definition | Examples | Use For |
|---|---|---|---|
| **Leading indicators** | Predict future performance. They move before business outcomes change. | Signups, activation rate, feature adoption, NPS of new cohorts, time-to-value | Early warnings, course corrections, sprint planning |
| **Lagging indicators** | Reflect past performance. They confirm whether previous actions worked. | Revenue, churn rate, LTV, market share, annual contract value | Board reporting, strategy validation, long-term trends |

A healthy metrics framework includes both. Leading indicators tell you where you are headed. Lagging indicators tell you where you have been. If you only track lagging indicators, you are always looking in the rearview mirror.

**Counter-Metrics and Guardrails:**

When optimizing a primary metric, you must define guardrail metrics that must not degrade. Optimizing without guardrails leads to pathological behavior.

| Primary Metric Being Optimized | Counter-Metric (Guardrail) | Why |
|---|---|---|
| Activation rate | Support ticket rate | Don't increase activation by spamming users with aggressive prompts that confuse them |
| Feature adoption | Task completion rate | Don't inflate adoption numbers by auto-enabling features users don't want |
| Email open rate | Unsubscribe rate | Don't optimize open rates with clickbait subjects that erode trust |
| Revenue per user | Churn rate | Don't increase ARPU by raising prices in a way that drives users away |
| Sprint velocity | Defect escape rate | Don't inflate velocity by cutting corners on quality |

**Rule of thumb:** For every primary metric you are optimizing, define at least one counter-metric. Include the counter-metric on the same dashboard. If the counter-metric degrades by more than a defined threshold (e.g., 10% regression), pause the optimization and investigate.

### Metric Quality Checklist

Before adding any metric to a dashboard or OKR, validate it against these criteria:

- [ ] **Measurable:** Can you actually track it with your current instrumentation? If not, what is the engineering cost to instrument it? Aspirational metrics that cannot be measured are useless.
- [ ] **Actionable:** Can the team influence it through their work? If the metric moves, can the team explain why and take corrective action? Metrics outside the team's control create frustration, not accountability.
- [ ] **Understandable:** Can every team member explain what the metric means and how it is calculated? If the definition requires a 10-minute explanation, simplify it or choose a different metric.
- [ ] **Comparable:** Is it consistent over time? Does it account for seasonality, user base growth, and definition changes? Comparing raw counts across months with different user bases is misleading -- use per-user or percentage-based metrics instead.
- [ ] **Not a vanity metric:** Does it correlate with business value? Page views, total registered users, and app downloads are vanity metrics -- they go up and to the right even if the business is failing. Active users, retention rates, and revenue per user are real metrics.

---

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/product-analytics-reference.md`](references/product-analytics-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- Dashboard Design
- Sprint Review
- Product Review
- Output Formats

