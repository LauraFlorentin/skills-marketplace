---
name: execution
description: Standups, sprint planning, decision tracking, and change management for software and general PMs
triggers:
  - standup
  - daily standup
  - sprint plan
  - iteration planning
  - decision log
  - decision record
  - adr
  - change request
  - change management
  - scope change
  - kanban
---

# Execution

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

---

## Standups & Daily Coordination

The daily standup is the heartbeat of execution. Done well, it keeps the team aligned, surfaces blockers before they metastasize, and creates a shared sense of progress. Done poorly, it becomes a performative status report that wastes everyone's time and teaches the team to tune out.

### Software Mode: Daily Standup

The classic format is three questions per person. Time-box the entire meeting to 15 minutes, regardless of team size. If 15 minutes is not enough, the team is too large for a single standup -- split into sub-teams.

**Three Questions:**
1. What did I complete since the last standup?
2. What will I work on before the next standup?
3. What is blocking me?

**Ground rules:**
- Stand up. Literally. Standing discourages rambling.
- Start on time. Do not wait for latecomers. They will learn.
- Each person speaks for 90 seconds max. Use a timer if needed.
- Direct updates to the team, not to the scrum master or manager. This is peer coordination, not a status report.
- Blockers get named, not solved. If a blocker needs discussion, note it and schedule a follow-up immediately after standup. "Let's take that offline" is the most important phrase in standup.
- Walk the board. If you use a physical or digital board, move cards as you speak. This makes progress visible and catches items that are stuck.

**Async Standup Template (Slack / Messaging):**

For distributed teams or teams spanning 3+ time zones, synchronous standups may not work. Use an async format posted in a dedicated channel by a consistent time each day.

```
ASYNC STANDUP — [Date]
=======================
Team: _______________
Channel: #standup-[team-name]
Post by: [time] [timezone] daily

[Your Name]
  Done: [What you completed since last update]
  Today: [What you plan to work on]
  Blocked: [Anything preventing progress — tag the person who can help]
  FYI: [Optional — context the team should know but that is not a blocker]

Example:
[Jamie Chen]
  Done: Finished API endpoint for user preferences (PR #342 open for review)
  Today: Starting front-end integration for preferences panel
  Blocked: Waiting on design spec for mobile layout — @Alex can you share by EOD?
  FYI: CI pipeline was flaky this morning, re-ran twice before green
```

**When to use async vs. sync standups:**

| Factor | Use Synchronous | Use Asynchronous |
|---|---|---|
| Time zones | Team within 3-hour spread | Team spans 4+ hours |
| Team size | 3-8 people | Any size (scales better) |
| Collaboration density | High interdependence, frequent pairing | Independent work streams |
| Blockers | Frequent, need real-time discussion | Infrequent, can wait hours for resolution |
| Culture | Team prefers face-to-face, energy from sync | Team prefers deep work, dislikes interruptions |

**Standup Anti-Patterns:**

These failure modes kill the value of standups. If you observe any, correct immediately.

1. **Status report to the manager.** Team members address updates to the lead or manager instead of peers. Fix: The manager stops attending for two weeks, or deliberately looks away while others speak. Standups are for the team, not for management visibility.
2. **Going over 15 minutes.** Updates ramble. People tell stories instead of stating facts. Fix: Use a visible timer. Cut off at 90 seconds per person. Appoint a facilitator who enforces time-boxing without exception.
3. **Problem-solving in standup.** Someone raises a blocker and the team spends 8 minutes debugging it. Fix: The facilitator says "park it" and writes it on a parking lot list. Interested parties stay after standup to discuss. Everyone else leaves.
4. **Skipping blockers.** People say "no blockers" reflexively even when they are stuck. Fix: Ask explicitly: "Is there anything slowing you down, even if it's not fully blocked?" Normalize raising small impediments.
5. **Not updating the board.** People give verbal updates but the Kanban or sprint board does not reflect reality. Fix: Walk the board instead of doing round-robin. Start with the rightmost column (closest to done) and move left.
6. **Attendance creep.** Stakeholders, managers, and "interested parties" join and the meeting grows to 15 people. Fix: Standups are for the delivery team only. Observers can read the async summary. No chickens at standup.

**Kanban Daily: Board-Focused Standup**

If the team uses Kanban rather than Scrum, the standup focuses on the board, not on individuals. Walk the board right to left.

