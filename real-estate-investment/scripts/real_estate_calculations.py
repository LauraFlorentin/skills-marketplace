#!/usr/bin/env python3
"""Calculate a transparent, single-property real-estate underwriting summary.

This tool intentionally does not source market data, infer missing inputs, or
make an investment recommendation. It turns a completed deal-intake JSON file
into reproducible calculations that an analyst can trace to stated inputs.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any


class InputError(ValueError):
    """Raised when a deal-intake input is absent or unsuitable for calculation."""


def _mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise InputError(f"{label} must be an object")
    return value


def _number(
    values: dict[str, Any],
    key: str,
    label: str,
    *,
    required: bool = False,
    default: float | None = None,
    minimum: float | None = None,
) -> float | None:
    value = values.get(key)
    if value is None:
        if required:
            raise InputError(f"{label} is required")
        return default
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{label} must be a number")
    result = float(value)
    if not math.isfinite(result):
        raise InputError(f"{label} must be finite")
    if minimum is not None and result < minimum:
        raise InputError(f"{label} must be at least {minimum:g}")
    return result


def _rate(
    values: dict[str, Any], key: str, label: str, *, default: float = 0.0
) -> float:
    result = _number(values, key, label, default=default, minimum=0.0)
    assert result is not None
    if result >= 1:
        raise InputError(f"{label} must be expressed as a decimal less than 1")
    return result


def monthly_payment(principal: float, annual_interest_rate: float, amortization_years: float) -> float:
    """Return the level monthly payment for a fully amortizing fixed-rate loan."""
    if principal < 0:
        raise InputError("loan amount must not be negative")
    if amortization_years <= 0:
        raise InputError("amortization years must be greater than zero")
    if principal == 0:
        return 0.0

    periods = amortization_years * 12
    monthly_rate = annual_interest_rate / 12
    if monthly_rate == 0:
        return principal / periods
    factor = (1 + monthly_rate) ** periods
    return principal * monthly_rate * factor / (factor - 1)


def remaining_balance(
    principal: float,
    annual_interest_rate: float,
    amortization_years: float,
    months_elapsed: int,
) -> float:
    """Return remaining principal after a number of scheduled monthly payments."""
    if months_elapsed < 0:
        raise InputError("months elapsed must not be negative")
    if principal == 0:
        return 0.0
    total_periods = int(round(amortization_years * 12))
    if months_elapsed >= total_periods:
        return 0.0

    payment = monthly_payment(principal, annual_interest_rate, amortization_years)
    monthly_rate = annual_interest_rate / 12
    if monthly_rate == 0:
        return max(0.0, principal - payment * months_elapsed)
    factor = (1 + monthly_rate) ** months_elapsed
    return max(0.0, principal * factor - payment * (factor - 1) / monthly_rate)


def npv(rate: float, cash_flows: list[float]) -> float:
    if rate <= -1:
        raise InputError("discount rate must be greater than -1")
    return sum(cash_flow / ((1 + rate) ** period) for period, cash_flow in enumerate(cash_flows))


def irr(cash_flows: list[float]) -> float | None:
    """Return a periodic IRR by bisection, or None when no sign-changing IRR exists."""
    if not cash_flows or not any(value < 0 for value in cash_flows) or not any(value > 0 for value in cash_flows):
        return None

    low, high = -0.9999, 1.0
    low_value, high_value = npv(low, cash_flows), npv(high, cash_flows)
    while low_value * high_value > 0 and high < 1_000_000:
        high *= 2
        high_value = npv(high, cash_flows)
    if low_value * high_value > 0:
        return None

    for _ in range(200):
        middle = (low + high) / 2
        middle_value = npv(middle, cash_flows)
        if abs(middle_value) < 1e-10:
            return middle
        if low_value * middle_value <= 0:
            high, high_value = middle, middle_value
        else:
            low, low_value = middle, middle_value
    return (low + high) / 2


def calculate(deal: dict[str, Any]) -> dict[str, Any]:
    """Return a reproducible underwriting summary from a completed intake object."""
    property_data = _mapping(deal.get("property"), "property")
    financing = _mapping(deal.get("financing", {}), "financing")
    investment = _mapping(deal.get("investment", {}), "investment")

    purchase_price = _number(
        property_data, "purchase_price", "property.purchase_price", required=True, minimum=0.0
    )
    assert purchase_price is not None
    annual_gross_income = _number(
        property_data, "annual_gross_potential_income", "property.annual_gross_potential_income"
    )
    if annual_gross_income is None:
        unit_count = _number(property_data, "unit_count", "property.unit_count", required=True, minimum=0.0)
        monthly_rent = _number(
            property_data,
            "monthly_rent_per_unit",
            "property.monthly_rent_per_unit",
            required=True,
            minimum=0.0,
        )
        assert unit_count is not None and monthly_rent is not None
        annual_gross_income = unit_count * monthly_rent * 12
    if annual_gross_income < 0:
        raise InputError("property.annual_gross_potential_income must not be negative")

    annual_other_income = _number(
        property_data, "annual_other_income", "property.annual_other_income", default=0.0, minimum=0.0
    )
    annual_operating_expenses = _number(
        property_data,
        "annual_operating_expenses",
        "property.annual_operating_expenses",
        required=True,
        minimum=0.0,
    )
    annual_capital_reserves = _number(
        property_data,
        "annual_capital_reserves",
        "property.annual_capital_reserves",
        default=0.0,
        minimum=0.0,
    )
    vacancy_rate = _rate(property_data, "vacancy_and_collection_loss_rate", "property.vacancy_and_collection_loss_rate")
    assert annual_other_income is not None
    assert annual_operating_expenses is not None
    assert annual_capital_reserves is not None

    loan_amount = _number(financing, "loan_amount", "financing.loan_amount", default=0.0, minimum=0.0)
    origination_fees = _number(
        financing, "origination_fees", "financing.origination_fees", default=0.0, minimum=0.0
    )
    assert loan_amount is not None and origination_fees is not None
    annual_interest_rate = 0.0
    amortization_years = 0.0
    if loan_amount > 0:
        annual_interest_rate = _rate(
            financing, "annual_interest_rate", "financing.annual_interest_rate"
        )
        amortization_years = _number(
            financing,
            "amortization_years",
            "financing.amortization_years",
            required=True,
            minimum=1.0 / 12,
        ) or 0.0

    acquisition_costs = _number(
        investment, "acquisition_costs", "investment.acquisition_costs", default=0.0, minimum=0.0
    )
    renovation_capex = _number(
        investment, "renovation_capex", "investment.renovation_capex", default=0.0, minimum=0.0
    )
    initial_reserves = _number(
        investment, "initial_reserves", "investment.initial_reserves", default=0.0, minimum=0.0
    )
    assert acquisition_costs is not None
    assert renovation_capex is not None
    assert initial_reserves is not None

    effective_gross_income = annual_gross_income * (1 - vacancy_rate) + annual_other_income
    noi = effective_gross_income - annual_operating_expenses - annual_capital_reserves
    monthly_debt_service = monthly_payment(loan_amount, annual_interest_rate, amortization_years) if loan_amount else 0.0
    annual_debt_service = monthly_debt_service * 12
    total_project_cost = purchase_price + acquisition_costs + renovation_capex + initial_reserves + origination_fees
    cash_invested = total_project_cost - loan_amount
    annual_cash_flow = noi - annual_debt_service
    potential_income = annual_gross_income + annual_other_income

    results: dict[str, Any] = {
        "annual_gross_potential_income": annual_gross_income,
        "effective_gross_income": effective_gross_income,
        "noi": noi,
        "cap_rate": noi / purchase_price if purchase_price else None,
        "monthly_debt_service": monthly_debt_service,
        "annual_debt_service": annual_debt_service,
        "dscr": noi / annual_debt_service if annual_debt_service else None,
        "debt_yield": noi / loan_amount if loan_amount else None,
        "total_project_cost": total_project_cost,
        "cash_invested": cash_invested,
        "annual_cash_flow": annual_cash_flow,
        "cash_on_cash_return": annual_cash_flow / cash_invested if cash_invested > 0 else None,
        "break_even_income_ratio": (
            (annual_operating_expenses + annual_capital_reserves + annual_debt_service) / potential_income
            if potential_income else None
        ),
    }

    hold_years = _number(investment, "hold_years", "investment.hold_years", minimum=1.0)
    exit_cap_rate = _number(investment, "exit_cap_rate", "investment.exit_cap_rate", minimum=0.0)
    if hold_years is not None or exit_cap_rate is not None:
        if hold_years is None or exit_cap_rate is None or exit_cap_rate == 0:
            raise InputError("investment.hold_years and a positive investment.exit_cap_rate are both required for exit analysis")
        if not float(hold_years).is_integer():
            raise InputError("investment.hold_years must be a whole number for annual cash flows")
        hold_years_int = int(hold_years)
        annual_noi_growth_rate = _rate(
            investment, "annual_noi_growth_rate", "investment.annual_noi_growth_rate"
        )
        sale_cost_rate = _rate(investment, "sale_cost_rate", "investment.sale_cost_rate")
        forward_noi = noi * ((1 + annual_noi_growth_rate) ** (hold_years_int + 1))
        gross_sale_value = forward_noi / exit_cap_rate
        sale_costs = gross_sale_value * sale_cost_rate
        loan_balance_at_exit = remaining_balance(
            loan_amount, annual_interest_rate, amortization_years, hold_years_int * 12
        ) if loan_amount else 0.0
        net_sale_proceeds = gross_sale_value - sale_costs - loan_balance_at_exit
        annual_cash_flows = [
            noi * ((1 + annual_noi_growth_rate) ** year) - annual_debt_service
            for year in range(1, hold_years_int + 1)
        ]
        annual_cash_flows[-1] += net_sale_proceeds
        cash_flows = [-cash_invested, *annual_cash_flows]
        total_distributions = sum(annual_cash_flows)
        results.update(
            {
                "hold_years": hold_years_int,
                "forward_noi_at_exit": forward_noi,
                "gross_sale_value": gross_sale_value,
                "sale_costs": sale_costs,
                "loan_balance_at_exit": loan_balance_at_exit,
                "net_sale_proceeds_after_debt": net_sale_proceeds,
                "equity_multiple": total_distributions / cash_invested if cash_invested > 0 else None,
                "levered_irr": irr(cash_flows),
                "annual_investor_cash_flows": cash_flows,
            }
        )

    return {
        "tool": "real-estate-investment/real_estate_calculations",
        "tool_version": "1.0.0",
        "results": results,
        "limitations": [
            "Calculations use only supplied inputs; this tool does not validate market data, legal terms, tax treatment, or borrower eligibility.",
            "Review the intake, source dates, units, and assumptions before using results in an investment decision.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Completed deal-intake JSON file")
    args = parser.parse_args()

    try:
        deal = json.loads(args.input.read_text(encoding="utf-8"))
        output = calculate(_mapping(deal, "deal intake"))
    except (OSError, json.JSONDecodeError, InputError) as exc:
        print(f"Input error: {exc}", file=sys.stderr)
        return 2

    json.dump(output, sys.stdout, indent=2, sort_keys=True)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
