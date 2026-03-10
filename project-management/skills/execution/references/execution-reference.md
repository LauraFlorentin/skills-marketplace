# Execution — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Decision Management

Projects die more often from unmade decisions than from bad decisions. A structured decision management process ensures decisions are made deliberately, documented for future reference, and reversible when new information emerges.

### Decision Log Template

Maintain a single, living decision log for the project. Every material decision goes here -- not buried in email threads, Slack messages, or meeting notes.

```
DECISION LOG
==============
Project: _______________
Owner: _______________
Last Updated: _______________

| ID | Date | Decision | Context / Rationale | Alternatives Considered | Made By | Impact | Status |
|----|------|----------|---------------------|------------------------|---------|--------|--------|
| D-001 | 2026-02-10 | Use PostgreSQL for primary datastore | Team has deep Postgres expertise; need JSONB for flexible schemas; strong ecosystem | MySQL (less JSONB support), MongoDB (team lacks NoSQL experience), CockroachDB (overkill for current scale) | Eng Lead + CTO | Architecture — affects all services | Active |
| D-002 | 2026-02-14 | 2-week sprint cadence | Team is mid-size (6 devs); need balance of feedback speed and feature completion | 1-week (too much ceremony overhead), 3-week (delays feedback), Kanban (team prefers time-boxed iterations) | Scrum Master + Team | Process — affects all planning | Active |
| D-003 | 2026-02-20 | Defer mobile app to Q3 | Insufficient data on mobile usage; web activation is the critical path; mobile would split the team | Build mobile now (splits focus), React Native (still splits focus), Progressive Web App (explored, poor offline support) | PM + CTO | Roadmap — delays mobile by 1 quarter | Active |
| D-004 | 2026-03-01 | Switch from REST to GraphQL for new endpoints | Front-end team spends 40% of time assembling data from multiple REST calls; GraphQL reduces this | Keep REST (familiar but slow for FE), gRPC (no browser support), BFF pattern (adds complexity) | Eng Lead | Architecture — new endpoints only; existing REST unchanged | Active |

Status values: Active | Superseded (by D-XXX) | Reversed (reason: ___)
```

### Decision-Making Frameworks

#### RAPID (Recommend, Agree, Perform, Input, Decide)

RAPID clarifies who plays which role in a decision. Use it when decisions stall because too many people think they have veto power, or when no one is willing to make the call.

| Role | Responsibility | Who |
|---|---|---|
| **R** - Recommend | Proposes a course of action with analysis and evidence. Does the legwork. | The person or team closest to the problem |
| **A** - Agree | Must agree before the decision proceeds. Has formal veto power. Use sparingly -- 1-2 people max. | Legal, compliance, or a key stakeholder whose domain is directly affected |
| **P** - Perform | Implements the decision once made. | The delivery team |
| **I** - Input | Provides information, data, or perspective to inform the decision. Does not have veto power. | Subject matter experts, affected teams, customers |
| **D** - Decide | Makes the final call. One person only. Accountable for the outcome. | The decision-maker (PM, tech lead, executive -- depends on decision scope) |

**Worked Example: Choosing a Third-Party Authentication Provider**

```
Decision: Select authentication provider for the platform

R (Recommend): Security Engineer — researches options, builds comparison
   matrix, recommends Auth0 based on feature set, SOC 2 compliance,
   and cost at projected scale.

A (Agree): CISO — must confirm the recommendation meets security
   policy. Reviews Auth0's security posture, data residency, and
   incident response SLA. Agrees.

I (Input):
   - Front-end Lead: Provides input on SDK quality and developer experience.
   - Finance: Provides input on budget impact and contract terms.
   - Customer Success: Provides input on customer SSO requirements.

D (Decide): CTO — reviews recommendation and input. Decides to
   proceed with Auth0. Documents rationale in decision log.

P (Perform): Platform Engineering team — implements Auth0 integration,
   migrates existing users, updates documentation.
```

#### Consent-Based Decision-Making

In consent-based decision-making, a proposal passes unless someone has a reasoned, material objection. It is not about everyone agreeing -- it is about no one having a fundamental objection. This is faster than consensus and more inclusive than autocratic decision-making.

**How it works:**
1. A team member presents a proposal with context and rationale.
2. The facilitator asks: "Does anyone have a principled objection to this proposal?" (Not "does everyone agree?" -- the framing matters.)
3. If no objections, the proposal is adopted.
4. If there is an objection, the objector must articulate why the proposal would cause harm or move the team backward. "I don't like it" is not a valid objection. "This would violate our SLA commitment to customers" is.
5. The proposer and objector work to modify the proposal to address the objection, then re-test for consent.

