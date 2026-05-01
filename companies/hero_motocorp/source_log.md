# Hero MotoCorp Source Log

## Purpose

This file documents the source trail for the Hero MotoCorp probabilistic DCF model. The goal is to separate public-source baseline work from final SSRN-ready audited reconciliation.

## Sources Identified

| Source | Use in Current Model | Status |
|---|---|---|
| Hero MotoCorp investor relations annual-report page | Official location for annual reports and company filings | Identified; line-by-line annual-report reconciliation pending |
| FY2025 public annual-report analysis / financial statement summary | Used to update FY2024 and FY2025 revenue, operating profit, depreciation, PBT, tax, and PAT baseline | Public-source reconciled baseline |
| Previous project framework assumptions | Used only as initial WACC / valuation architecture reference | Preliminary; must be refreshed |
| Public market data providers | Required for market price, beta, share count, and peer multiples | Pending date-consistent lock |

## Current Data Status

| Data Area | Current Status |
|---|---|
| Revenue | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| Operating profit | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| Depreciation and amortization | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| PBT | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| Tax | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| PAT | Updated to FY2024-FY2025 public-source annual-report analysis baseline |
| Capex | Pending official cash flow statement extraction |
| Working capital | Pending balance-sheet schedule extraction |
| Cash and debt | Pending official balance-sheet reconciliation |
| Shares outstanding | Pending official share-count verification |
| Market price | Pending valuation-date lock |
| Beta and WACC | Pending date-consistent beta regression and WACC refresh |

## Data Boundary

The current Hero MotoCorp model is stronger than the first placeholder scaffold, but it is still not final. It should be treated as:

```text
Public-source financial baseline upgraded
Annual-report line-by-line reconciliation pending
Market-input refresh pending
```

## Required Verification Before Level 2

1. Download and review the FY2025 annual report.
2. Reconcile revenue, operating profit, depreciation, PBT, tax, PAT, cash, debt, capex, and working capital directly from statements.
3. Add official source references and page/section notes where possible.
4. Verify shares outstanding.
5. Lock market price on a valuation date.
6. Refresh beta and WACC.
7. Re-run deterministic DCF and Monte Carlo outputs.
8. Add peer numerical table.

## Research Disclaimer

This is not investment advice and does not represent a final target price.
