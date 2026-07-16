# Real Estate Data Sources

Use this reference when market evidence or batch data is needed. Provider coverage, products, endpoints, prices, licensing, and terms change; verify current documentation before relying on an integration.

## Contents

- [Source selection](#source-selection)
- [Evidence record](#evidence-record)
- [Common source categories](#common-source-categories)
- [Integration rules](#integration-rules)
- [Batch screening](#batch-screening)
- [Quality checks](#quality-checks)

## Source selection

Prefer the most authoritative source that measures the needed fact:

1. executed deal documents, property records, rent rolls, leases, invoices, bank or ledger records;
2. official registries, assessors, permit offices, census or statistical agencies, central banks, tax authorities, and regulators;
3. licensed MLS, exchange, lender, hotel, or commercial-property data with documented methodology;
4. attributable third-party research and platform data;
5. advertisements, broker opinions, and user-generated listings as leads requiring corroboration.

Match geography, asset type, quality, unit, currency, and observation period. A national average or advertised rate is rarely a defensible property-level input.

## Evidence record

Store the following with every material observation:

```text
metric: effective rent
value: ...
unit: currency / area / month
geography and asset: ...
observation period: ...
source: publisher, dataset, document, or endpoint
source date: ...
retrieved: ...
sample and method: ...
adjustments: ...
confidence and limitations: ...
```

Preserve raw observations separately from cleaned inputs and model assumptions.

## Common source categories

| Need | Preferred evidence | Common limitation |
|---|---|---|
| Ownership, liens, transfers | Land registry, recorder, assessor | Delays, incomplete beneficial ownership |
| Zoning and permits | Municipal or regional authority | Parcel overlays and approvals can differ |
| Residential sales and rent | MLS, recorded sales, executed leases | Access restrictions and listing bias |
| Commercial rent and cap rates | Executed leases and sales, licensed datasets | Sparse, confidential, or modeled observations |
| Short-term rental | Operator statements, booking records, licensed STR data | Blocked nights and active-listing bias |
| Hospitality performance | Property accounts and attributable comp-set reports | Confidentiality and changing comp sets |
| Demographics and economy | Official statistical agencies | Publication lag and geographic mismatch |
| Rates and financing | Dated lender quote, agency or regulator | Borrower and property eligibility varies |
| Taxes and law | Tax authority, statute, regulation, treaty | Effective dates and taxpayer facts matter |
| Hazards and environment | Government maps, insurer, technical reports | Map resolution and future-risk uncertainty |

Examples of vendors or platforms are discovery aids, not endorsements. Check their current licensing, methodology, export rights, attribution requirements, and permitted uses.

## Integration rules

- Use documented APIs or licensed exports. Do not scrape a service that prohibits it.
- Keep credentials in environment variables or an approved secret store; never write them into the repository, prompts, logs, or output artifacts.
- Send the minimum data necessary and avoid uploading personal, tenant, financial-account, or confidential deal data without authorization.
- Pin and document API versions where supported. Handle timeouts, pagination, quotas, partial responses, schema changes, and retries.
- Cache only when licensing permits, record retrieval time, and define an expiration appropriate to the metric.
- Validate HTTP status, response shape, types, units, currency, time zone, and missing values before using data.

```python
import os
import requests

api_key = os.environ["REAL_ESTATE_DATA_API_KEY"]
response = requests.get(
    "https://api.example.com/v1/observations",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"market": "example", "metric": "effective_rent"},
    timeout=20,
)
response.raise_for_status()
payload = response.json()
if not isinstance(payload.get("observations"), list):
    raise ValueError("Unexpected response schema")
```

Replace the example URL with a provider's current documented endpoint.

## Batch screening

For a property list:

1. validate required columns and unique property identifiers;
2. standardize addresses, currencies, areas, dates, and units;
3. retain source and timestamp per row;
4. calculate only screening metrics supported by available data;
5. flag missing or stale inputs instead of silently imputing them;
6. rank for follow-up, then manually verify shortlisted deals.

Never interpret a batch-screening rank as investment approval.

## Quality checks

- Compare at least two independent sources for decision-critical market inputs when practical.
- Inspect sample size, dispersion, missingness, revisions, and outliers.
- Detect duplicate listings, repeated sales, non-arm's-length transfers, concessions, and mixed property classes.
- Reconcile market evidence with property documents and explain differences.
- Preserve reproducible query parameters and calculation code.
- State when evidence is unavailable, inaccessible, stale, or too weak for the requested conclusion.