**When to use:** Team-level process decisions, working agreements, approach selection when the team will implement the decision. Not suitable for high-stakes irreversible decisions (use RAPID for those).

#### Lazy Consensus

Lazy consensus is the lightest-weight decision process. A proposal is made (often via email or Slack). If no one objects within a defined time window, the proposal is adopted.

**How it works:**
1. Proposer sends a message: "I propose we [action]. Unless someone objects by [date/time], I will proceed."
2. If no objection by the deadline, the proposer proceeds.
3. If someone objects, the proposer and objector discuss. If they cannot resolve, escalate to a decision-maker.

**When to use:** Low-risk, reversible decisions. Minor process changes. Technical choices within a single component. Day-to-day operational decisions. Not suitable for decisions affecting multiple teams, significant budget, or external commitments.

### Software Mode: Architecture Decision Records (ADR)

ADRs are a lightweight documentation format for recording significant architectural decisions. They create a decision trail that helps future team members understand why the system is built the way it is.

**ADR Format:**

```
ADR-[number]: [Title]
======================
Status: Proposed | Accepted | Deprecated | Superseded by ADR-[number]
Date: [Date decided]
Deciders: [Who made this decision]

CONTEXT
What is the issue? What forces are at play? What constraints exist?
[2-5 sentences describing the situation that requires a decision.]

DECISION
What is the change that we are proposing and/or doing?
[1-3 sentences. Be specific.]

CONSEQUENCES
What becomes easier or more difficult as a result of this decision?

Positive:
- [Benefit 1]
- [Benefit 2]

Negative:
- [Trade-off 1]
- [Trade-off 2]

Neutral:
- [Side effect that is neither good nor bad]
```

**Worked ADR Example:**

```
ADR-007: Use event sourcing for order management
==================================================
Status: Accepted
Date: 2026-02-18
Deciders: Eng Lead, Staff Engineer, CTO

CONTEXT
The order management system currently uses a CRUD model with a single
orders table. As order complexity grows (partial fulfillment, returns,
exchanges, subscription modifications), we are losing critical state
transition history. Debugging order issues requires reconstructing
state from log files. Customer support cannot answer "what happened
to this order?" without engineering involvement.

DECISION
We will implement event sourcing for the order management domain.
All state changes will be recorded as immutable events. The current
state will be derived by replaying events. We will use a separate
read model (CQRS) for query performance.

CONSEQUENCES
Positive:
- Complete audit trail for every order state change
- Customer support can view order history without engineering
- Enables temporal queries ("what was the order state at 3pm Tuesday?")
- Simplifies complex state transitions (partial fulfillment, returns)

Negative:
- Steeper learning curve for engineers unfamiliar with event sourcing
- Read model adds infrastructure complexity (eventual consistency)
- Event schema evolution requires careful versioning
- Higher storage requirements (events are append-only)

Neutral:
- Will require a 2-sprint migration effort for existing orders
- Monitoring and alerting must be updated for new data flow
```

**Buy vs. Build Decision Framework:**

| Factor | Weight | Build (Score 1-5) | Buy (Score 1-5) |
|---|---|---|---|
| Core competency alignment | 25% | Is this central to your product's value? | Is this commodity infrastructure? |
| Total cost of ownership (3 years) | 20% | Dev cost + maintenance + ops + opportunity cost | License + integration + customization + vendor lock-in |
| Time to market | 20% | How long to build, test, and stabilize? | How long to integrate and go live? |
| Customization needs | 15% | Do you need deep control over behavior? | Can you live with the vendor's constraints? |
| Team expertise | 10% | Does the team have the skills? Will building it grow them? | Is the team better spent on core product? |
| Vendor risk | 10% | No vendor dependency, but you own all maintenance | Vendor could raise prices, sunset product, or get acquired |

**Rule of thumb:** Build what differentiates you. Buy everything else. If the component is not a source of competitive advantage, the opportunity cost of building it is almost always higher than the license fee.

### General Mode: Business Decisions

**Vendor Selection Criteria Matrix:**

