---
name: planning
description: WBS, scheduling, resource planning, risk management, and communication planning for software and general PMs Use when user asks to "create a WBS", "build a project schedule", "risk register", or mentions work breakdown structure, resource planning, RACI, or critical path.
triggers:
  - work breakdown structure
  - wbs
  - project schedule
  - gantt
  - sprint planning
  - resource plan
  - capacity planning
  - risk register
  - risk management
  - communication plan
  - raci
  - critical path
  - milestone
---

# Planning

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

Planning is the bridge between a charter and execution. A charter tells you why the project exists and what success looks like. Planning tells you how to get there -- what work needs to happen, in what order, with which people, against which risks, and communicated to whom. Skip planning and you get heroics, rework, and surprises. Over-plan and you get analysis paralysis, stale documents, and a team that confuses motion with progress.

This skill covers five planning disciplines: Work Breakdown Structure, Scheduling, Resource Planning, Risk Management, and Communication Planning. Each section provides both a **software mode** (Agile/Scrum-oriented, sprint-based, story-level) and a **general mode** (traditional/predictive, phase-based, activity-level). Use whichever fits your project context, or blend them for hybrid approaches.

---

## Work Breakdown Structure

A Work Breakdown Structure (WBS) is a hierarchical decomposition of the total scope of work the project team must execute. It is the foundation for scheduling, cost estimation, resource planning, and risk identification. If your WBS is wrong, everything downstream is wrong.

### WBS Principles

Three rules govern every well-formed WBS:

**The 100% Rule.** The WBS must capture 100% of the work defined by the project scope, including project management work itself. Every level of decomposition must collectively account for all the work of the parent element. Nothing is left out. Nothing is double-counted.

**Mutually Exclusive Elements.** No work package should overlap with another. If two work packages share the same task, you have a decomposition error. Ambiguous ownership leads to duplicated effort or gaps.

**Deliverable-Oriented Decomposition.** Each element in the WBS should describe a deliverable or outcome, not an action. "User authentication module" is a deliverable. "Write code" is an action. Actions belong in schedules; deliverables belong in the WBS.

### Software Mode: Epic-to-Task Decomposition

Software projects decompose scope through a four-level hierarchy:

```
Level 1: Epic           (large body of work, typically a quarter-level initiative)
  Level 2: Feature      (a user-facing capability within the epic)
    Level 3: Story      (a single unit of user value, completable in one sprint)
      Level 4: Task     (a technical step needed to implement the story)
```

**Story Point Estimation.** Stories are estimated in story points using a Fibonacci-like scale (1, 2, 3, 5, 8, 13). Points measure relative complexity, not hours. A 5-point story is roughly 2.5 times the effort of a 2-point story, but the team calibrates this through experience. Any story estimated at 13 or above should be split -- it is too large for a single sprint and too uncertain to estimate accurately.

**Acceptance Criteria Per Story.** Every story must have acceptance criteria before it enters a sprint. Acceptance criteria define the conditions under which the story is considered done. They are written in Given/When/Then format or as a simple checklist. Without acceptance criteria, "done" is a matter of opinion.

**Definition of Ready.** A story is ready for sprint planning when it meets all of these conditions:

- Acceptance criteria are written and reviewed by the team
- Dependencies are identified and either resolved or explicitly accepted
- The story is estimated (story points assigned)
- UX/design assets are available (if applicable)
- The story is small enough to complete in one sprint
- The team understands the story well enough to start work without further clarification

**Worked Example -- Software Mode:**

