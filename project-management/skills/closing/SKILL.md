---
name: closing
description: Retrospectives, lessons learned, and project closeout for software and general PMs Use when user asks to "run a retrospective", "close out the project", "lessons learned", or mentions post-mortem, project handoff, or release notes.
triggers:
  - retrospective
  - retro
  - lessons learned
  - post-mortem
  - project closeout
  - project close
  - handoff
  - release notes
  - wrap up
---

# Closing

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

---

## Retrospectives

Retrospectives are the single most important continuous improvement practice a team can adopt. A well-run retro surfaces friction, celebrates wins, and produces concrete action items that make the next cycle better. The difference between a useful retro and a time-waster is format selection, facilitation discipline, and follow-through.

### Retro Format 1: Start / Stop / Continue

Best for new teams or teams running their first retro. Three intuitive columns requiring no explanation.

**When to use:** New teams, first retro with a group, or when you want a lightweight format under 45 minutes.

```
RETROSPECTIVE — START / STOP / CONTINUE
=========================================
Sprint/Phase: _______________    Date: _______________
Facilitator: _______________     Attendees: _______________

START (begin doing)                      STOP (stop doing)                        CONTINUE (keep doing)
-------------------------------------   -------------------------------------    -------------------------------------
1. ________________________________     1. ________________________________     1. ________________________________
2. ________________________________     2. ________________________________     2. ________________________________
3. ________________________________     3. ________________________________     3. ________________________________
4. ________________________________     4. ________________________________     4. ________________________________
5. ________________________________     5. ________________________________     5. ________________________________

ACTION ITEMS:
| # | Action                        | Owner          | Due Date   | Status     |
|---|-------------------------------|----------------|------------|------------|
| 1 |                               |                |            | Open       |
| 2 |                               |                |            | Open       |
| 3 |                               |                |            | Open       |
```

**Worked example (software team, Sprint 14):**

```
START                                    STOP                                     CONTINUE
-------------------------------------   -------------------------------------    -------------------------------------
1. Pair programming on complex tasks    1. Deploying on Fridays                  1. Daily standups at 9:15am
2. Writing ADRs for arch decisions      2. Skipping code review for "small" PRs  2. Mob debugging for prod issues
3. Sprint goal visible on team board    3. Adding scope mid-sprint               3. Demo day every other Friday
4. Automated regression before merge    4. Slack DMs for team-wide decisions     4. Rotating scrum master role

ACTION ITEMS:
| # | Action                                   | Owner  | Due Date   | Status |
|---|------------------------------------------|--------|------------|--------|
| 1 | Create ADR template in repo wiki         | Sarah  | 2026-03-09 | Open   |
| 2 | Add CI gate: regression suite must pass  | Dev    | 2026-03-16 | Open   |
| 3 | Update team agreement: no Friday deploys | Marcus | 2026-03-06 | Open   |
```

### Retro Format 2: Mad / Sad / Glad

An emotional temperature check that surfaces how the team feels, not just what happened. Useful after stressful phases, incidents, or when morale feels low.

**When to use:** After a stressful sprint, post-incident, or when you want emotional honesty before process fixes.

```
RETROSPECTIVE — MAD / SAD / GLAD
==================================
Sprint/Phase: _______________    Date: _______________
Facilitator: _______________     Attendees: _______________

MAD (frustrated about)                   SAD (disappointed about)                 GLAD (happy about)
-------------------------------------   -------------------------------------    -------------------------------------
1. ________________________________     1. ________________________________     1. ________________________________
2. ________________________________     2. ________________________________     2. ________________________________
3. ________________________________     3. ________________________________     3. ________________________________
4. ________________________________     4. ________________________________     4. ________________________________

THEMES: _________________________________________________________________________
ACTION ITEMS:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 |        |       |          | Open   |
| 2 |        |       |          | Open   |
| 3 |        |       |          | Open   |
```

**Worked example (general PM, Phase 2 closeout):**

