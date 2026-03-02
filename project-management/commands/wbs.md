---
description: Create a work breakdown structure for a project
argument-hint: "<project name> [software|general]"
---

# WBS

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a work breakdown structure decomposing a project into manageable deliverables and work packages.

## Usage

```
/wbs <project name> [software|general]
```

### Arguments

- `project name` — The project to decompose
- `software|general` — (Optional) PM context:
  - `software` — Epic → Feature → Story → Task decomposition with story points
  - `general` — Phase → Deliverable → Work Package → Activity decomposition with hours
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask about: project scope, major deliverables, known constraints. Check ~~docs for project charter or scope statement. Check ~~project-tracker for existing epics or work items.

### 2. Decompose

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and create the WBS with dictionary.

### 3. Output

Deliver the WBS in indented outline format with a WBS dictionary. Offer to create work items in ~~project-tracker if connected.
