# Harness Engineer

Design and maintain project scaffolding for reliable coding-agent work: concise repository instructions, executable acceptance criteria, session handoffs, architecture checks, failure diagnosis, and non-destructive loop warnings.

## Components

| Skill | Command | Purpose |
|---|---|---|
| `harness-init` | `/harness-engineer:init` | Propose and scaffold project-local harness files |
| `harness-doctor` | `/harness-engineer:doctor` | Diagnose a failed agent run from available evidence |
| `harness-gc` | `/harness-engineer:gc` | Audit and repair stale harness state |
| `harness-onboard` | direct invocation | Orient a session to an existing harness |
| `harness-engineering` | `/harness-engineer:theory` | Design context, constraints, and evaluations |

The optional `orchestrator` agent coordinates requests spanning multiple skills. See [the component reference](references/PLUGIN-README.md) for details.

## Hooks

The plugin packages non-destructive hooks in `hooks/hooks.json`. They can provide repeat-edit review context, dirty-worktree checkpoint reminders, health warnings, and a concise session orientation. They never commit, stash, reset, revert, delete locks, or edit project files.

Hooks are inactive until a project opts in with `.harness/config.json`. From this plugin directory:

```bash
bash install.sh --configure
bash install.sh --verify
```

The installer preserves existing configuration and does not edit Claude settings or Git state.

## Operating rule

Inspect existing repository conventions first, preserve user-authored requirements, and verify generated scripts. Never commit, stage, discard, or rewrite existing work unless the user has authorized that Git action.
