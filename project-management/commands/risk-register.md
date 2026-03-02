---
description: Create a risk register with identification, scoring, and mitigation strategies
argument-hint: "<project name>"
---

# Risk Register

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

Create a risk register identifying project risks, scoring them by probability and impact, and defining response strategies.

## Usage

```
/risk-register <project name>
```

### Arguments

- `project name` — The project to identify risks for

## Workflow

### 1. Gather Context

Ask about: project scope, timeline pressure, team experience, dependencies, technology choices, stakeholder concerns. Check ~~docs for project charter and ~~project-tracker for known issues.

### 2. Identify & Score Risks

Use the **Planning** skill. Read `../skills/planning/SKILL.md` and:
- Identify risks using brainstorming, SWOT, and pre-mortem techniques
- Score each risk (Probability × Impact)
- Define response strategies (avoid, mitigate, transfer, accept)

### 3. Output

Deliver the risk register as a table with IDs, scores, owners, and response plans. Highlight the top 5 risks. Offer to save to ~~docs if connected.
