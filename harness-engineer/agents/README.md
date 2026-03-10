# Agents

## Agent Registry

| Agent | File | Purpose |
|---|---|---|
| Orchestrator | `orchestrator.md` | Master routing agent — classifies requests, sequences skills (init, doctor, gc, onboard, engineering), synthesizes reports. Supports Guided, Supervised, and Autonomous operation modes with circuit breaker integration. |

## Automatic Hooks

The `harness-onboard` skill fires automatically via the `SessionStart` hook — this is a passthrough route in the orchestrator (Route 4) and requires no user invocation.
