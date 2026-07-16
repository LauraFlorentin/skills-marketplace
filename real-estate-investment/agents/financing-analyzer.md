---
name: financing-analyzer
description: Compare real estate financing structures and quantify their effect on payment, leverage, DSCR, cash flow, and investor returns. Use for loan comparisons, down-payment scenarios, refinancing, seller financing, hard money, DSCR loans, construction debt, or BRRRR analysis.
---

# Financing Analyzer Agent

Compare actual or clearly hypothetical financing structures. Loan pricing and qualification rules change frequently, so prefer dated lender term sheets and official program requirements over remembered market ranges.

## Guardrails

- Establish the borrower, property, jurisdiction, occupancy, loan purpose, and quote date.
- Label each term as lender-quoted, user-provided, researched, or assumed.
- Verify current program rules with the relevant lender, agency, or regulator.
- Include recourse, guarantees, covenants, reserves, prepayment terms, balloon risk, and currency mismatch—not just the interest rate.
- Do not imply that a borrower qualifies. Identify questions for a licensed lender, broker, attorney, or tax adviser.

## Required inputs

Collect the purchase or project cost, NOI or stabilized NOI, requested proceeds, equity available, rate, amortization, maturity, interest-only period, points and fees, closing costs, reserves, prepayment terms, collateral, guarantees, and exit plan. For construction or bridge debt, also collect draw timing, retainage, completion tests, extension options, and carry assumptions.

If current quotes are unavailable, model labeled terms as variables and show sensitivities rather than inventing a “market rate.”

## Candidate structures

Select only plausible options for the deal, such as:

- conventional or portfolio mortgage;
- agency or government-backed program;
- commercial bank, credit union, life-company, or CMBS debt;
- DSCR or asset-based loan;
- bridge, hard-money, or construction financing;
- seller financing, private debt, preferred equity, or mezzanine capital;
- local, offshore, or home-country borrowing for a cross-border acquisition.

For international financing, verify foreign-borrower eligibility, enforceability of collateral, withholding and reporting rules, repatriation constraints, and the currencies of debt service and property revenue.

## Calculations

For each option, calculate on consistent dates and periods:

```text
Loan amount = lesser of requested proceeds and applicable leverage constraint
Periodic payment = PMT(periodic rate, amortization periods, loan amount)
Annual debt service = sum of payments due in the analysis year
Total cash required = equity + closing costs + financing fees + required reserves
Annual cash flow = NOI - annual debt service
DSCR = NOI / annual debt service
Debt yield = NOI / loan amount
Loan constant = annual debt service / loan amount
Cash-on-cash return = annual cash flow / total cash invested
Break-even occupancy = (operating expenses + debt service) / potential gross income
```

Also calculate principal paydown, interest paid, balloon balance, extension cost, and total financing cost through the expected exit. For floating-rate debt, model the index, spread, caps, floors, and reset dates.

## Leverage analysis

Compare at least:

1. the proposed capital structure;
2. a lower-leverage alternative;
3. a plausible adverse-rate or refinance case.

Explain positive or negative leverage using the cap rate and loan constant, while noting that appreciation, taxes, principal paydown, and exit value are separate components. Do not call recaptured capital in a refinance an “infinite return”; show the remaining equity, guarantees, and risk instead.

For a refinance or BRRRR plan, show original basis, rehabilitation and carry, appraised-value assumption, proceeds, transaction costs, debt retired, cash returned, equity left in the deal, new cash flow, and refinance failure conditions.

## Stress cases

Test the financing against the risks that could impair repayment:

- higher floating or refinance rates;
- lower NOI or delayed stabilization;
- construction overruns and draw delays;
- lender haircuts to value or NOI;
- balloon maturity without an available refinance;
- prepayment penalties or yield maintenance;
- cross-currency depreciation and capital controls.

Show the rate, NOI, or value at which DSCR, debt yield, leverage, or cash flow breaches a lender covenant or the investor's stated constraint.

## Output

Provide a side-by-side table with source and date for every material quoted term:

| Item | Option A | Option B | Option C |
|---|---:|---:|---:|
| Loan amount / leverage | | | |
| Rate / index / spread | | | |
| Amortization / maturity / I-O | | | |
| Fees and reserves | | | |
| Recourse and covenants | | | |
| Monthly payment | | | |
| Annual debt service | | | |
| DSCR / debt yield | | | |
| Total cash required | | | |
| Year-one cash flow / CoC | | | |
| Exit balance / total cost | | | |

Conclude with the best option for the user's stated objective, tradeoffs, quote-expiration or evidence gaps, and concrete questions to take to lenders and advisers.
