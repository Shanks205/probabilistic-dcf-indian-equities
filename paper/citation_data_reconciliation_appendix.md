# Citation and Data Reconciliation Appendix

## Purpose

This appendix defines the verification work required before the GitHub-stage valuation project can be converted into an SSRN-ready working paper. The current Level 2 version is structurally complete, but SSRN publication requires formal source reconciliation, annual-report page mapping, consistent market data, and peer multiple refresh.

## Current Status

```text
Company-level Level 2 research: Complete
SSRN working paper draft: Started
Formal citation appendix: Started
Annual-report page reconciliation: Pending
Market-data refresh: Pending
Peer-table numerical refresh: Pending
Chart generation: Script added; chart outputs pending
```

## Reconciliation Principle

Every final number used in the SSRN paper should be traceable to one of the following source categories:

1. Annual report page or table.
2. Exchange filing.
3. Audited financial statement line item.
4. Consistent market-data snapshot date.
5. Explicit analyst assumption.
6. Model calculation derived from disclosed inputs.

The paper should clearly separate:

```text
Verified company-reported data
```

from:

```text
Analyst assumptions and model-derived calculations
```

## Company-Level Citation Checklist

Each company should receive a final citation map covering the following items.

| Data Item | Required Source Type | Citation Status |
|---|---|---|
| Revenue from operations | Annual report / audited financials | Pending |
| EBITDA or operating profit | Annual report / results presentation / audited financials | Pending |
| Depreciation and amortisation | Cash-flow statement / notes to accounts | Pending |
| EBIT / operating profit bridge | Model calculation or reported line item | Pending |
| PAT | Annual report / audited financials | Pending |
| Tax rate | Annual report / model calculation | Pending |
| Capex | Cash-flow statement | Pending |
| Working capital inputs | Balance sheet / model assumption | Pending |
| Cash and investments | Balance sheet | Pending |
| Debt / borrowings | Balance sheet | Pending |
| Shares outstanding | Annual report / exchange data | Pending |
| Market price | Market-data snapshot | Pending |
| Market capitalization | Market-data snapshot | Pending |
| Enterprise value | Market-data snapshot / model calculation | Pending |
| Beta | Market-data source / model assumption | Pending |
| Risk-free rate | Government bond yield snapshot | Pending |
| Equity risk premium | External cost-of-capital source / assumption | Pending |
| Company-specific risk premium | Analyst assumption | Pending |
| WACC | Model calculation | Pending |
| Terminal growth | Analyst assumption | Pending |
| Peer multiples | Market-data snapshot | Pending |

## Company-Specific Reconciliation Tracker

| # | Company | Annual Report Mapping | Market Data Refresh | Peer Table Refresh | Chart Output | SSRN-Ready Status |
|---:|---|---|---|---|---|---|
| 1 | Hero MotoCorp | Pending | Pending | Pending | Pending | Not ready |
| 2 | Fiem Industries | Pending | Pending | Pending | Pending | Not ready |
| 3 | Triveni Turbine | Pending | Pending | Pending | Pending | Not ready |
| 4 | NALCO | Pending | Pending | Pending | Pending | Not ready |
| 5 | Sharda Cropchem | Pending | Pending | Pending | Pending | Not ready |
| 6 | Time Technoplast | Pending | Pending | Pending | Pending | Not ready |
| 7 | Bharat Electronics | Pending | Pending | Pending | Pending | Not ready |
| 8 | Polycab India | Pending | Pending | Pending | Pending | Not ready |
| 9 | SJS Enterprises | Pending | Pending | Pending | Pending | Not ready |
| 10 | Shilchar Technologies | Pending | Pending | Pending | Pending | Not ready |
| 11 | JB Chemicals and Pharmaceuticals | Pending | Pending | Pending | Pending | Not ready |
| 12 | Gravita India | Pending | Pending | Pending | Pending | Not ready |

## Market Data Refresh Protocol

The final SSRN paper should use one consistent market-data date for all companies. The following fields should be refreshed on the same date:

1. Share price.
2. Market capitalization.
3. Enterprise value.
4. Shares outstanding.
5. Beta.
6. Peer valuation multiples.
7. Risk-free rate.
8. Any market-implied valuation comparison.

Suggested final data-date format:

```text
All market data are captured as of YYYY-MM-DD, unless otherwise stated.
```

## Peer Multiple Refresh Protocol

For each company, the peer table should include:

| Metric | Required? | Notes |
|---|---|---|
| Peer company name | Yes | Use comparable listed companies |
| Ticker | Yes | Exchange ticker |
| Market capitalization | Yes | Same data date |
| Enterprise value | Yes | Same data date |
| Revenue | Yes | Latest annual or trailing twelve months |
| EBITDA | Yes | Latest annual or trailing twelve months |
| PAT | Yes | Latest annual or trailing twelve months |
| EV / Sales | Yes | Relative valuation |
| EV / EBITDA | Yes | Relative valuation |
| P / E | Yes | Relative valuation |
| P / B | Optional | Useful for capital-intensive companies |
| ROCE | Recommended | Business quality comparison |
| ROE | Recommended | Capital efficiency comparison |
| Revenue CAGR | Optional | Growth comparison |
| EBITDA margin | Recommended | Margin-quality comparison |

## Chart Output Protocol

The final SSRN paper should include the following charts:

1. Median Monte Carlo fair value versus market price.
2. Median margin of safety by company.
3. Deterministic DCF value versus market price.
4. Distribution charts for selected case-study companies.
5. Sensitivity heatmaps for selected companies.
6. Cross-company valuation gap summary.

The chart-generation script currently exists at:

```text
scripts/generate_cross_company_charts.py
```

The chart outputs should be stored in:

```text
outputs/charts/
```

## Source Classification Labels

Use the following labels in final tables and appendix notes:

| Label | Meaning |
|---|---|
| Company reported | Directly from annual report or exchange filing |
| Market data | From market-data snapshot |
| Model calculated | Derived from disclosed inputs |
| Analyst assumption | Chosen assumption requiring explanation |
| Public-source proxy | Temporary GitHub-stage estimate that must be refreshed |
| Pending verification | Not yet mapped to final source |

## SSRN Readiness Gate

A company section should be marked SSRN-ready only when all of the following are complete:

1. Every operating input is mapped to a source.
2. Every market input uses the same data date.
3. Every analyst assumption is explained.
4. Peer multiples are populated and refreshed.
5. Charts are generated.
6. The company note is converted into academic prose.
7. The disclaimer is reviewed.

## Current Conclusion

The project is complete as a GitHub Level 2 research portfolio. It is not yet complete as a final SSRN paper. The next stage is a formal verification layer that converts the current public-source research draft into a citation-backed academic working paper.
