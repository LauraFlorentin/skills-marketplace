---
description: Apply the active brand identity to a PowerPoint deck or create a new branded PPTX
argument-hint: "<presentation or brief>"
---

Load the active brand config from `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`, falling back to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. If neither exists, ask the user to run `/brand-studio:brand-setup`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/ppt-branding.md`. Apply the brand to the PowerPoint file the user specifies. If no `.pptx` is available, ask whether to brand an existing deck or create a new one.

$ARGUMENTS
