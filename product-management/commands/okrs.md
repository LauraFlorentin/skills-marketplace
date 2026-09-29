---
description: Draft OKRs with measurable key results
argument-hint: "<team or product> [quarterly|annual]"
---

# OKRs

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Draft Objectives and Key Results for a team or product area.

## Usage

```
/okrs <team or product> [quarterly|annual]
```

### Arguments

- `team or product` — The team, product area, or company to draft OKRs for
- `quarterly|annual` — (Optional) OKR cadence. Defaults to quarterly.

## Workflow

### 1. Gather Context

Ask the user about:
- What is the team's mission or product vision?
- What are the top priorities this period?
- Any existing OKRs or strategic goals to align with?

Check ~~docs for existing OKRs, vision docs, or strategy materials.

### 2. Draft OKRs

Use the **Strategy** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/strategy/SKILL.md` and apply the appropriate OKR framework (team-level for startups, cascading for enterprise).

### 3. Output

Deliver OKRs in a structured format: Objective → Key Results (3-4 each) with owners and measurement criteria. Flag any KRs that look like activities rather than outcomes.
