# Hero MotoCorp Market Input Log

## Purpose

This file defines the market inputs required before Hero MotoCorp can become Level 2 / Level 3 research-ready.

The current GitHub model uses public-source operating financials and placeholder valuation assumptions. Market inputs are not yet locked.

## Required Market Inputs

| Input | Required Source | Current Status | Research Use |
|---|---|---|---|
| Valuation date | Project-defined date | Pending | Required to lock market price and peer multiples |
| Current market price | NSE/BSE or reliable market-data source | Pending | Required for probability of undervaluation/overvaluation |
| Market capitalization | NSE/BSE or reliable market-data source | Pending | Used for sanity check against DCF equity value |
| Enterprise value | Market cap + debt - cash | Pending | Used for market-implied EV/EBITDA comparison |
| Shares outstanding | Annual report / exchange filings | Pending | Required for fair value per share |
| Cash and investments | Annual report balance sheet | Pending | Required for net cash / net debt |
| Borrowings | Annual report balance sheet | Pending | Required for net cash / net debt and WACC weights |
| Risk-free rate | India 10-year government bond yield on valuation date | Pending | Required for cost of equity |
| Equity risk premium | Damodaran / India ERP source / documented assumption | Pending | Required for cost of equity |
| Beta | Regression vs Nifty 50 / relevant benchmark | Pending | Required for WACC refresh |
| Cost of debt | Finance cost / average debt or market borrowing estimate | Pending | Required for WACC refresh |
| Tax rate | Normalized effective tax rate | Public-source baseline added | Required for after-tax debt cost and FCFF |

## WACC Refresh Framework

```text
Cost of Equity = Risk-free Rate + Beta × Equity Risk Premium + Company-Specific Risk Premium

After-tax Cost of Debt = Pre-tax Cost of Debt × (1 - Tax Rate)

WACC = Cost of Equity × Equity Weight + After-tax Cost of Debt × Debt Weight
```

## Research Boundary

No probability of undervaluation should be calculated until the market price is locked on a single valuation date.

## Next Action

After official annual-report reconciliation, lock the valuation date and refresh market inputs.
