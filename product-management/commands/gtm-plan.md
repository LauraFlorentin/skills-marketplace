---
description: Create a go-to-market plan for a product or feature launch
argument-hint: "<product or feature> [lean|enterprise]"
---

# GTM Plan

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a go-to-market plan for a product or feature launch.

## Usage

```
/gtm-plan <product or feature> [lean|enterprise]
```

### Arguments

- `product or feature` — The product or feature being launched
- `lean|enterprise` — (Optional) GTM style:
  - `lean` — Startup GTM: early adopters, community, content marketing, founder-led sales
  - `enterprise` — Cross-functional GTM: sales enablement, marketing campaigns, CS readiness, partner channels
  - If not specified, ask about team size and target market

## Workflow

### 1. Gather Context

Ask about: target audience, pricing, competitive positioning, launch timeline, available channels. Check ~~docs for existing positioning or messaging.

### 2. Build GTM Plan

Use the **Launch & Growth** skill. Read `../skills/launch-growth/SKILL.md` and create the GTM plan.

### 3. Output

Deliver the GTM plan with: target segments, messaging/positioning, channel strategy, timeline, success metrics, and owner for each workstream.
