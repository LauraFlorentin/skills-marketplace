---
description: Generate a kickoff meeting agenda and preparation checklist
argument-hint: "<project name> [software|general]"
---

# Kickoff

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a kickoff meeting agenda, preparation checklist, and follow-up template.

## Usage

```
/kickoff <project name> [software|general]
```

### Arguments

- `project name` — The project to kick off
- `software|general` — (Optional) PM context:
  - `software` — Includes tech stack walkthrough, dev environment setup, CI/CD overview
  - `general` — Includes governance walkthrough, roles and responsibilities, milestone overview
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask about: project charter (is there one?), attendee list, meeting duration, key decisions to make. Check ~~docs for existing charter or project brief.

### 2. Build Agenda

Use the **Initiation** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/initiation/SKILL.md` and create the kickoff package.

### 3. Output

Deliver the kickoff agenda, pre-meeting checklist, and post-meeting follow-up template. Offer to schedule via ~~calendar or post to ~~messaging if connected.
