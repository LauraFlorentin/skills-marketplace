---
name: "Brand Studio"
description: >
  Complete branding toolkit — apply consistent brand identity (colors, fonts,
  logo, tone of voice) across PowerPoint presentations, Word documents, logos,
  HTML/web artifacts, and social media templates. On first use, walks through
  a conversational setup (~10 questions) and saves the brand identity to
  brand-config.md. From then on, every branded output uses the exact colors,
  fonts, and tone automatically. Includes Brand Guard hook for auto-enforcement.
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
