---
description: Configure or update the brand identity used by Brand Studio
argument-hint: "[project|personal]"
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/SKILL.md` and `${CLAUDE_PLUGIN_ROOT}/skills/brand-studio/references/brand-config-template.md`.

Run the Brand Setup Flow. If `$ARGUMENTS` does not choose a scope, ask whether the brand applies to this project or should be the personal default. Write project configuration to `${CLAUDE_PROJECT_DIR}/.brand-studio/brand-config.md`; write a personal default to `${CLAUDE_PLUGIN_DATA}/brand-config.md`. Create the parent directory when needed. Never modify the bundled plugin copy.

If the selected config already exists, summarize it and confirm which fields the user wants to update before writing.
