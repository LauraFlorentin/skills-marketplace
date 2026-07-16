# Planning — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

## Contents

- [Resource Planning](#resource-planning)
- [Risk Management](#risk-management)
- [Communication Planning](#communication-planning)
- [Putting It All Together](#putting-it-all-together)

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
