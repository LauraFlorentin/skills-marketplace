---
description: Define stakeholder communication cadence, channels, and ownership
argument-hint: "<project name>"
---

# Communication Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a communication plan covering who needs what information, how often, through which channels.

## Usage

```
/communication-plan <project name>
```

### Arguments

- `project name` — The project to plan communications for

## Workflow

### 1. Gather Context

Ask about: stakeholder list, team structure, reporting requirements, existing communication channels. Check ~~docs for stakeholder map.

### 2. Build Plan

Use the **Planning** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/planning/SKILL.md` and create:
- Communication matrix (audience, message, frequency, channel, owner)
- RACI matrix for key decisions
- Escalation path

### 3. Output

Deliver the communication plan and RACI matrix. Offer to set up channels in ~~messaging or recurring events in ~~calendar if connected.
