# Real Estate Analysis Templates

These assets make an analysis reproducible. They are deliberately blank and do
not contain market assumptions, rate quotes, legal conclusions, or tax advice.

| Asset | Use |
|---|---|
| [deal-intake.template.json](deal-intake.template.json) | Structured input for the bundled calculator |
| [deal-intake.schema.json](deal-intake.schema.json) | Field definitions and validation contract |
| [real-estate-underwriting-template.xlsx](real-estate-underwriting-template.xlsx) | Editable single-property underwriting workbook |
| [source-assumption-register.csv](source-assumption-register.csv) | Record material inputs and provenance |
| [financing-comparison.csv](financing-comparison.csv) | Compare actual loan options consistently |
| [risk-register.csv](risk-register.csv) | Track risks, owners, and mitigations |
| [legal-issue-log.csv](legal-issue-log.csv) | Record document findings for counsel review |
| [investment-memo.md](investment-memo.md) | Decision-oriented memo structure |
| [diligence-checklist.md](diligence-checklist.md) | Pre-commitment evidence checklist |

Copy a template into an authorized private working location before filling it
out. Do not commit deal documents, rent rolls, investor lists, tax records,
bank information, credentials, or completed deal-intake files to this public
repository. See [data-handling.md](../skills/real-estate-analyzer/references/data-handling.md).

Rates are decimals: enter `0.06` for 6%, not `6`. The calculator requires a
purchase price, operating expenses, and either annual gross potential income or
both unit count and monthly rent per unit. It reports calculations only from
the values supplied; source and review every input before relying on it.
