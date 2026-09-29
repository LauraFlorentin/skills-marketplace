---
description: Record and track project decisions with context and rationale
argument-hint: "<decision summary>"
---

# Decision Log

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Record a project decision with full context, rationale, alternatives considered, and impact.

## Usage

```
/decision-log <decision summary>
```

### Arguments

- `decision summary` — A brief description of the decision to record

## Workflow

### 1. Gather Context

Ask about: what was decided, why, what alternatives were considered, who made the decision, what's affected. Check ~~docs for existing decision log.

### 2. Record Decision

Use the **Execution** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/execution/SKILL.md` and create a structured decision record.

### 3. Output

Deliver the decision record. Append to existing decision log if one exists in ~~docs, or create a new one.
