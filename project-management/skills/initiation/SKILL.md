---
name: initiation
description: Project charters, stakeholder mapping, and kickoff planning for software and general PMs
triggers:
  - project charter
  - stakeholder map
  - stakeholder analysis
  - kickoff
  - kickoff meeting
  - project setup
  - new project
  - project scope
---

# Initiation

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

---

## Project Charter

A project charter is the single document that authorizes a project to exist. It defines the why, the what, and the who at a level sufficient to secure funding, align stakeholders, and give the project manager authority to act. Without a signed charter, a project is just an idea with no organizational commitment behind it.

The charter should be concise -- one to three pages maximum. It is not the project plan. It is the agreement that a project plan should be created. Teams that confuse charters with plans end up with 30-page documents nobody reads and nobody signs.

### Software Mode

For software projects, the charter must address technical realities that directly affect feasibility and delivery. Skip these and you will discover them mid-sprint, when the cost of change is highest.

#### Technical Feasibility Assessment

Before committing to a software project, answer these questions explicitly:

| Question | What You Are Assessing | Red Flag If... |
|---|---|---|
| Can the current architecture support this? | Architecture dependencies | Requires a platform migration before feature work can begin |
| Do we have the skills on the team? | Team capacity and capability | Core technology is unfamiliar to >50% of the team |
| What is the expected load/scale? | Performance requirements | 10x current traffic with no scaling plan |
| Are there hard external deadlines? | Timeline constraints | Regulatory deadline in 8 weeks with 12 weeks of estimated work |
| What systems does this touch? | Integration points | More than 3 upstream/downstream systems affected |
| Is there existing technical debt blocking this? | Prerequisite work | Known debt items that must be resolved first |

#### Architecture Dependencies

Document every system this project touches. For each dependency, note:

```
Dependency: [System/Service Name]
Owner: [Team or individual]
Type: [Upstream data provider | Downstream consumer | Shared service | Third-party API]
Current State: [Stable | Degraded | Under active development]
Risk: [What breaks if this dependency is unavailable or changes?]
Action Needed: [None | API contract review | Load test | Migration]
```

**Worked Example:**

```
Dependency: User Authentication Service (AuthN)
Owner: Platform Team (Sarah Chen)
Type: Shared service
Current State: Stable, but scheduled for OAuth 2.1 migration in Q3
Risk: If migration timeline shifts left, our integration breaks mid-sprint
Action Needed: Confirm migration timeline with Platform Team; build against
               new OAuth 2.1 spec if migration completes before our launch
```

#### Team Capacity Check

Assess whether the team can absorb this project without overcommitting:

| Factor | Current State | Impact on This Project |
|---|---|---|
| Active projects per engineer | ___ | If >2, expect context-switching tax of 20-40% |
| On-call rotation burden | ___ hours/week | Deduct from available capacity |
| Planned PTO in project window | ___ days total | Adjust timeline accordingly |
| Open headcount / backfills | ___ positions | Do not plan capacity for unfilled roles |
| Upcoming tech debt sprints | ___ sprints reserved | Protect these; do not cannibalize for features |

#### Tech Stack Decisions

If the project introduces new technologies, document the decision and rationale:

```
Technology: [Name and version]
Category: [Language | Framework | Database | Infrastructure | Third-party service]
Why: [What problem does this solve that existing stack does not?]
Alternatives Considered: [What else was evaluated and why was it rejected?]
Team Familiarity: [High | Medium | Low -- if Low, what is the ramp-up plan?]
Licensing: [Open source | Commercial -- cost implications?]
Support/Community: [Active community? Enterprise support available?]
Decision Maker: [Who approved this?]
Reversibility: [Easy to swap out later | Medium effort | Locked in]
```

#### Definition of Done

Establish project-level Definition of Done before any work begins. This prevents end-of-sprint arguments about what "done" means.

```
A feature is DONE when:
[ ] Code is written and passes all unit tests (>80% coverage on new code)
[ ] Code has been peer-reviewed and approved by at least one reviewer
[ ] Integration tests pass in staging environment
[ ] Documentation is updated (API docs, runbooks, architecture diagrams)
[ ] Feature flag is configured (if applicable)
[ ] Performance benchmarks meet acceptance criteria
[ ] Security review completed (if touching auth, PII, or payment flows)
[ ] Product owner has accepted the feature in staging
[ ] Deployment runbook is updated
[ ] Monitoring and alerting are configured
```

