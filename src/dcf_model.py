"""Reusable FCFF DCF valuation functions.

This module contains a simple deterministic FCFF DCF engine. It is intentionally
transparent and beginner-readable so the valuation logic can be audited easily.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class DCFInputs:
    """Inputs for a deterministic FCFF DCF model."""

    starting_revenue: float
    revenue_growth: float
    ebit_margin: float
    tax_rate: float
    depreciation_sales: float
    capex_sales: float
    nwc_sales: float
    wacc: float
    terminal_growth: float
    net_debt: float
    shares_outstanding: float
    forecast_years: int = 5


def build_fcff_forecast(inputs: DCFInputs) -> List[Dict[str, float]]:
    """Build an explicit FCFF forecast.

    All percentages should be passed as decimals. Example: 8% = 0.08.
    """

    rows: List[Dict[str, float]] = []
    revenue = inputs.starting_revenue
    previous_nwc = revenue * inputs.nwc_sales

    for year in range(1, inputs.forecast_years + 1):
        revenue = revenue * (1 + inputs.revenue_growth)
        ebit = revenue * inputs.ebit_margin
        nopat = ebit * (1 - inputs.tax_rate)
        depreciation = revenue * inputs.depreciation_sales
        capex = revenue * inputs.capex_sales
        current_nwc = revenue * inputs.nwc_sales
        change_nwc = current_nwc - previous_nwc
        fcff = nopat + depreciation - capex - change_nwc

        rows.append(
            {
                "year": year,
                "revenue": revenue,
                "ebit": ebit,
                "nopat": nopat,
                "depreciation": depreciation,
                "capex": capex,
                "change_nwc": change_nwc,
                "fcff": fcff,
            }
        )

        previous_nwc = current_nwc

    return rows


def calculate_enterprise_value(inputs: DCFInputs) -> Dict[str, float]:
    """Calculate enterprise value, equity value, and fair value per share."""

    forecast = build_fcff_forecast(inputs)
    pv_fcff = 0.0

    for row in forecast:
        discount_factor = (1 + inputs.wacc) ** row["year"]
        pv_fcff += row["fcff"] / discount_factor

    final_fcff = forecast[-1]["fcff"]

    if inputs.wacc <= inputs.terminal_growth:
        raise ValueError("WACC must be greater than terminal growth.")

    terminal_value = final_fcff * (1 + inputs.terminal_growth) / (
        inputs.wacc - inputs.terminal_growth
    )
    pv_terminal_value = terminal_value / ((1 + inputs.wacc) ** inputs.forecast_years)
    enterprise_value = pv_fcff + pv_terminal_value
    equity_value = enterprise_value - inputs.net_debt
    fair_value_per_share = equity_value / inputs.shares_outstanding

    return {
        "pv_fcff": pv_fcff,
        "terminal_value": terminal_value,
        "pv_terminal_value": pv_terminal_value,
        "enterprise_value": enterprise_value,
        "equity_value": equity_value,
        "fair_value_per_share": fair_value_per_share,
    }


if __name__ == "__main__":
    demo_inputs = DCFInputs(
        starting_revenue=46300,
        revenue_growth=0.08,
        ebit_margin=0.12,
        tax_rate=0.25,
        depreciation_sales=0.025,
        capex_sales=0.035,
        nwc_sales=0.08,
        wacc=0.1258,
        terminal_growth=0.04,
        net_debt=-3000,
        shares_outstanding=20,
    )
    result = calculate_enterprise_value(demo_inputs)
    for key, value in result.items():
        print(f"{key}: {value:,.2f}")
