---
description: Map competitive landscape and positioning
argument-hint: "<product or market>"
---

# Competitive Analysis

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Map the competitive landscape for a product or market segment.

## Usage

```
/competitive-analysis <product or market>
```

### Arguments

- `product or market` — The product, market, or segment to analyze competitively

## Workflow

### 1. Gather Context

Ask the user about:
- Who do they currently consider competitors?
- What dimensions matter most (features, pricing, market share, UX)?
- Any specific competitors to include or exclude?

### 2. Research & Analyze

Use the **Strategy** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/strategy/SKILL.md` and apply the appropriate competitive analysis framework.

Use web search for competitor data: pricing pages, feature lists, press releases, Crunchbase profiles, G2/Capterra reviews.

### 3. Output

Deliver:
1. Competitive landscape overview (top 5-10 players)
2. Feature comparison matrix
3. Positioning map (2-axis)
4. Key takeaways: where you're strong, where you're vulnerable, white space opportunities