```
EPIC: User Authentication System
|
+-- FEATURE 1: Email/Password Login
|   +-- STORY 1.1: User can register with email and password (5 pts)
|   |   Acceptance criteria:
|   |   - Given a new user, when they submit a valid email and password,
|   |     then an account is created and a verification email is sent
|   |   - Given an existing email, when a user tries to register,
|   |     then they see an error "Account already exists"
|   |   Tasks:
|   |   - Create registration API endpoint
|   |   - Build registration form component
|   |   - Implement email verification service
|   |   - Write unit and integration tests
|   |
|   +-- STORY 1.2: User can log in with email and password (3 pts)
|   |   Acceptance criteria:
|   |   - Given valid credentials, when user submits login form,
|   |     then they receive a JWT and are redirected to dashboard
|   |   - Given invalid credentials, when user submits login form,
|   |     then they see a generic error (no credential enumeration)
|   |   Tasks:
|   |   - Create login API endpoint
|   |   - Build login form component
|   |   - Implement JWT token generation and validation
|   |   - Write unit and integration tests
|   |
|   +-- STORY 1.3: User can reset their password (5 pts)
|
+-- FEATURE 2: OAuth Social Login
|   +-- STORY 2.1: User can log in with Google (3 pts)
|   +-- STORY 2.2: User can log in with GitHub (3 pts)
|   +-- STORY 2.3: User can link/unlink social accounts (5 pts)
|
+-- FEATURE 3: Multi-Factor Authentication
    +-- STORY 3.1: User can enable TOTP-based MFA (8 pts)
    +-- STORY 3.2: User can use backup codes (5 pts)
    +-- STORY 3.3: Admin can enforce MFA for the organization (5 pts)
```

### General Mode: Phase-to-Activity Decomposition

Non-software projects (construction, events, organizational change, marketing campaigns) decompose scope through a four-level hierarchy:

```
Level 1: Phase          (a major stage of the project lifecycle)
  Level 2: Deliverable  (a tangible output produced in that phase)
    Level 3: Work Package (a grouping of related activities that produce part of the deliverable)
      Level 4: Activity  (a single task with an estimated duration and resource assignment)
```

**Hours-Based Estimation.** Activities are estimated in hours or days. Use three-point estimation (optimistic, most likely, pessimistic) for activities with high uncertainty. For routine activities, use analogous estimation based on past projects.

**Worked Example -- General Mode:**

```
PHASE 1: Office Relocation -- Planning
|
+-- DELIVERABLE 1.1: Site Selection Report
|   +-- WP 1.1.1: Requirements Gathering
|   |   - Activity: Interview department heads (16 hrs)
|   |   - Activity: Document space requirements per team (8 hrs)
|   |   - Activity: Define infrastructure requirements (8 hrs)
|   +-- WP 1.1.2: Site Evaluation
|   |   - Activity: Tour candidate sites (24 hrs)
|   |   - Activity: Score sites against criteria matrix (8 hrs)
|   |   - Activity: Negotiate preliminary lease terms (16 hrs)
|   +-- WP 1.1.3: Final Report
|       - Activity: Compile evaluation report (8 hrs)
|       - Activity: Present to steering committee (4 hrs)
|
+-- DELIVERABLE 1.2: Budget Approval Package
    +-- WP 1.2.1: Cost Estimation
    |   - Activity: Get contractor bids for build-out (40 hrs)
    |   - Activity: Estimate moving costs (8 hrs)
    |   - Activity: Calculate technology upgrade costs (16 hrs)
    +-- WP 1.2.2: Budget Presentation
        - Activity: Build budget model with contingency (8 hrs)
        - Activity: Present to finance committee (4 hrs)
```

### WBS Dictionary Template

Every work package in the WBS should have a corresponding dictionary entry. The dictionary provides the detail that the hierarchical chart cannot.

```
WBS DICTIONARY ENTRY
=====================
WBS ID:              _______________
Name:                _______________
Description:         _______________________________________________
                     _______________________________________________
Parent element:      _______________
Owner:               _______________
Effort estimate:     ___________ (hours or story points)
Duration estimate:   ___________ (calendar days)
Dependencies:        _______________________________________________
Predecessors:        _______________________________________________
Successors:          _______________________________________________
Acceptance criteria: _______________________________________________
                     _______________________________________________
Assumptions:         _______________________________________________
Constraints:         _______________________________________________
Risks:               _______________________________________________
Cost estimate:       _______________
Notes:               _______________________________________________
```

### Decomposition Rules of Thumb

