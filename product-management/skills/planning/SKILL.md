---
name: Product Planning
description: Roadmaps, PRDs, feature specifications, prioritization frameworks, and backlog grooming for startup and enterprise PMs — Now/Next/Later, timeline roadmaps, lean and full PRDs, RICE/ICE/MoSCoW scoring, and sprint-ready backlogs.
triggers:
  - roadmap
  - product roadmap
  - now next later
  - PRD
  - product requirements
  - requirements document
  - feature spec
  - specification
  - user stories
  - acceptance criteria
  - prioritization
  - RICE
  - ICE
  - MoSCoW
  - weighted scoring
  - backlog
  - backlog grooming
  - sprint planning
  - story points
  - definition of ready
---

# Product Planning

## Disclaimer

Planning artifacts are living documents. Update them as you learn -- a PRD written before user research is a hypothesis, not a spec.

## Roadmapping

A roadmap communicates what you are building, why it matters, and roughly when it will happen. It is not a project plan. It is not a feature list. It is a strategic communication tool that aligns the team around priorities and gives stakeholders enough visibility to do their jobs without micromanaging yours.

The right roadmap format depends on your organization's maturity, planning cadence, and audience. Startups need speed and flexibility. Enterprises need coordination and predictability. Both need clarity.

### Startup Mode: Now / Next / Later

For early-stage products (pre-Series B, teams under 30), avoid date-based roadmaps. You do not have enough data to predict timelines accurately, and false precision erodes trust faster than no dates at all. Use a theme-based Now/Next/Later format instead.

**How it works:** Three columns. No dates. Each column represents commitment level, not a timeline.

- **Now** -- Actively building. The team is working on these items today. 2-4 items max. These are committed and in progress.
- **Next** -- Committed to building. Scoped but not yet started. Engineering has reviewed feasibility. Up to 6 items. These are what we will start when a Now item ships.
- **Later** -- Exploring. We believe these are important, but they need more research, design, or validation before committing. Up to 8 items. These may change significantly or get cut.

**Rules:**
- Fits on one page. If it does not fit, you have too many items.
- Update weekly. Move items between columns as reality changes.
- Each item is a theme or outcome, not a feature. "Improve onboarding activation" not "Add tooltip to step 3."
- Items in Now should have an owner. Items in Next should have a rough scope. Items in Later can be just a problem statement.

**Now / Next / Later Template:**

```
ROADMAP — NOW / NEXT / LATER
==============================
Product: _______________
Last updated: _______________
Owner: _______________

NOW (actively building)          NEXT (committed, up next)         LATER (exploring)
-------------------------------- --------------------------------- ---------------------------------
[ ] Theme: _______________       [ ] Theme: _______________        [ ] Theme: _______________
    Owner: ___________               Rough scope: _________            Problem: ______________
    Key deliverable: ____            Depends on: __________
    Target outcome: _____            Target outcome: _____        [ ] Theme: _______________
                                                                      Problem: ______________
[ ] Theme: _______________       [ ] Theme: _______________
    Owner: ___________               Rough scope: _________        [ ] Theme: _______________
    Key deliverable: ____            Depends on: __________            Problem: ______________
    Target outcome: _____            Target outcome: _____
                                                                  [ ] Theme: _______________
[ ] Theme: _______________       [ ] Theme: _______________            Problem: ______________
    Owner: ___________               Rough scope: _________
    Key deliverable: ____            Target outcome: _____        [ ] Theme: _______________
    Target outcome: _____                                             Problem: ______________
                                 [ ] Theme: _______________
                                     Rough scope: _________        [ ] Theme: _______________
                                     Target outcome: _____             Problem: ______________

                                                                  [ ] Theme: _______________
                                                                      Problem: ______________

                                                                  [ ] Theme: _______________
                                                                      Problem: ______________

RECENTLY SHIPPED:
- [item] — [outcome achieved or pending measurement]
- [item] — [outcome achieved or pending measurement]
```

**Worked example:**

```
NOW (actively building)          NEXT (committed, up next)         LATER (exploring)
-------------------------------- --------------------------------- ---------------------------------
[ ] Reduce onboarding friction   [ ] Self-serve billing portal     [ ] Multi-workspace support
    Owner: Jamie                     Rough scope: Stripe                Problem: Power users want
    Key deliverable: Redesigned      integration, plan changes,         to separate projects but
    first-run experience             invoice history                    share billing
    Target outcome: Day-7            Target outcome: Reduce
    activation from 22% to 35%       billing support tickets by    [ ] AI-assisted prioritization
                                     50%                               Problem: PMs spend 10+
[ ] Search performance                                                 hrs/week on manual
    Owner: Alex                  [ ] Team permissions                   prioritization
    Key deliverable: Sub-200ms       Rough scope: Role-based
    p95 search latency               access, admin controls        [ ] Public API v2
    Target outcome: Reduce           Target outcome: Unblock           Problem: Current API lacks
    search-related churn             3 enterprise deals in              webhooks and bulk
    complaints to near zero          pipeline                           operations
```

### Enterprise Mode: Timeline Roadmap

For organizations with multiple teams, quarterly planning cycles, and cross-team dependencies, a timeline roadmap provides the structure needed to coordinate execution. This does not mean committing to exact ship dates for every feature -- it means establishing quarterly milestones with clear deliverables and dependency relationships.

**Timeline Roadmap Structure:**

- **Swim lanes by team or product area.** Each team or product area gets its own horizontal lane. This shows who owns what and where efforts overlap.
- **Quarterly milestones.** Each quarter has 2-3 major milestones with clear deliverables. A milestone is not "work on X" -- it is "X is shipped and measurable."
- **Cross-team dependencies via RACI.** For each milestone that involves multiple teams, document: who is Responsible (does the work), Accountable (owns the outcome), Consulted (provides input), Informed (needs to know).
- **Milestone gates.** For each major milestone, define what must be true to proceed to the next phase. Gates prevent teams from building on an unstable foundation.
- **Executive review format.** Quarterly review with leadership to confirm priorities, adjust scope, and communicate risks.

**Timeline Roadmap Template:**