#### Integration Points

Map every integration this project requires:

| Integration | Direction | Protocol | Auth Method | Data Format | SLA | Owner |
|---|---|---|---|---|---|---|
| Payment Gateway | Outbound | REST API | API Key | JSON | 99.9% uptime | Payments Team |
| Analytics Pipeline | Outbound | Event stream | Service account | Avro | Best effort | Data Eng |
| CRM Sync | Bidirectional | Webhook + REST | OAuth 2.0 | JSON | 99.5% uptime | Integrations Team |
| Legacy Billing DB | Inbound | Direct DB read | Connection pool | SQL | N/A (internal) | Platform Team |

### General Mode

For non-software projects -- organizational change, process improvement, facility build-outs, marketing campaigns, and similar -- the charter must ground the project in business value and governance.

#### Business Case

Every project needs a business case, even if the project feels "obviously" needed. The business case forces clarity on why this project deserves resources over competing priorities.

```
BUSINESS CASE

Problem Statement:
[What problem exists today? Who is affected? What is the cost of inaction?
Be specific: "Customer onboarding takes 14 days on average; industry
benchmark is 3 days. We lose 22% of signed customers during onboarding."]

Proposed Solution:
[What will this project deliver? Describe the end state, not the activities.
"Redesigned onboarding process that reduces time-to-value from 14 days to
5 days through automation of document collection, parallel processing of
compliance checks, and a dedicated onboarding specialist role."]

Expected Benefits:
- Quantitative: [Revenue retained: $1.2M/year from reduced churn during onboarding]
- Quantitative: [Cost savings: $180K/year from reduced manual processing]
- Qualitative: [Improved customer satisfaction; stronger first impression]
- Qualitative: [Reduced burden on operations team; lower burnout risk]

Cost Estimate:
- Project cost: [Total budget including labor, tools, external vendors]
- Ongoing cost: [Annual operating cost of the solution once implemented]
- ROI: [Payback period or ROI calculation]
  Example: "$340K project cost / $1.38M annual benefit = 3-month payback"

Timeline:
- Estimated duration: [X weeks/months]
- Target completion: [Date]
```

#### Sponsor Alignment

The project sponsor is the person who funds the project, removes organizational blockers, and makes final decisions when the team is stuck. Sponsor alignment means:

1. **Sponsor understands and agrees with the business case.** They can articulate why this project matters in their own words, not just nod at your slides.
2. **Sponsor commits time.** Minimum: 30-minute weekly check-in with PM, attendance at monthly steering committee, availability for escalations within 24 hours.
3. **Sponsor has decision-making authority.** If the sponsor needs to "check with their boss" on every decision, they are not the real sponsor. Find the real sponsor.
4. **Sponsor agrees to scope boundaries.** The sponsor understands what is in scope and what is out, and will defend those boundaries when pressure arises.

**Sponsor alignment checklist:**

- [ ] Sponsor has reviewed and approved the business case
- [ ] Sponsor has committed to governance cadence (weekly 1:1, monthly steering)
- [ ] Sponsor's success criteria are documented and match the charter
- [ ] Sponsor has identified who can act in their absence
- [ ] Sponsor agrees to the escalation path and response time expectations

#### Governance Structure

Define how decisions get made before decisions need to be made.

**Steering Committee:**

| Role | Name | Responsibility | Meeting Cadence |
|---|---|---|---|
| Executive Sponsor | ___ | Final decision authority; budget approval; escalation resolution | Monthly steering + weekly 1:1 with PM |
| Project Manager | ___ | Day-to-day management; risk management; status reporting | All meetings |
| Business Lead | ___ | Requirements validation; UAT sign-off; change impact assessment | Bi-weekly + monthly steering |
| Finance Representative | ___ | Budget tracking; cost approval; ROI validation | Monthly steering |
| PMO Representative | ___ | Standards compliance; resource coordination; portfolio alignment | Monthly steering |

**RACI at Project Level:**

| Decision Area | Sponsor | PM | Business Lead | Finance | PMO |
|---|---|---|---|---|---|
| Scope changes (>5% budget impact) | A | R | C | C | I |
| Budget reallocation (<5%) | I | A | C | R | I |
| Timeline changes (>2 weeks) | A | R | C | I | C |
| Vendor selection | A | R | C | C | I |
| Risk escalation (Red status) | A | R | I | I | C |
| Go/No-Go at phase gates | A | R | C | C | I |

