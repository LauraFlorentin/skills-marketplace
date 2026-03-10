---
name: planning
description: Roadmaps, PRDs, feature specifications, prioritization frameworks, and backlog grooming for startup and enterprise PMs — Now/Next/Later, timeline roadmaps, lean and full PRDs, RICE/ICE/MoSCoW scoring, and sprint-ready backlogs. Use when user asks to "create a roadmap", "write a PRD", "prioritize features", or mentions product requirements, backlog grooming, user stories, or RICE scoring.
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

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/planning-reference.md`](references/planning-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- PRDs
- Feature Specs
- Prioritization
- Backlog Grooming
- Output Formats

