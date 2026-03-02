# Project Management Plugin — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the project-management plugin with 5 lifecycle skills, 20 commands, 1 orchestrator agent, and MCP connectors.

**Architecture:** Hybrid plugin — skills + commands for direct workflows, orchestrator agent for cross-cutting multi-stage requests. Software/Tech PM and General PM modes separated within each skill.

**Tech Stack:** Markdown (SKILL.md, commands, orchestrator), JSON (plugin.json, .mcp.json)

**Design Doc:** `docs/plans/2026-03-01-project-management-design.md`

**Reference Plugins:** Study `product-management/` for skills+commands pattern, `real-estate-investment/` for orchestrator agent pattern.

---

## Task 1: Scaffold Plugin Structure & Metadata

**Files:**
- Create: `project-management/.claude-plugin/plugin.json`
- Create: `project-management/.mcp.json`
- Create: `project-management/CONNECTORS.md`

**Step 1: Create plugin.json**

Create `project-management/.claude-plugin/plugin.json`:

```json
{
    "name": "project-management",
    "version": "1.0.0",
    "description": "Project management workflows from initiation to closing — charters, WBS, scheduling, risk registers, sprint planning, status reports, retrospectives, and project closeout for software and general PMs.",
    "author": {
        "name": "LauraFlorentin"
    },
    "repository": "https://github.com/LauraFlorentin/skills-marketplace",
    "license": "MIT",
    "skills": "./skills/",
    "commands": "./commands/",
    "keywords": [
        "project",
        "pm",
        "agile",
        "scrum",
        "kanban",
        "waterfall",
        "sprint",
        "risk",
        "gantt",
        "retrospective"
    ]
}
```

**Step 2: Create .mcp.json**

Create `project-management/.mcp.json`:

```json
{
    "mcpServers": {
        "jira": {
            "type": "npm",
            "package": "@anthropic/jira-mcp",
            "description": "Issue tracking, sprint management, backlog, boards"
        },
        "linear": {
            "type": "npm",
            "package": "@anthropic/linear-mcp",
            "description": "Lightweight project tracking, cycles, triage"
        },
        "asana": {
            "type": "npm",
            "package": "@anthropic/asana-mcp",
            "description": "Task management, timelines, portfolios"
        },
        "notion": {
            "type": "npm",
            "package": "@anthropic/notion-mcp",
            "description": "Docs, wikis, meeting notes, knowledge base"
        },
        "slack": {
            "type": "npm",
            "package": "@anthropic/slack-mcp",
            "description": "Team messaging, standups, status updates"
        }
    }
}
```

**Step 3: Create CONNECTORS.md**

Create `project-management/CONNECTORS.md`:

```markdown
# Connectors

Commands in this plugin reference external tools using `~~placeholder` syntax. You do **not** need any of these tools to use the plugin — commands work standalone and produce richer output when tools are connected.

## Placeholder Reference

| Placeholder | Category | Example Tools |
|-------------|----------|---------------|
| `~~project-tracker` | Issue tracking & sprints | Jira, Linear, Asana, Monday, Shortcut |
| `~~docs` | Documentation & wikis | Notion, Confluence, Google Docs |
| `~~time-tracker` | Time tracking & capacity | Harvest, Toggl, Clockify |
| `~~messaging` | Team communication | Slack, Teams |
| `~~calendar` | Scheduling & availability | Google Calendar, Outlook |
| `~~ci-cd` | Build & deploy pipelines | GitHub Actions, Jenkins, CircleCI |
| `~~repo` | Source code & PRs | GitHub, GitLab, Bitbucket |

## Notes

- **`~~ci-cd` and `~~repo`** are software-mode-only connectors. General PM mode does not reference them.
- **`~~docs`** can serve as a project wiki, meeting notes repo, and decision log — same tool, multiple uses.
- **Pre-configured MCP servers** are listed in [`.mcp.json`](./.mcp.json). Enable whichever tools your team uses.
```

**Step 4: Commit**

```bash
git add project-management/.claude-plugin/plugin.json project-management/.mcp.json project-management/CONNECTORS.md
git commit -m "feat(project-management): scaffold plugin metadata, MCP config, and connectors"
```

---

## Task 2: Initiation Skill

**Files:**
- Create: `project-management/skills/initiation/SKILL.md`

**Step 1: Write the Initiation skill**

Create `project-management/skills/initiation/SKILL.md`. This skill covers project charters, stakeholder mapping, and kickoff planning.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Initiation"
- Disclaimer: adapted-to-context warning (this plugin assists with project management workflows but does not replace professional judgment)
- **Project Charter** section with:
  - Software mode: Technical feasibility assessment, architecture dependencies, team capacity check, tech stack decisions, definition of done, integration points
  - General mode: Business case (problem, proposed solution, expected benefits, cost estimate), sponsor alignment, governance structure (steering committee, RACI at project level), procurement needs, compliance/regulatory check
  - Charter template with sections: Project Name, Sponsor, PM, Start/End, Objectives, Scope (in/out), Success Criteria, Key Stakeholders, High-Level Risks, Budget, Assumptions, Constraints
  - Charter quality checklist
- **Stakeholder Mapping** section with:
  - Power/Interest grid (4 quadrants: Manage Closely, Keep Satisfied, Keep Informed, Monitor)
  - Stakeholder register template: Name, Role, Influence (H/M/L), Interest (H/M/L), Communication Need, Potential Resistance, Engagement Strategy
  - Software mode: Technical stakeholders (architects, SREs, security), product stakeholders (PM, design), business stakeholders (leadership, sales)
  - General mode: Executive sponsors, functional managers, external stakeholders (vendors, regulators, customers), PMO
  - Stakeholder analysis anti-patterns (forgetting end users, assuming all execs are equal, not revisiting the map)
- **Kickoff Planning** section with:
  - Kickoff agenda template (60-min and 30-min versions)
  - Software mode: Tech stack walkthrough, dev environment setup, CI/CD overview, branching strategy, on-call expectations
  - General mode: Project overview, governance walkthrough, communication plan preview, roles and responsibilities, key milestones, Q&A
  - Pre-kickoff checklist (what to prepare before the meeting)
  - Post-kickoff follow-up template (action items, decisions, next steps)

**Step 2: Commit**

```bash
git add project-management/skills/initiation/SKILL.md
git commit -m "feat(project-management): add initiation skill — charters, stakeholder mapping, kickoffs"
```