*R = Responsible, A = Accountable, C = Consulted, I = Informed*

#### Procurement Needs

If the project requires external vendors, tools, or services, document procurement requirements early. Procurement cycles (RFP, vendor evaluation, contract negotiation, legal review) routinely add 4-12 weeks to timelines.

```
Procurement Item: [What you need]
Estimated Cost: [$X]
Procurement Method: [Direct purchase | RFP | Sole source | Existing contract]
Lead Time: [Estimated weeks from request to delivery]
Approval Required From: [Procurement, Legal, Finance, IT Security]
Dependency: [What project work is blocked until this is procured?]
```

#### Compliance and Regulatory Check

Before launch, identify any regulatory, legal, or compliance requirements that constrain the project:

- [ ] Data privacy (GDPR, CCPA, HIPAA) -- does the project handle personal data?
- [ ] Industry regulations -- are there sector-specific rules (financial services, healthcare, government)?
- [ ] Internal policies -- does the project comply with corporate security, procurement, and HR policies?
- [ ] Audit requirements -- will the project be subject to internal or external audit?
- [ ] Accessibility requirements -- does the output need to meet WCAG or ADA standards?
- [ ] Environmental/safety regulations -- applicable for physical projects or facilities

### Charter Template

Use this template for both software and general projects. Adapt sections as needed.

```
PROJECT CHARTER
===============
Version: ___  |  Date: _______________
Status: [Draft | Under Review | Approved]

1. PROJECT NAME
   [Clear, descriptive name -- not a code name that nobody outside the team
   understands]

2. PROJECT SPONSOR
   Name: _______________
   Title: _______________
   Authority: [Budget approval up to $X; escalation decision-maker]

3. PROJECT MANAGER
   Name: _______________
   Authority: [Day-to-day decisions; budget allocation within approved limits;
              team assignments]

4. START DATE / END DATE
   Planned Start: _______________
   Planned End: _______________
   Key Phase Gates: [Phase 1 complete by ___, Phase 2 by ___, etc.]

5. OBJECTIVES
   [What will this project achieve? Write 3-5 objectives using the SMART
   format: Specific, Measurable, Achievable, Relevant, Time-bound]
   - Objective 1: _______________
   - Objective 2: _______________
   - Objective 3: _______________

6. SCOPE
   In Scope:
   - [Specific deliverable or work area]
   - [Specific deliverable or work area]
   - [Specific deliverable or work area]

   Out of Scope:
   - [Explicitly excluded item -- name it so nobody assumes it is included]
   - [Explicitly excluded item]
   - [Explicitly excluded item]

7. SUCCESS CRITERIA
   [How will we know this project succeeded? Define measurable outcomes.]
   - Criterion 1: [Metric] reaches [target] by [date]
   - Criterion 2: [Deliverable] is accepted by [stakeholder] by [date]
   - Criterion 3: [Outcome] is sustained for [duration] post-launch

8. KEY STAKEHOLDERS
   | Name | Role | Interest | Influence | Communication Need |
   |------|------|----------|-----------|-------------------|
   |      |      |          |           |                   |

9. HIGH-LEVEL RISKS
   | Risk | Likelihood | Impact | Mitigation |
   |------|-----------|--------|------------|
   |      |           |        |            |

10. BUDGET
    | Category | Estimated Cost | Approved? |
    |----------|---------------|-----------|
    | Labor (internal) | $_______ | [ ] |
    | Labor (external/vendor) | $_______ | [ ] |
    | Tools/licenses | $_______ | [ ] |
    | Infrastructure | $_______ | [ ] |
    | Contingency (10-15%) | $_______ | [ ] |
    | TOTAL | $_______ | [ ] |

11. ASSUMPTIONS
    [What are we assuming to be true that, if wrong, would change the plan?]
    - Assumption 1: _______________
    - Assumption 2: _______________
    - Assumption 3: _______________

12. CONSTRAINTS
    [What limits are imposed on the project?]
    - Constraint 1: [Budget cap of $X]
    - Constraint 2: [Must use existing vendor; no new procurement]
    - Constraint 3: [Team cannot exceed X headcount]
    - Constraint 4: [Must comply with regulation Y]

APPROVALS:
Sponsor: _______________ Date: ___
PM: _______________ Date: ___
Finance: _______________ Date: ___
```

