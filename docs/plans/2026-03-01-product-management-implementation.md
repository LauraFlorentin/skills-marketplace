# Product Management Plugin — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the product-management plugin with 5 lifecycle skills, 19 commands, 1 orchestrator agent, and MCP connectors.

**Architecture:** Hybrid plugin — skills + commands for direct workflows, orchestrator agent for cross-cutting multi-stage requests. Startup and enterprise PM modes separated within each skill.

**Tech Stack:** Markdown (SKILL.md, commands, orchestrator), JSON (plugin.json, .mcp.json)

**Design Doc:** `docs/plans/2026-03-01-product-management-design.md`

**Reference Plugins:** Study `management-consulting/` for skills+commands pattern, `real-estate-investment/` for orchestrator agent pattern.

---

## Task 1: Scaffold Plugin Structure & Metadata

**Files:**
- Create: `product-management/.claude-plugin/plugin.json`
- Create: `product-management/.mcp.json`
- Create: `product-management/CONNECTORS.md`

**Step 1: Create plugin.json**

Create `product-management/.claude-plugin/plugin.json`:

```json
{
    "name": "product-management",
    "version": "1.0.0",
    "description": "Product management workflows from strategy to growth — vision docs, PRDs, roadmaps, user research, prioritization, GTM, analytics, and product reviews for startup and enterprise PMs.",
    "author": {
        "name": "LauraFlorentin"
    },
    "repository": "https://github.com/LauraFlorentin/skills-marketplace",
    "license": "MIT",
    "skills": "./skills/",
    "commands": "./commands/",
    "keywords": [
        "product",
        "pm",
        "roadmap",
        "prd",
        "discovery",
        "okr",
        "prioritization",
        "gtm",
        "analytics",
        "user-research"
    ]
}
```

**Step 2: Create .mcp.json**

Create `product-management/.mcp.json`:

```json
{
    "mcpServers": {
        "linear": {
            "type": "http",
            "url": "https://linear.mcp.claude.com/mcp"
        },
        "notion": {
            "type": "http",
            "url": "https://notion.mcp.claude.com/mcp"
        },
        "posthog": {
            "type": "http",
            "url": "https://posthog.mcp.claude.com/mcp"
        },
        "slack": {
            "type": "http",
            "url": "https://mcp.slack.com/mcp"
        },
        "figma": {
            "type": "http",
            "url": "https://figma.mcp.claude.com/mcp"
        }
    }
}
```

Note: Use `"type": "http"` with `"url"` to match the convention in `management-consulting/.mcp.json`.

**Step 3: Create CONNECTORS.md**

Create `product-management/CONNECTORS.md`:

```markdown
# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~project-tracker` might mean Linear, Jira, Asana, or any other project tracker with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Roadmap & planning | `~~roadmap-tool` | Linear, Notion | Productboard, Aha! |
| Product analytics | `~~analytics` | PostHog | Amplitude, Mixpanel, Heap |
| Tickets & sprints | `~~project-tracker` | Linear | Jira, Shortcut, Asana |
| Documentation | `~~docs` | Notion | Confluence, Google Docs |
| Research repository | `~~research-repo` | Notion | Dovetail, EnjoyHQ |
| Team communication | `~~messaging` | Slack | Microsoft Teams |
| Design files | `~~design` | Figma | — |

## Shared tool note