```
MAD                                      SAD                                      GLAD
1. Stakeholder changed reqs 3 times     1. Lost 2 team members mid-phase         1. Client loved the final deliverable
2. No one read status reports           2. Missed vendor deadline by 1 week       2. New risk process caught 2 issues
3. Budget approval took 4 weeks         3. Training materials were rushed          3. Team collaboration was excellent

THEMES: Scope instability, resource churn, strong team culture despite obstacles
```

### Retro Format 3: 4Ls (Liked / Learned / Lacked / Longed For)

Four columns capturing positive experiences and unmet needs. "Lacked" identifies concrete gaps; "Longed For" captures aspirational improvements.

**When to use:** Mature teams wanting more nuance. Good for end-of-project retros requiring thorough experience capture.

```
RETROSPECTIVE — 4Ls
=====================
Sprint/Phase/Project: _______________    Date: _______________
Facilitator: _______________             Attendees: _______________

LIKED (went well)                LEARNED (new knowledge)           LACKED (was missing)              LONGED FOR (wish we had)
-------------------------------  --------------------------------  --------------------------------  --------------------------------
1. ___________________________  1. ___________________________   1. ___________________________   1. ___________________________
2. ___________________________  2. ___________________________   2. ___________________________   2. ___________________________
3. ___________________________  3. ___________________________   3. ___________________________   3. ___________________________
4. ___________________________  4. ___________________________   4. ___________________________   4. ___________________________

ACTION ITEMS:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 |        |       |          | Open   |
| 2 |        |       |          | Open   |
| 3 |        |       |          | Open   |
```

**Worked example (software team, end of Q4 release):**

```
LIKED                            LEARNED                           LACKED                            LONGED FOR
1. Feature flag rollout smooth   1. Canary deploys catch staging   1. Load testing before launch     1. Dedicated QA engineer
2. Team morale stayed high          misses                         2. Clear ownership of shared      2. Better observability tooling
3. New CI cut build time 40%     2. Infra estimates need 1.5x        services                       3. A full sprint for tech debt
4. Cross-team API collab great      buffer                         3. Onboarding docs for hires         every quarter
                                 3. Stakeholder demos reduce       4. Automated rollback capability  4. More async, fewer meetings
                                    late-stage surprises
```

### Retro Format 4: Sailboat (Wind / Anchor / Rocks / Island)

A visual metaphor where the project is a sailboat. **Wind** = what propelled us forward (tailwinds, accelerators). **Anchor** = what held us back (drag, friction). **Rocks** = risks and obstacles ahead. **Island** = our destination/goal for the next phase.

**When to use:** Teams that respond well to metaphor. Good for remote teams on shared whiteboards (Miro, FigJam). Shifts conversation from backward-looking to forward-looking.

```
RETROSPECTIVE — SAILBOAT
==========================
Sprint/Phase: _______________    Date: _______________
Facilitator: _______________     Attendees: _______________

WIND (propelled us forward)              ANCHOR (held us back)
-------------------------------------   -------------------------------------
1. ________________________________     1. ________________________________
2. ________________________________     2. ________________________________
3. ________________________________     3. ________________________________

ROCKS (risks/obstacles ahead)            ISLAND (our destination/goal)
-------------------------------------   -------------------------------------
1. ________________________________     1. ________________________________
2. ________________________________     2. ________________________________
3. ________________________________     3. ________________________________

ACTION ITEMS:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 |        |       |          | Open   |
| 2 |        |       |          | Open   |
| 3 |        |       |          | Open   |
```

### Retro Format 5: Timeline Retro

Walk through the project chronologically, annotating each phase. Especially powerful for longer efforts where the team may have forgotten early-phase events.

**When to use:** End-of-project retros, release retros, or any retro spanning more than 4 weeks. Requires prep (facilitator should prepare a timeline of key events).

