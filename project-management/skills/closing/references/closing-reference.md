# Closing — Detailed Reference

Detailed frameworks, templates, and field-level guidance. Read when SKILL.md directs you here.

---

## Project Closeout

Formally ending a project so deliverables are accepted, knowledge transferred, resources released, and the organization can measure goal achievement. Skipping closeout is one of the most common and costly PM failures.

### Closeout Checklist Template

```
PROJECT CLOSEOUT CHECKLIST
============================
Project: _______________  PM: _______________
Closeout Date: _______________  Sign-off By: _______________

DELIVERABLES
[ ] All deliverables formally accepted by stakeholder (sign-off documented)
[ ] Acceptance criteria verified for each deliverable
[ ] All deliverables stored in agreed-upon location
[ ] Outstanding defects/issues documented and transferred to BAU team

DOCUMENTATION
[ ] Project documentation archived (plans, designs, meeting notes)
[ ] Knowledge transfer sessions completed
[ ] Runbooks and operational documentation complete and reviewed
[ ] Architecture decision records (ADRs) up to date
[ ] User/admin guides finalized and published

FINANCIALS
[ ] Final budget reconciliation complete (planned vs. actual)
[ ] All purchase orders closed
[ ] Vendor contracts closed or transitioned to BAU
[ ] All vendor payments processed
[ ] Time tracking records finalized

RESOURCES
[ ] Team members formally released or transitioned
[ ] Resource managers notified of availability
[ ] Access and permissions revoked for project-specific systems
[ ] Contractor/vendor access removed

TOOLS & ENVIRONMENTS
[ ] Project boards archived (Jira, Trello, Asana, etc.)
[ ] Repositories transferred to long-term owner or archived
[ ] Staging/dev environments decommissioned or transferred
[ ] CI/CD pipelines transferred or decommissioned
[ ] Cloud resources tagged and ownership transferred

COMMUNICATION
[ ] Final status report sent to all stakeholders
[ ] Stakeholders notified of support/escalation path post-project
[ ] Team celebration/recognition completed
[ ] Lessons learned published and accessible

PM: _________________ (sign)  Date: ________  Sponsor: _________________ (sign)  Date: ________
```

### Software Mode: Release, Runbook, and Technical Handoff

**Release Notes Compilation Template:**

```
RELEASE NOTES — v[X.Y.Z]
===========================
Release Date: _______________  Release Manager: _______________

SUMMARY: [2-3 sentence overview of what this release delivers]

NEW FEATURES:
- [TICKET-123] Feature name: Brief description and why it matters
- [TICKET-456] Feature name: Brief description

IMPROVEMENTS:
- [TICKET-234] What changed and expected impact

BUG FIXES:
- [TICKET-345] What was broken and how it is resolved

BREAKING CHANGES:
- [TICKET-890] Description, migration steps required. Migration guide: [link]

KNOWN ISSUES:
- [TICKET-901] Description, workaround, expected fix timeline

DEPENDENCIES:
- Requires database migration v[X] (run before deploy)
- Requires environment variable [VAR_NAME]

ROLLBACK PROCEDURE: [Steps to rollback if critical issues discovered post-deploy]
```

**Runbook Handoff Template (Operations Documentation):**

```
OPERATIONS RUNBOOK — [Service/Application Name]
=================================================
Version: ___________  Last Updated: ___________  Author: ___________  Handoff To: ___________

SERVICE OVERVIEW:
- Purpose: [1-2 sentences]  Architecture: [Monolith/microservice/serverless]
- Repository: [URL]  Documentation: [URL]  Slack: [#channel]

WHAT TO MONITOR:
| Metric              | Expected Range | Alert Threshold | Dashboard Link |
|---------------------|----------------|-----------------|----------------|
| Response time (p99) | < 200ms        | > 500ms         | [link]         |
| Error rate          | < 0.1%         | > 1%            | [link]         |
| CPU utilization     | 20-60%         | > 85%           | [link]         |
| Memory utilization  | 30-70%         | > 90%           | [link]         |
| Queue depth         | < 100          | > 500           | [link]         |

HOW TO RESTART: [Step-by-step procedure, commands/scripts, post-restart verification, expected recovery time]
HOW TO DEPLOY: [Deployment procedure or CI/CD link, pre/post-deploy checks, rollback steps]

KNOWN ISSUES:
| Issue                          | Workaround                    | Fix Status             |
|--------------------------------|-------------------------------|------------------------|
| Memory leak under high traffic | Restart pods every 48 hours   | Backlog TICK-1234      |
| Slow query on /reports         | Read replica; monitor timeout | Scheduled for v2.3     |

ESCALATION CONTACTS:
| Level | Contact             | Channel            | Response Time |
|-------|---------------------|--------------------|---------------|
| L1    | On-call engineer    | PagerDuty          | 15 min        |
| L2    | Team tech lead      | Slack #team-oncall | 30 min        |
| L3    | Engineering manager | Phone              | 1 hour        |

TROUBLESHOOTING:
- Symptom: [desc] -> Cause: [cause] -> Fix: [steps]
- Symptom: [desc] -> Cause: [cause] -> Fix: [steps]
```