`~~research-repo` and `~~docs` can point to the same tool (e.g., Notion). Configure the tool once — no duplicate configuration needed.
```

**Step 4: Commit**

```bash
git add product-management/.claude-plugin/plugin.json product-management/.mcp.json product-management/CONNECTORS.md
git commit -m "feat(product-management): scaffold plugin metadata, MCP config, and connectors"
```

---

## Task 2: Strategy Skill

**Files:**
- Create: `product-management/skills/strategy/SKILL.md`

**Step 1: Write the Strategy skill**

Create `product-management/skills/strategy/SKILL.md`. This skill covers product vision, OKRs, and competitive analysis with startup and enterprise modes.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Product Strategy"
- Disclaimer about outputs needing stakeholder review
- **Product Vision** section with:
  - Startup mode: Lean canvas (Problem, Solution, UVP, Unfair Advantage, Channels, Customer Segments, Revenue Streams, Cost Structure, Key Metrics), elevator pitch template
  - Enterprise mode: Full vision doc structure (Vision statement, Strategic context, Target customer, Value proposition, Key differentiators, Success metrics, Stakeholder alignment matrix, Review cadence)
- **OKRs** section with:
  - OKR writing principles (measurable, time-bound, ambitious but achievable)
  - Startup mode: Team-level quarterly OKRs, 1 objective + 3-4 key results template
  - Enterprise mode: Cascading OKRs — company → department → team, dependency mapping, cross-team alignment scoring
  - Anti-patterns: vanity metrics, too many objectives, activity-based KRs
- **Competitive Analysis** section with:
  - Startup mode: Quick landscape scan — who are the top 5 competitors, what do they do well, where are the gaps
  - Enterprise mode: Full competitive matrix — feature parity grid (scored 1-5 across dimensions), positioning map (2-axis), competitive threat assessment (market share, funding, product velocity, talent), SWOT per competitor
  - Data sources: G2, Capterra, LinkedIn, Crunchbase, press releases, product changelogs
- **Output Formats** section: vision doc template, OKR spreadsheet spec, competitive matrix template

Reference: Study `management-consulting/skills/research-analysis/SKILL.md` for depth, structure, and methodology patterns. Match that level of detail.

**Step 2: Commit**

```bash
git add product-management/skills/strategy/SKILL.md
git commit -m "feat(product-management): add strategy skill — vision, OKRs, competitive analysis"
```

---

## Task 3: Discovery Skill

**Files:**
- Create: `product-management/skills/discovery/SKILL.md`

**Step 1: Write the Discovery skill**

Create `product-management/skills/discovery/SKILL.md`. This skill covers user research, personas, jobs-to-be-done, and opportunity scoring.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Product Discovery"
- Disclaimer about research needing validation with real users
- **User Research** section with:
  - Startup mode: Guerrilla research — intercept interviews, unmoderated surveys (Typeform, Google Forms), 5-user tests (Nielsen), recording tools (Loom, Hotjar)
  - Enterprise mode: Formal research plans — recruiting criteria, screener surveys, moderated 1:1 interviews (60 min protocol), research repository structure, stakeholder readout format
  - Interview guide template: opening (rapport), exploration (open questions), deep dive (specific scenarios), closing (summary + next steps)
  - Synthesis methods: affinity mapping, thematic coding, insight statements ("We observed [behavior] because [motivation], which means [implication]")
- **Personas** section with:
  - Startup mode: Proto-personas — name, photo, role, goals (3), frustrations (3), tools used, one-line quote. Build from founder intuition + 5-10 conversations.
  - Enterprise mode: Data-backed personas — demographic data, behavioral segmentation, purchase journey mapping, Jobs-to-be-Done integration, persona validation metrics, review cadence (quarterly)
  - Template for each mode
- **Jobs-to-be-Done** section with:
  - Job statement format: "When I [situation], I want to [motivation], so I can [expected outcome]"
  - Job map: define, locate, prepare, confirm, execute, monitor, modify, conclude
  - Startup mode: Quick job stories (3-5 core jobs)
  - Enterprise mode: Full JTBD framework — outcome-driven innovation, importance vs. satisfaction matrix, over-served / under-served / appropriately-served classification
- **Opportunity Scoring** section with:
  - Opportunity Solution Trees (Teresa Torres): outcome → opportunities → solutions → experiments
  - Scoring criteria: reach, impact, confidence, effort
  - Startup mode: Simple scoring spreadsheet
  - Enterprise mode: Weighted multi-criteria with stakeholder input, confidence-weighted estimates

**Step 2: Commit**

```bash
git add product-management/skills/discovery/SKILL.md
git commit -m "feat(product-management): add discovery skill — research, personas, JTBD, opportunity scoring"
```

---

## Task 4: Planning Skill

**Files:**
- Create: `product-management/skills/planning/SKILL.md`

**Step 1: Write the Planning skill**

Create `product-management/skills/planning/SKILL.md`. This skill covers roadmaps, PRDs, feature specs, prioritization, and backlog grooming.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Product Planning"
- **Roadmapping** section with:
  - Startup mode: Now/Next/Later format — no dates, theme-based, fits on one page, update weekly
  - Enterprise mode: Timeline roadmap — quarterly milestones, cross-team dependencies (RACI), swim lanes by team/product area, milestone gates, executive review format
  - Roadmap communication: audience-specific views (board, exec, engineering, customers)
  - Anti-patterns: feature factories, date-driven roadmaps without outcomes, roadmap-as-contract
- **PRDs** section with:
  - Startup mode: 1-pager PRD — problem statement, proposed solution, success metrics (2-3), scope (in/out), key risks, open questions
  - Enterprise mode: Full PRD — background & strategic context, user stories with acceptance criteria, functional requirements, non-functional requirements (performance, security, accessibility, i18n), technical considerations, edge cases, analytics instrumentation plan, rollout plan, dependencies, approvals
  - PRD quality checklist: Is the problem validated? Are success metrics measurable? Are edge cases covered? Is scope clearly bounded?
- **Feature Specs** section with:
  - User story format: "As a [persona], I want [action], so that [outcome]"
  - Acceptance criteria: Given/When/Then format
  - Design integration: wireframe references, interaction specs, error states
  - Technical spec section: API contracts, data models, migration needs
- **Prioritization** section with:
  - RICE scoring: Reach (users/quarter) x Impact (0.25/0.5/1/2/3) x Confidence (%) / Effort (person-months)
  - ICE scoring: Impact (1-10) x Confidence (1-10) x Ease (1-10)
  - MoSCoW: Must have, Should have, Could have, Won't have (this time)
  - Weighted scoring: Custom criteria with stakeholder-assigned weights
  - Startup mode: ICE for speed, gut-check validation
  - Enterprise mode: RICE with stakeholder input matrix, weighted scoring for cross-team decisions
  - When to use which framework (decision guide)
- **Backlog Grooming** section with:
  - Story point estimation: Fibonacci sequence, planning poker
  - Backlog health metrics: % groomed, avg age of items, items per sprint ratio
  - Grooming ceremony structure: review incoming, estimate, prioritize, split large stories
  - Definition of Ready checklist

**Step 2: Commit**

```bash
git add product-management/skills/planning/SKILL.md
git commit -m "feat(product-management): add planning skill — roadmaps, PRDs, specs, prioritization, backlog"
```

---

## Task 5: Launch & Growth Skill

**Files:**
- Create: `product-management/skills/launch-growth/SKILL.md`

**Step 1: Write the Launch & Growth skill**

Create `product-management/skills/launch-growth/SKILL.md`. This skill covers GTM, launches, A/B tests, and growth experiments.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Launch & Growth"
- **Go-to-Market** section with:
  - Startup mode: Lean GTM — target early adopters, Product Hunt / Hacker News launch, beta waitlist, founder-led sales, community seeding, content marketing basics
  - Enterprise mode: Cross-functional GTM — sales enablement (battle cards, objection handling, demo scripts), marketing launch plan (press, analyst briefings, webinars), customer success readiness (training, documentation, support runbooks), partner channel activation
  - GTM checklist template (both modes)
  - Pricing strategy basics: value-based, competitor-based, cost-plus; freemium vs. trial vs. paid-only decision framework
- **Launch Management** section with:
  - Startup mode: Simple launch checklist — feature complete, basic QA, landing page live, analytics instrumented, support email ready, social posts drafted
  - Enterprise mode: Phased rollout — internal dogfood → beta users → % rollout → GA. Feature flags strategy, rollback plan, monitoring dashboards, incident response, launch communication plan (internal + external), stakeholder sign-off matrix
  - Launch day run-of-show template
  - Post-launch review template (what went well, what didn't, metrics vs. targets)
- **A/B Testing** section with:
  - Hypothesis format: "We believe [change] will cause [effect] for [segment], which we'll measure by [metric] over [timeframe]"
  - Test design: control vs. variant, sample size calculation (significance level, power, MDE), test duration estimation
  - Startup mode: Quick tests — fake door tests, painted door tests, Wizard of Oz, concierge MVP
  - Enterprise mode: Structured experimentation — multi-variant tests, holdout groups, sequential testing, Bayesian vs. frequentist approaches, guardrail metrics
  - Common pitfalls: peeking, underpowered tests, multiple comparison problem, novelty effects
- **Growth Experiments** section with:
  - Pirate metrics (AARRR): Acquisition, Activation, Retention, Revenue, Referral
  - Growth loop types: viral loops, content loops, paid loops, sales loops
  - Experiment design: hypothesis, metric, effort, timeline, expected impact
  - ICE scoring for experiment prioritization
  - Startup mode: High-tempo testing (1-2 experiments/week), qualitative signals OK
  - Enterprise mode: Growth team structure, experiment review board, statistical rigor, portfolio approach

**Step 2: Commit**

```bash
git add product-management/skills/launch-growth/SKILL.md
git commit -m "feat(product-management): add launch-growth skill — GTM, launches, A/B tests, growth experiments"
```

---

## Task 6: Product Analytics Skill

**Files:**
- Create: `product-management/skills/product-analytics/SKILL.md`

**Step 1: Write the Product Analytics skill**

Create `product-management/skills/product-analytics/SKILL.md`. This skill covers metrics frameworks, dashboards, sprint reviews, and product reviews.

Content must include:
- YAML frontmatter: `name`, `description`, `triggers` list
- H1 title: "Product Analytics"
- **Metrics Frameworks** section with:
  - North Star Metric: definition, properties (measures value, leading indicator, actionable), examples by product type (marketplace: GMV, SaaS: weekly active users, media: time spent)
  - Input metrics: the 3-5 levers that drive the North Star
  - Startup mode: North Star + 3-5 key metrics, single dashboard
  - Enterprise mode: Metrics hierarchy — company-level North Star → team-level input metrics → feature-level instrumentation. Leading vs. lagging indicators. Counter-metrics (guardrails)
  - Metric quality checklist: Is it measurable? Actionable? Understandable? Comparable over time?
- **Dashboard Design** section with:
  - Startup mode: Single-page scorecard — North Star trend, input metrics, acquisition funnel, retention curve
  - Enterprise mode: Multi-level dashboards — executive (North Star, revenue, growth rate), team-level (feature adoption, funnel conversion, NPS), feature-level (usage, errors, latency)
  - Dashboard spec template: metric name, definition, data source, refresh cadence, owner, alert thresholds
  - Visualization best practices: choose chart type by data type, avoid vanity metrics, show trends not snapshots
- **Sprint Review** section with:
  - What shipped: features, fixes, improvements (with links)
  - Metrics impact: what moved, what didn't, why
  - User feedback: qualitative signals from support, interviews, NPS
  - Startup mode: Weekly standup format — 5-min update, async-friendly
  - Enterprise mode: Formal sprint review — demo, metrics readout, stakeholder Q&A, action items
  - Template for both modes
- **Product Review** section with:
  - Cross-cutting assessment (triggers orchestrator agent)
  - Strategy alignment: Are we building toward the vision? Are OKRs on track?
  - Discovery health: Are we talking to users? Are insights feeding the roadmap?
  - Execution quality: Sprint velocity, defect rate, cycle time
  - Growth metrics: Funnel performance, retention cohorts, revenue trends
  - Startup mode: Monthly lightweight review
  - Enterprise mode: Quarterly business review (QBR) with deep dives, board-ready format
  - Product review output template

**Step 2: Commit**

```bash
git add product-management/skills/product-analytics/SKILL.md
git commit -m "feat(product-management): add product-analytics skill — metrics, dashboards, reviews"
```

---

## Task 7: Strategy Commands (3 commands)

**Files:**
- Create: `product-management/commands/vision.md`
- Create: `product-management/commands/okrs.md`
- Create: `product-management/commands/competitive-analysis.md`

**Step 1: Write vision.md**

```markdown
---
description: Generate a product vision document — lean canvas or full vision doc
argument-hint: "<product name> [lean|full]"
---

