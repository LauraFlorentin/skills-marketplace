---
description: Design a growth experiment targeting acquisition, activation, retention, or referral
argument-hint: "<growth lever> [acquisition|activation|retention|revenue|referral]"
---

# Growth Experiment

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Design a structured growth experiment targeting a specific stage of the user funnel.

## Usage

```
/growth-experiment <growth lever> [acquisition|activation|retention|revenue|referral]
```

### Arguments

- `growth lever` — The specific idea or area to experiment with
- `acquisition|activation|retention|revenue|referral` — (Optional) Which stage of the pirate metrics (AARRR) funnel this targets

## Workflow

### 1. Define the Lever

Ask the user about: current funnel metrics, biggest drop-off points, growth goals. Check ~~analytics for funnel data if connected.

### 2. Design Experiment

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create:
- Hypothesis
- Target metric and baseline
- Experiment design (what changes, for whom)
- Expected impact and effort (ICE score)
- Timeline and success criteria
- Learning goal (what will we know after this, regardless of outcome?)

### 3. Output

Deliver the experiment design. Recommend whether to run it as a quick test or a full A/B test based on effort and risk.
