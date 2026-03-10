---
description: Garbage collect the harness. Find and fix stale docs, layer violations, stuck features, dead context, and entropy accumulated from agent-generated code.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-gc skill to garbage collect and repair the harness.

Scope (if specified): $ARGUMENTS

Follow the full workflow in the harness-gc SKILL.md:
1. Scan for all issue types (doc staleness, feature integrity, layer violations, dead context, stale locks)
2. Prioritize by severity (P0 → P3)
3. Apply all P0 and P1 fixes
4. Log P2/P3 items in docs/tech-debt.md
5. Generate a GC report in docs/
6. Commit all fixes

Output: GC report summary with issues found, fixed, and health score.