---

## Task 3: Planning Skill

**Files:**
- Create: `project-management/skills/planning/SKILL.md`

**Step 1: Write the Planning skill**

Create `project-management/skills/planning/SKILL.md`. This skill covers WBS, scheduling, resource planning, risk management, and communication planning.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Planning"
- Disclaimer
- **Work Breakdown Structure** section with:
  - WBS principles: 100% rule, mutually exclusive, deliverable-oriented
  - Software mode: Epic → Feature → Story → Task decomposition, story point estimation, acceptance criteria per story
  - General mode: Phase → Deliverable → Work Package → Activity decomposition, hours-based estimation
  - WBS dictionary template (ID, name, description, owner, effort, dependencies, acceptance criteria)
  - Decomposition rules of thumb: stop decomposing when a work package is 8-80 hours (general) or fits in one sprint (software)
- **Scheduling** section with:
  - Software mode: Sprint-based scheduling — sprint length selection (1/2/3/4 weeks), velocity estimation for new teams, sprint goal setting, release planning (mapping sprints to releases), story mapping for sequencing
  - General mode: Critical path method (CPM) — forward/backward pass, float calculation, critical path identification. PERT estimates (optimistic/most likely/pessimistic). Gantt chart structure. Milestone definition. Phase gate criteria.
  - Dependencies: Finish-to-Start, Start-to-Start, Finish-to-Finish, Start-to-Finish with examples
  - Schedule compression: crashing vs. fast-tracking with trade-offs
  - Buffer management: project buffer, feeding buffers, resource buffers
- **Resource Planning** section with:
  - Resource allocation matrix template (person × week, % allocation)
  - Software mode: Team topology considerations (stream-aligned, platform, enabling, complicated-subsystem), T-shaped skills, pairing/mobbing strategies, on-call rotation planning
  - General mode: Resource leveling (resolving over-allocation), resource smoothing, skills gap analysis, contractor vs. full-time decision framework
  - Capacity planning: available hours - meetings - overhead = productive hours
  - Common pitfalls: 100% allocation myth, context switching cost, not accounting for leave
- **Risk Management** section with:
  - Risk identification techniques: brainstorming, SWOT, pre-mortem, checklist review, assumption analysis
  - Risk register template: ID, Description, Category, Probability (1-5), Impact (1-5), Score (P×I), Response Strategy (avoid/mitigate/transfer/accept), Owner, Status, Trigger
  - Software mode: Technical risks (architecture, dependencies, performance, security), integration risks, deployment risks, technical debt risks
  - General mode: Scope risks, schedule risks, budget risks, resource risks, external risks (regulatory, market, vendor)
  - Risk response strategies with examples for each
  - Risk review cadence recommendations
- **Communication Planning** section with:
  - Communication plan template: Audience, Message, Frequency, Channel, Owner, Format
  - Software mode: Sprint review, daily standup (sync vs. async), demo cadence, Slack channel strategy, PR review expectations, incident communication
  - General mode: Steering committee updates, sponsor briefings, team meetings, vendor check-ins, change advisory board
  - RACI matrix: Responsible, Accountable, Consulted, Informed — with worked example
  - Escalation path definition

**Step 2: Commit**

```bash
git add project-management/skills/planning/SKILL.md
git commit -m "feat(project-management): add planning skill — WBS, scheduling, resources, risks, communication"
```

---

## Task 4: Execution Skill

**Files:**
- Create: `project-management/skills/execution/SKILL.md`

**Step 1: Write the Execution skill**

Create `project-management/skills/execution/SKILL.md`. This skill covers standups, sprint planning, decision tracking, and change management.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Execution"
- Disclaimer
- **Standups & Daily Coordination** section with:
  - Software mode: Daily standup format — what I did, what I'll do, blockers. Async standup template (Slack/messaging format). Standup anti-patterns (status reports to managers, going over 15 min, solving problems in standup). Kanban daily: focus on board flow, WIP limits, blocked items.
  - General mode: Daily or weekly team check-in template. Focus on: progress against plan, upcoming milestones, resource needs, decisions needed. Vendor/contractor coordination cadence.
  - When to escalate vs. when to handle in standup
- **Sprint/Iteration Planning** section with:
  - Software mode: Sprint planning ceremony — capacity calculation (team members × available days × focus factor), sprint goal selection, story selection from backlog, task breakdown, commitment. Definition of Ready checklist. Sprint length trade-offs. Kanban alternative: WIP limits, pull system, cycle time targets.
  - General mode: Phase/iteration planning — deliverables for this period, resource assignments, dependency check, risk review. Weekly planning rhythm. Workstream coordination.
  - Velocity tracking and forecasting (software mode)
  - Milestone tracking and earned value (general mode)
- **Decision Management** section with:
  - Decision log template: ID, Date, Decision, Context/Rationale, Alternatives Considered, Made By, Impact, Status (Active/Superseded/Reversed)
  - Decision-making frameworks: RAPID (Recommend, Agree, Perform, Input, Decide), Consent-based, Lazy consensus
  - Software mode: Architecture Decision Records (ADR) format, tech stack decisions, buy vs. build
  - General mode: Business decisions, vendor selection, scope trade-offs, budget reallocation
  - When to escalate a decision
- **Change Management** section with:
  - Change request template: ID, Requestor, Date, Description, Justification, Impact (scope, schedule, cost, risk), Priority, Approval Status
  - Impact analysis framework: What changes? What's affected? What's the cost of the change vs. the cost of not changing?
  - Software mode: Feature scope changes, technical pivots, dependency changes, infrastructure changes. Link to deployment planning.
  - General mode: Formal change control board process, change categories (minor/significant/major), integrated change control
  - Scope creep detection signals

**Step 2: Commit**

```bash
git add project-management/skills/execution/SKILL.md
git commit -m "feat(project-management): add execution skill — standups, sprint planning, decisions, change management"
```

---

## Task 5: Monitoring Skill

**Files:**
- Create: `project-management/skills/monitoring/SKILL.md`

**Step 1: Write the Monitoring skill**