| Guideline | Software Mode | General Mode |
|-----------|--------------|--------------|
| Stop decomposing when... | A story fits in one sprint | An activity is 8-80 hours |
| Too granular if... | You are writing tasks for tasks | An activity is under 4 hours |
| Too coarse if... | A story cannot be estimated with confidence | An activity spans more than 2 weeks |
| Number of children per parent | 3-7 is ideal | 3-9 is ideal |
| Who decomposes | The team that will do the work | The team that will do the work |

The 8-80 rule for general mode means no activity should be estimated at fewer than 8 hours (too granular to manage) or more than 80 hours (too coarse to track meaningfully). For software mode, the equivalent is the one-sprint rule: if a story cannot be completed in a single sprint, it needs to be split.

---

## Scheduling

Scheduling transforms the WBS into a time-sequenced plan. It answers: what happens when, in what order, and how long will the project take?

### Software Mode: Sprint-Based Scheduling

#### Sprint Length Selection

The sprint length determines your feedback cadence. Shorter sprints mean faster feedback but higher ceremony overhead. Longer sprints give more focus time but delay course corrections.

| Sprint Length | Best For | Trade-offs |
|--------------|----------|------------|
| **1 week** | High-uncertainty projects, brand-new teams, rapidly changing requirements, prototyping phases | Very fast feedback. High ceremony overhead (planning, review, retro every week). Stories must be very small. Limited time for deep work. |
| **2 weeks** | Most software teams. Default recommendation when unsure. | Good balance of feedback speed and focus time. Enough room for 3-8 point stories. Industry standard. |
| **3 weeks** | Teams with heavy external dependencies, hardware/software integration, teams spanning multiple time zones | More room for integration work. Retros feel less frequent, which can slow improvement. Uncommon -- can feel like an awkward middle ground. |
| **4 weeks** | Regulated environments, teams with long QA cycles, projects with heavy documentation requirements | Maximum focus time. Delayed feedback increases risk of building the wrong thing. Feels close to mini-waterfall if the team is not disciplined. |

**Recommendation:** Start with 2-week sprints. Adjust only after 4-6 sprints when you have data on what works for your team.

#### Velocity Estimation for New Teams

New teams have no historical velocity. Do not guess. Instead:

1. **Sprint 0 approach.** Run a short spike sprint where the team works on a representative mix of stories. Measure how many points the team completes. Use 60-80% of that number as your initial velocity estimate.
2. **Heuristic method.** Count the number of developers on the team. Assume each developer can complete roughly 5-8 story points per 2-week sprint (this varies enormously, but it gives a starting point). Multiply by the number of developers. Reduce by 20% for a new team learning to work together.
3. **Yesterday's weather.** After 3 sprints, use the average of the last 3 sprints as your velocity. After 6 sprints, use the average of the last 6. This is the most reliable method and should replace heuristics as soon as possible.

| Method | When to Use | Accuracy |
|--------|------------|----------|
| Sprint 0 spike | Before first real sprint | Low-Medium |
| Heuristic (devs x 5-8 pts) | Day one, no data | Low |
| 3-sprint average | After sprint 3 | Medium |
| 6-sprint average | After sprint 6 | Medium-High |

#### Sprint Goal Setting

Every sprint needs a goal -- a single sentence describing what the team commits to achieving. The sprint goal is not a list of stories. It is the outcome those stories collectively produce.

**Good sprint goals:**
- "Users can complete the checkout flow end-to-end using a credit card."
- "The API response time for the search endpoint is under 200ms at p95."
- "The admin dashboard displays real-time metrics for all active campaigns."

**Bad sprint goals:**
- "Complete stories 101, 102, 103, 104, 105." (This is a task list, not a goal.)
- "Make progress on the authentication epic." (Too vague to know if you achieved it.)
- "Fix bugs." (Not outcome-oriented.)

#### Sprint Planning Meeting Structure

Sprint planning is the ceremony where the team commits to a sprint goal and selects stories from the backlog. A poorly run sprint planning meeting wastes hours and produces vague commitments. A well-run one takes 1-2 hours (for a 2-week sprint) and leaves the team with clear work and a shared understanding of the goal.

