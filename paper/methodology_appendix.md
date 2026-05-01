# Methodology Appendix

## Purpose

This appendix documents the research workflow used in the GitHub-stage Monte Carlo DCF project. It is intended to support later conversion into an SSRN-ready methodology section.

## Company-Level Workflow

Each company is processed through the same Level 2 workflow:

1. Define valuation archetype.
2. Create company README.
3. Build FY2025 operating baseline.
4. Estimate normalized FCFF assumptions.
5. Build WACC working.
6. Generate deterministic DCF output.
7. Generate Monte Carlo valuation summary.
8. Create sensitivity summary.
9. Create business-risk matrix.
10. Create peer framework.
11. Create peer multiples template.
12. Write final Level 2 analysis note.
13. Add research completion audit.
14. Update research tracker.

## FCFF Model

The project uses a simplified FCFF approach:

```text
Revenue
× EBIT margin
= EBIT
× (1 - tax rate)
= NOPAT
+ Depreciation and amortisation
- Capital expenditure
- Change in net working capital
= Free cash flow to firm
```

## WACC Framework

The WACC framework uses:

```text
Cost of equity = risk-free rate + beta × equity risk premium + company-specific risk premium
```

For low-debt companies, the project uses a cost-of-equity-style WACC as the practical discount-rate anchor. For companies with greater commodity or execution risk, a higher company-specific risk premium is applied.

## Monte Carlo Variables

The Monte Carlo simulation framework focuses on the following variables:

| Variable | Reason for Inclusion |
|---|---|
| Revenue growth | Drives scale and future FCFF |
| EBIT margin | Captures profitability and operating leverage |
| Tax rate | Converts EBIT to NOPAT |
| Depreciation / sales | Links operating asset base to cash-flow add-back |
| Capex / sales | Captures reinvestment requirements |
| NWC / sales | Captures cash absorbed by receivables, inventory, and payables |
| WACC | Major present-value driver |
| Terminal growth | Major terminal-value driver |

## Output Metrics

Each company includes:

| Output | Meaning |
|---|---|
| Deterministic fair value per share | Base-case FCFF valuation output |
| Mean simulated fair value | Average of Monte Carlo fair-value distribution |
| Median simulated fair value | Central fair-value estimate |
| 5th percentile | Severe downside valuation estimate |
| 25th percentile | Conservative valuation estimate |
| 75th percentile | Upside valuation estimate |
| 95th percentile | Strong upside valuation estimate |
| Probability value above market price | Share of simulations above market price |
| Median margin of safety | Median fair value divided by market price minus one |

## Interpretation Framework

The project does not classify stocks as buy or sell recommendations. Instead, it classifies the relationship between conservative intrinsic-value distributions and market prices.

The key interpretation principle is:

```text
A strong business can still have high valuation-expectation risk if the market price already discounts optimistic assumptions.
```

## Current Level 2 Limitation

The Level 2 GitHub version is not a fully institutional-grade research report. It still requires:

1. exact annual-report page citations,
2. formal source reconciliation,
3. refreshed market data date,
4. populated peer-multiple tables,
5. chart generation,
6. academic literature review,
7. compliance-style disclaimer and review.
