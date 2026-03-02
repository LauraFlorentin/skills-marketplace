---
description: Run a comprehensive cross-cutting product review — triggers the orchestrator for multi-stage analysis
argument-hint: "<product name> [monthly|quarterly]"
---

# Product Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a comprehensive product review spanning strategy, discovery, execution, and growth.

**This command triggers the orchestrator agent** for cross-cutting analysis across all lifecycle stages.

## Usage

```
/product-review <product name> [monthly|quarterly]
```

### Arguments

- `product name` — The product to review
- `monthly|quarterly` — (Optional) Review cadence and depth:
  - `monthly` — Lightweight review: metrics check, roadmap progress, key risks
  - `quarterly` — Full QBR: strategy alignment, discovery health, execution quality, growth metrics, deep dives

## Workflow

### 1. Activate Orchestrator

Read the orchestrator at `../agents/orchestrator.md`. This command triggers the "Product review" routing path.

### 2. Cross-Stage Assessment

The orchestrator sequences:
1. **Strategy check** — Vision alignment, OKR progress
2. **Analytics pull** — North Star trend, funnel metrics, retention cohorts
3. **Planning assessment** — Roadmap progress, backlog health, sprint velocity
4. **Synthesis** — Unified report with alignment flags

### 3. Output

Deliver the product review report. If any strategic-execution divergence is detected, include an **Alignment Flag** section with resolution options for human decision.
