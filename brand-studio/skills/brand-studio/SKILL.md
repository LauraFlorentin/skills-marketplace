---
name: brand-studio
description: >
  Complete branding toolkit — apply consistent brand identity (colors, fonts,
  logo, tone of voice) across PowerPoint presentations, Word documents, logos,
  HTML/web artifacts, and social media templates. On first use, walks through
  a conversational setup (~10 questions) and saves the brand identity to
  brand-config.md. From then on, every branded output uses the exact colors,
  fonts, and tone automatically. Includes Brand Guard hook for auto-enforcement.
  Use when user asks to "apply brand guidelines", "create branded content", "brand consistency", or mentions brand identity, logo usage, brand colors, or branded templates.
version: "1.0"
author: "LauraFlorentin"
---

# Brand Studio

Master routing skill for brand identity creation and enforcement. Brand Studio ensures every output — slides, documents, logos, web pages, social assets — reflects a single, consistent brand identity.

## When to Use

- Setting up a new brand identity from scratch
- Applying branding to PowerPoint presentations or Word documents
- Generating logo variations (SVG)
- Creating branded HTML landing pages or web artifacts
- Producing social media templates (LinkedIn, Twitter/X, Instagram)
- Checking or updating an existing brand configuration

## How It Works

1. **Setup** — Run `/brand-setup` to walk through brand identity questions (name, tagline, colors, fonts, logo style, tone of voice). Results are saved to `brand-config.md`.
2. **Create** — Use any output command (`/brand-ppt`, `/brand-doc`, `/brand-logo`, `/brand-web`, `/brand-social`) to produce branded assets.
3. **Guard** — The Brand Guard hook (`hooks/brand_guard.py`) auto-enforces branding on `.pptx`, `.docx`, `.html`, `.svg`, `.png`, `.pdf` files so nothing ships unbranded.

## Output Types

| Output | Reference | Command |
| :--- | :--- | :--- |
| PowerPoint | `references/ppt-branding.md` | `/brand-ppt` |
| Word Documents | `references/doc-branding.md` | `/brand-doc` |
| Logos | `references/logo-creator.md` | `/brand-logo` |
| Web / HTML | `references/web-branding.md` | `/brand-web` |
| Social Media | `references/social-media-templates.md` | `/brand-social` |

## Brand Config

The brand identity is stored in `brand-config.md` alongside this skill. See `references/brand-config-template.md` for the full template. Key sections:

- **Identity** — Brand name, tagline, industry, personality
- **Colors** — Primary, secondary, accent, background, text (hex values)
- **Typography** — Heading and body fonts with fallbacks
- **Logo** — Style, icon description, usage rules
- **Tone of Voice** — Communication style, do/don't guidelines


## Examples

**Input**: "Set up brand guidelines for Luminary AI, a teal-and-white enterprise AI company."

**brand-config.md output** (excerpt):
```
Brand: Luminary AI | Tagline: Intelligence You Can Trust
Colors: Primary #00B5A3 (teal), Secondary #FFFFFF, Accent #1A1A2E (navy)
Fonts: Headings: Inter Bold, Body: Inter Regular
Tone: Professional, clear, confidence-inspiring. Avoid: jargon, hyperbole
```

**Follow-up**: `/brand-ppt` now generates PowerPoint slides using Luminary AI's exact teal palette and Inter typography automatically.

---

**Input**: "/brand-social — create a LinkedIn post announcing our Series B."

**Output**: LinkedIn post formatted with Luminary AI brand voice, teal accent CTA, and character-count within LinkedIn limits.


## Troubleshooting

| Problem | Cause | Fix |
|---|---|---|
| Brand config not found | `brand-config.md` missing | Run `/brand-setup` to generate it; file must be in the project root |
| Wrong colors applied | Hex values entered incorrectly | Verify hex codes are 6 digits with `#` prefix; use `/brand-check` to validate |
| Font not rendering in PowerPoint | Font not installed on target machine | Use web-safe fallbacks (Arial, Helvetica) or embed fonts in the PPTX |
| Brand Guard fires on every file save | Overly broad file pattern | Narrow the hook's glob pattern to specific file types in `settings.json` |
