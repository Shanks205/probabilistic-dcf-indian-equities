# Market Data Review Notes

## Purpose

This file reviews the `ssrn-next-steps-outputs` workflow artifact uploaded after running the SSRN Next Steps Pipeline.

## Pipeline Result

The uploaded artifact confirms that the SSRN Next Steps Pipeline executed successfully.

| Pipeline Step | Status |
|---|---|
| Market-data refresh | Success |
| Expanded peer template generation | Success |
| Cross-company chart generation | Success |

## Generated Files Confirmed in Artifact

```text
outputs/market_data/final_market_data_refresh_filled.csv
outputs/market_data/market_data_refresh_status.md
outputs/peer_tables/peer_multiple_refresh_expanded_template.csv
outputs/charts/median_fair_value_vs_market_price.png
outputs/charts/median_margin_of_safety.png
outputs/charts/valuation_gap_by_company.png
outputs/research_tracker/ssrn_next_steps_pipeline_status.md
```

## Market-Data Timestamp

```text
2026-05-02 01:31 UTC
```

## Market-Data Refresh Summary

```text
Companies auto-filled: 12
Companies failed: 0
```

## Market Data Review Observations

The automated refresh successfully populated share price, market capitalization, enterprise value, shares outstanding and beta for all 12 companies using Yahoo Finance fields.

However, this output should still be treated as a first-pass market-data refresh because:

1. Yahoo Finance enterprise value may not use the same cash/debt definitions as the annual-report-based DCF bridge.
2. Beta values for some companies appear unusually low or negative and should be manually reviewed before use in WACC.
3. The India 10-year government bond yield was intentionally left as manual input because it should be locked to the same final market-data date.
4. Market data should be refreshed again immediately before final SSRN upload if the paper is finalized later.

## Companies Requiring Beta Review

The following beta values should be reviewed before final WACC use:

| Company | Auto-filled beta | Review note |
|---|---:|---|
| Triveni Turbine | 0.149 | Very low for capital goods; review source and methodology |
| Shilchar Technologies | -0.533 | Negative beta is likely unsuitable for final WACC without strong justification |
| JB Chemicals and Pharmaceuticals | -0.003 | Near-zero beta is likely unsuitable for final WACC without strong justification |
| Gravita India | 0.172 | Very low for commodity-linked recycling business; review source and methodology |

## Suggested Risk-Free Rate Treatment

For the final SSRN draft, use one clearly documented India 10-year government bond yield date. If the final market-data date remains close to the artifact date, a provisional India 10-year G-sec yield of approximately 7.0% can be used for sensitivity review, but the exact final source should be cited and locked before upload.

## Recommended Enterprise Value Treatment

For final SSRN use, enterprise value should preferably be recalculated manually using:

```text
Enterprise value = market capitalization + gross debt - cash and cash equivalents - current investments selected as cash-like
```

This is especially important for:

| Company | Reason |
|---|---|
| Polycab India | Net cash definition must be reconciled with borrowings, cash equivalents, investments and acceptances |
| JB Chemicals and Pharmaceuticals | Cash plus current investments minus borrowings should replace the earlier Level 2 proxy |
| Hero MotoCorp | Large cash/investment balance materially affects enterprise value |
| NALCO | Net cash and commodity-cycle valuation sensitivity should be reconciled |
| Bharat Electronics | Cash and order-book-driven working capital can affect EV bridge |

## Current Status

```text
Market-data pipeline: Successfully executed
Market-data table: Auto-filled for all 12 companies
Market-data use in final SSRN paper: Pending manual review
Risk-free rate: Pending final source/date lock
EV bridge: Pending manual reconciliation for key companies
```

## Next Action

1. Use `final_market_data_refresh_filled.csv` as the first-pass market-data table.
2. Add final India 10-year G-sec rate once the final market-data date is locked.
3. Replace suspicious beta values with a documented normalized beta assumption where appropriate.
4. Recalculate enterprise value manually for cash-heavy or debt-definition-sensitive companies.
5. Use the generated charts as draft exhibits, subject to final data refresh.

## Research Boundary

This review is part of the SSRN verification workflow. It is not investment advice, financial advice, or a buy/sell recommendation.
