# Default Consulting Palettes

Fallback palettes when brand-config.md is not configured.
Present these options to the user and ask them to choose one.

---

## Palette 1 — Midnight Executive (classic consulting)
Best for: Strategy, financial services, executive-level decks
```
Primary:    1E2761  (deep navy)
Secondary:  CADCFC  (ice blue)
Accent:     E8B84B  (gold)
Background: FFFFFF  (white)
Text:       1A1A2E  (near-black)
Heading Font: Georgia
Body Font:    Calibri
```

---

## Palette 2 — Deloitte Green (professional services adjacent)
Best for: Consulting, transformation, AI strategy decks
```
Primary:    86BC25  (Deloitte green)
Secondary:  012169  (dark blue)
Accent:     00A3E0  (light blue)
Background: FFFFFF  (white)
Text:       1A1A1A  (near-black)
Heading Font: Arial Black
Body Font:    Arial
```

---

## Palette 3 — Charcoal Minimal (clean, modern)
Best for: Tech, AI, innovation pitches
```
Primary:    212121  (charcoal)
Secondary:  0D9488  (teal)
Accent:     F59E0B  (amber)
Background: FAFAFA  (off-white)
Text:       212121  (charcoal)
Heading Font: Trebuchet MS
Body Font:    Calibri
```

---

## Palette 4 — Navy & Coral (bold, high-contrast)
Best for: Client pitches, proposals, investor decks
```
Primary:    1B3A6B  (navy)
Secondary:  F96167  (coral)
Accent:     F9E795  (gold)
Background: FFFFFF  (white)
Text:       1B3A6B  (navy)
Heading Font: Cambria
Body Font:    Calibri
```

---

## Palette 5 — Premium Dark (high-stakes, boardroom)
Best for: Board presentations, PE/VC pitches, crisis comms
```
Primary:    0F172A  (near-black)
Secondary:  334155  (slate)
Accent:     38BDF8  (sky blue)
Background: 0F172A  (dark — use for title/closing slides)
Alt BG:     F8FAFC  (light — use for content slides)
Text:       F8FAFC  (off-white on dark)
Text Dark:  0F172A  (near-black on light)
Heading Font: Arial Black
Body Font:    Arial
```

---

## How to apply (pptxgenjs)

```javascript
// Example: Midnight Executive
const BRAND = {
  primary:    "1E2761",
  secondary:  "CADCFC",
  accent:     "E8B84B",
  background: "FFFFFF",
  text:       "1A1A2E",
  headingFont: "Georgia",
  bodyFont:    "Calibri"
};

// Title slide background
slide.background = { color: BRAND.primary };

// Slide title
slide.addText(title, {
  x: 0.5, y: 0.4, w: 9, h: 0.7,
  fontFace: BRAND.headingFont,
  color: BRAND.primary,
  fontSize: 28, bold: true, margin: 0
});

// Accent bar (left side of content slides)
slide.addShape(pres.shapes.RECTANGLE, {
  x: 0, y: 0, w: 0.08, h: 5.625,
  fill: { color: BRAND.accent }, line: { color: BRAND.accent }
});
```
