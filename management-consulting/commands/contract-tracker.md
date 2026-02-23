---
description: Review contract status, track renewals, or manage change orders
argument-hint: "<client name> or <action>"
---

# Contract Management

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../CONNECTORS.md).

**Important**: Contract decisions should be reviewed by qualified legal professionals.

Track and manage the operational lifecycle of consulting contracts.

## Usage

```
/contract-tracker <client-or-action>
```

### Arguments

- `client-or-action` — Either:
  - A client name to review all contracts for that client
  - `renewals` — Review upcoming contract renewals
  - `change-order <client>` — Draft a change order for a specific engagement
  - `status` — Overview of all active contracts

## Workflow

### 1. Gather Contract Data

If ~~documents or ~~crm is connected:
- Pull active MSAs, SOWs, and amendments
- Check contract dates, values, and key terms
- Review billing status and outstanding invoices

If no data source is connected:
> Provide: client name, contract type (MSA/SOW), key dates (start, end, renewal), contract value, payment terms, and any pending changes.

### 2. Generate Output

**Contract Status Review:**
- Active contracts summary (client, type, value, expiration, status)
- Upcoming renewals within 90 days
- Outstanding change orders or amendments
- Billing status and receivables aging
- Risk flags (expiring contracts, unfavorable terms, scope concerns)

**Change Order Draft:**
- Reference to original SOW
- Description of scope change
- Impact on timeline, budget, and resources
- Approval signatures needed

### 3. Output

Provide the contract summary or change order draft with action items and escalation flags.
