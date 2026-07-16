---
description: Generate a launch readiness checklist
argument-hint: "<product or feature> [simple|phased]"
---

# Launch Checklist

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a launch readiness checklist to ensure nothing is missed before shipping.

## Usage

```
/launch-checklist <product or feature> [simple|phased]
```

### Arguments

- `product or feature` — The product or feature being launched
- `simple|phased` — (Optional) Launch complexity:
  - `simple` — Basic checklist: feature complete, QA, analytics, support, comms
  - `phased` — Enterprise phased rollout: internal → beta → % rollout → GA, with feature flags, rollback plan, monitoring
  - If not specified, ask about the blast radius and risk level

## Workflow

### 1. Gather Context

Ask about: launch date, rollout strategy, stakeholders, dependencies. Check ~~project-tracker for open blockers.

### 2. Build Checklist

Use the **Launch & Growth** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/launch-growth/SKILL.md` and generate the checklist.

### 3. Output

Deliver a categorized checklist (Engineering, Design, Marketing, Support, Legal) with owners and status. Include a launch day run-of-show if applicable.
