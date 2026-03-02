# Agents

## Orchestrator

**File:** [`orchestrator.md`](./orchestrator.md)

The orchestrator is the master routing agent for multi-stage project management workflows. It classifies requests, selects lifecycle skills, sequences them, and synthesizes outputs into unified reports.

### Routing Paths

| Route | Trigger | Skills Deployed |
|-------|---------|----------------|
| Health Check | "project health check", "how is the project doing" | Planning → Execution → Monitoring → Synthesis |
| Stakeholder Update | "status report for leadership", "steering committee update" | Monitoring → Synthesis (formatted for audience) |
| New Project Setup | "new project", "project kickoff" | Initiation → Planning → Execution |
| Project Recovery | "project is behind", "recovery plan", "red status" | Monitoring → Planning → Execution |
| Project Closeout | "close the project", "project wrap-up" | Monitoring → Closing |
| Single-Stage | Maps to one skill | Direct passthrough |

### Key Features

- **Bidirectional re-entry routing** — loops back to earlier stages when gaps are found, and resumes forward when issues resolve
- **Conflict escalation with severity thresholds** — Low (noted), Medium (Alignment Flag), High (requires immediate decision)
- **Partial data protocol** — flags gaps, proceeds with available data, marks confidence levels
- **Single-pass synthesis** — snapshot execution model, not a live loop
