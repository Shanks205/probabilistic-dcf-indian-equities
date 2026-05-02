"""Enrich Screener peer multiples with Yahoo Finance EV and P/B fields.

This script combines:
1. Screener same-source operating/return fields, and
2. Yahoo Finance market data fields for true enterprise value and price-to-book.

This is a pragmatic two-source enrichment layer. It should be described clearly
in the SSRN manuscript as:
- Screener: peer universe + operating / return metrics
- Yahoo Finance: EV, P/B and market-data fields

Usage:
    python scripts/enrich_peer_multiples_with_yahoo_ev_pb.py

Inputs:
    outputs/peer_tables/peer_multiple_refresh_screener_filled.csv
    data/peer_sources/peer_yahoo_ticker_map.csv

Outputs:
    outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
    outputs/peer_tables/peer_multiple_ev_pb_enrichment_status.md
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
SCREENER = ROOT / "outputs" / "peer_tables" / "peer_multiple_refresh_screener_filled.csv"
TICKER_MAP = ROOT / "data" / "peer_sources" / "peer_yahoo_ticker_map.csv"
OUTPUT = ROOT / "outputs" / "peer_tables" / "peer_multiple_refresh_ev_pb_enriched.csv"
STATUS = ROOT / "outputs" / "peer_tables" / "peer_multiple_ev_pb_enrichment_status.md"


def to_inr_cr(value):
    if value is None:
        return "TBD"
    try:
        return round(float(value) / 10_000_000, 2)
    except Exception:
        return "TBD"


def as_float(value):
    try:
        if value in [None, "TBD", ""]:
            return None
        return float(value)
    except Exception:
        return None


def enrich_yahoo(ticker: str) -> dict:
    out = {
        "yahoo_market_cap_inr_cr": "TBD",
        "yahoo_enterprise_value_inr_cr": "TBD",
        "yahoo_price_to_book": "TBD",
        "yahoo_trailing_pe": "TBD",
        "yahoo_forward_pe": "TBD",
        "yahoo_refresh_status": "Pending",
        "yahoo_parse_note": "",
    }
    try:
        info = yf.Ticker(ticker).info or {}
        out["yahoo_market_cap_inr_cr"] = to_inr_cr(info.get("marketCap"))
        out["yahoo_enterprise_value_inr_cr"] = to_inr_cr(info.get("enterpriseValue"))
        out["yahoo_price_to_book"] = round(float(info.get("priceToBook")), 2) if info.get("priceToBook") is not None else "TBD"
        out["yahoo_trailing_pe"] = round(float(info.get("trailingPE")), 2) if info.get("trailingPE") is not None else "TBD"
        out["yahoo_forward_pe"] = round(float(info.get("forwardPE")), 2) if info.get("forwardPE") is not None else "TBD"
        missing = [k for k in ["yahoo_market_cap_inr_cr", "yahoo_enterprise_value_inr_cr", "yahoo_price_to_book"] if out[k] == "TBD"]
        out["yahoo_refresh_status"] = "Fetched; manual review required"
        out["yahoo_parse_note"] = "Missing: " + ", ".join(missing) if missing else "Fetched core Yahoo EV/PB fields"
    except Exception as exc:
        out["yahoo_refresh_status"] = "Failed"
        out["yahoo_parse_note"] = str(exc)
    return out


def main() -> None:
    refresh_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    screener = pd.read_csv(SCREENER)
    tickers = pd.read_csv(TICKER_MAP)
    df = screener.merge(tickers[["peer_company", "yahoo_ticker"]], on="peer_company", how="left")

    yahoo_cache = {}
    rows = []
    for _, row in df.iterrows():
        ticker = row.get("yahoo_ticker")
        row_dict = row.to_dict()
        row_dict["ev_pb_refresh_date"] = refresh_date
        if pd.isna(ticker) or not ticker:
            row_dict.update({
                "yahoo_market_cap_inr_cr": "TBD",
                "yahoo_enterprise_value_inr_cr": "TBD",
                "yahoo_price_to_book": "TBD",
                "yahoo_trailing_pe": "TBD",
                "yahoo_forward_pe": "TBD",
                "yahoo_refresh_status": "Failed",
                "yahoo_parse_note": "Missing Yahoo ticker mapping",
            })
        else:
            if ticker not in yahoo_cache:
                yahoo_cache[ticker] = enrich_yahoo(ticker)
            row_dict.update(yahoo_cache[ticker])

        ev = as_float(row_dict.get("yahoo_enterprise_value_inr_cr"))
        sales = as_float(row_dict.get("revenue_inr_cr"))
        ebitda = as_float(row_dict.get("ebitda_inr_cr"))
        row_dict["true_ev_sales_yahoo_screener"] = round(ev / sales, 2) if ev and sales else "TBD"
        row_dict["true_ev_ebitda_yahoo_screener"] = round(ev / ebitda, 2) if ev and ebitda else "TBD"
        row_dict["final_pb"] = row_dict.get("yahoo_price_to_book", "TBD")
        row_dict["final_ev_source"] = "Yahoo enterpriseValue; reviewed against Screener operating metrics"
        row_dict["final_pb_source"] = "Yahoo priceToBook"
        rows.append(row_dict)

    out_df = pd.DataFrame(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(OUTPUT, index=False)

    status_counts = out_df["yahoo_refresh_status"].value_counts(dropna=False).to_string()
    ev_count = (out_df["yahoo_enterprise_value_inr_cr"] != "TBD").sum()
    pb_count = (out_df["final_pb"] != "TBD").sum()
    true_ev_sales_count = (out_df["true_ev_sales_yahoo_screener"] != "TBD").sum()
    true_ev_ebitda_count = (out_df["true_ev_ebitda_yahoo_screener"] != "TBD").sum()

    status = f"""# Peer Multiple EV/PB Enrichment Status

## Refresh timestamp

```text
{refresh_date}
```

## Inputs

```text
outputs/peer_tables/peer_multiple_refresh_screener_filled.csv
data/peer_sources/peer_yahoo_ticker_map.csv
```

## Output

```text
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
```

## Result summary

```text
{status_counts}
```

## Coverage

```text
Yahoo EV populated: {ev_count} / {len(out_df)}
Yahoo P/B populated: {pb_count} / {len(out_df)}
True EV/Sales calculated: {true_ev_sales_count} / {len(out_df)}
True EV/EBITDA calculated: {true_ev_ebitda_count} / {len(out_df)}
```

## Methodology note

This table intentionally uses two clearly labelled source families:

1. Screener.in for peer universe, revenue, operating profit proxy, PAT, ROE and ROCE.
2. Yahoo Finance for market cap, enterprise value and price-to-book.

This is stronger than the earlier market-cap proxy approach, but final SSRN wording must disclose the mixed-source method and data timestamp.

## Final review requirement

Rows with missing Yahoo EV or P/B should be manually replaced from Screener, Moneycontrol, Bloomberg, Capital IQ, TIKR, Refinitiv or annual-report reconstruction before the final SSRN-ready tag.
"""
    STATUS.write_text(status, encoding="utf-8")
    print(f"Saved {OUTPUT}")
    print(f"Saved {STATUS}")


if __name__ == "__main__":
    main()
