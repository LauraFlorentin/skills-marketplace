# M&A Advisory — Commands

Slash commands for Claude Code. Invoke commands through the `/ma-advisory:` namespace.

## Usage

In Claude Code, type `/ma-advisory:` to see available commands from this plugin.

## Available Commands

### Daily Operations (9)
| Command | Skill | Description |
|---------|-------|-------------|
| `/ma-advisory:vdr-classify` | VDR Management | Auto-folder raw VDR uploads into standard DD categories |
| `/ma-advisory:cim-extract` | Deal Screening | Extract EBITDA, adjustments, and defensibility narratives from a CIM |
| `/ma-advisory:redline-nda` | Legal Diligence | Review bidder NDA markup against firm playbook, generate counter-draft |
| `/ma-advisory:flag-coc` | Legal Diligence | Scan contracts for change-of-control, assignment, and termination clauses |
| `/ma-advisory:synergy-map` | Synergy Analysis | Compare target and buyer organizations for redundancies |
| `/ma-advisory:draft-qna` | Q&A Management | Draft diligence Q&A responses from approved VDR documents |
| `/ma-advisory:culture-diag` | Integration Planning | Analyze cultural friction points between acquirer and target |
| `/ma-advisory:screen-fdi` | Regulatory Screening | Screen against antitrust and FDI threshold triggers |
| `/ma-advisory:schedule-disclosure` | Legal Diligence | Draft disclosure schedules from VDR source documents |

### Report Generation (7)
| Command | Skill | Deliverable |
|---------|-------|-------------|
| `/ma-advisory:draft-cim` | Deal Marketing | Confidential Information Memorandum |
| `/ma-advisory:draft-ioi` | Deal Screening | Indication of Interest letter |
| `/ma-advisory:draft-red-flag` | Legal Diligence | Red Flag Due Diligence Report |
| `/ma-advisory:draft-qoe` | Financial Diligence | Quality of Earnings (Financial DD) Report |
| `/ma-advisory:draft-synergy-report` | Synergy Analysis | Synergy and Cost Savings Analysis |
| `/ma-advisory:draft-mgmt-deck` | Deal Marketing | Management Presentation (Equity Story) |
| `/ma-advisory:draft-pmi` | Integration Planning | Post-Merger Integration Target Operating Model |

### Workflow Chains (3)
| Command | Skill | Pipeline |
|---------|-------|---------|
| `/ma-advisory:chain-origination` | Workflow Chains | CIM extraction → valuation → IOI |
| `/ma-advisory:chain-red-flag` | Workflow Chains | VDR classify → CoC scan → Red Flag report |
| `/ma-advisory:chain-integration` | Workflow Chains | Synergy map → cost report → PMI plan |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `vdr-classify.md` → `/ma-advisory:vdr-classify`).
