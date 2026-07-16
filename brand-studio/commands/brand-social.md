---
description: Create branded social media assets for one platform or a complete channel kit
argument-hint: "[linkedin|x|instagram|full-kit]"
---

Load the active brand config from `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`, falling back to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. If neither exists, ask the user to run `/brand-studio:brand-setup`.

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/social-media-templates.md`. Create the platform or template requested in `$ARGUMENTS`; otherwise ask what the user needs. For `full-kit`, produce a LinkedIn banner and post card, X card, Instagram square, and Instagram story.

$ARGUMENTS