```
VENDOR EVALUATION MATRIX
==========================
Decision: _______________
Date: _______________
Evaluators: _______________

| Criterion | Weight | Vendor A | Vendor B | Vendor C |
|-----------|--------|----------|----------|----------|
| Capability fit | 25% | [1-5] | [1-5] | [1-5] |
| Cost (TCO 3-year) | 20% | [1-5] | [1-5] | [1-5] |
| Implementation timeline | 15% | [1-5] | [1-5] | [1-5] |
| References / track record | 15% | [1-5] | [1-5] | [1-5] |
| Support & SLA | 10% | [1-5] | [1-5] | [1-5] |
| Integration with existing systems | 10% | [1-5] | [1-5] | [1-5] |
| Financial stability of vendor | 5% | [1-5] | [1-5] | [1-5] |
| Weighted Total | 100% | ___ | ___ | ___ |

RECOMMENDATION: Vendor [X] — Rationale: _______________
RISKS: _______________
NEXT STEPS: _______________
```

### Decision Escalation Criteria

**Escalate a decision when:**
- The decision affects multiple teams or workstreams and no single team has authority
- The decision has budget implications beyond the PM's approval authority
- Stakeholders disagree and cannot reach consent within 48 hours
- The decision is irreversible or very costly to reverse (technology migration, vendor contract, public commitment)
- The decision changes committed scope, timeline, or budget
- Legal, regulatory, or compliance implications exist

**Escalation path:**
1. Team-level decisions: Team lead or PM decides, logs in decision log
2. Cross-team decisions: Program manager or product director decides, with input from affected teams
3. Strategic decisions: Executive sponsor or steering committee decides, with recommendation from PM
4. Organizational decisions: C-level, with recommendation from the program team

### Decision Anti-Patterns