- **Start with blocked items.** What is stuck? Who can unblock it? By when?
- **Review items approaching WIP limits.** If a column is at or near its WIP limit, the team should pull less and finish more. "Stop starting, start finishing."
- **Check cycle time.** Are any items aging beyond the team's cycle time target? Flag items that have been in progress for longer than the 85th percentile cycle time.
- **Pull new work only if capacity exists.** Do not start new items if WIP limits are hit. Help finish existing items instead.

### General Mode: Team Check-In

For non-software teams (operations, marketing, consulting, cross-functional programs), daily standups may be too frequent. Use a weekly or twice-weekly check-in instead, but follow the same principles: time-boxed, focused on coordination, not status reporting.

**Weekly Team Check-In Template:**

```
WEEKLY TEAM CHECK-IN
======================
Team: _______________
Date: _______________
Facilitator: _______________
Duration: 30 minutes

ROUND 1: PROGRESS (10 min)
Each person — 2 minutes max:
  - What did you deliver or advance this week?
  - Are you on track against the plan?

ROUND 2: UPCOMING (8 min)
Each person — 1 minute max:
  - What are your top priorities for next week?
  - Any upcoming milestones or deadlines?

ROUND 3: NEEDS & BLOCKERS (7 min)
  - Resource needs: Does anyone need help, budget, or access?
  - Decisions needed: What decisions are pending that block progress?
  - Dependencies: Is anyone waiting on someone else? Flag it.

ROUND 4: ANNOUNCEMENTS (5 min)
  - Org-wide updates, schedule changes, new information
  - Celebrate wins — name specific accomplishments

PARKING LOT:
  - [Topic] — Owner: ___ — Follow-up by: [date]
  - [Topic] — Owner: ___ — Follow-up by: [date]
```

**Vendor / Contractor Coordination Cadence:**

When external parties are involved, establish a separate coordination rhythm. Do not mix vendor check-ins with internal standups -- the information needs and trust levels are different.

| Vendor Relationship | Cadence | Format | Focus |
|---|---|---|---|
| Strategic partner (long-term, embedded) | Weekly 30 min | Video call | Progress, blockers, upcoming dependencies, change requests |
| Project contractor (fixed deliverable) | Bi-weekly 30 min | Video call or email | Milestone progress, deliverable quality, timeline adherence |
| Staff augmentation (individual contributors) | Daily standup (join team) | Same as team standup | Treat as team member; include in all coordination |
| Advisory / consulting | Monthly 60 min | In-person or video | Strategic alignment, deliverable review, course correction |

### Escalation Criteria: Handle in Standup vs. Escalate

Not every issue belongs in standup, and not every issue should wait for a formal escalation. Use this guide.

**Handle in standup (or immediately after):**
- A team member needs a code review, design clarification, or quick decision from a peer
- A task is taking longer than expected but the team member has a plan
- A minor dependency is slightly delayed but the team can re-sequence work
- Someone needs access, a tool, or a resource that a peer can provide

**Escalate outside standup:**
- A blocker has persisted for more than 2 business days without resolution
- The blocker requires a decision from someone not on the delivery team (stakeholder, executive, external party)
- The issue affects the sprint goal or a committed milestone
- The issue involves a cross-team dependency where the other team is unresponsive
- There is a resource conflict (two teams need the same person or system)
- A risk has materialized that changes the scope, timeline, or cost of the project

**Escalation path:** Team member raises in standup -> Scrum master / PM documents and follows up within 4 hours -> If unresolved within 24 hours, PM escalates to the sponsor or steering committee with a written summary (what is blocked, what is the impact, what decision is needed).

### Async Standup Best Practices for Distributed Teams

1. **Pick one timezone-neutral posting window.** For example, "post by 10:00 UTC" gives everyone a morning window regardless of timezone.
2. **Use a bot or template.** Automate the daily prompt so no one forgets. Tools like Geekbot, Standuply, or a simple Slack workflow reduce friction.
3. **Read before you write.** Require team members to read yesterday's posts before writing today's. This catches dependencies and duplicated work.
4. **Flag items that need response.** Use a convention like a specific emoji or `@mention` for items that need action from a specific person. Everything else is FYI.
5. **Designate a "standup reviewer."** One person (rotating weekly) reads all posts and flags patterns: repeated blockers, work that is drifting, items with no progress for 2+ days.
6. **Weekly sync as a complement.** Even fully async teams benefit from one synchronous meeting per week (30 minutes) to discuss themes, resolve ambiguity, and maintain team cohesion. Async standup handles the daily pulse; weekly sync handles the human connection.

---

## Sprint / Iteration Planning

