# AI Skills Marketplace

Welcome to the premier **AI Skills Marketplace**, designed for **Claude Code**, **Vercel AI SDK**, and other agentic systems.

This repository hosts a curated collection of specialized agentic skills—from foundational architecture patterns to high-level strategic capabilities—ready to be installed directly into your AI agents.

## 🚀 Installation

You can install these skills directly using the Vercel `skills` CLI. This command works for **Claude Code**, **Cursor**, **Vercel AI SDK**, and other supported agents.

### Install All Skills
To access the full marketplace:
```bash
npx skills add LauraFlorentin/skills-marketplace
```

### Install Specific Skills
To install a specific pattern, such as the **Planning** skill:
```bash
npx skills add LauraFlorentin/skills-marketplace/skills/agentic_systems_architecture/planning
```

## 🧩 Available Collections

### 1. [Agentic Systems Architecture](./skills/agentic_systems_architecture/README.md)
The core building blocks for autonomous agents.
- **Includes**: Planning, Routing, Tool Use, RAG, Memory, Reflection, and 15+ more.
- **Best for**: Building robust, production-grade agentic workflows.

### 2. [Consulting Strategies](./skills/consulting/README.md)
*(Coming Soon)* Strategic frameworks for AI implementation and business analysis.

## 🤖 Claude Plugin Integration

This repository is configured as a **Claude Code Plugin**.
When you use `npx skills add`, it will automatically detect your Claude configuration and install the selected skills as instructions or tools available to Claude.

The `claude.json` manifest ensures that all skills are correctly exposed to the Claude ecosystem.

## Contributing
Contributions are welcome! Please open an issue or submit a PR to add new skills to the marketplace.
