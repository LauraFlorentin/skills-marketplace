# Skill 11: Data Sources & API Integrations

Structured guidance for pulling real estate market data from external APIs and data platforms. This skill provides endpoints, data fields, code snippets, and best practices for integrating market intelligence into investment analysis.

## When to Use

- User needs comparable property values (comps) for underwriting
- User wants rental rate validation or STR performance data
- User needs demographic/economic data for market analysis
- User wants to automate deal screening across multiple properties
- User asks about Zillow, Redfin, AirDNA, CoStar, Census, or similar platforms
- Any agent (A1-A12) needs market data to validate assumptions

## Platform Reference

### 1. Zillow / Zillow API (Residential Values & Rents)

**What it provides**: Property values (Zestimate), rent estimates (Rent Zestimate), property details, sale history, neighborhood data.

**Access methods**:
- **Zillow Rapid API** (via RapidAPI): Most accessible for developers. Endpoints for property search, Zestimate, comparables.
- **Bridge Interactive API**: MLS-connected data with broader coverage.
- **Web scraping** (Zillow prohibits this in TOS — use official APIs or manual lookup).

```javascript
// Example: Zillow property lookup via RapidAPI
const response = await fetch(
  `https://zillow-com1.p.rapidapi.com/property?zpid=${zpid}`,
  {
    headers: {
      'x-rapidapi-key': process.env.ZILLOW_RAPIDAPI_KEY,
      'x-rapidapi-host': 'zillow-com1.p.rapidapi.com'
    }
  }
);
const data = await response.json();
// Key fields: zestimate, rentZestimate, bedrooms, bathrooms, 
//   livingArea, lotSize, yearBuilt, taxAssessedValue
```

```python
# Python equivalent
import requests

url = "https://zillow-com1.p.rapidapi.com/propertyExtendedSearch"
params = {"location": "Indianapolis, IN", "home_type": "Houses", "minPrice": "100000", "maxPrice": "300000"}
headers = {"x-rapidapi-key": ZILLOW_RAPIDAPI_KEY, "x-rapidapi-host": "zillow-com1.p.rapidapi.com"}

response = requests.get(url, headers=headers, params=params)
properties = response.json().get("props", [])
# Returns: zpid, price, bedrooms, bathrooms, livingArea, zestimate, rentZestimate
```

**Key data fields for investment analysis**:
| Field | Use In Analysis |
|---|---|
| zestimate | Purchase price validation |
| rentZestimate | Rent projection for 1% rule, CoC calc |
| yearBuilt | CapEx reserve estimation (older = higher) |
| taxAssessedValue | Property tax projection |
| livingArea + lotSize | Per-SF analysis, comp matching |
| price history | Market trend direction, days on market |

**Rate limits**: Varies by plan. Free tiers typically 5-20 requests/day. Paid plans $10-$100/month for 500-10,000 requests.

### 2. Redfin (Comps & Market Trends)

**What it provides**: Active and sold comparables, market trends (median price, days on market, price/SF), neighborhood-level data.

**Access methods**:
- **Redfin Data Center**: Free downloadable CSV datasets (market-level trends by zip code, metro, and state — updated weekly).
- **Unofficial API**: Redfin has no official public API, but the data center CSVs are excellent for market-level analysis.

```python
# Download Redfin market trend data (free, no API key needed)
import pandas as pd

# Market-level data by zip code
url = "https://redfin-public-data.s3.us-west-2.amazonaws.com/redfin_market_tracker/zip_code_market_tracker.tsv000.gz"
df = pd.read_csv(url, sep='\t', compression='gzip')

