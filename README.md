# From Screening to Probabilistic Intrinsic Value

## A Monte Carlo DCF Framework for Indian Equities

This repository develops a probabilistic discounted cash flow valuation framework for Indian listed companies. It converts deterministic FCFF valuation assumptions into Monte Carlo simulation inputs so that intrinsic value is treated as a distribution rather than a single fair-value estimate.

Traditional DCF valuation often produces one intrinsic value estimate based on fixed assumptions for revenue growth, operating margins, reinvestment, working capital, WACC, and terminal growth. This project treats those assumptions as uncertain and generates a fair-value range, downside/upside percentiles, and probability-based valuation interpretation.

## Current Project Status

```text
12 / 12 companies completed at Level 2 Final Draft
All FY2024-25 annual reports uploaded and reviewed
Page-level annual-report mapping first final pass complete
Market-data first pass complete
Peer EV/PB enrichment complete with manual gap-fill notes
Enterprise-value bridge methodology complete
Final SSRN manuscript v2 created
Draft SSRN PDF packet created locally for review
Official SSRN-ready tag: Not yet; final proofing and final chart rerun still pending
```

## Latest Manuscript Files

```text
paper/final_ssrn_manuscript_v2.md
paper/ev_bridge_methodology_note.md
paper/source_maps/final_audit_grade_note_lock_v1.md
outputs/research_tracker/final_ssrn_packet_status.md
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
├── docs/
├── src/
├── scripts/
├── outputs/
│   ├── charts/
│   ├── market_data/
│   ├── peer_tables/
│   └── research_tracker/
├── paper/
│   ├── final_ssrn_manuscript_v2.md
│   ├── ev_bridge_methodology_note.md
│   └── source_maps/
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

## Key Verification Layers

```text
Annual-report mapping:
paper/source_maps/page_level_mapping_master_template.csv
paper/source_maps/all_companies_page_mapping_completion_notes.md
paper/source_maps/final_audit_grade_note_lock_v1.md

Market data and WACC:
outputs/market_data/final_market_data_refresh_filled.csv
outputs/market_data/normalized_beta_wacc_review.csv
outputs/market_data/risk_free_rate_lock.md
outputs/market_data/manual_ev_bridge_recalculated_v1.csv

Peer valuation:
outputs/peer_tables/peer_multiple_refresh_ev_pb_enriched.csv
outputs/peer_tables/peer_multiple_ev_pb_summary_by_company.csv
outputs/peer_tables/peer_ev_pb_manual_gap_fill.csv
outputs/peer_tables/peer_ev_pb_enrichment_final_review.md
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
→ Annual-report citation mapping
→ Market-data refresh
→ Peer EV/PB enrichment
→ Final SSRN manuscript v2
→ Draft SSRN PDF packet
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

## Finalization Notes

The project is close to SSRN-ready but should not yet be labelled as finally uploaded or officially publication-ready. Remaining quality-control items are:

1. decide whether to accept current note-lock caveats or perform one more extraction pass for NALCO and BEL cash/investment notes,
2. rerun final charts after final EV/WACC assumptions are accepted,
3. add formal references/citations section if needed for SSRN formatting,
4. final PDF proofread and disclaimer review.

## Disclaimer

This repository is for education, research practice, and portfolio demonstration only. It does not provide investment advice, financial advice, valuation advice, or buy/sell recommendations. All valuation outputs depend on assumptions and must be independently verified before real investment use.
