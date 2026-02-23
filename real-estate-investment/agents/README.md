# Agents

This directory contains the orchestrator and specialist agent definitions for the Real Estate Investment Analyzer.

## Orchestrator

The [orchestrator](./orchestrator.md) classifies deals and routes them to the right specialist agents.

## Specialist Agents

Each agent has its own folder with a `reference.md` knowledge base:

| Agent | Folder | Role |
| :--- | :--- | :--- |
| A2 Deal Screener | [`deal-screener/`](./deal-screener/) | Quick pass/fail on rules of thumb |
| A3 Property Underwriter | [`property-underwriter/`](./property-underwriter/) | Full financial analysis |
| A4 Pro Forma Builder | [`pro-forma-builder/`](./pro-forma-builder/) | Multi-year projections |
| A5 Financing Analyzer | [`financing-analyzer/`](./financing-analyzer/) | Loan comparison & leverage |
| A6 Tax Strategist | [`tax-strategist/`](./tax-strategist/) | Depreciation, 1031, cost seg |
| A7 Stress Tester | [`stress-tester/`](./stress-tester/) | Scenario analysis & resilience |
| A8 Syndication Analyzer | [`syndication-analyzer/`](./syndication-analyzer/) | SPV/fund structure & fee analysis |
| A9 Int'l Risk Assessor | [`international-risk-assessor/`](./international-risk-assessor/) | Cross-border & jurisdiction risk |
| A10 Hospitality Underwriter | [`hospitality-underwriter/`](./hospitality-underwriter/) | Hotel/resort specific metrics |
| A11 Legal Reviewer | [`legal-reviewer/`](./legal-reviewer/) | Document red flags |
| — Data Sources | [`data-sources/`](./data-sources/) | API lookups, batch screening, market data |