```
TIMELINE ROADMAP
=================
Product: _______________  |  Period: FY 20__
Owner: _______________    |  Last updated: _______________

SWIM LANE: [Team / Product Area 1]
---------------------------------------------------------------------
Q1                    Q2                    Q3                    Q4
---------------------------------------------------------------------
M: [Milestone 1]     M: [Milestone 3]     M: [Milestone 5]     M: [Milestone 7]
   Deliverable:          Deliverable:          Deliverable:          Deliverable:
   Success metric:       Success metric:       Success metric:       Success metric:
   Gate: [what must      Gate:                 Gate:                 Gate:
   be true to proceed]

M: [Milestone 2]     M: [Milestone 4]                           M: [Milestone 8]
   Deliverable:          Deliverable:                               Deliverable:
   Success metric:       Success metric:                            Success metric:

SWIM LANE: [Team / Product Area 2]
---------------------------------------------------------------------
Q1                    Q2                    Q3                    Q4
---------------------------------------------------------------------
M: [Milestone A]     M: [Milestone C]     M: [Milestone D]     M: [Milestone E]
   Deliverable:          Deliverable:          Deliverable:          Deliverable:
   Success metric:       Success metric:       Success metric:       Success metric:

DEPENDENCIES:
| Milestone | Depends On | Owning Team | RACI | Handoff Date | Status |
|-----------|------------|-------------|------|--------------|--------|
| M3        | M2 shipped | Team 1      | R: Team 1, A: PM Lead, C: Team 2, I: Exec | Mar 31 | On track |
| M-C       | M1 API     | Team 2      | R: Team 2, A: Eng Lead, C: Team 1, I: Sales | Feb 15 | At risk  |

MILESTONE GATES:
| Milestone | Gate Criteria | Owner | Status |
|-----------|--------------|-------|--------|
| M2 -> M3  | API latency < 200ms p99, zero critical bugs, load test passed | Eng Lead | Pending |
| M-C -> M-D| 80% of beta users activated, NPS > 30 from beta cohort | PM Lead | Not started |

RISKS & MITIGATIONS:
| Risk | Impact (H/M/L) | Probability (H/M/L) | Mitigation | Owner |
|------|----------------|---------------------|------------|-------|
|      |                |                     |            |       |

EXECUTIVE REVIEW CADENCE: [Quarterly — next review: ___]
```

### Roadmap Communication

Different audiences need different views of the same roadmap. Showing engineering details to the board wastes their time and yours. Showing strategic themes to engineers without scope details leaves them unable to plan. Tailor the message.

| Audience | What They Care About | Format | Cadence | What to Exclude |
|---|---|---|---|---|
| **Board** | Strategy, market positioning, key metrics, major bets | 3-5 slides: vision, strategic themes, KPI dashboard, major risks | Quarterly (board meeting) | Feature names, engineering details, sprint-level scope |
| **Executive team** | Themes, milestones, resource allocation, cross-team risks | 1-page timeline with swim lanes, milestone gates, dependency map | Monthly (leadership sync) | Individual story-level items, technical implementation details |
| **Engineering** | Detailed scope, technical requirements, dependencies, sequencing | Full roadmap with PRD links, API contracts, data model changes, story breakdowns | Weekly (planning/standup) | Business justification (they should already know the "why") |
| **Customers** | What is coming that solves their problems, general direction | Blog post, changelog preview, or "coming soon" page -- value-oriented, no dates | Quarterly or as features ship | Internal codenames, exact timelines, features that may get cut |

**Key rule:** Never share dates with customers unless you are highly confident (>90%) in delivery. "Coming this quarter" is acceptable. "Shipping March 15" is a commitment you may not be able to keep. Missed external dates damage trust far more than vague timelines.

### Roadmap Anti-Patterns

Watch for these failure modes and correct them immediately:

- **Feature factory.** Teams ship features without connecting them to outcomes. The roadmap is a list of things to build, not a strategy. Fix: every roadmap item must have a target outcome and success metric. If you cannot articulate why you are building it, do not build it.
- **Date-driven roadmaps without outcomes.** The roadmap says "Ship X by March" but does not say what success looks like. Teams hit the date but miss the impact. Fix: pair every date commitment with a measurable outcome. "Ship X by March; target: 20% increase in activation."
- **Roadmap-as-contract.** Stakeholders treat roadmap estimates as commitments. When priorities shift, trust breaks down. Fix: explicitly label commitment levels. "Committed" vs. "Planned" vs. "Exploring." Educate stakeholders that only "Committed" items are near-certain.
- **Not updating the roadmap.** The roadmap was last updated 3 months ago and no longer reflects reality. Teams work off tribal knowledge instead. Fix: set a weekly 15-minute review to update the roadmap. If you cannot maintain it weekly, your roadmap is too detailed.
- **Stakeholder-driven roadmap (loudest voice wins).** The VP of Sales dictates the roadmap based on the last customer call. Product strategy is reactive, not proactive. Fix: use a prioritization framework (see Prioritization section below). Every request goes through the same scoring process, regardless of who is asking.

---

## PRDs

A PRD (Product Requirements Document) describes what you are building, why you are building it, and how you will know it worked. It is the bridge between strategy ("we need to improve activation") and execution ("here is exactly what engineering should build"). The right level of detail depends on your team size, risk tolerance, and how much is unknown.

### Startup Mode: 1-Pager PRD

For small teams (2-15 people), long PRDs are waste. Engineers are in the room when decisions are made. Context is shared verbally. What you need is a concise document that captures the key decisions so the team does not re-litigate them, and so future team members can understand why you built what you built.

**1-Pager PRD Template:**

```
1-PAGER PRD
=============
Title: _______________
Author: _______________  |  Date: _______________
Status: Draft / In Review / Approved

PROBLEM
What is the problem? Who experiences it? How do we know it is real?
[2-4 sentences. Reference user research, support tickets, data, or direct
customer quotes. If you cannot cite evidence, this is a hypothesis -- label it
as such.]

PROPOSED SOLUTION
How does it work from the user's perspective? Walk through the core flow in
plain language.
[3-6 sentences. Focus on the user experience, not the technical
implementation. Include a wireframe or sketch if it helps.]

SUCCESS METRICS (2-3 measurable outcomes)
1. [Metric]: from [current baseline] to [target] within [timeframe]
2. [Metric]: from [current baseline] to [target] within [timeframe]
3. [Metric]: from [current baseline] to [target] within [timeframe]

SCOPE
In (what we are building):
- [item]
- [item]
- [item]

Out (what we are NOT building -- be explicit):
- [item] — reason it is out of scope
- [item] — reason it is out of scope

KEY RISKS
- [Risk 1]: [Mitigation or acceptance]
- [Risk 2]: [Mitigation or acceptance]

OPEN QUESTIONS
- [Question 1]: [Who will answer it, by when]
- [Question 2]: [Who will answer it, by when]
```

**Worked Example:**