1. **Analysis paralysis.** The team gathers more and more data but never decides. Decisions stall for weeks. Fix: Set a decision deadline. "We will decide by Friday. If we do not have perfect information by then, we decide with what we have." Most decisions are reversible -- act on 70% confidence.
2. **HiPPO (Highest Paid Person's Opinion).** The most senior person in the room makes the decision, overriding analysis and team input. Fix: Use RAPID. The senior person is the D (Decide) role, but the R (Recommend) role presents analysis first. The D should override the R only with stated rationale, documented in the decision log.
3. **Decisions without documentation.** A decision is made in a hallway conversation or Slack thread and never recorded. Three months later, no one remembers why. Fix: No decision is real until it is in the decision log. If it is not logged, it did not happen.
4. **Revisiting decided issues.** A decision is made, but a stakeholder who was absent reopens it. The team re-litigates the same arguments. Fix: The decision log includes the date, deciders, and rationale. If someone wants to revisit, they must present new information that was not available at the time of the decision. "I disagree" is not new information.
5. **Decision by committee.** Everyone must agree before the team can proceed. This produces watered-down compromises that satisfy no one. Fix: Use consent-based or RAPID. One person decides. Others provide input. Disagreement is logged but does not block action.

---

## Change Management

Change is inevitable. Scope changes, priority shifts, new information, stakeholder requests, technical discoveries -- all of these require the team to adapt. The goal of change management is not to prevent change but to manage it deliberately: assess impact, make informed decisions, and maintain project integrity.

### Change Request Template

Every change request should be documented before work begins. This prevents scope creep, creates an audit trail, and ensures the team understands the full impact before committing.

```
CHANGE REQUEST
================
CR-ID: CR-[number]
Project: _______________
Date Submitted: _______________
Requestor: _______________
Priority: Critical | High | Medium | Low

DESCRIPTION:
What is being requested? Be specific.
[2-4 sentences describing the change.]

JUSTIFICATION:
Why is this change needed? What happens if we do not make it?
[2-4 sentences. Reference business need, customer feedback, risk, or new information.]

IMPACT ANALYSIS:
  Scope: [What deliverables change? What is added, removed, or modified?]
  Schedule: [Does this extend the timeline? By how much?]
  Cost: [Additional budget required? Resource reallocation?]
  Risk: [New risks introduced? Existing risks changed?]
  Quality: [Does this affect testing, performance, or reliability targets?]

EFFORT ESTIMATE:
  [X] person-days / [Y] story points
  Teams affected: _______________

ALTERNATIVES:
  Option A: [Implement as requested — impact summary]
  Option B: [Modified approach — reduced scope, same benefit]
  Option C: [Defer to next phase/sprint — no immediate action]

APPROVAL:
  | Approver | Role | Decision | Date |
  |----------|------|----------|------|
  |          |      | Approve / Reject / Defer | |

APPROVAL STATUS: Pending | Approved | Rejected | Deferred
```

### Impact Analysis Framework

When a change request arrives, run it through this analysis before approving or rejecting.

**Four questions to answer:**

1. **What changes?** Map every deliverable, component, and dependency that the change touches. A "small" UI change may require API changes, database migration, test updates, documentation updates, and deployment coordination. List everything.

2. **What is affected downstream?** If this change delays Deliverable A, does that cascade to Deliverable B? If the database schema changes, do existing reports break? Think two steps ahead.

3. **What is the cost of change vs. cost of not changing?** Quantify both sides.
   - Cost of change: effort, delay, risk, rework.
   - Cost of not changing: missed revenue, customer churn, technical debt, compliance violation.
   - If the cost of not changing exceeds the cost of changing, approve. Otherwise, defer or reject.

4. **What is the risk delta?** Does this change increase or decrease project risk? A change that adds scope increases risk. A change that removes a flaky dependency decreases risk. Include both in the assessment.

### Software Mode: Technical Changes

**Feature scope changes:** When a feature's requirements expand or shift mid-sprint, assess whether the sprint goal is still achievable. If yes, adjust stories within the sprint. If no, negotiate with the Product Owner: either remove a lower-priority story to make room or defer the change to the next sprint.

**Technical pivots:** When the team discovers mid-implementation that the chosen approach will not work (performance is unacceptable, a library has a critical bug, a dependency is deprecated), document the pivot as an ADR and update the change log. Do not treat technical pivots as failures -- they are learning.

**Dependency changes:** When an external dependency changes (API version update, vendor sunset, infrastructure migration), assess impact on all downstream services. Use a dependency map to trace the blast radius.

**Feature flags as partial change mechanism:** Feature flags allow the team to deploy code without activating it for users. This enables:
- Incremental delivery: Ship partially complete features behind a flag
- Risk reduction: Roll back a feature without rolling back a deployment
- A/B testing: Expose the feature to a subset of users
- Phased rollout: 1% -> 10% -> 50% -> 100% over days or weeks

When a change request is approved but carries risk, require a feature flag as a condition of approval. "Approved, but must be behind a flag with a kill switch."

### General Mode: Formal Change Control

**Change Control Board (CCB):**

For larger projects or regulated environments, establish a Change Control Board that reviews and approves all change requests above a defined threshold.

**CCB composition:** Project sponsor (chair), PM, technical lead, business lead, QA lead (optional), finance representative (for budget changes).

**CCB cadence:** Weekly during active execution, bi-weekly during lower-activity phases.

**Change Categories and Approval Paths:**

| Category | Definition | Approval Path | Examples |
|---|---|---|---|
| **Minor** | < 5% impact on scope, schedule, or cost. No new risks. | PM approves, logs in change log, informs CCB | Rewording a deliverable, adjusting a task deadline by 2 days, adding a minor clarification |
| **Significant** | 5-15% impact on scope, schedule, or cost. Manageable new risks. | PM recommends, CCB approves | Adding a new deliverable, extending timeline by 1-2 weeks, reallocating budget between workstreams |
| **Major** | > 15% impact on scope, schedule, or cost. Material new risks. Changes project objectives or success criteria. | PM recommends, CCB reviews, Sponsor approves | Adding a new workstream, extending timeline by 1+ month, increasing budget, changing project objectives |

**Integrated Change Control (per PMBOK):**

Integrated change control means evaluating every change against the entire project baseline -- not just the directly affected area. A scope change affects schedule, cost, quality, risk, resources, and communications. Evaluate all six dimensions before approving.

### Scope Creep Detection Signals

Scope creep is the gradual, uncontrolled expansion of project scope without corresponding adjustments to time, cost, or resources. It is the most common cause of project failure. Watch for these signals:

1. **"While we're at it..." requests.** Stakeholders append small additions to approved work. Each one is minor, but they accumulate. "While we're building the report, can we also add export to PDF?" "And Excel?" "And scheduled email delivery?"

2. **Requirements discovered during implementation.** The team finds that a story is more complex than estimated. Instead of re-scoping, they absorb the extra work silently. Sprint after sprint, the team falls further behind.

3. **Stakeholder-direct requests to developers.** A stakeholder asks an engineer directly for a "quick change," bypassing the PM and the backlog. The engineer, wanting to be helpful, implements it. The PM does not know until the sprint review.

4. **Deliverables growing in detail.** A report that was scoped as "10 pages" becomes "25 pages with executive appendix." A dashboard with "3 charts" becomes "3 charts, 2 tables, a filter panel, and drill-down capability."

5. **New stakeholders appearing mid-project.** A new VP joins the steering committee and adds their priorities without removing existing scope. The project gains a new master but the same timeline.

6. **"Must-have" features appearing after scope lock.** Requirements that were not identified during planning suddenly become critical after development starts. The team is told to accommodate them without adjusting the timeline.

7. **Testing scope expanding.** QA discovers edge cases that were not in the original acceptance criteria. Instead of deferring them, the team is expected to handle all of them in the current phase.

8. **No formal change request for additions.** Work is added to the project without a change request. If the team is doing work that was not in the original plan and no CR exists, scope creep is happening.

**Prevention Strategies:**
- Require a change request for every addition, no matter how small. The process itself is a deterrent.
- Maintain a visible scope baseline document. When someone asks for something new, show them the baseline and ask: "What should we remove to make room?"
- Educate stakeholders: "Every addition has a cost. We can do this, but it means [trade-off]."
- Empower the PM to say no. If the PM cannot reject scope changes without executive override, scope creep is a governance failure, not a PM failure.

### Change Log Template

Track all approved changes in a single log to maintain a complete history of how the project evolved from its original baseline.

```
CHANGE LOG
============
Project: _______________
Baseline Date: _______________
Last Updated: _______________

| CR-ID | Date Approved | Description | Impact Summary | Approved By | Cumulative Schedule Impact | Cumulative Cost Impact |
|-------|---------------|-------------|----------------|-------------|---------------------------|----------------------|
| CR-001 | 2026-02-12 | Add SSO support for enterprise clients | +2 weeks, +$15K | Sponsor | +2 weeks | +$15K |
| CR-002 | 2026-02-20 | Remove mobile-responsive dashboard (deferred to Phase 2) | -1 week, -$8K | PM | +1 week | +$7K |
| CR-003 | 2026-02-28 | Switch payment provider from Stripe to Adyen (EU regulatory) | +1 week, +$5K | CCB | +2 weeks | +$12K |

BASELINE vs. CURRENT:
  Original end date: 2026-06-15
  Current projected end date: 2026-06-29 (+2 weeks)
  Original budget: $200,000
  Current projected budget: $212,000 (+6%)
```

### Change Management Anti-Patterns

1. **Rubber-stamping.** The CCB approves every change request without meaningful analysis. The change process exists on paper but provides no actual governance. Fix: Require the impact analysis fields to be completed before the CCB meeting. Reject incomplete submissions. Ask "what do we cut to make room?" for every addition.

2. **Change avoidance.** The PM or CCB rejects all changes to "protect the baseline." The project delivers exactly what was originally planned, but the original plan no longer reflects reality. The deliverables are on time but useless. Fix: Change is not the enemy -- uncontrolled change is. Evaluate each request on its merits. If the business case is strong, approve it and adjust the plan.

3. **Gold plating.** The team adds features, polish, or functionality beyond what was requested. No one asked for it, but the team "thought it would be nice." This consumes capacity that should go to committed deliverables. Fix: The scope baseline is the ceiling, not the floor. If the team finishes early, they pull the next item from the backlog -- they do not embellish the current item.

4. **Informal changes.** Changes are made through hallway conversations, Slack messages, or verbal agreements. No documentation, no impact analysis, no approval. Three months later, the project is 30% over scope and no one can explain how. Fix: No change is authorized until it has a CR number in the change log. Verbal agreements are not binding.

5. **Change request as punishment.** The process is so bureaucratic and slow that people avoid it. They either absorb extra work silently (scope creep) or refuse reasonable requests (change avoidance). Fix: The change process should take minutes for minor changes and hours for major ones. If it takes weeks, the process is the problem, not the people.

---

## Output Templates Summary

### Quick Reference: Which Template When

| Situation | Template | Section |
|---|---|---|
| Need a daily team sync format | Async Standup Template or Kanban Daily | Standups & Daily Coordination |
| Planning a sprint or iteration | Sprint Planning / Phase Planning Template | Sprint/Iteration Planning |
| Recording a project decision | Decision Log Template | Decision Management |
| Documenting an architecture choice | ADR Format | Decision Management |
| Evaluating vendors | Vendor Selection Criteria Matrix | Decision Management |
| Someone requests a scope change | Change Request Template | Change Management |
| Tracking all approved changes | Change Log Template | Change Management |
| Weekly team coordination | Weekly Team Check-In Template | Standups & Daily Coordination |
| Multi-workstream program sync | Workstream Coordination Format | Sprint/Iteration Planning |
| Calculating sprint capacity | Capacity Calculation Formula | Sprint/Iteration Planning |
| Forecasting project completion | Velocity + Earned Value | Sprint/Iteration Planning |
