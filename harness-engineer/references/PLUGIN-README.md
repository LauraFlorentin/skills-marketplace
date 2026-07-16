# Harness Engineer Reference

## Components

```text
harness-engineer/
├── .claude-plugin/plugin.json
├── agents/orchestrator.md
├── commands/{init,doctor,gc,theory}.md
├── hooks/
│   ├── hooks.json
│   ├── circuit-breaker.sh
│   ├── dead-mans-switch.sh
│   ├── watchdog.sh
│   └── model-context.sh
├── skills/
│   ├── harness-init/
│   ├── harness-doctor/
│   ├── harness-gc/
│   ├── harness-onboard/
│   └── harness-engineering/
├── templates/
└── install.sh
```

Claude Code discovers skills, commands, agents, and `hooks/hooks.json` from their standard plugin locations. No project `.claude/settings.json` entry is required.

## Project opt-in

The packaged hooks are inactive unless the project has `.harness/config.json`. With the user's authorization, create it with:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/install.sh" --configure
```

The script preserves existing configuration. It does not copy hooks, stage or commit files, or edit Claude settings.

## Hook behavior

| Hook | Event | Behavior |
|---|---|---|
| Circuit breaker | Before file writes or edits | Counts repeated attempts; adds review context and later requests confirmation |
| Checkpoint reminder | After tool use | Warns once when a dirty worktree remains dirty beyond configured bands |
| Watchdog | Periodic after tool use | Reports invalid feature state and stale-lock candidates |
| Model context | Session start | Adds a short project-harness and verification reminder |

The hooks may write runtime counters only under `.harness/state/`. They do not modify application files, task locks, or Git state.

## Configuration

`.harness/config.json` controls hook thresholds. Environment variables override the corresponding value for temporary tuning:

| Variable | Default |
|---|---:|
| `HARNESS_SOFT_THRESHOLD` | 5 edits |
| `HARNESS_HARD_THRESHOLD` | 10 edits |
| `HARNESS_COMMIT_TIMEOUT` | 30 minutes |
| `HARNESS_CRITICAL_TIMEOUT` | 60 minutes |
| `HARNESS_HEALTH_CHECK_INTERVAL` | 20 tool calls |
| `HARNESS_LOCK_STALE_MINUTES` | 30 minutes |

Removing `.harness/config.json` opts the project out. Runtime counters reset at session start.

## Templates

Templates are starting points. Inspect the repository and adapt or skip each one. In particular, do not generate a persistent dev-server script, feature tracker, task locks, or layer model unless the project actually needs it.

## Troubleshooting

Run:

```bash
bash "${CLAUDE_PLUGIN_ROOT}/install.sh" --verify
```

If hook guidance is too noisy, change the environment thresholds or remove `.harness/config.json` to opt out. Preserve `.harness/state/` as ignored runtime state.