```
RETROSPECTIVE — TIMELINE
==========================
Project/Release: _______________    Date: _______________
Facilitator: _______________        Attendees: _______________

PHASE 1: _____________ (dates: _____ to _____)
  Went well: 1. ___________________  2. ___________________
  Did not go well: 1. ___________________  2. ___________________
  Key events: _____________________________________________________________

PHASE 2: _____________ (dates: _____ to _____)
  Went well: 1. ___________________  2. ___________________
  Did not go well: 1. ___________________  2. ___________________
  Key events: _____________________________________________________________

PHASE 3: _____________ (dates: _____ to _____)
  Went well: 1. ___________________  2. ___________________
  Did not go well: 1. ___________________  2. ___________________
  Key events: _____________________________________________________________

CROSS-CUTTING THEMES:
1. ___________________________  2. ___________________________  3. ___________________________

ACTION ITEMS:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 |        |       |          | Open   |
| 2 |        |       |          | Open   |
| 3 |        |       |          | Open   |
```

---

### Retro Facilitation Guide

Total time: 50 minutes.

| Phase         | Duration | Activity                                                                                         |
|---------------|----------|--------------------------------------------------------------------------------------------------|
| Setup         | 5 min    | State format, ground rules, and time-boxes. Remind: no blame, focus on systems, everything stays here. |
| Generate      | 10 min   | Silent brainstorming. Everyone writes sticky notes for each column. No discussion yet (prevents anchoring). |
| Cluster       | 5 min    | Facilitator groups similar items into themes. Read each cluster aloud and confirm grouping.        |
| Vote          | 5 min    | Each person gets 3 dots. Vote silently on themes to discuss. Tally and rank.                      |
| Discuss       | 20 min   | Discuss top 2-3 themes. For each: root cause, what can we change, who owns the action, due date.  |
| Action Items  | 5 min    | Summarize all action items aloud. Confirm owner and due date. These get reviewed at next retro.   |

**Ground rules (read aloud at every retro):**
1. We examine systems and processes, not people.
2. Assume everyone did their best with the information they had.
3. What is said in retro stays in retro (unless the group agrees to share outward).
4. Everyone's voice matters equally -- junior and senior alike.
5. We leave with action items, not just complaints.

### Software Mode: Sprint, Release, and Incident Retros

**Sprint Retrospective (every 2 weeks):** Use Start/Stop/Continue or Mad/Sad/Glad. 45 minutes. Focus on last 2 weeks only. Carry forward unresolved items from previous retro.

**Release Retrospective (after each release):** Use Timeline or 4Ls. Include full release team (dev, QA, design, product, DevOps). Cover entire release cycle. 60-90 minutes.

**Incident Post-Mortem (separate format):** Not a retro -- a distinct root-cause-focused format. Run within 48 hours of resolution.

```
INCIDENT POST-MORTEM
======================
Incident ID: ___________  Title: ___________  Severity: P1/P2/P3/P4
Date: ___________  Duration: ___________  Post-Mortem Date: ___________
Facilitator: ___________  Attendees: ___________

EXECUTIVE SUMMARY: [2-3 sentences: what happened, who was affected, how resolved]

TIMELINE:
| Time (UTC) | Event                                            | Actor           |
|------------|--------------------------------------------------|-----------------|
| HH:MM      | [First detection / alert fired]                  | [person/system] |
| HH:MM      | [Incident declared, on-call paged]               |                 |
| HH:MM      | [Initial diagnosis / hypothesis]                 |                 |
| HH:MM      | [First mitigation attempt]                       |                 |
| HH:MM      | [Root cause identified]                          |                 |
| HH:MM      | [Fix deployed / rollback executed]               |                 |
| HH:MM      | [Incident resolved, monitoring confirms recovery]|                 |

ROOT CAUSE: [Detailed technical explanation]

CONTRIBUTING FACTORS:
1. ________________  2. ________________  3. ________________

CUSTOMER IMPACT:
- Users affected: ______  Revenue impact: ______  Data loss: Yes/No
- SLA breach: Yes/No     Support tickets: ______

WHAT WENT WELL: 1. ________________  2. ________________
WHAT COULD IMPROVE: 1. ________________  2. ________________

ACTION ITEMS:
| # | Action | Owner | Priority | Due Date | Status |
|---|--------|-------|----------|----------|--------|
| 1 |        |       | P1/P2    |          | Open   |
| 2 |        |       | P1/P2    |          | Open   |
| 3 |        |       | P1/P2    |          | Open   |

FOLLOW-UP REVIEW DATE: ___________  OWNER: ___________
```

