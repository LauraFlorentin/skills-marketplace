---
description: Map jobs-to-be-done and desired outcomes
argument-hint: "<product or feature>"
---

# Jobs-to-be-Done

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map the jobs your customers are trying to accomplish and their desired outcomes.

## Usage

```
/jtbd <product or feature>
```

### Arguments

- `product or feature` — The product or feature area to map jobs for

## Workflow

### 1. Gather Context

Ask the user about the customer and situation. What are they trying to accomplish? What tools or workarounds do they use today?

### 2. Map Jobs

Use the **Discovery** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/discovery/SKILL.md` and apply the JTBD framework:
- Core functional jobs
- Related jobs
- Emotional and social jobs
- Job map (define → locate → prepare → confirm → execute → monitor → modify → conclude)

### 3. Output

Deliver job statements in standard format: "When I [situation], I want to [motivation], so I can [expected outcome]." Include importance vs. satisfaction scoring for prioritization.
