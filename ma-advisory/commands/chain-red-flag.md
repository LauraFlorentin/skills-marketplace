---
description: Coordinate VDR intake through an initial red-flag report with source tracking, specialist review, and stop conditions
---

Use the **Workflow Chains** skill.

Read the full skill reference at `${CLAUDE_PLUGIN_ROOT}/skills/workflow-chains/SKILL.md` and execute **Chain 2: VDR Drop to Initial Red Flag Report**:

1. **Step 1**: Run `/ma-advisory:vdr-classify` — propose and review Legal/Financial/HR/Ops classifications without mutating the VDR
2. **Step 2**: Run `/ma-advisory:flag-coc` + `/ma-advisory:schedule-disclosure` (parallel) — scan for CoC risks AND extract core representations
3. **Step 3**: Generate Red Flag Report — populate Executive Risk Summary with discovered triggers and discrepancies

Review and validate at each transition point before proceeding.

Ask the user for: the VDR document set or describe the files to process.