### General Mode: Phase-End and Project Retros

**Phase-End Review:** At each major phase completion (Discovery, Design, Build, Test, Launch). Use 4Ls or Sailboat. Include full phase team. Focus on what the next phase needs to know. 60 minutes.

**Project Milestone Retro:** At significant milestones (50% complete, major deliverable accepted). Use Start/Stop/Continue. 30 minutes. Focus on course correction.

**End-of-Project Retro:** Within 2 weeks of completion. Use Timeline format. Include all key team members and stakeholders. 90 minutes. Feeds directly into the formal Lessons Learned session.

**Formal Lessons Learned Session:** A structured meeting (separate from retro) producing documentation for organizational knowledge management. See Lessons Learned section below.

### Retro Anti-Patterns

| Anti-Pattern                       | What It Looks Like                                                      | Fix                                                                            |
|------------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| Blame sessions                     | "John broke the build" instead of "our CI process has a gap"            | Enforce ground rule 1. Redirect blame to process.                              |
| No action items                    | 45 min discussion, nothing written down                                 | Reserve last 5 min for action items. No items = failed retro.                  |
| Same issues every retro            | "Communication is bad" for the 5th consecutive time                     | Make it concrete: what specifically changes, who owns it, by when?             |
| Only negative feedback             | Every note is a complaint                                               | Start with positives. Celebrate wins before addressing problems.               |
| Manager dominates                  | Manager talks 70% of the time                                           | Manager speaks last. Use silent brainstorming before discussion.               |
| No follow-through                  | Last retro's action items were never reviewed                           | Start every retro by reviewing previous action items.                          |
| Retro skipped for time pressure    | "Too busy for retro this sprint"                                        | This is when you need it most. Even 15-minute mini-retro beats nothing.        |

### Action Item Tracking Template

```
RETRO ACTION ITEM TRACKER
============================
Team: _______________  Updated: _______________

| ID    | Action                                    | Owner     | Due Date   | Status      | Follow-up Retro |
|-------|-------------------------------------------|-----------|------------|-------------|-----------------|
| R14-1 | Create ADR template in repo wiki          | Sarah     | 2026-03-09 | Complete    | Sprint 15       |
| R14-2 | Add CI gate for regression suite          | Dev       | 2026-03-16 | In Progress | Sprint 15       |
| R14-3 | Update team agreement: no Friday deploys  | Marcus    | 2026-03-06 | Complete    | Sprint 15       |
| R15-1 | Schedule load testing for Q2 release      | QA Lead   | 2026-03-23 | Open        | Sprint 16       |
```

**Rules:** Every action has exactly one owner (not "the team"). Every action has a due date (not "soon"). Status: Open / In Progress / Complete / Cancelled. Review all open items at the start of the next retro.

### Tips for Psychological Safety in Retros

1. **Normalize vulnerability.** Facilitator models it: "Here is something I could have done better this sprint."
2. **Use anonymous input for sensitive topics.** Allow anonymous sticky notes or use tools with anonymous mode (EasyRetro, Retrium).
3. **Separate retros from performance reviews.** Never use retro content to evaluate individuals.
4. **Address power dynamics.** If a VP is present, juniors will self-censor. Run retros without skip-level leadership, or use anonymous input.
5. **Follow through on action items.** Nothing destroys retro trust faster than ignored action items.
6. **Celebrate the retro itself.** "Remember when we identified the Friday deploy problem? We haven't had a weekend incident since."
7. **Rotate the facilitator.** Rotation gives everyone ownership and brings different styles.

