---
description: Apply the active brand identity to a Word document or create a new branded DOCX
argument-hint: "<document or brief>"
---

Load the active brand config from `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`, falling back to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. If neither exists, ask the user to run `/brand-studio:brand-setup`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/doc-branding.md`. Apply the brand to the Word document the user specifies. If no `.docx` is available, ask whether to brand an existing file or create a new document.

$ARGUMENTS
