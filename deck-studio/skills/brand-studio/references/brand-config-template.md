# Brand Configuration Template

Use this template when writing brand-config.md after setup. Replace all placeholder values with the user's actual brand details.

---

## Template to write into brand-config.md:

```markdown
# Brand Config
# Last updated: [DATE]
# To update: say "update my brand config" to Claude

## Identity
- **Brand Name:** [Company Name]
- **Tagline:** [One-line tagline or "Not set"]
- **Industry:** [Industry/sector]
- **Personality:** [e.g. Bold & modern, Warm & approachable]

## Colors
- **Primary:** #[HEXCODE] — [name/description, e.g. "Deep Navy"]
- **Secondary:** #[HEXCODE] — [name/description, e.g. "Gold"]
- **Accent:** #[HEXCODE] — [name/description, e.g. "White"] (or "Not set")
- **Background:** #[HEXCODE] — [e.g. "Off-white #FAFAFA"] (or "Not set")
- **Text/Dark:** #[HEXCODE] — [e.g. "Near-black #1A1A1A"]

## Typography
- **Heading Font:** [Font name, e.g. "Poppins"] — [weight, e.g. "Bold/SemiBold"]
- **Body Font:** [Font name, e.g. "Inter"] — [weight, e.g. "Regular/Light"]
- **Accent Font:** [Font name or "Not set"] — [use case if set]

## Logo
- **Logo file:** [filename in assets/ folder, or "Not provided"]
- **Logo description:** [Brief description for generation, e.g. "Minimalist wordmark in primary color"]
- **Logo placement:** [e.g. "Top-left on slides, centered on docs"]

## Voice & Tone
- **Tone:** [e.g. Professional but approachable, Confident and direct]
- **Key phrases/themes:** [e.g. "innovation, trust, transformation" or "Not set"]
- **Avoid:** [e.g. "jargon, passive voice" or "Not set"]

## Web & Contact
- **Website:** [URL or "Not set"]
- **Social handles:** [e.g. "@brandname" or "Not set"]
```

---

## Notes for Claude when writing brand-config.md:

1. Always suggest hex codes if the user only describes colors (e.g. "deep navy" → suggest #1B2A4A, confirm with user)
2. If no font preference, suggest a pairing based on brand personality:
   - Bold/modern → Poppins + Inter
   - Warm/approachable → Lora + Source Sans Pro  
   - Luxurious → Playfair Display + Cormorant Garamond
   - Technical/clean → IBM Plex Sans + IBM Plex Mono
3. Store project configuration at `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md` or the personal default at `${CLAUDE_PLUGIN_DATA}/brand-config.md`; never edit the installed plugin directory
4. After writing, confirm by reading the file back and summarizing it to the user
