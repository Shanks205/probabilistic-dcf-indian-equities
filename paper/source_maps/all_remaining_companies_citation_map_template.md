# Citation Map Template for Remaining Companies

## Purpose

This template standardizes annual-report mapping and source verification for the remaining company source maps. Each company-specific citation map should follow this structure before SSRN publication.

## Standard Verification Status Block

```text
Company: [Company Name]
Ticker: [Ticker]
Mapping stage: Citation map initialized
SSRN-ready status: Not ready
Investment recommendation: None
```

## Standard Sources to Use

| Source Type | Source | Current Use |
|---|---|---|
| Official annual report | FY2024-25 annual report | Primary audited financial source |
| Exchange filings | NSE/BSE filings | Results and share-count cross-check |
| Market-data source | Final common market-data date | Market price, market cap, EV, beta |
| Model files | Level 2 GitHub company files | Starting point for reconciliation |

## Standard Annual-Report Checklist

| Data Item | Required Source Type | Mapping Status | SSRN Action Required |
|---|---|---|---|
| Revenue from operations | Annual report / audited financial statements | Pending | Add exact page and line-item reference |
| EBITDA or operating profit | Annual report / result presentation / calculated bridge | Pending | Reconcile reported value or calculation |
| Depreciation and amortisation | Cash-flow statement / notes to accounts | Pending | Add exact page reference |
| EBIT / operating profit bridge | Model calculation or reported line item | Pending | Document formula and source inputs |
| PAT | Annual report / audited financial statements | Pending | Add exact page reference |
| Tax expense / tax rate | Annual report / model calculation | Pending | Map tax expense and calculate tax rate |
| Capex | Cash-flow statement | Pending | Map purchase of PPE / intangible assets |
| Working capital inputs | Balance sheet / model assumption | Pending | Map receivables, inventory and payables if used |
| Cash and investments | Balance sheet / notes | Pending | Reconcile cash, bank balances and investments |
| Debt / borrowings | Balance sheet / notes | Pending | Reconcile borrowings and lease liabilities |
| Shares outstanding | Share capital note / exchange data | Pending | Reconcile share count used in valuation |

## Standard Market-Data Refresh Checklist

| Data Item | Current Status | Required SSRN Action |
|---|---|---|
| Market price | Public delayed proxy | Refresh using one common data date |
| Market capitalization | Public delayed proxy | Refresh using one common data date |
| Enterprise value | Public delayed proxy / model calculation | Refresh or recalculate using one common data date |
| Beta | Public market-data proxy / analyst assumption | Refresh using consistent source/date |
| Risk-free rate | India 10-year government bond proxy | Refresh using final common data date |
| Equity risk premium | Analyst / country-risk assumption | Cite source or explain assumption |
| Company-specific risk premium | Analyst assumption | Explain in methodology appendix |

## SSRN Readiness Assessment

```text
Annual-report mapping: Initialized / Pending detailed page mapping
Market-data refresh: Pending
Peer-table refresh: Pending
Chart output: Pending
Academic rewrite: Pending
SSRN-ready status: Not ready
```

## Research Boundary

These citation maps are for research verification and SSRN preparation only. They are not investment advice, financial advice, or buy/sell recommendations.
