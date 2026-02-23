---
description: Draft a client proposal or statement of work
argument-hint: "<client name> <engagement type>"
---

# Proposal / SOW Drafting

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

**Important**: All proposals and SOWs should be reviewed by qualified professionals before submission to clients.

Draft a proposal or statement of work for a consulting engagement.

## Usage

```
/proposal <client> <engagement-type>
```

### Arguments

- `client` — Client name or identifier
- `engagement-type` — Type of engagement:
  - `strategy` — Strategic advisory engagement
  - `assessment` — Current-state assessment or diagnostic
  - `transformation` — Operating model transformation or process redesign
  - `implementation` — Implementation support or program management
  - `custom` — Custom engagement type (describe in prompt)

## Workflow

### 1. Gather Context

If ~~crm or ~~documents is connected:
- Pull existing client information, past proposals, and relationship history
- Review any RFP or brief documents provided

If no data source is connected:
> Connect ~~crm or ~~documents to pull client context automatically. To draft manually, provide:
> 1. Client name and industry
> 2. Business challenge or opportunity being addressed
> 3. Desired outcomes and success criteria
> 4. Estimated duration and team size
> 5. Pricing model preference (fixed fee, T&M, retainer)
> 6. Any constraints (budget, timeline, travel)

### 2. Draft Proposal

Generate a proposal with these sections:
1. **Executive Summary** — One-page overview of the opportunity and proposed approach
2. **Understanding of Need** — Demonstrate comprehension of the client's challenge
3. **Proposed Approach** — Phased methodology with key activities per phase
4. **Team & Staffing** — Proposed team composition with relevant experience
5. **Timeline & Milestones** — Visual timeline with key deliverables and checkpoints
6. **Investment** — Pricing with clear breakdown by phase or workstream
7. **Why Us** — Differentiators and relevant proof points

### 3. Draft SOW (if requested)

Generate a SOW with:
1. **Scope of Services** — Detailed scope with explicit inclusions and exclusions
2. **Deliverables** — Numbered list with acceptance criteria
3. **Assumptions** — Key assumptions that underpin the scope and pricing
4. **Timeline** — Milestone schedule with dependencies
5. **Billing Schedule** — Payment terms tied to milestones or time periods
6. **Change Order Process** — How scope changes will be handled

### 4. Output

Provide:
1. Complete proposal or SOW draft
2. Pricing summary with rate card assumptions
3. Risk flags or items needing client clarification
4. Suggested next steps for the sales process
