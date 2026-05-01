# Hero MotoCorp Preliminary Probabilistic DCF Note

## Company Role in the Project

Hero MotoCorp is used as Company 1 in the probabilistic DCF valuation project. It represents the mature auto/two-wheeler recovery archetype. The company is useful as a first implementation case because its DCF logic is easier to model than highly cyclical commodity, refining, or product-cycle-driven companies.

## Modelling Objective

The objective is not to issue a target price. The objective is to demonstrate how a deterministic FCFF DCF can be converted into a probabilistic valuation framework using Monte Carlo simulation.

## Preliminary Historical Baseline

The current baseline uses FY2025 public-source financial data:

| Metric | FY2025 Baseline |
|---|---:|
| Revenue | Rs 40,923.4 crore |
| EBIT | Rs 5,163.2 crore |
| EBIT margin | 12.62% |
| EBITDA | Rs 5,776.8 crore |
| EBITDA margin | 14.12% |
| Depreciation and amortization | Rs 613.6 crore |
| Effective tax rate | 26.25% |
| Net cash | Rs 6,487.9 crore |
| Shares outstanding | 20.001 crore |

These figures are preliminary and require annual-report reconciliation before research-paper use.

## Deterministic DCF Output

The first-pass deterministic DCF model produces the following preliminary outputs:

| Output | Value |
|---|---:|
| PV of explicit FCFF | Rs 12,149.61 crore |
| PV of terminal value | Rs 27,059.17 crore |
| Enterprise value | Rs 39,208.78 crore |
| Equity value | Rs 45,696.68 crore |
| Fair value per share | Rs 2,284.72 |

This is not a target price. It is a model architecture output based on preliminary assumptions.

## Monte Carlo Output

The Monte Carlo simulation uses 10,000 simulations and produces the following preliminary valuation range:

| Metric | Value |
|---|---:|
| Mean fair value per share | Rs 2,239.20 |
| Median fair value per share | Rs 2,204.48 |
| 5th percentile | Rs 1,670.86 |
| 25th percentile | Rs 1,976.17 |
| 75th percentile | Rs 2,466.82 |
| 95th percentile | Rs 2,904.26 |

## Interpretation

The current output demonstrates how Monte Carlo DCF converts a single valuation estimate into a valuation distribution. The distribution captures uncertainty in revenue growth, EBIT margin, tax rate, depreciation intensity, capex intensity, working capital intensity, WACC, and terminal growth.

The model currently suggests that valuation dispersion is meaningful even under a relatively simple mature-company framework. This supports the project’s core idea that single-point DCF outputs can create false precision.

## Key Uncertainty Drivers

For Hero MotoCorp, the main uncertainty drivers are:

1. two-wheeler demand recovery,
2. premiumisation and product mix,
3. EV transition risk,
4. competitive intensity,
5. EBIT margin sustainability,
6. WACC and terminal value assumptions,
7. reinvestment and working capital needs.

## Required Next Refinements

Before this company can be considered research-paper ready:

1. Reconcile all FY2025 numbers with the audited annual report.
2. Verify share count and net cash.
3. Build a detailed capex and working-capital schedule.
4. Refresh beta and WACC using date-consistent market data.
5. Add a valuation-date market price.
6. Calculate probability of undervaluation relative to that market price.
7. Add charts: valuation distribution, percentile bands, and sensitivity/tornado analysis.

## Research Boundary

This file is for education, research practice, and GitHub portfolio demonstration only. It is not investment advice, financial advice, or a buy/sell recommendation.