**Monitoring/Alerting Transfer Checklist:** All alert rules documented and ownership transferred. Dashboard access granted. Alert channels updated (PagerDuty, Slack, email). On-call rotation updated. Escalation policies reviewed with receiving team. Historical incident context shared.

**On-Call Rotation Handoff:** Provide 2 weeks of shadowed on-call (original team primary, new team shadow). Document top 10 most common alerts and resolutions. Share 3 months of incident history. Confirm new team has access to all systems, dashboards, and runbooks.

**Tech Debt Register Handoff:**

```
TECH DEBT REGISTER — [Service/Project Name]
=============================================
Handoff Date: _______________  Handed Off To: _______________

| # | Debt Item                       | Category    | Priority | Est. Effort | Impact If Ignored            | Ticket    |
|---|---------------------------------|-------------|----------|-------------|------------------------------|-----------|
| 1 | Legacy auth module rewrite      | Code        | High     | 3 sprints   | Security vulnerability risk  | TICK-2001 |
| 2 | No integration tests for API v2 | Testing     | High     | 1 sprint    | Regressions on every deploy  | TICK-2002 |
| 3 | Hardcoded config values         | Code        | Medium   | 2 days      | Cannot change without deploy | TICK-2003 |
| 4 | Outdated dependency (log4j)     | Security    | High     | 1 day       | Known CVE exposure           | TICK-2004 |

Categories: Code, Testing, Security, Performance, Infrastructure, Documentation
Priority: High (within 1 quarter), Medium (within 2 quarters), Low (when convenient)
```

**Environment Cleanup:** Feature branches merged or deleted (stale > 30 days). Staging cleaned up. Feature flags removed for shipped features. CI/CD pipeline ownership transferred. Cloud resources tagged with new owner. Unused infra decommissioned. Secrets rotated and ownership transferred.

**CI/CD Pipeline Ownership Transfer:** Document all pipelines (build, test, deploy, IaC). Transfer admin access. Walk through configuration and custom scripts. Confirm receiving team can trigger, modify, and debug independently. Update notification channels.

### General Mode: Acceptance, Contracts, and Benefits Tracking

**Formal Acceptance Documentation Template:**

```
PROJECT ACCEPTANCE FORM
=========================
Project: _______________  Date: _______________
Sponsor: _______________  PM: _______________

| # | Deliverable | Acceptance Criteria Met? | Accepted By | Date | Notes |
|---|-------------|--------------------------|-------------|------|-------|
| 1 |             | Yes / Partial / No       |             |      |       |
| 2 |             | Yes / Partial / No       |             |      |       |
| 3 |             | Yes / Partial / No       |             |      |       |

OUTSTANDING ITEMS (if Partial):
| # | Item | Resolution Plan | Owner | Due Date |
|---|------|-----------------|-------|----------|
| 1 |      |                 |       |          |

ACCEPTANCE STATEMENT: I confirm deliverables listed above are accepted as complete
per agreed scope and acceptance criteria.
Sponsor: _________________ Date: _______  PM: _________________ Date: _______
```

**Contract Closure Checklist:** All contractual deliverables completed and accepted. Final vendor performance review. All change orders reconciled. Final payment processed. Warranty/support terms documented. Contract file archived with amendments. Vendor performance evaluation completed. IP/confidentiality obligations confirmed.

**Benefits Realization Plan:**

