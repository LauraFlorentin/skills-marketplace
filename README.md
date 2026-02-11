# AI Skills Marketplace

A curated collection of specialized AI skills, organized as a **Claude Code Plugin Marketplace**. Install individual skill packs directly into Claude Code, Cowork, or any Vercel AI SDK-compatible agent.

## 📦 Available Skill Packs

| Plugin | Skills | Description |
| :--- | :---: | :--- |
| **[Agentic Skills](./plugins/agentic-skills/skills/README.md)** | 21 | Core building blocks for autonomous agents — planning, routing, RAG, memory, reflection, and more. |
| **[Management Consulting](./plugins/management-consulting/skills/README.md)** | — | *(Coming Soon)* Strategic frameworks for AI implementation and business transformation. |

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

Install a specific skill pack:
```bash
npx skills add LauraFlorentin/skills-marketplace/plugins/agentic-skills
```

Install a single skill:
```bash
npx skills add LauraFlorentin/skills-marketplace/plugins/agentic-skills/skills/planning
```

---

## 🗂 Repository Structure

```
skills-marketplace/
├── .claude-plugin/
│   └── marketplace.json            ← Marketplace definition
├── plugins/
│   ├── agentic-skills/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json         ← Plugin manifest
│   │   └── skills/                 ← 21 agentic skills (SKILL.md each)
│   └── management-consulting/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/                 ← Consulting skills (coming soon)
└── README.md
```

## Contributing

Contributions are welcome! Please open an issue or submit a PR to add new skills to the marketplace.
