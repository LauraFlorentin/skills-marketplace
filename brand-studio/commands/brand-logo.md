---
description: Create logo concepts and SVG variants from the active brand identity
argument-hint: "[wordmark|lettermark|combination|icon|badge]"
---

Load the active brand config from `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`, falling back to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. If neither exists, ask the user to run `/brand-studio:brand-setup`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/logo-creator.md`. Ask which logo type the user wants when `$ARGUMENTS` does not specify one. Create full-color, dark-background, and monochrome SVG variants.

$ARGUMENTS
