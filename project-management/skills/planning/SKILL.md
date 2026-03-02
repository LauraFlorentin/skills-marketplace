---
name: planning
description: WBS, scheduling, resource planning, risk management, and communication planning for software and general PMs
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

## Resource Planning

Resource planning assigns people (and sometimes equipment and materials) to the work defined in the WBS and scheduled on the timeline. The goal is to ensure the right people are available at the right time with the right skills, without burning them out.

### Resource Allocation Matrix

The resource allocation matrix shows who is working on what and at what percentage of their time, week by week.

```
RESOURCE ALLOCATION MATRIX
===========================
Project: _______________
Period:  Week of YYYY-MM-DD to YYYY-MM-DD

                    Week 1   Week 2   Week 3   Week 4   Week 5   Week 6
                    ------   ------   ------   ------   ------   ------
Alice (Backend)      80%      80%      100%     100%     50%      --
Bob (Frontend)       --       50%      80%      80%      80%      50%
Carol (QA)           --       --       20%      50%      80%      100%
Dave (DevOps)        20%      20%      20%      20%      50%      80%
Eve (UX)             80%      50%      20%      --       --       --
Frank (PM)           30%      30%      30%      30%      30%      30%

NOTES:
- Alice split with Platform team (20%) in Weeks 1-2
- Bob joining after Sprint 0 wraps on other project
- Carol ramping up as testable increments become available
- Frank at 30% — also managing Project Y
```

**Rules for the matrix:**
- No one should be allocated above 80% to a single project (leave room for meetings, overhead, and unexpected work).
- If someone is split across more than 2 projects, flag it as a risk. Context switching destroys productivity.
- Update weekly. Stale allocation matrices are worse than no matrix because they create false confidence.

### Software Mode: Team Topology Considerations

