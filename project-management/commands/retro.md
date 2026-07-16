---
description: Facilitate a retrospective in multiple formats
argument-hint: "<team or project> [start-stop-continue|mad-sad-glad|4ls|sailboat|timeline]"
---

# Retro

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Facilitate a retrospective using one of several proven formats.

## Usage

```
/retro <team or project> [start-stop-continue|mad-sad-glad|4ls|sailboat|timeline]
```

### Arguments

- `team or project` — The team or project to run the retro for
- `start-stop-continue|mad-sad-glad|4ls|sailboat|timeline` — (Optional) Retro format:
  - `start-stop-continue` — Simple three-column retro, good for new teams
  - `mad-sad-glad` — Emotional temperature check
  - `4ls` — Liked/Learned/Lacked/Longed For — comprehensive
  - `sailboat` — Visual metaphor: Wind/Anchor/Rocks/Island
  - `timeline` — Walk through the sprint/project chronologically
  - If not specified, recommend based on team maturity and context

## Workflow

### 1. Gather Context

Ask about: what period are we reflecting on? How is the team feeling? Any known issues? Check ~~project-tracker for sprint data.

### 2. Facilitate

Use the **Closing** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/closing/SKILL.md` and generate the retro structure with facilitation guide.

### 3. Output

Deliver the retro board template, facilitation guide with time-boxes, and action item tracker. Offer to post to ~~messaging or ~~docs if connected.