### Charter Quality Checklist

Before circulating the charter for approval, validate it against these criteria:

- [ ] **Objectives are SMART.** Each objective is Specific, Measurable, Achievable, Relevant, and Time-bound. If an objective says "improve customer experience," it fails -- improve by how much, measured how, by when?
- [ ] **Scope boundaries are explicit.** Both "in scope" and "out of scope" are listed. Out-of-scope items are named specifically, not implied. If it is not in the "in scope" list, it should be in "out of scope."
- [ ] **Success criteria are measurable.** Every criterion has a number, a date, or a verifiable outcome. "Project is successful" is not a criterion. "NPS increases from 32 to 45 within 90 days of launch" is.
- [ ] **Stakeholders are identified by name.** Not "engineering team" -- specific people. You cannot communicate with a department; you communicate with individuals.
- [ ] **Risks have mitigations.** Every identified risk has at least one mitigation action. A risk without a mitigation is just a worry.
- [ ] **Budget includes contingency.** A budget without 10-15% contingency is a fantasy. Something will go wrong. Plan for it.
- [ ] **Assumptions are documented.** Assumptions are the invisible load-bearing walls of a project. If an assumption breaks, the project may collapse. Write them down so you can test and monitor them.
- [ ] **Constraints are acknowledged.** The charter reflects real-world limits: budget caps, headcount freezes, regulatory deadlines, technology mandates. Ignoring constraints does not make them go away.
- [ ] **Sponsor has signed.** A charter without sponsor sign-off is a wishlist. The signature represents organizational commitment of resources, budget, and political support.
- [ ] **The charter fits on 1-3 pages.** If it is longer, you are writing a project plan, not a charter. Cut it down.

### Charter Anti-Patterns

These are the most common ways charters fail. Recognize and correct them early.

**Scope Too Vague**
- Symptom: Scope section says "Build a new customer portal" with no further detail.
- Problem: Every stakeholder imagines a different portal. Engineering thinks it is a dashboard. Sales thinks it is a self-service buying tool. Support thinks it is a ticketing system.
- Fix: List 5-10 specific capabilities in scope. List 3-5 things explicitly out of scope. Use concrete language: "Self-service password reset, order history view, and support ticket submission. Does NOT include payment processing, live chat, or account creation."

**No Success Criteria**
- Symptom: The charter lists objectives but no way to measure whether they were achieved.
- Problem: At project close, nobody can agree on whether it succeeded. The sponsor says "I expected more." The team says "We delivered everything we were asked for." Both are right because there was no shared definition of success.
- Fix: For every objective, write a corresponding success criterion with a specific metric and target. "Reduce onboarding time from 14 days to 5 days, measured by median time across all new customers in the first 90 days post-launch."

**Missing Stakeholders**
- Symptom: The charter lists the sponsor and PM but nobody else. Or it lists departments instead of people.
- Problem: Stakeholders who are not identified are not engaged. They surface mid-project with requirements that blow up scope, timeline, or both.
- Fix: Conduct a stakeholder identification exercise before writing the charter. Ask: "Who can block this project? Who is affected by the outcome? Who controls resources we need? Who has expertise we require?" Name them individually.

**Charter-as-Contract**
- Symptom: The charter is treated as a legally binding document that can never change. Any proposed modification triggers a formal change control process.
- Problem: Projects operate in uncertain environments. If the charter cannot evolve as the team learns more, it becomes an anchor rather than a compass. Teams either ignore it entirely or spend more time managing change requests than doing work.
- Fix: The charter is a living document. It should be reviewed at every phase gate and updated when material assumptions change. Changes to objectives or scope require sponsor approval. Changes to implementation details do not. Version the charter and track what changed and why.

---

## Stakeholder Mapping

Stakeholder mapping identifies who matters, how much influence they have, what they care about, and how to engage them. A project can have a perfect plan and still fail because a key stakeholder was ignored, surprised, or actively working against it.

### Power/Interest Grid

The Power/Interest grid is the foundational tool for stakeholder classification. It plots stakeholders on two axes: their power to influence the project outcome and their interest in the project.