Team structure shapes the work, not the other way around (Conway's Law). When planning resources for software projects, consider four team types:

| Team Type | Purpose | Staffing Pattern |
|-----------|---------|-----------------|
| **Stream-aligned** | Delivers a continuous flow of value for a specific business domain or user segment | 5-9 people. Cross-functional (dev, QA, UX, product). Owns their domain end-to-end. This is your default team type. |
| **Platform** | Provides internal services that stream-aligned teams consume (CI/CD, infrastructure, auth services) | 3-7 people. Treats stream-aligned teams as customers. Reduces cognitive load on stream-aligned teams. |
| **Enabling** | Helps stream-aligned teams adopt new capabilities (new language, new framework, observability practices) | 2-4 people. Temporary engagements with stream-aligned teams. Goal is to transfer knowledge, not to do the work for them. |
| **Complicated-subsystem** | Owns a component that requires deep specialist knowledge (ML model, real-time engine, cryptography module) | 2-6 specialists. Provides a simple API surface to other teams. Justified only when the subsystem is genuinely complex and cannot be learned by a generalist team in a reasonable time. |

**T-Shaped Skills.** Within a stream-aligned team, aim for T-shaped engineers: deep expertise in one area (the vertical bar of the T) with working knowledge of adjacent areas (the horizontal bar). T-shaped teams are resilient -- if one person is sick or on vacation, others can cover.

**Pairing and Mobbing Strategies:**

| Practice | When to Use | Resource Impact |
|----------|------------|-----------------|
| **Solo work** | Well-understood tasks, low-risk changes, documentation | 1x cost. Best for throughput on routine work. |
| **Pair programming** | Complex logic, onboarding new team members, critical path items, cross-pollinating knowledge | 2x cost, ~1.5x quality. Reduces defects and bus factor. |
| **Mob/ensemble programming** | Architecture decisions, spike investigations, team-wide learning, extremely complex problems | Nx cost, highest shared understanding. Use sparingly -- 2-4 hours max per session. |

**On-Call Rotation Planning.** If your team operates a production service, plan on-call into your capacity model. On-call engineers are available for sprint work but at reduced capacity (typically 50-70% of normal). Rotate weekly. Never put the same person on-call for consecutive weeks.

### General Mode: Resource Leveling and Smoothing

**Resource Leveling.** Adjusts the schedule to resolve resource over-allocation. If a person is assigned to two full-time activities in the same week, one activity must be delayed. Resource leveling often extends the project duration.

**Resource Smoothing.** Adjusts work within available float to reduce peaks and valleys in resource demand without extending the project duration. Smoothing is less disruptive than leveling because it only rearranges work that has slack.

**Skills Gap Analysis:**

```
SKILLS GAP ANALYSIS
====================
Project: _______________

Required Skill       Level Needed   Available Staff     Gap    Mitigation Plan
-------------------  ------------   ----------------    ----   -------------------------
Data engineering     Expert         2 mid-level         HIGH   Hire contractor for 3 months
Cloud architecture   Expert         1 expert            NONE   --
Change management    Intermediate   0                   HIGH   Train internal PM + coach
Regulatory filings   Expert         1 expert (part-time) MED   Extend expert to 80% allocation
Financial modeling   Intermediate   2 intermediate      NONE   --
```

**Contractor vs. Full-Time Decision Framework:**

| Factor | Favors Contractor | Favors Full-Time |
|--------|------------------|-----------------|
| Duration of need | Less than 6 months | More than 6 months |
| Skill rarity | Highly specialized, not a recurring need | Core competency the team needs permanently |
| Ramp-up time | Low (well-documented domain) | High (deep institutional knowledge needed) |
| IP sensitivity | Low (non-core functionality) | High (competitive advantage) |
| Cost | Higher hourly rate but no benefits/overhead | Lower total cost over 12+ months |
| Availability | Immediate (if you can find one) | 4-12 weeks to hire |

### Capacity Planning Formula

Capacity planning starts with a simple formula, then adjusts for reality.

```
CAPACITY CALCULATION PER PERSON PER SPRINT (2-week sprint = 10 working days)

Gross hours available:          10 days x 8 hrs           = 80 hrs
  - Company holidays/PTO:      avg 0.5 days per sprint   = -4 hrs
  - Recurring meetings:        avg 1.5 hrs/day x 10 days = -15 hrs
  - Sprint ceremonies:         planning + review + retro  = -6 hrs
  - Email/Slack/admin:         avg 1 hr/day x 10 days    = -10 hrs
  - On-call (if applicable):   -20% of remaining         = varies
                                                          --------
Net productive hours:           approximately 45 hrs      = ~5.6 hrs/day

Productive hours as % of gross: 45/80                     = 56%
```

This means a team of 6 developers has roughly 270 productive hours per 2-week sprint, not 480. Planning at 480 hours guarantees missed commitments.

**For general mode**, replace sprint ceremonies with project meeting overhead and use a similar formula:

```
CAPACITY PER PERSON PER MONTH (22 working days)

Gross hours:        22 x 8                  = 176 hrs
  - PTO/holidays:   avg 2 days              = -16 hrs
  - Meetings:       avg 2 hrs/day x 22      = -44 hrs
  - Admin overhead: avg 0.5 hrs/day x 22    = -11 hrs
                                              --------
Net productive hours:                        = 105 hrs  (60% utilization)
```

### Common Pitfalls

**The 100% Allocation Myth.** No one is 100% productive for 8 hours a day. Managers who plan at 100% utilization will consistently under-deliver. Plan at 60-70% utilization and treat the remainder as buffer for meetings, overhead, and the unexpected.

**Context Switching Cost.** Every time a person switches between projects, they lose 15-25 minutes of productive time to task-switching overhead. A person split across 3 projects does not deliver 33% to each -- they deliver roughly 20% to each due to switching costs. The following table illustrates:

| Number of Projects | Productive Time Per Project | Total Productive Time | Lost to Switching |
|-------------------|---------------------------|----------------------|-------------------|
| 1 | 100% | 100% | 0% |
| 2 | 40% | 80% | 20% |
| 3 | 20% | 60% | 40% |
| 4 | 10% | 40% | 60% |
| 5 | 5% | 25% | 75% |

**Not Accounting for Leave.** Over a 12-month project, assume each team member will take 15-20 days of PTO plus 5-10 company holidays. That is roughly 1 month of lost capacity per person per year. Plan for it upfront, not as a surprise when someone submits a vacation request mid-sprint.

---

## Risk Management

Risk management is the discipline of identifying what could go wrong, assessing how likely and damaging each risk is, and planning responses before the risk materializes. Reactive risk management (also known as "firefighting") is more expensive, more stressful, and less effective than proactive risk management.

### Risk Identification Techniques

Use multiple techniques. No single method catches all risks.

**Brainstorming.** Gather the team and ask: "What could go wrong?" Time-box to 30 minutes. Capture everything without judgment. Categorize and assess later. Works best with a diverse group -- include developers, testers, designers, and stakeholders. The facilitator should prompt with categories (technical, schedule, resource, external) to avoid blind spots.

**SWOT Analysis.** Map Strengths, Weaknesses, Opportunities, and Threats for the project. Threats are external risks; Weaknesses are internal risks. This is useful at project kickoff to establish the risk landscape at a high level.

**Pre-mortem.** Imagine the project has failed spectacularly. Ask: "What went wrong?" This reverses the usual optimism bias and surfaces risks that teams are reluctant to raise in a standard brainstorming session. Especially effective for projects with strong executive sponsorship where the team may feel pressure to appear confident.

**Checklist Review.** Use a risk checklist from past projects or industry standards. Walk through each category and ask: "Does this apply to our project?" Checklists catch the common, predictable risks. They miss novel risks, so always combine with other techniques.

**Assumption Analysis.** List every assumption the project is making (technology will work as expected, vendor will deliver on time, regulatory approval will be granted, key staff will remain available). For each assumption, ask: "What if this assumption is wrong?" Every false assumption is a risk.

### Risk Register Template

The risk register is the single source of truth for all identified risks. It is a living document updated at every risk review.

```
RISK REGISTER
==============
Project: _______________
Last updated: YYYY-MM-DD
Owner: _______________

ID   Description                   Category    P   I   Score  Response     Owner    Status    Trigger
                                               1-5 1-5 (PxI)  Strategy
---  ----------------------------  ----------  --  --  -----  ----------   -------  --------  ------------------
R01  Key architect leaves          Resource    3   5   15     Mitigate     PM       Open      Resignation notice
R02  API vendor changes terms      External    2   4   8      Transfer     Lead     Open      Vendor comm.
R03  Scope creep from marketing    Scope       4   3   12     Mitigate     PM       Open      Change requests
R04  Performance under load        Technical   3   4   12     Mitigate     Arch.    Open      Load test results
R05  Regulatory delay              External    2   5   10     Accept       PM       Open      Filing feedback
R06  Integration test env unavail. Technical   3   3   9      Avoid        DevOps   Open      Env request denied
R07  Budget overrun >10%           Budget      2   4   8      Mitigate     PM       Open      Monthly actuals
R08  Holiday season staffing       Resource    4   2   8      Accept       PM       Open      Calendar review
```

**Scoring guide:**

| Score | Probability | Impact |
|-------|------------|--------|
| 1 | Rare (<10%) | Negligible -- minor inconvenience, absorbed without schedule/cost impact |
| 2 | Unlikely (10-30%) | Minor -- less than 1 week schedule impact or <5% cost overrun |
| 3 | Possible (30-50%) | Moderate -- 1-3 weeks schedule impact or 5-10% cost overrun |
| 4 | Likely (50-70%) | Major -- 3+ weeks schedule impact or 10-20% cost overrun |
| 5 | Almost certain (>70%) | Severe -- project failure, regulatory violation, or >20% cost overrun |

### Software Mode: Technical Risks

Software projects have a distinct set of risk categories. Here are common risks with examples:

**Architecture Risks:**
- Chosen technology does not scale to projected user load
- Microservices architecture introduces unmanageable operational complexity
- Database schema cannot accommodate a newly discovered requirement without major refactoring

**Dependency Risks:**
- A third-party library has a critical vulnerability with no patch available
- An upstream API changes its contract without backward compatibility
- An open-source project the system depends on is abandoned

**Performance Risks:**
- Response times degrade under concurrent load beyond initial estimates
- Batch processing jobs exceed the available maintenance window
- Memory leaks cause service degradation over time

**Security Risks:**
- Authentication mechanism has a bypass vulnerability
- Sensitive data is logged in plaintext
- RBAC model does not enforce least privilege

**Technical Debt Risks:**
- Accumulated shortcuts make new feature development 2-3x slower than estimated
- Test coverage is too low to refactor safely
- Undocumented systems create single points of knowledge failure

**Deployment Risks:**
- Zero-downtime deployment is not tested, and the first attempt is production
- Rollback procedure is untested or takes longer than the maintenance window
- Configuration drift between environments causes "works on my machine" failures

### General Mode: Common Risk Categories

Non-software projects face a different but equally predictable set of risks:

**Scope Risks:**
- Stakeholders add requirements after baseline is set
- Deliverable acceptance criteria are ambiguous, leading to disputes at handoff
- Regulatory requirements change during execution

**Schedule Risks:**
- Critical path activities take longer than estimated
- External dependencies (permits, approvals, vendor deliveries) are delayed
- Weather or site conditions delay physical work

**Budget Risks:**
- Material costs increase beyond estimates
- Scope changes are approved without corresponding budget increases
- Exchange rate fluctuations affect international procurement

**Resource Risks:**
- Key personnel leave or are reassigned
- Contractor performance is below expectations
- Skills gap is discovered mid-project

**External Risks:**
- Regulatory body changes requirements or timelines
- Market conditions shift, reducing project value
- Natural disaster, pandemic, or geopolitical event disrupts supply chain

### Risk Response Strategies

Every risk with a score above your threshold (typically Score >= 8) needs a response strategy.

| Strategy | Definition | When to Use | Worked Example |
|----------|-----------|-------------|----------------|
| **Avoid** | Eliminate the risk by changing the plan | When the risk is high-impact and can be designed away | Risk: "Chosen cloud provider may not meet data residency requirements." Response: Switch to a provider with guaranteed in-region data centers before development starts. |
| **Mitigate** | Reduce the probability or impact of the risk | When the risk cannot be eliminated but can be reduced to an acceptable level | Risk: "Key architect may leave mid-project." Response: Conduct knowledge transfer sessions, document architecture decisions in ADRs, and cross-train a second engineer on the critical subsystem. |
| **Transfer** | Shift the risk to a third party | When the risk is best handled by someone with more capability or capacity | Risk: "Data center hardware failure causes extended downtime." Response: Purchase a service-level agreement (SLA) with financial penalties from the hosting provider, or buy business interruption insurance. |
| **Accept** | Acknowledge the risk and plan no proactive response | When the cost of mitigation exceeds the expected impact, or when the risk is outside your control | Risk: "Minor UI bugs will be found during UAT." Response: Accept and allocate a bug-fix buffer sprint before launch. Active acceptance means creating a contingency plan. Passive acceptance means doing nothing and dealing with it if it happens. |

**Worked Example -- Risk Response in Practice:**

Consider risk R01 from the register above: "Key architect leaves mid-project" (P=3, I=5, Score=15).

The response strategy is **Mitigate**. Here is what a concrete mitigation plan looks like:

```
RISK MITIGATION PLAN — R01
============================
Risk: Key architect (Alex) leaves mid-project
Score: 15 (HIGH)
Owner: PM
Review: Weekly

Mitigation Actions:
  1. Alex documents all architecture decisions in Architecture Decision Records (ADRs)
     — Due: End of Sprint 2
     — Status: In progress (4 of 7 ADRs written)

  2. Sarah (senior dev) shadows Alex on all critical-path design work
     — Ongoing, started Sprint 1
     — Sarah attends all architecture reviews and co-authors ADRs

  3. Weekly 1:1 between PM and Alex to gauge engagement and satisfaction
     — Ongoing
     — If Alex signals intent to leave, trigger contingency plan immediately

  4. Architecture review board meets biweekly to ensure no single-person knowledge silos
     — Ongoing

Contingency Plan (if risk materializes):
  - Sarah assumes architecture lead role
  - Engage external architecture consultant for 4-week bridge period
  - Defer non-critical architecture decisions until new hire onboards
  - Budget impact: $40K-60K for consultant engagement
```

This example illustrates the difference between a risk response strategy (one word: "mitigate") and a risk response plan (a set of concrete, scheduled, owned actions).

### Risk Review Cadence

| Project Risk Level | Review Frequency | Participants | Duration |
|-------------------|-----------------|--------------|----------|
| High-risk (many scores >= 12) | Weekly | PM, tech lead, sponsor | 30 min |
| Standard (mostly scores 4-9) | Biweekly | PM, tech lead | 20 min |
| Low-risk (all scores < 6) | Monthly | PM | 15 min |

At each review:
1. Walk through all open risks. Has anything changed?
2. Check triggers. Has any risk trigger fired?
3. Reassess probability and impact. Risks evolve as the project progresses.
4. Identify new risks. Every review should include a quick scan for emerging risks.
5. Close risks that are no longer relevant (the activity passed without the risk materializing, or the risk was successfully mitigated).

### Risk Heat Map

A heat map provides an at-a-glance view of the risk landscape. Plot each risk by probability (y-axis) and impact (x-axis).

```
RISK HEAT MAP
==============

Probability
    5 |          |          |          | R01      |          |
    4 |          |          | R03      |          |          |
    3 |          |          | R06      | R04      | R01*     |
    2 |          |          |          | R02, R07 | R05      |
    1 |          |          |          |          |          |
      +---------+----------+----------+----------+----------+
         1           2          3          4          5
                                Impact

ZONES:
  Score 1-4:   LOW (green)     — Monitor only
  Score 5-9:   MEDIUM (yellow) — Mitigation plan required
  Score 10-15: HIGH (orange)   — Active mitigation, escalate to sponsor
  Score 16-25: CRITICAL (red)  — Immediate action, may require project pause

* R01 appears at P=3, I=5 (Score 15) — HIGH zone
```

Risks in the HIGH and CRITICAL zones should be discussed at every status meeting. Risks in the MEDIUM zone should be reviewed biweekly. Risks in the LOW zone are monitored but do not require active management.

---

## Communication Planning

Communication planning defines who needs to know what, when, through which channel, and who is responsible for delivering it. Poor communication is the most commonly cited cause of project failure in post-mortems, yet communication planning is the most commonly skipped planning activity.

### Communication Plan Template

```
COMMUNICATION PLAN
===================
Project: _______________
Last updated: YYYY-MM-DD

Audience            Message/Content              Frequency    Channel         Owner    Format
------------------  ---------------------------  -----------  --------------  -------  -----------
Executive sponsor   Project health, key risks,   Biweekly     1:1 meeting     PM       Slide deck
                    decisions needed                                                    (3 slides max)

Steering committee  Status, milestones,          Monthly      Meeting +       PM       Status report
                    budget, escalations                       email summary            template

Project team        Sprint/phase progress,       Weekly       Team meeting    PM       Agenda +
                    blockers, priorities                      (or standup)             action items

Stakeholders        Progress against milestones,  Monthly     Email update    PM       Newsletter
(broad)             upcoming changes                                                   format

Vendors/partners    Deliverable status,          As needed    Email + call    Lead     Meeting notes
                    timeline changes                          (scheduled)

End users           Upcoming changes,            Per release  Email + help    Change   Release notes
                    training, support                         center          mgr      + FAQ
```

### Software Mode: Communication Cadence

**Sprint Review (Demo).** End of every sprint. The team demonstrates completed work to stakeholders. This is the primary feedback mechanism. Keep it under 60 minutes. Show working software, not slides. Invite anyone who wants to attend, but require attendance from the product owner and at least one stakeholder.

**Daily Standup (Sync vs. Async).**

| Format | How It Works | Best For |
|--------|-------------|----------|
| **Synchronous (meeting)** | 15-minute standing meeting. Each person answers: What did I do yesterday? What am I doing today? Any blockers? | Co-located teams, teams in overlapping time zones, new teams still building trust |
| **Asynchronous (written)** | Each person posts a standup update in Slack/Teams by a set time. Responses are threaded. | Distributed teams spanning 3+ time zones, experienced teams with high trust, teams that find sync standups low-value |

**Demo Cadence.** Internal demos should happen every sprint. External demos (to customers, partners, or executives) should happen at release boundaries or monthly, whichever is more frequent. External demos require more preparation -- rehearse them.

**Slack Channel Strategy:**

| Channel | Purpose | Who Joins | Norms |
|---------|---------|-----------|-------|
| #proj-[name] | General project discussion | Everyone on the project | Default channel for questions. Async-first. |
| #proj-[name]-dev | Technical discussion | Engineers, QA | Code-level conversations, PR links, technical decisions |
| #proj-[name]-alerts | Automated notifications | Engineers, PM | CI/CD results, monitoring alerts, deployment status. Low-noise -- no chatter. |
| #proj-[name]-stakeholders | Stakeholder updates | PM, stakeholders, leads | Weekly summary posts. Stakeholders ask questions here instead of DMs. |

**PR Review Expectations.** Define and communicate review turnaround time. A common standard:

- PRs should receive a first review within 4 business hours
- Authors should respond to review comments within 8 business hours
- PRs should not remain open for more than 2 business days
- If a PR is blocked on a reviewer, the author escalates to the tech lead

**Incident Communication.** When production incidents occur:

| Phase | Action | Channel | Who |
|-------|--------|---------|-----|
| Detection (0-5 min) | Acknowledge incident in #incidents | Slack | On-call engineer |
| Investigation (5-30 min) | Post initial assessment and severity | Slack + page | On-call + incident commander |
| Resolution (ongoing) | Update every 30 minutes | Slack + status page | Incident commander |
| Post-incident (within 48 hrs) | Publish blameless post-mortem | Email + wiki | Incident commander |

### General Mode: Communication Cadence

**Steering Committee Updates.** Monthly. 30-60 minutes. The PM presents project health (RAG status), milestone progress, budget variance, key risks, and decisions needed. Prepare a written report and distribute it 24 hours before the meeting so attendees can read ahead.

**Sponsor Briefings.** Biweekly or as needed. 15-30 minutes, 1:1 with the sponsor. Focus on: Are we on track? What risks should you know about? What decisions do I need from you? Never surprise the sponsor in a steering committee meeting -- brief them first.

**Team Meetings.** Weekly. 30-45 minutes. Review progress against the plan, discuss blockers, and adjust priorities for the coming week. Keep an action item log and review it at the start of each meeting.

**Vendor Check-ins.** Frequency depends on vendor criticality. For critical-path vendors, meet weekly. For non-critical vendors, meet biweekly or monthly. Always document agreements and action items in writing.

**Change Advisory Board (CAB).** For projects in regulated environments or projects that affect production systems, changes may need CAB approval. Understand the CAB schedule, submission requirements, and lead times. Build CAB submissions into your project schedule.

### RACI Matrix

RACI defines roles and responsibilities for project activities. It prevents ambiguity about who does what.

- **R = Responsible.** Does the work. There can be multiple Rs.
- **A = Accountable.** Ultimately answerable for the work being done correctly. There must be exactly one A per activity.
- **C = Consulted.** Provides input before or during the work. Two-way communication.
- **I = Informed.** Notified after the work is done or a decision is made. One-way communication.

**Worked Example:**

| Activity | PM | Tech Lead | UX Lead | QA Lead | Sponsor |
|----------|-----|-----------|---------|---------|---------|
| Define project scope | R, A | C | C | I | C |
| Create technical architecture | I | R, A | C | C | I |
| Design user interface | C | C | R, A | I | I |
| Develop features | I | R, A | C | C | I |
| Execute test plan | I | C | I | R, A | I |
| Approve milestone deliverables | R | C | C | C | A |
| Manage project budget | R, A | I | I | I | C |
| Conduct stakeholder updates | R, A | C | I | I | I |
| Sign off on go-live | R | C | C | C | A |

**RACI rules:**
- Every row must have exactly one A. If no one is accountable, no one owns it. If multiple people are accountable, no one owns it.
- Minimize the number of Cs. Too many consulted parties slow down decisions.
- If someone is both R and A for most activities, they may be overloaded.
- If a role column is mostly I, consider whether they need to be on the RACI at all.
- Review the RACI with the team. Do not assign roles without agreement.

### Escalation Path Definition

Define escalation paths before you need them. When a problem arises mid-project, the team should not have to figure out who to call.

```
ESCALATION PATH
================
Project: _______________

Level  Trigger/Threshold                    Escalate To          Response Time  Action
-----  -----------------------------------  -------------------  ------------- -------------------------
L1     Task blocked for > 1 day             Tech Lead            4 hours        Reassign, unblock, or
                                                                                find workaround

L2     Milestone at risk (>3 day slip)      PM + Product Owner   1 business     Adjust scope, add
       OR budget variance > 5%                                   day            resources, or re-plan

L3     Release date at risk (>1 week slip)  Sponsor + Steering   2 business     Executive decision:
       OR budget variance > 10%             Committee            days           cut scope, extend date,
       OR critical risk materialized                                            or add budget

L4     Project viability in question        Executive sponsor    Same day       Stop work, reassess
       OR regulatory/legal issue            + Legal/Compliance                  project, determine
       OR safety concern                                                       go/no-go
```

**Escalation norms:**
- Escalating is not failure. It is responsible management. Penalizing escalation trains the team to hide problems.
- Always escalate with a recommendation. Do not just bring problems -- bring options.
- The person who escalates owns the follow-up until the issue is resolved or explicitly reassigned.
- Never skip levels. L1 must be attempted before L2, unless the trigger clearly matches a higher level.

### Communication Anti-Patterns

These are common communication failures. Recognizing them is the first step to preventing them.

**The Watermelon Report.** Status is green on the outside (reported as "on track") but red on the inside (the team knows there are serious problems). This happens when PMs fear delivering bad news or when the culture punishes honesty. Fix it by making it safe to report accurately, and by using objective metrics (velocity, burn-down, defect counts) rather than subjective RAG ratings.

**Stakeholder Surprise.** A stakeholder learns about a significant change, delay, or problem for the first time in a public meeting. This destroys trust and triggers defensive behavior. Fix it by briefing key stakeholders individually before any group meeting where bad news will be shared.

**Information Hoarding.** One person holds critical knowledge and does not share it. This creates a bottleneck and a single point of failure. Fix it by making documentation a team norm (architecture decisions in ADRs, process decisions in meeting notes), conducting regular knowledge-sharing sessions, and practicing pair work.

**Over-Communication.** Every update goes to every person. Inboxes are flooded with irrelevant information, so important messages get buried. Fix it by using the communication plan to target messages to the right audience. Not everyone needs to know everything.

**Under-Communication.** Critical information is shared verbally in hallway conversations and never documented or broadcast. Team members outside the conversation are left in the dark. Fix it by establishing a norm: if a decision is made or information is shared that affects the project, it must be posted in the appropriate channel or documented in the appropriate artifact.

**Meeting-as-Default.** Every question, update, or decision triggers a meeting. The team spends more time in meetings than doing work. Fix it by using async communication for updates and information sharing. Reserve synchronous meetings for discussions, decisions, and relationship-building. Before scheduling a meeting, ask: "Could this be an email, a Slack thread, or a document?"

---

## Putting It All Together

The five planning disciplines are not independent activities. They form a reinforcing system:

1. **WBS** defines the scope of work.
2. **Scheduling** sequences the work against time.
3. **Resource Planning** assigns people to the work and ensures capacity.
4. **Risk Management** identifies what could disrupt the work and prepares responses.
5. **Communication Planning** ensures the right people have the right information to make decisions and do their work.

A change in any one discipline ripples through the others. A new risk may require a schedule buffer. A resource constraint may force re-sequencing. A scope change resets the WBS, which resets the schedule, which resets resource allocation.

**Planning is iterative.** You do not plan once at the start and follow the plan blindly. You plan, execute, learn, and re-plan. In software mode, this happens every sprint. In general mode, this happens at every phase gate. The plan is a living document -- or rather, a living system of documents -- that evolves as the project progresses.

### Planning Checklist

Before declaring planning complete and moving to execution, verify:

```
PLANNING COMPLETENESS CHECKLIST
================================

Work Breakdown Structure
  [ ] WBS covers 100% of project scope
  [ ] Decomposition level is appropriate (8-80 hrs or one-sprint stories)
  [ ] WBS dictionary entries exist for all work packages
  [ ] WBS reviewed and approved by the team

Scheduling
  [ ] All activities/stories sequenced with dependencies
  [ ] Critical path identified (general mode) or release plan mapped (software mode)
  [ ] Milestones defined and approved by sponsor
  [ ] Buffers allocated (project buffer, feeding buffers)
  [ ] Schedule baseline set

Resource Planning
  [ ] Resource allocation matrix complete for first phase/release
  [ ] No one allocated above 80% to a single project
  [ ] Skills gaps identified with mitigation plans
  [ ] Capacity calculated using realistic utilization rates
  [ ] Leave and holidays factored in

Risk Management
  [ ] Risk identification completed using 2+ techniques
  [ ] Risk register populated with probability, impact, and response strategies
  [ ] High and critical risks have assigned owners and mitigation actions
  [ ] Risk review cadence established
  [ ] Top 5 risks briefed to sponsor

Communication Planning
  [ ] Communication plan covers all audiences
  [ ] RACI matrix defined and agreed
  [ ] Escalation path defined with thresholds
  [ ] Meeting cadence established (standups, reviews, steering committee)
  [ ] Tools and channels set up
```

When every box is checked, you are ready to execute. When a box cannot be checked, you have identified a planning gap that needs attention before it becomes an execution problem.
