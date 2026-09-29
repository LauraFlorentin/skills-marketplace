---
description: Score and prioritize product opportunities using Opportunity Solution Trees
argument-hint: "<outcome or opportunity area>"
---

# Opportunity Scoring

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Score and prioritize product opportunities to identify the highest-impact areas to invest in.

## Usage

```
/opportunity-score <outcome or opportunity area>
```

### Arguments

- `outcome or opportunity area` — The desired outcome or area to identify opportunities in

## Workflow

### 1. Define the Target Outcome

Clarify what success looks like. What metric or user outcome are we optimizing for?

### 2. Map Opportunities

Use the **Discovery** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/discovery/SKILL.md` and build an Opportunity Solution Tree:
- Target outcome at the top
- Opportunities branching below (unmet needs, pain points, desires)
- Potential solutions for each opportunity
- Experiments to validate solutions

### 3. Score & Prioritize

Score each opportunity on: reach, impact, confidence, effort. Rank and recommend the top 2-3 opportunities to pursue.

### 4. Output

Deliver the Opportunity Solution Tree visualization and a prioritized list with scores and rationale.
