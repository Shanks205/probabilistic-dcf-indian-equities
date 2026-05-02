# Probabilistic DCF Valuation of Selected Indian Listed Equities: A Monte Carlo FCFF Framework

## Abstract

This working paper develops a probabilistic discounted cash flow framework for a 12-company Indian listed-equity sample. The project applies free cash flow to firm valuation, scenario-based operating assumptions, WACC normalization, terminal value sensitivity, enterprise-value bridge reconciliation, and peer multiple triangulation. The purpose is to separate business quality from valuation-expectation risk. Rather than presenting a single target price, the study compares market price with a distribution of intrinsic value outcomes.

The sample covers businesses across autos, auto ancillaries, capital goods, metals, agrochemicals, industrial packaging, defence electronics, electricals, pharmaceuticals, and recycling. The key contribution is a reproducible GitHub-based research framework that combines annual-report evidence, probabilistic DCF modelling, external market-data refreshes, and relative valuation checks.

## 1. Introduction

Single-point valuation models often create false precision. This limitation is especially relevant in emerging markets where cyclicality, working-capital volatility, commodity exposure, policy risk, sector sentiment, order-book timing, and liquidity conditions can materially alter outcomes. A deterministic discounted cash flow model can be useful, but it may hide the range of plausible outcomes behind one apparently precise fair value.

This project applies a probabilistic FCFF framework to 12 selected Indian listed companies:

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

The central research question is:

```text
How does a probabilistic FCFF valuation framework change the interpretation of apparent undervaluation or overvaluation when compared with market price for selected Indian listed companies?
```

The paper deliberately avoids presenting its outputs as buy/sell recommendations. It treats valuation as a probability-weighted research process.

## 2. Data and Verification Framework

The project uses FY2024-25 annual reports as the primary financial evidence layer. Page-level mapping and source tracking are documented in:

```text
paper/source_maps/page_level_mapping_master_template.csv
paper/source_maps/all_companies_page_mapping_completion_notes.md
paper/source_maps/cash_debt_working_capital_reconciliation_notes.md
paper/source_maps/final_audit_grade_note_lock_v1.md
```

The evidence architecture separates four layers:

1. corporate overview and management KPI disclosures,
2. consolidated income statement and cash-flow data,
3. balance-sheet notes for cash, investments, debt, share capital, and working capital,
4. external market data including share price, market capitalization, enterprise value, P/B, and beta.

This separation is important because corporate-overview pages are useful for narrative, while valuation mechanics should rely on consolidated financial statements and notes where available.

## 3. Methodology

### 3.1 FCFF Valuation Framework

The valuation framework uses free cash flow to firm:

```text
FCFF = EBIT x (1 - tax rate) + depreciation and amortisation - capital expenditure - change in net working capital
```

Enterprise value is estimated by discounting forecast FCFF and terminal value at WACC. Equity value is then estimated after adjusting enterprise value for cash, investments, and debt.

### 3.2 Probabilistic Assumption Design

Instead of treating growth, margins, and reinvestment as fixed values, the model uses scenario ranges for:

```text
revenue growth
EBITDA margin
capital expenditure intensity
working-capital movement
terminal growth
WACC / cost of capital
```

The output is a valuation distribution rather than a single target price. This makes the framework better suited for comparing price attractiveness, downside risk, and assumption sensitivity.

### 3.3 Market Data and WACC

The market-data refresh layer is stored in:

```text
outputs/market_data/final_market_data_refresh_filled.csv
outputs/market_data/normalized_beta_wacc_review.csv
outputs/market_data/risk_free_rate_lock.md
```

The first-pass market-data refresh was completed for all 12 companies. The WACC review uses a draft India 10-year government bond yield assumption of 7.01% for sensitivity review. Raw market beta values were reviewed and, where they were unusually low or negative, normalized beta assumptions were documented.

### 3.4 Enterprise Value Bridge

Enterprise value is treated carefully because provider-reported EV can differ from annual-report reconstructed EV. The methodology separates:

```text
1. Yahoo Finance enterprise value
2. Annual-report reconstructed enterprise value
3. Manual-patched enterprise value where automated parsing was incomplete
```

The preferred reconstruction formula is:

```text
Enterprise value = market capitalization + gross debt - cash and cash equivalents - current investments treated as cash-like
```

The EV methodology and supporting tables are documented in:

```text
paper/ev_bridge_methodology_note.md
outputs/market_data/ev_bridge_review_priority.csv
outputs/market_data/manual_ev_bridge_reconciliation_v1.csv
outputs/market_data/manual_ev_bridge_recalculated_v1.csv
```

High-priority companies for EV bridge review include Hero MotoCorp, NALCO, Bharat Electronics, Polycab India, JB Chemicals and Pharmaceuticals, and Gravita India.

## 4. Final Audit-Grade Note-Lock Pass

A final high-priority note-lock pass was completed for Hero MotoCorp, NALCO, Bharat Electronics, and Gravita India. The note-lock file is:

```text
paper/source_maps/final_audit_grade_note_lock_v1.md
```

The audit-note status is:

