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
| **[Real Estate Investment](./real-estate-investment/)** | 1 | 11 | 11 | — | Adaptive multi-agent system for investment analysis — deal screening, underwriting, pro forma, financing, tax strategy, stress testing, syndication, and international deals. |
| | **46** | **78** | **11** | **1** | |

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
├── real-estate-investment/
│   ├── .claude-plugin/plugin.json
│   ├── agents/                ← Orchestrator + 10 specialist agents
│   ├── commands/              ← 11 slash commands
│   ├── hooks/
│   ├── skills/
│   └── README.md
└── README.md
```

---

## Contributing

Contributions are welcome! To add a new plugin:

1. **Create a directory** at the repo root with your plugin name (kebab-case).
2. **Follow the standardized structure:**
   ```
   your-plugin/
   ├── .claude-plugin/
   │   └── plugin.json         # Plugin manifest (see below)
   ├── skills/
   │   └── skill-name/
   │       └── SKILL.md        # Skill definition with YAML frontmatter
   ├── commands/
   │   ├── README.md           # Command index
   │   └── command-name.md     # Command files (filename → /slash-command)
   ├── agents/                 # Optional: agent definitions
   │   └── README.md
   ├── hooks/                  # Optional: lifecycle hooks
   │   └── README.md
   └── README.md               # Plugin documentation
   ```
3. **Plugin manifest** (`plugin.json`):
   ```json
   {
     "name": "your-plugin",
     "version": "1.0.0",
     "description": "What your plugin does",
     "author": { "name": "YourName" },
     "repository": "https://github.com/LauraFlorentin/skills-marketplace",
     "license": "MIT",
     "skills": "./skills/",
     "commands": "./commands/",
     "keywords": ["relevant", "tags"]
   }
   ```
4. **SKILL.md frontmatter:**
   ```yaml
   ---
   name: "Skill Name"
   description: "What this skill does"
   version: "1.0"
   author: "YourName"
   ---
   ```
5. **Command frontmatter:**
   ```yaml
   ---
   description: "What this command does"
   ---
   ```
6. **README template** — include these sections: intro, Skills table, Commands section, Agents (if any), Hooks (if any), Installation.

Open an issue or submit a PR to get your plugin reviewed and merged.

---

## License

[MIT](https://opensource.org/licenses/MIT)
