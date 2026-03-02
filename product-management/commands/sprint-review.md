---
description: Generate a sprint or iteration review summary
argument-hint: "<sprint name or number>"
---

# Sprint Review

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Generate a sprint review summary covering what shipped, metrics impact, and learnings.

## Usage

```
/sprint-review <sprint name or number>
```

### Arguments

- `sprint name or number` — The sprint or iteration to review

## Workflow

### 1. Gather Data

Ask the user about: what shipped, what didn't, any blockers. Check ~~project-tracker for completed tickets and ~~analytics for metrics changes.

### 2. Compile Review

Use the **Product Analytics** skill. Read `../skills/product-analytics/SKILL.md` and create the sprint review.

### 3. Output

Deliver the review: what shipped, metrics impact, user feedback, blockers, and action items for next sprint. Offer to post to ~~messaging if connected.
