# Monitoring — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

## Contents

- [Risk Review](#risk-review)
- [Dependency Tracking](#dependency-tracking)
- [Health Check](#health-check)
- [Output Formats](#output-formats)
- [Burndown and Forecasting](#burndown-and-forecasting)

---

## Risk Review

Risk management is not a one-time planning exercise. Risks evolve throughout the project lifecycle -- new risks emerge, existing risks change in probability or impact, and some risks resolve themselves. The risk review is the mechanism for keeping the risk register alive and actionable.

### Risk Review Meeting Agenda (30 Minutes)

This is a standing meeting, held weekly for active projects or biweekly for stable projects. The PM facilitates. Attendees include the core team, risk owners, and optionally the sponsor for high-risk projects.

```
RISK REVIEW MEETING AGENDA
=============================
Project: _______________
Date: _______________  |  Facilitator: _______________
Duration: 30 minutes

1. REVIEW TOP RISKS (10 min)
   Walk through the top 5 risks by current risk score (probability x impact).
   For each risk:
   - Has the probability changed? Up, down, or same?
   - Has the impact changed?
   - Is the mitigation action on track?
   - Is the owner still the right person?
   - Has the risk triggered? (If yes, move to Issue log.)

2. RE-SCORE (5 min)
   Update probability and impact scores for any risks that have changed.
   Re-rank the risk register by updated scores.

3. NEW RISKS (5 min)
   Go around the table: "Has anyone identified a new risk since last review?"
   For each new risk:
   - Description (what could go wrong)
   - Probability (H/M/L)
   - Impact (H/M/L)
   - Owner (who will monitor and mitigate)
   - Initial mitigation action

4. TRIGGERS CHECK (5 min)
   Review risk triggers -- the predefined conditions that indicate a risk
   is about to materialize or has materialized.
   For each trigger:
   - Has the trigger condition been met?
   - If yes, activate the contingency plan and move risk to Issue log.
   - If approaching, increase monitoring frequency.

5. ACTION ITEMS (5 min)
   Summarize all actions from this review:
   - New mitigation actions assigned
   - Escalations needed
   - Risks to close
   - Follow-up investigations
   Next review date: _______________
```

### Risk Register Update Process

The risk register is a living document. Update it at every risk review meeting following this process:

1. **Re-score existing risks.** For each open risk, reassess probability and impact based on current project state. A risk scored High probability at project start may now be Low if the uncertain event has been avoided.

2. **Identify new risks.** Every team member should be actively scanning for new risks. Common sources: changed requirements, team changes, technology surprises, vendor issues, market shifts, regulatory changes.

3. **Close resolved risks.** If a risk can no longer occur (the uncertain event has passed), close it with a resolution note. Example: "Risk: Key vendor may not deliver API by March 1. Resolution: Vendor delivered API on Feb 25. Closed."

4. **Check triggers.** Risk triggers are early warning indicators that a risk is about to materialize. Example: If the risk is "contractor may leave before project end," the trigger might be "contractor has not renewed contract and renewal date is within 30 days."

**Risk Register Template:**

```
RISK REGISTER
===============
Project: _______________  |  Last Updated: _______________

| ID | Description | Category | Probability | Impact | Score | Owner | Mitigation | Trigger | Status | Date Identified | Last Reviewed |
|----|-------------|----------|-------------|--------|-------|-------|------------|---------|--------|-----------------|---------------|
| R-001 | [What could go wrong] | [Schedule/Scope/Cost/Quality/Technical/External] | [H/M/L] | [H/M/L] | [P x I] | [Name] | [Action + deadline] | [Trigger condition] | [Open/Mitigating/Closed] | [Date] | [Date] |
| R-002 | | | | | | | | | | | |
| R-003 | | | | | | | | | | | |

SCORING KEY:
  Probability: High (>70%) = 3, Medium (30-70%) = 2, Low (<30%) = 1
  Impact: High (project objectives at risk) = 3, Medium (significant but manageable) = 2, Low (minor inconvenience) = 1
  Score: Probability x Impact (max 9)
  Priority: 7-9 = Critical (review weekly), 4-6 = Significant (review biweekly), 1-3 = Low (review monthly)
```

### Risk Trend Tracking

Tracking whether risks are increasing or decreasing over time is as important as tracking individual risks. A project where the total number and severity of risks is trending down is converging toward success. A project where risks are growing is diverging.

**Risk burn-down:** Plot the total risk score (sum of all open risk scores) over time. This should generally decrease as the project progresses and uncertainties are resolved. If total risk score is flat or increasing, the project is not de-risking -- something is wrong.

```
Total Risk
Score
  |
45|*
  |  *
40|    *
  |      *
35|        *
  |          *
30|            *  *         <-- Risk not decreasing: investigate
  |                 *
25|                   *
  |                     *
20|                       *
  |                         *
15|                           *
  |                             *
10|                               *
  |                                 *
 5|                                   *
  |                                     *
 0|_______________________________________> Sprints/Weeks
```

**Supplementary risk metrics:**
- Number of open risks (should decrease over project life)
- Number of new risks identified per period (should decrease after initial phases)
- Average age of open risks (if increasing, risks are not being resolved)
- Number of risks that materialized into issues (indicates whether risk identification was effective)

### Software Mode: Technical Risks

Software projects carry specific technical risks that must be tracked alongside standard project risks.

**Technical Debt as Risk:**

Technical debt is deferred work that increases future cost or risk. Track it as a risk when it crosses a threshold: "If we do not address X, it will cause Y within Z timeframe." Examples:
- "Authentication module has 2 known security vulnerabilities. If not patched by Q2, we risk a production exploit."
- "Test coverage on the payment module is 30%. If we add the subscription feature without increasing coverage, regression risk is High."

Track technical debt risk in the risk register with Category = "Technical" and include specific trigger conditions.

**Security Vulnerability Tracking:**

Maintain a vulnerability register alongside the risk register. For each known vulnerability:
- Severity (Critical/High/Medium/Low using CVSS or equivalent)
- Affected component
- Exploit likelihood
- Patch available (yes/no)
- Patch deployment date
- Owner

Vulnerabilities rated Critical or High with no patch deployed should appear in the project risk register as Red risks.

**Dependency Update Risk:**

Third-party libraries and frameworks with pending major version updates represent risk. Track:
- Dependencies with end-of-life dates approaching
- Dependencies with known vulnerabilities in current version
- Dependencies requiring breaking-change upgrades

**Performance Regression Risk:**

Track performance baselines (response time, throughput, error rate) and flag when current measurements deviate >10% from baseline. Performance regression often compounds silently until it becomes a user-visible incident.

### General Mode: Risk Categories

For non-software projects, organize risks into standard categories to ensure complete coverage:

| Category | Examples | Typical Sources |
|----------|----------|-----------------|
| **Scope** | Requirements creep, unclear deliverables, stakeholder changing direction | Weak change control, vague SOW, multiple stakeholders with conflicting goals |
| **Schedule** | Milestone delays, dependency slippage, approval bottlenecks | Optimistic planning, external dependencies, decision-maker availability |
| **Cost** | Budget overrun, unplanned expenses, vendor price changes | Poor estimation, scope creep without budget adjustment, inflation |
| **Quality** | Deliverable rework, failed acceptance criteria, compliance gaps | Unclear standards, insufficient review cycles, skills mismatch |
| **External** | Regulatory changes, market shifts, natural events, vendor bankruptcy | Factors outside project control; mitigate with contingency planning |

**Risk Owner Accountability:**

Every risk must have a single named owner (not a team, not a role -- a person). The owner is responsible for:
- Monitoring the risk at each review cycle
- Executing or coordinating the mitigation action
- Reporting status changes to the PM
- Activating the contingency plan if the risk triggers

**Risk Appetite Definition:**

At project kickoff, align with the sponsor on risk appetite:
- "How much schedule delay is acceptable before we escalate?" (e.g., 1 week)
- "How much budget overrun triggers a formal review?" (e.g., 5%)
- "Are there any risks we will not accept under any circumstances?" (e.g., data breach, regulatory non-compliance)

Document risk appetite in the project charter. Reference it when deciding whether to mitigate, accept, or escalate.

### Escalation Criteria: Risk to Issue

A risk becomes an issue when the uncertain event has occurred or is certain to occur. The distinction matters: risks are potential problems with mitigations; issues are actual problems requiring immediate resolution.

**When to escalate a risk to an issue:**

- The risk trigger condition has been met
- Probability has increased to near-certainty (>90%)
- The mitigation has failed and the risk is materializing
- The impact has increased beyond the project's risk appetite threshold

**Issue Log Template:**

```
ISSUE LOG
===========
Project: _______________  |  Last Updated: _______________

| ID | Description | Source Risk | Severity | Impact | Owner | Resolution Plan | Target Date | Status | Actual Resolution |
|----|-------------|-----------|----------|--------|-------|----------------|-------------|--------|-------------------|
| I-001 | [What went wrong] | [R-XXX or new] | [Critical/High/Medium/Low] | [Quantified impact] | [Name] | [Step-by-step resolution] | [Date] | [Open/In Progress/Resolved] | [What was actually done] |
| I-002 | | | | | | | | | |
```

### Risk Review Anti-Patterns

**Stale Register:**

The risk register was created at project kickoff and has not been updated since. It contains risks that no longer apply and is missing risks that have emerged. No one references it because it does not reflect reality. Fix: Make the risk register a standing agenda item in weekly status meetings. Set a policy: any risk not reviewed in 2 weeks is flagged for review. The PM is accountable for register freshness.

**Risk Theater:**

The team goes through the motions of risk management -- they have a register, they hold reviews, they score risks -- but no one actually takes action on the mitigations. Risks are identified and scored but never addressed. The risk review becomes a ritual that creates the illusion of control without reducing actual risk. Fix: Every risk must have a mitigation action with a deadline and an owner. Track mitigation completion rate as a project metric. If mitigations are consistently overdue, escalate the risk management process itself.

**Ignoring Low-Probability High-Impact Risks:**

The team focuses all attention on high-probability risks and ignores risks that are unlikely but catastrophic if they occur (single point of failure, key person dependency, vendor bankruptcy, data loss). These "black swan adjacent" risks destroy projects when they materialize precisely because no contingency was planned. Fix: Maintain a separate section in the register for low-probability/high-impact risks. Define contingency plans (not mitigations) for each. Review them monthly, not weekly. Accept that you cannot prevent them, but ensure you can respond.

---

## Dependency Tracking

Dependencies are the connective tissue of complex projects. A dependency exists when one work item, team, or deliverable cannot proceed without an input from another. Untracked dependencies are the number one cause of project delays that "nobody saw coming" -- they were visible, just not tracked.

### Dependency Map Template

```
DEPENDENCY MAP
================
Project: _______________  |  Last Updated: _______________

| ID | Source (waiting team/item) | Target (providing team/item) | Type | Status | Owner | Due Date | Impact if Late |
|----|--------------------------|---------------------------|------|--------|-------|----------|---------------|
| D-001 | [Team/deliverable that is waiting] | [Team/deliverable that must provide] | [Blocking/Enabling/Shared Resource] | [On Track/At Risk/Blocked] | [Name] | [Date] | [What breaks if this is late] |
| D-002 | | | | | | | |
| D-003 | | | | | | | |

DEPENDENCY TYPES:
  Blocking:        Source cannot start until Target completes. Hard dependency.
  Enabling:        Source can start but cannot finish until Target delivers. Soft dependency.
  Shared Resource: Both Source and Target need the same resource (person, environment, tool).
                   Scheduling conflict, not a sequencing dependency.

STATUS DEFINITIONS:
  On Track:  Target is on schedule to deliver by due date. No action needed.
  At Risk:   Target may not deliver on time. Mitigation in progress.
  Blocked:   Target will not deliver on time. Escalation required.
```

### Software Mode: Cross-Team Dependencies

Software projects generate dependency types that are specific to the engineering domain.

**Cross-Team API Dependencies:**

Team A needs Team B to provide an API endpoint before Team A can build the feature that consumes it. Track: API specification agreement date, implementation date, testing date, production readiness date. The specification agreement is the critical early milestone -- if teams do not agree on the contract early, integration will fail late.

**Shared Library Dependencies:**

Multiple teams depend on a shared library (authentication SDK, design system components, logging framework). Track: version pinning, upgrade schedules, breaking change notifications. A breaking change in a shared library can block multiple teams simultaneously.

**Infrastructure Dependencies:**

Teams depend on shared infrastructure: databases, message queues, Kubernetes clusters, CI/CD pipelines, staging environments. Track: provisioning timelines, capacity limits, maintenance windows, and shared environment availability.

**CI/CD Pipeline Dependencies:**

Deployment depends on pipeline health. Track: pipeline reliability (% of builds that pass without infrastructure failure), average pipeline duration, queue depth (how long before a build starts). A slow or unreliable pipeline is a hidden dependency that affects every team.

**Feature Flag Dependencies:**

Feature A is behind a feature flag that must be enabled before Feature B (which depends on A) can be tested in production. Track: flag state, rollout percentage, and the team responsible for flag management.

### General Mode: Cross-Project Dependencies

**Cross-Project Dependencies:**

Project A depends on a deliverable from Project B, which has its own timeline and priorities. Track: the specific deliverable, the providing project's PM, the agreed delivery date, and escalation path if the providing project's priorities shift.

**Vendor Dependencies:**

External vendors (software providers, contractors, suppliers) introduce dependencies outside your control. Track: contractual delivery dates, vendor health indicators (responsiveness, quality of prior deliverables), and backup plans if the vendor fails.

**Regulatory Dependencies:**

Projects in regulated industries depend on approvals, certifications, or compliance clearances. Track: submission dates, expected review durations, approval status, and the impact of delays on downstream work.

**Resource Sharing Dependencies:**

Multiple projects share the same people. When Project A's timeline shifts, it consumes resources that Project B was counting on. Track: shared resources by name, allocation percentages, and the priority rules when conflicts arise.

**Procurement Dependencies:**

Hardware purchases, software licenses, facility leases -- anything that requires a procurement process introduces a dependency with lead times that project teams often underestimate. Track: requisition date, approval date, expected delivery date, and buffer for delays.

### Dependency Review Cadence

- **Active dependencies** (status = At Risk or Blocked, or due date within 2 weeks): Review weekly in the project status meeting. Owner provides update. Escalation happens in real-time.
- **Stable dependencies** (status = On Track, due date > 2 weeks away): Review biweekly or monthly. Quick confirmation that nothing has changed.
- **New dependencies:** Identified at any time by any team member. Added to the dependency map immediately with an owner and due date.

### Blocked Dependency Escalation Process

When a dependency is blocked, follow this escalation ladder. Each step has a time limit. Do not let blocked dependencies sit without escalation.

**Step 1: Owner resolves (Target: 48 hours)**

The dependency owner contacts the providing team directly to understand the blocker, negotiate a resolution, and agree on a new date. Most dependencies are resolved at this level through direct communication.

**Step 2: PM escalates to dependency owner's manager (Target: 1 week from block)**

If the providing team cannot resolve within 48 hours, the PM escalates to the providing team's manager or PM. Frame it as a prioritization request: "Our project is blocked waiting for X. Can you help us prioritize this on your team's backlog?"

**Step 3: Steering committee (Target: 2 weeks from block)**

If the providing team's management cannot or will not prioritize the dependency, escalate to the steering committee or program-level governance. Provide: the business impact of the delay, the specific ask, and the cost of waiting vs. the cost of a workaround.

**Escalation Template:**

```
DEPENDENCY ESCALATION
=======================
Date: _______________
Escalated by: _______________
Escalation level: [1: Owner / 2: Manager / 3: Steering Committee]

BLOCKED DEPENDENCY:
  ID: [D-XXX]
  Our team/project: [name]
  Waiting for: [description of what we need]
  From: [providing team/project/vendor]
  Original due date: [date]
  Days blocked: [number]

BUSINESS IMPACT:
  [What work is stopped because of this dependency?]
  [What is the downstream impact on milestones/deliverables?]
  [What is the cost of each additional day of delay?]

ASK:
  [What specifically do we need the escalation recipient to do?]

OPTIONS:
  Option A: [Providing team prioritizes delivery by new date]
  Option B: [We implement a workaround -- describe workaround and its cost]
  Option C: [We descope the dependent work -- describe impact]

RECOMMENDATION: [Option X, with rationale]
```

### Dependency Visualization Approaches

Dependencies are hard to manage when they only exist in a spreadsheet. Visual representations help teams see the web of relationships and identify critical paths and bottlenecks.

**Approaches:**

- **Directed graph / network diagram:** Nodes represent work items or teams. Arrows represent dependencies (direction = flow of dependency). Tools: draw.io, Miro, Lucidchart. Good for: seeing the overall structure and identifying clusters of dependencies.

- **Gantt chart with dependency lines:** Traditional project schedule with lines connecting dependent tasks. Tools: MS Project, Smartsheet, Monday. Good for: showing how dependencies affect the timeline and where float exists.

- **Dependency matrix:** A grid where rows and columns are teams or work items. Each cell indicates whether a dependency exists between the row and column, and its type/status. Tools: spreadsheet. Good for: large projects with many teams where a graph would be too complex.

- **Kanban board with blocked indicators:** A visual board where items move through columns (To Do, In Progress, Done). Blocked items get a visual indicator (red flag, blocked label) with the dependency noted. Tools: Jira, Trello, Linear. Good for: day-to-day visibility of which items are stuck and why.

---

## Health Check

A health check is a periodic, holistic assessment of project vitality. Unlike status reports, which focus on progress and metrics, a health check evaluates the qualitative and systemic factors that determine whether a project will succeed. A project can be "on schedule" and still be unhealthy if the team is burned out, stakeholders are misaligned, or technical debt is accumulating unsustainably.

### Multi-Dimensional Project Health Assessment

Assess project health across six core dimensions. Each dimension captures a different aspect of project vitality that can independently cause project failure.

**Dimension 1: Schedule Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Ahead | Project is ahead of schedule. Buffer exists. No critical path pressure. |
| 4 | On Track | Project is on schedule. All milestones on plan. Manageable float on critical path. |
| 3 | At Risk | 1-2 milestones slipping. Critical path float exhausted. Recovery plan in progress. |
| 2 | Behind | Multiple milestones missed. End date at risk. Recovery plan struggling. |
| 1 | Failing | End date has slipped or will slip. No credible recovery plan. Re-baseline required. |

**Dimension 2: Scope Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Locked | Scope fully defined, baselined, and stable. Change control enforced. |
| 4 | Stable | Scope defined with minor adjustments processed through change control. No drift. |
| 3 | Creeping | Scope growing without formal approval. 1-3 uncontrolled additions. Boundary softening. |
| 2 | Unclear | Significant scope ambiguity. Team unsure what is in vs. out. Rework occurring. |
| 1 | Uncontrolled | Scope is being defined in real-time. No baseline. Team building the wrong things. |

**Dimension 3: Budget Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Under Budget | Spend <95% of plan. Forecast under budget. Contingency intact. |
| 4 | On Budget | Spend within 5% of plan. Forecast on budget. Contingency available. |
| 3 | At Risk | Spend 5-10% over plan. Contingency being consumed. Cost controls tightened. |
| 2 | Over Budget | Spend >10% over plan. Contingency exhausted. Additional funding needed. |
| 1 | Failing | Budget exceeded with no additional funding. Cost cuts impacting scope or quality. |

**Dimension 4: Team Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Thriving | Team engaged and energized. Collaboration strong. Low attrition. Growth happening. |
| 4 | Engaged | Team performing well. Normal stress levels. Good communication. Stable composition. |
| 3 | Stressed | Sustained overtime (>2 weeks). Some frustration visible. Communication gaps emerging. |
| 2 | Strained | Overtime is the norm. Attrition risk. Quality dropping. Team conflict visible. |
| 1 | Burned Out | Key departures. Remaining team disengaged. Quality failing. Morale critically low. |

**Dimension 5: Risk Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Clear | Few open risks, all Low impact. Risk trend decreasing. Mitigations effective. |
| 4 | Manageable | Moderate open risks with active mitigations. Risk trend flat or decreasing. |
| 3 | Elevated | Multiple High risks. Mitigations in progress but not yet proven. Risk trend flat. |
| 2 | Concerning | High risks with ineffective mitigations. Issues materializing. Risk trend increasing. |
| 1 | Critical | Unmitigated High risks threatening project viability. Multiple issues unresolved. |

**Dimension 6: Stakeholder Health**

| Score | Label | Definition |
|-------|-------|------------|
| 5 | Champion | Stakeholders actively advocating for the project. Full alignment on goals and approach. |
| 4 | Aligned | Stakeholders supportive. Regular engagement. Minor differences managed constructively. |
| 3 | Mixed | Some stakeholders supportive, others disengaged or skeptical. Alignment requires effort. |
| 2 | Fragmented | Stakeholders pulling in different directions. Conflicting priorities. Decision-making stalled. |
| 1 | Misaligned | Key stakeholders actively opposing or undermining. No consensus on objectives. Sponsor at risk. |

### Health Check Scoring

**Scoring Rules:**

- Score each dimension 1-5 using the definitions above.
- Scores are assigned by the PM based on evidence, not optimism. Cite specific data points for each score.
- Discuss scores with the core team to calibrate. If the PM and tech lead disagree on Team Health, that disagreement is itself a data point.

**Threshold Interpretation:**

| Score Range | Color | Meaning | Action |
|-------------|-------|---------|--------|
| 4-5 | Green | Healthy. No intervention needed. Continue current approach. | Monitor at standard cadence. |
| 3 | Amber | Caution. Dimension requires attention and active management. | Increase monitoring. Create a targeted improvement plan. |
| 1-2 | Red | Unhealthy. Dimension is actively threatening project success. | Escalate. Dedicate resources to recovery. Consider re-baseline. |

**Overall Health Score:**

Calculate the average of all six dimensions. But also report the minimum score -- a project with an average of 4.0 but a Team Health of 1 is not a healthy project.

```
Overall Health = Average of all dimensions
Weakest Dimension = Minimum score across all dimensions
Project Health Status = Color of the weakest dimension
```

### Software Mode: Additional Health Dimensions

Software projects should assess four additional dimensions alongside the core six.

**Code Quality:**

| Score | Definition |
|-------|------------|
| 5 | Code review completion >95%. Linting passes. Low cyclomatic complexity. Minimal code smells. Consistent patterns. |
| 4 | Code review completion >85%. Occasional linting warnings. Complexity manageable. Standards mostly followed. |
| 3 | Code review completion 70-85%. Growing linting warnings. Some complex modules. Standards inconsistently applied. |
| 2 | Code review often skipped. Significant linting failures. High complexity. No consistent patterns. |
| 1 | No code review process. Lint rules disabled. Codebase is a maintenance liability. |

**Test Coverage:**

| Score | Definition |
|-------|------------|
| 5 | Coverage >80% overall, >90% on critical paths. All new code requires tests. Tests are fast and reliable. |
| 4 | Coverage 60-80%. Most new code has tests. Occasional flaky tests. Critical paths well covered. |
| 3 | Coverage 40-60%. Test gaps in important modules. Flaky tests causing false failures. |
| 2 | Coverage 20-40%. Large untested areas. Regression risk is high for any change. |
| 1 | Coverage <20%. No testing culture. Deployments are acts of faith. |

**Deployment Health:**

| Score | Definition |
|-------|------------|
| 5 | Automated deployment. <1% failure rate. Rollback <5 minutes. Feature flags for gradual rollout. |
| 4 | Mostly automated. <5% failure rate. Rollback <30 minutes. Some manual steps. |
| 3 | Semi-automated. 5-15% failure rate. Rollback takes hours. Deployment is stressful. |
| 2 | Mostly manual. >15% failure rate. Rollback is difficult. Deployment requires weekend. |
| 1 | Fully manual. Frequent failures. No rollback capability. Each deployment is a project. |

**Tech Debt Level:**

| Score | Definition |
|-------|------------|
| 5 | Tech debt is low and actively managed. Debt reduction is part of every sprint. No legacy drag. |
| 4 | Tech debt exists but is tracked and prioritized. Team allocates 10-20% capacity to debt. |
| 3 | Tech debt is growing. Team acknowledges it but struggles to allocate time. Velocity impact starting. |
| 2 | Tech debt is significant. It slows every feature. Refactoring needed before new work can proceed. |
| 1 | Tech debt dominates. Team spends more time on workarounds than features. Rewrite discussions occurring. |

### General Mode: Additional Health Dimensions

Non-software projects should assess three additional dimensions.

**Vendor Performance:**

| Score | Definition |
|-------|------------|
| 5 | All vendors delivering on time, on quality, within budget. Strong relationships. |
| 4 | Vendors mostly delivering well. Minor quality or timing issues managed through normal channels. |
| 3 | 1-2 vendors underperforming. Deliverables late or below quality. Active management required. |
| 2 | Vendor issues impacting project. Deliverables significantly late. Considering vendor replacement. |
| 1 | Critical vendor failure. Project blocked by vendor non-delivery. Contractual remedies being invoked. |

**Compliance Status:**

| Score | Definition |
|-------|------------|
| 5 | All regulatory and compliance requirements identified, tracked, and on schedule for approval. |
| 4 | Compliance requirements documented. Submissions on track. No gaps identified. |
| 3 | Some compliance requirements at risk. Submission delays possible. Gaps being addressed. |
| 2 | Compliance gaps exist. Regulatory submission delayed. Project may not meet compliance deadline. |
| 1 | Non-compliance risk. Regulatory failure could halt the project or result in penalties. |

**Benefits Realization Tracking:**

| Score | Definition |
|-------|------------|
| 5 | Benefits clearly defined, baselined, and on track. Early indicators positive. Measurement in place. |
| 4 | Benefits defined and tracked. Expected to realize as planned. Measurement framework active. |
| 3 | Benefits defined but tracking shows some may not be fully realized. Adjustment needed. |
| 2 | Benefits poorly defined or significantly at risk. Stakeholders questioning ROI. |
| 1 | No benefits tracking. Project purpose unclear. "Why are we doing this?" being asked. |

### Health Check Report Template

```
PROJECT HEALTH CHECK REPORT
==============================
Project: _______________
Assessment Date: _______________
Assessor: _______________
Assessment Period: [from] - [to]

HEALTH SUMMARY:
  Overall Score: [X.X] / 5.0
  Weakest Dimension: [Dimension Name] ([Score])
  Overall Status: [Green / Amber / Red]
  Trend: [Improving / Stable / Declining]

DIMENSION SCORES:
| Dimension          | Score | Status | Trend   | Evidence / Notes                    |
|--------------------|-------|--------|---------|-------------------------------------|
| Schedule           | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |
| Scope              | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |
| Budget             | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |
| Team Health        | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |
| Risk               | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |
| Stakeholder        | [1-5] | [R/A/G]| [arrow] | [Key data point supporting score]   |

SOFTWARE-SPECIFIC (if applicable):
| Code Quality       | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |
| Test Coverage      | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |
| Deployment Health  | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |
| Tech Debt          | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |

GENERAL-SPECIFIC (if applicable):
| Vendor Performance | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |
| Compliance Status  | [1-5] | [R/A/G]| [arrow] | [Key data point]                    |
| Benefits Realization| [1-5]| [R/A/G]| [arrow] | [Key data point]                    |

RADAR CHART CONCEPT:
  Plot each dimension on a radial axis (0-5 scale). Connect the points.
  A healthy project has a large, roughly circular shape (all dimensions balanced).
  An unhealthy project has a lopsided shape with one or more dimensions collapsed
  toward the center.

  Visualization tools: Excel radar chart, Google Sheets radar chart, or
  draw.io for a manual version. Include in the report for visual impact.

  Ideal shape:        Unhealthy shape:
       5                   5
      /|\                 /|
     / | \               / |
    /  |  \             /  |
   4---+---4           4---+---1  <-- Team Health collapsed
    \  |  /             \  |  /
     \ | /               \ | /
      \|/                 \|/
       4                   4

CRITICAL FINDINGS:
1. [Finding]: [description, evidence, impact on project]
2. [Finding]: [description, evidence, impact on project]
3. [Finding]: [description, evidence, impact on project]

RECOMMENDED ACTIONS:
| # | Action | Dimension | Priority | Owner | Deadline |
|---|--------|-----------|----------|-------|----------|
| 1 | [Specific improvement action] | [Which dimension] | [Critical/High/Medium] | [Name] | [Date] |
| 2 | [Specific improvement action] | [Which dimension] | [Critical/High/Medium] | [Name] | [Date] |
| 3 | [Specific improvement action] | [Which dimension] | [Critical/High/Medium] | [Name] | [Date] |

COMPARISON TO LAST HEALTH CHECK:
| Dimension | Last Score | Current Score | Change | Commentary |
|-----------|-----------|---------------|--------|------------|
|           |           |               | [+/-]  |            |

NEXT HEALTH CHECK: [Date]
```

### Health Check Cadence

- **Standard projects (overall health Green):** Monthly health check. Enough to catch trends without creating meeting fatigue.
- **Troubled projects (any dimension Amber or Red):** Biweekly health check. Increased frequency ensures recovery actions are being tracked and problems are not worsening.
- **Crisis projects (multiple dimensions Red):** Weekly health check until at least one dimension recovers to Amber. The health check becomes a recovery tracking tool.
- **Post-recovery:** Return to monthly cadence only after all dimensions have been Green for two consecutive assessment periods.

### Orchestrator Agent Integration

The health check triggers the orchestrator agent for cross-stage assessment when:

- Any dimension drops to Red (score 1-2): The orchestrator assesses whether upstream stages (initiation, planning) had gaps that caused the issue and whether downstream stages (execution, closure) will be impacted.
- Overall health score drops below 3.0: The orchestrator performs a full cross-stage review, checking whether the project plan, risk register, resource allocation, and stakeholder alignment are consistent with each other and with reality.
- A dimension changes by 2 or more points in a single period: Rapid deterioration signals a systemic issue that may span multiple project management domains.

The orchestrator produces a cross-stage assessment report that identifies root causes across the project lifecycle and recommends coordinated interventions, not just fixes for the immediate symptom.

### Health Check Anti-Patterns

**Gaming the Scores:**

Team members or PMs inflate health scores to avoid scrutiny or to present a more favorable picture. Symptoms: all dimensions consistently scored 4-5 despite visible problems. Stakeholders surprised by issues that "came out of nowhere." Fix: Require evidence for every score. Each dimension must cite at least one specific data point. Introduce anonymous team surveys for Team Health scoring to prevent social pressure from inflating the number. Have the sponsor or an independent PMO validate scores periodically.

**Health Check Fatigue:**

The health check is conducted so frequently, or the process is so burdensome, that it becomes a box-checking exercise. Team members disengage. Scores become copy-paste from the prior period without reassessment. Fix: Keep the health check lean -- 30 minutes for a 6-dimension assessment. Use the standard cadence (monthly for Green projects). Automate data collection where possible (pull velocity from the project tracker, pull budget from finance, pull deployment metrics from CI/CD). The PM should spend time on interpretation and action planning, not data gathering.

**Not Acting on Results:**

The health check identifies problems, but no actions are taken. The same issues appear in consecutive health checks with the same scores and the same "recommended actions" that are never executed. Fix: Every health check that produces an Amber or Red dimension must generate at least one action item with an owner, a deadline, and a defined outcome. Track action item completion as a meta-metric. If health check actions are consistently not completed, escalate the health check process itself to the steering committee.

---

## Output Formats

### Status Report Template (Software — Sprint Level)

```
SPRINT STATUS REPORT
======================
Sprint: _______________  |  Dates: _______________
Team: _______________    |  Report Date: _______________

VELOCITY:
  Planned: ___ pts  |  Completed: ___ pts  |  4-Sprint Avg: ___ pts
  Variance: ___% from plan

BURNDOWN: [On track / Flat / Hockey stick / Ahead]

SPRINT GOAL: _______________
  Status: [On track / At risk / Missed]

COMPLETED: [list items with points and deployment status]
IN PROGRESS: [list items with points and % complete]
BLOCKERS: [table: item, blocked by, days blocked, owner, ETA]
DEPLOYMENTS: [list with dates and status]
DORA METRICS: [DF, LT, CFR, TTRS with tier]
RISKS/ISSUES: [top 3]
DECISIONS NEEDED: [list]
```

### Status Report Template (General — Project Level)

```
PROJECT STATUS REPORT
=======================
Project: _______________  |  Report Date: _______________
PM: _______________       |  Sponsor: _______________

RAG SUMMARY: [5-dimension table with status, trend, notes]

EARNED VALUE:
  PV: $___  |  EV: $___  |  AC: $___
  SV: $___  |  CV: $___
  SPI: ___  |  CPI: ___
  EAC: $___  |  ETC: $___

KEY ACCOMPLISHMENTS: [3-5 items]
UPCOMING MILESTONES: [table with planned vs. forecast dates]
RISKS/ISSUES: [top 3]
DECISIONS NEEDED: [list]
HELP NEEDED: [list]
```

### Risk Register Template

```
RISK REGISTER
===============
Project: _______________  |  Last Updated: _______________

| ID | Description | Category | Prob | Impact | Score | Owner | Mitigation | Trigger | Status |
|----|-------------|----------|------|--------|-------|-------|------------|---------|--------|
|    |             |          |      |        |       |       |            |         |        |

SCORING: P(H=3,M=2,L=1) x I(H=3,M=2,L=1). Priority: 7-9 Critical, 4-6 Significant, 1-3 Low.
```

### Dependency Map Template

```
DEPENDENCY MAP
================
Project: _______________  |  Last Updated: _______________

| ID | Source | Target | Type | Status | Owner | Due Date | Impact if Late |
|----|--------|--------|------|--------|-------|----------|---------------|
|    |        |        |      |        |       |          |               |

Types: Blocking / Enabling / Shared Resource
Status: On Track / At Risk / Blocked
```

### Health Check Template

```
PROJECT HEALTH CHECK
======================
Project: _______________  |  Date: _______________

| Dimension     | Score (1-5) | Status | Trend | Evidence |
|---------------|-------------|--------|-------|----------|
| Schedule      |             |        |       |          |
| Scope         |             |        |       |          |
| Budget        |             |        |       |          |
| Team Health   |             |        |       |          |
| Risk          |             |        |       |          |
| Stakeholder   |             |        |       |          |

Overall: ___ / 5.0  |  Weakest: ___  |  Status: [R/A/G]

ACTIONS:
| # | Action | Dimension | Owner | Deadline |
|---|--------|-----------|-------|----------|
|   |        |           |       |          |
```


---

## Burndown and Forecasting


Burndown charts and forecasting techniques answer the most important question in project management: "Will we finish on time, and if not, when?" Raw progress tracking tells you where you are. Forecasting tells you where you are headed. The gap between those two is where project management happens.

### Software Mode: Sprint Burndown

**Sprint Burndown Chart:**

The sprint burndown plots story points remaining (Y-axis) against days in the sprint (X-axis). The ideal line is a straight diagonal from total planned points at Day 0 to zero at the final day.

```
Story Points Remaining
  |
40|*
  | *  .
35|  *   .
  |   *    .
30|    *      .        <-- Ideal line (dotted)
  |     *       .
25|      *        .
  |        *        .
20|          *        .
  |            *        .
15|              *        .
  |                *        .
10|                  *        .
  |                    *        .
 5|                      *        .
  |                        *        .
 0|____________________________*_______.___
  Day1  2  3  4  5  6  7  8  9  10

  * = Actual remaining
  . = Ideal burndown
```

**What to read from the shape:** If the actual line tracks close to the ideal line, the team is burning down work at a sustainable, predictable rate. Deviations from the ideal line signal problems (see Warning Signs below).

**Release Burndown Chart:**

The release burndown zooms out from a single sprint to show features or story points remaining across multiple sprints. Each sprint, the remaining work should decrease. If it stays flat or increases, scope is being added faster than work is being completed.

**Burnup Chart:**

A burnup chart plots two lines: total scope (top line) and completed work (bottom line). The advantage over a burndown is that scope changes become visible. If the top line moves up, scope was added. If the bottom line is rising but the top line is rising faster, the team is making progress but losing ground to scope creep. This transparency makes burnup charts the better choice when scope instability is a concern.

**Velocity-Based Forecasting:**

Velocity is the average number of story points completed per sprint, calculated as a rolling average over the last 4-6 sprints. Use velocity to forecast when remaining work will be complete.

**Formula:**

```
Sprints Remaining = Remaining Story Points / Average Velocity
Forecast Completion Date = Current Date + (Sprints Remaining x Sprint Length)
```

**Worked Example:**

```
Remaining backlog: 120 story points
Average velocity (last 6 sprints): 32 points/sprint
Sprint length: 2 weeks

Sprints Remaining: 120 / 32 = 3.75 sprints
Round up: 4 sprints (you cannot ship 0.75 of a sprint)
Forecast Completion: Current date + (4 x 2 weeks) = 8 weeks from now

Confidence adjustment:
  Best case (velocity = 38, highest recent sprint):  120 / 38 = 3.2 sprints = ~7 weeks
  Worst case (velocity = 26, lowest recent sprint):  120 / 26 = 4.6 sprints = ~10 weeks
  Most likely: 8 weeks

Report as: "Forecast completion in 8 weeks (range: 7-10 weeks depending on velocity)."
```

**Monte Carlo Simulation for Probabilistic Forecasting:**

Monte Carlo simulation takes velocity-based forecasting further by running thousands of simulated outcomes based on historical velocity data (including its variability). Instead of a single forecast, you get a probability distribution.

How it works at a practical level:
1. Collect the last 10-20 sprints of velocity data.
2. For each simulation run, randomly sample a velocity value from the historical distribution.
3. Simulate sprint after sprint until remaining work reaches zero. Record how many sprints it took.
4. Repeat 10,000 times.
5. Plot the results as a histogram. The 50th percentile is the "most likely" completion date. The 85th percentile is the "high confidence" date. The 95th percentile is the "very high confidence" date.

Report as: "There is a 50% chance we finish by June 1, an 85% chance we finish by June 15, and a 95% chance we finish by July 1." This gives stakeholders the language to make risk-informed commitments. If they need high confidence, they commit to the 85th percentile date, not the optimistic 50th.

Tools that support Monte Carlo: Jira with plugins (ActionableAgile), Azure DevOps forecasting, or a custom spreadsheet sampling from historical velocity.

### General Mode: Milestone Burndown

For non-software projects, burndown tracks milestones or deliverables remaining (or percent of project scope remaining) over time.

**Earned Value S-Curve:**

The S-curve plots Planned Value, Earned Value, and Actual Cost over the project timeline. It is called an S-curve because well-planned projects ramp up slowly (mobilization), accelerate through the middle phases, and taper off near the end.

```
$$$
  |                                        ____ PV (Planned Value)
  |                                   ___/
  |                              ___/
  |                         ___/
  |                    ___/       ...... EV (Earned Value)
  |               ___/      ...../
  |          ___/      ..../
  |     ___/      ..../         ----- AC (Actual Cost)
  |  __/     ..../         ----/
  | /   ..../         ----/
  |/.../         ----/
  |/        ----/
  |    ----/
  |---/
  |____________________________________________________> Time
```

When the EV line is below the PV line, you are behind schedule (delivering less value than planned). When the AC line is above the EV line, you are over budget (spending more than the value of work completed). The ideal state is EV tracking PV (on schedule) with AC at or below EV (on or under budget).

**Earned Value Worked Example:**

```
Project: Annual Compliance Audit Program
Budget at Completion (BAC): $200,000
Duration: 10 months
Current month: Month 5

Work packages:
  WP1: Policy review        -- Budget: $40,000 -- Planned 100% by Month 3 -- Actual: 100% complete
  WP2: Control testing       -- Budget: $80,000 -- Planned 60% by Month 5  -- Actual: 40% complete
  WP3: Remediation planning  -- Budget: $50,000 -- Planned 20% by Month 5  -- Actual: 10% complete
  WP4: Final reporting       -- Budget: $30,000 -- Planned 0% by Month 5   -- Actual: 0% complete

Planned Value (PV):
  WP1: $40,000 x 100% = $40,000
  WP2: $80,000 x 60%  = $48,000
  WP3: $50,000 x 20%  = $10,000
  WP4: $30,000 x 0%   = $0
  Total PV = $98,000

Earned Value (EV):
  WP1: $40,000 x 100% = $40,000
  WP2: $80,000 x 40%  = $32,000
  WP3: $50,000 x 10%  = $5,000
  WP4: $30,000 x 0%   = $0
  Total EV = $77,000

Actual Cost (AC): $95,000 (from finance system)

SV = $77,000 - $98,000 = -$21,000  (behind schedule)
CV = $77,000 - $95,000 = -$18,000  (over budget)
SPI = $77,000 / $98,000 = 0.79     (seriously behind schedule)
CPI = $77,000 / $95,000 = 0.81     (seriously over budget)
EAC = $200,000 / 0.81 = $246,914   (projected cost: $46,914 over budget)
ETC = $246,914 - $95,000 = $151,914

Action: SPI and CPI are both below 0.80. Escalate immediately.
Present options to steering committee:
  Option A: Add 2 contractors to control testing. Cost: ~$20K. Recovers 3 weeks.
  Option B: Reduce scope of control testing from 100% to risk-based sample (60%).
            Saves ~$25K and 4 weeks. Requires regulatory approval.
  Option C: Extend timeline by 2 months. No additional cost. Delays final report.
```

**Percent Complete Calculation Methods:**

Different methods for calculating percent complete have different trade-offs. Choose the method that fits your project's needs and apply it consistently.

| Method | How It Works | Pros | Cons | Best For |
|--------|-------------|------|------|----------|
| **0/100** | Item is 0% until fully complete, then 100%. No partial credit. | Simple. Eliminates "almost done" syndrome. No subjective estimation. | Understates progress on long-duration tasks. Can make burndown look flat then suddenly jump. | Short-duration tasks (<1 week). Projects with many small deliverables. |
| **50/50** | Item is 0% until started, jumps to 50%, then 100% when complete. | Balances simplicity with credit for work in progress. Easy to apply. | Still somewhat coarse. A task at 80% effort looks the same as one at 10%. | Medium-duration tasks (1-4 weeks). Status reports where rough progress is sufficient. |
| **Milestones Weighted** | Define 3-5 milestones within a task, each worth a percentage (e.g., draft = 30%, review = 60%, approved = 100%). | Granular and objective. Based on observable deliverables, not estimates. Reduces gaming. | Requires upfront milestone definition for every task. More setup effort. | Long-duration tasks (>4 weeks). High-value deliverables where accuracy matters. Earned value analysis. |

### Forecast Accuracy Tracking

Your forecasts are only useful if they are reliable. Track forecast accuracy over time to improve your estimation and build stakeholder trust.

**How to track:**

At each reporting period, record:
1. The forecast completion date (or forecast cost at completion)
2. The actual completion date (or actual cost) when the project finishes

**Calculate forecast accuracy:**

```
Forecast Error = |Forecast - Actual| / Actual x 100%

Example:
  Sprint 3 forecast: Project completes in Sprint 8
  Actual completion: Sprint 10
  Forecast Error: |8 - 10| / 10 = 20%
```

Plot forecast error over time. As the project progresses, forecasts should converge toward the actual outcome. If forecast error is not decreasing over time, your estimation process is broken -- you are not incorporating new information.

**Benchmark:** Forecasts made at the 50% completion mark should be within 10-15% of the actual outcome. Forecasts at 75% completion should be within 5%.

### Warning Signs in Burndown Shapes

**Flat Line (Blocked):**

```
Points |*  *  *  *  *  *  *
       |                     .
       |                       .
       |_________________________._> Days
```

Description: Remaining work is not decreasing. The line is horizontal for multiple days or reporting periods. The team is working but not completing anything.

Causes: Blockers preventing completion. Work in progress is too high (everything started, nothing finished). Dependencies not resolved. Stories are too large to complete within the period.

Recommended Action: Conduct an immediate blocker review. Limit work in progress. If stories are too large, split them. Escalate dependency blockers within 24 hours.

**Hockey Stick (Back-Loaded):**

```
Points |*  *  *  *  *  *
       |                  *
       |                    *
       |                      *
       |                        *
       |__________________________> Days
```

Description: Little progress early in the period, then a steep drop near the end. Teams scramble to complete work in the final days.

Causes: Procrastination or delayed starts. Unclear requirements causing rework cycles. Testing and review pushed to the end. "Student syndrome" -- starting late because the deadline seems far away.

Recommended Action: Enforce daily standups focused on "what did you finish yesterday?" (not "what did you work on?"). Move acceptance criteria review to the start of each story, not the end. Implement WIP limits. Set mid-sprint checkpoints.

**Scope Creep Sawtooth:**

```
Points |*
       |  *
       |    *      *
       |      *  *   *
       |        *      *
       |                 *
       |                   *
       |_____________________> Days
```

Description: The burndown drops, then jumps back up, then drops again, creating a jagged sawtooth pattern. Progress is being offset by new work being added.

Causes: Scope is being added mid-sprint or mid-period without removing other work. Change control is weak or absent. Stakeholders are injecting new requirements directly to the team. Bug discoveries adding unplanned work.

Recommended Action: Enforce change control. New work in the current sprint requires removing equivalent effort. Make scope additions visible to the sponsor. Track "scope added after sprint start" as a metric and report it.

**Early Completion (Over-Estimated):**

```
Points |*
       |  *
       |    *
       |      *
       |        *
       |          *  (done -- 4 days early)
       |            .
       |              .
       |________________.> Days
```

Description: Work completes well before the planned end date. The burndown hits zero with significant time remaining.

Causes: Estimates were too conservative. Team sandbagged estimates to create a buffer. Scope was reduced without adjusting the plan. Team is significantly more experienced than when estimates were made.

Recommended Action: Recalibrate estimation by reviewing historical actuals vs. estimates. Pull forward work from the next period. Use the slack time for tech debt reduction, documentation, or skill development. Gradually right-size estimates over 2-3 cycles.

### Forecasting Anti-Patterns

**Optimism Bias:**

Every forecast assumes the best case. "We will recover the lost time next sprint." "The vendor will definitely deliver on Friday." "The new hire will be productive immediately." Humans systematically underestimate effort and overestimate speed. Fix: Use historical data, not hopes. If the team has averaged 32 points per sprint for 6 sprints, the forecast should use 32, not the aspirational 40. Add a buffer: forecast using the 25th percentile velocity (worst recent sprint), not the average.

**Using Best-Case as Plan:**

The plan assumes everything goes right. No one gets sick. No requirements change. No infrastructure breaks. No dependencies slip. This is not a plan -- it is a fantasy. Fix: Plan using expected case (average velocity, average cost rates). Set the committed date using the 85th percentile forecast. Keep the best-case date as an internal stretch goal, never as an external commitment.

**Not Updating Forecasts:**

The forecast was made 3 months ago and has not been revised despite significant changes in velocity, scope, and team composition. Stakeholders are operating on stale information. Fix: Update the forecast at every reporting period. Even if the forecast has not changed, confirm it: "Forecast reconfirmed as of March 1: on track for June 15 completion." This builds trust that the forecast is actively maintained.