# Filter to target market
target = df[df['region'].str.contains('46201')]  # Indianapolis zip
# Key columns: median_sale_price, median_ppsf, homes_sold, inventory,
#   days_on_market, avg_sale_to_list, median_dom
```

**Best free data source for**: Market trend analysis, identifying hot/cooling markets, price-per-SF benchmarking, days-on-market trends.

### 3. AirDNA (Short-Term Rental Performance)

**What it provides**: STR occupancy rates, ADR, RevPAR, seasonal patterns, revenue projections, comp set data — the gold standard for STR underwriting.

**Access methods**:
- **AirDNA MarketMinder**: Web platform with neighborhood-level data. Paid subscription ($20-$250/month).
- **AirDNA API**: Enterprise access for bulk data. Contact sales for pricing.
- **AirDNA Rentalizer**: Single-property revenue projection tool (some free lookups).

```python
# AirDNA API example (enterprise/paid)
import requests

url = "https://api.airdna.co/v1/market/overview"
params = {
    "access_token": AIRDNA_API_KEY,
    "city": "Tulum",
    "country": "MX",
    "property_type": "entire_place",
    "bedrooms": 2
}
response = requests.get(url, params=params)
market_data = response.json()
# Returns: adr, occupancy_rate, revenue, revpar, active_listings, 
#   demand_score, investability_score, seasonality data
```

**Key data fields for STR analysis**:
| Field | Use In Analysis |
|---|---|
| adr (average daily rate) | Revenue projection, hospitality underwriting |
| occupancy_rate | Revenue projection, stress test base |
| revpar | RevPAR validation (ADR × occupancy) |
| revenue (annual) | Cash flow projection validation |
| active_listings | Supply/competition assessment |
| demand_score | Market demand strength |
| seasonality | Monthly revenue distribution for cash flow timing |

**Alternative free sources for STR data**:
- **Mashvisor**: Limited free lookups, Airbnb + VRBO data
- **AirROI**: Free market reports by neighborhood (Bali, global markets)
- **Hospitable / PriceLabs**: Revenue management tools with market data
- **InsideAirbnb**: Open-source scraped data for select markets

### 4. US Census / American Community Survey (Demographics)

**What it provides**: Population, median household income, employment, education, poverty rates, housing characteristics — essential for market analysis and rent-to-income validation.

**Access methods**:
- **Census API**: Free, no key required for basic access (API key recommended for higher limits).
- **Census Data Explorer**: Web interface for manual lookup.
- **FRED (Federal Reserve Economic Data)**: Economic indicators by metro.

```python
# Census API - median household income by zip code
import requests

api_key = "YOUR_CENSUS_API_KEY"  # Free from api.census.gov
year = "2023"  # Latest ACS 5-year estimates
url = f"https://api.census.gov/data/{year}/acs/acs5"
params = {
    "get": "B19013_001E,B01003_001E,B25064_001E",  
    # median_household_income, total_population, median_gross_rent
    "for": "zip code tabulation area:46201",
    "key": api_key
}
response = requests.get(url, params=params)
data = response.json()
# [['B19013_001E', 'B01003_001E', 'B25064_001E', 'zip'], 
#  ['45000', '25000', '950', '46201']]
# Median income: $45,000, Population: 25,000, Median rent: $950
```

**Key variables for RE investment analysis**:
| Variable Code | Description | Use In Analysis |
|---|---|---|
| B19013_001E | Median household income | Rent-to-income ratio (target <30%) |
| B01003_001E | Total population | Market size, growth trends |
| B25064_001E | Median gross rent | Rent comp validation |
| B25077_001E | Median home value | Purchase price benchmarking |
| B23025_005E | Unemployed population | Employment risk assessment |
| B25002_003E | Vacant housing units | Vacancy rate validation |
| DP04_0047PE | Renter-occupied % | Rental demand indicator |

**Rent-to-income validation formula**:
```python
rent_to_income = (monthly_rent * 12) / median_household_income
# Healthy: <= 0.30 (30%)
# Stressed: 0.30 - 0.40
# Unaffordable: > 0.40 (tenant payment risk)
```

### 5. CoStar / LoopNet (Commercial Real Estate)

**What it provides**: Commercial property comps, cap rates, vacancy rates, tenant data, lease comps, market analytics. The industry standard for commercial RE.

**Access methods**:
- **CoStar**: Enterprise subscription (~$5,000-$15,000/year). Provides the most comprehensive commercial RE data.
- **LoopNet** (owned by CoStar): Free listings and basic property data. Limited analytics without CoStar subscription.
- **Crexi**: Alternative commercial marketplace with some free data.
- **Reonomy**: Property intelligence platform with owner/debt data.

**Since CoStar is expensive, free alternatives for commercial data**:
```python
# FRED API for market-level commercial RE metrics (free)
import requests

