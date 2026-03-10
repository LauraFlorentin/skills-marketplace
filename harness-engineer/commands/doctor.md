---
description: Diagnose the last agent session failure and generate harness patches to prevent recurrence. Reads git log, circuit breaker logs, progress files, and feature state.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-doctor skill to diagnose what went wrong and fix the harness.

Context about the failure (if known): $ARGUMENTS

Follow the full workflow in the harness-doctor SKILL.md:
1. Collect evidence (git log, circuit breaker logs, stash list, feature status)
2. Classify the failure mode(s) from the taxonomy
3. Generate and apply targeted harness patches
4. Recover the working state if the repo is dirty
5. Write a doctor report to claude-progress.txt
6. Commit all fixes

Output: tell me what failed, what was patched, and what to run next.
