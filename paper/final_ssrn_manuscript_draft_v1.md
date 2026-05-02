# Probabilistic DCF Valuation of Selected Indian Listed Equities: A Monte Carlo FCFF Framework

## Abstract

This working paper develops a probabilistic discounted cash flow framework for a 12-company Indian listed-equity sample. The project applies free cash flow to firm valuation, scenario-based operating assumptions, WACC normalization, terminal value sensitivity and Monte Carlo-style fair-value distributions to separate business quality from valuation-expectation risk. The sample includes companies across autos, auto ancillaries, capital goods, metals, agrochemicals, electricals, defence electronics, pharmaceuticals and recycling. The main research contribution is not a single point-estimate target price, but a structured framework for comparing market price against a distribution of intrinsic value outcomes.

## 1. Introduction

Traditional equity valuation frequently relies on single-point DCF estimates or relative valuation multiples. These approaches are useful but can create false precision, especially in emerging markets where cyclicality, working-capital volatility, commodity exposure, order-book timing, policy risk and market sentiment can materially change outcomes. This project therefore uses a probabilistic valuation framework in which operating assumptions are expressed as ranges rather than fixed values.

The research sample covers 12 Indian listed companies:

1. Hero MotoCorp
2. Fiem Industries
3. Triveni Turbine
4. NALCO
5. Sharda Cropchem
6. Time Technoplast
7. Bharat Electronics
8. Polycab India
9. SJS Enterprises
10. Shilchar Technologies
11. JB Chemicals and Pharmaceuticals
12. Gravita India

The core research question is:

```text
How does a probabilistic FCFF valuation framework change the interpretation of apparent undervaluation or overvaluation when compared with market price for selected Indian listed companies?
```

## 2. Data and Source Verification

The project uses FY2024-25 annual reports as the core financial evidence layer. Annual-report page mapping has been documented in:

```text
paper/source_maps/page_level_mapping_master_template.csv
paper/source_maps/all_companies_page_mapping_completion_notes.md
```

The source verification process separates four evidence tiers:

1. management and corporate overview KPIs,
2. consolidated income statement and cash-flow data,
3. balance-sheet cash, debt and share-capital notes,
4. external market-data fields such as share price, market capitalization, enterprise value and beta.

This distinction is important because corporate overview pages are useful for narrative and quick reference, while final valuation mechanics should rely on consolidated financial statements and notes wherever possible.

## 3. Methodology

### 3.1 FCFF Valuation Framework

The project uses a free cash flow to firm approach:

```text
FCFF = EBIT × (1 - tax rate) + depreciation and amortisation - capital expenditure - change in net working capital
```

Enterprise value is estimated by discounting forecast FCFF and terminal value at the weighted average cost of capital. Equity value is then estimated by adjusting enterprise value for cash, investments and debt.

### 3.2 Probabilistic Assumptions

Instead of relying on a single growth rate, margin or reinvestment assumption, the model uses scenario ranges for:

```text
revenue growth
EBITDA margin
capital expenditure intensity
working-capital movement
terminal growth
WACC / cost of capital
```

The objective is to estimate a valuation range and probability distribution rather than one definitive fair value.

### 3.3 Market Data and WACC

The market-data layer was refreshed using a common timestamp from the SSRN next-steps pipeline. The first-pass output is stored in:

```text
outputs/market_data/final_market_data_refresh_filled.csv
```

The beta/WACC review is stored in:

```text
outputs/market_data/normalized_beta_wacc_review.csv
```

Some raw beta values were considered unsuitable for final WACC use because they were unusually low or negative. For such companies, normalized beta assumptions were documented rather than mechanically accepting unstable market beta values.

### 3.4 Enterprise Value Bridge

The project distinguishes between Yahoo Finance enterprise value and manually reconstructed enterprise value. For cash-heavy or debt-definition-sensitive companies, manual EV is preferred:

