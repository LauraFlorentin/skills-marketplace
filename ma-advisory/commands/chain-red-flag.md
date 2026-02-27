---
description: "Execute Chain 2: VDR Drop to Red Flag Report pipeline — compress 5 days of initial diligence into 6 hours"
---

Use the **Workflow Chains** skill.

Read the full skill reference at `../skills/workflow-chains/SKILL.md` and execute **Chain 2: VDR Drop to Initial Red Flag Report**:

1. **Step 1**: Run `/vdr-classify` — auto-categorize the document dump into Legal/Financial/HR/Ops folders
2. **Step 2**: Run `/flag-coc` + `/schedule-disclosure` (parallel) — scan for CoC risks AND extract core representations
3. **Step 3**: Generate Red Flag Report — populate Executive Risk Summary with discovered triggers and discrepancies

Review and validate at each transition point before proceeding.

Ask the user for: the VDR document set or describe the files to process.
