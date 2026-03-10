# Initiation — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Kickoff Planning

The kickoff meeting is the project's first impression. It sets the tone for collaboration, establishes shared understanding, and creates momentum. A bad kickoff -- information dump, no discussion, unclear next steps -- can undermine a project before it starts.

### Kickoff Agenda: 60-Minute Version

Use this for standard projects with 8-20 stakeholders.

```
PROJECT KICKOFF AGENDA (60 minutes)
====================================
Project: _______________
Date: _______________  |  Location/Link: _______________
Facilitator: [PM Name]

TIME    TOPIC                              OWNER        DURATION
------  ---------------------------------  -----------  --------
0:00    Welcome and Introductions          PM           5 min
        - Each person: Name, role, one
          sentence on what success looks
          like for them

0:05    Project Overview                   Sponsor      10 min
        - Why this project exists (the
          business case in 2 minutes)
        - What success looks like from
          the sponsor's perspective
        - How this project fits into
          broader organizational strategy

0:15    Scope and Objectives               PM           10 min
        - What is in scope (specific
          deliverables)
        - What is out of scope (name it)
        - Key objectives and success
          criteria
        - Assumptions and constraints

0:25    Roles, Governance, and             PM           10 min
        Decision-Making
        - RACI overview (who decides what)
        - Steering committee structure
          and cadence
        - Escalation path
        - How decisions are made (consensus
          vs. sponsor decides vs. PM decides)

0:35    Key Milestones and Timeline        PM           5 min
        - High-level timeline with
          3-5 major milestones
        - Phase gate criteria
        - Known hard deadlines

0:40    Communication Plan                 PM           5 min
        - Meeting cadence (standup,
          weekly status, steering)
        - Status report format and
          distribution
        - Tools (Slack channel, Jira board,
          shared drive, email list)
        - How to raise issues or blockers

0:45    Top Risks and Open Questions       PM           5 min
        - 3-5 known risks from the charter
        - Open questions that need answers
          in the first 2 weeks
        - Who owns each open question

0:50    Q&A and Discussion                 All          8 min
        - Open floor for questions,
          concerns, and input
        - Capture action items from
          discussion

0:58    Next Steps and Close               PM           2 min
        - Recap key decisions made
        - List action items with owners
          and due dates
        - Confirm next meeting date
        - Thank everyone for their time
```

### Kickoff Agenda: 30-Minute Version

Use this for smaller projects (3-8 people), internal initiatives, or teams that already work together.

```
PROJECT KICKOFF AGENDA (30 minutes)
====================================
Project: _______________
Date: _______________  |  Location/Link: _______________
Facilitator: [PM Name]

TIME    TOPIC                              OWNER        DURATION
------  ---------------------------------  -----------  --------
0:00    Quick Introductions (if needed)    PM           2 min

0:02    Why We Are Here                    Sponsor/PM   5 min
        - Problem we are solving
        - Expected outcome
        - How this connects to team/org
          goals

0:07    Scope, Objectives, Success         PM           5 min
        Criteria
        - In scope / out of scope
        - 3-5 objectives
        - How we will measure success

0:12    Roles and Working Agreements       PM           5 min
        - Who does what
        - Decision-making process
        - Meeting cadence
        - Communication channels

0:17    Timeline and Key Milestones        PM           3 min
        - High-level timeline
        - Next 2-week plan in detail

0:20    Risks and Open Questions           PM           3 min
        - Top 3 risks
        - Questions that need answers
          this week

0:23    Discussion                         All          5 min

0:28    Next Steps and Close               PM           2 min
        - Action items with owners
        - Next meeting date
```

### Software Mode: Kickoff Additions

For software projects, add a technical block after the standard kickoff or schedule a separate 30-minute technical kickoff within the first week.

**Tech Stack Walkthrough (10 min):**
- Languages, frameworks, and key libraries
- Infrastructure: cloud provider, deployment targets, environments (dev/staging/prod)
- Key third-party services and APIs

**Dev Environment Setup (5 min or link to setup guide):**
- Repository location and access
- Local development prerequisites
- How to run the application locally
- How to run tests
- Link to setup documentation (wiki/README)

