---
description: Define project scope, objectives, stakeholders, and success criteria
argument-hint: "<project name> [software|general]"
---

# Project Charter

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a project charter that establishes the scope, objectives, and authority for a project.

## Usage

```
/project-charter <project name> [software|general]
```

### Arguments

- `project name` — The project to charter
- `software|general` — (Optional) PM context:
  - `software` — Tech/software project: architecture dependencies, team capacity, tech stack, CI/CD
  - `general` — Cross-industry project: business case, governance, procurement, compliance
  - If not specified, ask about the project type

## Workflow

### 1. Gather Context

Ask the user about: project purpose, sponsor, key stakeholders, timeline, constraints, and budget. Check ~~docs for any existing project documentation.

### 2. Build Charter

Use the **Initiation** skill. Read `../skills/initiation/SKILL.md` and apply the appropriate charter template.

### 3. Output

Deliver the project charter in markdown. Run through the charter quality checklist. Offer to save to ~~docs if connected.
