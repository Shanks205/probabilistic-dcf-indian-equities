# Enterprise Value Bridge Methodology Note

## Purpose

This note documents how enterprise value should be treated in the final SSRN manuscript.

## Why This Matters

Enterprise value can differ across sources because cash, current investments, deposits, acceptances, lease liabilities, current borrowings, long-term borrowings and other debt-like obligations may be treated differently by different market-data providers.

For this project, enterprise value is not blindly accepted from one source. Instead, three layers are separated:

```text
1. Yahoo Finance enterprise value
2. Annual-report reconstructed enterprise value
3. Manual-patched enterprise value for rows where automated parsing was incomplete
```

## Preferred Formula

For final company-level valuation:

```text
Enterprise value = market capitalization + gross debt - cash and cash equivalents - current investments treated as cash-like
```

Where appropriate, the model should explicitly state whether it includes or excludes:

```text
lease liabilities
acceptances
cash credit
short-term deposits
current investments
bank balances other than cash equivalents
```

## High-Priority EV Bridge Companies

| Company | Reason |
|---|---|
| Hero MotoCorp | Large cash/investment balance materially affects equity bridge |
| NALCO | Commodity-cycle valuation and cash balance affect downside protection |
| Bharat Electronics | Debt-equity is low/nil but cash and deposits materially affect EV |
| Polycab India | Net cash, cash credit and acceptances need clear definition |
| JB Chemicals and Pharmaceuticals | Cash plus current investments minus borrowings creates materially different EV from Yahoo |
| Gravita India | QIP and net-debt-free transition changed the capital structure |

## Treatment in Manuscript

The final manuscript should not present EV as one unquestioned figure. It should use wording such as:

```text
Enterprise value was reviewed using both market-data provider values and annual-report-based cash/debt reconstruction. Where the difference was material, the annual-report-based bridge was preferred for interpretation, while provider EV was retained as an external reference.
```

## Current Files

```text
outputs/market_data/ev_bridge_review_priority.csv
outputs/market_data/manual_ev_bridge_reconciliation_v1.csv
outputs/market_data/manual_ev_bridge_recalculated_v1.csv
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
outputs/peer_tables/peer_ev_pb_manual_gap_fill.csv
```

## Research Boundary

This note is for research methodology and SSRN preparation only. It is not investment advice, financial advice, or a buy/sell recommendation.
