---
name: execution
description: Standups, sprint planning, decision tracking, and change management for software and general PMs Use when user asks to "plan a sprint", "run standup", "track decisions", or mentions sprint planning, daily standup, change requests, or kanban.
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

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/execution-reference.md`](references/execution-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- Decision Management
- Change Management
- Output Templates Summary

