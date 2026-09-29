"""Synthetic regression checks for the bundled underwriting calculator."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PLUGIN_ROOT / "scripts"))

import real_estate_calculations as calculator  # noqa: E402


class RealEstateCalculationTests(unittest.TestCase):
    def fixture(self, name: str) -> dict[str, object]:
        path = Path(__file__).parent / "fixtures" / name
        return json.loads(path.read_text(encoding="utf-8"))

    def test_stabilized_multifamily_outputs_are_reproducible(self) -> None:
        output = calculator.calculate(self.fixture("stabilized-multifamily.json"))
        results = output["results"]
        self.assertAlmostEqual(results["annual_gross_potential_income"], 180000)
        self.assertAlmostEqual(results["effective_gross_income"], 177000)
        self.assertAlmostEqual(results["noi"], 97000)
        self.assertAlmostEqual(results["cap_rate"], 0.097)
        self.assertAlmostEqual(results["monthly_debt_service"], 3897.07841349292, places=6)
        self.assertAlmostEqual(results["annual_debt_service"], 46764.94096191504, places=6)
        self.assertAlmostEqual(results["dscr"], 2.0742034097508206, places=6)
        self.assertAlmostEqual(results["cash_invested"], 385000)
        self.assertAlmostEqual(results["cash_on_cash_return"], 0.13048067282619472, places=6)
        self.assertIn("levered_irr", results)
        self.assertGreater(results["levered_irr"], 0)

    def test_zero_rate_payment_is_principal_divided_by_periods(self) -> None:
        self.assertAlmostEqual(calculator.monthly_payment(120000, 0, 10), 1000)
        self.assertAlmostEqual(calculator.remaining_balance(120000, 0, 10, 24), 96000)

    def test_irr_matches_known_two_period_cash_flow(self) -> None:
        self.assertAlmostEqual(calculator.irr([-100, 60, 60]), 0.1306623863, places=8)

    def test_invalid_rate_is_rejected_instead_of_coerced(self) -> None:
        deal = self.fixture("stabilized-multifamily.json")
        deal["property"]["vacancy_and_collection_loss_rate"] = 5  # type: ignore[index]
        with self.assertRaisesRegex(calculator.InputError, "decimal less than 1"):
            calculator.calculate(deal)

    def test_partial_exit_assumptions_are_rejected(self) -> None:
        deal = self.fixture("stabilized-multifamily.json")
        del deal["investment"]["exit_cap_rate"]  # type: ignore[index]
        with self.assertRaisesRegex(calculator.InputError, "both required"):
            calculator.calculate(deal)


if __name__ == "__main__":
    unittest.main()