**CI/CD Overview (5 min):**
- Build pipeline stages (lint, test, build, deploy)
- How deployments work (automated vs. manual promotion)
- Rollback procedure
- Environment promotion path (dev -> staging -> prod)

**Branching Strategy (5 min):**
- Branch naming convention (e.g., `feature/TICKET-123-short-description`)
- Main/trunk branch policy
- Pull request requirements (reviewers, CI checks, approvals)
- Release branch strategy (if applicable)

**On-Call Expectations (3 min):**
- Will this project add on-call responsibilities?
- Who is on the rotation?
- Escalation path for production incidents
- Expected response times

**Code Review Norms (2 min):**
- Turnaround time expectation (e.g., <24 hours for reviews)
- Review checklist or standards link
- How to handle disagreements in reviews
- Pair programming or mob programming norms (if applicable)

### General Mode: Kickoff Additions

For non-software projects, the kickoff should emphasize organizational context, governance, and human factors.

**Project Overview Deep-Dive:** Full business case walkthrough, connection to organizational strategy, and cost of inaction if the project does not succeed.

**Governance Walkthrough:** Steering committee membership and schedule, approval authorities and decision rights, change control process, and reporting requirements.

**Communication Plan Preview:** Who gets what information, how often, in what format. Escalation triggers. Feedback mechanisms.

**Roles and Responsibilities:** Walk through the RACI for major deliverables. Clarify gray areas between PM and sponsor authority. Confirm time commitments from each team member.

**Key Milestones with Decision Gates:** Each milestone has a go/no-go gate with criteria and a designated decision-maker.

**Decision-Making Process:** PM decides operational matters. Sponsor decides scope, budget, and timeline changes. Consensus items are identified explicitly. Tie-breaking authority is assigned before it is needed.

### Pre-Kickoff Checklist

Complete these items before the kickoff meeting. Walking into a kickoff unprepared is worse than not having one at all.

- [ ] **Charter is drafted and reviewed by sponsor.** You do not need final sign-off before kickoff, but the sponsor should have seen and agreed to the direction.
- [ ] **Stakeholder register is complete.** You know who needs to be in the room (and who does not). Everyone on the invite list has context on why they are included.
- [ ] **Agenda is distributed 3+ business days in advance.** Attendees know what will be covered, what is expected of them, and how long it will take.
- [ ] **Pre-read materials are sent.** If attendees need to review the charter, business case, or background documents before the meeting, send them with the agenda. Highlight what specifically to read (do not send a 50-page deck with no guidance).
- [ ] **Room/meeting link is booked and tested.** For virtual meetings: test screen sharing, confirm calendar invites are correct, have a backup dial-in number. For in-person: confirm room has a projector, whiteboard, and enough seats.
- [ ] **Facilitator is prepared.** The PM has rehearsed the agenda, knows who will present each section, has backup plans if a key attendee is absent, and has prepared for likely questions.
- [ ] **Risk register has initial entries.** At least 3-5 risks identified from the charter to seed the discussion.
- [ ] **Action item tracker is ready.** Have a system (spreadsheet, Jira board, shared doc) ready to capture action items in real time during the meeting.
- [ ] **Success criteria are defined.** Before walking into the room, you should know what a successful kickoff looks like: attendees leave with a shared understanding of scope, timeline, and roles.
- [ ] **Parking lot is ready.** Have a place to capture topics that come up but are out of scope for the kickoff. This prevents derailment while respecting that people's concerns are valid.

### Post-Kickoff Follow-Up Template

Send this within 24 hours of the kickoff. Speed matters -- it demonstrates that the project is being managed with rigor from day one.

