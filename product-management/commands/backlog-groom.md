---
description: Structure and refine a product backlog
argument-hint: "<product or sprint>"
---

# Backlog Groom

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Structure and refine a product backlog — organize items, estimate effort, and ensure stories meet the Definition of Ready.

## Usage

```
/backlog-groom <product or sprint>
```

### Arguments

- `product or sprint` — The product backlog or upcoming sprint to groom

## Workflow

### 1. Gather Backlog

Ask the user for their current backlog items or check ~~project-tracker for existing tickets.

### 2. Groom

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and:
- Review each item against the Definition of Ready
- Split oversized stories into smaller deliverables
- Suggest story point estimates (Fibonacci)
- Flag items with unclear requirements or missing acceptance criteria
- Organize by priority and sprint readiness

### 3. Output

Deliver the groomed backlog: prioritized, estimated, and ready for sprint planning. Flag items that need more research or design before they're ready.
