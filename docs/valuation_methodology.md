# Valuation Methodology

## Overview

This project uses a free cash flow to the firm (FCFF) discounted cash flow framework. The deterministic DCF output is then converted into a probabilistic valuation distribution using Monte Carlo simulation.

## FCFF Formula

```text
FCFF = EBIT × (1 - Tax Rate)
       + Depreciation and Amortization
       - Capital Expenditure
       - Change in Net Working Capital
```

FCFF is used because it values cash flows available to all providers of capital before financing decisions.

## Enterprise Value

Enterprise value is calculated as:

```text
Enterprise Value = Present Value of Explicit Forecast FCFF
                 + Present Value of Terminal Value
```

## Terminal Value

The terminal value is estimated using the Gordon growth method:

```text
Terminal Value = Final Year FCFF × (1 + Terminal Growth) / (WACC - Terminal Growth)
```

Terminal growth must remain conservative because terminal value often dominates DCF output.

## Equity Value

```text
Equity Value = Enterprise Value - Net Debt
```

Where:

```text
Net Debt = Total Debt - Cash and Cash Equivalents
```

## Fair Value Per Share

```text
Fair Value Per Share = Equity Value / Shares Outstanding
```

## Monte Carlo Simulation

Instead of using only one assumption set, the model simulates a range of assumptions for key drivers:

- revenue growth,
- EBIT margin,
- tax rate,
- capex as % of sales,
- working capital as % of sales,
- WACC,
- terminal growth.

Each simulation produces one intrinsic value estimate. Thousands of simulations produce a full valuation distribution.

## Main Output Metrics

The simulation will report:

| Metric | Meaning |
|---|---|
| Mean value | Average simulated fair value |
| Median value | Central fair value estimate |
| 5th percentile | Severe downside valuation |
| 25th percentile | Conservative valuation |
| 75th percentile | Upside valuation |
| 95th percentile | Strong upside valuation |
| Probability of undervaluation | % of simulations above current market price |
| Probability of overvaluation | % of simulations below current market price |

## Research Boundary

The model is designed for education and reproducible valuation research. It does not issue investment recommendations.
