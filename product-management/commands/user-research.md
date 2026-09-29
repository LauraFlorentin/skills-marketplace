---
description: Design a user research plan with interview guides
argument-hint: "<research topic> [guerrilla|formal]"
---

# User Research

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a user research plan including methodology, recruiting criteria, and interview guides.

## Usage

```
/user-research <research topic> [guerrilla|formal]
```

### Arguments

- `research topic` — The question, feature, or problem area to research
- `guerrilla|formal` — (Optional) Research style:
  - `guerrilla` — Quick, scrappy research for startups: intercept interviews, unmoderated surveys, 5-user tests
  - `formal` — Structured research for enterprise: recruiting criteria, moderated interviews, research repository
  - If not specified, ask the user about their timeline and resources

## Workflow

### 1. Define Research Questions

Ask the user what they're trying to learn. Frame as 3-5 specific research questions.

### 2. Design Research Plan

Use the **Discovery** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/discovery/SKILL.md` and create:
- Research methodology
- Participant criteria and recruiting plan
- Interview guide with opening, exploration, and closing sections
- Synthesis plan

### 3. Output

Deliver the research plan and interview guide. If ~~research-repo is connected, offer to save it there.
