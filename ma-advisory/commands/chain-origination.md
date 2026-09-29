---
description: Coordinate an opportunity-to-IOI workflow with explicit evidence, dependencies, review gates, and authorization before submission
---

Use the **Workflow Chains** skill.

Read the full skill reference at `${CLAUDE_PLUGIN_ROOT}/skills/workflow-chains/SKILL.md` and execute **Chain 1: Origination to IOI**:

1. **Step 1**: Run `/ma-advisory:cim-extract` — strip CIM to isolate EBITDA, growth assumptions, concentration metrics
2. **Step 2**: Feed extracted data into valuation models for baseline pricing
3. **Step 3**: Run `/ma-advisory:draft-ioi` — generate customized IOI mapping buyer advantages to CIM growth pillars

Review and validate at each transition point before proceeding.

Ask the user for: the CIM document, the buyer's investment thesis, and approved valuation parameters.
