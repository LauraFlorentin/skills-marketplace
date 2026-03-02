---
description: Generate daily standup summaries or async standup templates
argument-hint: "<team or project> [sync|async]"
---

# Standup

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate standup summaries from project data or create async standup templates for your team.

## Usage

```
/standup <team or project> [sync|async]
```

### Arguments

- `team or project` — The team or project to run standups for
- `sync|async` — (Optional) Standup format:
  - `sync` — In-person or video standup agenda and facilitation guide
  - `async` — Slack/messaging template for asynchronous daily updates
  - If not specified, ask about the team's preference

## Workflow

### 1. Gather Context

Ask about: team size, sprint/phase status, known blockers. Check ~~project-tracker for recent activity and ~~messaging for existing standup channels.

### 2. Generate

Use the **Execution** skill. Read `../skills/execution/SKILL.md` and create the standup format.

### 3. Output

Deliver the standup template or summary. For async: provide a copy-paste message template for ~~messaging. For sync: provide a facilitation guide with time-boxes.
