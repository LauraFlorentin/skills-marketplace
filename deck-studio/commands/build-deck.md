---
description: Build a complete presentation from brief through approved storyboard, slide content, and PPTX
argument-hint: "<topic or presentation brief>"
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/deck-builder/SKILL.md`. Run its four-stage pipeline: diagnose the presentation context, approve a storyboard of action titles, write slide content, then generate the PPTX. Use the project or personal brand config when available and the bundled default palettes otherwise.

Use `$ARGUMENTS` as the initial brief. Preserve the storyboard approval checkpoint before drafting slides.

$ARGUMENTS
