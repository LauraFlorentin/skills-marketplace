---
name: orchestrator
description: Coordinate multi-stage harness engineering across setup, failure diagnosis, maintenance, onboarding, and evaluation design. Use when a request spans more than one Harness Engineer skill or needs sequencing and synthesis.
---

# Harness Engineer Orchestrator

Route a request to the smallest useful skill sequence. Preserve existing work and user authority throughout.

## Skill registry

| Need | Skill |
|---|---|
| New or missing project harness | `harness-init` |
| Failed or recurring agent behavior | `harness-doctor` |
| Stale instructions, plans, or harness state | `harness-gc` |
| Fresh-session orientation | `harness-onboard` |
| Context, constraint, or evaluation design | `harness-engineering` |

## Routes

- **New setup:** inspect repository → consult theory only for non-obvious design choices → initialize selected components → verify.
- **Failure recovery:** preserve and inspect current state → diagnose → propose the smallest fix → apply within scope → reproduce or verify.
- **Maintenance:** audit → prioritize → repair supported drift → surface deletions or product changes → verify.
- **Existing-project orientation:** onboard only; do not add scaffold unless a concrete gap appears.
- **Mixed request:** sequence dependencies and avoid re-running scans whose results are already available.

## Safety boundary

The plugin's hooks provide warnings and permission prompts only. They do not authorize any agent to stage, commit, stash, reset, revert, delete locks, install dependencies, start services, or write to external systems. Request explicit authority when the user's task does not already include such an action.

Treat a dirty worktree, task lock, or existing configuration as owned state. Preserve it and surface conflicts rather than “recovering” automatically.

## Decision process

1. Restate the concrete outcome and determine whether the request is read-only or authorizes changes.
2. Read applicable repository instructions and identify existing sources of truth.
3. Choose one skill when possible; add another only for a dependency or newly discovered issue.
4. State assumptions and user decisions required before material structural changes.
5. Verify each change with the repository's actual tooling.
6. Synthesize evidence, changes, checks, unresolved risks, and next action.

Do not invent autonomy modes or switch modes based on trigger phrases. Follow the user's explicit scope and the host agent's permission model.
