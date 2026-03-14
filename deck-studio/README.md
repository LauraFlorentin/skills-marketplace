# Deck Studio

End-to-end presentation toolkit — strategic storytelling, narrative frameworks, branded PPTX generation, and data-driven slide craft. Combines deck building, storytelling, and brand identity into one seamless pipeline.

> **Important**: This plugin generates presentation content and branded assets. Always review outputs for accuracy, data correctness, and brand compliance before presenting.

## How It Works

Deck Studio orchestrates three skills into a single pipeline:

```
STORYTELLING              BRAND STUDIO              PPTX OUTPUT
(narrative + structure) + (colors, fonts, logo)  →  (branded .pptx)
```

1. **Diagnose** — Understand the audience, goal, and context
2. **Storyboard** — Choose a framework and draft action titles
3. **Write** — Generate slide content, visuals, and speaker notes
4. **Brand & Build** — Apply brand identity and generate the final PPTX

## Skills

| Skill | Description |
| :--- | :--- |
| [Deck Builder](./skills/deck-builder/SKILL.md) | 4-stage pipeline: diagnose → storyboard → content → branded PPTX |
| [Storytelling](./skills/storytelling/SKILL.md) | Narrative frameworks, action titles, data storytelling, audience modes |
| [Brand Studio](./skills/brand-studio/SKILL.md) | Brand identity setup and enforcement across all output types |

## Commands

14 slash commands — see [`commands/README.md`](./commands/README.md) for the full list.

### Deck Building
| Command | Description |
| :--- | :--- |
| `/build-deck` | Full 4-stage pipeline: diagnose → storyboard → content → branded PPTX |
| `/storyboard` | Diagnose context and generate action-title storyboard |
| `/write-slides` | Write full slide content for an approved storyboard |

### Storytelling
| Command | Description |
| :--- | :--- |
| `/story-framework` | Choose the right narrative framework for your presentation |
| `/action-titles` | Rewrite topic titles into action titles |
| `/data-story` | Turn data into a compelling Data Story Arc narrative |
| `/audience-mode` | Adapt tone and structure for a specific audience type |

### Brand Identity
| Command | Description |
| :--- | :--- |
| `/brand-setup` | Configure or update your brand identity |
| `/brand-status` | Show a summary of your current brand config |
| `/brand-ppt` | Brand a PowerPoint or create one from scratch |
| `/brand-doc` | Brand a Word doc or create one from scratch |
| `/brand-logo` | Generate logo SVGs (3 variations) |
| `/brand-social` | Create social media assets (or full kit) |
| `/brand-web` | Create branded HTML artifacts |

## Agents

None.

## Hooks

Includes a **Brand Guard hook** (`hooks/brand_guard.py`) that auto-enforces branding on `.pptx`, `.docx`, `.html`, `.svg`, `.png`, `.pdf` files — so you never accidentally create unbranded content.

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **deck-studio**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/deck-studio
```