```
SPRINT PLANNING AGENDA
=======================
Sprint: ___    Date: YYYY-MM-DD    Duration: 2 hours max

PART 1: WHAT (45 min)
  1. Product owner presents the proposed sprint goal             (10 min)
  2. Product owner walks through top-priority backlog items      (20 min)
     - For each item: context, acceptance criteria, open questions
  3. Team asks clarifying questions                              (15 min)
     - If a story cannot be understood, it goes back to refinement

PART 2: HOW (60 min)
  4. Team selects stories that fit the sprint goal and capacity  (15 min)
     - Use yesterday's weather (average velocity) as the guide
     - Do not exceed capacity — leave 10-15% buffer
  5. Team breaks stories into tasks (optional for mature teams)  (30 min)
     - Identify technical approach for each story
     - Flag stories that need spikes or have unknowns
  6. Team confirms sprint goal and commitment                    (10 min)
     - Read the sprint goal aloud
     - Each team member verbally confirms they understand and commit

PART 3: WRAP-UP (15 min)
  7. Identify risks or dependencies for this sprint              (10 min)
  8. Update the sprint board                                     (5 min)

OUTPUT:
  - Sprint goal (one sentence)
  - Selected stories with point total
  - Identified risks and dependencies
  - Sprint board updated and visible to all
```

#### Release Planning

Release planning maps sprints to releases. A release is a deployable increment that you choose to ship to users.

```
RELEASE PLAN
=============
Product: _______________
Release cadence: _______________
Velocity assumption: ___________ pts/sprint

Release 1.0 — Target: Sprint 4 (YYYY-MM-DD)
  Sprint 1: [sprint goal] — [total pts planned]
  Sprint 2: [sprint goal] — [total pts planned]
  Sprint 3: [sprint goal] — [total pts planned]
  Sprint 4: [sprint goal + stabilization] — [total pts planned]
  Total scope: ___ pts | Buffer: ___ pts (10-20% of total)

Release 1.1 — Target: Sprint 8 (YYYY-MM-DD)
  Sprint 5: [sprint goal] — [total pts planned]
  Sprint 6: [sprint goal] — [total pts planned]
  Sprint 7: [sprint goal] — [total pts planned]
  Sprint 8: [sprint goal + stabilization] — [total pts planned]
  Total scope: ___ pts | Buffer: ___ pts
```

**Key rule:** Never plan a release at 100% of theoretical capacity. Reserve 10-20% for bugs, technical debt, and scope changes discovered mid-release.

#### Story Mapping for Sequencing

Story mapping arranges stories in two dimensions: left-to-right by user workflow sequence, top-to-bottom by priority. The top row forms the "walking skeleton" -- the minimum set of stories that delivers an end-to-end user flow.

```
USER WORKFLOW (left to right):
  Sign Up  →  Browse  →  Search  →  Add to Cart  →  Checkout  →  Confirm

PRIORITY (top to bottom):
  Row 1 (MVP):        Basic    List     Keyword    Add item    Credit     Email
                       reg.    view     search     to cart     card       receipt

  Row 2 (Release 2):  OAuth    Filter   Advanced   Save for    PayPal    Order
                       login   by cat.  filters    later                  tracking

  Row 3 (Release 3):  SSO      Recs     AI search  Wishlist   Apple Pay  Returns
```

Use story mapping to define release boundaries. Draw a horizontal line across the map -- everything above the line is in the release, everything below is deferred.

**Story mapping workshop process:**

1. **Identify the user's journey** from start to finish. Write each major step on a card and arrange them left to right. These become the "backbone" of the map.
2. **Decompose each step** into the specific stories needed to implement it. Place these vertically below the backbone step, ordered by priority (most critical at top).
3. **Draw the walking skeleton line** under the minimum set of stories that delivers a usable end-to-end flow. This is your MVP or Release 1.
4. **Draw additional release lines** below. Each horizontal slice is a release that adds depth to the experience.
5. **Validate with stakeholders.** Walk them through the backbone first (do they agree on the user journey?), then the release slices (do they agree on priorities?).