```
POST-KICKOFF SUMMARY
=====================
Project: _______________
Kickoff Date: _______________
Prepared By: [PM Name]
Distribution: [All kickoff attendees + stakeholders who could not attend]

DECISIONS MADE:
| # | Decision | Made By | Date |
|---|----------|---------|------|
| 1 | [e.g., "Project will use Agile methodology with 2-week sprints"] | [Sponsor] | [Date] |
| 2 | [e.g., "Scope limited to North America region for Phase 1"] | [PM + Sponsor] | [Date] |
| 3 | ___ | ___ | ___ |

ACTION ITEMS:
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | [e.g., "Set up Jira project and Slack channel"] | [PM] | [Date] | Not Started |
| 2 | [e.g., "Provide vendor shortlist for procurement review"] | [Business Lead] | [Date] | Not Started |
| 3 | [e.g., "Schedule security review with InfoSec team"] | [Tech Lead] | [Date] | Not Started |
| 4 | [e.g., "Confirm budget allocation with Finance"] | [Sponsor] | [Date] | Not Started |
| 5 | ___ | ___ | ___ | ___ |

KEY DATES CONFIRMED:
- Sprint 1 begins: [Date]
- First status report: [Date]
- First steering committee: [Date]
- Phase 1 milestone: [Date]

OPEN QUESTIONS (from Parking Lot):
| # | Question | Owner to Resolve | Target Date |
|---|----------|-----------------|-------------|
| 1 | [e.g., "Can we access the legacy database directly or do we need an API wrapper?"] | [Tech Lead] | [Date] |
| 2 | [e.g., "Is the training budget separate from the project budget?"] | [Finance Rep] | [Date] |
| 3 | ___ | ___ | ___ |

NEXT STEPS:
- [PM] will distribute the project schedule by [Date]
- [Team] will begin Sprint 1 / Phase 1 on [Date]
- Next team meeting: [Date, Time, Location/Link]
- Steering committee #1: [Date, Time, Location/Link]

ATTACHMENTS:
- Project Charter v[X]
- Stakeholder Register
- Risk Register (initial)
- Communication Plan

If you have questions or corrections to this summary, reply to this email
by [Date]. Silence will be taken as agreement.
```

### Kickoff Anti-Patterns

**Information Dump With No Discussion**
- Symptom: The PM presents 40 slides for 55 minutes and asks "Any questions?" with 2 minutes left. Nobody speaks.
- Impact: Attendees leave overwhelmed and unengaged. They did not internalize the information. They do not feel ownership. Issues and concerns go unvoiced.
- Fix: Limit presentation to 60-70% of the total meeting time. Reserve 30-40% for discussion, questions, and working through concerns. A kickoff is a conversation, not a lecture. If you have more content than time allows, send the detail as pre-read and use the meeting for discussion.

**Skipping Introductions**
- Symptom: The PM jumps straight into content because "everyone knows each other."
- Impact: New team members feel excluded. People who do not know each other stay silent. Cross-functional attendees do not understand each other's roles or perspectives.
- Fix: Always do introductions, even if the team has worked together before. For returning teams, use a one-sentence prompt: "Name, role, and one thing you want to make sure we get right on this project." For new teams, add: "One thing about your experience that is relevant to this project." This takes 5 minutes and dramatically improves engagement.

**No Clear Next Steps**
- Symptom: The kickoff ends with "Great meeting, let's get started!" No action items are assigned. No dates are set. No follow-up is sent.
- Impact: Momentum dies within 48 hours. Nobody knows what to do first. The next meeting does not happen for 2 weeks because nobody scheduled it.
- Fix: End every kickoff with a concrete list of action items, each with an owner and a due date. Schedule the next meeting before people leave the room. Send the post-kickoff summary within 24 hours.

**Wrong People in the Room**
- Symptom: The kickoff includes 30 people, most of whom are tangentially involved. Or the kickoff is missing a critical stakeholder who later derails the project.
- Impact: Too many people turns the kickoff into a performance rather than a working session. Missing people means decisions are made without key input and must be revisited.
- Fix: Use the stakeholder register to determine the invite list. "Manage Closely" stakeholders attend. "Keep Satisfied" stakeholders get a summary. If you are unsure whether someone should attend, ask them: "Would a post-meeting summary work for you, or do you need to be in the room?"

**Skipping the "Why"**
- Symptom: The kickoff dives into timelines, Jira boards, and technical details without first explaining why the project exists and why it matters.
- Impact: The team executes tasks without understanding the purpose. When trade-offs arise, they make poor decisions because they do not know what the project is trying to achieve.
- Fix: The sponsor should spend the first 5-10 minutes on the "why." Why does this project exist? What problem are we solving? What happens if we do nothing? This is not a formality -- it is the foundation of every decision the team will make.
