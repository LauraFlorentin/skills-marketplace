# Logo Creator Reference

Generate a professional brand logo using the user's brand identity from `brand-config.md`.

---

## Prerequisites

1. Read `brand-config.md` — extract brand name, personality, colors, fonts, logo description
2. Clarify logo type with user if not already specified (see Logo Types below)

---

## Logo Types — Ask the User Which They Want

| Type | Description | Best for |
|---|---|---|
| **Wordmark** | Brand name only, styled typographically | Clean, text-forward brands |
| **Lettermark** | Initials only (e.g. "IBM", "HP") | Brands with long names |
| **Icon + Wordmark** | Symbol beside brand name | Most versatile, recommended default |
| **Icon only** | Abstract or pictorial symbol alone | Brands with strong recognition |
| **Badge/Emblem** | Text enclosed in a shape | Heritage, premium, sports brands |

Default recommendation: **Icon + Wordmark** unless brand personality suggests otherwise.

---

## Generation Approach

Logos are generated as **SVG files** (vector, infinitely scalable, downloadable). For complex designs, also export a PNG via Python/Pillow.

### Step 1 — Design Brief
Based on brand-config.md, internally draft:
- Primary concept: What does the icon represent? (abstract geometric, initial letter, industry symbol)
- Visual mood: Does it match the brand personality?
- Color application: Which brand colors go where?
- Typography: Use the Heading Font for wordmark text

### Step 2 — Generate SVG

Write clean, well-structured SVG code. Requirements:
- ViewBox: `0 0 400 150` for horizontal logo, `0 0 200 200` for icon-only
- Use exact hex codes from brand-config.md — never approximate
- Embed font via Google Fonts `<defs>` or use web-safe fallbacks
- Icon should be on the left, wordmark on the right (for horizontal)
- Include a `<title>` element with the brand name for accessibility
- Design must look professional at both 32px and 300px size

### Step 3 — Variations to Generate

Always generate 3 variations:
1. **Full color** — primary background or transparent, brand colors
2. **Dark version** — dark background, light text/icon
3. **Monochrome** — single color (black or white), for flexibility

### Step 4 — PNG Export (optional but recommended)

Use Python + cairosvg or Pillow to export PNG at 2x resolution (800×300 for horizontal):

```python
import subprocess
# If cairosvg available:
# cairosvg.svg2png(url='logo.svg', write_to='logo.png', scale=2)

# Fallback: save SVG and instruct user to convert
```

---

## Quality Checklist

Before presenting, verify:
- [ ] Colors exactly match brand-config.md hex codes
- [ ] Brand name spelled correctly
- [ ] Icon is clean and not overly complex at small sizes
- [ ] Looks balanced — icon and text proportionally matched
- [ ] Works on both light and dark backgrounds (check both versions)
- [ ] SVG code is valid and renders without errors

---

## Delivery

1. Save SVG files as `[BrandName]_logo_color.svg`, `[BrandName]_logo_dark.svg`, `[BrandName]_logo_mono.svg`
2. If PNG generated: `[BrandName]_logo.png`
3. Copy all to `/mnt/user-data/outputs/`
4. Present all files via `present_files` tool
5. Offer: "Want me to try a different icon concept, adjust proportions, or update the colors?"

---

## Icon Concept Ideas by Brand Personality

Use these as starting points — always customize to the actual brand:

- **Bold & modern** → geometric shapes, sharp angles, negative space tricks
- **Warm & approachable** → rounded forms, soft curves, organic shapes
- **Luxurious & premium** → thin letterforms, minimalist icon, gold/dark palette
- **Technical/innovative** → circuit-inspired lines, data patterns, abstract nodes
- **Clean & minimal** → initial letter with clever negative space, single-weight icon
