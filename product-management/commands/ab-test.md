---
description: Design an A/B test with hypothesis, variants, and success metrics
argument-hint: "<feature or change to test>"
---

# A/B Test

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a rigorous A/B test for a product change.

## Usage

```
/ab-test <feature or change to test>
```

### Arguments

- `feature or change to test` — The change, feature variant, or UX modification to test

## Workflow

### 1. Define Hypothesis

Ask the user what they expect to happen and why. Frame as: "We believe [change] will cause [effect] for [segment], which we'll measure by [metric] over [timeframe]."

### 2. Design Test

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create:
- Hypothesis statement
- Control and variant descriptions
- Primary metric and guardrail metrics
- Sample size calculation and test duration estimate
- Segment targeting (if applicable)

Check ~~analytics for baseline metric values to inform sample size.

### 3. Output

Deliver the test design document. If ~~analytics supports feature flags or experimentation, offer to set up the test there.