fred_key = "YOUR_FRED_API_KEY"  # Free from fred.stlouisfed.org
series = {
    "CPIAUCSL": "CPI (inflation for expense growth)",
    "MORTGAGE30US": "30-year mortgage rate",
    "RRVRUSQ156N": "Rental vacancy rate (national)",
    "MSPUS": "Median sales price of houses (national)"
}

for series_id, description in series.items():
    url = f"https://api.stlouisfed.org/fred/series/observations"
    params = {"series_id": series_id, "api_key": fred_key, 
              "file_type": "json", "sort_order": "desc", "limit": 12}
    resp = requests.get(url, params=params).json()
    print(f"{description}: {resp['observations'][0]['value']}")
```

### 6. Rentometer / Rent Comps

**What it provides**: Rental comparables within a defined radius. Quick rent validation.

```python
# Rentometer API (paid, ~$40-200/month)
import requests

url = "https://www.rentometer.com/api/v1/summary"
params = {
    "api_key": RENTOMETER_KEY,
    "address": "123 Main St, Indianapolis, IN 46201",
    "bedrooms": 3,
    "baths": 2
}
response = requests.get(url, params=params)
rent_data = response.json()
# Returns: mean, median, percentile_25, percentile_75, sample_size
# Use median for conservative underwriting, 25th percentile for stress test
```

### 7. Property Tax Lookups

Property taxes are often the largest operating expense. Verify before underwriting.

```python
# Most counties have free online lookup — no unified API
# General approach: county assessor website scraping or data downloads

# Example: using ATTOM API (paid, comprehensive)
url = "https://api.gateway.attomdata.com/propertyapi/v1.0.0/assessment/detail"
params = {"address1": "123 Main St", "address2": "Indianapolis, IN 46201"}
headers = {"apikey": ATTOM_API_KEY, "accept": "application/json"}
response = requests.get(url, headers=headers, params=params)
# Returns: assessed value, tax amount, tax year, jurisdiction
```

## Data Integration Workflow

When an agent needs market data, follow this sequence:

```
MARKET DATA COLLECTION PROTOCOL

1. IDENTIFY DATA NEEDS
   - What metric? (comps, rents, occupancy, demographics, cap rates)
   - What geography? (address, zip, metro, state)
   - What property type? (residential, commercial, STR)

2. SELECT SOURCE (in priority order)
   Residential values:  Zillow API → Redfin data → manual MLS
   Rental comps:        Rentometer → Zillow Rent Zestimate → AirDNA (STR)
   STR performance:     AirDNA → AirROI (free) → Mashvisor
   Demographics:        Census API (free) → FRED (free)
   Commercial:          CoStar (if available) → LoopNet → Crexi
   Market trends:       Redfin Data Center (free) → FRED → Zillow ZHVI
   Property tax:        County assessor → ATTOM API

3. VALIDATE & CROSS-REFERENCE
   - Never rely on a single data source
   - Cross-reference at least 2 sources for key assumptions
   - Prefer more recent data (< 6 months)
   - Note sample sizes — small samples are unreliable
   
4. APPLY TO ANALYSIS
   - Feed into the appropriate agent's framework
   - Document source and date in assumptions section
   - Use conservative estimates when sources conflict
```

## Batch Deal Screening Script

For users who want to screen multiple properties programmatically:

```python
"""
Batch Deal Screener — screens properties against investment criteria
Requires: Zillow RapidAPI key, Census API key
"""
import requests
import json

