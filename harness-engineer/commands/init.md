---
description: Scaffold a complete harness for this project. Generates AGENTS.md, features.json, init.sh, claude-progress.txt, layers.json, docs/ structure, and wires circuit breaker hooks.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-init skill to scaffold a complete harness for this project.

Project context: $ARGUMENTS

Follow the full workflow in the harness-init SKILL.md:
1. Gather context from the existing repo (or from the arguments above)
2. Generate AGENTS.md as a 100-line table of contents
3. Generate features.json with comprehensive feature list (all passes=false)
4. Generate init.sh with dev server startup and smoke test
5. Generate layers.json with architectural constraints
6. Create docs/ structure (architecture.md, quality.md, beliefs.md)
7. Wire circuit breaker hooks via install.sh
8. Make initial git commit

Output: tell me how many features were generated, what port the dev server uses, and that the harness is ready.
