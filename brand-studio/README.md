# Brand Studio

A complete branding toolkit — apply consistent brand identity (colors, fonts, logo, tone of voice) across PowerPoint presentations, Word documents, logos, HTML/web artifacts, and social media templates.

> **Important**: This plugin generates brand assets based on your configured identity. Always review outputs for accuracy and brand compliance before publishing.

## How It Works

On first use, Brand Studio creates either a project brand at `.brand-studio/brand-config.md` or a personal default in the plugin data directory. Project configuration takes precedence. Installed plugin files remain immutable.

## Skills

| Skill | Description |
| :--- | :--- |
| [Brand Studio](./skills/brand-studio/SKILL.md) | Master routing skill — brand setup, PPT/doc/logo/web/social branding |

### Output Types

| Output | Reference | Trigger |
| :--- | :--- | :--- |
| PowerPoint | [ppt-branding.md](./skills/brand-studio/references/ppt-branding.md) | "brand my slides" |
| Word Documents | [doc-branding.md](./skills/brand-studio/references/doc-branding.md) | "brand this document" |
| Logos | [logo-creator.md](./skills/brand-studio/references/logo-creator.md) | "create my logo" |
| Web / HTML | [web-branding.md](./skills/brand-studio/references/web-branding.md) | "create a branded landing page" |
| Social Media | [social-media-templates.md](./skills/brand-studio/references/social-media-templates.md) | "LinkedIn banner", "social media kit" |

## Commands

7 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

| Command | Description |
| :--- | :--- |
| `/brand-studio:brand-setup` | Configure or update your brand identity |
| `/brand-studio:brand-status` | Show a summary of your current brand config |
| `/brand-studio:brand-ppt` | Brand a PowerPoint or create one from scratch |
| `/brand-studio:brand-doc` | Brand a Word doc or create one from scratch |
| `/brand-studio:brand-logo` | Generate logo SVGs (3 variations) |
| `/brand-studio:brand-social` | Create social media assets (or full kit) |
| `/brand-studio:brand-web` | Create branded HTML artifacts |

## Agents

None.

## Hooks

Includes a non-blocking **Brand Guard hook** (`hooks/brand_guard.py`). When a brand is configured and a supported asset is about to be written, it injects the active brand summary into context. It does not modify files or approve tool use.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **brand-studio**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/brand-studio
```