---

## Lessons Learned

The challenge is not capturing lessons -- most teams can fill a page after any project. The challenge is making lessons specific enough to be actionable and embedded in workflow so future teams actually find and use them.

### Lessons Learned Template

```
LESSONS LEARNED REGISTER
==========================
Project: _______________  Date: _______________  Facilitator: _______________

| # | Category      | What Happened                          | Impact | Root Cause                        | Lesson                                         | Recommendation                                       | Applicable To     |
|---|---------------|----------------------------------------|--------|-----------------------------------|-------------------------------------------------|------------------------------------------------------|--------------------|
| 1 | Planning      | Estimated 6 weeks; took 11 weeks       | H      | No spike for unknowns; optimism   | New-tech estimates need 1.5-2x buffer           | Add mandatory spike tasks for new technology          | Team-wide          |
| 2 | Execution     | 3 critical bugs found in production    | H      | No load testing in pre-prod       | Load testing must be in release checklist        | Add load test gate to CI/CD before prod deploy        | Org-wide           |
| 3 | Communication | Stakeholder surprised by delay         | M      | Status reports went to wrong DL   | Verify distribution list at kickoff              | PM confirms stakeholder email list in week 1          | Team-wide          |
| 4 | Technical     | Microservice coupling caused cascade   | H      | Shared database, no circuit break | Shared DBs create hidden coupling                | Enforce service-owns-its-data pattern                 | Org-wide           |
| 5 | Process       | Code reviews took 3-5 days average     | M      | No SLA, no reviewer rotation      | Review SLAs must be explicit                     | Set 24-hour review SLA, auto-assign reviewers         | This project only  |
```

**Column definitions:** Category = Planning / Execution / Communication / Technical / Process. Impact = H (schedule slip, budget overrun, customer impact), M (rework, team friction), L (minor inconvenience). Root Cause = use 5-Whys if needed. Applicable To = This project only / Team-wide / Org-wide.

### Collection Methods

1. **Retro synthesis:** Review all retro themes across the project. If the same issue appeared in 3+ retros, it is systemic.
2. **1:1 stakeholder interviews:** 20-30 min with sponsor, product owner, tech lead. People share more candid feedback privately.
3. **Metrics review:** Compare planned vs. actual schedule, budget, velocity, defect rates, CSAT. Numbers need context but do not lie.
4. **Anonymous team survey:** Short 10-question survey with Likert-scale and open-text. Useful for large teams (10+) or low trust.
5. **Project timeline review:** Walk the plan comparing planned vs. actual milestones. At each variance: "Why? What does this tell us?"

### Software Mode: Technical and Process Lessons

**Technical lessons to capture:**

| Area                   | Questions to Ask                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------------------|
| Architecture decisions | Which proved correct? Which would we reverse? What data would have changed our mind?                     |
| Tooling choices        | Did tooling help or hinder? What to add, replace, or remove?                                             |
| Testing strategy       | Did coverage catch the bugs that mattered? Where did testing fail? Was the test pyramid balanced?         |
| Deployment improvements| How smooth were deploys? What broke? What manual steps should be automated?                               |
| Monitoring gaps        | Did we detect issues before customers? Where were observability blind spots?                              |

**Process lessons to capture:**

| Area                   | Questions to Ask                                                                                         |
|------------------------|----------------------------------------------------------------------------------------------------------|
| Estimation accuracy    | How did estimates compare to actuals? Consistently over or under? By what factor?                        |
| Sprint cadence         | Was 2-week length right? Did we deliver working software every sprint?                                   |
| Code review quality    | Reviews thorough or rubber-stamped? Did they catch real issues? Turnaround acceptable?                   |
| Incident response      | How quickly did we detect, respond, resolve? Where were bottlenecks?                                     |

### General Mode: Non-Technical Lessons