```
1-PAGER PRD
=============
Title: Onboarding Redesign — Guided First Project
Author: Jamie Chen  |  Date: 2026-02-15
Status: In Review

PROBLEM
New users who sign up for SignalPM abandon during onboarding at a 68% rate.
Exit surveys and session recordings show that users do not understand what to
do after account creation. The empty state provides no guidance. Users who
create their first project within 10 minutes of signup retain at 3x the rate
of users who do not (internal cohort analysis, Jan 2026).

PROPOSED SOLUTION
Replace the current empty-state dashboard with a guided "Create Your First
Project" experience. The flow walks users through: (1) naming a project,
(2) importing 3 sample feature requests from a template, (3) running their
first prioritization sort, and (4) seeing the output. Total time: under 5
minutes. At the end, users have a populated project they can continue to
build on or reset.

SUCCESS METRICS
1. Day-7 activation rate: from 22% to 35% within 8 weeks of launch
2. Time-to-first-value: from 25 minutes to under 8 minutes
3. Onboarding completion rate: from 32% to 60%

SCOPE
In:
- Guided first-run flow (4 steps)
- Sample project template with pre-loaded data
- Progress indicator showing completion status
- "Skip" option at each step (never trap the user)

Out:
- Team onboarding (multi-user) — will address in next cycle
- Custom template creation — not enough data on what templates users want
- Email drip campaign — Marketing owns this; coordinate separately

KEY RISKS
- Risk: Guided flow feels patronizing to experienced PMs.
  Mitigation: Add "I know what I'm doing — skip setup" link on first screen.
- Risk: Sample data confuses users who think it is real.
  Mitigation: Clear "Sample Project" badge + one-click reset/delete.

OPEN QUESTIONS
- Should we auto-detect the user's role during signup to customize the
  experience? (Jamie to test with 5 users by Feb 22)
- What is the right sample dataset? B2B SaaS features? Generic?
  (Product to decide by Feb 20)
```

### Enterprise Mode: Full PRD

For larger teams, products with regulatory requirements, or high-risk features (payments, security, data migrations), you need a comprehensive PRD that leaves minimal ambiguity for engineering, design, QA, and legal.

**Full PRD Template:**

```
PRODUCT REQUIREMENTS DOCUMENT
===============================
Title: _______________
Author: _______________  |  Date: _______________
Version: ___  |  Status: Draft / In Review / Approved / Archived
Approvers: [Name, Role] | [Name, Role] | [Name, Role]

1. BACKGROUND & STRATEGIC CONTEXT
   Why are we building this now? How does it align with company and product
   strategy?
   - Business context: [What strategic priority does this support?]
   - Market context: [What competitive or market pressure makes this urgent?]
   - Customer context: [What user research or data supports this?]
   - Link to OKR: [Which OKR does this contribute to?]

2. USER STORIES
   [For each persona affected, write user stories with acceptance criteria]

   Story 1: As a [persona], I want [action], so that [outcome].
     Acceptance Criteria:
       - Given [precondition], when [action], then [expected result].
       - Given [precondition], when [action], then [expected result].
       - Given [precondition], when [action], then [expected result].

   Story 2: As a [persona], I want [action], so that [outcome].
     Acceptance Criteria:
       - Given [precondition], when [action], then [expected result].
       - Given [precondition], when [action], then [expected result].

   [Continue for all stories]

3. FUNCTIONAL REQUIREMENTS
   [Detailed behavior specifications]
   FR-1: [Description of behavior]
   FR-2: [Description of behavior]
   FR-3: [Description of behavior]
   ...

4. NON-FUNCTIONAL REQUIREMENTS
   Performance:
   - [Target]: [e.g., Page load < 2s at p95]
   - [Target]: [e.g., API response < 300ms at p99]
   - [Target]: [e.g., Support 500 concurrent users without degradation]

   Security:
   - [Requirement]: [e.g., All PII encrypted at rest and in transit]
   - [Requirement]: [e.g., Audit log for all admin actions]
   - [Requirement]: [e.g., SOC 2 compliance maintained]

   Accessibility:
   - WCAG 2.1 Level AA compliance required
   - Screen reader compatibility for all new UI components
   - Keyboard navigation for all interactive elements
   - Color contrast ratios meeting AA standards (4.5:1 for text)

   Internationalization / Localization:
   - [Languages supported]: [e.g., English, Spanish, French, German, Japanese]
   - [Date/time/currency formatting]: [e.g., Locale-aware rendering]
   - [RTL support]: [Yes/No — specify if Arabic or Hebrew required]
   - [String externalization]: All user-facing strings in resource files

5. TECHNICAL CONSIDERATIONS
   API Contracts:
   - [Endpoint]: [Method] [Path]
     Request: [Schema]
     Response: [Schema]
     Error codes: [List]

   Data Model Changes:
   - [New table/field]: [Description, type, constraints]
   - [Migration]: [Forward and rollback plan]

   Migration Needs:
   - [Data migration]: [What data moves, from where to where, volume]
   - [Backward compatibility]: [How existing users/integrations are affected]
   - [Rollback plan]: [How to revert if migration fails]

6. EDGE CASES
   - [Edge case 1]: [Expected behavior]
   - [Edge case 2]: [Expected behavior]
   - [Edge case 3]: [Expected behavior]
   - [Edge case 4]: [Expected behavior]
   [Aim for 10+ edge cases. If you cannot think of 10, you have not thought
   hard enough. Include: empty states, max limits, concurrent edits, network
   failures, permission boundaries, time zone edge cases, Unicode/special
   characters, bulk operations at scale.]

7. ANALYTICS INSTRUMENTATION PLAN
   | Event Name | Trigger | Properties | Funnel Position |
   |------------|---------|------------|-----------------|
   |            |         |            |                 |

   Key funnels to track:
   - [Funnel 1]: [Steps]
   - [Funnel 2]: [Steps]

   Success dashboard:
   - [Metric 1]: [Source, refresh cadence]
   - [Metric 2]: [Source, refresh cadence]

8. ROLLOUT PLAN
   Phase 1: Internal dogfood ([dates])
     - Audience: Internal team only
     - Feature flag: [flag name]
     - Success criteria to proceed: [criteria]

   Phase 2: Beta ([dates])
     - Audience: [X]% of users, selected cohort
     - Feature flag: [flag name], [% rollout]
     - Monitoring: [What to watch for]
     - Rollback trigger: [What would cause us to revert]
     - Success criteria to proceed: [criteria]

   Phase 3: General availability ([dates])
     - Audience: 100% of users
     - Announcement: [Changelog, email, in-app notification]
     - Support readiness: [Documentation, training, FAQ]

9. DEPENDENCIES
   Cross-team:
   - [Team]: [What we need from them, by when]
   - [Team]: [What we need from them, by when]

   Third-party:
   - [Vendor/service]: [Integration, timeline, risk]

10. APPROVALS
    | Approver | Role | Status | Date |
    |----------|------|--------|------|
    |          |      |        |      |

APPENDIX:
- [Links to designs, wireframes, prototypes]
- [Links to user research]
- [Links to technical design docs]
```

### PRD Quality Checklist

Before marking any PRD as "Ready for Engineering," validate it against these criteria:

- [ ] **Is the problem validated with research?** The PRD cites user interviews, support tickets, analytics data, or market research -- not just intuition or stakeholder requests. If the problem is not validated, label the PRD as a hypothesis and plan a validation step before full build.
- [ ] **Are success metrics measurable and time-bound?** Each metric has a current baseline, a target, and a timeframe. "Improve activation" is not a metric. "Increase Day-7 activation from 22% to 35% within 8 weeks of launch" is.
- [ ] **Are edge cases covered?** At minimum: empty states, error states, permission boundaries, max limits, concurrent actions, network failures. For a full PRD, aim for 10+ edge cases.
- [ ] **Is scope clearly bounded?** The "Out of scope" section is as important as "In scope." Explicit exclusions prevent scope creep and set clear expectations. Every out-of-scope item should have a reason.
- [ ] **Are dependencies identified?** Cross-team dependencies have owners, handoff dates, and status. Third-party dependencies have risk assessments and fallback plans.
- [ ] **Is the rollout plan safe?** The feature can be rolled back. There is a monitoring plan. There are clear criteria for proceeding from each phase to the next. No big-bang launches for high-risk features.

---

## Feature Specs

Feature specs translate PRD-level requirements into detailed, buildable descriptions. Where a PRD says "users can manage their team members," a feature spec defines every interaction, state, error condition, and technical contract needed to implement that capability.

### User Story Format

User stories describe a feature from the user's perspective. They follow the standard format:

> As a **[persona]**, I want **[action]**, so that **[outcome]**.

The persona is specific (not "a user"). The action is concrete. The outcome is the value the user gets, not the feature itself.

**Five Example User Stories:**

1. As a **product manager**, I want **to drag and drop roadmap items between Now/Next/Later columns**, so that **I can re-prioritize quickly during weekly planning without leaving the roadmap view**.

2. As a **new user on a free trial**, I want **to see a pre-populated sample project when I first log in**, so that **I understand how the product works before investing time in setting up my own data**.

3. As an **engineering lead**, I want **to filter the backlog by team and sprint**, so that **I can see only the items relevant to my team's upcoming sprint planning session**.

4. As a **VP of Product**, I want **to export the roadmap as a PDF with our company branding**, so that **I can include it in quarterly board presentations without recreating it in slides**.

5. As a **customer success manager**, I want **to subscribe to roadmap updates for specific customer accounts**, so that **I am notified when features requested by my accounts move to "Now" status**.

### Acceptance Criteria

Acceptance criteria define the conditions that must be met for a user story to be considered complete. Use the Given/When/Then format for clarity and testability.

**Rules for writing acceptance criteria:**
- **Testable.** A QA engineer can write a test case directly from the criterion. If it is ambiguous, rewrite it.
- **Unambiguous.** There is only one way to interpret the criterion. "The page loads quickly" is ambiguous. "The page loads in under 2 seconds at p95" is not.
- **One behavior per criterion.** Each Given/When/Then covers a single behavior. Do not combine multiple behaviors into one criterion.

**Worked Examples:**

User story: As a **product manager**, I want **to drag and drop roadmap items between columns**, so that **I can re-prioritize quickly**.

```
Acceptance Criteria:

AC-1: Successful drag and drop
  Given I am viewing the Now/Next/Later roadmap
  When I drag an item from the "Next" column and drop it in the "Now" column
  Then the item appears in the "Now" column in the position where I dropped it
  And the item is removed from the "Next" column
  And the change is saved automatically (no save button required)

AC-2: Undo after move
  Given I have just moved an item between columns
  When I click the "Undo" toast notification that appears for 5 seconds
  Then the item returns to its original column and position

AC-3: Permission restriction
  Given I am a viewer (read-only) on the roadmap
  When I attempt to drag an item
  Then the drag action is not initiated
  And a tooltip appears: "You need Editor access to move items"

AC-4: Concurrent edit conflict
  Given another user has moved the same item while I was viewing the page
  When I attempt to drag that item
  Then the page refreshes to show the current state
  And a notification appears: "This item was recently moved by [user name]"

AC-5: Mobile / touch behavior
  Given I am on a touch device with screen width < 768px
  When I long-press an item for 500ms
  Then the item enters drag mode with a visual lift effect
  And I can drag it to a different column
```

### Design Integration

Feature specs must reference design assets and specify interaction behaviors that are not visible in static mockups.

**Required design references:**
- Link to wireframes or mockups (Figma, Sketch, or equivalent)
- Link to interactive prototype if available

**Interaction specs to define:**
- **Hover states:** What happens when the user hovers over interactive elements? (Color change, tooltip, cursor change)
- **Loading states:** What does the user see while data loads? (Skeleton screen, spinner, placeholder content). Define the threshold: show spinner after 300ms, show skeleton after 1s.
- **Empty states:** What does the user see when there is no data? (Illustration + helpful message + CTA to create first item). Empty states are onboarding opportunities -- do not waste them with "No data found."
- **Error states:** What does the user see when something goes wrong? (Inline error message, toast notification, full-page error). Distinguish between user errors (validation) and system errors (server failure). Provide actionable guidance: "Check your connection and try again" not "Error 500."
- **Responsive breakpoints:** Define behavior at each breakpoint. At minimum: mobile (<768px), tablet (768px-1024px), desktop (>1024px). Specify what collapses, what reflows, what hides.

### Technical Spec Section

For features that involve backend changes, include a technical spec section that gives engineering enough detail to estimate and plan without requiring a separate technical design document.

**API contracts:**

```
Endpoint: POST /api/v1/roadmap/{roadmap_id}/items/{item_id}/move
Method: POST
Authentication: Bearer token (requires Editor role on roadmap)

Request body:
{
  "target_column": "now" | "next" | "later",
  "position": integer (0-indexed, position within target column),
  "source_column": "now" | "next" | "later"
}

Response (200 OK):
{
  "item_id": "string",
  "column": "now" | "next" | "later",
  "position": integer,
  "updated_at": "ISO 8601 timestamp",
  "updated_by": "user_id"
}

Error responses:
  403 Forbidden: User lacks Editor permission
  404 Not Found: Roadmap or item does not exist
  409 Conflict: Item was modified by another user since last fetch
  422 Unprocessable Entity: Invalid target_column or position
```

**Data model changes:**

```
Table: roadmap_items
  New field: column_position (integer, not null, default 0)
  New field: moved_at (timestamp, nullable)
  New field: moved_by (foreign key -> users.id, nullable)

Index: idx_roadmap_items_column_position ON roadmap_items(roadmap_id, column, column_position)

Migration: Backfill column_position for existing items based on current sort order.
Rollback: Drop new fields. No data loss — fields are additive only.
```

**Performance requirements:**
- Drag-and-drop save: < 200ms round-trip at p95
- Roadmap load with up to 50 items: < 1s at p95
- Real-time sync for concurrent editors: < 500ms propagation delay

### Feature Spec Template

