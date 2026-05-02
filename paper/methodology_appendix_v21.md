# Methodology Appendix V2.1

## Purpose

This appendix strengthens Paper 1 before starting Paper 2. It documents the Monte Carlo assumption design, WACC components, terminal-value logic, and a first EV reconciliation pilot using Bharat Electronics.

## A. Monte Carlo Assumption Design

The simulation framework converts key valuation drivers into bounded assumption ranges. Each company is modelled using revenue growth, EBITDA margin, capital expenditure intensity, working-capital movement, WACC, and terminal growth.

| Input variable | Typical distribution design | Reason for inclusion |
|---|---|---|
| Revenue growth | Triangular or bounded normal distribution | Captures demand, pricing, cyclicality, order-book conversion, and sector growth uncertainty |
| EBITDA margin | Triangular distribution around conservative/base/upside margins | Captures operating leverage, input-cost pressure, pricing power, and scale benefits |
| Capex intensity | Bounded range as % of revenue | Links growth to reinvestment requirement and asset intensity |
| Working-capital change | Sector-specific bounded range | Important for defence, agrochemicals, industrials, and commodity-linked companies |
| WACC | Scenario range around normalized beta and risk-free-rate assumptions | Captures discount-rate uncertainty and beta instability |
| Terminal growth | Low bounded range below or near long-run nominal growth | Prevents terminal value from dominating the output unrealistically |

## B. WACC Components

The WACC layer should be treated as a normalized research assumption rather than a mechanically accepted market-data output.

| Component | Current treatment | Future improvement |
|---|---|---|
| Risk-free rate | India 10-year government bond yield assumption documented in repository | Refresh on final upload date and cite exact source/date |
| Beta | Raw beta reviewed; normalized beta used where raw beta was unstable | Estimate rolling beta using consistent index and lookback window |
| Equity risk premium | Applied as a market-level assumption | Test India ERP and emerging-market ERP sensitivity |
| Cost of debt | Low relevance for net-cash companies; relevant for leveraged names | Use company-specific borrowing cost from finance-cost/debt schedule where meaningful |
| Tax rate | Based on effective or normalized tax assumptions | Use marginal tax-rate sensitivity for stable mature companies |

## C. Terminal-Value Discipline

Terminal value is treated as a major source of valuation risk. The model uses conservative terminal-growth assumptions and sensitivity checks because small changes in terminal growth and WACC can dominate fair-value estimates.

| Company archetype | Terminal-growth treatment | Reason |
|---|---|---|
| Quality compounder | Moderate but bounded terminal growth | Higher reinvestment durability and brand/scale advantages may support longer growth runway |
| Defence/order-book business | Conservative-to-moderate terminal growth | Order book supports medium-term growth, but policy and execution risk remain |
| Commodity/cyclical business | Low terminal growth | Cycle normalization and margin reversion risk are material |
| Working-capital-sensitive business | Conservative terminal value | Cash conversion uncertainty reduces terminal confidence |

## D. Worked EV Reconciliation Pilot: Bharat Electronics

Bharat Electronics was selected as the first pilot because it is a large, cash-rich defence electronics company. The objective was to test whether provider-reported enterprise value materially differs from annual-report reconstructed enterprise value.

| BEL item | Amount | Source / interpretation |
|---|---:|---|
| Cash and cash equivalents | Rs 713.45 crore | FY2024-25 annual-report lock |
| Bank balances other than cash and cash equivalents | Rs 8,831.65 crore | FY2024-25 annual-report lock |
| Borrowings | Nil | FY2024-25 annual-report lock |
| Conservative net cash | Rs 9,545.10 crore | Cash + bank balances - borrowings |
| StockAnalysis current market cap | Approx. Rs 327,113 crore | NSE:BEL statistics, April 2026 |
| StockAnalysis current enterprise value | Approx. Rs 319,072 crore | NSE:BEL statistics, April 2026 |
| Screener market cap | Rs 327,185 crore | Screener BEL consolidated page, April 2026 |
| Annual-report reconstructed EV using Screener market cap | Rs 317,639.90 crore | Screener market cap - annual-report conservative net cash |

## E. Pilot Result

The BEL pilot should not be overstated. Provider enterprise value appears reasonably close to annual-report reconstructed EV when using comparable current market-cap data. The difference between StockAnalysis EV and a Screener-market-cap-based reconstructed EV is approximately Rs 1,432 crore, or around 0.45% of provider EV. This is not a large distortion.

Therefore, BEL alone is not a green-light proof for Paper 2. It is a useful validation case showing that provider EV can be reasonably accurate for some large, well-covered companies.

## F. Decision Rule for Paper 2

| Pilot outcome | Interpretation | Action |
|---|---|---|
| Average absolute deviation < 5% | Weak evidence of provider EV distortion | Do not expand unless sector-specific exceptions are strong |
| Average absolute deviation 5-10% | Moderate evidence | Continue only if distortion affects valuation multiples materially |
| Average absolute deviation 10-30% | Strong evidence | Expand to 50-80 companies with a defined sampling frame |
| Sector-specific outliers > 30% | Potentially publishable finding | Investigate drivers, but avoid scope creep |

## G. Forward-Return Testing

A forward-return test of probabilistic margin of safety is valuable but should not be attempted until point-in-time data are available. Without point-in-time annual reports, historical provider snapshots, filing dates, and delisted-company coverage, a backtest can suffer from look-ahead bias and survivorship bias.
