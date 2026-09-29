---
description: Diagnose an agent-session failure from available repository evidence and propose the smallest preventive fix
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Use the harness-doctor skill to diagnose what went wrong and fix the harness.

Context about the failure (if known): $ARGUMENTS

Follow the full workflow in the harness-doctor SKILL.md:
1. Collect read-only evidence from the diff, logs, validation, instructions, and task state
2. Classify the failure mode(s) from the taxonomy
3. Propose the smallest targeted harness or regression-test change
4. Preserve the dirty worktree and request authorization for any recovery action
5. Apply changes only within the user's requested scope and verify them

Do not stage, commit, stash, reset, revert, or delete files unless the user explicitly authorizes that action.

Output: evidence, root cause, confidence, changes made, verification, and next action.