# Product Vision

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a product vision document for a product or feature.

## Usage

```
/vision <product name> [lean|full]
```

### Arguments

- `product name` — The product or feature to create a vision for
- `lean|full` — (Optional) Vision format:
  - `lean` — Lean canvas: one-page format ideal for startups and early-stage products
  - `full` — Full vision doc with strategic context, stakeholder alignment, and review cadence for enterprise teams
  - If not specified, ask the user about their team size and context to recommend a format

## Workflow

### 1. Gather Context

Ask the user about:
- What problem does this product solve?
- Who is the target customer?
- What does success look like in 12 months?

Check ~~docs for any existing vision documents or strategy materials.

### 2. Generate Vision

Use the **Strategy** skill. Read `../skills/strategy/SKILL.md` and apply the appropriate vision template (lean or full).

### 3. Output

Deliver the vision document in markdown. If ~~docs is connected, offer to save it there.
```

**Step 2: Write okrs.md**

```markdown
---
description: Draft OKRs with measurable key results
argument-hint: "<team or product> [quarterly|annual]"
---

# OKRs

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Draft Objectives and Key Results for a team or product area.

## Usage

```
/okrs <team or product> [quarterly|annual]
```

### Arguments

- `team or product` — The team, product area, or company to draft OKRs for
- `quarterly|annual` — (Optional) OKR cadence. Defaults to quarterly.

## Workflow

### 1. Gather Context

Ask the user about:
- What is the team's mission or product vision?
- What are the top priorities this period?
- Any existing OKRs or strategic goals to align with?

Check ~~docs for existing OKRs, vision docs, or strategy materials.

### 2. Draft OKRs

Use the **Strategy** skill. Read `../skills/strategy/SKILL.md` and apply the appropriate OKR framework (team-level for startups, cascading for enterprise).

### 3. Output

