# Peer EV/PB Enrichment Final Review

## Artifact Reviewed

The uploaded `peer-ev-pb-enriched-outputs.zip` artifact was extracted and reviewed.

Files reviewed:

```text
peer_multiple_refresh_screener_filled.csv
peer_multiple_screener_fetch_status.md
peer_multiple_refresh_ev_pb_enriched.csv
peer_multiple_ev_pb_enrichment_status.md
```

## Status Output

```text
Screener refresh timestamp: 2026-05-02 08:01 UTC
Yahoo EV/PB enrichment timestamp: 2026-05-02 08:03 UTC
Screener rows fetched: 47 / 47
Yahoo refresh rows fetched: 47 / 47
Yahoo EV populated: 46 / 47
Yahoo P/B populated: 47 / 47
True EV/Sales calculated: 42 / 47
True EV/EBITDA calculated: 42 / 47
```

## Files Added to Repository

```text
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
outputs/peer_tables/peer_multiple_ev_pb_summary_by_company.csv
```

## Company-Level Median Peer Multiples

| Company | Median True EV/Sales | Median True EV/EBITDA | Median P/E | Median P/B | Median ROE | Median ROCE | Status |
|---|---:|---:|---:|---:|---:|---:|---|
| Hero MotoCorp | 5.06 | 24.95 | 36.10 | 8.83 | 24.10 | 28.10 | Complete |
| Fiem Industries | 2.12 | 18.55 | 37.80 | 6.00 | 17.55 | 17.60 | Complete |
| Triveni Turbine | 11.04 | 60.02 | 82.45 | 14.60 | 17.95 | 23.05 | Partial |
| NALCO | 2.20 | 8.38 | 12.90 | 2.55 | 21.30 | 23.05 | Complete |
| Sharda Cropchem | 2.07 | 14.16 | 24.75 | 2.84 | 15.00 | 19.20 | Complete |
| Time Technoplast | 2.37 | 14.62 | 24.45 | 3.19 | 16.55 | 20.50 | Complete |
| Bharat Electronics | 8.72 | 30.86 | 49.60 | 10.57 | 20.25 | 26.30 | Partial |
| Polycab India | 2.71 | 28.79 | 40.10 | 7.56 | 17.50 | 23.10 | Complete |
| SJS Enterprises | 2.49 | 20.03 | 42.90 | 7.64 | 14.80 | 15.75 | Complete |
| Shilchar Technologies | 7.52 | 43.08 | 59.95 | 7.32 | 20.70 | 26.85 | Partial |
| JB Chemicals and Pharmaceuticals | 6.70 | 23.53 | 38.05 | 7.00 | 22.15 | 23.70 | Complete |
| Gravita India | 1.70 | 9.79 | 15.85 | 4.29 | 16.50 | 16.05 | Complete |

## Remaining Missing Items

Five row-level EV/Sales or EV/EBITDA values remain unavailable because the required operating metrics or Yahoo EV were not fully available:

```text
Siemens India: missing Yahoo enterprise value
Bharat Dynamics: missing Screener operating fields
Data Patterns: missing Screener operating fields
Voltamp Transformers: missing Screener operating fields
Bharat Bijlee: missing Screener operating fields
```

## Methodology Assessment

This is now a much stronger peer valuation layer than the earlier market-cap proxy table because:

1. Screener provides a consistent source for peer universe and operating/return metrics.
2. Yahoo Finance provides enterprise value and P/B where Screener did not expose them in the parsed output.
3. True EV/Sales and EV/EBITDA were calculated for 42 out of 47 peer rows.
4. P/B was populated for all 47 rows.

## SSRN Use Status

This peer layer can be used in the SSRN manuscript as a draft-to-near-final relative valuation exhibit with one caveat: the manuscript must disclose the two-source method and the five row-level missing items.

Recommended wording:

```text
Peer multiples were constructed using Screener.in for peer operating metrics and Yahoo Finance for enterprise value and price-to-book data. The data were refreshed on 2 May 2026. Five peer rows required manual review due to missing operating metrics or enterprise value, and company-level medians were computed using available parsed values.
```

## Research Boundary

This peer valuation layer is for research documentation only. It is not investment advice, financial advice, or a buy/sell recommendation.
