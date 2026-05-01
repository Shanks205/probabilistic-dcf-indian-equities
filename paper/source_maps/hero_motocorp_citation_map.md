# Hero MotoCorp Citation and Data Reconciliation Map

## Purpose

This file starts the annual-report mapping and source-verification layer for Hero MotoCorp. It converts the Level 2 GitHub inputs into an SSRN-style citation checklist.

## Verification Status

```text
Company: Hero MotoCorp
Ticker: HEROMOTOCO.NS
Mapping stage: Partial annual-report mapping started
SSRN-ready status: Not ready
Investment recommendation: None
```

## Primary Sources Identified

| Source Type | Source | Current Use |
|---|---|---|
| Official annual report page | Hero MotoCorp investor relations annual report page | Primary annual-report source locator |
| Official FY2024-25 annual report PDF | `hero_motocorp_ir_2024_25_c2c_v3.pdf` from Hero MotoCorp website | Primary FY2025 audited financial source |
| Public annual-report analysis cross-check | Equitymaster FY2024-25 annual report analysis | Secondary cross-check for consolidated income statement values |
| Market-data source | Public delayed market data used in Level 2 file | Temporary market-data proxy; final SSRN refresh required |

## Annual-Report Values Mapped So Far

| Data Item | Level 2 Value | Unit | Mapping Status | Source Evidence | SSRN Action Required |
|---|---:|---|---|---|---|
| Consolidated total income | 41,967.50 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Profit before finance cost and depreciation | 6,989.92 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Finance cost | 70.65 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Depreciation and amortisation expense | 824.59 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Profit before tax | 5,933.56 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Tax expense | 1,557.75 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Net profit after tax | 4,375.81 | INR crore | Mapped to official annual-report snippet | Official Hero MotoCorp FY2024-25 annual report financial highlights | Add exact PDF page number in final manuscript |
| Revenue from operations / operating income | 40,923.4 | INR crore | Cross-checked but needs official annual-report line mapping | Equitymaster reports FY2025 net sales / operating income of Rs 409,234 million | Map directly to annual-report consolidated revenue from operations note |
| Capex | Not used in final Level 2 input table | INR crore | Needs mapping if used in appendix | Cash-flow statement should be mapped directly | Add cash-flow statement page reference |
| Cash and short-term investments | 10,795.0 | INR crore | Not yet annual-report mapped | Public market-data balance-sheet proxy | Reconcile with annual-report balance sheet and investment notes |
| Debt | 718.0 | INR crore | Not yet annual-report mapped | Public market-data balance-sheet proxy | Reconcile with borrowings / lease liabilities in annual report |
| Shares outstanding | 20.009 | crore shares | Not yet annual-report mapped | Public market-data proxy | Reconcile with equity share capital note |

## Market-Data Inputs Requiring Refresh

| Data Item | Level 2 Value | Current Status | Required SSRN Action |
|---|---:|---|---|
| Market price | Rs 5,111.55 | Public delayed market-data proxy | Refresh on one common data date for all 12 companies |
| Market capitalization | Rs 102,000 crore | Public delayed market-data proxy | Refresh on common data date |
| Enterprise value | Rs 92,123 crore | Public delayed market-data proxy | Recalculate or source on common data date |
| Beta | 0.64 | Public market-data proxy | Refresh using consistent source/date |
| Risk-free rate | 6.98% | India 10-year government bond proxy | Refresh using common final data date |
| Equity risk premium | 7.00% | Analyst / country-risk assumption | Cite source or explain assumption |
| Company-specific risk premium | 1.00% | Analyst assumption | Explain in methodology appendix |

## Model-Derived Inputs

| Data Item | Value | Status | Notes |
|---|---:|---|---|
| Net cash estimate | Rs 10,077 crore | Model-derived | Cash and short-term investments less debt |
| WACC used | 12.46% | Model-derived | Approximate cost-of-equity style WACC due to net-cash balance sheet |
| Terminal growth | 4.00% | Analyst assumption | Should be justified as conservative long-term nominal growth |

## Reconciliation Notes

1. The official annual report source confirms the core consolidated FY2025 financial highlights used in the Level 2 model, including total income, EBITDA-style profit before finance cost and depreciation, finance cost, depreciation, PBT, tax expense, and PAT.
2. Revenue from operations / net sales is cross-checked through a public annual-report analysis source but should still be mapped directly to the official annual-report revenue note before SSRN publication.
3. Balance-sheet items such as cash, investments, debt, and shares outstanding remain temporary public-source proxies until mapped directly to annual-report notes.
4. Market price, market capitalization, enterprise value, beta, and risk-free rate must be refreshed using one common date across all 12 companies.

## SSRN Readiness Assessment

```text
Annual-report mapping: Partial
Market-data refresh: Pending
Peer-table refresh: Pending
Chart output: Pending
Academic rewrite: Pending
SSRN-ready status: Not ready
```

## Next Required Actions

1. Download or review the official FY2024-25 annual report PDF directly.
2. Add exact page numbers for all mapped income-statement and cash-flow items.
3. Map revenue from operations directly to the annual-report financial statements.
4. Map cash, investments, borrowings, and share capital to balance-sheet notes.
5. Refresh all market data using the final common data date.
6. Update the Hero company section in the SSRN draft after source reconciliation.

## Research Boundary

This citation map is for research verification and SSRN preparation only. It is not investment advice, financial advice, or a buy/sell recommendation.
