# M&A Advisory — Commands

Slash commands for Claude Code. Each `.md` file in this directory becomes a `/command-name` you can invoke directly.

## Usage

In Claude Code, type `/` to see available commands from this plugin.

## Available Commands

### Daily Operations (9)
| Command | Skill | Description |
|---------|-------|-------------|
| `/vdr-classify` | VDR Management | Auto-folder raw VDR uploads into standard DD categories |
| `/cim-extract` | Deal Screening | Extract EBITDA, adjustments, and defensibility narratives from a CIM |
| `/redline-nda` | Legal Diligence | Review bidder NDA markup against firm playbook, generate counter-draft |
| `/flag-coc` | Legal Diligence | Scan contracts for change-of-control, assignment, and termination clauses |
| `/synergy-map` | Synergy Analysis | Compare target and buyer organizations for redundancies |
| `/draft-qna` | Q&A Management | Draft diligence Q&A responses from approved VDR documents |
| `/culture-diag` | Integration Planning | Analyze cultural friction points between acquirer and target |
| `/screen-fdi` | Regulatory Screening | Screen against antitrust and FDI threshold triggers |
| `/schedule-disclosure` | Legal Diligence | Draft disclosure schedules from VDR source documents |

### Report Generation (7)
| Command | Skill | Deliverable |
|---------|-------|-------------|
| `/draft-cim` | Deal Marketing | Confidential Information Memorandum |
| `/draft-ioi` | Deal Screening | Indication of Interest letter |
| `/draft-red-flag` | Legal Diligence | Red Flag Due Diligence Report |
| `/draft-qoe` | Financial Diligence | Quality of Earnings (Financial DD) Report |
| `/draft-synergy-report` | Synergy Analysis | Synergy and Cost Savings Analysis |
| `/draft-mgmt-deck` | Deal Marketing | Management Presentation (Equity Story) |
| `/draft-pmi` | Integration Planning | Post-Merger Integration Target Operating Model |

### Workflow Chains (3)
| Command | Skill | Pipeline |
|---------|-------|---------|
| `/chain-origination` | Workflow Chains | CIM extraction → valuation → IOI |
| `/chain-red-flag` | Workflow Chains | VDR classify → CoC scan → Red Flag report |
| `/chain-integration` | Workflow Chains | Synergy map → cost report → PMI plan |

## Adding a Command

Create a new `.md` file in this directory:

```markdown
---
description: Brief description of what this command does
---

Your command instructions here...
```

The filename becomes the command name (e.g., `vdr-classify.md` → `/vdr-classify`).
