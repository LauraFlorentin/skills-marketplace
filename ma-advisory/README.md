# M&A Advisory

Source-traceable workflows for transaction screening, diligence, marketing, bidding, synergy analysis, regulatory issue spotting, and integration planning.

> This plugin supports professional workflows; it is not legal, tax, accounting, valuation, regulatory, securities, or investment advice. Use current authoritative sources and qualified advisers for live transactions. Protect confidential and privileged deal information.

## Skills

| Skill | Purpose |
|---|---|
| [VDR Management](skills/vdr-management/SKILL.md) | Document classification and proposed data-room index |
| [Deal Screening](skills/deal-screening/SKILL.md) | CIM extraction, preliminary evaluation, and IOI drafting |
| [Legal Diligence](skills/legal-diligence/SKILL.md) | Contract comparison, cited issue spotting, and disclosure support |
| [Financial Diligence](skills/financial-diligence/SKILL.md) | QoE, EBITDA, working-capital, and debt-like-item analysis |
| [Synergy Analysis](skills/synergy-analysis/SKILL.md) | Savings, timing, dependencies, and costs to achieve |
| [Deal Marketing](skills/deal-marketing/SKILL.md) | Source-backed CIM and management-presentation drafts |
| [Integration Planning](skills/integration-planning/SKILL.md) | Governance, Day 1, workstreams, and change planning |
| [Regulatory Screening](skills/regulatory-screening/SKILL.md) | Current-source preliminary filing and approval map |
| [Q&A Management](skills/qa-management/SKILL.md) | Cited response drafts and approval routing |
| [Workflow Chains](skills/workflow-chains/SKILL.md) | Multi-stage dependencies, gates, and audit trail |

## Commands

The plugin includes 19 namespaced commands. Type `/ma-advisory:` in Claude Code to discover them; see [commands/README.md](commands/README.md) for the catalog.

Typical entry points:

- `/ma-advisory:cim-extract`
- `/ma-advisory:vdr-classify`
- `/ma-advisory:draft-qoe`
- `/ma-advisory:screen-fdi`
- `/ma-advisory:chain-red-flag`

Commands create drafts and analyses. They do not authorize VDR mutation, external distribution, bid submission, regulatory filing, or legal-document acceptance.

## Installation

Add the `LauraFlorentin/skills-marketplace` marketplace in Claude Code, then install `ma-advisory`.

For compatible skill installers:

```bash
npx skills add LauraFlorentin/skills-marketplace/ma-advisory
```
