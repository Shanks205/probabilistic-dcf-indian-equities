"""Fetch peer valuation multiples from Screener.in.

This script builds a same-source peer multiple table from Screener.in pages.
It is intentionally conservative: if a field cannot be parsed, it is left as
TBD rather than estimated.

Important compliance note:
- Use this script only for personal research and with reasonable request pacing.
- Screener pages can change structure or block automated access.
- Final SSRN use should cite Screener as the source and include the refresh date.

Usage:
    python scripts/fetch_screener_peer_multiples.py

Input:
    data/peer_sources/screener_peer_universe.csv

Output:
    outputs/peer_tables/peer_multiple_refresh_screener_filled.csv
    outputs/peer_tables/peer_multiple_screener_fetch_status.md
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re
import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data" / "peer_sources" / "screener_peer_universe.csv"
OUTPUT = ROOT / "outputs" / "peer_tables" / "peer_multiple_refresh_screener_filled.csv"
STATUS = ROOT / "outputs" / "peer_tables" / "peer_multiple_screener_fetch_status.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 research script; contact: educational-use",
    "Accept-Language": "en-US,en;q=0.9",
}

FIELD_ALIASES = {
    "market_cap_inr_cr": ["Market Cap"],
    "current_price": ["Current Price", "Stock P/E"],
    "pe": ["Stock P/E", "P/E"],
    "book_value": ["Book Value"],
    "pb": ["Price to book value", "Price to book", "P/B"],
    "roe": ["ROE", "Return on equity"],
    "roce": ["ROCE", "Return on capital employed"],
    "dividend_yield": ["Dividend Yield"],
    "face_value": ["Face Value"],
}


def clean_number(text: str) -> str:
    if text is None:
        return "TBD"
    text = text.replace("₹", "").replace("Cr.", "").replace("Cr", "")
    text = text.replace("%", "").replace(",", "").strip()
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return match.group(0) if match else "TBD"


def parse_top_ratios(soup: BeautifulSoup) -> dict[str, str]:
    ratios: dict[str, str] = {}
    top = soup.select_one("ul#top-ratios")
    if not top:
        return ratios
    for li in top.select("li"):
        name_el = li.select_one("span.name")
        value_el = li.select_one("span.value")
        if not name_el or not value_el:
            continue
        name = " ".join(name_el.get_text(" ", strip=True).split())
        value = " ".join(value_el.get_text(" ", strip=True).split())
        ratios[name] = value
    return ratios


def get_by_alias(ratios: dict[str, str], aliases: list[str]) -> str:
    for alias in aliases:
        for key, value in ratios.items():
            if key.lower() == alias.lower():
                return clean_number(value)
    return "TBD"


def parse_profit_loss_table(soup: BeautifulSoup) -> dict[str, str]:
    """Try to pull latest TTM / last column sales, operating profit and net profit."""
    result = {"revenue_inr_cr": "TBD", "ebitda_inr_cr": "TBD", "pat_inr_cr": "TBD"}
    section = soup.select_one("section#profit-loss")
    if not section:
        return result
    rows = section.select("table.data-table tr")
    for row in rows:
        cells = [c.get_text(" ", strip=True) for c in row.select("td, th")]
        if len(cells) < 2:
            continue
        label = cells[0].strip().lower()
        latest = cells[-1]
        if label.startswith("sales"):
            result["revenue_inr_cr"] = clean_number(latest)
        elif label.startswith("operating profit"):
            result["ebitda_inr_cr"] = clean_number(latest)
        elif label.startswith("net profit"):
            result["pat_inr_cr"] = clean_number(latest)
    return result


def safe_float(value: str):
    try:
        return float(value)
    except Exception:
        return None


def calc_ev_ebitda(market_cap: str, ebitda: str) -> str:
    mc = safe_float(market_cap)
    eb = safe_float(ebitda)
    if mc is None or eb is None or eb == 0:
        return "TBD"
    return round(mc / eb, 2)


def calc_ev_sales(market_cap: str, revenue: str) -> str:
    mc = safe_float(market_cap)
    rev = safe_float(revenue)
    if mc is None or rev is None or rev == 0:
        return "TBD"
    return round(mc / rev, 2)


def fetch_one(row: pd.Series, refresh_date: str) -> dict:
    out = row.to_dict()
    url = row["screener_url"]
    out.update({
        "market_data_date": refresh_date,
        "market_cap_inr_cr": "TBD",
        "enterprise_value_inr_cr": "TBD",
        "revenue_inr_cr": "TBD",
        "ebitda_inr_cr": "TBD",
        "pat_inr_cr": "TBD",
        "ev_sales": "TBD",
        "ev_ebitda": "TBD",
        "pe": "TBD",
        "pb": "TBD",
        "roe": "TBD",
        "roce": "TBD",
        "source": url,
        "refresh_status": "Pending",
        "parse_notes": "",
    })
    try:
        response = requests.get(url, headers=HEADERS, timeout=20)
        out["http_status"] = response.status_code
        if response.status_code != 200:
            out["refresh_status"] = "Failed"
            out["parse_notes"] = f"HTTP {response.status_code}"
            return out
        soup = BeautifulSoup(response.text, "lxml")
        ratios = parse_top_ratios(soup)
        pl = parse_profit_loss_table(soup)

        out["market_cap_inr_cr"] = get_by_alias(ratios, ["Market Cap"])
        out["pe"] = get_by_alias(ratios, ["Stock P/E", "P/E"])
        out["pb"] = get_by_alias(ratios, ["Price to book value", "Price to book", "P/B"])
        out["roe"] = get_by_alias(ratios, ["ROE", "Return on equity"])
        out["roce"] = get_by_alias(ratios, ["ROCE", "Return on capital employed"])
        out.update(pl)

        # Screener top card usually does not expose EV directly. For a conservative
        # same-source table we leave EV as TBD unless separately populated.
        out["ev_sales"] = calc_ev_sales(out["market_cap_inr_cr"], out["revenue_inr_cr"])
        out["ev_ebitda"] = calc_ev_ebitda(out["market_cap_inr_cr"], out["ebitda_inr_cr"])
        out["refresh_status"] = "Fetched; manual review required"
        missing = [k for k in ["market_cap_inr_cr", "revenue_inr_cr", "ebitda_inr_cr", "pat_inr_cr", "pe", "pb", "roe", "roce"] if out[k] == "TBD"]
        out["parse_notes"] = "Missing: " + ", ".join(missing) if missing else "Parsed all core fields"
    except Exception as exc:
        out["refresh_status"] = "Failed"
        out["parse_notes"] = str(exc)
    return out


def main() -> None:
    refresh_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    df = pd.read_csv(INPUT)
    rows = []
    for _, row in df.iterrows():
        rows.append(fetch_one(row, refresh_date))
        time.sleep(1.5)
    out_df = pd.DataFrame(rows)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(OUTPUT, index=False)

    counts = out_df["refresh_status"].value_counts(dropna=False).to_string()
    status = f"""# Screener Peer Multiple Fetch Status

## Refresh timestamp

```text
{refresh_date}
```

## Result summary

```text
{counts}
```

## Output

```text
outputs/peer_tables/peer_multiple_refresh_screener_filled.csv
```

## Important caveats

Screener does not always expose enterprise value in the top ratio block. This script fetches same-source market cap, P/E, P/B, ROE, ROCE and latest table values where available. EV/Sales and EV/EBITDA are approximated using market capitalization when EV is unavailable and must be reviewed before final SSRN use.

For final SSRN tables, manually review every row and replace market-cap-based EV approximations with true enterprise value wherever available.
"""
    STATUS.write_text(status, encoding="utf-8")
    print(f"Saved {OUTPUT}")
    print(f"Saved {STATUS}")


if __name__ == "__main__":
    main()
