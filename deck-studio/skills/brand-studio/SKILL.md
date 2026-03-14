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

## Step 0: Always Check Brand Config First

Before doing anything else, **always** read `brand-config.md` from this skill's directory.

- **If it exists and is configured** → proceed directly to the requested task using the brand identity stored there.
- **If it doesn't exist or is empty/placeholder** → run the Brand Setup Flow below before proceeding.

## Brand Setup Flow

Run this when `brand-config.md` is missing or unconfigured. Ask the user the following questions conversationally (not all at once — feel natural, group related questions):

### Round 1 — Core Identity
1. What's your company or brand name?
2. What's your tagline or one-line description? (optional)
3. What industry or sector are you in?
4. How would you describe your brand's personality? (e.g. bold & modern, warm & approachable, clean & minimal, luxurious & premium)

### Round 2 — Visual Identity
5. What are your primary brand colors? (ask for hex codes if they have them, otherwise ask them to describe — e.g. "deep navy and gold" — and suggest hex values)
6. Do you have secondary/accent colors?
7. What fonts do you use? (heading font + body font — suggest Google Fonts pairings if they're unsure)
8. Do you have a logo? If so, ask them to upload it or describe it for generation.

### Round 3 — Voice & Content
9. What's your tone of voice? (e.g. professional, conversational, inspirational, technical)
10. Any words, phrases, or themes you always/never want to use?
11. What's your website URL? (optional, for footers/web assets)

### After collecting answers:
- Confirm the brand config with the user in a clean summary
- Write everything to `brand-config.md` using the template in `references/brand-config-template.md`
- Tell the user: "Your brand is saved! You can update it anytime by saying 'update my brand config'."
- Proceed immediately to the task they originally asked for (if any)

## How It Works

1. **Setup** — Run `/brand-setup` or ask to "set up my brand" to walk through the Brand Setup Flow above. Results are saved to `brand-config.md`.
2. **Create** — Use any output command (`/brand-ppt`, `/brand-doc`, `/brand-logo`, `/brand-web`, `/brand-social`) to produce branded assets.
3. **Guard** — The Brand Guard hook (`hooks/brand_guard.py`) auto-enforces branding on `.pptx`, `.docx`, `.html`, `.svg`, `.png`, `.pdf` files so nothing ships unbranded.

## Routing — What Does the User Want to Create?

After confirming brand config exists, route to the appropriate reference file:

| User request | Reference file to read |
|---|---|
| "brand my PowerPoint / slides / deck" | `references/ppt-branding.md` |
| "brand my Word doc / document / report" | `references/doc-branding.md` |
| "create / generate a logo" | `references/logo-creator.md` |
| "create a branded website / HTML / landing page / email template" | `references/web-branding.md` |
| "create social media assets / banners / LinkedIn banner / Instagram post" | `references/social-media-templates.md` |
| "social media kit / full social kit" | `references/social-media-templates.md` (batch generation) |
| "apply my brand" (no file type specified) | Ask which output type they want |
| "update my brand config" | Re-run Brand Setup Flow (pre-fill current values) |

Read only the relevant reference file — do not load all of them.

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


## General Principles

- **Consistency is everything.** Every output must use the exact hex codes, fonts, and tone from `brand-config.md`. Never improvise brand colors.
- **Brand config is the source of truth.** If there's a conflict between what the user says in chat and what's in the config, apply the config and flag the discrepancy.
- **Always present output.** Every file created should be presented to the user for review.
- **Offer brand refresh.** After completing a task, offer: "Want me to update your brand config with any changes?"

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
