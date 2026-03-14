# Document Branding Reference

Apply the user's brand identity from `brand-config.md` to a Word (.docx) document.

---

## Prerequisites

1. Read `brand-config.md` — extract colors, fonts, logo path, brand name, tagline
2. Read `/mnt/skills/public/docx/SKILL.md` — follow all technical DOCX instructions from that skill
3. If the user has an existing `.docx` file: find it in `/mnt/user-data/uploads/`
4. If creating from scratch: ask for document type (report, proposal, memo, brief) and content

---

## What to Apply

### Document Header
- Top of every page: brand name in **Heading Font**, **Primary** color, left-aligned
- Tagline (if set) beside or below name in smaller **Body Font**, muted/secondary color
- Logo (if available): top-right of header
- Horizontal rule below header in **Primary** or **Secondary** color

### Typography Styles
- **Heading 1**: Heading Font, 20pt+, **Primary** color, bold
- **Heading 2**: Heading Font, 16pt, **Secondary** color, semibold
- **Heading 3**: Body Font, 13pt, dark text, bold
- **Body text**: Body Font, 11pt, dark text color from config
- **Captions**: Body Font, 9pt, muted gray

### Accent Elements
- Pull quotes / callout boxes: **Primary** color left border, light background tint
- Key stats or highlights: bold in **Secondary** color
- Table headers: **Primary** background, white text, **Heading Font**
- Table alternating rows: very light tint of Background color

### Document Footer
- Page number centered
- Website URL (if set) right-aligned in small **Body Font**
- Brand name left-aligned

### Cover Page (for reports/proposals)
- Full-page **Primary** color background
- Document title: large **Heading Font**, white
- Subtitle/date: **Body Font**, white or **Secondary** color
- Logo centered or bottom
- Tagline at bottom in smaller italic

---

## Tone Application

Use the **Tone** and **Key phrases** from brand-config.md when:
- Writing document boilerplate (executive summaries, introductions)
- Generating section headers
- Adding placeholder body text

Avoid words listed under **Avoid** in the config.

---

## Delivery

1. Save as `[BrandName]_branded_[original_filename].docx` (or descriptive name if new)
2. Copy to `/mnt/user-data/outputs/`
3. Present via `present_files` tool
4. Offer: "Want me to adjust styles, add sections, or update your brand config?"