Deliver OKRs in a structured format: Objective → Key Results (3-4 each) with owners and measurement criteria. Flag any KRs that look like activities rather than outcomes.
```

**Step 3: Write competitive-analysis.md**

```markdown
---
description: Map competitive landscape and positioning
argument-hint: "<product or market>"
---

# Competitive Analysis

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map the competitive landscape for a product or market segment.

## Usage

```
/competitive-analysis <product or market>
```

### Arguments

- `product or market` — The product, market, or segment to analyze competitively

## Workflow

### 1. Gather Context

Ask the user about:
- Who do they currently consider competitors?
- What dimensions matter most (features, pricing, market share, UX)?
- Any specific competitors to include or exclude?

### 2. Research & Analyze

Use the **Strategy** skill. Read `../skills/strategy/SKILL.md` and apply the appropriate competitive analysis framework.

Use web search for competitor data: pricing pages, feature lists, press releases, Crunchbase profiles, G2/Capterra reviews.

### 3. Output

Deliver:
1. Competitive landscape overview (top 5-10 players)
2. Feature comparison matrix
3. Positioning map (2-axis)
4. Key takeaways: where you're strong, where you're vulnerable, white space opportunities
```

**Step 4: Commit**

```bash
git add product-management/commands/vision.md product-management/commands/okrs.md product-management/commands/competitive-analysis.md
git commit -m "feat(product-management): add strategy commands — vision, okrs, competitive-analysis"
```

---

## Task 8: Discovery Commands (4 commands)

**Files:**
- Create: `product-management/commands/user-research.md`
- Create: `product-management/commands/persona.md`
- Create: `product-management/commands/jtbd.md`
- Create: `product-management/commands/opportunity-score.md`

**Step 1: Write user-research.md**

```markdown
---
description: Design a user research plan with interview guides
argument-hint: "<research topic> [guerrilla|formal]"
---

# User Research

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a user research plan including methodology, recruiting criteria, and interview guides.

## Usage

```
/user-research <research topic> [guerrilla|formal]
```

### Arguments

- `research topic` — The question, feature, or problem area to research
- `guerrilla|formal` — (Optional) Research style:
  - `guerrilla` — Quick, scrappy research for startups: intercept interviews, unmoderated surveys, 5-user tests
  - `formal` — Structured research for enterprise: recruiting criteria, moderated interviews, research repository
  - If not specified, ask the user about their timeline and resources

## Workflow

### 1. Define Research Questions

Ask the user what they're trying to learn. Frame as 3-5 specific research questions.

### 2. Design Research Plan

Use the **Discovery** skill. Read `../skills/discovery/SKILL.md` and create:
- Research methodology
- Participant criteria and recruiting plan
- Interview guide with opening, exploration, and closing sections
- Synthesis plan

### 3. Output

Deliver the research plan and interview guide. If ~~research-repo is connected, offer to save it there.
```

**Step 2: Write persona.md**

```markdown
---
description: Create user personas from research data or team knowledge
argument-hint: "<product or segment> [proto|data-backed]"
---

# Persona

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create user personas for a product or customer segment.

## Usage

```
/persona <product or segment> [proto|data-backed]
```

### Arguments

- `product or segment` — The product or customer segment to build personas for
- `proto|data-backed` — (Optional) Persona depth:
  - `proto` — Lightweight proto-personas from founder intuition and early conversations
  - `data-backed` — Data-driven personas with behavioral segmentation and validation metrics
  - If not specified, ask about available research data

## Workflow

### 1. Gather Inputs

Ask the user about available research: interview transcripts, survey data, analytics, CRM data. Check ~~research-repo and ~~analytics for existing data.

### 2. Build Personas

Use the **Discovery** skill. Read `../skills/discovery/SKILL.md` and apply the appropriate persona template.

### 3. Output

Deliver 2-4 personas with name, role, goals, frustrations, tools, and a representative quote. For data-backed personas, include segment size and behavioral data.
```

**Step 3: Write jtbd.md**

```markdown
---
description: Map jobs-to-be-done and desired outcomes
argument-hint: "<product or feature>"
---

# Jobs-to-be-Done

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map the jobs your customers are trying to accomplish and their desired outcomes.

## Usage

```
/jtbd <product or feature>
```

### Arguments

- `product or feature` — The product or feature area to map jobs for

## Workflow

### 1. Gather Context

Ask the user about the customer and situation. What are they trying to accomplish? What tools or workarounds do they use today?

### 2. Map Jobs

Use the **Discovery** skill. Read `../skills/discovery/SKILL.md` and apply the JTBD framework:
- Core functional jobs
- Related jobs
- Emotional and social jobs
- Job map (define → locate → prepare → confirm → execute → monitor → modify → conclude)

### 3. Output

Deliver job statements in standard format: "When I [situation], I want to [motivation], so I can [expected outcome]." Include importance vs. satisfaction scoring for prioritization.
```

**Step 4: Write opportunity-score.md**

```markdown
---
description: Score and prioritize product opportunities using Opportunity Solution Trees
argument-hint: "<outcome or opportunity area>"
---

# Opportunity Scoring

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Score and prioritize product opportunities to identify the highest-impact areas to invest in.

## Usage

```
/opportunity-score <outcome or opportunity area>
```

### Arguments

- `outcome or opportunity area` — The desired outcome or area to identify opportunities in

## Workflow

### 1. Define the Target Outcome

Clarify what success looks like. What metric or user outcome are we optimizing for?

### 2. Map Opportunities

Use the **Discovery** skill. Read `../skills/discovery/SKILL.md` and build an Opportunity Solution Tree:
- Target outcome at the top
- Opportunities branching below (unmet needs, pain points, desires)
- Potential solutions for each opportunity
- Experiments to validate solutions

### 3. Score & Prioritize

Score each opportunity on: reach, impact, confidence, effort. Rank and recommend the top 2-3 opportunities to pursue.

### 4. Output

