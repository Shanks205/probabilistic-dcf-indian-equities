# Screener Peer Multiple Review Notes

## Artifact Reviewed

The uploaded artifact `screener-peer-multiple-outputs.zip` was extracted and reviewed.

Files reviewed:

```text
peer_multiple_refresh_screener_filled.csv
peer_multiple_screener_fetch_status.md
```

## Fetch Status

```text
Refresh timestamp: 2026-05-02 06:24 UTC
Rows fetched: 47
Failed rows: 0
```

## Main Result

The Screener workflow successfully fetched a same-source peer dataset for the selected peer universe. This is now a usable peer-comparison layer for draft SSRN analysis, subject to final review caveats.

## Parsed Coverage

| Metric | Coverage |
|---|---:|
| Market cap | 43 / 47 rows |
| Revenue | 43 / 47 rows |
| Operating profit / EBITDA proxy | 43 / 47 rows |
| PAT | 43 / 47 rows |
| P/E | 43 / 47 rows |
| ROE | 43 / 47 rows |
| ROCE | 43 / 47 rows |
| P/B | 0 / 47 rows |
| True EV | 0 / 47 rows |

## Rows Requiring Manual Replacement

Four rows returned HTTP 200 but could not be parsed into the expected ratio fields:

```text
Bharat Dynamics
Data Patterns
Voltamp Transformers
Bharat Bijlee
```

These rows should be manually replaced or refetched with a parser adjustment before the peer table is called fully verified.

## Important Methodology Caveat

Screener's visible parsed data did not expose true enterprise value. Therefore:

```text
EV/Sales and EV/EBITDA in the generated table are market-cap-based approximations, not true enterprise-value multiples.
```

For final SSRN upload, either:

1. replace those values with true EV-based multiples from a verified source, or
2. rename them as market-cap-to-sales and market-cap-to-operating-profit proxy multiples.

## Peer Summary File Added

A company-level peer summary has been added at:

```text
outputs/peer_tables/peer_multiple_screener_summary_by_company.csv
```

This summary uses median peer multiples by company and clearly labels EV ratios as market-cap proxy ratios.

## Current Peer Layer Status

```text
Screener peer source: Consistent
Same-date fetch: Complete
Rows fetched: 47 / 47
Rows parsed for core fields: 43 / 47
P/B: Not parsed
True EV: Not parsed
SSRN use status: Usable as draft relative valuation layer; not final verified EV multiple table
```

## Research Boundary

This peer review is part of the SSRN verification workflow. It is not investment advice, financial advice, or a buy/sell recommendation.
