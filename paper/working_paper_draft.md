# From Screening to Probabilistic Intrinsic Value

## A Monte Carlo DCF Framework for Indian Equities

### Working Paper Draft for SSRN Development

## Abstract

This study develops a probabilistic discounted cash flow framework for selected Indian listed equities by converting deterministic FCFF valuation assumptions into Monte Carlo simulation inputs. Traditional DCF models often present a single intrinsic value estimate, even though valuation is highly sensitive to assumptions about growth, operating margins, reinvestment, working capital, cost of capital, and terminal value. This project treats intrinsic value as a distribution rather than a point estimate.

The research applies a 12-company Indian equity sample covering mature auto, auto components, capital goods, commodities, agrochemicals, industrial packaging, defence electronics, cables and electricals, auto ancillary premiumization, transformer manufacturing, branded pharmaceuticals, and recycling businesses. Each company is modeled using a Level 2 public-source research standard consisting of company-level operating baselines, deterministic FCFF valuation, WACC working, Monte Carlo valuation output, sensitivity analysis, risk matrices, peer frameworks, and completion audits.

The preliminary GitHub-stage results show that several high-quality or high-growth businesses may still trade above conservative cash-flow-supported valuation ranges. The framework therefore separates business quality from valuation-expectation risk. The study contributes a reproducible research workflow for equity valuation in emerging markets and provides a foundation for a later SSRN working paper after full annual-report reconciliation, formal citations, refreshed market data, and chart generation.

## 1. Introduction

Equity valuation is often presented as a precise estimate of fair value, but most intrinsic-value models are driven by uncertain assumptions. A small change in revenue growth, operating margin, working-capital intensity, reinvestment, WACC, or terminal growth can materially change the final fair value estimate. This issue is especially important in emerging markets where business cycles, commodity exposure, working-capital volatility, market liquidity, and changing investor expectations can create wide valuation ranges.

This project develops a reproducible valuation workflow for Indian listed companies using a probabilistic FCFF DCF framework. Instead of treating valuation as a single number, the framework treats intrinsic value as a distribution. The method starts with a deterministic DCF model and then converts major assumptions into ranges suitable for Monte Carlo simulation.

The central research question is:

```text
How does valuation uncertainty differ across Indian listed companies with different business models, and how far are market prices from conservative probabilistic intrinsic-value ranges?
```

The project is designed for GitHub reproducibility first and SSRN paper development second. The current version should be treated as a Level 2 public-source draft, not as a fully audited institutional research report.

## 2. Research Motivation

Traditional DCF analysis has three limitations:

1. It often produces a single intrinsic value estimate even though the inputs are uncertain.
2. It can hide the difference between business quality and valuation attractiveness.
3. It may not clearly show what happens when assumptions move across realistic ranges.

A probabilistic DCF framework helps address these limitations by generating a range of possible fair values. This is particularly useful for companies that appear fundamentally strong but trade at premium valuations. In such cases, the key question is not whether the business is good. The key question is whether the current market price already discounts very optimistic assumptions.

## 3. Sample Design

The research uses a 12-company Indian equity sample. The sample is intentionally diversified across valuation archetypes rather than designed as a statistically representative index sample.

| # | Company | Ticker | Source Type | Valuation Archetype |
|---:|---|---|---|---|
| 1 | Hero MotoCorp | HEROMOTOCO.NS | Retained | Mature auto cash-flow recovery |
| 2 | Fiem Industries | FIEMIND.NS | Retained | Auto-component growth |
| 3 | Triveni Turbine | TRITURBINE.NS | Retained | Capital goods / order-book conversion |
| 4 | NALCO | NATIONALUM.NS | Retained | Cyclical commodity |
| 5 | Sharda Cropchem | SHARDACROP.NS | Retained | Working-capital-sensitive agrochemical |
| 6 | Time Technoplast | TIMETECHNO.NS | Retained | Industrial packaging / cash conversion |
| 7 | Bharat Electronics | BEL.NS | Fresh Screen | Defence electronics / order book |
| 8 | Polycab India | POLYCAB.NS | Fresh Screen | Quality compounder / cables and electricals |
| 9 | SJS Enterprises | SJS.NS | Fresh Screen | Auto ancillary / premiumization |
| 10 | Shilchar Technologies | SHILCTECH.NS | Fresh Screen | High-ROCE industrial growth |
| 11 | JB Chemicals and Pharmaceuticals | JBCHEPHARM.NS | Fresh Screen | Stable pharma |
| 12 | Gravita India | GRAVITA.NS | Fresh Screen | Recycling / commodity-linked industrial |