```
FEATURE SPECIFICATION
======================
Feature: _______________
PRD Reference: [Link to parent PRD]
Author: _______________  |  Date: _______________
Status: Draft / In Review / Approved

USER STORIES:
  Story 1: As a [persona], I want [action], so that [outcome].
    AC-1: Given [context], when [action], then [result].
    AC-2: Given [context], when [action], then [result].
    AC-3: Given [context], when [action], then [result].

  Story 2: As a [persona], I want [action], so that [outcome].
    AC-1: Given [context], when [action], then [result].
    AC-2: Given [context], when [action], then [result].

DESIGN:
  Mockups: [Link to Figma / Sketch / etc.]
  Prototype: [Link if available]

  Interaction specs:
    Hover states: _______________
    Loading states: _______________
    Empty states: _______________
    Error states: _______________
    Responsive breakpoints:
      Mobile (<768px): _______________
      Tablet (768-1024px): _______________
      Desktop (>1024px): _______________

TECHNICAL SPEC:
  API contracts:
    [Endpoint]: [Method] [Path]
      Request: [Schema]
      Response: [Schema]
      Errors: [Codes and meanings]

  Data model changes:
    [Table]: [New/modified fields]
    Migration plan: _______________
    Rollback plan: _______________

  Performance requirements:
    - [Operation]: [Target latency at percentile]
    - [Operation]: [Target throughput]

EDGE CASES:
  - [Case]: [Expected behavior]
  - [Case]: [Expected behavior]
  - [Case]: [Expected behavior]

ANALYTICS:
  | Event | Trigger | Properties |
  |-------|---------|------------|
  |       |         |            |

DEPENDENCIES:
  - [Team / service]: [What is needed, by when]

ESTIMATION:
  Story points: ___
  Sprint target: ___
```

---

## Prioritization

Prioritization is the core skill of product management. Every team has more ideas than capacity. Frameworks give you a structured, repeatable way to compare options and defend decisions. No framework is perfect -- the value is in the structured thinking, not the precise score. Pick one, apply it consistently, and iterate.

### RICE Scoring

RICE is a quantitative framework developed by Intercom. It scores initiatives on four dimensions and produces a single comparable number.

**Dimensions:**

- **Reach:** How many users/customers will this impact in a given time period (usually one quarter)? Use real data: monthly active users who would encounter the feature, support tickets related to the problem, or segment size from analytics. Avoid "everyone" -- be specific.
- **Impact:** How much will this move the needle for each user who encounters it? Use the standard scale:
  - 3 = Massive impact (transforms the workflow)
  - 2 = High impact (significant improvement)
  - 1 = Medium impact (noticeable improvement)
  - 0.5 = Low impact (minor improvement)
  - 0.25 = Minimal impact (barely noticeable)
- **Confidence:** How confident are you in your Reach and Impact estimates? Be honest.
  - 100% = High confidence (backed by data, user research, or strong precedent)
  - 80% = Medium confidence (some data, reasonable assumptions)
  - 50% = Low confidence (gut feel, limited data, novel territory)
- **Effort:** How many person-months of work will this take? Include engineering, design, QA, and any other team effort. Round up to account for unknowns.

**Formula:**

```
RICE Score = (Reach x Impact x Confidence) / Effort
```

**Worked Example:**

| Feature | Reach (users/quarter) | Impact (0.25-3) | Confidence (%) | Effort (person-months) | RICE Score |
|---|---|---|---|---|---|
| Guided onboarding flow | 5,000 | 2 | 80% | 3 | (5000 x 2 x 0.8) / 3 = **2,667** |
| Advanced search filters | 2,000 | 1 | 100% | 2 | (2000 x 1 x 1.0) / 2 = **1,000** |
| Slack integration | 1,500 | 2 | 50% | 4 | (1500 x 2 x 0.5) / 4 = **375** |
| Dark mode | 8,000 | 0.25 | 100% | 1 | (8000 x 0.25 x 1.0) / 1 = **2,000** |

**Ranked by RICE score:** Guided onboarding (2,667) > Dark mode (2,000) > Advanced search (1,000) > Slack integration (375).

**Key insight from the example:** Dark mode has massive reach but minimal impact per user. It still scores well because it is cheap. The Slack integration scores lowest despite high impact because low confidence and high effort drag it down. If you can increase confidence (run a survey, check usage of competitor Slack integrations), the score may change significantly.

**When to use RICE:** Quarterly planning when you have data on reach and can estimate effort reasonably well. Best for teams with analytics infrastructure and at least 6-12 months of product history.

### ICE Scoring

ICE is a faster, simpler framework suitable for rapid prioritization when you do not have detailed reach data or effort estimates.

**Dimensions:**

- **Impact:** How much will this improve the key metric? Score 1-10.
- **Confidence:** How sure are you about your Impact and Ease estimates? Score 1-10.
- **Ease:** How easy is this to implement? Score 1-10 (10 = trivial, 1 = massive effort).

**Formula:**

```
ICE Score = Impact x Confidence x Ease
```

**Example:**

| Feature | Impact (1-10) | Confidence (1-10) | Ease (1-10) | ICE Score |
|---|---|---|---|---|
| Guided onboarding flow | 9 | 7 | 5 | **315** |
| Advanced search filters | 6 | 8 | 7 | **336** |
| Slack integration | 8 | 4 | 3 | **96** |
| Dark mode | 3 | 9 | 8 | **216** |

**When to use ICE:** Weekly or bi-weekly prioritization in fast-moving teams. When you need a quick gut-check, not a precision instrument. Best for startups and small teams.

### MoSCoW

MoSCoW is a categorical prioritization method. Instead of scoring items numerically, you sort them into four buckets based on necessity for the current release or sprint.

- **Must have:** Non-negotiable. The release cannot ship without these. They are launch blockers, regulatory requirements, or features without which the product does not function. If a Must is not delivered, the release fails.
- **Should have:** Important. Painful to defer. Significant value to users, but the product still functions without them. These are the first items you add back if Must haves come in under budget.
- **Could have:** Nice to have. Desirable but first to cut when time or resources are constrained. These improve the experience but do not make or break the release.
- **Won't have this time:** Explicitly deferred. Not in this release. Documenting what you are NOT doing is as important as documenting what you are. This prevents scope creep and sets expectations.

**Rules:**
- Must haves should consume no more than 60% of available effort. If Must haves exceed 60%, you have too many -- force-rank and demote some to Should.
- Every Won't have should include a brief reason for deferral, so the decision is traceable.
- MoSCoW is for scoping a single release or sprint. It does not replace a roadmap or strategic prioritization.

**Example:**

| Item | Category | Rationale |
|---|---|---|
| User authentication (SSO) | Must have | Enterprise deal blocker; 3 accounts waiting |
| Onboarding redesign | Must have | Activation rate is critical path to growth |
| Slack integration | Should have | Frequently requested; improves daily workflow |
| Dark mode | Could have | User demand exists but no churn correlation |
| Mobile app | Won't have | Insufficient data on mobile usage; revisit Q3 |

