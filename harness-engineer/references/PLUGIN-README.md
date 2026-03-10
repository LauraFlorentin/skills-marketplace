# Harness Engineer Plugin

> Agent-first development toolkit. Prevents stuck loops, orients fresh agents, repairs failures, and fights entropy.

Built from OpenAI, Anthropic, and LangChain's harness engineering research (Feb 2026).

---

## Install

```bash
bash .claude/plugins/harness-engineer/install.sh
git commit -m "feat: install harness-engineer plugin"
/harness-engineer:init
```

---

## Four Skills

### `/harness-engineer:init` — Scaffold
Generates everything a fresh project needs for agent-first development in one command.

- `AGENTS.md` — 100-line table of contents (map, not encyclopedia)
- `features.json` — all features pre-marked failing, JSON format
- `init.sh` — dev server startup + smoke test
- `claude-progress.txt` — session handoff log
- `layers.json` — architectural dependency constraints
- `docs/` — architecture, quality, design, beliefs
- `current_tasks/` — multi-agent task locks

### `/harness-engineer:doctor` — Diagnose & Fix
After any agent session goes wrong, runs a structured failure diagnosis and patches the harness.

8 failure modes detected: `DOOM_LOOP`, `PREMATURE_EXIT`, `ONE_SHOT`, `DIRTY_STASH`, `BROKEN_FOUNDATION`, `LAYER_VIOLATION`, `CONTEXT_BLIND`, `ENVIRONMENT_BLIND`

Every fix is written by the agent and committed — never applied manually.

### `/harness-engineer:gc` — Garbage Collect
Periodic maintenance. Finds and fixes 7 categories of entropy:

1. Stale documentation references
2. Inconsistent feature states
3. Architectural layer violations
4. Dead context (removed features, old plans)
5. Progress file bloat
6. Stale task locks
7. Harness config drift

Produces a GC report with health score. Run weekly on active projects.

### Auto: `harness-onboard` — Session Startup
Fires automatically via `SessionStart` hook. Orients every fresh agent in ~30 seconds.

- Reads git log + progress file
- Maps the environment (directory structure, available tools)
- Picks next feature from features.json
- Acquires task lock for parallel-agent safety
- Applies reasoning sandwich: xhigh → high → xhigh

---

## Circuit Breaker System

Three deterministic hooks that prevent stuck loops from corrupting the codebase.

```
File Edit    → circuit-breaker.sh    Soft nudge at 5 edits, hard stash+revert at 10
Any Tool     → dead-mans-switch.sh  Warning at 15min no-commit, auto-stash at 30min
Every 10     → watchdog.sh          Dev server health, layer checks, stale lock cleanup
On Stop      → Pre-completion       Forced end-to-end verification before declaring done
```

All stashes are preserved with descriptive messages. Nothing is ever deleted automatically.

---

## Research Foundation

| Component | Source |
|---|---|
| AGENTS.md as TOC, docs/ as truth | OpenAI Harness Engineering (Feb 13 2026) |
| features.json, progress files, git checkpoints | Anthropic Effective Harnesses (Nov 26 2025) |
| JSON > Markdown for agent-edited files | Anthropic |
| LoopDetectionMiddleware → circuit breaker | LangChain Deep Agents (Feb 17 2026) |
| PreCompletionChecklist → Stop hook | LangChain |
| Reasoning sandwich (xhigh/high/xhigh) | LangChain |
| LocalContextMiddleware → onboard ritual | LangChain |
| Task locks (current_tasks/) | Anthropic C Compiler (2025) |
| Garbage collection agents | OpenAI |
| Failure = harness signal | OpenAI |

---

## File Structure

```
harness-engineer/
├── SKILL.md                           ← Plugin entry point
├── install.sh                         ← Wires everything into a project
├── hooks/
│   ├── circuit-breaker.sh             ← Layer 1: loop detection + hard stash
│   ├── dead-mans-switch.sh            ← Layer 2: time-based commit watchdog
│   └── watchdog.sh                    ← Layer 3: env health + lock cleanup
├── skills/
│   ├── harness-init/SKILL.md          ← Scaffold skill
│   ├── harness-doctor/SKILL.md        ← Diagnosis skill
│   ├── harness-gc/
│   │   ├── SKILL.md                   ← GC skill
│   │   └── scripts/
│   │       ├── check-layers.sh        ← Layer constraint validator
│   │       └── check-doc-refs.py      ← Documentation staleness checker
│   └── harness-onboard/SKILL.md       ← Session startup skill
├── commands/
│   ├── init.md                        ← /harness-engineer:init
│   ├── doctor.md                      ← /harness-engineer:doctor
│   └── gc.md                          ← /harness-engineer:gc
└── templates/
    ├── AGENTS.md.template
    ├── features.json.template
    ├── init.sh.template
    ├── layers.json.template
    └── settings.json.template
```

---

## Configuration

Edit `.harness/config.json` after install:

```json
{
  "dev_server_port": 3000,
  "circuit_breaker": {
    "soft_threshold": 5,
    "hard_threshold": 10
  },
  "dead_mans_switch": {
    "warning_minutes": 15,
    "critical_minutes": 30
  },
  "watchdog": {
    "check_interval_tool_calls": 10,
    "lock_stale_minutes": 20
  }
}
```

Or via env vars: `HARNESS_SOFT_THRESHOLD`, `HARNESS_HARD_THRESHOLD`, `HARNESS_COMMIT_TIMEOUT`, `HARNESS_CRITICAL_TIMEOUT`, `HARNESS_HEALTH_CHECK_INTERVAL`, `HARNESS_LOCK_STALE_MINUTES`

---

## Verify Installation

```bash
bash .claude/plugins/harness-engineer/install.sh --verify
```
