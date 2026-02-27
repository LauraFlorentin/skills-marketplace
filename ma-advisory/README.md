# M&A Advisory

AI-powered workflows for the full mergers and acquisitions lifecycle — from origination and deal screening through due diligence, synergy underwriting, deal marketing, and post-merger integration.

> **Important**: This plugin assists with M&A advisory workflows but does not provide legal, financial, or professional advice. All outputs — especially in legal diligence and regulatory screening — should be reviewed by qualified professionals before use in live transactions.

## Skills

| Skill | Description |
| :--- | :--- |
| [VDR Management](./skills/vdr-management/SKILL.md) | Virtual Data Room classification, document categorization, and index standardization |
| [Deal Screening](./skills/deal-screening/SKILL.md) | CIM extraction, target evaluation, and IOI drafting |
| [Legal Diligence](./skills/legal-diligence/SKILL.md) | NDA redlining, change-of-control scanning, disclosure schedules, red flag reports |
| [Financial Diligence](./skills/financial-diligence/SKILL.md) | Quality of Earnings, EBITDA validation, working capital analysis |
| [Synergy Analysis](./skills/synergy-analysis/SKILL.md) | Headcount and vendor overlap mapping, cost-takeout plans |
| [Deal Marketing](./skills/deal-marketing/SKILL.md) | CIM drafting, management presentation decks |
| [Integration Planning](./skills/integration-planning/SKILL.md) | PMI target operating model, cultural diagnostics, Day 1 readiness |
| [Regulatory Screening](./skills/regulatory-screening/SKILL.md) | FDI and antitrust threshold screening across jurisdictions |
| [Q&A Management](./skills/qa-management/SKILL.md) | Diligence Q&A drafting, multi-bidder consistency tracking |
| [Workflow Chains](./skills/workflow-chains/SKILL.md) | End-to-end pipeline orchestration (3 chains) |

## Commands

### Daily Operations (9)

| Command | Description | Time Saved |
| :--- | :--- | :--- |
| `/vdr-classify` | Auto-folder raw VDR uploads into standard DD categories | 10+ hours |
| `/cim-extract` | Extract EBITDA, adjustments, and defensibility narratives from a CIM | 3-5 hours |
| `/redline-nda` | Review bidder NDA markup against firm playbook, generate counter-draft | 1-2 hours/bidder |
| `/flag-coc` | Scan contracts for change-of-control, assignment, and termination clauses | 20+ hours |
| `/synergy-map` | Compare target and buyer organizations for redundancies | 15+ hours |
| `/draft-qna` | Draft diligence Q&A responses from approved VDR documents | 30 min/query |
| `/culture-diag` | Analyze cultural friction points between acquirer and target | Days |
| `/screen-fdi` | Screen against antitrust and FDI threshold triggers | 8+ hours |
| `/schedule-disclosure` | Draft disclosure schedules from VDR source documents | 12+ hours |

### Report Generation (7)

| Command | Deliverable |
| :--- | :--- |
| `/draft-cim` | Confidential Information Memorandum |
| `/draft-ioi` | Indication of Interest letter |
| `/draft-red-flag` | Red Flag Due Diligence Report |
| `/draft-qoe` | Quality of Earnings (Financial DD) Report |
| `/draft-synergy-report` | Synergy and Cost Savings Analysis |
| `/draft-mgmt-deck` | Management Presentation (Equity Story) |
| `/draft-pmi` | Post-Merger Integration Target Operating Model |

### Workflow Chains (3)

| Command | Pipeline | Compression |
| :--- | :--- | :--- |
| `/chain-origination` | CIM extraction → valuation → IOI | 7 days → 4 hours |
| `/chain-red-flag` | VDR classify → CoC scan → Red Flag report | 5 days → 6 hours |
| `/chain-integration` | Synergy map → cost report → PMI plan | 3 weeks → 3 days |

## Example Workflows

### Buy-Side: New Opportunity
1. `/cim-extract` to screen the target
2. `/draft-ioi` to submit a competitive bid
3. Or chain it: `/chain-origination` for the full pipeline

### Sell-Side: Auction Process
1. `/redline-nda` for each incoming bidder markup
2. `/draft-qna` for buyer diligence questions
3. `/draft-cim` to build the marketing document

### Due Diligence
1. `/vdr-classify` to organize the data room
2. `/flag-coc` + `/schedule-disclosure` to scan contracts
3. `/draft-qoe` for financial DD
4. `/draft-red-flag` to compile findings
5. Or chain it: `/chain-red-flag` for the full pipeline

### Post-Signing
1. `/synergy-map` to quantify value creation
2. `/culture-diag` to assess integration risks
3. `/draft-pmi` to build the Day 1 plan
4. Or chain it: `/chain-integration` for the full pipeline

## Installation

### Claude Code / Cowork

Add the marketplace (`LauraFlorentin/skills-marketplace`) via Plugins, then install **ma-advisory**.

### Vercel AI SDK

```bash
npx skills add LauraFlorentin/skills-marketplace/ma-advisory
```