### Weighted Scoring

Weighted scoring is the most flexible framework. It allows you to define custom criteria, assign weights based on strategic importance, and produce a total score that reflects your organization's specific priorities. It is ideal for cross-team decisions where stakeholders disagree on what matters most.

**How it works:**

1. **Define 4-6 criteria** that matter for this decision. Common criteria: strategic alignment, user impact, revenue potential, effort required (inverted -- lower effort = higher score), technical risk (inverted), competitive differentiation.
2. **Assign weights** to each criterion. Weights must sum to 100%. The weights encode your strategy. If growth is the top priority, weight user impact and reach higher. If efficiency is the priority, weight effort and risk higher.
3. **Score each item** 1-5 per criterion. Use a rubric to ensure consistency: 1 = very low, 2 = low, 3 = medium, 4 = high, 5 = very high.
4. **Multiply each score by its weight** and sum for a total weighted score.

**Example:**

| Criterion | Weight | Onboarding Redesign | Slack Integration | Dark Mode | Mobile App |
|---|---|---|---|---|---|
| Strategic alignment | 30% | 5 (1.50) | 3 (0.90) | 2 (0.60) | 3 (0.90) |
| User impact | 25% | 4 (1.00) | 4 (1.00) | 2 (0.50) | 3 (0.75) |
| Revenue potential | 20% | 4 (0.80) | 3 (0.60) | 1 (0.20) | 2 (0.40) |
| Ease of implementation | 15% | 3 (0.45) | 2 (0.30) | 5 (0.75) | 1 (0.15) |
| Competitive differentiation | 10% | 3 (0.30) | 2 (0.20) | 1 (0.10) | 4 (0.40) |
| **Total** | **100%** | **4.05** | **3.00** | **2.15** | **2.60** |

**When to use weighted scoring:** Quarterly or annual planning with multiple stakeholders. When RICE or ICE feels too simplistic. When you need a transparent, auditable decision process that stakeholders can critique and improve. The explicit weights make trade-offs visible -- "we are weighting revenue potential at 20%, not 50%, because our current strategy prioritizes growth over monetization."

### Decision Guide: When to Use Which Framework

| Context | Recommended Framework | Why |
|---|---|---|
| Weekly sprint prioritization, small team, fast decisions needed | **ICE** | Quick to apply, no detailed data needed, good for rapid iteration |
| Quarterly planning, data-rich environment, need precision | **RICE** | Quantitative rigor, accounts for reach and effort separately |
| Scoping a single release, need to define minimum viable scope | **MoSCoW** | Categorical, clear boundaries between must/should/could/won't |
| Cross-team decision, multiple stakeholders disagree | **Weighted scoring** | Customizable criteria, explicit weights make trade-offs visible |
| High uncertainty, limited data, need to move fast | **ICE** | Tolerance for low-confidence estimates, speed over precision |
| Board or executive presentation, need defensible reasoning | **RICE or Weighted** | Produces auditable scores with clear methodology |

### Startup vs. Enterprise Prioritization

**Startup mode:** Use ICE for speed. Score items in a 15-minute session with 2-3 people (PM, tech lead, designer). Re-prioritize weekly as you learn. Do not over-invest in frameworks -- the framework should take less time than the execution. Gut-check the top 3 items: "If we could only ship one thing this week, is this the right one?"

**Enterprise mode:** Use RICE with a stakeholder input matrix for quarterly planning. Collect reach estimates from analytics, impact ratings from PM and design, confidence levels from user research, and effort estimates from engineering. Compile into a single scorecard. Use weighted scoring for cross-team decisions where teams bring different criteria to the table. Present the framework and its inputs to leadership -- the process transparency builds trust even when the output is imperfect.

---

## Backlog Grooming

Backlog grooming (also called backlog refinement) is the ongoing process of preparing work items so they are ready for sprint planning. The goal is to ensure that when a sprint starts, the team can pick up items and begin work immediately -- no ambiguity, no missing designs, no unresolved dependencies. A well-groomed backlog is the difference between a productive sprint and one that stalls on day two because no one knows what "improve search" actually means.

### Story Point Estimation

Story points measure relative effort, complexity, and uncertainty -- not time. A 5-point story is roughly 2-3x the effort of a 2-point story, but it might take longer or shorter depending on who works on it and what surprises emerge. The value of story points is in relative comparison, not absolute prediction.

**Fibonacci Sequence:** 1, 2, 3, 5, 8, 13, 21

| Points | Rough Meaning | Example |
|---|---|---|
| **1** | Trivial. Well-understood, no unknowns. A few hours of work. | Fix a typo in the UI, update a config value |
| **2** | Small. Straightforward, minimal uncertainty. Less than a day. | Add a new field to an existing form, write a simple API endpoint |
| **3** | Medium-small. Some complexity, but approach is clear. 1-2 days. | Add filtering to a list view, implement a new notification type |
| **5** | Medium. Moderate complexity, some unknowns. 2-4 days. | Build a new CRUD feature with UI and API, integrate a third-party service |
| **8** | Large. Significant complexity or uncertainty. About a week of work. | Redesign onboarding flow, build a reporting dashboard with multiple chart types |
| **13** | Very large. High complexity, multiple unknowns. Should probably be split. | Build a permissions system with role-based access, implement real-time collaboration |
| **21** | Epic-sized. Too large for a single sprint. Must be split. | Rewrite the billing system, build a public API from scratch |

**Planning Poker Process:**

1. **Present the story.** PM or story author reads the story and acceptance criteria. Team asks clarifying questions (5 minutes max).
2. **Vote silently.** Each team member selects a story point value without revealing it. Use cards, fingers, or a tool like PlanITpoker.
3. **Reveal simultaneously.** Everyone shows their estimate at the same time.
4. **Discuss outliers.** The highest and lowest estimators explain their reasoning. This is where hidden complexity or misunderstandings surface. (3 minutes max)
5. **Re-vote.** After discussion, vote again. If estimates converge (within one Fibonacci step), take the higher number. If they still diverge, discuss once more and use the median or let the implementer's estimate stand.

**Reference stories:** Anchor the scale by identifying 3-5 well-understood, previously completed stories that the team agrees on:
- "The login page redesign was a 5."
- "Adding the CSV export was a 3."
- "The Stripe integration was a 13."

New stories are estimated relative to these anchors. This prevents point inflation and keeps estimates consistent over time.

### Backlog Health Metrics

Track these metrics to know if your grooming process is working:

