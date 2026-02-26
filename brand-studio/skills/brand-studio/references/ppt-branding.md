# PPT Branding Reference

Apply the user's brand identity from `brand-config.md` to a PowerPoint presentation.

---

## Prerequisites

1. Read `brand-config.md` — extract colors, fonts, logo path, brand name
2. Read `/mnt/skills/public/pptx/SKILL.md` — follow all technical PPTX instructions from that skill
3. If the user has an existing `.pptx` file: find it in `/mnt/user-data/uploads/`
4. If creating from scratch: ask for slide topics/content before building

---

## What to Apply

### Slide Master / Global
- Set background color to brand **Background** color (or white if not set)
- Apply **Primary** color to all title text
- Apply **Body Font** to all body text, **Heading Font** to all titles
- If logo file exists in `assets/`: add it to every slide (bottom-right or top-left based on config)

### Title Slide
- Large centered brand name in **Heading Font**, **Primary** color
- Tagline below in **Body Font**, **Secondary** or muted color
- Full-bleed background using **Primary** color (white text version)
- Logo centered or top-left

### Section/Content Slides
- Slide title: **Heading Font**, **Primary** color
- Body text: **Body Font**, dark text color from config
- Accent shapes/dividers: **Secondary** or **Accent** color
- Data callouts / highlighted boxes: **Primary** color background, white text

### Charts & Tables (if present)
- Chart colors: cycle through Primary → Secondary → Accent
- Table header row: **Primary** background, white text
- Alternating rows: light tint of Background color

### Closing/Thank You Slide
- Mirror the title slide style
- Include website URL from config (if set) in footer

---

## Delivery

1. Save the branded file as `[BrandName]_branded_[original_filename].pptx`
2. Copy to `/mnt/user-data/outputs/`
3. Present via `present_files` tool
4. Offer: "Want me to adjust any colors, fonts, or slide layout?"
