# Hero MotoCorp Assumption Log

## Modelling Stage

```text
Stage: Company 1 public-source baseline upgrade
Data status: FY2024-FY2025 public-source annual-report analysis baseline added
Conclusion status: No investment conclusion
```

## Updated Base Case Assumptions

| Variable | Base Case | Rationale | Status |
|---|---:|---|---|
| Starting revenue | Rs 40,923.4 crore | FY2025 public-source annual-report analysis baseline | Public-source baseline; official line-item reconciliation pending |
| Revenue growth | 8.0% | Mature two-wheeler recovery assumption; close to FY2025 revenue growth | Preliminary |
| Operating profit margin | 13.70% | FY2025 public-source operating profit margin baseline | Public-source baseline; official reconciliation pending |
| Tax rate | 26.30% | FY2025 public-source tax / PBT baseline | Public-source baseline; official reconciliation pending |
| Depreciation / sales | 1.58% | FY2025 depreciation divided by revenue | Public-source baseline; official reconciliation pending |
| Capex / sales | 3.50% | Placeholder normalized reinvestment assumption | Preliminary; cash-flow extraction pending |
| NWC / sales | 8.00% | Normalized modelling assumption | Preliminary; balance-sheet schedule pending |
| WACC | 12.58% | Retained from earlier framework pending beta regression refresh | Preliminary; beta refresh pending |
| Terminal growth | 4.00% | Conservative long-term nominal growth assumption | Preliminary |
| Net debt | Not locked | Cash and debt require official balance-sheet reconciliation | Pending |
| Shares outstanding | Not locked | Share count requires official filing verification | Pending |

## Monte Carlo Distribution Assumptions

| Variable | Distribution | Bear | Base / Mode | Bull | Rationale |
|---|---|---:|---:|---:|---|
| Revenue growth | Triangular | 4.0% | 8.0% | 12.0% | Captures recovery uncertainty |
| Operating profit margin | Triangular | 11.0% | 13.7% | 15.0% | Captures margin pressure/upside based on FY2025 margin baseline |
| Tax rate | Triangular | 24.0% | 26.3% | 28.0% | Captures normalized tax uncertainty |
| Depreciation / sales | Triangular | 1.3% | 1.58% | 1.9% | Captures asset-intensity uncertainty |
| Capex / sales | Triangular | 2.5% | 3.5% | 5.0% | Captures reinvestment uncertainty |
| NWC / sales | Triangular | 6.0% | 8.0% | 10.0% | Captures working-capital uncertainty |
| WACC | Normal | n/a | 12.58% | n/a | Standard deviation 1.0%; beta refinement pending |
| Terminal growth | Uniform | 3.0% | n/a | 5.0% | Conservative terminal range |

## Professional Refinement Required

Before SSRN-level publication, update this log with:

1. line-by-line annual-report reconciliation,
2. audited cash flow statement capex,
3. verified working capital schedule,
4. verified cash, debt, and share count,
5. beta regression output,
6. risk-free rate and equity risk premium source,
7. market price locked on valuation date.
