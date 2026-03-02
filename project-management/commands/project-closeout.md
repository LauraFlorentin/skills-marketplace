---
description: Generate a project closeout report with handoff checklist
argument-hint: "<project name> [software|general]"
---

# Project Closeout

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a comprehensive project closeout report and handoff checklist.

## Usage

```
/project-closeout <project name> [software|general]
```

### Arguments

- `project name` — The project to close out
- `software|general` — (Optional) PM context:
  - `software` — Includes release notes, runbook handoff, tech debt register, on-call transition
  - `general` — Includes formal acceptance, contract closure, benefits realization plan
  - If not specified, ask about the project type

## Workflow

### 1. Gather Status

Ask about: were all deliverables accepted? Any open items? Final budget status? Check ~~project-tracker for open items and ~~docs for project documentation.

### 2. Compile Closeout

Use the **Closing** skill. Read `../skills/closing/SKILL.md` and create:
- Closeout report (objectives vs. actuals)
- Handoff checklist
- Lessons learned summary

### 3. Output

Deliver the closeout report and checklist. Flag any incomplete items that need resolution before formal closure.