Story mapping is particularly useful when a project has many stories and the team is struggling to decide what to build first. It forces a conversation about user value rather than technical convenience.

### General Mode: Critical Path Method

#### Forward and Backward Pass

The Critical Path Method (CPM) calculates the earliest and latest start/finish times for every activity. The difference between latest and earliest is the **float** (also called slack). Activities with zero float are on the **critical path** -- any delay to these activities delays the entire project.

**Forward Pass (calculates Early Start and Early Finish):**
- Start at the first activity. ES = 0 (or project start date).
- EF = ES + Duration.
- For each subsequent activity, ES = maximum EF of all predecessors.
- Continue until you reach the last activity. Its EF is the project duration.

**Backward Pass (calculates Late Finish and Late Start):**
- Start at the last activity. LF = project duration (or EF from forward pass).
- LS = LF - Duration.
- For each preceding activity, LF = minimum LS of all successors.
- Continue until you reach the first activity.

**Float Calculation:**
- Float = LS - ES (or equivalently, LF - EF).
- Activities where Float = 0 are on the critical path.

**Worked Example:**

```
Activity  Duration  Predecessors  ES   EF   LS   LF   Float  Critical?
--------  --------  ------------  ---  ---  ---  ---  -----  ---------
A         3         --            0    3    0    3    0      YES
B         5         A             3    8    4    9    1      no
C         6         A             3    9    3    9    0      YES
D         2         B             8    10   9    11   1      no
E         4         C             9    13   9    13   0      YES
F         3         D, E          13   16   13   16   0      YES

Project duration: 16 days
Critical path: A → C → E → F
```

In this example, activities B and D have 1 day of float each. They can slip by 1 day without delaying the project. Activities A, C, E, and F have zero float -- any delay to these activities pushes out the project end date.

#### PERT Estimates

When activity durations are uncertain, use PERT (Program Evaluation and Review Technique) three-point estimation:

**Formula:**

```
Expected Duration = (Optimistic + 4 * Most Likely + Pessimistic) / 6
Standard Deviation = (Pessimistic - Optimistic) / 6
```

**Worked Example:**

| Activity | Optimistic (O) | Most Likely (M) | Pessimistic (P) | Expected | Std Dev |
|----------|---------------|-----------------|-----------------|----------|---------|
| Requirements gathering | 5 days | 8 days | 17 days | 9.0 days | 2.0 |
| Design | 10 days | 15 days | 26 days | 16.0 days | 2.67 |
| Development | 20 days | 30 days | 46 days | 31.0 days | 4.33 |
| Testing | 8 days | 12 days | 22 days | 13.0 days | 2.33 |

To calculate the probability of completing the project by a target date, sum the expected durations for the critical path and use the combined standard deviation (square root of the sum of variances).

#### Gantt Chart Structure

A Gantt chart is a bar chart that maps activities against time. It is the most common way to communicate a project schedule.

```
GANTT CHART — [Project Name]
Start: YYYY-MM-DD | End: YYYY-MM-DD

Activity              Owner       Week1  Week2  Week3  Week4  Week5  Week6
--------------------  ----------  -----  -----  -----  -----  -----  -----
Requirements          PM          =====  ==
Design                UX Lead            ====   =====
Development (Phase 1) Dev Lead                  ===    =====  ==
Development (Phase 2) Dev Lead                                ====   ==
Testing               QA Lead                          ==     =====  ===
Deployment            DevOps                                         ===
Documentation         Tech Writer               ===    ===    ===    ==

LEGEND: ===== Active work period    ---- Float/buffer    * Milestone
```

#### Milestone Definition

Milestones are zero-duration events that mark significant points in the schedule. They are decision points, phase transitions, or external commitments.

**Good milestones:**
- Requirements approved by sponsor
- Architecture review complete
- Feature freeze
- UAT sign-off
- Go-live

**Bad milestones:**
- "Halfway done" (not a verifiable event)
- "Development in progress" (this is an activity, not a milestone)