Create `project-management/skills/monitoring/SKILL.md`. This skill covers status reporting, burndown analysis, risk reviews, dependency tracking, and health checks.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Monitoring"
- Disclaimer
- **Status Reporting** section with:
  - RAG (Red/Amber/Green) status framework — criteria for each color across dimensions: Schedule, Scope, Budget, Risk, Team Health
  - Software mode: Sprint-level status — velocity vs. plan, burndown shape, blockers, deployment status. Metrics: cycle time, lead time, deployment frequency, change failure rate (DORA metrics).
  - General mode: Project-level status — milestone progress, budget burn rate (planned vs. actual), resource utilization, critical path status. Metrics: SPI, CPI, EAC, ETC.
  - Status report template (1-page): RAG summary, key accomplishments, upcoming milestones, risks/issues, decisions needed, help needed
  - Audience-specific formatting: executive summary (3 bullets), team detail (full report), steering committee (RAG + decisions)
- **Burndown & Forecasting** section with:
  - Software mode: Sprint burndown (story points remaining vs. ideal line), release burndown, burnup chart (scope changes visible). Velocity-based forecasting: "At current velocity, remaining scope will complete in N sprints." Monte Carlo simulation concepts for probabilistic forecasting.
  - General mode: Milestone burndown, earned value analysis — EV, PV, AC, SV, CV, SPI, CPI, EAC, ETC. S-curve visualization. Percent complete calculation methods (0/100, 50/50, milestones weighted).
  - Forecast accuracy tracking
  - Warning signs in burndown shapes (flat line, hockey stick, scope creep sawtooth)
- **Risk Review** section with:
  - Risk review meeting agenda template
  - Risk register update process: re-score existing risks, identify new risks, close resolved risks, review trigger conditions
  - Risk trend tracking: are risks increasing or decreasing over time?
  - Software mode: Technical debt as risk, security vulnerability tracking, dependency update risk
  - General mode: Risk categories review (scope, schedule, cost, quality, external), risk owner accountability
  - Escalation criteria: when does a risk become an issue?
- **Dependency Tracking** section with:
  - Dependency map template: Source, Target, Type (blocking/enabling/shared resource), Status, Owner, Due Date, Impact if Late
  - Software mode: Cross-team API dependencies, shared library dependencies, infrastructure dependencies, CI/CD pipeline dependencies
  - General mode: Cross-project dependencies, vendor dependencies, regulatory dependencies, resource sharing dependencies
  - Dependency review cadence
  - Blocked dependency escalation process
- **Health Check** section with:
  - Multi-dimensional project health assessment:
    - Schedule health (on track, at risk, behind)
    - Scope health (stable, creeping, unclear)
    - Budget health (within budget, at risk, over)
    - Team health (engaged, stressed, burned out)
    - Risk health (manageable, elevated, critical)
    - Stakeholder health (aligned, mixed, misaligned)
  - Health check scoring: 1-5 per dimension, with thresholds for Green/Amber/Red
  - Software mode: Add dimensions for code quality, test coverage, deployment health, tech debt
  - General mode: Add dimensions for vendor performance, compliance, benefits realization
  - Health check report template
  - Triggers orchestrator agent for cross-stage assessment

**Step 2: Commit**

```bash
git add project-management/skills/monitoring/SKILL.md
git commit -m "feat(project-management): add monitoring skill — status reports, burndown, risk reviews, dependencies, health checks"
```

---

## Task 6: Closing Skill

**Files:**
- Create: `project-management/skills/closing/SKILL.md`

**Step 1: Write the Closing skill**

Create `project-management/skills/closing/SKILL.md`. This skill covers retrospectives, lessons learned, and project closeout.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Closing"
- Disclaimer
- **Retrospectives** section with:
  - Multiple retro formats:
    - Start/Stop/Continue — simple, good for new teams
    - Mad/Sad/Glad — emotional temperature check
    - 4Ls (Liked/Learned/Lacked/Longed For) — comprehensive
    - Sailboat (Wind/Anchor/Rocks/Island) — visual metaphor
    - Timeline retro — walk through the sprint/project chronologically
  - Retro facilitation guide: setup (5 min), generate (10 min), cluster (5 min), vote (5 min), discuss top items (20 min), action items (5 min)
  - Software mode: Sprint retro (every 2 weeks), release retro, incident post-mortem format (timeline, root cause, contributing factors, action items, follow-up)
  - General mode: Phase-end review, project milestone retro, end-of-project retro
  - Anti-patterns: blame sessions, no action items, same issues every retro, only negative feedback
  - Action item tracking: owner, due date, follow-up in next retro