Deliver the Opportunity Solution Tree visualization and a prioritized list with scores and rationale.
```

**Step 5: Commit**

```bash
git add product-management/commands/user-research.md product-management/commands/persona.md product-management/commands/jtbd.md product-management/commands/opportunity-score.md
git commit -m "feat(product-management): add discovery commands — user-research, persona, jtbd, opportunity-score"
```

---

## Task 9: Planning Commands (5 commands)

**Files:**
- Create: `product-management/commands/roadmap.md`
- Create: `product-management/commands/prd.md`
- Create: `product-management/commands/feature-spec.md`
- Create: `product-management/commands/prioritize.md`
- Create: `product-management/commands/backlog-groom.md`

**Step 1: Write roadmap.md**

```markdown
---
description: Build a product roadmap — Now/Next/Later or timeline format
argument-hint: "<product or team> [lean|detailed]"
---

# Roadmap

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Build a product roadmap for a product or team.

## Usage

```
/roadmap <product or team> [lean|detailed]
```

### Arguments

- `product or team` — The product or team to roadmap for
- `lean|detailed` — (Optional) Roadmap style:
  - `lean` — Now/Next/Later theme-based roadmap, no dates, fits on one page
  - `detailed` — Timeline roadmap with quarterly milestones, dependencies, and swim lanes
  - If not specified, ask about team size and planning horizon

## Workflow

### 1. Gather Inputs

Ask the user about: strategic priorities, OKRs, backlog themes, dependencies, stakeholder needs. Check ~~roadmap-tool and ~~project-tracker for existing data.

### 2. Build Roadmap

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and apply the appropriate roadmap format.

### 3. Output

Deliver the roadmap in markdown. For lean: themed columns (Now/Next/Later). For detailed: timeline with milestones, owners, and dependencies. Offer to save to ~~roadmap-tool if connected.
```

**Step 2: Write prd.md**

```markdown
---
description: Write a product requirements document
argument-hint: "<feature or project> [lean|full]"
---

# PRD

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Write a Product Requirements Document for a feature or project.

## Usage

```
/prd <feature or project> [lean|full]
```

### Arguments

- `feature or project` — The feature or project to write requirements for
- `lean|full` — (Optional) PRD depth:
  - `lean` — 1-page PRD: problem, solution, metrics, scope, risks
  - `full` — Complete PRD: user stories, acceptance criteria, edge cases, technical considerations, rollout plan
  - If not specified, ask about the feature complexity and team size

## Workflow

### 1. Gather Context

Ask the user about: the problem being solved, target user, desired outcome, constraints, and any existing research. Check ~~docs for prior PRDs or specs.

### 2. Write PRD

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and apply the appropriate PRD template.

### 3. Output

Deliver the PRD in markdown. Run through the PRD quality checklist. Offer to save to ~~docs if connected.
```

**Step 3: Write feature-spec.md**

```markdown
---
description: Write a detailed feature specification with user stories and acceptance criteria
argument-hint: "<feature name>"
---

# Feature Spec

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Write a detailed feature specification ready for engineering handoff.

## Usage

```
/feature-spec <feature name>
```

### Arguments

- `feature name` — The feature to specify

## Workflow

### 1. Gather Context

Ask the user about: user stories, design references, technical constraints, and dependencies. Check ~~docs for related PRDs and ~~design for wireframes or mockups.

### 2. Write Spec

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create:
- User stories with acceptance criteria (Given/When/Then)
- Interaction design notes and error states
- Technical considerations (API contracts, data models)
- Out-of-scope items

### 3. Output

Deliver the feature spec in markdown. Offer to create tickets in ~~project-tracker if connected.
```

**Step 4: Write prioritize.md**

```markdown
---
description: Run a prioritization exercise using RICE, ICE, MoSCoW, or weighted scoring
argument-hint: "<items to prioritize> [rice|ice|moscow|weighted]"
---

# Prioritize

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a structured prioritization exercise on a set of features, initiatives, or backlog items.

## Usage

```
/prioritize <items to prioritize> [rice|ice|moscow|weighted]
```

### Arguments

- `items to prioritize` — The features, initiatives, or backlog items to rank
- `rice|ice|moscow|weighted` — (Optional) Prioritization framework:
  - `rice` — Reach x Impact x Confidence / Effort — best for data-rich environments
  - `ice` — Impact x Confidence x Ease — best for speed
  - `moscow` — Must/Should/Could/Won't — best for scope negotiation
  - `weighted` — Custom weighted scoring — best for cross-team decisions with multiple stakeholders
  - If not specified, recommend a framework based on context

## Workflow

### 1. Gather Items

Ask the user for the list of items to prioritize. Check ~~project-tracker for backlog items if connected.

### 2. Score Items

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and apply the selected framework. For each item, score on all dimensions.

### 3. Output

Deliver a ranked table with scores, a brief rationale for the top 3, and any items that were difficult to score (flagged for discussion).
```

**Step 5: Write backlog-groom.md**

```markdown
---
description: Structure and refine a product backlog
argument-hint: "<product or sprint>"
---

# Backlog Groom

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Structure and refine a product backlog — organize items, estimate effort, and ensure stories meet the Definition of Ready.

## Usage

```
/backlog-groom <product or sprint>
```

### Arguments

- `product or sprint` — The product backlog or upcoming sprint to groom

## Workflow

### 1. Gather Backlog

Ask the user for their current backlog items or check ~~project-tracker for existing tickets.

### 2. Groom

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and:
- Review each item against the Definition of Ready
- Split oversized stories into smaller deliverables
- Suggest story point estimates (Fibonacci)
- Flag items with unclear requirements or missing acceptance criteria
- Organize by priority and sprint readiness

### 3. Output

Deliver the groomed backlog: prioritized, estimated, and ready for sprint planning. Flag items that need more research or design before they're ready.
```

**Step 6: Commit**

```bash
git add product-management/commands/roadmap.md product-management/commands/prd.md product-management/commands/feature-spec.md product-management/commands/prioritize.md product-management/commands/backlog-groom.md
git commit -m "feat(product-management): add planning commands — roadmap, prd, feature-spec, prioritize, backlog-groom"
```

---

## Task 10: Launch & Growth Commands (4 commands)

**Files:**
- Create: `product-management/commands/gtm-plan.md`
- Create: `product-management/commands/launch-checklist.md`
- Create: `product-management/commands/ab-test.md`
- Create: `product-management/commands/growth-experiment.md`

**Step 1: Write gtm-plan.md**

```markdown
---
description: Create a go-to-market plan for a product or feature launch
argument-hint: "<product or feature> [lean|enterprise]"
---

