---
description: Write a detailed feature specification with user stories and acceptance criteria
argument-hint: "<feature name>"
---

# Feature Spec

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Write a detailed feature specification ready for engineering handoff.

## Usage

```
/feature-spec <feature name>
```

### Arguments

- `feature name` — The feature to specify

## Workflow

### 1. Gather Context

Ask the user about: user stories, design references, technical constraints, and dependencies. Check ~~docs for related PRDs and ~~design for wireframes or mockups.

### 2. Write Spec

Use the **Planning** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/planning/SKILL.md` and create:
- User stories with acceptance criteria (Given/When/Then)
- Interaction design notes and error states
- Technical considerations (API contracts, data models)
- Out-of-scope items

### 3. Output

Deliver the feature spec in markdown. Offer to create tickets in ~~project-tracker if connected.
