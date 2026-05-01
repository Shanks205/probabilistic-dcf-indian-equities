# From Screening to Probabilistic Intrinsic Value

## A Monte Carlo DCF Framework for Indian Equities

This repository develops a probabilistic discounted cash flow valuation framework for Indian listed companies. It converts deterministic FCFF valuation assumptions into Monte Carlo simulation inputs so that intrinsic value is treated as a distribution rather than a single fair-value estimate.

Traditional DCF valuation often produces one intrinsic value estimate based on fixed assumptions for revenue growth, operating margins, reinvestment, working capital, WACC, and terminal growth. This project treats those assumptions as uncertain and generates a fair-value range, downside/upside percentiles, and probability-based valuation interpretation.

## Current Project Status

```text
12 / 12 companies completed at Level 2 Final Draft
SSRN paper construction started
```

## Objective

The objective is to build a reproducible GitHub research project that can:

1. document sample selection using screening and analyst judgement,
2. build deterministic FCFF DCF models,
3. convert major valuation assumptions into probability-distribution ranges,
4. run Monte Carlo valuation simulations,
5. estimate fair-value ranges and downside/upside probabilities,
6. compare valuation uncertainty across different business models,
7. support an SSRN working paper after citation and data-reconciliation upgrades.

## Research Design

The project uses a 12-company Indian equity sample:

- 6 companies retained from an earlier Indian equity valuation framework for continuity.
- 6 companies added through fresh Screener-style fundamental screening for originality.

The project is not a stock recommendation system. The selected companies are used as research cases to study how valuation uncertainty behaves across mature, growth, cyclical, working-capital-sensitive, order-book-driven, high-ROCE, defensive, and commodity-linked businesses.

## Final 12-Company Sample

| # | Company | Ticker | Source Type | Valuation Archetype | Status |
|---:|---|---|---|---|---|
| 1 | Hero MotoCorp | HEROMOTOCO.NS | Retained | Mature auto cash-flow recovery | Level 2 Final Draft |
| 2 | Fiem Industries | FIEMIND.NS | Retained | Auto-component growth | Level 2 Final Draft |
| 3 | Triveni Turbine | TRITURBINE.NS | Retained | Capital goods / order-book conversion | Level 2 Final Draft |
| 4 | NALCO | NATIONALUM.NS | Retained | Cyclical commodity | Level 2 Final Draft |
| 5 | Sharda Cropchem | SHARDACROP.NS | Retained | Working-capital-sensitive agrochemical | Level 2 Final Draft |
| 6 | Time Technoplast | TIMETECHNO.NS | Retained | Industrial packaging / cash conversion | Level 2 Final Draft |
| 7 | Bharat Electronics | BEL.NS | Fresh Screen | Defence electronics / order book | Level 2 Final Draft |
| 8 | Polycab India | POLYCAB.NS | Fresh Screen | Quality compounder / cables and electricals | Level 2 Final Draft |
| 9 | SJS Enterprises | SJS.NS | Fresh Screen | Auto ancillary / premiumization | Level 2 Final Draft |
| 10 | Shilchar Technologies | SHILCTECH.NS | Fresh Screen | High-ROCE industrial growth | Level 2 Final Draft |
| 11 | JB Chemicals and Pharmaceuticals | JBCHEPHARM.NS | Fresh Screen | Stable pharma | Level 2 Final Draft |
| 12 | Gravita India | GRAVITA.NS | Fresh Screen | Recycling / commodity-linked industrial | Level 2 Final Draft |

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── data/
│   ├── company_master.csv
│   └── monte_carlo_distribution_template.csv
├── docs/
│   ├── sample_selection_protocol.md
│   └── valuation_methodology.md
├── src/
│   ├── dcf_model.py
│   └── monte_carlo_engine.py
├── scripts/
│   └── run_hero_motocorp_demo.py
├── outputs/
│   └── research_tracker/
│       ├── company_completion_tracker.csv
│       └── project_phase_status.md
├── paper/
│   ├── abstract.md
│   ├── working_paper_draft.md
│   └── methodology_appendix.md
└── companies/
    ├── hero_motocorp/
    ├── fiem_industries/
    ├── triveni_turbine/
    ├── nalco/
    ├── sharda_cropchem/
    ├── time_technoplast/
    ├── bharat_electronics/
    ├── polycab_india/
    ├── sjs_enterprises/
    ├── shilchar_technologies/
    ├── jb_chemicals_pharmaceuticals/
    └── gravita_india/
```

## Company-Level File Standard

Each Level 2 company folder is designed to include:

```text
company_readme.md
final_level2_inputs.csv
wacc_working.csv
dcf_output_summary.csv
monte_carlo_summary.csv
risk_matrix.md
sensitivity_summary.csv
peer_framework.md
peer_multiples_template.csv
final_level2_analysis.md
research_completion_audit.md
```

## Workflow

```text
Sample selection
→ Company-level historical baseline
→ Deterministic FCFF DCF
→ WACC working
→ Scenario and sensitivity assumptions
→ Monte Carlo valuation distribution
→ Risk matrix
→ Peer framework
→ Company-level final analysis
→ Completion audit
→ Consolidated SSRN working paper draft
```

## Interpretation Principle

The project separates:

```text
Business quality
```

from:

```text
Valuation-expectation risk
```

A company can be operationally strong and still trade above conservative cash-flow-supported valuation ranges if the market price already discounts optimistic growth, margin, risk, or terminal-value assumptions.

## SSRN Development Status

The SSRN phase has started with:

```text
paper/abstract.md
paper/working_paper_draft.md
paper/methodology_appendix.md
```

Before SSRN upload, the project still requires:

1. annual-report page-level citation reconciliation,
2. refreshed market data using one consistent date,
3. populated peer multiple tables,
4. chart generation,
5. formal literature review,
6. final academic editing,
7. compliance-style disclaimer review.

## Disclaimer

This repository is for education, research practice, and portfolio demonstration only. It does not provide investment advice, financial advice, or buy/sell recommendations. All valuation outputs depend on assumptions and must be independently verified before real investment use.