```
BENEFITS REALIZATION PLAN
============================
Project: _______________  PM: _______________  Benefits Owner: _______________

| # | Expected Benefit                | Metric              | Baseline | 3-Mo Target | 6-Mo Target | 12-Mo Target | Measurement Method     |
|---|---------------------------------|----------------------|----------|-------------|-------------|--------------|------------------------|
| 1 | Reduce support tickets          | Tickets/month        | 450      | 350         | 250         | 200          | Zendesk monthly report |
| 2 | Improve onboarding time         | Days to productivity | 21       | 14          | 10          | 10           | HR tracker             |
| 3 | Revenue from new channel        | Monthly revenue ($)  | $0       | $50K        | $150K       | $400K        | Finance monthly close  |
| 4 | Reduce manual processing        | Hours/week           | 40       | 20          | 10          | 5            | Time tracking system   |

REVIEW SCHEDULE: 3-month [Date], 6-month [Date], 12-month [Date]
ESCALATION: If off-target, Benefits Owner escalates to Sponsor with root cause and corrective plan.
```

**Archive Procedures:**

| What to Archive                     | Where                           | Retention | Access             |
|-------------------------------------|---------------------------------|-----------|--------------------|
| Project charter, plan, schedule     | PMO SharePoint / Confluence     | 7 years   | PMO + project team |
| Financial records                   | Finance system of record        | 7 years   | Finance + PM       |
| Contracts and legal documents       | Legal document management       | 10 years  | Legal + PM         |
| Technical docs and code             | Repository (GitHub, GitLab)     | Indefinite| Engineering        |
| Meeting minutes and decisions       | PMO SharePoint / Confluence     | 3 years   | PMO + project team |
| Lessons learned                     | Lessons learned database        | Indefinite| All employees      |

**PMO Reporting and Portfolio Update:** Update portfolio register to "Closed." Submit final metrics (schedule/budget variance, scope changes, quality). Update resource capacity planning. Archive in PMO inventory with final RAG status and summary.

### Project Closeout Report Template

```
PROJECT CLOSEOUT REPORT
=========================
Project: _______________  PM: _______________  Date: _______________  Sponsor: _______________

1. PROJECT SUMMARY
[3-5 sentences: what the project was, why undertaken, what it delivered.]

2. OBJECTIVES: ACHIEVED vs. PLANNED
| # | Objective | Planned Outcome | Actual Outcome | Status              |
|---|-----------|-----------------|----------------|---------------------|
| 1 |           |                 |                | Met / Partial / Not Met |
| 2 |           |                 |                | Met / Partial / Not Met |
| 3 |           |                 |                | Met / Partial / Not Met |

3. SCHEDULE PERFORMANCE
| Milestone                  | Planned Date | Actual Date | Variance (days) | Reason          |
|----------------------------|--------------|-------------|-----------------|-----------------|
| Kickoff                    |              |             |                 |                 |
| Requirements complete      |              |             |                 |                 |
| Design complete            |              |             |                 |                 |
| Build complete             |              |             |                 |                 |
| Testing complete           |              |             |                 |                 |
| Go-live / Launch           |              |             |                 |                 |

4. BUDGET PERFORMANCE
| Category                   | Planned ($) | Actual ($) | Variance ($) | Variance (%) |
|----------------------------|-------------|------------|--------------|--------------|
| Internal labor             |             |            |              |              |
| External labor             |             |            |              |              |
| Software/licensing         |             |            |              |              |
| Infrastructure             |             |            |              |              |
| TOTAL                      |             |            |              |              |

5. KEY METRICS
- Metric 1: _______________  Metric 2: _______________  Metric 3: _______________

6. TEAM CONTRIBUTIONS & RECOGNITION
- [Name]: [Specific contribution and impact]
- [Name]: [Specific contribution and impact]

7. LESSONS LEARNED SUMMARY (TOP 5)
| # | Lesson | Recommendation |
|---|--------|----------------|
| 1 |        |                |
| 2 |        |                |
| 3 |        |                |
| 4 |        |                |
| 5 |        |                |

8. RECOMMENDATIONS FOR FUTURE PROJECTS
- Recommendation 1: _______________
- Recommendation 2: _______________
- Recommendation 3: _______________

9. OPEN ITEMS TRANSFERRED TO BAU
| # | Item | Owner (BAU) | Priority | Notes |
|---|------|-------------|----------|-------|
| 1 |      |             |          |       |
| 2 |      |             |          |       |

SIGN-OFF:
PM: _________________ Date: _______  Sponsor: _________________ Date: _______
```

