---
description: Generate a product vision document — lean canvas or full vision doc
argument-hint: "<product name> [lean|full]"
---

# Product Vision

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a product vision document for a product or feature.

## Usage

```
/vision <product name> [lean|full]
```

### Arguments

- `product name` — The product or feature to create a vision for
- `lean|full` — (Optional) Vision format:
  - `lean` — Lean canvas: one-page format ideal for startups and early-stage products
  - `full` — Full vision doc with strategic context, stakeholder alignment, and review cadence for enterprise teams
  - If not specified, ask the user about their team size and context to recommend a format

## Workflow

### 1. Gather Context

Ask the user about:
- What problem does this product solve?
- Who is the target customer?
- What does success look like in 12 months?

Check ~~docs for any existing vision documents or strategy materials.

### 2. Generate Vision

Use the **Strategy** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/strategy/SKILL.md` and apply the appropriate vision template (lean or full).

### 3. Output

Deliver the vision document in markdown. If ~~docs is connected, offer to save it there.
