"""Refresh common-date market data for the 12-company sample.

This script is the next SSRN verification layer after annual-report mapping.
It pulls Yahoo Finance data for the tickers listed in the market-data refresh
template and writes a populated CSV with a single refresh timestamp.

Important: market data should be manually reviewed before the SSRN paper is
marked ready. This script creates a first-pass refresh, not a final audit.

Usage:
    python scripts/refresh_market_data.py

Outputs:
    outputs/market_data/final_market_data_refresh_filled.csv
    outputs/market_data/market_data_refresh_status.md
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "outputs" / "market_data" / "final_market_data_refresh_template.csv"
OUTPUT = ROOT / "outputs" / "market_data" / "final_market_data_refresh_filled.csv"
STATUS = ROOT / "outputs" / "market_data" / "market_data_refresh_status.md"

RISK_FREE_RATE_PLACEHOLDER = "TBD - update with India 10Y G-sec on same data date"


def safe_get(info: dict, *keys: str):
    for key in keys:
        value = info.get(key)
        if value is not None:
            return value
    return None


def to_inr_cr(value):
    if value is None:
        return "TBD"
    try:
        return round(float(value) / 10_000_000, 2)
    except Exception:
        return "TBD"


def refresh_row(row: pd.Series, refresh_date: str) -> dict:
    ticker = row["ticker"]
    result = row.to_dict()
    result["market_data_date"] = refresh_date

    try:
        yf_ticker = yf.Ticker(ticker)
        info = yf_ticker.info or {}
        hist = yf_ticker.history(period="5d")

        if not hist.empty:
            result["share_price"] = round(float(hist["Close"].dropna().iloc[-1]), 2)
            result["source_price"] = "Yahoo Finance last available close"
        else:
            result["share_price"] = "TBD"
            result["source_price"] = "No recent price returned"

        market_cap = safe_get(info, "marketCap")
        enterprise_value = safe_get(info, "enterpriseValue")
        shares_outstanding = safe_get(info, "sharesOutstanding", "impliedSharesOutstanding")
        beta = safe_get(info, "beta")

        result["market_cap_inr_cr"] = to_inr_cr(market_cap)
        result["enterprise_value_inr_cr"] = to_inr_cr(enterprise_value)
        result["shares_outstanding_cr"] = round(float(shares_outstanding) / 10_000_000, 4) if shares_outstanding else "TBD"
        result["beta"] = round(float(beta), 3) if beta is not None else "TBD"
        result["risk_free_rate"] = RISK_FREE_RATE_PLACEHOLDER
        result["source_market_cap"] = "Yahoo Finance marketCap"
        result["source_ev"] = "Yahoo Finance enterpriseValue"
        result["source_beta"] = "Yahoo Finance beta"
        result["source_risk_free_rate"] = "Manual India 10Y G-sec input required"
        result["refresh_status"] = "Auto-filled; manual review required"
        result["next_action"] = "Review Yahoo data, add India 10Y G-sec, and lock common data date"
    except Exception as exc:
        result["refresh_status"] = "Failed"
        result["next_action"] = f"Manual refresh required: {exc}"

    return result


def main() -> None:
    refresh_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    df = pd.read_csv(TEMPLATE)
    refreshed = pd.DataFrame([refresh_row(row, refresh_date) for _, row in df.iterrows()])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    refreshed.to_csv(OUTPUT, index=False)

    completed = (refreshed["refresh_status"] == "Auto-filled; manual review required").sum()
    failed = (refreshed["refresh_status"] == "Failed").sum()

    status = f"""# Market Data Refresh Status

## Purpose

This file records the first automated market-data refresh for the SSRN verification layer.

## Refresh Timestamp

```text
{refresh_date}
```

## Output File

```text
outputs/market_data/final_market_data_refresh_filled.csv
```

## Result Summary

```text
Companies auto-filled: {completed}
Companies failed: {failed}
```

## Important Manual Review Requirements

The output is not final SSRN evidence yet. Before final use:

1. Confirm all share prices, market caps, enterprise values and beta values.
2. Add India 10-year government bond yield using the same data date.
3. Decide whether Yahoo Finance enterprise value should be used or whether EV should be recalculated manually from annual-report cash/debt values.
4. Lock one common market-data date for all companies.
5. Update the DCF and Monte Carlo files if market price, share count, net cash/debt or beta changes materially.

## Research Boundary

This is a research automation helper, not investment advice or a buy/sell recommendation.
"""
    STATUS.write_text(status, encoding="utf-8")
    print(f"Saved market data to {OUTPUT}")
    print(f"Saved status report to {STATUS}")


if __name__ == "__main__":
    main()