### Team Celebration and Recognition

**Software team ideas:** Demo day showcase to broader engineering org. Retro + team meal (retro first, then celebrate). Shout-outs in engineering all-hands naming specific people and accomplishments. Written recognition from manager/VP in Slack -- be specific about what was hard and achieved. Project-themed swag. "Ship it" ritual (bell, button, deploy animation).

**General PM team ideas:** Stakeholder thank-you event acknowledging full team including client-side contributors. Written commendations from sponsor to each member's manager. Project retrospective + social gathering. Awards reflecting the project's personality. Team outing chosen by the team. Portfolio showcase at PMO/department meeting, highlighting members by name.

**Recognition principles:**
1. **Be specific.** "Your risk analysis in Phase 2 identified the vendor dependency 3 weeks early, saving $50K and 2 weeks" beats "Great job."
2. **Be timely.** Recognize within 1 week of close, not at annual reviews.
3. **Be inclusive.** All roles and levels, not just the loudest or most senior.
4. **Be proportional.** 3-month project = team lunch. 12-month transformation = meaningful celebration.
5. **Be genuine.** If you did not notice their work, ask peers before writing recognition.

### Closeout Anti-Patterns

| Anti-Pattern                                     | What It Looks Like                                                         | Fix                                                                                   |
|--------------------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| Skipping closeout ("on to the next thing")       | Team rolls off immediately. No retro, handoff, or report.                  | Block 1-2 weeks for closeout in the project plan. Non-negotiable phase.                |
| Incomplete handoffs                              | Ops inherits a service with no runbook, no alerts, no escalation contacts. | Use runbook template. Do not close until ops confirms readiness.                       |
| No benefits tracking                             | Project ships and no one measures whether goals were achieved.             | Create benefits realization plan during planning, not closeout. Assign benefits owner. |
| Zombie projects                                  | "Done" but never formally closed. Resources partially allocated.           | Formal closure announcement + resource release. Unambiguous: closed as of [date].     |
| Knowledge loss                                   | Key member leaves, takes all context. No documentation.                    | Mandatory KT sessions before close. Document the "why," not just the "what."          |
| Skipping recognition                             | Project ends and team gets nothing but a new assignment.                   | Schedule recognition into closeout checklist. 30 minutes, months of impact.            |

---

## Quick Reference: Which Format When

| Scenario                        | Retro Format                | Closeout Activity                       |
|---------------------------------|-----------------------------|-----------------------------------------|
| End of sprint (software)        | Start/Stop/Continue         | Action item tracker update              |
| End of sprint (low morale)      | Mad/Sad/Glad                | Action item tracker + 1:1 check-ins     |
| End of release (software)       | Timeline or 4Ls             | Release notes + runbook handoff         |
| Incident post-mortem (software) | Incident post-mortem format | Action items with follow-up date        |
| Phase gate (general PM)         | Sailboat or 4Ls             | Phase acceptance + lessons capture      |
| End of project (any)            | Timeline (full project)     | Full closeout checklist + closeout report|
| First retro with a new team     | Start/Stop/Continue         | Establish action item tracker           |
| Team in conflict or stress      | Mad/Sad/Glad                | 1:1 interviews + anonymous survey       |

## Workflow Overview

1. **Run retrospectives throughout the project** -- at every sprint, phase gate, release, and incident. Use the format that fits the context.
2. **Capture lessons learned continuously** -- synthesize retro themes into the lessons learned register. Do not wait until the end.
3. **Conduct a formal lessons learned session** -- within 2 weeks of project completion. Use the 60-minute facilitation guide.
4. **Execute the closeout checklist** -- deliverables accepted, documentation archived, finances reconciled, resources released, tools cleaned up, stakeholders notified.
5. **Write the closeout report** -- summarize objectives vs. actuals, schedule and budget performance, top lessons, and recommendations.
6. **Celebrate and recognize the team** -- specific, timely, inclusive recognition for the work done.
7. **Set up benefits tracking** -- ensure someone owns measurement of project outcomes at 3, 6, and 12 months.
