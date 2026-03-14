# AI Skills Marketplace

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A curated collection of specialized AI skills, organized as a **Claude Code Plugin Marketplace**. Install individual skill packs directly into Claude Code, Cowork, or any Vercel AI SDK-compatible agent.

## Available Plugins

| Plugin | Skills | Commands | Agents | Hooks | Description |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **[Agentic Skills](./agentic-skills/)** | 21 | 21 | — | — | Core building blocks for autonomous agents — planning, routing, RAG, memory, reflection, tool use, and more. |
| **[Brand Studio](./brand-studio/)** | 1 | 7 | — | 1 | Complete branding toolkit — apply consistent brand identity across PowerPoint, Word, logos, HTML/web, and social media. Includes auto-branding hook. |
| **[M&A Advisory](./ma-advisory/)** | 10 | 19 | — | — | AI-powered M&A workflows — VDR management, deal screening, legal and financial diligence, synergy analysis, deal marketing, integration planning, and workflow chains. |
| **[Management Consulting](./management-consulting/)** | 13 | 20 | — | — | End-to-end consulting workflows — proposals, deliverables, research, project management, workshops, bench ops, contracts, and structured thinking frameworks. |
| **[Product Management](./product-management/)** | 5 | 19 | 1 | — | Product management from strategy to growth — vision, PRDs, roadmaps, user research, prioritization, GTM, A/B testing, analytics, and product reviews for startup and enterprise PMs. |
| **[Project Management](./project-management/)** | 5 | 20 | 1 | — | Project management from initiation to closing — charters, WBS, scheduling, risk registers, sprint planning, status reports, retrospectives, and closeout for software and general PMs. |
| **[Real Estate Investment](./real-estate-investment/)** | 1 | 11 | 11 | — | Adaptive multi-agent system for investment analysis — deal screening, underwriting, pro forma, financing, tax strategy, stress testing, syndication, and international deals. |
| **[Harness Engineer](./harness-engineer/)** | 4 | 3 | — | 4 | Agent-first development toolkit — scaffold harnesses, diagnose agent failures, garbage collect stale docs, and auto-orient fresh sessions. Three-layer circuit breaker system. |
| **[Deck Studio](./deck-studio/)** | 3 | 14 | — | 1 | End-to-end presentation toolkit — strategic storytelling, narrative frameworks, branded PPTX generation, and data-driven slide craft. |
| **[Skill Checker](./skill-checker/)** | 1 | 1 | — | — | Validate, review, and score Claude skills against Anthropic's official best practices. Automated structural validator and multi-dimensional audit scorecard. |
| | **65** | **136** | **13** | **6** | |

---

## Installation

### Claude Code

1. Open Claude Code and run `/plugins`
2. Select **Add Marketplace**
3. Enter the source:
   ```
   LauraFlorentin/skills-marketplace
   ```
4. Browse the available plugins and choose which to install.

### Cowork

1. Open Cowork and navigate to **Settings → Plugins**
2. Select **Add from Marketplace**
3. Enter:
   ```
   LauraFlorentin/skills-marketplace
   ```
4. Select the skill pack you want to add.

### Vercel AI SDK (`npx skills`)

Install the full marketplace:
```bash
npx skills add LauraFlorentin/skills-marketplace
```

Install a specific plugin:
```bash
npx skills add LauraFlorentin/skills-marketplace/agentic-skills
```

Install a single skill:
```bash
npx skills add LauraFlorentin/skills-marketplace/agentic-skills/skills/planning
```

---

## Repository Structure

Each plugin follows a standardized layout:

```
skills-marketplace/
├── agentic-skills/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 21 slash commands
│   ├── hooks/
│   ├── skills/                ← 21 agentic design patterns
│   └── README.md
├── brand-studio/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 7 brand commands
│   ├── hooks/                 ← Brand Guard auto-enforcement
│   ├── skills/                ← Brand identity toolkit
│   └── README.md
├── ma-advisory/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 19 commands (9 daily + 7 reports + 3 chains)
│   ├── hooks/
│   ├── skills/                ← 10 M&A lifecycle skills
│   └── README.md
├── management-consulting/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 20 slash commands
│   ├── hooks/
│   ├── skills/                ← 13 consulting skills
│   └── README.md
├── product-management/
│   ├── .claude-plugin/plugin.json
│   ├── agents/                ← Orchestrator with bidirectional routing
│   ├── commands/              ← 19 slash commands
│   ├── skills/                ← 5 lifecycle skills (startup + enterprise)
│   └── README.md
├── project-management/
│   ├── .claude-plugin/plugin.json
│   ├── agents/                ← Orchestrator with bidirectional re-entry routing
│   ├── commands/              ← 20 slash commands
│   ├── skills/                ← 5 lifecycle skills (software + general PM)
│   └── README.md
├── real-estate-investment/
│   ├── .claude-plugin/plugin.json
│   ├── agents/                ← Orchestrator + 10 specialist agents
│   ├── commands/              ← 11 slash commands
│   ├── hooks/
│   ├── skills/
│   └── README.md
├── deck-studio/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 14 slash commands (3 deck + 4 storytelling + 7 brand)
│   ├── hooks/                 ← Brand Guard auto-enforcement
│   ├── skills/                ← 3 skills (deck-builder, storytelling, brand-studio)
│   └── README.md
├── harness-engineer/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 3 slash commands (init, doctor, gc)
│   ├── hooks/                 ← Circuit breaker, dead man's switch, watchdog, model-context
│   ├── skills/                ← 4 skills (init, doctor, gc, onboard)
│   ├── templates/             ← Scaffolding templates
│   └── README.md
├── skill-checker/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/              ← 1 slash command (check)
│   ├── hooks/
│   ├── skills/                ← 1 skill (skill-checker) with validation script
│   └── README.md
└── README.md
```

---

## License

[MIT](https://opensource.org/licenses/MIT)