Sprint planning translates the backlog into a concrete, achievable plan for the next iteration. It is where strategy meets capacity. The output is not a list of things the team hopes to do -- it is a forecast based on real capacity, clear scope, and shared understanding.

### Software Mode: Sprint Planning

**Sprint Planning Ceremony:**

- **Who attends:** Product Owner, Scrum Master, entire delivery team (engineering, design, QA). No observers, no stakeholders. Planning is a working session, not a presentation.
- **Duration:** 2 hours per week of sprint length. A 2-week sprint gets a 4-hour planning session. If the team consistently finishes planning in less time, shorten it.
- **Inputs:** Prioritized and groomed backlog, team capacity, previous sprint velocity, sprint goal candidates.

**Capacity Calculation Formula:**

```
Sprint Capacity = Team Members x Available Days x Focus Factor

Where:
  Team Members   = Number of people on the delivery team
  Available Days = Working days in the sprint minus PTO, holidays, and known meetings
  Focus Factor   = Percentage of time available for sprint work (typically 0.6-0.8)

Focus Factor guidance:
  0.8 = Experienced team, minimal meetings, stable codebase
  0.7 = Average team, moderate meeting load, some support duties
  0.6 = New team, heavy meeting load, on-call rotation, or significant tech debt

Worked Example:
  Team: 6 engineers
  Sprint: 2 weeks = 10 working days
  PTO: 1 engineer out for 3 days = effectively 5.7 engineers average
  Focus Factor: 0.7 (moderate meeting load, some on-call duties)

  Capacity = 5.7 x 10 x 0.7 = 39.9 person-days

  If historical velocity is 40 story points per sprint,
  and 1 story point ~ 1 person-day for this team,
  then target ~39-40 story points for this sprint.
```

**Sprint Goal Setting:**

The sprint goal is a single sentence describing the outcome the team commits to achieving. It is not a list of stories. It provides focus and gives the team flexibility to adjust scope within the sprint if surprises arise.

| Quality | Bad Sprint Goal | Good Sprint Goal |
|---|---|---|
| Specificity | "Work on the payments feature" | "Users can complete a purchase using credit card checkout" |
| Outcome focus | "Finish stories PY-101 through PY-108" | "Reduce checkout abandonment by enabling guest checkout" |
| Testability | "Make progress on performance" | "Search results load in under 200ms at p95 in staging" |
| Single focus | "Do payments, search, and onboarding" | "Complete the credit card payment flow end-to-end" |

**Story Selection Process:**

1. Product Owner presents the sprint goal and the top-priority stories from the backlog.
2. Team reviews each story. Confirm it meets the Definition of Ready (see below). If not, send it back for grooming.
3. Team estimates capacity and pulls stories until capacity is reached. The team decides how much they can commit to -- the Product Owner does not dictate.
4. For each story, the team breaks it into tasks and identifies who will work on what. This is not binding assignment -- it is initial planning.
5. Team confirms: "We believe we can achieve the sprint goal and complete these stories within the sprint."

**Definition of Ready Checklist:**

A story must meet all of these criteria before it enters a sprint.

- [ ] User story written in standard format (As a [persona], I want [action], so that [outcome])
- [ ] Acceptance criteria defined (Given/When/Then, at least 2 per story)
- [ ] Design assets complete and reviewed by engineering (wireframes, mockups, or prototypes)
- [ ] Dependencies identified and resolved (or resolution committed with date)
- [ ] Estimated at 8 story points or fewer (larger stories must be split)
- [ ] Technical approach discussed (team understands how to implement, not just what to implement)
- [ ] Test strategy identified (unit tests, integration tests, manual QA -- who does what)
- [ ] No open questions remaining (all ambiguity resolved before sprint start)

**Sprint Length Trade-Offs:**

| Sprint Length | Best For | Advantages | Disadvantages |
|---|---|---|---|
| **1 week** | Fast-moving startups, high-uncertainty projects, teams learning Scrum | Rapid feedback, low planning overhead, small batch size reduces risk | Very short; planning/retro overhead is proportionally high; hard to complete meaningful features |
| **2 weeks** | Most software teams, balanced pace | Industry standard; enough time for meaningful work; frequent feedback; manageable planning sessions | Can feel rushed for complex features; mid-sprint interruptions are harder to absorb |
| **3 weeks** | Teams with heavy QA cycles, regulated industries | More time for testing and documentation; fewer ceremonies per month | Unusual cadence; harder to synchronize with monthly business rhythms |
| **4 weeks** | Large enterprise teams, hardware/firmware, complex integrations | Enough time for large features; fewer planning sessions | Delayed feedback; higher risk of scope creep within sprint; harder to estimate accurately |