```
                        HIGH POWER
                            |
         Keep Satisfied     |     Manage Closely
         (High Power,       |     (High Power,
          Low Interest)     |      High Interest)
                            |
        These stakeholders  |  These are your most
        can block you but   |  critical stakeholders.
        are not paying      |  Engage them deeply,
        close attention.    |  consult them on major
        Keep them informed  |  decisions, and never
        enough to prevent   |  surprise them.
        negative surprises. |
                            |
   LOW INTEREST ------------+------------ HIGH INTEREST
                            |
         Monitor            |     Keep Informed
         (Low Power,        |     (Low Power,
          Low Interest)     |      High Interest)
                            |
        Minimal effort.     |  These stakeholders care
        Periodic updates.   |  deeply but cannot directly
        Watch for changes   |  influence outcomes. Keep
        in their power or   |  them informed, listen to
        interest level.     |  their concerns, and use
                            |  them as advocates.
                            |
                        LOW POWER
```

**Quadrant Descriptions and Engagement Strategies:**

| Quadrant | Power | Interest | Strategy | Engagement Examples |
|---|---|---|---|---|
| **Manage Closely** | High | High | Deep, frequent engagement. Co-create solutions. Weekly or bi-weekly meetings. Include in decision-making. | Executive sponsor, key business owner, lead architect (software). Invite to steering committee. Share draft deliverables for early feedback. |
| **Keep Satisfied** | High | Low | Provide high-level updates. Do not overwhelm with detail. Anticipate their concerns and address proactively. | CFO on a non-financial project, CTO on a marketing initiative. Send monthly executive summary. Flag only items that affect budget or timeline. |
| **Keep Informed** | Low | High | Regular communication. Listen to their input even if they cannot mandate changes. They can become advocates or detractors. | End users, junior team members, customer advisory board members. Include in newsletters, demos, and feedback sessions. |
| **Monitor** | Low | Low | Light touch. Periodic updates. Watch for shifts -- a stakeholder's power or interest can change as the project evolves. | Tangentially affected departments, external observers. Quarterly update email. No meetings unless they request one. |

### Stakeholder Register Template

Maintain a living register of all identified stakeholders. Update it at every phase gate and whenever organizational changes occur.

```
STAKEHOLDER REGISTER
=====================
Project: _______________  |  Last Updated: _______________
Maintained By: [PM Name]

| # | Name | Role/Title | Org/Dept | Influence (H/M/L) | Interest (H/M/L) | Grid Quadrant | Communication Need | Potential Resistance | Engagement Strategy |
|---|------|-----------|----------|-------------------|------------------|---------------|-------------------|---------------------|-------------------|
| 1 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| 2 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
| 3 | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ | ___ |
```

**Column guide:** Influence = can they approve, block, or materially change the project? Interest = how much do they care about the outcome? Communication Need = format, frequency, and detail level (e.g., "Bi-weekly 1:1, wants to review deliverables"). Potential Resistance = concerns that could cause opposition (e.g., "Worried about headcount reductions"). Engagement Strategy = specific actions to keep them aligned (e.g., "Include in design reviews to address technical concerns early").

### Software Mode: Technical Stakeholder Categories

Software projects have a distinct stakeholder landscape. Missing any of these groups creates risk.

**Technical Stakeholders:**

| Stakeholder | Why They Matter | Typical Concerns | How to Engage |
|---|---|---|---|
| Lead/Staff Architects | Define technical direction; can veto approaches | Architectural integrity, scalability, tech debt | Include in design reviews; seek their approval on architecture decisions before committing |
| SRE/DevOps Engineers | Own production reliability; control deployment pipeline | Operational burden, monitoring gaps, on-call impact | Share operational requirements early; involve in non-functional requirements definition |
| Security Team | Gate deployments through security review; own compliance | Vulnerability exposure, data handling, audit readiness | Engage at project start, not before launch; schedule threat modeling session |
| QA/Test Engineers | Define quality bar; own test strategy | Test coverage, automation feasibility, regression risk | Include in sprint planning; involve in Definition of Done |

**Product Stakeholders:**

| Stakeholder | Why They Matter | Typical Concerns | How to Engage |
|---|---|---|---|
| Product Manager | Owns the "what" and "why"; prioritizes backlog | Scope clarity, customer value, delivery timeline | Weekly sync; co-own charter objectives; joint stakeholder communications |
| UX/Design Lead | Owns user experience; defines interaction patterns | Usability, accessibility, design system consistency | Include in kickoff; schedule design review checkpoints at each milestone |
| Data/Analytics Lead | Defines metrics instrumentation; owns reporting | Event tracking coverage, data pipeline capacity, metric definitions | Involve in success criteria definition; agree on instrumentation requirements before development |

