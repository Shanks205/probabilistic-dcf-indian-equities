# Hero MotoCorp Assumption Log

## Modelling Stage

```text
Stage: Company 1 preliminary GitHub model
Data status: Public-source baseline
Conclusion status: No investment conclusion
```

## Base Case Assumptions

| Variable | Base Case | Rationale | Status |
|---|---:|---|---|
| Starting revenue | Rs 40,923.4 crore | FY2025 public-source revenue baseline | Preliminary |
| Revenue growth | 8.0% | Mature auto recovery assumption based on recent growth and earlier framework | Preliminary |
| EBIT margin | 12.62% | FY2025 EBIT margin baseline | Preliminary |
| Tax rate | 26.25% | FY2025 effective tax rate baseline | Preliminary |
| Depreciation / sales | 1.50% | Based on FY2025 depreciation divided by revenue | Preliminary |
| Capex / sales | 3.50% | Placeholder normalized reinvestment assumption | Preliminary |
| NWC / sales | 8.00% | Normalized modelling assumption; FY2025 balance sheet working capital is higher and needs reconciliation | Preliminary |
| WACC | 12.58% | Retained from earlier framework pending beta regression refresh | Preliminary |
| Terminal growth | 4.00% | Conservative long-term nominal growth assumption | Preliminary |
| Net debt | -Rs 6,487.9 crore | Preliminary net cash estimate from cash minus debt | Preliminary |
| Shares outstanding | 20.001 crore | Preliminary share count estimate | Preliminary |

## Monte Carlo Distribution Assumptions

| Variable | Distribution | Bear | Base / Mode | Bull | Rationale |
|---|---|---:|---:|---:|---|
| Revenue growth | Triangular | 4.0% | 8.0% | 12.0% | Captures recovery uncertainty |
| EBIT margin | Triangular | 10.0% | 12.62% | 14.5% | Captures margin pressure/upside |
| Tax rate | Triangular | 23.0% | 26.25% | 28.0% | Captures normalized tax uncertainty |
| Depreciation / sales | Triangular | 1.2% | 1.5% | 1.8% | Captures asset intensity uncertainty |
| Capex / sales | Triangular | 2.5% | 3.5% | 5.0% | Captures reinvestment uncertainty |
| NWC / sales | Triangular | 6.0% | 8.0% | 10.0% | Captures working-capital uncertainty |
| WACC | Normal | n/a | 12.58% | n/a | Standard deviation 1.0%; beta refinement pending |
| Terminal growth | Uniform | 3.0% | n/a | 5.0% | Conservative terminal range |

## Professional Refinement Required

Before SSRN-level publication, update this log with:

1. annual-report-reconciled financials,
2. audited cash flow statement capex,
3. verified working capital schedule,
4. beta regression output,
5. risk-free rate and equity risk premium source,
6. market price locked on valuation date.