## 4. Methodology

The valuation process follows these steps:

1. Select company and assign valuation archetype.
2. Build FY2025 public-source operating baseline.
3. Estimate normalized operating assumptions.
4. Build deterministic FCFF DCF model.
5. Estimate WACC using risk-free rate, beta, equity risk premium, and company-specific risk premium.
6. Convert core assumptions into downside, base, and upside ranges.
7. Run Monte Carlo valuation simulation.
8. Compare simulated fair-value distribution with market price.
9. Create company-level risk matrix.
10. Document peer framework and SSRN upgrade requirements.

## 5. FCFF Valuation Framework

The project uses a free cash flow to firm approach. The simplified operating model follows this structure:

```text
Revenue
× EBIT margin
= EBIT
× (1 - tax rate)
= NOPAT
+ Depreciation and amortisation
- Capital expenditure
- Change in net working capital
= FCFF
```

The explicit forecast period is followed by a terminal value based on the Gordon growth framework:

```text
Terminal value = FCFF_next_year / (WACC - terminal growth)
```

Enterprise value is calculated as the present value of explicit FCFF plus the present value of terminal value. Equity value is then estimated by adjusting enterprise value for net cash or net debt.

## 6. Monte Carlo Framework

The Monte Carlo framework treats valuation assumptions as uncertain variables rather than fixed inputs. The major variables are:

- revenue growth,
- EBIT margin,
- tax rate,
- depreciation / sales,
- capex / sales,
- net working capital / sales,
- WACC,
- terminal growth.

For each company, the simulation generates a distribution of fair values per share. The outputs include:

- mean fair value,
- median fair value,
- 5th percentile,
- 25th percentile,
- 75th percentile,
- 95th percentile,
- probability that intrinsic value is above market price,
- probability that intrinsic value is below market price,
- median margin of safety.

## 7. Cross-Company Interpretation

The Level 2 company files show that many companies in the sample have market prices above conservative DCF-derived fair-value ranges. This does not automatically imply that these businesses are poor investments or that market prices must fall. Instead, it indicates that the market may be discounting stronger assumptions than the current conservative model, such as longer growth runways, higher margin durability, better working-capital performance, lower risk perception, or superior competitive advantages.

The research contribution is the distinction between:

```text
Business quality
```

and:

```text
Valuation-expectation risk
```

A company can be operationally strong and still appear expensive under a conservative probabilistic FCFF framework.

## 8. Level 2 Research Status

All 12 companies now have Level 2 Final Draft folders. Each company includes a company README, final input file, WACC working, deterministic DCF output, Monte Carlo summary, risk matrix, sensitivity summary, peer framework, peer multiples template, final Level 2 analysis, and research completion audit.

## 9. Limitations

This draft has important limitations:

1. The current version uses public-source baseline data and analyst assumptions.
2. Exact annual-report page citations have not yet been added.
3. Market prices, market capitalization, enterprise value, and beta should be refreshed using a consistent data date.
4. Peer multiples templates have not yet been populated with final numerical peer data.
5. Monte Carlo distributions are framework-driven and require further validation.
6. This project is not a stock recommendation system.
7. The analysis is not audited, verified, or compliance-reviewed.

## 10. SSRN Upgrade Plan

Before SSRN upload, the following work should be completed:

1. Reconcile every company input with annual-report pages or exchange filings.
2. Add formal citations and references.
3. Create cross-company comparison tables.
4. Generate charts for deterministic DCF output, Monte Carlo distribution, and sensitivity analysis.
5. Write the literature review.
6. Convert GitHub company notes into academic prose.
7. Add methodology appendix and data appendix.
8. Add reproducibility instructions.
9. Add final disclaimers.

## 11. Conclusion

This project builds a structured Monte Carlo DCF framework for Indian equities. The current Level 2 GitHub version demonstrates how probabilistic valuation can be used to compare intrinsic-value uncertainty across different business models. The framework helps separate business quality from valuation expectations and provides a foundation for a later SSRN-ready working paper.

## Disclaimer

This working paper draft is for education, research practice, and portfolio demonstration only. It is not investment advice, financial advice, or a buy/sell recommendation.
