"""Generate Hero MotoCorp Level 2 draft DCF, Monte Carlo, and chart outputs.

This script is designed for reproducibility. It uses the current Level 2 draft
public-source input table and produces deterministic DCF, Monte Carlo summary,
and charts.

Run from repository root:

    python scripts/generate_hero_motocorp_level2_outputs.py

Important: this is not investment advice. Outputs depend on assumptions.
"""

from __future__ import annotations

from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT / "src"))

from dcf_model import DCFInputs, calculate_enterprise_value
from monte_carlo_engine import run_monte_carlo_dcf, summarize_simulation


OUTPUT_DIR = PROJECT_ROOT / "outputs" / "charts" / "hero_motocorp"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_inputs() -> DCFInputs:
    """Return final Level 2 draft Hero MotoCorp DCF inputs."""

    return DCFInputs(
        starting_revenue=40923.4,
        revenue_growth=0.08,
        ebit_margin=0.15065537076586988,
        tax_rate=0.26253210551507017,
        depreciation_sales=0.0201495965633354,
        capex_sales=0.02020457733228422,
        nwc_sales=0.08,
        wacc=0.1246,
        terminal_growth=0.04,
        net_debt=-10076.0,
        shares_outstanding=20.009,
        forecast_years=5,
    )


def main() -> None:
    market_price = 5111.55
    inputs = build_inputs()

    dcf = calculate_enterprise_value(inputs)
    print("Hero MotoCorp Level 2 Draft Deterministic DCF")
    for key, value in dcf.items():
        print(f"{key}: {value:,.2f}")

    distributions = {
        "revenue_growth": ("triangular", 0.04, 0.08, 0.12),
        "ebit_margin": ("triangular", 0.13, inputs.ebit_margin, 0.17),
        "tax_rate": ("triangular", 0.24, inputs.tax_rate, 0.28),
        "depreciation_sales": ("triangular", 0.017, inputs.depreciation_sales, 0.024),
        "capex_sales": ("triangular", 0.016, inputs.capex_sales, 0.035),
        "nwc_sales": ("triangular", 0.06, 0.08, 0.10),
        "wacc": ("normal", 0.1246, 0.01),
        "terminal_growth": ("uniform", 0.03, 0.05),
    }

    simulation = run_monte_carlo_dcf(
        base_inputs=inputs,
        distributions=distributions,
        simulations=10_000,
        seed=42,
    )
    summary = summarize_simulation(simulation, market_price=market_price)
    print("\nHero MotoCorp Level 2 Draft Monte Carlo Summary")
    for key, value in summary.items():
        print(f"{key}: {value:,.2f}")

    # Save machine-readable outputs
    output_csv = PROJECT_ROOT / "companies" / "hero_motocorp" / "generated_monte_carlo_values.csv"
    simulation[["simulation", "fair_value_per_share"]].to_csv(output_csv, index=False)

    # Chart 1: operating baseline
    years = ["FY2024", "FY2025"]
    revenue = [37788.6, 40923.4]
    operating_profit = [6204.17, 6989.92]
    plt.figure(figsize=(8, 5))
    plt.plot(years, revenue, marker="o", label="Revenue / Net Sales")
    plt.plot(years, operating_profit, marker="o", label="Profit before finance cost & depreciation")
    plt.title("Hero MotoCorp: FY2024-FY2025 Operating Baseline")
    plt.ylabel("INR crore")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "hero_operating_baseline.png", dpi=200)
    plt.close()

    # Chart 2: Monte Carlo distribution
    plt.figure(figsize=(8, 5))
    plt.hist(simulation["fair_value_per_share"], bins=50)
    plt.axvline(summary["median_value"], linestyle="--", label="Median simulated value")
    plt.axvline(market_price, linestyle=":", label="Market price used")
    plt.title("Hero MotoCorp Monte Carlo Fair Value Distribution")
    plt.xlabel("Fair value per share (INR)")
    plt.ylabel("Simulation count")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "hero_monte_carlo_distribution.png", dpi=200)
    plt.close()

    # Chart 3: percentile band
    labels = ["5th", "25th", "Median", "75th", "95th", "Market"]
    values = [
        summary["p5_value"],
        summary["p25_value"],
        summary["median_value"],
        summary["p75_value"],
        summary["p95_value"],
        market_price,
    ]
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Hero MotoCorp Valuation Percentile Band")
    plt.ylabel("INR per share")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "hero_valuation_percentiles.png", dpi=200)
    plt.close()

    print(f"\nGenerated chart outputs in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
