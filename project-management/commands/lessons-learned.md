---
description: Compile lessons learned into a structured knowledge document
argument-hint: "<project name>"
---

# Lessons Learned

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Compile lessons learned from a project or phase into a structured document for organizational knowledge.

## Usage

```
/lessons-learned <project name>
```

### Arguments

- `project name` — The project to capture lessons from

## Workflow

### 1. Gather Inputs

Ask about: what went well, what didn't, surprises, what would you do differently. Check ~~docs for retro notes and ~~project-tracker for project history.

### 2. Compile

Use the **Closing** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/closing/SKILL.md` and organize lessons by category with root causes and recommendations.

### 3. Output

Deliver the lessons learned document. Flag lessons that apply organization-wide vs. project-specific. Offer to save to ~~docs as a knowledge base entry.
