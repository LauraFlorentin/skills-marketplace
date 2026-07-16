# AI Skills Marketplace

[![Validate marketplace](https://github.com/LauraFlorentin/skills-marketplace/actions/workflows/validate.yml/badge.svg)](https://github.com/LauraFlorentin/skills-marketplace/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Claude Code plugin marketplace containing 10 focused plugins. Components use the standard plugin locations for skills, commands, agents, and hooks.

## Catalog

| Plugin | Skills | Commands | Agents | Hooks | Scope |
|---|---:|---:|---:|---:|---|
| [Agentic Skills](agentic-skills/) | 21 | 21 | 0 | 0 | Reusable agent architecture patterns |
| [Brand Studio](brand-studio/) | 1 | 7 | 0 | 1 | Persistent project or personal brand guidance |
| [Deck Studio](deck-studio/) | 3 | 14 | 0 | 1 | Storytelling, slide writing, and branded decks |
| [Harness Engineer](harness-engineer/) | 5 | 4 | 1 | 4 | Context, evaluation, non-destructive diagnostics, and scaffolding |
| [M&A Advisory](ma-advisory/) | 10 | 19 | 0 | 0 | Source-traceable transaction workflows and issue spotting |
| [Management Consulting](management-consulting/) | 13 | 20 | 0 | 0 | Consulting delivery, research, operations, and structured thinking |
| [Product Management](product-management/) | 5 | 19 | 1 | 0 | Strategy, discovery, planning, launch, and analytics |
| [Project Management](project-management/) | 5 | 20 | 1 | 0 | Initiation, planning, execution, monitoring, and closing |
| [Real Estate Investment](real-estate-investment/) | 1 | 11 | 11 | 0 | Evidence-based underwriting and specialist risk analysis |
| [Skill Checker](skill-checker/) | 1 | 1 | 0 | 0 | Structural validation and skill-quality review |
| **Total** | **65** | **136** | **14** | **6** | |

## Install

In Claude Code, open `/plugins`, add the marketplace source `LauraFlorentin/skills-marketplace`, and select the plugins you need. Plugin commands are namespaced, such as `/deck-studio:build-deck`.

Compatible skill installers can install the marketplace, a plugin, or one skill:

```bash
npx skills add LauraFlorentin/skills-marketplace
npx skills add LauraFlorentin/skills-marketplace/agentic-skills
npx skills add LauraFlorentin/skills-marketplace/agentic-skills/skills/planning
```

## Repository layout

```text
skills-marketplace/
├── .claude-plugin/marketplace.json
├── .github/                     community files and validation workflow
├── scripts/validate_marketplace.py
├── <plugin>/
│   ├── .claude-plugin/plugin.json
│   ├── skills/<skill>/SKILL.md
│   ├── commands/                optional
│   ├── agents/                  optional
│   ├── hooks/hooks.json         optional
│   └── README.md
├── CONTRIBUTING.md
├── SECURITY.md
└── LICENSE
```

Plugin manifests own plugin versions; marketplace entries point to local plugin sources without duplicating version metadata.

## Develop

Run the dependency-free catalog validator before opening a pull request:

```bash
python3 scripts/validate_marketplace.py
claude plugin validate . --strict
```

The validator checks catalog coverage, manifests, frontmatter, component discovery, local Markdown links, JSON syntax, reference navigation, and generated artifacts. See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [CHANGELOG.md](CHANGELOG.md).

## License

[MIT](LICENSE)