| Company | Note-lock status | Remaining caveat |
|---|---|---|
| Hero MotoCorp | Substantially locked for cash-flow and investment-note evidence | Final model should decide treatment of associates and non-current investments versus cash-like current investments |
| NALCO | Debt lock complete | Cash/investment numeric lock still needs one final extraction if the paper requires full audit-grade precision |
| Bharat Electronics | Debt, share capital, and capex lock complete | Cash/investment numeric lock still needs one final extraction if the paper requires full audit-grade precision |
| Gravita India | Cash, debt, equity, and capital-management evidence substantially locked | Final model should define which financial assets are treated as cash-like |

This means the project is suitable for a pre-submission research packet, but the final SSRN version should retain a transparent caveat if NALCO and BEL cash/investment values are not fully locked.

## 5. Annual-Report Evidence Summary

The annual-report evidence layer now covers all 12 companies. Examples from the mapped evidence include:

- Hero MotoCorp reported FY25 revenue of Rs 40,756 crore, EBITDA of Rs 5,868 crore, and PAT of Rs 4,610 crore.
- Fiem Industries reported consolidated net sales of Rs 240,536.78 lakh, consolidated operating profit before finance cost/depreciation/exceptional items of Rs 32,219.66 lakh, and consolidated PAT after associate share of Rs 20,491.98 lakh.
- Triveni Turbine reported consolidated revenue from operations of Rs 20,058 million, EBITDA of Rs 5,177 million, and PAT of Rs 3,586 million.
- Time Technoplast reported consolidated revenue from operations of Rs 545,704.11 lakh and profit for the year of Rs 39,444.57 lakh.
- Bharat Electronics reported turnover of Rs 23,024 crore, EBITDA of Rs 6,768 crore, PAT of Rs 5,288 crore, and capex spend of Rs 908 crore.
- Polycab India reported consolidated revenue from operations of Rs 224,083 million and PAT of Rs 20,455.37 million.
- SJS Enterprises reported FY25 revenue from operations of Rs 7,605 million, EBITDA of Rs 2,032 million, PAT of Rs 1,188 million, and net cash of Rs 992 million.
- JB Chemicals and Pharmaceuticals reported FY25 operating revenue of Rs 391,798.86 lakh, PBT of Rs 88,739.16 lakh, and PAT of Rs 65,958.21 lakh.
- Gravita India reported consolidated revenue from operations of Rs 3,868.77 crore and PAT of Rs 312.90 crore.

These data are used as the baseline evidence layer for model assumptions and cross-company comparisons.

## 6. Relative Valuation Layer

The relative valuation layer has been upgraded from a template to an enriched peer table. The current peer files are:

```text
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
outputs/peer_tables/peer_multiple_ev_pb_summary_by_company.csv
outputs/peer_tables/peer_ev_pb_manual_gap_fill.csv
outputs/peer_tables/peer_ev_pb_enrichment_final_review.md
```

### 6.1 Peer Data Method

Peer multiples were constructed using two clearly labelled source families:

```text
Screener.in: peer universe, operating metrics, P/E, ROE, and ROCE
Yahoo Finance: enterprise value, P/B, and market-data enrichment
```

The enrichment layer achieved:

```text
Screener rows fetched: 47 / 47
Yahoo EV/PB rows fetched: 47 / 47
Yahoo EV populated: 46 / 47
Yahoo P/B populated: 47 / 47
True EV/Sales calculated: 42 / 47
True EV/EBITDA calculated: 42 / 47
```

The remaining automated gaps were filled manually for Siemens India, Bharat Dynamics, Data Patterns, Voltamp Transformers, and Bharat Bijlee. Those manual patches are documented in:

```text
outputs/peer_tables/peer_ev_pb_manual_gap_fill.csv
outputs/peer_tables/peer_ev_pb_manual_gap_fill_notes.md
```

### 6.2 Peer Median Summary

| Company | Median True EV/Sales | Median True EV/EBITDA | Median P/E | Median P/B | Median ROE | Median ROCE |
|---|---:|---:|---:|---:|---:|---:|
| Hero MotoCorp | 5.06 | 24.95 | 36.10 | 8.83 | 24.10 | 28.10 |
| Fiem Industries | 2.12 | 18.55 | 37.80 | 6.00 | 17.55 | 17.60 |
| Triveni Turbine | 11.04 | 60.02 | 82.45 | 14.60 | 17.95 | 23.05 |
| NALCO | 2.20 | 8.38 | 12.90 | 2.55 | 21.30 | 23.05 |
| Sharda Cropchem | 2.07 | 14.16 | 24.75 | 2.84 | 15.00 | 19.20 |
| Time Technoplast | 2.37 | 14.62 | 24.45 | 3.19 | 16.55 | 20.50 |
| Bharat Electronics | 8.72 | 30.86 | 49.60 | 10.57 | 20.25 | 26.30 |
| Polycab India | 2.71 | 28.79 | 40.10 | 7.56 | 17.50 | 23.10 |
| SJS Enterprises | 2.49 | 20.03 | 42.90 | 7.64 | 14.80 | 15.75 |
| Shilchar Technologies | 7.52 | 43.08 | 59.95 | 7.32 | 20.70 | 26.85 |
| JB Chemicals and Pharmaceuticals | 6.70 | 23.53 | 38.05 | 7.00 | 22.15 | 23.70 |
| Gravita India | 1.70 | 9.79 | 15.85 | 4.29 | 16.50 | 16.05 |