#### Phase Gate Criteria

Phase gates are formal checkpoints where the project must meet defined criteria before proceeding. They prevent throwing resources at a project that should be killed, pivoted, or paused.

| Gate | Name | Key Criteria |
|------|------|-------------|
| G0 | Concept | Business case approved, rough order-of-magnitude estimate within budget tolerance, sponsor identified |
| G1 | Planning Complete | WBS complete and baselined, schedule approved, resources committed, risks assessed, communication plan in place |
| G2 | Design Complete | Design reviewed and approved, technical architecture validated, key risks mitigated or accepted |
| G3 | Build Complete | All deliverables produced, unit testing passed, integration testing passed, defect count within threshold |
| G4 | Acceptance | UAT passed, training completed, operational readiness confirmed, deployment plan approved |
| G5 | Close | Lessons learned captured, resources released, final financials reconciled, sponsor sign-off received |

### Dependency Types

Dependencies define the sequencing logic between activities. There are four types:

| Type | Name | Meaning | Example |
|------|------|---------|---------|
| FS | Finish-to-Start | B cannot start until A finishes | Testing cannot start until development finishes |
| SS | Start-to-Start | B cannot start until A starts | Documentation can start when development starts (but not before) |
| FF | Finish-to-Finish | B cannot finish until A finishes | Testing cannot finish until all defect fixes finish |
| SF | Start-to-Finish | B cannot finish until A starts | The night shift cannot finish until the day shift starts (rare, usually scheduling/coverage) |

**FS is the default and most common.** SS and FF are useful for overlapping activities. SF is rare -- if you think you need it, double-check your logic.

**Leads and Lags:**
- A **lead** accelerates the successor. FS - 2 days means B can start 2 days before A finishes.
- A **lag** delays the successor. FS + 3 days means B starts 3 days after A finishes (e.g., waiting for concrete to cure).

### Schedule Compression

When the calculated end date is later than the required deadline, you have two options:

| Technique | How It Works | Trade-offs |
|-----------|-------------|------------|
| **Crashing** | Add resources to critical path activities to shorten their duration | Increases cost. Only works if the activity is resource-constrained (not all are). Adding people to a late project often makes it later (Brooks's Law). Diminishing returns -- doubling the team does not halve the duration. |
| **Fast-tracking** | Overlap activities that were planned sequentially | Increases risk. Activities done in parallel may need rework if the predecessor output changes. Only works for activities that have a discretionary (soft) dependency, not a mandatory (hard) dependency. |

**Decision framework:**

1. Identify the critical path.
2. For each critical path activity, ask: Can we shorten it with more resources (crash)? Can we overlap it with its successor (fast-track)?
3. Crash first if budget is available and the activity is resource-constrained.
4. Fast-track if the risk of rework is acceptable and the dependency is discretionary.
5. Never crash and fast-track simultaneously on the same activity pair -- the combined risk is usually unacceptable.

### Buffer Management

Buffers protect the schedule from uncertainty without inflating individual activity estimates.

**Project Buffer.** Placed at the end of the critical path. Sized at 25-50% of the critical path duration. Consumed as critical path activities run late. Monitor the rate of consumption -- if you are burning buffer faster than completing work, the project is trending late.

**Feeding Buffers.** Placed where non-critical paths feed into the critical path. Sized at 25-50% of the feeding path duration. Protect the critical path from delays on non-critical paths.

**Resource Buffers.** Not time buffers -- they are early warnings. Placed before critical path activities that require a specific resource. The warning tells the resource: "You will be needed on this activity in X days. Be ready."

```
BUFFER PLACEMENT EXAMPLE

Non-critical path:  [Activity B] [Activity D] [FEEDING BUFFER] ──┐
                                                                  ↓
Critical path:      [Activity A] [Activity C] [Activity E] [Activity F] [PROJECT BUFFER] → End
```

---

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/planning-reference.md`](references/planning-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- Resource Planning
- Risk Management
- Communication Planning
- Putting It All Together

