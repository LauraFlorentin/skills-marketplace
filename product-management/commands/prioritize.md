---
description: Run a prioritization exercise using RICE, ICE, MoSCoW, or weighted scoring
argument-hint: "<items to prioritize> [rice|ice|moscow|weighted]"
---

# Prioritize

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Run a structured prioritization exercise on a set of features, initiatives, or backlog items.

## Usage

```
/prioritize <items to prioritize> [rice|ice|moscow|weighted]
```

### Arguments

- `items to prioritize` — The features, initiatives, or backlog items to rank
- `rice|ice|moscow|weighted` — (Optional) Prioritization framework:
  - `rice` — Reach x Impact x Confidence / Effort — best for data-rich environments
  - `ice` — Impact x Confidence x Ease — best for speed
  - `moscow` — Must/Should/Could/Won't — best for scope negotiation
  - `weighted` — Custom weighted scoring — best for cross-team decisions with multiple stakeholders
  - If not specified, recommend a framework based on context

## Workflow

### 1. Gather Items

Ask the user for the list of items to prioritize. Check ~~project-tracker for backlog items if connected.

### 2. Score Items

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and apply the selected framework. For each item, score on all dimensions.

### 3. Output

Deliver a ranked table with scores, a brief rationale for the top 3, and any items that were difficult to score (flagged for discussion).