# GTM Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a go-to-market plan for a product or feature launch.

## Usage

```
/gtm-plan <product or feature> [lean|enterprise]
```

### Arguments

- `product or feature` — The product or feature being launched
- `lean|enterprise` — (Optional) GTM style:
  - `lean` — Startup GTM: early adopters, community, content marketing, founder-led sales
  - `enterprise` — Cross-functional GTM: sales enablement, marketing campaigns, CS readiness, partner channels
  - If not specified, ask about team size and target market

## Workflow

### 1. Gather Context

Ask about: target audience, pricing, competitive positioning, launch timeline, available channels. Check ~~docs for existing positioning or messaging.

### 2. Build GTM Plan

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create the GTM plan.

### 3. Output

Deliver the GTM plan with: target segments, messaging/positioning, channel strategy, timeline, success metrics, and owner for each workstream.
```

**Step 2: Write launch-checklist.md**

```markdown
---
description: Generate a launch readiness checklist
argument-hint: "<product or feature> [simple|phased]"
---

# Launch Checklist

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a launch readiness checklist to ensure nothing is missed before shipping.

## Usage

```
/launch-checklist <product or feature> [simple|phased]
```

### Arguments

- `product or feature` — The product or feature being launched
- `simple|phased` — (Optional) Launch complexity:
  - `simple` — Basic checklist: feature complete, QA, analytics, support, comms
  - `phased` — Enterprise phased rollout: internal → beta → % rollout → GA, with feature flags, rollback plan, monitoring
  - If not specified, ask about the blast radius and risk level

## Workflow

### 1. Gather Context

Ask about: launch date, rollout strategy, stakeholders, dependencies. Check ~~project-tracker for open blockers.

### 2. Build Checklist

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and generate the checklist.

### 3. Output

Deliver a categorized checklist (Engineering, Design, Marketing, Support, Legal) with owners and status. Include a launch day run-of-show if applicable.
```

**Step 3: Write ab-test.md**

```markdown
---
description: Design an A/B test with hypothesis, variants, and success metrics
argument-hint: "<feature or change to test>"
---

# A/B Test

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a rigorous A/B test for a product change.

## Usage

```
/ab-test <feature or change to test>
```

### Arguments

- `feature or change to test` — The change, feature variant, or UX modification to test

## Workflow

### 1. Define Hypothesis

Ask the user what they expect to happen and why. Frame as: "We believe [change] will cause [effect] for [segment], which we'll measure by [metric] over [timeframe]."

### 2. Design Test

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create:
- Hypothesis statement
- Control and variant descriptions
- Primary metric and guardrail metrics
- Sample size calculation and test duration estimate
- Segment targeting (if applicable)

Check ~~analytics for baseline metric values to inform sample size.

### 3. Output

Deliver the test design document. If ~~analytics supports feature flags or experimentation, offer to set up the test there.
```

**Step 4: Write growth-experiment.md**

```markdown
---
description: Design a growth experiment targeting acquisition, activation, retention, or referral
argument-hint: "<growth lever> [acquisition|activation|retention|revenue|referral]"
---

# Growth Experiment

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a structured growth experiment targeting a specific stage of the user funnel.

## Usage

```
/growth-experiment <growth lever> [acquisition|activation|retention|revenue|referral]
```

### Arguments

- `growth lever` — The specific idea or area to experiment with
- `acquisition|activation|retention|revenue|referral` — (Optional) Which stage of the pirate metrics (AARRR) funnel this targets

## Workflow

### 1. Define the Lever

Ask the user about: current funnel metrics, biggest drop-off points, growth goals. Check ~~analytics for funnel data if connected.

### 2. Design Experiment

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create:
- Hypothesis
- Target metric and baseline
- Experiment design (what changes, for whom)
- Expected impact and effort (ICE score)
- Timeline and success criteria
- Learning goal (what will we know after this, regardless of outcome?)

### 3. Output

Deliver the experiment design. Recommend whether to run it as a quick test or a full A/B test based on effort and risk.
```

**Step 5: Commit**

```bash
git add product-management/commands/gtm-plan.md product-management/commands/launch-checklist.md product-management/commands/ab-test.md product-management/commands/growth-experiment.md
git commit -m "feat(product-management): add launch-growth commands — gtm-plan, launch-checklist, ab-test, growth-experiment"
```

---

## Task 11: Analytics Commands (3 commands)

**Files:**
- Create: `product-management/commands/metrics-dashboard.md`
- Create: `product-management/commands/sprint-review.md`
- Create: `product-management/commands/product-review.md`

**Step 1: Write metrics-dashboard.md**

```markdown
---
description: Define a metrics framework and dashboard specification
argument-hint: "<product or team>"
---

# Metrics Dashboard

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a metrics framework and dashboard specification for a product or team.

## Usage

```
/metrics-dashboard <product or team>
```

### Arguments

- `product or team` — The product or team to define metrics for

## Workflow

### 1. Gather Context

Ask the user about: product stage, business model, current metrics (if any), key questions they need the dashboard to answer. Check ~~analytics for existing instrumentation.

### 2. Design Framework

Use the **Product Analytics** skill. Read `../skills/product-analytics/SKILL.md` and define:
- North Star Metric with rationale
- Input metrics (3-5 levers)
- Dashboard layout with metric definitions, data sources, and refresh cadence

### 3. Output

Deliver the metrics framework and dashboard spec. Include implementation notes for ~~analytics if connected.
```

**Step 2: Write sprint-review.md**

```markdown
---
description: Generate a sprint or iteration review summary
argument-hint: "<sprint name or number>"
---

# Sprint Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a sprint review summary covering what shipped, metrics impact, and learnings.

## Usage

```
/sprint-review <sprint name or number>
```

### Arguments

