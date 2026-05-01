"""Run a first-pass Hero MotoCorp probabilistic DCF demo.

This script uses placeholder assumptions and is intended only to test the model
structure. The assumptions must be replaced with verified financial statement
and market data before any research conclusion is drawn.
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from dcf_model import DCFInputs, calculate_enterprise_value
from monte_carlo_engine import run_monte_carlo_dcf, summarize_simulation


def main() -> None:
    base_inputs = DCFInputs(
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
        forecast_years=5,
    )

    deterministic_result = calculate_enterprise_value(base_inputs)
    print("Hero MotoCorp deterministic DCF demo")
    print("------------------------------------")
    for key, value in deterministic_result.items():
        print(f"{key}: {value:,.2f}")

    distributions = {
        "revenue_growth": ("triangular", 0.04, 0.08, 0.12),
        "ebit_margin": ("triangular", 0.10, 0.12, 0.14),
        "tax_rate": ("triangular", 0.23, 0.25, 0.27),
        "depreciation_sales": ("triangular", 0.020, 0.025, 0.030),
        "capex_sales": ("triangular", 0.025, 0.035, 0.045),
        "nwc_sales": ("triangular", 0.06, 0.08, 0.10),
        "wacc": ("normal", 0.1258, 0.01),
        "terminal_growth": ("uniform", 0.03, 0.05),
    }

    simulation_results = run_monte_carlo_dcf(
        base_inputs=base_inputs,
        distributions=distributions,
        simulations=10_000,
        seed=42,
    )

    summary = summarize_simulation(simulation_results)
    print("\nHero MotoCorp Monte Carlo DCF demo")
    print("----------------------------------")
    for key, value in summary.items():
        print(f"{key}: {value:,.2f}")


if __name__ == "__main__":
    main()
