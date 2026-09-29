---
description: Create a branded HTML artifact, email, style guide, or component library
argument-hint: "<artifact type or brief>"
---

Load the active brand config from `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`, falling back to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. If neither exists, ask the user to run `/brand-studio:brand-setup`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/web-branding.md`. Build the artifact specified in `$ARGUMENTS`; otherwise ask what the user needs.

$ARGUMENTS
