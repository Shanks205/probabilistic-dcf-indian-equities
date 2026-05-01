# From Screening to Probabilistic Intrinsic Value

## A Monte Carlo DCF Framework for Indian Equities

This repository develops a probabilistic discounted cash flow valuation framework for Indian listed companies. It extends a public-source equity valuation workflow by converting deterministic DCF assumptions into probability distributions using Monte Carlo simulation.

Traditional DCF valuation often produces a single intrinsic value estimate based on fixed assumptions for revenue growth, operating margins, reinvestment, working capital, WACC, and terminal growth. This project treats valuation as uncertain and generates a distribution of intrinsic values instead of one exact fair value.

## Objective

The objective is to build a reproducible GitHub project that can:

1. document sample selection using screening and analyst judgement,
2. build deterministic FCFF DCF models,
3. convert major assumptions into probability distributions,
4. run Monte Carlo valuation simulations,
5. estimate fair value ranges and downside/upside probabilities,
6. compare valuation uncertainty across different business models,
7. later support an SSRN research paper.

## Research Design

The project uses a 12-company Indian equity sample:

- 6 companies retained from the earlier Indian equity valuation framework for continuity.
- 6 companies added through fresh Screener-style fundamental screening for originality.

The project is not a stock recommendation system. The selected companies are used as research cases to study how valuation uncertainty behaves across mature, growth, cyclical, working-capital-sensitive, order-book-driven, and high-ROCE companies.

## Final 12-Company Sample

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
└── companies/
    └── hero_motocorp/
        ├── company_readme.md
        └── assumptions_template.csv
```

## First Company

The first company is **Hero MotoCorp**. It is used as the initial clean implementation case because it is a mature operating company with relatively clearer FCFF DCF logic than highly cyclical, refining, or product-cycle-driven companies.

## Workflow

```text
Sample selection
→ Company-level historical analysis
→ Deterministic FCFF DCF
→ Scenario assumptions
→ Monte Carlo distributions
→ Simulation output
→ Sensitivity analysis
→ Company-level valuation report
→ Consolidated cross-company comparison
```

## Current Status

```text
Project stage: GitHub setup started
Company 1: Hero MotoCorp setup started
SSRN paper: not started yet
```

## Disclaimer

This repository is for education, research practice, and portfolio demonstration only. It does not provide investment advice, financial advice, or buy/sell recommendations. All valuation outputs depend on assumptions and must be independently verified before real investment use.
