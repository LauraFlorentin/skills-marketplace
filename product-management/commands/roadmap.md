---
description: Build a product roadmap — Now/Next/Later or timeline format
argument-hint: "<product or team> [lean|detailed]"
---

# Roadmap

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Build a product roadmap for a product or team.

## Usage

```
/roadmap <product or team> [lean|detailed]
```

### Arguments

- `product or team` — The product or team to roadmap for
- `lean|detailed` — (Optional) Roadmap style:
  - `lean` — Now/Next/Later theme-based roadmap, no dates, fits on one page
  - `detailed` — Timeline roadmap with quarterly milestones, dependencies, and swim lanes
  - If not specified, ask about team size and planning horizon

## Workflow

### 1. Gather Inputs

Ask the user about: strategic priorities, OKRs, backlog themes, dependencies, stakeholder needs. Check ~~roadmap-tool and ~~project-tracker for existing data.

### 2. Build Roadmap

Use the **Planning** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/planning/SKILL.md` and apply the appropriate roadmap format.

### 3. Output

Deliver the roadmap in markdown. For lean: themed columns (Now/Next/Later). For detailed: timeline with milestones, owners, and dependencies. Offer to save to ~~roadmap-tool if connected.