**Recommendation:** Start with 2-week sprints. Shorten to 1 week only if the team has mature CI/CD and can ship increments frequently. Lengthen to 3-4 weeks only if the work genuinely requires it (hardware dependencies, regulatory review cycles).

**Kanban Alternative: Flow-Based Execution**

If the team uses Kanban instead of sprints, there is no sprint planning ceremony. Instead, the team manages flow continuously.

**WIP Limits -- How to Set Them:**

WIP (Work in Progress) limits cap the number of items allowed in each column of the board. They prevent overload, expose bottlenecks, and force the team to finish work before starting new work.

Starting point formula:
```
WIP Limit per column = Number of people who work in that column + 1

Example:
  3 developers work in the "In Progress" column
  WIP Limit for "In Progress" = 3 + 1 = 4

  2 QA engineers work in the "In Review" column
  WIP Limit for "In Review" = 2 + 1 = 3
```

Adjust over time. If the column is always at the limit and items are queuing, increase by 1. If items flow through too quickly and quality suffers, decrease by 1. The goal is smooth flow, not maximum throughput.

**Pull System:** Team members pull work from the next column to the left when they have capacity. No one assigns work to others. The board is the single source of truth.

**Cycle Time Targets:** Measure how long items take from "In Progress" to "Done." Track the 50th and 85th percentile. Use the 85th percentile as the team's service level expectation: "85% of items complete within X days."

**Classes of Service:**

| Class | Description | WIP Allocation | Example |
|---|---|---|---|
| **Expedite** | Production emergency, security vulnerability | 1 item max, bypasses WIP limits | Critical bug in production affecting revenue |
| **Fixed Date** | External deadline, regulatory, contractual | Reserve capacity; track separately | Feature needed for conference demo on March 15 |
| **Standard** | Normal priority work | Bulk of WIP budget | Feature development, tech debt, improvements |
| **Intangible** | Long-term investment, no immediate urgency | 10-20% of capacity | Infrastructure upgrades, developer tooling, documentation |

### General Mode: Phase / Iteration Planning

For non-software teams, the equivalent of sprint planning is phase or iteration planning -- deciding what will be delivered in the next period (week, two weeks, or month) and confirming the team has the resources and clarity to execute.

**Phase Planning Template:**

```
ITERATION PLAN
================
Period: [Start date] to [End date]
Team: _______________
Plan Owner: _______________

DELIVERABLES THIS PERIOD:
| # | Deliverable | Owner | Due Date | Dependencies | Status |
|---|-------------|-------|----------|--------------|--------|
| 1 |             |       |          |              |        |
| 2 |             |       |          |              |        |
| 3 |             |       |          |              |        |

RESOURCE ASSIGNMENTS:
| Team Member | Allocation (%) | Primary Deliverable | Secondary |
|-------------|----------------|--------------------:|-----------|
|             |                |                     |           |

DEPENDENCY CHECK:
| Dependency | Owner | Status | Needed By | Risk if Late |
|------------|-------|--------|-----------|--------------|
|            |       |        |           |              |

RISK REVIEW:
| Risk | Probability | Impact | Mitigation | Owner |
|------|-------------|--------|------------|-------|
|      |             |        |            |       |

DECISIONS NEEDED THIS PERIOD:
| Decision | Needed By | Decision Maker | Impact if Delayed |
|----------|-----------|----------------|-------------------|
|          |           |                |                   |
```

**Weekly Planning Rhythm:**

- **Monday:** 30-minute planning session. Review the week's priorities, confirm assignments, identify blockers.
- **Wednesday:** 15-minute mid-week check-in. Are we on track? Any course corrections?
- **Friday:** 15-minute close-out. What shipped? What carries over? Quick retrospective note.

**Workstream Coordination Meeting Format (for multi-workstream programs):**

```
WORKSTREAM COORDINATION
=========================
Program: _______________
Date: _______________
Facilitator: Program Manager
Duration: 45 minutes

ROLL CALL BY WORKSTREAM (5 min):
  Each workstream lead — 1 sentence status (Green / Amber / Red + one-liner)

CROSS-WORKSTREAM DEPENDENCIES (15 min):
  Review dependency board. Which dependencies are at risk?
  Which handoffs are coming in the next 2 weeks?

ESCALATIONS (10 min):
  Issues that cannot be resolved within a single workstream.
  Decisions that need program-level authority.

UPCOMING MILESTONES (10 min):
  Next 4 weeks: Which milestones are approaching?
  Readiness check: Is everything in place to hit them?

ACTION ITEMS (5 min):
  - [Action] — Owner: ___ — Due: ___
  - [Action] — Owner: ___ — Due: ___
```