- `sprint name or number` — The sprint or iteration to review

## Workflow

### 1. Gather Data

Ask the user about: what shipped, what didn't, any blockers. Check ~~project-tracker for completed tickets and ~~analytics for metrics changes.

### 2. Compile Review

Use the **Product Analytics** skill. Read `../skills/product-analytics/SKILL.md` and create the sprint review.

### 3. Output

Deliver the review: what shipped, metrics impact, user feedback, blockers, and action items for next sprint. Offer to post to ~~messaging if connected.
```

**Step 3: Write product-review.md**

```markdown
---
description: Run a comprehensive cross-cutting product review — triggers the orchestrator for multi-stage analysis
argument-hint: "<product name> [monthly|quarterly]"
---

# Product Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a comprehensive product review spanning strategy, discovery, execution, and growth.

**This command triggers the orchestrator agent** for cross-cutting analysis across all lifecycle stages.

## Usage

```
/product-review <product name> [monthly|quarterly]
```

### Arguments

- `product name` — The product to review
- `monthly|quarterly` — (Optional) Review cadence and depth:
  - `monthly` — Lightweight review: metrics check, roadmap progress, key risks
  - `quarterly` — Full QBR: strategy alignment, discovery health, execution quality, growth metrics, deep dives

## Workflow

### 1. Activate Orchestrator

Read the orchestrator at `../agents/orchestrator.md`. This command triggers the "Product review" routing path.

### 2. Cross-Stage Assessment

The orchestrator sequences:
1. **Strategy check** — Vision alignment, OKR progress
2. **Analytics pull** — North Star trend, funnel metrics, retention cohorts
3. **Planning assessment** — Roadmap progress, backlog health, sprint velocity
4. **Synthesis** — Unified report with alignment flags

### 3. Output

Deliver the product review report. If any strategic-execution divergence is detected, include an **Alignment Flag** section with resolution options for human decision.
```

**Step 4: Commit**

```bash
git add product-management/commands/metrics-dashboard.md product-management/commands/sprint-review.md product-management/commands/product-review.md
git commit -m "feat(product-management): add analytics commands — metrics-dashboard, sprint-review, product-review"
```

---

## Task 12: Orchestrator Agent

**Files:**
- Create: `product-management/agents/orchestrator.md`
- Create: `product-management/agents/README.md`

**Step 1: Write orchestrator.md**

Create `product-management/agents/orchestrator.md`. This is the routing agent for multi-stage product management workflows.

Reference: Study `real-estate-investment/agents/orchestrator.md` for structure, classification matrix, routing rules, and synthesis template. Adapt that pattern for PM lifecycle stages.

Content must include:
- H1: "Agent: Product Management Orchestrator"
- **How It Works** section: classify request → select skills → sequence execution → synthesize output
- **Request Classification** section with code block showing:
  - Request type: Product Review, New Product, Pivot Assessment, Launch Readiness, Single-Stage
  - Complexity: Simple (1 skill), Moderate (2-3 skills), Complex (4-5 skills)
  - Context: Startup or Enterprise mode
- **Skill Registry** table mapping skills to their file paths
- **Forward Routing Rules** — 4 named routes (from design doc) with flow diagrams in code blocks:
  - Route 1: Product Review (Strategy → Analytics → Planning → Report)
  - Route 2: New Product (Strategy → Discovery → Planning → Launch)
  - Route 3: Pivot Assessment (Analytics → Discovery → Strategy → Planning)
  - Route 4: Launch Readiness (Planning → Analytics → Launch)
  - Single-stage passthrough
- **Bidirectional Re-entry Routing** section with code block showing all re-entry paths:
  - Build blocker → Discovery or Planning
  - Launch metrics miss → Discovery or Strategy
  - Growth stall → Discovery → Strategy
  - Explicit user request → any previous stage
  - Context tracking: what triggered re-entry and why
- **Conflict Escalation** section:
  - Detection criteria: strategic intent (roadmap, vision, OKRs) vs. execution reality (sprint scope, velocity, blockers)
  - Output format: "Alignment Flag" section
  - Behavior: surface tension, describe gap, suggest 2-3 resolution options, never silently resolve
- **Synthesis Template** in code block — the final output format for multi-stage reviews:
  - Product name, review type, date, skills deployed
  - Executive summary (2-3 sentences)
  - Sections per skill with findings
  - Alignment Flags (if any)
  - Recommendations and next steps
- **Handling Partial Information** section: analyze what's available, flag gaps, provide confidence levels

**Step 2: Write agents/README.md**

```markdown
# Agents

## Orchestrator

The Product Management Orchestrator routes multi-stage requests across lifecycle skills and synthesizes outputs into unified reports.

| Agent | File | Role |
|-------|------|------|
| Orchestrator | [orchestrator.md](./orchestrator.md) | Classify requests, route to skills, synthesize cross-stage outputs |

See [orchestrator.md](./orchestrator.md) for routing logic and synthesis templates.
```

**Step 3: Commit**

```bash
git add product-management/agents/orchestrator.md product-management/agents/README.md
git commit -m "feat(product-management): add orchestrator agent with bidirectional routing and conflict escalation"
```

---

## Task 13: Commands README

**Files:**
- Create: `product-management/commands/README.md`

**Step 1: Write commands/README.md**

```markdown
# Commands

19 slash commands organized by product lifecycle stage.

## Strategy

| Command | Description |
|---------|-------------|
| [/vision](./vision.md) | Generate a product vision document — lean canvas or full vision doc |
| [/okrs](./okrs.md) | Draft OKRs with measurable key results |
| [/competitive-analysis](./competitive-analysis.md) | Map competitive landscape and positioning |

## Discovery

| Command | Description |
|---------|-------------|
| [/user-research](./user-research.md) | Design a user research plan with interview guides |
| [/persona](./persona.md) | Create user personas from research data or team knowledge |
| [/jtbd](./jtbd.md) | Map jobs-to-be-done and desired outcomes |
| [/opportunity-score](./opportunity-score.md) | Score and prioritize product opportunities |

## Planning