The peer layer should be read as a triangulation check, not as the primary valuation engine. The primary valuation method remains probabilistic FCFF.

## 7. Exhibits and Chart Status

The current draft exhibits are stored at:

```text
outputs/charts/median_fair_value_vs_market_price.png
outputs/charts/median_margin_of_safety.png
outputs/charts/valuation_gap_by_company.png
```

The chart-generation workflow exists and can be rerun after final EV and WACC assumptions are accepted. Because several EV bridge caveats remain open, the current charts should be labelled as pre-submission draft exhibits rather than final locked publication exhibits.

The first-pass interpretation is that several high-quality businesses appear expensive under conservative Monte Carlo DCF assumptions. This does not mean the businesses are weak. It means the market price may already discount stronger growth, higher margin durability, lower capital intensity, lower risk, or longer competitive advantage than the conservative model assumes.

The research therefore separates two questions:

```text
Is the business fundamentally strong?
Is the market price attractive relative to a conservative distribution of intrinsic values?
```

## 8. Limitations

This project remains a research framework rather than an investment recommendation. Important limitations include:

1. NALCO and Bharat Electronics still have cash/investment note-lock caveats if the standard required is full audit-grade numeric extraction.
2. Manual EV bridge calculations are draft where exact note extraction remains incomplete.
3. Peer multiples use a two-source method: Screener for operating metrics and Yahoo Finance for EV/P/B; this should be disclosed wherever the table is used.
4. Five peer rows were manually patched after automated parser gaps.
5. Market data may change materially before upload, so final SSRN submission should use a fresh market-data refresh.
6. Monte Carlo outputs depend on assumption design; results should be interpreted as scenario distributions, not objective truth.
7. The analysis does not constitute a valuation opinion, investment advice, or a buy/sell recommendation.

## 9. Conclusion

The project demonstrates how a probabilistic FCFF valuation framework can be applied to selected Indian listed equities across sectors. It improves upon single-point valuation by showing how fair value changes across operating, capital-intensity, and discount-rate assumptions.

The main conclusion is:

```text
A probabilistic valuation framework helps distinguish business quality from price attractiveness.
```

The relative valuation layer supports the framework by providing peer-context triangulation, while annual-report mapping and EV bridge notes improve evidence quality. The project is now suitable for a pre-submission SSRN packet. A final publication-ready upload should follow one last market-data refresh, chart rerun, PDF proofread, and final disclaimer check.

## References and Data Sources

This working paper uses company annual reports, Screener.in, Yahoo Finance, and project-generated valuation outputs. Key repository files are listed below.

### Company annual reports

- Hero MotoCorp Integrated / Annual Report FY2024-25.
- Fiem Industries Annual Report FY2024-25.
- Triveni Turbine Annual Report FY2024-25.
- National Aluminium Company Limited Annual Report FY2024-25.
- Sharda Cropchem Annual Report FY2024-25.
- Time Technoplast Annual Report FY2024-25.
- Bharat Electronics Integrated Annual Report FY2024-25.
- Polycab India Integrated Annual Report FY2024-25.
- SJS Enterprises Annual Report FY2024-25.
- Shilchar Technologies Annual Report FY2024-25.
- JB Chemicals and Pharmaceuticals Annual Report FY2024-25.
- Gravita India Annual Report FY2024-25.

### Market and peer data

- Screener.in company pages for peer operating metrics, P/E, ROE, and ROCE.
- Yahoo Finance market-data fields for market capitalization, enterprise value, P/B, and beta.
- India 10-year government bond yield assumption documented in `outputs/market_data/risk_free_rate_lock.md`.

### Repository evidence files

```text
paper/source_maps/page_level_mapping_master_template.csv
paper/source_maps/all_companies_page_mapping_completion_notes.md
paper/source_maps/final_audit_grade_note_lock_v1.md
paper/ev_bridge_methodology_note.md
paper/final_ssrn_manuscript_v3_pre_submission.md
outputs/market_data/final_market_data_refresh_filled.csv
outputs/market_data/normalized_beta_wacc_review.csv
outputs/market_data/manual_ev_bridge_recalculated_v1.csv
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
outputs/peer_tables/peer_multiple_ev_pb_summary_by_company.csv
outputs/peer_tables/peer_ev_pb_manual_gap_fill.csv
outputs/charts/median_fair_value_vs_market_price.png
outputs/charts/median_margin_of_safety.png
outputs/charts/valuation_gap_by_company.png
```

## Disclaimer

This paper is for educational and research purposes only. It is not investment advice, financial advice, a valuation opinion, or a buy/sell recommendation. The author may hold or not hold positions in securities discussed. Readers should conduct their own research and consult qualified professionals before making financial decisions.
