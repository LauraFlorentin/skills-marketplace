---
description: Inspect a project and scaffold only the agent-harness components it needs while preserving existing conventions
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-init skill to scaffold a complete harness for this project.

Project context: $ARGUMENTS

Follow the adaptive workflow in the harness-init SKILL.md:
1. Gather context from the existing repo (or from the arguments above)
2. Identify existing sources of truth and propose the smallest useful component set
3. Preserve or extend existing instructions, plans, tasks, and scripts
4. Generate only approved, project-specific harness files
5. Enable optional packaged hooks with `.harness/config.json` only when wanted
6. Parse and verify generated files and scripts

Do not modify Claude settings or stage, commit, stash, reset, or revert Git state.

Output: files created or preserved, assumptions, checks run, and optional next steps.
