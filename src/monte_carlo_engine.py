"""Monte Carlo simulation engine for probabilistic DCF valuation."""

from __future__ import annotations

from dataclasses import replace
from typing import Dict, Tuple

import numpy as np
import pandas as pd

from dcf_model import DCFInputs, calculate_enterprise_value


DistributionSpec = Dict[str, Tuple[float, ...]]


def sample_assumption(rng: np.random.Generator, spec: Tuple) -> float:
    """Sample one valuation assumption from a distribution specification.

    Supported distribution formats:
    - ("triangular", low, mode, high)
    - ("normal", mean, standard_deviation)
    - ("uniform", low, high)
    - ("fixed", value)
    """

    dist = spec[0]

    if dist == "triangular":
        _, low, mode, high = spec
        return float(rng.triangular(low, mode, high))

    if dist == "normal":
        _, mean, std = spec
        return float(rng.normal(mean, std))

    if dist == "uniform":
        _, low, high = spec
        return float(rng.uniform(low, high))

    if dist == "fixed":
        _, value = spec
        return float(value)

    raise ValueError(f"Unsupported distribution: {dist}")


def run_monte_carlo_dcf(
    base_inputs: DCFInputs,
    distributions: DistributionSpec,
    simulations: int = 10_000,
    seed: int = 42,
) -> pd.DataFrame:
    """Run Monte Carlo DCF simulations and return all simulation results."""

    rng = np.random.default_rng(seed)
    results = []

    for i in range(simulations):
        sampled_values = {
            variable: sample_assumption(rng, spec)
            for variable, spec in distributions.items()
        }

        simulated_inputs = replace(base_inputs, **sampled_values)

        try:
            valuation = calculate_enterprise_value(simulated_inputs)
        except ValueError:
            continue

        results.append(
            {
                "simulation": i + 1,
                **sampled_values,
                **valuation,
            }
        )

    return pd.DataFrame(results)


def summarize_simulation(results: pd.DataFrame, market_price: float | None = None) -> Dict[str, float]:
    """Summarize Monte Carlo valuation results."""

    values = results["fair_value_per_share"]

    summary = {
        "mean_value": float(values.mean()),
        "median_value": float(values.median()),
        "p5_value": float(values.quantile(0.05)),
        "p25_value": float(values.quantile(0.25)),
        "p75_value": float(values.quantile(0.75)),
        "p95_value": float(values.quantile(0.95)),
        "simulations_used": float(len(values)),
    }

    if market_price is not None:
        summary["probability_undervalued"] = float((values > market_price).mean())
        summary["probability_overvalued"] = float((values < market_price).mean())
        summary["median_margin_of_safety"] = float((values.median() / market_price) - 1)

    return summary


if __name__ == "__main__":
    base = DCFInputs(
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

    demo_distributions = {
        "revenue_growth": ("triangular", 0.04, 0.08, 0.12),
        "ebit_margin": ("triangular", 0.10, 0.12, 0.14),
        "wacc": ("normal", 0.1258, 0.01),
        "terminal_growth": ("uniform", 0.03, 0.05),
    }

    df = run_monte_carlo_dcf(base, demo_distributions, simulations=1000)
    print(summarize_simulation(df))
