---
description: Define a metrics framework and dashboard specification
argument-hint: "<product or team>"
---

# Metrics Dashboard

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Define a metrics framework and dashboard specification for a product or team.

## Usage

```
/metrics-dashboard <product or team>
```

### Arguments

- `product or team` — The product or team to define metrics for

## Workflow

### 1. Gather Context

Ask the user about: product stage, business model, current metrics (if any), key questions they need the dashboard to answer. Check ~~analytics for existing instrumentation.

### 2. Design Framework

Use the **Product Analytics** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/product-analytics/SKILL.md` and define:
- North Star Metric with rationale
- Input metrics (3-5 levers)
- Dashboard layout with metric definitions, data sources, and refresh cadence

### 3. Output

Deliver the metrics framework and dashboard spec. Include implementation notes for ~~analytics if connected.