- **Lessons Learned** section with:
  - Lessons learned template: Category, What Happened, Impact, Root Cause, Lesson, Recommendation, Applicable To (this project only / org-wide)
  - Collection methods: retro synthesis, stakeholder interviews, metrics review, team survey
  - Software mode: Technical lessons (architecture decisions that worked/didn't, tooling choices, testing strategy effectiveness, deployment improvements), process lessons (estimation accuracy, sprint cadence, code review)
  - General mode: Planning accuracy, risk management effectiveness, stakeholder management, vendor management, communication effectiveness
  - Knowledge management: how to store and surface lessons for future projects
- **Project Closeout** section with:
  - Closeout checklist template:
    - Deliverables: all deliverables accepted by stakeholder
    - Documentation: project docs archived, knowledge transferred
    - Financials: final budget reconciliation, PO/contracts closed
    - Resources: team members released, access/permissions revoked
    - Tools: project boards archived, repos transferred, environments decommissioned
    - Communication: final status report sent, celebration/recognition
  - Software mode: Release notes compilation, runbook handoff (operations documentation), monitoring/alerting transfer, on-call rotation handoff, tech debt register handoff, environment cleanup (staging, feature branches), CI/CD pipeline ownership transfer
  - General mode: Formal acceptance documentation, contract closure, benefits realization plan (how will we measure if the project achieved its goals?), archive procedures, PMO reporting
  - Project closeout report template: Project summary, objectives achieved (vs. planned), schedule performance, budget performance, key metrics, lessons learned summary, recommendations for future projects
  - Team celebration/recognition suggestions

**Step 2: Commit**

```bash
git add project-management/skills/closing/SKILL.md
git commit -m "feat(project-management): add closing skill — retrospectives, lessons learned, project closeout"
```

---

## Task 7: Initiation Commands (3 commands)

**Files:**
- Create: `project-management/commands/project-charter.md`
- Create: `project-management/commands/stakeholder-map.md`
- Create: `project-management/commands/kickoff.md`

**Step 1: Write project-charter.md**

```markdown
---
description: Define project scope, objectives, stakeholders, and success criteria
argument-hint: "<project name> [software|general]"
---

# Project Charter

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a project charter that establishes the scope, objectives, and authority for a project.

## Usage

```
/project-charter <project name> [software|general]
```

### Arguments

- `project name` — The project to charter
- `software|general` — (Optional) PM context:
  - `software` — Tech/software project: architecture dependencies, team capacity, tech stack, CI/CD
  - `general` — Cross-industry project: business case, governance, procurement, compliance
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask the user about: project purpose, sponsor, key stakeholders, timeline, constraints, and budget. Check ~~docs for any existing project documentation.

### 2. Build Charter

Use the **Initiation** skill. Read `../skills/initiation/SKILL.md` and apply the appropriate charter template.

### 3. Output

Deliver the project charter in markdown. Run through the charter quality checklist. Offer to save to ~~docs if connected.
```

**Step 2: Write stakeholder-map.md**

```markdown
---
description: Map stakeholders by influence and interest with engagement strategies
argument-hint: "<project name>"
---

# Stakeholder Map

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map project stakeholders using a power/interest grid and define engagement strategies for each.

## Usage

```
/stakeholder-map <project name>
```

### Arguments

- `project name` — The project to map stakeholders for

## Workflow

### 1. Identify Stakeholders

Ask the user about: who is involved, who is affected, who has decision-making authority, who has concerns. Check ~~docs for any existing stakeholder lists.

### 2. Map & Analyze

Use the **Initiation** skill. Read `../skills/initiation/SKILL.md` and create:
- Stakeholder register with influence, interest, and engagement strategy
- Power/interest grid visualization
- Communication needs per stakeholder

### 3. Output

Deliver the stakeholder map and register. Flag any high-influence stakeholders who may resist the project.
```

**Step 3: Write kickoff.md**

```markdown
---
description: Generate a kickoff meeting agenda and preparation checklist
argument-hint: "<project name> [software|general]"
---

# Kickoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a kickoff meeting agenda, preparation checklist, and follow-up template.

## Usage

```
/kickoff <project name> [software|general]
```

### Arguments

- `project name` — The project to kick off
- `software|general` — (Optional) PM context:
  - `software` — Includes tech stack walkthrough, dev environment setup, CI/CD overview
  - `general` — Includes governance walkthrough, roles and responsibilities, milestone overview
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask about: project charter (is there one?), attendee list, meeting duration, key decisions to make. Check ~~docs for existing charter or project brief.

### 2. Build Agenda

Use the **Initiation** skill. Read `../skills/initiation/SKILL.md` and create the kickoff package.

### 3. Output

Deliver the kickoff agenda, pre-meeting checklist, and post-meeting follow-up template. Offer to schedule via ~~calendar or post to ~~messaging if connected.
```

**Step 4: Commit**

```bash
git add project-management/commands/project-charter.md project-management/commands/stakeholder-map.md project-management/commands/kickoff.md
git commit -m "feat(project-management): add initiation commands — project-charter, stakeholder-map, kickoff"
```

---

## Task 8: Planning Commands (5 commands)

**Files:**
- Create: `project-management/commands/wbs.md`
- Create: `project-management/commands/schedule.md`
- Create: `project-management/commands/resource-plan.md`
- Create: `project-management/commands/risk-register.md`
- Create: `project-management/commands/communication-plan.md`

**Step 1: Write wbs.md**

```markdown
---
description: Create a work breakdown structure for a project
argument-hint: "<project name> [software|general]"
---

# WBS

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a work breakdown structure decomposing a project into manageable deliverables and work packages.

## Usage

```
/wbs <project name> [software|general]
```

### Arguments

- `project name` — The project to decompose
- `software|general` — (Optional) PM context:
  - `software` — Epic → Feature → Story → Task decomposition with story points
  - `general` — Phase → Deliverable → Work Package → Activity decomposition with hours
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask about: project scope, major deliverables, known constraints. Check ~~docs for project charter or scope statement. Check ~~project-tracker for existing epics or work items.

### 2. Decompose

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create the WBS with dictionary.

### 3. Output

Deliver the WBS in indented outline format with a WBS dictionary. Offer to create work items in ~~project-tracker if connected.
```

**Step 2: Write schedule.md**

```markdown
---
description: Build a project schedule with milestones and dependencies
argument-hint: "<project name> [sprint-based|timeline]"
---

# Schedule

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Build a project schedule with milestones, dependencies, and time estimates.

## Usage

```
/schedule <project name> [sprint-based|timeline]
```

### Arguments

- `project name` — The project to schedule
- `sprint-based|timeline` — (Optional) Schedule style:
  - `sprint-based` — Agile: sprint cadence, velocity estimation, release mapping
  - `timeline` — Traditional: Gantt-style milestones, critical path, PERT estimates
  - If not specified, ask about the team's methodology

## Workflow

### 1. Gather Inputs

Ask about: WBS or scope, team size, target dates, known dependencies, constraints. Check ~~project-tracker for existing work items and ~~calendar for key dates.

### 2. Build Schedule

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create the schedule.

### 3. Output

Deliver the schedule with milestones, dependencies, and critical path (or sprint plan). Flag any scheduling risks. Offer to sync with ~~project-tracker if connected.
```

**Step 3: Write resource-plan.md**

```markdown
---
description: Plan team allocation, roles, and capacity
argument-hint: "<project name>"
---

# Resource Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Plan team allocation, roles, capacity, and identify resource risks.

## Usage

```
/resource-plan <project name>
```

### Arguments

- `project name` — The project to plan resources for

## Workflow

### 1. Gather Context

Ask about: team members available, their roles and skills, allocation percentage, project duration, known constraints (leave, other projects). Check ~~time-tracker for current utilization.

### 2. Build Plan

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create:
- Resource allocation matrix (person × week)
- Skills gap analysis
- Capacity calculation

### 3. Output

Deliver the resource plan with allocation matrix, capacity summary, and risk flags (over-allocation, single points of failure, skills gaps).
```

**Step 4: Write risk-register.md**

```markdown
---
description: Create a risk register with identification, scoring, and mitigation strategies
argument-hint: "<project name>"
---

# Risk Register

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a risk register identifying project risks, scoring them by probability and impact, and defining response strategies.

## Usage

```
/risk-register <project name>
```

### Arguments

- `project name` — The project to identify risks for

## Workflow

### 1. Gather Context

Ask about: project scope, timeline pressure, team experience, dependencies, technology choices, stakeholder concerns. Check ~~docs for project charter and ~~project-tracker for known issues.

### 2. Identify & Score Risks

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and:
- Identify risks using brainstorming, SWOT, and pre-mortem techniques
- Score each risk (Probability × Impact)
- Define response strategies (avoid, mitigate, transfer, accept)

### 3. Output

Deliver the risk register as a table with IDs, scores, owners, and response plans. Highlight the top 5 risks. Offer to save to ~~docs if connected.
```

**Step 5: Write communication-plan.md**

```markdown
---
description: Define stakeholder communication cadence, channels, and ownership
argument-hint: "<project name>"
---

# Communication Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a communication plan covering who needs what information, how often, through which channels.

## Usage

```
/communication-plan <project name>
```

### Arguments

- `project name` — The project to plan communications for

## Workflow

### 1. Gather Context

Ask about: stakeholder list, team structure, reporting requirements, existing communication channels. Check ~~docs for stakeholder map.

### 2. Build Plan

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create:
- Communication matrix (audience, message, frequency, channel, owner)
- RACI matrix for key decisions
- Escalation path

### 3. Output

Deliver the communication plan and RACI matrix. Offer to set up channels in ~~messaging or recurring events in ~~calendar if connected.
```

**Step 6: Commit**

```bash
git add project-management/commands/wbs.md project-management/commands/schedule.md project-management/commands/resource-plan.md project-management/commands/risk-register.md project-management/commands/communication-plan.md
git commit -m "feat(project-management): add planning commands — wbs, schedule, resource-plan, risk-register, communication-plan"
```

---

## Task 9: Execution Commands (4 commands)

**Files:**
- Create: `project-management/commands/standup.md`
- Create: `project-management/commands/sprint-plan.md`
- Create: `project-management/commands/decision-log.md`
- Create: `project-management/commands/change-request.md`

**Step 1: Write standup.md**

```markdown
---
description: Generate daily standup summaries or async standup templates
argument-hint: "<team or project> [sync|async]"
---

# Standup

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate standup summaries from project data or create async standup templates for your team.

## Usage

```
/standup <team or project> [sync|async]
```

### Arguments

- `team or project` — The team or project to run standups for
- `sync|async` — (Optional) Standup format:
  - `sync` — In-person or video standup agenda and facilitation guide
  - `async` — Slack/messaging template for asynchronous daily updates
  - If not specified, ask about the team's preference

## Workflow

### 1. Gather Context

Ask about: team size, sprint/phase status, known blockers. Check ~~project-tracker for recent activity and ~~messaging for existing standup channels.

### 2. Generate

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and create the standup format.

### 3. Output

Deliver the standup template or summary. For async: provide a copy-paste message template for ~~messaging. For sync: provide a facilitation guide with time-boxes.
```

**Step 2: Write sprint-plan.md**

```markdown
---
description: Plan a sprint or iteration with scope, capacity, and commitments
argument-hint: "<team or project> [sprint-number]"
---

# Sprint Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Plan a sprint or iteration — calculate capacity, select scope, set a sprint goal, and define commitments.

## Usage

```
/sprint-plan <team or project> [sprint-number]
```

### Arguments

- `team or project` — The team or project to plan the sprint for
- `sprint-number` — (Optional) The sprint number or iteration name

## Workflow

### 1. Gather Inputs

Ask about: team members and availability, sprint length, backlog priorities, carry-over items, dependencies. Check ~~project-tracker for backlog and velocity data.

### 2. Plan Sprint

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and:
- Calculate team capacity
- Select stories/tasks from backlog
- Set sprint goal
- Identify risks and dependencies for this sprint

### 3. Output

Deliver the sprint plan: goal, committed items with estimates, capacity breakdown, risks. Offer to update ~~project-tracker with sprint assignments.
```

**Step 3: Write decision-log.md**

```markdown
---
description: Record and track project decisions with context and rationale
argument-hint: "<decision summary>"
---

# Decision Log

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Record a project decision with full context, rationale, alternatives considered, and impact.

## Usage

```
/decision-log <decision summary>
```

### Arguments

- `decision summary` — A brief description of the decision to record

## Workflow

### 1. Gather Context

Ask about: what was decided, why, what alternatives were considered, who made the decision, what's affected. Check ~~docs for existing decision log.

### 2. Record Decision

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and create a structured decision record.

### 3. Output

Deliver the decision record. Append to existing decision log if one exists in ~~docs, or create a new one.
```

**Step 4: Write change-request.md**

```markdown
---
description: Draft a formal change request with impact analysis
argument-hint: "<change description>"
---

# Change Request

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Draft a formal change request documenting the proposed change, justification, and impact on scope, schedule, and cost.

## Usage

```
/change-request <change description>
```

### Arguments

- `change description` — A brief description of the proposed change

## Workflow

### 1. Gather Context

Ask about: what's changing, why, who requested it, what's the urgency. Check ~~project-tracker for affected work items and ~~docs for the current project plan.

### 2. Analyze Impact

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and create:
- Change request with full description
- Impact analysis (scope, schedule, cost, risk)
- Recommendation (approve, defer, reject)

### 3. Output

Deliver the change request document. Flag if this change would affect the critical path or trigger a re-plan.
```

**Step 5: Commit**

```bash
git add project-management/commands/standup.md project-management/commands/sprint-plan.md project-management/commands/decision-log.md project-management/commands/change-request.md
git commit -m "feat(project-management): add execution commands — standup, sprint-plan, decision-log, change-request"
```

---

## Task 10: Monitoring Commands (5 commands)

**Files:**
- Create: `project-management/commands/status-report.md`
- Create: `project-management/commands/burndown.md`
- Create: `project-management/commands/risk-review.md`
- Create: `project-management/commands/dependency-tracker.md`
- Create: `project-management/commands/health-check.md`

**Step 1: Write status-report.md**

```markdown
---
description: Generate a project status report in RAG format
argument-hint: "<project name> [executive|team|steering]"
---

# Status Report

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a project status report with RAG (Red/Amber/Green) indicators across key dimensions.

## Usage

```
/status-report <project name> [executive|team|steering]
```

### Arguments

- `project name` — The project to report on
- `executive|team|steering` — (Optional) Audience level:
  - `executive` — 3-bullet summary with RAG, key risks, decisions needed
  - `team` — Full detail: progress, metrics, blockers, upcoming work
  - `steering` — Steering committee format: RAG dashboard, decisions required, budget status
  - If not specified, ask about the audience

## Workflow

### 1. Gather Data

Ask about: what happened this period, blockers, upcoming milestones. Check ~~project-tracker for progress data and ~~docs for previous status reports.

### 2. Compile Report

Use the **Monitoring** skill. Read `../skills/monitoring/SKILL.md` and generate the status report.

### 3. Output

Deliver the status report formatted for the target audience. Offer to post to ~~messaging or save to ~~docs if connected.
```

**Step 2: Write burndown.md**

```markdown
---
description: Analyze sprint or project burndown and forecast completion
argument-hint: "<project or sprint> [sprint|release|project]"
---

# Burndown

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Analyze burndown data and forecast completion for a sprint, release, or project.

## Usage

```
/burndown <project or sprint> [sprint|release|project]
```

### Arguments

- `project or sprint` — The sprint, release, or project to analyze
- `sprint|release|project` — (Optional) Burndown scope:
  - `sprint` — Sprint burndown: story points remaining vs. ideal line
  - `release` — Release burndown: features remaining across sprints
  - `project` — Project burndown: milestones or earned value over time
  - If not specified, ask about the scope

## Workflow

### 1. Gather Data

Ask about: remaining work, completed work, time elapsed, team velocity. Check ~~project-tracker for burndown data.

### 2. Analyze & Forecast

Use the **Monitoring** skill. Read `../skills/monitoring/SKILL.md` and:
- Analyze current burndown shape
- Forecast completion date
- Identify warning signs

### 3. Output

Deliver the burndown analysis with forecast and recommendations. Flag if the current trajectory won't meet the target date.
```

**Step 3: Write risk-review.md**

```markdown
---
description: Review and update the project risk register
argument-hint: "<project name>"
---

# Risk Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Review and update the risk register — re-score existing risks, identify new ones, and close resolved risks.

## Usage

```
/risk-review <project name>
```

### Arguments

- `project name` — The project to review risks for

## Workflow

### 1. Gather Current State

Ask about: current project status, recent issues, upcoming concerns. Check ~~docs for the existing risk register.

### 2. Review Risks

Use the **Monitoring** skill. Read `../skills/monitoring/SKILL.md` and:
- Re-score existing risks based on current information
- Identify new risks
- Close risks that have been resolved or are no longer relevant
- Check if any risk triggers have fired

### 3. Output

Deliver the updated risk register with changes highlighted. Flag any risks that have escalated to issues.
```

**Step 4: Write dependency-tracker.md**

```markdown
---
description: Map and track cross-team or cross-project dependencies
argument-hint: "<project name>"
---

# Dependency Tracker

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map and track dependencies between teams, projects, or external parties.

## Usage

```
/dependency-tracker <project name>
```

### Arguments

- `project name` — The project to track dependencies for

## Workflow

### 1. Gather Dependencies

Ask about: what does this project depend on from others? What do others depend on from this project? Check ~~project-tracker for linked issues and blocking items.

### 2. Map & Assess

Use the **Monitoring** skill. Read `../skills/monitoring/SKILL.md` and create:
- Dependency map with status for each dependency
- Critical path impact for blocked dependencies
- Escalation recommendations for at-risk dependencies

### 3. Output

Deliver the dependency map and status report. Flag any blocked or at-risk dependencies with recommended actions.
```

**Step 5: Write health-check.md**

```markdown
---
description: Run a multi-dimensional project health assessment — triggers the orchestrator
argument-hint: "<project name>"
---

# Health Check

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a comprehensive project health check assessing schedule, scope, budget, team, risk, and stakeholder dimensions.

**This command triggers the orchestrator agent** for cross-stage assessment.

## Usage

```
/health-check <project name>
```

### Arguments

- `project name` — The project to assess

## Workflow

### 1. Activate Orchestrator

Read the orchestrator at `../agents/orchestrator.md`. This command triggers the "Project health check" routing path.

### 2. Cross-Stage Assessment

The orchestrator sequences:
1. **Planning check** — Scope/schedule alignment, WBS completeness
2. **Execution check** — Team velocity, sprint health, blockers
3. **Monitoring pull** — RAG status, burndown trajectory, risk state
4. **Synthesis** — Unified health report with alignment flags

### 3. Output

Deliver the health check report with scores per dimension. If any plan-vs-reality divergence is detected, include an **Alignment Flag** section with resolution options.
```

**Step 6: Commit**

```bash
git add project-management/commands/status-report.md project-management/commands/burndown.md project-management/commands/risk-review.md project-management/commands/dependency-tracker.md project-management/commands/health-check.md
git commit -m "feat(project-management): add monitoring commands — status-report, burndown, risk-review, dependency-tracker, health-check"
```

---

## Task 11: Closing Commands (3 commands)

**Files:**
- Create: `project-management/commands/retro.md`
- Create: `project-management/commands/lessons-learned.md`
- Create: `project-management/commands/project-closeout.md`

**Step 1: Write retro.md**

```markdown
---
description: Facilitate a retrospective in multiple formats
argument-hint: "<team or project> [start-stop-continue|mad-sad-glad|4ls|sailboat|timeline]"
---

# Retro

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Facilitate a retrospective using one of several proven formats.

## Usage

```
/retro <team or project> [start-stop-continue|mad-sad-glad|4ls|sailboat|timeline]
```

### Arguments

- `team or project` — The team or project to run the retro for
- `start-stop-continue|mad-sad-glad|4ls|sailboat|timeline` — (Optional) Retro format:
  - `start-stop-continue` — Simple three-column retro, good for new teams
  - `mad-sad-glad` — Emotional temperature check
  - `4ls` — Liked/Learned/Lacked/Longed For — comprehensive
  - `sailboat` — Visual metaphor: Wind/Anchor/Rocks/Island
  - `timeline` — Walk through the sprint/project chronologically
  - If not specified, recommend based on team maturity and context

## Workflow

### 1. Gather Context

Ask about: what period are we reflecting on? How is the team feeling? Any known issues? Check ~~project-tracker for sprint data.

### 2. Facilitate

Use the **Closing** skill. Read `../skills/closing/SKILL.md` and generate the retro structure with facilitation guide.

### 3. Output

Deliver the retro board template, facilitation guide with time-boxes, and action item tracker. Offer to post to ~~messaging or ~~docs if connected.
```

**Step 2: Write lessons-learned.md**

```markdown
---
description: Compile lessons learned into a structured knowledge document
argument-hint: "<project name>"
---

# Lessons Learned

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Compile lessons learned from a project or phase into a structured document for organizational knowledge.

## Usage

```
/lessons-learned <project name>
```

### Arguments

- `project name` — The project to capture lessons from

## Workflow

### 1. Gather Inputs

Ask about: what went well, what didn't, surprises, what would you do differently. Check ~~docs for retro notes and ~~project-tracker for project history.

### 2. Compile

Use the **Closing** skill. Read `../skills/closing/SKILL.md` and organize lessons by category with root causes and recommendations.

### 3. Output

Deliver the lessons learned document. Flag lessons that apply organization-wide vs. project-specific. Offer to save to ~~docs as a knowledge base entry.
```

**Step 3: Write project-closeout.md**

```markdown
---
description: Generate a project closeout report with handoff checklist
argument-hint: "<project name> [software|general]"
---

# Project Closeout

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a comprehensive project closeout report and handoff checklist.

## Usage

```
/project-closeout <project name> [software|general]
```

### Arguments

- `project name` — The project to close out
- `software|general` — (Optional) PM context:
  - `software` — Includes release notes, runbook handoff, tech debt register, on-call transition
  - `general` — Includes formal acceptance, contract closure, benefits realization plan
  - If not specified, ask about the project type

## Workflow

### 1. Gather Status

Ask about: were all deliverables accepted? Any open items? Final budget status? Check ~~project-tracker for open items and ~~docs for project documentation.

### 2. Compile Closeout

Use the **Closing** skill. Read `../skills/closing/SKILL.md` and create:
- Closeout report (objectives vs. actuals)
- Handoff checklist
- Lessons learned summary

### 3. Output

Deliver the closeout report and checklist. Flag any incomplete items that need resolution before formal closure.
```

**Step 4: Commit**

```bash
git add project-management/commands/retro.md project-management/commands/lessons-learned.md project-management/commands/project-closeout.md
git commit -m "feat(project-management): add closing commands — retro, lessons-learned, project-closeout"
```

---

## Task 12: Orchestrator Agent

**Files:**
- Create: `project-management/agents/orchestrator.md`
- Create: `project-management/agents/README.md`

**Step 1: Write orchestrator.md**

Create `project-management/agents/orchestrator.md`. This is the routing agent for multi-stage project management workflows.

Reference: Study `product-management/agents/orchestrator.md` for structure and adapt for project lifecycle stages.

Content must include:
- H1: "Agent: Project Management Orchestrator"
- **How It Works** section: classify request → select skills → sequence execution → synthesize output. Execution model: single-pass synthesis (snapshot, not live loop). Re-entry is a separate invocation.
- **Request Classification** section with code block showing:
  - Request type: Health Check, Stakeholder Update, New Project Setup, Project Recovery, Project Closeout, Single-Stage
  - Complexity: Simple (1 skill), Moderate (2-3 skills), Complex (4-5 skills)
  - Context: Software or General PM mode
- **Skill Registry** table mapping skills to their file paths (S1-S5)
- **Forward Routing Rules** — 6 named routes:
  - Route 1: Project Health Check (Planning → Execution → Monitoring → Report)
  - Route 2: Stakeholder Update (Monitoring → Synthesis formatted for audience)
  - Route 3: New Project Setup (Initiation → Planning → Execution first sprint/phase)
  - Route 4: Project Recovery (Monitoring → Planning → Execution revised plan)
  - Route 5: Project Closeout (Monitoring → Closing)
  - Single-stage passthrough
- **Bidirectional Re-entry Routing** section with both backward AND forward paths:
  - Backward: schedule slip → Planning, resource conflict → Planning, risk materialized → Planning or Execution, scope creep → Initiation or Planning, stakeholder misalignment → Initiation
  - Forward: replanning complete → resume Execution, risk resolved → resume Execution, charter amended → resume Planning, change request approved → resume Execution, resource conflict resolved → resume Execution
  - Context tracking: what triggered re-entry and why
- **Conflict Escalation** section with severity thresholds:
  - Low (< 10% slip, minor resource shift): noted in report, no flag
  - Medium (10-25% slip, scope change without CR): Alignment Flag raised
  - High (> 25% slip, critical risk materialized, sponsor misalignment): Alignment Flag with "requires immediate decision" marker
  - Flag format: planned vs. happening, gap description, severity, 2-3 resolution options, never auto-resolves
- **Partial Data Protocol**: if a skill returns incomplete data — flag gap, proceed with available data, mark confidence level, surface Data Gap callout
- **Synthesis Template** in code block — inlined, self-contained (not referencing product-management):
  - Project name, assessment type, context, skills deployed, date, execution model
  - Executive summary
  - Sections per skill (Initiation, Planning, Execution, Monitoring, Closing — only deployed ones)
  - Alignment Flags (if any)
  - Data Gaps (if any)
  - Recommendations and next steps
  - Assumptions & gaps
- **Handling Partial Information** section: analyze what's available, flag gaps, provide confidence levels

**Step 2: Write agents/README.md**

```markdown
# Agents

## Orchestrator

The Project Management Orchestrator routes multi-stage requests across lifecycle skills and synthesizes outputs into unified reports.

| Agent | File | Role |
|-------|------|------|
| Orchestrator | [orchestrator.md](./orchestrator.md) | Classify requests, route to skills, synthesize cross-stage outputs |

See [orchestrator.md](./orchestrator.md) for routing logic, conflict escalation thresholds, and synthesis templates.
```

**Step 3: Commit**

```bash
git add project-management/agents/orchestrator.md project-management/agents/README.md
git commit -m "feat(project-management): add orchestrator agent with bidirectional routing, severity thresholds, and partial data protocol"
```

---

## Task 13: Commands README

**Files:**
- Create: `project-management/commands/README.md`

**Step 1: Write commands/README.md**

```markdown
# Commands

20 slash commands organized by project lifecycle stage.

## Initiation

| Command | Description |
|---------|-------------|
| [/project-charter](./project-charter.md) | Define project scope, objectives, stakeholders, and success criteria |
| [/stakeholder-map](./stakeholder-map.md) | Map stakeholders by influence/interest with engagement strategies |
| [/kickoff](./kickoff.md) | Generate a kickoff meeting agenda and preparation checklist |

## Planning

| Command | Description |
|---------|-------------|
| [/wbs](./wbs.md) | Create a work breakdown structure |
| [/schedule](./schedule.md) | Build a project schedule with milestones and dependencies |
| [/resource-plan](./resource-plan.md) | Plan team allocation, roles, and capacity |
| [/risk-register](./risk-register.md) | Create a risk register with mitigation strategies |
| [/communication-plan](./communication-plan.md) | Define stakeholder communication cadence and channels |

## Execution

| Command | Description |
|---------|-------------|
| [/standup](./standup.md) | Generate daily standup summaries or async standup templates |
| [/sprint-plan](./sprint-plan.md) | Plan a sprint or iteration with scope, capacity, and commitments |
| [/decision-log](./decision-log.md) | Record and track project decisions with context and rationale |
| [/change-request](./change-request.md) | Draft a formal change request with impact analysis |

## Monitoring

| Command | Description |
|---------|-------------|
| [/status-report](./status-report.md) | Generate a project status report (RAG format) |
| [/burndown](./burndown.md) | Analyze sprint/project burndown and forecast completion |
| [/risk-review](./risk-review.md) | Review and update the risk register |
| [/dependency-tracker](./dependency-tracker.md) | Map and track cross-team or cross-project dependencies |
| [/health-check](./health-check.md) | Run a project health assessment (triggers orchestrator) |

## Closing

| Command | Description |
|---------|-------------|
| [/retro](./retro.md) | Facilitate a retrospective in multiple formats |
| [/lessons-learned](./lessons-learned.md) | Compile lessons learned into a structured document |
| [/project-closeout](./project-closeout.md) | Generate a project closeout report with handoff checklist |
```

**Step 2: Commit**

```bash
git add project-management/commands/README.md
git commit -m "feat(project-management): add commands README with all 20 commands"
```

---

## Task 14: Plugin README

**Files:**
- Create: `project-management/README.md`

**Step 1: Write README.md**

```markdown
# Project Management

Project management workflows from initiation to closing — charters, WBS, scheduling, risk registers, sprint planning, status reports, retrospectives, and project closeout for software and general PMs.

> **Important**: This plugin assists with project management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and your team before making project decisions.

## Skills

| Skill | Description |
| :--- | :--- |
| [Initiation](./skills/initiation/SKILL.md) | Project charters, stakeholder mapping, and kickoff planning |
| [Planning](./skills/planning/SKILL.md) | WBS, scheduling, resource planning, risk management, and communication planning |
| [Execution](./skills/execution/SKILL.md) | Standups, sprint planning, decision tracking, and change management |
| [Monitoring](./skills/monitoring/SKILL.md) | Status reports, burndown analysis, risk reviews, dependency tracking, and health checks |
| [Closing](./skills/closing/SKILL.md) | Retrospectives, lessons learned, and project closeout |

## Commands

20 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Agents

| Agent | Description |
| :--- | :--- |
| [Orchestrator](./agents/orchestrator.md) | Routes multi-stage requests across lifecycle skills, supports bidirectional re-entry, severity-based conflict escalation, and partial data handling |

## Hooks

None.

## Software vs. General PM

Every skill supports both modes. Commands accept an optional mode hint (e.g., `/schedule my-project sprint-based` or `/project-closeout my-project general`). When no mode is specified, the command asks about your project context and recommends the appropriate approach.

## MCP Integration

Connect your project tools via MCP servers for the richest experience. See [CONNECTORS.md](./CONNECTORS.md) for details.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **project-management**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/project-management
```
```

**Step 2: Commit**

```bash
git add project-management/README.md
git commit -m "feat(project-management): add plugin README"
```

---

## Task 15: Update Root README

**Files:**
- Modify: `README.md` (root)

**Step 1: Add project-management to the Available Plugins table**

In the root `README.md`, add a row to the Available Plugins table after the Product Management row:

```markdown
| **[Project Management](./project-management/)** | 5 | 20 | 1 | — | Project management from initiation to closing — charters, WBS, scheduling, risk registers, sprint planning, status reports, retrospectives, and closeout for software and general PMs. |
```

Update the totals row to reflect the new counts: Skills +5, Commands +20, Agents +1.

Also add `project-management/` to the Repository Structure tree.

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add project-management plugin to root README"
```

---

## Summary

| Task | What | Files | Commit |
|------|------|-------|--------|
| 1 | Plugin scaffold | plugin.json, .mcp.json, CONNECTORS.md | `feat(project-management): scaffold plugin metadata, MCP config, and connectors` |
| 2 | Initiation skill | skills/initiation/SKILL.md | `feat(project-management): add initiation skill` |
| 3 | Planning skill | skills/planning/SKILL.md | `feat(project-management): add planning skill` |
| 4 | Execution skill | skills/execution/SKILL.md | `feat(project-management): add execution skill` |
| 5 | Monitoring skill | skills/monitoring/SKILL.md | `feat(project-management): add monitoring skill` |
| 6 | Closing skill | skills/closing/SKILL.md | `feat(project-management): add closing skill` |
| 7 | Initiation commands (3) | commands/project-charter.md, stakeholder-map.md, kickoff.md | `feat(project-management): add initiation commands` |
| 8 | Planning commands (5) | commands/wbs.md, schedule.md, resource-plan.md, risk-register.md, communication-plan.md | `feat(project-management): add planning commands` |
| 9 | Execution commands (4) | commands/standup.md, sprint-plan.md, decision-log.md, change-request.md | `feat(project-management): add execution commands` |
| 10 | Monitoring commands (5) | commands/status-report.md, burndown.md, risk-review.md, dependency-tracker.md, health-check.md | `feat(project-management): add monitoring commands` |
| 11 | Closing commands (3) | commands/retro.md, lessons-learned.md, project-closeout.md | `feat(project-management): add closing commands` |
| 12 | Orchestrator agent | agents/orchestrator.md, agents/README.md | `feat(project-management): add orchestrator agent` |
| 13 | Commands README | commands/README.md | `feat(project-management): add commands README` |
| 14 | Plugin README | README.md | `feat(project-management): add plugin README` |
| 15 | Root README update | README.md (root) | `docs: add project-management to root README` |

**Total: 15 tasks, 31 files, 15 commits**
