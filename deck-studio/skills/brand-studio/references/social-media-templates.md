# Social Media Templates Reference

Create branded social media assets — banners, cards, and posts — using the user's brand identity from `brand-config.md`. All outputs are HTML/CSS files that render visually and can be screenshotted or exported.

---

## Prerequisites

1. Read `brand-config.md` — extract colors, fonts, logo, brand name, tagline, tone
2. Clarify which template type(s) the user wants (see Asset Types below)
3. Ask for any specific copy/content if not provided (headline, body text, CTA, image placeholder)

---

## Asset Types & Dimensions

| Template | Dimensions | Use case |
|---|---|---|
| **LinkedIn Banner** | 1584 × 396px | Profile cover image |
| **LinkedIn Post Card** | 1200 × 627px | Feed post with text + visual |
| **Twitter/X Header** | 1500 × 500px | Profile cover image |
| **Twitter/X Post Card** | 1200 × 675px | Feed post / quote card |
| **Instagram Square Post** | 1080 × 1080px | Feed post |
| **Instagram Story** | 1080 × 1920px | Story card |
| **Facebook Cover** | 820 × 312px | Page cover |
| **General Social Card** | 1200 × 630px | OG image / link preview |

When the user doesn't specify a platform, default to **LinkedIn Post Card + Instagram Square Post** as the most versatile pair.

Always build assets at 1x pixel dimensions in HTML — they render sharply and can be screenshotted at any scale.

---

## HTML Generation Approach

Generate each template as a **self-contained HTML file** with:
- Fixed pixel dimensions matching the asset type
- Inline or `<style>` block CSS (no external dependencies except Google Fonts)
- Google Fonts import for brand heading + body font
- All brand colors as CSS variables
- A clean `<div class="card">` wrapper at exact pixel dimensions

### Base Template Structure

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link href="https://fonts.googleapis.com/css2?family=[HEADING_FONT]:wght@400;600;700&family=[BODY_FONT]:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #[PRIMARY_HEX];
      --secondary: #[SECONDARY_HEX];
      --accent: #[ACCENT_HEX];
      --bg: #[BACKGROUND_HEX];
      --text: #[TEXT_HEX];
      --font-heading: '[HEADING_FONT]', sans-serif;
      --font-body: '[BODY_FONT]', sans-serif;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { width: [WIDTH]px; height: [HEIGHT]px; overflow: hidden; }
    .card {
      width: [WIDTH]px;
      height: [HEIGHT]px;
      position: relative;
      /* layout styles here */
    }
  </style>
</head>
<body>
  <div class="card">
    <!-- content here -->
  </div>
</body>
</html>
```

---

## Design Patterns by Template

### LinkedIn / Facebook Banner
- Full-width horizontal layout
- Brand primary color as background (or gradient primary → secondary)
- Brand name large left, tagline below in lighter weight
- Logo right-aligned or centered
- Subtle geometric accent shape (circle, diagonal stripe) in secondary color
- Keep center-left clear — profile photo overlaps left on LinkedIn

### Post Cards (LinkedIn, Twitter, Instagram Square)
Design variations to offer:

**1. Quote / Stat Card**
- Bold stat or quote as hero text (large, center or left)
- Brand primary or dark background
- Small brand name + logo in corner
- Accent color underline or highlight on key word

**2. Announcement Card**
- Headline top, supporting text below
- CTA button in accent color at bottom
- Brand logo top-left
- Background: brand color or clean white with color accents

**3. Tip / List Card**
- Numbered list of 3–5 points
- Each item has accent color number, body font text
- Header in primary color
- Clean, editorial layout

**4. Personal Brand / Thought Leadership Card**
- Large pull quote in italic heading font
- Author name + title at bottom
- Minimal design, lots of whitespace
- Subtle brand color accent (left border, bottom bar, or background tint)

### Instagram Story (vertical)
- Full-bleed vertical layout (1080 × 1920)
- Bold headline takes up top 40%
- Supporting content in middle
- CTA / swipe up prompt at bottom 15%
- Brand logo top-right corner, small

---

## Content Guidelines

When writing copy for the templates, use:
- **Tone** from brand-config.md
- **Key phrases/themes** naturally in headlines
- Avoid words listed under **Avoid** in config
- Headlines: punchy, ≤8 words
- Supporting text: 1–2 sentences max
- CTAs: active verb + outcome (e.g. "Read the full guide →", "Join 500+ leaders")

If the user provides their own copy, use it exactly — only apply brand styling.

---

## Batch Generation

When asked for a "social media kit" or multiple templates, generate them all in one pass:
1. LinkedIn Banner
2. LinkedIn Post Card (announcement style)
3. Twitter/X Post Card (quote style)
4. Instagram Square Post (tip/list style)
5. Instagram Story

Name files clearly: `[BrandName]_linkedin_banner.html`, `[BrandName]_instagram_square.html`, etc.

---

## Quality Checklist

Before presenting, verify each template:
- [ ] Exact brand hex codes used — no approximations
- [ ] Fonts loaded from Google Fonts
- [ ] Brand name and tagline correct
- [ ] Logo included (or clearly marked placeholder)
- [ ] Text is legible — sufficient contrast against background
- [ ] Layout looks intentional at the correct aspect ratio
- [ ] No content is clipped or overflowing the card bounds
- [ ] Tone of copy matches brand-config.md

---

## Delivery

1. Save each file as `[BrandName]_[platform]_[type].html`
2. Save all outputs to the workspace or artifact location provided by the host environment
3. Present all files via `present_files` tool — they render as visual previews
4. Offer: "Want me to swap the layout style, adjust copy, or generate more sizes?"