| Command | Description |
|---------|-------------|
| [/roadmap](./roadmap.md) | Build a product roadmap — Now/Next/Later or timeline format |
| [/prd](./prd.md) | Write a product requirements document |
| [/feature-spec](./feature-spec.md) | Write a detailed feature specification |
| [/prioritize](./prioritize.md) | Run a prioritization exercise (RICE, ICE, MoSCoW, weighted) |
| [/backlog-groom](./backlog-groom.md) | Structure and refine a product backlog |

## Launch & Growth

| Command | Description |
|---------|-------------|
| [/gtm-plan](./gtm-plan.md) | Create a go-to-market plan |
| [/launch-checklist](./launch-checklist.md) | Generate a launch readiness checklist |
| [/ab-test](./ab-test.md) | Design an A/B test with hypothesis, variants, and success metrics |
| [/growth-experiment](./growth-experiment.md) | Design a growth experiment |

## Product Analytics

| Command | Description |
|---------|-------------|
| [/metrics-dashboard](./metrics-dashboard.md) | Define a metrics framework and dashboard specification |
| [/sprint-review](./sprint-review.md) | Generate a sprint or iteration review summary |
| [/product-review](./product-review.md) | Run a comprehensive product review (triggers orchestrator) |
```

**Step 2: Commit**

```bash
git add product-management/commands/README.md
git commit -m "feat(product-management): add commands README with all 19 commands"
```

---

## Task 14: Plugin README

**Files:**
- Create: `product-management/README.md`

**Step 1: Write README.md**

```markdown
# Product Management

Product management workflows from strategy to growth — vision docs, PRDs, roadmaps, user research, prioritization, GTM, analytics, and product reviews for startup and enterprise PMs.

> **Important**: This plugin assists with product management workflows but does not replace professional judgment. All outputs should be validated with stakeholders and users before making product decisions.

## Skills

| Skill | Description |
| :--- | :--- |
| [Strategy](./skills/strategy/SKILL.md) | Product vision, OKRs, and competitive analysis — lean canvas or full strategic docs |
| [Discovery](./skills/discovery/SKILL.md) | User research, personas, jobs-to-be-done, and opportunity scoring |
| [Planning](./skills/planning/SKILL.md) | Roadmaps, PRDs, feature specs, prioritization frameworks, and backlog grooming |
| [Launch & Growth](./skills/launch-growth/SKILL.md) | Go-to-market plans, launch checklists, A/B testing, and growth experiments |
| [Product Analytics](./skills/product-analytics/SKILL.md) | Metrics frameworks, dashboards, sprint reviews, and product reviews |

## Commands

19 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

## Agents

| Agent | Description |
| :--- | :--- |
| [Orchestrator](./agents/orchestrator.md) | Routes multi-stage requests across lifecycle skills, supports bidirectional re-entry and conflict escalation |

## Hooks

None.

## Startup vs. Enterprise

Every skill supports both modes. Commands accept an optional mode hint (e.g., `/prd my-feature lean` or `/prd my-feature full`). When no mode is specified, the command asks about your team context and recommends the appropriate depth.

## MCP Integration

Connect your product tools via MCP servers for the richest experience. See [CONNECTORS.md](./CONNECTORS.md) for details.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **product-management**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/product-management
```
```

**Step 2: Commit**

```bash
git add product-management/README.md
git commit -m "feat(product-management): add plugin README"
```

---

## Task 15: Update Root README

**Files:**
- Modify: `README.md` (root)

**Step 1: Add product-management to the Available Plugins table**

In the root `README.md`, add a row to the Available Plugins table after the Management Consulting row:

```markdown
| **[Product Management](./product-management/)** | 5 | 19 | 1 | — | Product management from strategy to growth — vision, PRDs, roadmaps, user research, prioritization, GTM, A/B testing, analytics, and product reviews for startup and enterprise PMs. |
```

Update the totals row to reflect the new counts: Skills +5, Commands +19, Agents +1.

Also add `product-management/` to the Repository Structure tree.

**Step 2: Commit**

```bash
git add README.md
git commit -m "docs: add product-management plugin to root README"
```

---

## Summary

| Task | What | Files | Commit |
|------|------|-------|--------|
| 1 | Plugin scaffold | plugin.json, .mcp.json, CONNECTORS.md | `feat(product-management): scaffold plugin metadata, MCP config, and connectors` |
| 2 | Strategy skill | skills/strategy/SKILL.md | `feat(product-management): add strategy skill` |
| 3 | Discovery skill | skills/discovery/SKILL.md | `feat(product-management): add discovery skill` |
| 4 | Planning skill | skills/planning/SKILL.md | `feat(product-management): add planning skill` |
| 5 | Launch & Growth skill | skills/launch-growth/SKILL.md | `feat(product-management): add launch-growth skill` |
| 6 | Product Analytics skill | skills/product-analytics/SKILL.md | `feat(product-management): add product-analytics skill` |
| 7 | Strategy commands (3) | commands/vision.md, okrs.md, competitive-analysis.md | `feat(product-management): add strategy commands` |
| 8 | Discovery commands (4) | commands/user-research.md, persona.md, jtbd.md, opportunity-score.md | `feat(product-management): add discovery commands` |
| 9 | Planning commands (5) | commands/roadmap.md, prd.md, feature-spec.md, prioritize.md, backlog-groom.md | `feat(product-management): add planning commands` |
| 10 | Launch commands (4) | commands/gtm-plan.md, launch-checklist.md, ab-test.md, growth-experiment.md | `feat(product-management): add launch-growth commands` |
| 11 | Analytics commands (3) | commands/metrics-dashboard.md, sprint-review.md, product-review.md | `feat(product-management): add analytics commands` |
| 12 | Orchestrator agent | agents/orchestrator.md, agents/README.md | `feat(product-management): add orchestrator agent` |
| 13 | Commands README | commands/README.md | `feat(product-management): add commands README` |
| 14 | Plugin README | README.md | `feat(product-management): add plugin README` |
| 15 | Root README update | README.md (root) | `docs: add product-management to root README` |

**Total: 15 tasks, 30 files, 15 commits**
