# Fiem Industries Assumption Log

## Modelling Stage

```text
Stage: Company 2 preliminary GitHub model
Data status: Public-source baseline / placeholder where necessary
Conclusion status: No investment conclusion
```

## Base Case Assumptions

| Variable | Base Case | Rationale | Status |
|---|---:|---|---|
| Starting revenue | Rs 2,405.6 crore | FY2025 public-source revenue baseline | Preliminary |
| Revenue growth | 10.0% | Auto-component growth and LED content assumption | Preliminary |
| EBIT margin | 11.55% | FY2025 EBIT margin baseline | Preliminary |
| Tax rate | 25.8% | Normalized effective tax assumption | Preliminary |
| Depreciation / sales | 2.62% | Based on FY2025 D&A estimate divided by revenue | Preliminary |
| Capex / sales | 4.0% | Normalized reinvestment assumption | Preliminary |
| NWC / sales | 12.0% | Working-capital intensity placeholder | Preliminary |
| WACC | 15.13% | Retained from earlier framework pending beta regression refresh | Preliminary |
| Terminal growth | 4.0% | Conservative long-term nominal growth assumption | Preliminary |
| Net debt | -Rs 276.2 crore | Preliminary net cash estimate | Preliminary |
| Shares outstanding | 26.32 crore | Preliminary share count estimate; verify carefully | Preliminary |

## Monte Carlo Distribution Assumptions

| Variable | Distribution | Bear | Base / Mode | Bull | Rationale |
|---|---|---:|---:|---:|---|
| Revenue growth | Triangular | 6.0% | 10.0% | 14.0% | Captures growth and auto-cycle uncertainty |
| EBIT margin | Triangular | 9.5% | 11.55% | 13.5% | Captures margin pressure/upside |
| Tax rate | Triangular | 24.0% | 25.8% | 28.0% | Captures tax uncertainty |
| Depreciation / sales | Triangular | 2.2% | 2.62% | 3.0% | Captures asset-intensity uncertainty |
| Capex / sales | Triangular | 3.0% | 4.0% | 5.5% | Captures reinvestment uncertainty |
| NWC / sales | Triangular | 9.0% | 12.0% | 16.0% | Captures working-capital uncertainty |
| WACC | Normal | n/a | 15.13% | n/a | Standard deviation 1.2%; beta refinement pending |
| Terminal growth | Uniform | 3.0% | n/a | 5.0% | Conservative terminal range |

## Professional Refinement Required

Before SSRN-level publication, update this log with:

1. annual-report-reconciled financials,
2. verified capex and working-capital schedules,
3. customer concentration and platform-risk documentation,
4. beta regression output,
5. risk-free rate and equity risk premium source,
6. market price locked on valuation date.