**Planning accuracy:** Compare original plan (scope, schedule, budget, resources) against actuals. Where were assumptions wrong?
**Risk management effectiveness:** Which risks materialized? Were mitigations effective? What was missed entirely?
**Stakeholder management:** Right stakeholders engaged at the right time? Expectations managed? Surprises at project end?
**Vendor management:** On-time delivery? Contract protections adequate? Proactive or reactive relationship management?
**Communication effectiveness:** Right information to right people at right time? Status reports useful or ignored?
**Budget management:** Realistic budget? Where did overruns occur? Contingency reserves used appropriately?
**Change management:** Plan effective? Adoption achieved? Resistance patterns anticipated?

### Knowledge Management: Storing and Surfacing Lessons

**Tagging:** Every lesson tagged with project type, technology stack, team size, industry/domain, and lesson category.

**Searchability:** Store in a system supporting full-text search (wiki, tagged spreadsheet, dedicated database). A folder of PDFs does not work.

**Review cadence:**
- **Project kickoff:** PM reviews lessons database for similar past projects. Share 3-5 relevant lessons at kickoff.
- **Quarterly:** PMO/engineering leadership reviews new lessons, identifies org-wide patterns requiring systemic changes.
- **Annually:** Lessons-learned retrospective across all projects. Publish top 10 organizational lessons.

```
LESSON CARD
=============
Title: [Short title — e.g., "Shared databases create hidden service coupling"]
Project: [Source project]  Date: [Captured]  Category: [Planning/Execution/Communication/Technical/Process]
Tags: [microservices, architecture, coupling, database]  Applicable To: [Org-wide]

CONTEXT: [2-3 sentences describing the situation]
LESSON: [1-2 sentences stating what we learned]
RECOMMENDATION: [Specific action for future projects]
EVIDENCE: [Metrics or data supporting this, if available]
```

### Lessons Learned Session Facilitation Guide (60-Minute Format)

| Phase                 | Duration | Activity                                                                                                      |
|-----------------------|----------|---------------------------------------------------------------------------------------------------------------|
| Opening               | 5 min    | State purpose: "Capture what we learned so future teams benefit." Ground rules: no blame, be specific.         |
| Individual reflection | 10 min   | Silent writing. One lesson per note. Prompt: "What worked? What didn't? What surprised you?"                   |
| Share and cluster     | 15 min   | Each person reads notes aloud. Facilitator groups by theme. Similar lessons clustered together.                 |
| Deep dive             | 20 min   | Per cluster: root cause, recommendation, who should this apply to? Document in Lessons Learned Register format. |
| Prioritize and assign | 5 min    | Rank by impact. Identify top 5 to publish. Assign owner to finalize each lesson card.                          |
| Close                 | 5 min    | Summarize takeaways. Confirm storage location. State when published lessons will be available.                  |

### Lessons Learned Anti-Patterns

| Anti-Pattern                          | What It Looks Like                                          | Fix                                                                                     |
|---------------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Captured but never referenced         | Beautiful Confluence page no one reads                      | Build lesson review into project kickoff checklist as a gate, not a suggestion.          |
| Blame-oriented lessons                | "John should have tested more"                              | Enforce "systems, not people." Rewrite any lesson naming an individual.                  |
| Too generic to be actionable          | "Communication could be better"                             | "What specifically would you change? Can a future PM act on this?" Rewrite if not.       |
| Only captured at the end              | All lessons collected final week, memory fuzzy              | Capture continuously at retros, milestones, phase gates. End session synthesizes.        |
| No ownership of recommendations       | "We should improve testing" with no assignee                | Every recommendation needs an owner and deadline.                                        |

---

---

## References

For detailed templates, frameworks, and field-level guidance, read:

- [`references/closing-reference.md`](references/closing-reference.md) — Complete framework details, templates, and examples

Read this file when the task requires:
- Project Closeout
- Quick Reference: Which Format When
- Workflow Overview

