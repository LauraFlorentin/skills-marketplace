# Web & HTML Branding Reference

Create branded HTML artifacts — landing pages, email templates, web components, or style sheets — using the user's brand identity from `brand-config.md`.

---

## Prerequisites

1. Read `brand-config.md` — extract all brand variables
2. Read `/mnt/skills/public/frontend-design/SKILL.md` — follow design quality standards
3. Clarify the deliverable type if not specified (see Output Types below)

---

## Output Types

| Type | Description |
|---|---|
| **Landing page** | Single-page HTML with hero, features, CTA |
| **Email template** | HTML email, table-based layout, inline styles |
| **Component library** | Buttons, cards, badges, inputs styled to brand |
| **Style sheet** | CSS variables file defining the entire brand system |
| **Social media card** | OG image / shareable graphic as HTML/CSS |
| **Brand style guide** | Interactive HTML page showcasing the brand |

---

## CSS Brand Variables

Always start by defining CSS custom properties from brand-config.md. Include this in every output:

```css
:root {
  /* Brand: [Brand Name] */
  --color-primary: #[PRIMARY_HEX];
  --color-secondary: #[SECONDARY_HEX];
  --color-accent: #[ACCENT_HEX];
  --color-background: #[BACKGROUND_HEX];
  --color-text: #[TEXT_HEX];
  
  --font-heading: '[HEADING_FONT]', sans-serif;
  --font-body: '[BODY_FONT]', sans-serif;
  
  --radius: 8px;           /* adjust to brand personality */
  --shadow: 0 2px 12px rgba(0,0,0,0.08);
}
```

Import Google Fonts at the top of `<head>` for heading and body fonts if they're Google Fonts.

---

## Design Standards by Personality

Match the layout density and style to brand personality from config:

- **Bold & modern** → full-width sections, large typography, dark hero, high contrast
- **Warm & approachable** → rounded corners (12-16px), soft shadows, generous whitespace, warm tones
- **Clean & minimal** → strict grid, minimal decoration, lots of whitespace, thin typography
- **Luxurious & premium** → serif fonts, dark backgrounds, gold/metallic accents, elegant spacing
- **Technical/innovative** → monospace accents, sharp edges, data-forward layout, subtle gradients

---

## Landing Page Structure (if building full page)

```
1. <nav>      — Logo left, links right, CTA button in Primary color
2. <hero>     — Full-width, Primary background, large headline, tagline, CTA
3. <features> — 3-column grid, icon + heading + body per feature
4. <social proof> — Testimonial or stat callouts in Secondary color
5. <cta>      — Full-width banner, contrasting background, single action
6. <footer>   — Brand name, links, website URL, social handles from config
```

---

## Email Template Rules

- Use `<table>` layout (not flexbox/grid) — email clients require it
- All styles must be **inline** — no `<style>` blocks
- Max width: 600px, centered
- Use web-safe fonts as fallbacks (Arial, Georgia)
- Include plain-text version note
- Brand colors apply to: header bar, CTA button, footer background
- Logo in `<img>` tag at top — use a hosted URL or describe as placeholder

---

## Tone in Copy

When writing placeholder or actual copy:
- Match the **Tone** from brand-config.md
- Use **Key phrases/themes** naturally in headlines and body
- Avoid words listed under **Avoid** in config
- CTAs should be active, specific (not "Click here" → "Start your free trial")

---

## Quality Checklist

- [ ] CSS variables defined for all brand colors
- [ ] Google Fonts imported for heading + body fonts
- [ ] Logo included (or clear placeholder)
- [ ] Tagline used in hero/header
- [ ] Website URL in footer (if set)
- [ ] Responsive: works on mobile (320px) and desktop (1440px)
- [ ] Color contrast meets WCAG AA (4.5:1 for body text)
- [ ] No hardcoded colors — everything uses CSS variables

---

## Delivery

1. Save as `[BrandName]_[type].html` (e.g. `Acme_landing_page.html`)
2. Copy to `/mnt/user-data/outputs/`
3. Present via `present_files` tool (HTML renders in-browser preview)
4. Offer: "Want me to adjust the layout, copy, or generate additional components?"
