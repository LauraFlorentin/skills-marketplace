---
description: "Execute Chain 1: Origination-to-IOI pipeline — compress 7 days of target evaluation and bid preparation into 4 hours"
---

Use the **Workflow Chains** skill.

Read the full skill reference at `../skills/workflow-chains/SKILL.md` and execute **Chain 1: Origination to IOI**:

1. **Step 1**: Run `/cim-extract` — strip CIM to isolate EBITDA, growth assumptions, concentration metrics
2. **Step 2**: Feed extracted data into valuation models for baseline pricing
3. **Step 3**: Run `/draft-ioi` — generate customized IOI mapping buyer advantages to CIM growth pillars

Review and validate at each transition point before proceeding.

Ask the user for: the CIM document, the buyer's investment thesis, and approved valuation parameters.