### Velocity Tracking

**How to Calculate Velocity:**

Velocity is the number of story points the team completes per sprint. Count only stories that are 100% done (meet the Definition of Done). Partially complete stories count as zero.

```
Sprint Velocity = Sum of story points for all stories completed in the sprint

Rolling Average (recommended):
  Use the average of the last 3-4 sprints for forecasting.

  Example:
    Sprint 12: 38 points
    Sprint 13: 42 points
    Sprint 14: 35 points
    Sprint 15: 41 points

    Rolling average = (38 + 42 + 35 + 41) / 4 = 39 points/sprint
```

**How to Use Velocity for Forecasting:**

If the backlog has 200 story points remaining and the team's rolling average velocity is 39 points per sprint (2-week sprints), then:

```
Estimated sprints remaining = 200 / 39 = ~5.1 sprints
Estimated completion = ~10-11 weeks from now (5.1 x 2 weeks)

Add buffer: Multiply by 1.2-1.5 for uncertainty.
  Optimistic: 10 weeks
  Likely: 12 weeks (1.2x)
  Conservative: 15 weeks (1.5x)
```

**When Velocity Is Unreliable:**

- First 3 sprints of a new team (velocity has not stabilized)
- After team composition changes (someone joins or leaves)
- When the nature of work changes significantly (e.g., shifting from feature development to infrastructure)
- When the team re-calibrates story point scale
- When comparing velocity across different teams (story points are team-specific, not universal)

### Milestone Tracking and Earned Value (General Mode)

For non-software projects, track progress against milestones using earned value concepts.

**Simplified Earned Value:**

| Metric | Formula | What It Tells You |
|---|---|---|
| Planned Value (PV) | Budgeted cost of work scheduled to date | What you planned to have done by now |
| Earned Value (EV) | Budgeted cost of work actually completed | What you have actually accomplished |
| Actual Cost (AC) | Actual cost incurred to date | What you have actually spent |
| Schedule Variance (SV) | EV - PV | Negative = behind schedule |
| Cost Variance (CV) | EV - AC | Negative = over budget |
| Schedule Performance Index (SPI) | EV / PV | < 1.0 = behind schedule |
| Cost Performance Index (CPI) | EV / AC | < 1.0 = over budget |

**Worked Example:**

```
A project has a $500,000 budget over 20 weeks.
At week 10 (midpoint):
  Planned Value (PV): $250,000 (50% of work should be done)
  Earned Value (EV): $200,000 (40% of work is actually done)
  Actual Cost (AC): $230,000 (what has actually been spent)

  Schedule Variance = $200K - $250K = -$50K (behind schedule)
  Cost Variance = $200K - $230K = -$30K (over budget)
  SPI = $200K / $250K = 0.80 (20% behind schedule)
  CPI = $200K / $230K = 0.87 (13% over budget)

  Interpretation: The project is both behind schedule and over budget.
  At current rates, the project will cost ~$575K ($500K / 0.87)
  and take ~25 weeks (20 weeks / 0.80).
```

### Planning Anti-Patterns

1. **Overcommitting.** The team takes on more work than capacity allows, driven by optimism or pressure. Every sprint ends with carry-over. Fix: Use the rolling velocity average, not the best-ever sprint. Protect the team's right to say "that is too much."
2. **Sandbagging.** The team deliberately undercommits to guarantee they finish everything. Velocity is artificially low. Fix: Track velocity trends. If the team consistently finishes 2 days early and pulls no additional work, the estimate is too conservative. Challenge gently.
3. **Planning without the team.** A manager or PM plans the sprint and hands it to the team as a fait accompli. Fix: The team must be in the room for planning. They own the estimate and the commitment. The PM owns the priority; the team owns the capacity.
4. **No sprint goal.** Stories are a disconnected grab bag of work with no unifying theme. The team cannot explain what the sprint is about. Fix: Start every planning session with "What is the one thing we must achieve this sprint?" Derive the story list from the goal, not the other way around.
5. **Ignoring carry-over.** Incomplete stories from the last sprint are not discussed or re-estimated. They silently consume capacity. Fix: Start planning by reviewing carry-over items. Re-estimate if scope has changed. Account for them in capacity before pulling new work.

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
