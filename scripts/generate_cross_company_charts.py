"""Generate cross-company valuation charts for the Monte Carlo DCF project.

This script reads the consolidated Level 2 summary table and creates simple
research-paper-ready charts for GitHub and SSRN drafting.

Usage:
    python scripts/generate_cross_company_charts.py

Outputs:
    outputs/charts/median_fair_value_vs_market_price.png
    outputs/charts/median_margin_of_safety.png
    outputs/charts/valuation_gap_by_company.png
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
SUMMARY_PATH = ROOT / "outputs" / "consolidated" / "cross_company_valuation_summary.csv"
CHART_DIR = ROOT / "outputs" / "charts"


def _to_percent(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace("%", "", regex=False).astype(float)


def load_summary() -> pd.DataFrame:
    df = pd.read_csv(SUMMARY_PATH)
    df["deterministic_value_vs_market_pct"] = _to_percent(df["deterministic_value_vs_market"])
    df["median_margin_of_safety_pct"] = _to_percent(df["median_margin_of_safety"])
    df["probability_value_above_market_pct"] = _to_percent(df["probability_value_above_market"])
    return df


def plot_median_fair_value_vs_market_price(df: pd.DataFrame) -> None:
    plot_df = df[["company", "monte_carlo_median_fair_value", "market_price_used"]].copy()
    plot_df = plot_df.sort_values("market_price_used", ascending=False)

    ax = plot_df.plot(
        x="company",
        y=["monte_carlo_median_fair_value", "market_price_used"],
        kind="bar",
        figsize=(14, 7),
    )
    ax.set_title("Monte Carlo Median Fair Value vs Market Price")
    ax.set_xlabel("Company")
    ax.set_ylabel("INR per share")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "median_fair_value_vs_market_price.png", dpi=200)
    plt.close()


def plot_margin_of_safety(df: pd.DataFrame) -> None:
    plot_df = df[["company", "median_margin_of_safety_pct"]].copy()
    plot_df = plot_df.sort_values("median_margin_of_safety_pct", ascending=True)

    ax = plot_df.plot(
        x="company",
        y="median_margin_of_safety_pct",
        kind="bar",
        figsize=(14, 7),
        legend=False,
    )
    ax.set_title("Median Margin of Safety by Company")
    ax.set_xlabel("Company")
    ax.set_ylabel("Median margin of safety (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "median_margin_of_safety.png", dpi=200)
    plt.close()


def plot_valuation_gap(df: pd.DataFrame) -> None:
    plot_df = df[["company", "deterministic_value_vs_market_pct"]].copy()
    plot_df = plot_df.sort_values("deterministic_value_vs_market_pct", ascending=True)

    ax = plot_df.plot(
        x="company",
        y="deterministic_value_vs_market_pct",
        kind="bar",
        figsize=(14, 7),
        legend=False,
    )
    ax.set_title("Deterministic DCF Value vs Market Price")
    ax.set_xlabel("Company")
    ax.set_ylabel("DCF value vs market price (%)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "valuation_gap_by_company.png", dpi=200)
    plt.close()


def main() -> None:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    df = load_summary()
    plot_median_fair_value_vs_market_price(df)
    plot_margin_of_safety(df)
    plot_valuation_gap(df)
    print(f"Charts saved to: {CHART_DIR}")


if __name__ == "__main__":
    main()