| Metric | Target | Why It Matters |
|---|---|---|
| **% of items groomed** (2 sprints ahead) | > 80% | If less than 80% of the next 2 sprints' worth of items are groomed, sprint planning will stall. You are living sprint-to-sprint instead of planning ahead. |
| **Avg age of ungroomed items** | < 4 weeks | Items sitting in the backlog for months without grooming are probably stale. They need to be re-evaluated, updated, or removed. Old items accumulate debt. |
| **Items per sprint ratio (velocity)** | Stable +/- 15% | Velocity should be relatively stable sprint-to-sprint. Large swings indicate estimation problems, scope changes, or team disruptions. Track the 4-sprint rolling average. |
| **% of stories that change after grooming** | < 10% | If more than 10% of stories require significant re-scoping after grooming, the grooming process is not thorough enough. Investigate whether acceptance criteria are being reviewed, designs are finalized, and dependencies are identified. |

### Grooming Ceremony Structure

**Cadence:** Weekly, 60 minutes, whole team (PM, engineering, design, QA).

| Segment | Duration | Activity | Output |
|---|---|---|---|
| **Review incoming items** | 15 min | Walk through new items added to the backlog since last session. PM provides context. Team asks clarifying questions. | New items have enough context for estimation. Items needing more research are flagged. |
| **Estimate top items** | 20 min | Planning poker on the highest-priority unestimated items. Aim for 5-8 items per session. | Top items have story point estimates. Outlier discussions documented. |
| **Prioritize** | 10 min | Re-order the backlog based on new information, changing priorities, or updated estimates. PM drives, team provides input. | Backlog order reflects current priorities. |
| **Split large stories** | 15 min | Identify items estimated at 13 or 21 points. Break them into smaller stories using splitting patterns (see below). | Large stories replaced with 2-4 smaller stories, each <= 8 points. |

**Ground rules:**
- Start on time. End on time. If discussion runs long on one item, timebox it and take it offline.
- The PM owns priority order. Engineering owns estimates. Neither overrides the other.
- If the team consistently cannot groom enough items in 60 minutes, increase frequency (twice per week) rather than increasing meeting length.

### Definition of Ready

A story is "Ready" when it meets all of these criteria. Stories that are not Ready should not enter a sprint.

- [ ] **User story written.** Follows the "As a [persona], I want [action], so that [outcome]" format. The persona is specific. The outcome is a user benefit, not a feature description.
- [ ] **Acceptance criteria defined.** Given/When/Then format. At least 2 criteria per story. Each criterion is testable and unambiguous.
- [ ] **Design reviewed.** Wireframes, mockups, or prototypes are complete and reviewed by engineering. Interaction specs (hover, loading, empty, error states) are documented.
- [ ] **Dependencies identified.** If the story depends on another team, API, third-party service, or another story, the dependency is documented and the blocker is resolved or has a committed resolution date.
- [ ] **Estimated (story points).** The team has estimated the story using planning poker. The estimate is 8 points or fewer. Stories > 8 points must be split.
- [ ] **Small enough for one sprint.** The story can be completed (coded, tested, reviewed, deployed) within a single sprint. If not, split it further.
- [ ] **No open questions.** All open questions from the PRD or spec are resolved. If a question cannot be resolved before the sprint, descope the story to exclude the uncertain part.

### Story Splitting Patterns

When a story is too large (estimated at 13+ points), split it using one of these patterns. The goal is to produce smaller stories that are each independently valuable and deliverable.

**By workflow step:**
Split a multi-step workflow into separate stories for each step.
- Original: "As a user, I want to create, configure, and publish a report."
- Split: Story A: "Create a report (name, description, select data source)." Story B: "Configure report (choose chart type, set filters, preview)." Story C: "Publish report (share link, set permissions, notify subscribers)."

**By business rule:**
Split based on the different rules or conditions that apply.
- Original: "As a user, I want to see dynamic pricing based on my plan, location, and usage."
- Split: Story A: "Show pricing based on plan tier." Story B: "Apply location-based pricing adjustments." Story C: "Apply usage-based discounts."

**By data variation:**
Split based on different data types, sources, or formats.
- Original: "As a user, I want to import data from CSV, Excel, Google Sheets, and Salesforce."
- Split: Story A: "Import from CSV." Story B: "Import from Excel." Story C: "Import from Google Sheets." Story D: "Import from Salesforce."

**By interface:**
Split based on different interfaces or platforms.
- Original: "As a user, I want to manage my account settings on web and mobile."
- Split: Story A: "Account settings on web." Story B: "Account settings on mobile."

**By operation (CRUD):**
Split based on Create, Read, Update, Delete operations.
- Original: "As an admin, I want to manage team members."
- Split: Story A: "View list of team members (Read)." Story B: "Invite a new team member (Create)." Story C: "Edit a team member's role (Update)." Story D: "Remove a team member (Delete)."

**Splitting rules:**
- Each split story must be independently deployable and testable.
- Each split story should deliver value on its own. "Build the database schema" is not a story -- it is a task within a story.
- After splitting, re-estimate each new story. The sum of split stories often exceeds the original estimate -- that is normal and expected. Splitting reveals hidden complexity.

---

## Output Formats

### Now / Next / Later Roadmap Template

```
ROADMAP — NOW / NEXT / LATER
==============================
Product: _______________
Last updated: _______________
Owner: _______________

NOW (actively building)          NEXT (committed, up next)         LATER (exploring)
-------------------------------- --------------------------------- ---------------------------------
[ ] Theme: _______________       [ ] Theme: _______________        [ ] Theme: _______________
    Owner: ___________               Rough scope: _________            Problem: ______________
    Key deliverable: ____            Depends on: __________
    Target outcome: _____            Target outcome: _____        [ ] Theme: _______________
                                                                      Problem: ______________
[ ] Theme: _______________       [ ] Theme: _______________
    Owner: ___________               Rough scope: _________        [ ] Theme: _______________
    Key deliverable: ____            Depends on: __________            Problem: ______________
    Target outcome: _____            Target outcome: _____
                                                                  [ ] Theme: _______________
                                 [ ] Theme: _______________            Problem: ______________
                                     Rough scope: _________
                                     Target outcome: _____        [ ] Theme: _______________
                                                                      Problem: ______________

RECENTLY SHIPPED:
- [item] — [outcome achieved or pending measurement]
```

### Timeline Roadmap Template

```
TIMELINE ROADMAP
=================
Product: _______________  |  Period: FY 20__
Owner: _______________    |  Last updated: _______________

SWIM LANE: [Team / Product Area]
---------------------------------------------------------------------
Q1                    Q2                    Q3                    Q4
---------------------------------------------------------------------
M: [Milestone]        M: [Milestone]        M: [Milestone]        M: [Milestone]
   Deliverable:          Deliverable:          Deliverable:          Deliverable:
   Success metric:       Success metric:       Success metric:       Success metric:
   Gate:                 Gate:                 Gate:                 Gate:

DEPENDENCIES:
| Milestone | Depends On | Owning Team | RACI | Handoff Date | Status |
|-----------|------------|-------------|------|--------------|--------|
|           |            |             |      |              |        |

MILESTONE GATES:
| Milestone | Gate Criteria | Owner | Status |
|-----------|--------------|-------|--------|
|           |              |       |        |

RISKS & MITIGATIONS:
| Risk | Impact | Probability | Mitigation | Owner |
|------|--------|-------------|------------|-------|
|      |        |             |            |       |
```

