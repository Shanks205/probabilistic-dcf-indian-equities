# Peer Multiple Source Plan

## Purpose

This file records the final source policy for peer multiple completion.

## Status

The peer-table structure is complete, but numerical peer multiples are not marked as verified because the current workflow artifact did not include a verified source export for peer market caps, enterprise values, EBITDA, PAT, book value, ROE and ROCE.

## Source Policy for SSRN-Ready Peer Multiples

To avoid inconsistent definitions, peer multiples must be populated using one source family and one data date.

Acceptable sources:

1. Screener.in company pages exported on the same date for all peers.
2. TIKR / Capital IQ / Refinitiv / Bloomberg export, if available.
3. Manual annual-report + market-cap reconstruction for each peer, if no database is used.

Not acceptable for final SSRN-ready numerical tables:

1. Mixing Yahoo Finance, Screener, brokerage reports and unaudited website snapshots without a reconciliation note.
2. Estimating missing peer EBITDA or EV/EBITDA from memory.
3. Using peer multiples from different dates without explaining the mismatch.

## Current Peer Table Status

The peer framework file exists and remains the master template:

```text
outputs/peer_tables/peer_multiple_refresh_expanded_template.csv
```

A status file exists at:

```text
outputs/peer_tables/verified_peer_multiple_status_v1.csv
```

## Final Completion Requirement

Before the project is labelled fully SSRN-ready, add a filled file:

```text
outputs/peer_tables/peer_multiple_refresh_filled_verified.csv
```

Minimum required fields:

```text
company
peer_company
market_data_date
market_cap_inr_cr
enterprise_value_inr_cr
revenue_inr_cr
ebitda_inr_cr
pat_inr_cr
ev_sales
ev_ebitda
pe
pb
roe
roce
source
notes
```

## Research Boundary

This file prevents false precision in the relative valuation layer. It is not investment advice, financial advice, or a buy/sell recommendation.
