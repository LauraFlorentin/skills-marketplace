---
description: Create user personas from research data or team knowledge
argument-hint: "<product or segment> [proto|data-backed]"
---

# Persona

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create user personas for a product or customer segment.

## Usage

```
/persona <product or segment> [proto|data-backed]
```

### Arguments

- `product or segment` — The product or customer segment to build personas for
- `proto|data-backed` — (Optional) Persona depth:
  - `proto` — Lightweight proto-personas from founder intuition and early conversations
  - `data-backed` — Data-driven personas with behavioral segmentation and validation metrics
  - If not specified, ask about available research data

## Workflow

### 1. Gather Inputs

Ask the user about available research: interview transcripts, survey data, analytics, CRM data. Check ~~research-repo and ~~analytics for existing data.

### 2. Build Personas

Use the **Discovery** skill. Read `${CLAUDE_PLUGIN_ROOT}/skills/discovery/SKILL.md` and apply the appropriate persona template.

### 3. Output

Deliver 2-4 personas with name, role, goals, frustrations, tools, and a representative quote. For data-backed personas, include segment size and behavioral data.