### 1-Pager PRD Template

```
1-PAGER PRD
=============
Title: _______________
Author: _______________  |  Date: _______________
Status: Draft / In Review / Approved

PROBLEM
[What is the problem? Who experiences it? How do we know it is real?
 Cite evidence: user research, support tickets, analytics.]

PROPOSED SOLUTION
[How does it work from the user's perspective? Core flow in plain language.
 Include wireframe or sketch if helpful.]

SUCCESS METRICS
1. [Metric]: from [baseline] to [target] within [timeframe]
2. [Metric]: from [baseline] to [target] within [timeframe]
3. [Metric]: from [baseline] to [target] within [timeframe]

SCOPE
In:
-
-
-

Out:
- [item] — [reason]
- [item] — [reason]

KEY RISKS
- [Risk]: [Mitigation]
- [Risk]: [Mitigation]

OPEN QUESTIONS
- [Question]: [Owner, deadline]
- [Question]: [Owner, deadline]
```

### Full PRD Template

```
PRODUCT REQUIREMENTS DOCUMENT
===============================
Title: _______________
Author: _______________  |  Date: _______________
Version: ___  |  Status: Draft / In Review / Approved / Archived
Approvers: [Name, Role] | [Name, Role] | [Name, Role]

1. BACKGROUND & STRATEGIC CONTEXT
   Business context:
   Market context:
   Customer context:
   Link to OKR:

2. USER STORIES
   Story 1: As a [persona], I want [action], so that [outcome].
     AC-1: Given [context], when [action], then [result].
     AC-2: Given [context], when [action], then [result].

3. FUNCTIONAL REQUIREMENTS
   FR-1:
   FR-2:
   FR-3:

4. NON-FUNCTIONAL REQUIREMENTS
   Performance:
   -
   Security:
   -
   Accessibility (WCAG 2.1 AA):
   -
   Internationalization:
   -

5. TECHNICAL CONSIDERATIONS
   API Contracts:
     [Endpoint]: [Method] [Path]
       Request: [Schema]
       Response: [Schema]
       Errors: [Codes]

   Data Model Changes:
     [Table]: [Fields, types, constraints]
     Migration: [Plan]
     Rollback: [Plan]

6. EDGE CASES
   - [Case]: [Expected behavior]
   (aim for 10+)

7. ANALYTICS INSTRUMENTATION
   | Event | Trigger | Properties | Funnel Position |
   |-------|---------|------------|-----------------|
   |       |         |            |                 |

8. ROLLOUT PLAN
   Phase 1: Internal dogfood
     Feature flag:
     Success criteria:
   Phase 2: Beta (X% rollout)
     Monitoring:
     Rollback trigger:
   Phase 3: GA (100%)
     Announcement:
     Support readiness:

9. DEPENDENCIES
   Cross-team:
   -
   Third-party:
   -

10. APPROVALS
    | Approver | Role | Status | Date |
    |----------|------|--------|------|
    |          |      |        |      |
```

### Feature Spec Template

```
FEATURE SPECIFICATION
======================
Feature: _______________
PRD Reference: [Link]
Author: _______________  |  Date: _______________
Status: Draft / In Review / Approved

USER STORIES & ACCEPTANCE CRITERIA:
  Story 1: As a [persona], I want [action], so that [outcome].
    AC-1: Given [context], when [action], then [result].
    AC-2: Given [context], when [action], then [result].

DESIGN:
  Mockups: [Link]
  Interaction specs:
    Hover: _______________
    Loading: _______________
    Empty: _______________
    Error: _______________
  Breakpoints:
    Mobile (<768px): _______________
    Tablet (768-1024px): _______________
    Desktop (>1024px): _______________

TECHNICAL:
  API: [Method] [Path]
    Request: [Schema]
    Response: [Schema]
  Data model: [Changes]
  Performance: [Targets]

EDGE CASES:
  -

ANALYTICS:
  | Event | Trigger | Properties |
  |-------|---------|------------|
  |       |         |            |

ESTIMATION: ___ story points
SPRINT TARGET: Sprint ___
```

### Prioritization Scorecard Template

```
PRIORITIZATION SCORECARD
==========================
Framework: RICE / ICE / MoSCoW / Weighted Scoring
Date: _______________  |  Author: _______________
Decision context: _______________

SCORING:
| Feature | [Dim 1] | [Dim 2] | [Dim 3] | [Dim 4] | Score |
|---------|---------|---------|---------|---------|-------|
|         |         |         |         |         |       |
|         |         |         |         |         |       |
|         |         |         |         |         |       |

RANKED OUTPUT:
1. [Feature] — Score: ___ — Rationale: ___
2. [Feature] — Score: ___ — Rationale: ___
3. [Feature] — Score: ___ — Rationale: ___

DECISION:
  Selected: _______________
  Deferred: _______________
  Rationale: _______________

STAKEHOLDER SIGN-OFF:
  | Name | Role | Agrees? | Notes |
  |------|------|---------|-------|
  |      |      |         |       |
```

### Grooming Tracker Template

```
BACKLOG GROOMING TRACKER
==========================
Sprint: _______________  |  Date: _______________
Facilitator: _______________  |  Team: _______________

SESSION NOTES:
  Items reviewed: ___  |  Items estimated: ___  |  Items split: ___

ESTIMATED ITEMS:
| Item | Story Points | Estimators Agreed? | Notes |
|------|-------------|-------------------|-------|
|      |             |                   |       |
|      |             |                   |       |

SPLIT ITEMS:
| Original Item | Points | Split Into | New Points |
|---------------|--------|-----------|------------|
|               |        |           |            |

ITEMS NEEDING MORE WORK:
| Item | Blocker | Owner | Due By |
|------|---------|-------|--------|
|      |         |       |        |

BACKLOG HEALTH:
  Items groomed (next 2 sprints): ___% (target: >80%)
  Avg age of ungroomed items: ___ weeks (target: <4)
  Velocity (4-sprint avg): ___ points/sprint
  Stories changed post-grooming: ___% (target: <10%)

DEFINITION OF READY CHECK (for top items):
| Item | Story? | ACs? | Design? | Dependencies? | Estimated? | Fits sprint? | No open Qs? | READY? |
|------|--------|------|---------|---------------|------------|-------------|-------------|--------|
|      |        |      |         |               |            |             |             |        |

ACTION ITEMS:
- [ ] [Action] — Owner: ___ — Due: ___
- [ ] [Action] — Owner: ___ — Due: ___
```