```text
Enterprise value = market capitalization + gross debt - cash and cash equivalents - current investments treated as cash-like
```

The EV bridge review is documented in:

```text
outputs/market_data/manual_ev_bridge_reconciliation_v1.csv
outputs/market_data/manual_ev_bridge_recalculated_v1.csv
```

## 4. Evidence Summary

The annual-report mapping now covers the full 12-company sample.

Examples include:

- Hero MotoCorp reported FY25 revenue of Rs 40,756 crore, EBITDA of Rs 5,868 crore and PAT of Rs 4,610 crore.
- Fiem Industries reported consolidated net sales of Rs 240,536.78 lakh and consolidated PAT after associate share of Rs 20,491.98 lakh.
- Time Technoplast reported consolidated revenue from operations of Rs 545,704.11 lakh and profit for the year of Rs 39,444.57 lakh.
- Bharat Electronics reported turnover of Rs 23,024 crore, EBITDA of Rs 6,768 crore, PAT of Rs 5,288 crore and capex spend of Rs 908 crore.
- SJS Enterprises reported FY25 revenue from operations of Rs 7,605 million, EBITDA of Rs 2,032 million, PAT of Rs 1,188 million and net cash of Rs 992 million.
- Gravita India reported consolidated revenue from operations of Rs 3,868.77 crore and PAT of Rs 312.90 crore.

## 5. Draft Results and Interpretation

The generated chart outputs are stored at:

```text
outputs/charts/median_fair_value_vs_market_price.png
outputs/charts/median_margin_of_safety.png
outputs/charts/valuation_gap_by_company.png
```

The first-pass interpretation is that several high-quality businesses appear expensive under conservative Monte Carlo DCF assumptions. This does not mean the businesses are weak. It means the market price may already be discounting a combination of stronger growth, higher margin durability, lower risk, superior reinvestment economics or longer terminal quality than the conservative model assumes.

The framework therefore separates two different questions:

```text
Is the business fundamentally strong?
Is the market price attractive relative to a conservative distribution of intrinsic values?
```

This distinction is central to the paper.

## 6. Relative Valuation Layer

A peer multiple framework has been created but not yet treated as verified numerical evidence. The current files are:

```text
outputs/peer_tables/peer_multiple_refresh_expanded_template.csv
outputs/peer_tables/verified_peer_multiple_status_v1.csv
outputs/peer_tables/peer_multiple_source_plan.md
```

The paper should treat peer multiples as a secondary valuation check until a verified peer export is added from one consistent source and date.

## 7. Limitations

This project is a research framework, not an investment recommendation. Important limitations include:

1. The final peer multiple table still requires verified numerical values from a consistent source and date.
2. Some balance-sheet note pages require final audit-grade locking for cash, investments, borrowings and share capital.
3. Manual EV bridge calculations remain draft for companies where cash/debt note extraction is incomplete.
4. Market data may change materially before upload, so the market-data refresh should be rerun before final SSRN submission.
5. Monte Carlo valuation depends on assumption design; therefore, results should be interpreted as scenario distributions rather than objective truth.

## 8. Conclusion

This project demonstrates how a probabilistic FCFF valuation framework can be used to evaluate Indian listed equities across different sectors. The framework improves upon single-point valuation by showing valuation sensitivity across operating, capital intensity and discount-rate assumptions. The current evidence suggests that valuation-expectation risk is meaningful even for businesses with strong operating performance.

The project’s main conclusion is:

```text
A probabilistic valuation framework helps distinguish business quality from price attractiveness.
```

The next completion step is to finalize audit-grade balance-sheet note mapping, populate verified peer multiples from one consistent source/date and rerun the charts immediately before SSRN upload.

## Disclaimer

This paper is for educational and research purposes only. It is not investment advice, financial advice, a valuation opinion, or a buy/sell recommendation. The author may hold or not hold positions in securities discussed. Readers should conduct their own research and consult qualified professionals before making financial decisions.
