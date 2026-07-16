---
description: Audit and repair stale harness documentation, state, rules, and configuration without discarding active work
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-gc skill to garbage collect and repair the harness.

Scope (if specified): $ARGUMENTS

Follow the full workflow in the harness-gc SKILL.md:
1. Scan for all issue types (doc staleness, feature integrity, layer violations, dead context, stale locks)
2. Prioritize by severity (P0 → P3)
3. Apply supported P0 and P1 fixes within the requested scope
4. Surface product changes, lock removal, deletion, and archival choices for confirmation
5. Re-run relevant checks and generate a report only if this repo uses persistent reports

Do not stage, commit, stash, reset, revert, or delete active state automatically.

Output: issues by priority, fixes, decisions needed, and verification results.
