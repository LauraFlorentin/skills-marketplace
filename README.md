# AI Skills Marketplace

A curated collection of specialized AI skills, organized as a **Claude Code Plugin Marketplace**. Install individual skill packs directly into Claude Code, Cowork, or any Vercel AI SDK-compatible agent.

## 📦 Available Plugins

| Plugin | Skills | Description |
| :--- | :---: | :--- |
| **[Agentic Skills](./agentic-skills/)** | 21 | Core building blocks for autonomous agents — planning, routing, RAG, memory, reflection, tool use, and more. |
| **[Real Estate Investment](./real-estate-investment/)** | 1 | Adaptive multi-agent system for investment analysis — deal screening, underwriting, pro forma, financing, tax strategy, stress testing, syndication, and international deals. |
| **[Management Consulting](./management-consulting/)** | 3 | Strategic frameworks for consulting operations — bench management, thought leadership content creation, and ASE workshop planning. |

---

## 🚀 Installation

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

## 🗂 Repository Structure

Each plugin follows a standardized layout:

```
skills-marketplace/
├── agentic-skills/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   ├── skills/          ← 21 agentic design patterns
│   └── README.md
├── real-estate-investment/
│   ├── .claude-plugin/plugin.json
│   ├── agents/          ← Orchestrator + 11 specialist agents
│   ├── commands/
│   ├── hooks/
│   ├── skills/
│   └── README.md
├── management-consulting/
│   ├── .claude-plugin/plugin.json
│   ├── agents/
│   ├── commands/
│   ├── hooks/
│   ├── skills/          ← Coming soon
│   └── README.md
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a PR to add new skills to the marketplace.
