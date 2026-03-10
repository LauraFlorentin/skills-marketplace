---
name: harness-engineer
description: "A complete harness engineering toolkit for agent-first development — scaffold harnesses, diagnose failures, garbage collect stale docs, and orient fresh sessions. Use when user says: 'set up a harness', 'my agent is stuck', 'agent loop broke', 'clean up the harness', 'start a new session', 'harness for this project', 'agent keeps failing', 'circuit breaker', 'garbage collect my docs', or 'agent made a mess'."
---

# Harness Engineer Plugin

A complete harness engineering toolkit synthesized from OpenAI, Anthropic, and LangChain's
2026 research. Prevents stuck loops, orients fresh agents, repairs failures, and fights entropy.

## Plugin Map

| Skill | Command | Trigger |
|---|---|---|
| `harness-init` | `/harness-engineer:init` | New project, new repo, needs harness scaffold |
| `harness-doctor` | `/harness-engineer:doctor` | Agent failed, loop broke, session went wrong |
| `harness-gc` | `/harness-engineer:gc` | Docs stale, constraints violated, features inconsistent |
| `harness-onboard` | Auto (SessionStart hook) | Every new Claude Code session in a harness project |
| `harness-engineering` | `/harness-engineer:theory` | Theory, CLASS metrics, Constitutional AI, evaluation design |

## Orchestrator Agent

For multi-stage workflows, the **orchestrator** (`agents/orchestrator.md`) classifies requests, sequences skills, and synthesizes outputs. Three operation modes:
- **Guided** (default) — single command, no orchestration
- **Supervised** — orchestrator recommends, user confirms
- **Autonomous** — orchestrator diagnoses + executes with circuit breaker safety rails

## Circuit Breaker System

Three deterministic hooks wired via `.claude/settings.json`:

| Hook | File | Fires |
|---|---|---|
| Circuit Breaker | `hooks/circuit-breaker.sh` | PostToolUse Write/Edit — hard stash at 10 edits |
| Dead Man's Switch | `hooks/dead-mans-switch.sh` | PostToolUse * — auto-stash at 30min no-commit |
| Watchdog | `hooks/watchdog.sh` | PostToolUse * every 10 calls — env health + lock cleanup |
| Pre-Completion | settings.json Stop hook | Before agent exits — forced verification |

## Quick Start

```bash
# Install into any project
bash .claude/plugins/harness-engineer/install.sh

# Scaffold a new harness
/harness-engineer:init

# After an agent failure
/harness-engineer:doctor

# Weekly maintenance
/harness-engineer:gc
```

## Examples

**Input**: "My Claude Code agent went into a loop and corrupted three files before I stopped it."

**What happens**: Run `/harness-engineer:doctor` — the skill analyzes the last 20 tool calls, identifies the loop trigger, proposes harness constraints to prevent recurrence, and outputs a `CONSTRAINTS.md` patch ready to apply.

---

**Input**: "Starting a new project and want to set up a proper agent harness from scratch."

**What happens**: Run `/harness-engineer:init` — scaffolds `HARNESS.md`, `PROGRESS.md`, `FEATURES.md`, `CONSTRAINTS.md`, and wires the three-layer circuit breaker hooks into `.claude/settings.json`.

---

**Input**: "My harness docs are stale — constraints reference files that no longer exist."

**What happens**: Run `/harness-engineer:gc` — audits all harness docs against the current codebase, removes stale references, updates feature states, and outputs a clean diff.

## Research Foundation

- **OpenAI** (Feb 13 2026): Context engineering, architectural constraints, garbage collection agents
- **Anthropic** (Nov 26 2025): Dual-agent architecture, progress files, JSON feature lists, git checkpoints
- **LangChain** (Feb 17 2026): LoopDetectionMiddleware, PreCompletionChecklist, reasoning sandwich, trace analysis

Read individual skill SKILL.md files for deep implementation details.

## References

- [PLUGIN-README.md](references/PLUGIN-README.md) — Full installation guide, hook wiring, and advanced configuration
