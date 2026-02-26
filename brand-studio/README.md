# Brand Studio

A complete branding toolkit — apply consistent brand identity (colors, fonts, logo, tone of voice) across PowerPoint presentations, Word documents, logos, HTML/web artifacts, and social media templates.

## How It Works

On first use, Brand Studio walks you through a conversational setup (~10 questions) and saves your brand identity to `brand-config.md`. From then on, every branded output uses your exact colors, fonts, and tone automatically.

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

| Command | Description |
| :--- | :--- |
| `/brand-setup` | Configure or update your brand identity |
| `/brand-status` | Show a summary of your current brand config |
| `/brand-ppt` | Brand a PowerPoint or create one from scratch |
| `/brand-doc` | Brand a Word doc or create one from scratch |
| `/brand-logo` | Generate logo SVGs (3 variations) |
| `/brand-social` | Create social media assets (or full kit) |
| `/brand-web` | Create branded HTML artifacts |

## Hooks

Includes a **Brand Guard hook** (`hooks/brand_guard.py`) that auto-enforces branding on `.pptx`, `.docx`, `.html`, `.svg`, `.png`, `.pdf` files — so you never accidentally create unbranded content.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **brand-studio**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/brand-studio
```