def screen_property(address, criteria):
    """Screen a single property against investment criteria"""
    
    # 1. Get property data from Zillow
    zillow_data = get_zillow_data(address)
    if not zillow_data:
        return {"address": address, "status": "NO_DATA"}
    
    price = zillow_data.get("price") or zillow_data.get("zestimate")
    rent = zillow_data.get("rentZestimate")
    
    if not price or not rent:
        return {"address": address, "status": "INCOMPLETE_DATA"}
    
    # 2. Quick screen metrics
    results = {
        "address": address,
        "price": price,
        "monthly_rent": rent,
        "annual_rent": rent * 12,
    }
    
    # 1% Rule
    results["pct_rule"] = rent / price
    results["passes_1pct"] = results["pct_rule"] >= 0.01
    
    # GRM
    results["grm"] = price / (rent * 12)
    results["grm_pass"] = results["grm"] <= criteria.get("max_grm", 8.33)
    
    # 50% Rule estimate
    estimated_noi = (rent * 12) * 0.50
    results["estimated_noi"] = estimated_noi
    results["estimated_cap_rate"] = estimated_noi / price
    
    # Estimated CoC (with financing assumptions)
    down_pct = criteria.get("down_payment", 0.25)
    rate = criteria.get("interest_rate", 0.065)
    term = criteria.get("loan_term", 30)
    
    loan = price * (1 - down_pct)
    monthly_rate = rate / 12
    n_payments = term * 12
    monthly_pmt = loan * (monthly_rate * (1 + monthly_rate)**n_payments) / ((1 + monthly_rate)**n_payments - 1)
    annual_debt_service = monthly_pmt * 12
    
    cash_flow = estimated_noi - annual_debt_service
    total_cash_in = price * down_pct * 1.03  # +3% closing costs
    
    results["annual_cash_flow"] = cash_flow
    results["cash_on_cash"] = cash_flow / total_cash_in if total_cash_in > 0 else 0
    results["dscr"] = estimated_noi / annual_debt_service if annual_debt_service > 0 else 0
    results["monthly_cash_flow_per_door"] = cash_flow / 12
    
    # Pass/Fail
    results["passes_coc"] = results["cash_on_cash"] >= criteria.get("min_coc", 0.08)
    results["passes_dscr"] = results["dscr"] >= criteria.get("min_dscr", 1.25)
    
    results["overall_pass"] = all([
        results["passes_1pct"],
        results["passes_coc"],
        results["passes_dscr"]
    ])
    
    results["status"] = "PASS" if results["overall_pass"] else "FAIL"
    return results


# Usage example:
criteria = {
    "min_coc": 0.08,        # 8% minimum cash-on-cash
    "min_dscr": 1.25,       # 1.25x minimum DSCR
    "max_grm": 8.33,        # 1% rule equivalent
    "down_payment": 0.25,   # 25% down
    "interest_rate": 0.065, # 6.5%
    "loan_term": 30         # 30-year amortization
}

addresses = [
    "123 Main St, Indianapolis, IN 46201",
    "456 Oak Ave, Memphis, TN 38103",
    "789 Elm Dr, Kansas City, MO 64101",
]

results = [screen_property(addr, criteria) for addr in addresses]
passing = [r for r in results if r.get("status") == "PASS"]
print(f"Screened {len(results)} properties, {len(passing)} passed all criteria")
```

## International Data Sources

For Bali, Mexico, and other international markets where US-centric APIs don't apply:

| Market | Free Data Sources | Paid Data Sources |
|---|---|---|
| Bali STR | AirROI, InsideAirbnb, Hospitable | AirDNA, Key Data Dashboard |
| Bali Property | Rumah123.com, Lamudi.co.id | Knight Frank Indonesia, Colliers |
| Mexico/Tulum STR | AirROI, InsideAirbnb | AirDNA, AllTheRooms |
| Mexico Property | Inmuebles24.com, Segundamano | Softec (Mexican RE data) |
| Global | Numbeo (cost of living), Trading Economics (macro) | MSCI Real Estate, JLL Research |
