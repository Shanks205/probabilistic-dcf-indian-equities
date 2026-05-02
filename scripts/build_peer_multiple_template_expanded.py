"""Build an expanded peer-multiple input template.

This script creates a richer peer-table template with suggested peer buckets for
manual refresh. Peer multiples should generally be manually sourced or reviewed
because automated sources can vary in definitions of EBITDA, EV, PAT, and TTM.

Usage:
    python scripts/build_peer_multiple_template_expanded.py

Output:
    outputs/peer_tables/peer_multiple_refresh_expanded_template.csv
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs" / "peer_tables" / "peer_multiple_refresh_expanded_template.csv"

PEERS = {
    "Hero MotoCorp": ["Bajaj Auto", "TVS Motor", "Eicher Motors", "Honda India peer proxy"],
    "Fiem Industries": ["Lumax Industries", "Minda Corporation", "Uno Minda", "Pricol"],
    "Triveni Turbine": ["Thermax", "TD Power Systems", "Siemens India", "ABB India"],
    "NALCO": ["Hindalco", "Vedanta", "Hindustan Zinc", "NMDC"],
    "Sharda Cropchem": ["PI Industries", "Bharat Rasayan", "Dhanuka Agritech", "Rallis India"],
    "Time Technoplast": ["Mold-Tek Packaging", "Supreme Industries", "Nilkamal", "TPL Plastech"],
    "Bharat Electronics": ["Data Patterns", "Astra Microwave", "HAL", "Bharat Dynamics"],
    "Polycab India": ["KEI Industries", "RR Kabel", "Finolex Cables", "Havells India"],
    "SJS Enterprises": ["Minda Corporation", "Uno Minda", "Suprajit Engineering", "Lumax Auto Technologies"],
    "Shilchar Technologies": ["Transformers and Rectifiers", "Voltamp Transformers", "Bharat Bijlee", "TD Power Systems"],
    "JB Chemicals and Pharmaceuticals": ["Torrent Pharma", "Alkem Laboratories", "Ajanta Pharma", "Eris Lifesciences"],
    "Gravita India": ["Pondy Oxides", "Hindustan Zinc", "Vedanta", "Hindalco"],
}

TICKERS = {
    "Hero MotoCorp": "HEROMOTOCO.NS",
    "Fiem Industries": "FIEMIND.NS",
    "Triveni Turbine": "TRITURBINE.NS",
    "NALCO": "NATIONALUM.NS",
    "Sharda Cropchem": "SHARDACROP.NS",
    "Time Technoplast": "TIMETECHNO.NS",
    "Bharat Electronics": "BEL.NS",
    "Polycab India": "POLYCAB.NS",
    "SJS Enterprises": "SJS.NS",
    "Shilchar Technologies": "SHILCTECH.NS",
    "JB Chemicals and Pharmaceuticals": "JBCHEPHARM.NS",
    "Gravita India": "GRAVITA.NS",
}

BUCKETS = {
    "Hero MotoCorp": "Two-wheeler / auto OEM",
    "Fiem Industries": "Auto components / lighting",
    "Triveni Turbine": "Capital goods / turbines",
    "NALCO": "Aluminium / commodity metals",
    "Sharda Cropchem": "Agrochemicals / asset-light registrations",
    "Time Technoplast": "Industrial packaging / polymers",
    "Bharat Electronics": "Defence electronics / PSU defence",
    "Polycab India": "Cables and electricals",
    "SJS Enterprises": "Auto ancillary / decorative aesthetics",
    "Shilchar Technologies": "Transformers / electrical capital goods",
    "JB Chemicals and Pharmaceuticals": "Branded formulations / pharma",
    "Gravita India": "Recycling / non-ferrous metals",
}

COLUMNS = [
    "company", "company_ticker", "peer_bucket", "peer_company", "peer_ticker",
    "market_data_date", "market_cap_inr_cr", "enterprise_value_inr_cr",
    "revenue_inr_cr", "ebitda_inr_cr", "pat_inr_cr", "ev_sales",
    "ev_ebitda", "pe", "pb", "roce", "roe", "revenue_cagr",
    "ebitda_margin", "cash_conversion", "source", "refresh_status", "notes",
]


def main() -> None:
    rows = []
    for company, peers in PEERS.items():
        for peer in peers:
            rows.append(
                {
                    "company": company,
                    "company_ticker": TICKERS[company],
                    "peer_bucket": BUCKETS[company],
                    "peer_company": peer,
                    "peer_ticker": "TBD",
                    "market_data_date": "TBD",
                    "market_cap_inr_cr": "TBD",
                    "enterprise_value_inr_cr": "TBD",
                    "revenue_inr_cr": "TBD",
                    "ebitda_inr_cr": "TBD",
                    "pat_inr_cr": "TBD",
                    "ev_sales": "TBD",
                    "ev_ebitda": "TBD",
                    "pe": "TBD",
                    "pb": "TBD",
                    "roce": "TBD",
                    "roe": "TBD",
                    "revenue_cagr": "TBD",
                    "ebitda_margin": "TBD",
                    "cash_conversion": "TBD",
                    "source": "Manual market-data / annual-report refresh required",
                    "refresh_status": "Pending",
                    "notes": "Review peer suitability before final SSRN use",
                }
            )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows, columns=COLUMNS).to_csv(OUTPUT, index=False)
    print(f"Saved expanded peer template to {OUTPUT}")


if __name__ == "__main__":
    main()
