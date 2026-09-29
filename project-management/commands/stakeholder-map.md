---
description: Map stakeholders by influence and interest with engagement strategies
argument-hint: "<project name>"
---

# Stakeholder Map

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map project stakeholders using a power/interest grid and define engagement strategies for each.

## Usage

```
/stakeholder-map <project name>
```

### Arguments

- `project name` — The project to map stakeholders for

## Workflow

### 1. Identify Stakeholders

Ask the user about: who is involved, who is affected, who has decision-making authority, who has concerns. Check ~~docs for any existing stakeholder lists.

### 2. Map & Analyze

Use the **Initiation** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/initiation/SKILL.md` and create:
- Stakeholder register with influence, interest, and engagement strategy
- Power/interest grid visualization
- Communication needs per stakeholder

### 3. Output

Deliver the stakeholder map and register. Flag any high-influence stakeholders who may resist the project.