**Business Stakeholders:**

| Stakeholder | Why They Matter | Typical Concerns | How to Engage |
|---|---|---|---|
| Engineering Leadership (VP/Director) | Allocate engineers; set team priorities | Headcount allocation, competing priorities, org-level commitments | Monthly update; escalation path for resource conflicts |
| Sales/GTM Leadership | Sell what you build; set customer expectations | Feature availability dates, competitive positioning, customer commitments | Quarterly roadmap preview; flag any date changes immediately |
| Customer Success/Support | Handle post-launch customer impact | Support burden, documentation quality, training needs | Include in launch planning; provide runbooks and FAQ before launch |

### General Mode: Stakeholder Categories

Non-software projects have broader organizational reach and often involve external parties.

| Category | Examples | Key Concern | Engagement Approach |
|---|---|---|---|
| Executive Sponsors | CEO, COO, Division President | Strategic alignment, ROI, organizational impact | Monthly steering committee; quarterly business review |
| Functional Managers | Department heads whose teams are affected | Resource allocation, workflow disruption, change fatigue | Bi-weekly working sessions; involve in impact assessment |
| PMO | Portfolio managers, standards owners | Methodology compliance, resource conflicts, reporting | Regular check-ins; align on templates and governance |
| Vendors/Suppliers | Technology vendors, consultants, outsourced teams | Contract scope, deliverable expectations, payment terms | Formal contract management; weekly vendor status calls |
| Regulators | Government agencies, industry bodies, auditors | Compliance, reporting, audit readiness | Dedicated compliance workstream; legal review of touchpoints |
| Customers/End Users | Direct customers, internal users of project output | Quality, usability, disruption to current service | User research, beta testing, feedback sessions, launch comms |
| Partners | Channel partners, integration partners | Timeline coordination, shared deliverables | Joint planning sessions; shared milestones and cadence |

### Stakeholder Analysis Anti-Patterns

**Forgetting End Users**
- Symptom: The stakeholder map includes executives, managers, and the project team but nobody who will actually use the project output day-to-day.
- Impact: The project delivers something that looks good in a steering committee but is unusable in practice. Adoption fails.
- Fix: Always include representative end users on the stakeholder register. Engage them in requirements, design reviews, and UAT. If you cannot name specific end users, you do not understand your audience well enough.

**Assuming All Executives Are Equal**
- Symptom: Every VP and C-level is placed in the "Manage Closely" quadrant regardless of their actual influence on or interest in the project.
- Impact: The PM spends excessive time managing executives who do not care about the project, while under-engaging the ones who do.
- Fix: Assess each executive individually. A CFO on a marketing project may be "Keep Satisfied" (high power, low interest) while the CMO is "Manage Closely." Not every executive needs the same level of engagement.

**Not Revisiting the Map**
- Symptom: Stakeholder map is created at project start and never updated.
- Impact: Organizational changes, role changes, or shifting priorities mean the map becomes inaccurate. A stakeholder who was "Monitor" in month 1 may become "Manage Closely" by month 3 due to a reorg or strategic shift.
- Fix: Review and update the stakeholder register at every phase gate (minimum monthly). Ask: "Has anyone's power or interest changed? Are there new stakeholders we missed? Has anyone left the organization?"

**Treating It as a One-Time Exercise**
- Symptom: Stakeholder mapping is done as a checkbox activity during project initiation and filed away.
- Impact: The map becomes a dead artifact. Engagement strategies are never executed. Stakeholders who needed attention do not get it.
- Fix: The stakeholder register should be a working document that drives weekly engagement actions. Every PM weekly planning session should include: "Who do I need to talk to this week based on the stakeholder register?"

**Ignoring Potential Resistance**
- Symptom: The "Potential Resistance" column is left blank or filled with "None" for every stakeholder.
- Impact: Resistance surprises the team mid-project. A department head blocks a process change because they feel threatened. An architect vetoes a technical approach because they were not consulted.
- Fix: Assume resistance exists until proven otherwise. For each stakeholder, ask: "What could they lose from this project? What could make them uncomfortable? What past experiences might make them skeptical?" Document it and plan for it.

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
