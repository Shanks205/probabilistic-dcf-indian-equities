# All Companies Page-Level Mapping Completion Notes

## Purpose

This file records the first final pass of page-level annual-report mapping after all 12 FY2024-25 annual reports became available in the review environment.

## Current Status

All 12 annual reports are now available and the page-level mapping master table has been updated at:

```text
paper/source_maps/page_level_mapping_master_template.csv
```

## What Was Completed

The mapping now covers all 12 companies:

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

For each company, the table now identifies page/section evidence for the major valuation inputs where available:

```text
revenue
EBITDA / operating profit
finance cost
depreciation and amortisation
profit before tax
tax expense
profit after tax
capex / PPE purchase candidate
cash and investments candidate
debt / borrowings candidate
working-capital candidate
share capital / shares outstanding candidate
```

## Mapping Confidence Categories

| Category | Meaning |
|---|---|
| Substantially mapped | Key operating and P&L values are mapped; final balance-sheet note lock may still be needed |
| Uploaded and pending detailed extraction | Annual report is available but some financial-statement pages still need deeper extraction |
| Final note lock pending | Core figures are mapped, but final SSRN paper should still lock exact financial-statement note pages for cash/debt/share count |

## Companies with Strongest Current Mapping

| Company | Reason |
|---|---|
| Polycab India | Operating data, P&L, capex, cash, borrowings and share count already substantially mapped |
| JB Chemicals and Pharmaceuticals | Operating data, P&L, capex, cash/current investments, borrowings and share capital mapped |
| Bharat Electronics | Financial performance table, capex, debt-equity and share-count evidence mapped |
| Time Technoplast | Directors' Report and consolidated P&L mapped |
| Fiem Industries | Directors' Report financial table mapped |
| Gravita India | Board Report and segment table mapped |

## Items Still Requiring Final Audit-Grade Line Lock

The current mapping is sufficient for the research draft and internal reconciliation layer. Before final SSRN upload, the following should still be checked one final time:

```text
1. Exact consolidated balance-sheet note pages for cash/investments/debt for Hero, NALCO, Sharda, Time, BEL, SJS, Shilchar and Gravita.
2. Exact share-capital/share-count note pages for Hero, Fiem, NALCO, Sharda, Time, Shilchar and Gravita.
3. Final cash-flow capex/PPE purchase lines for Fiem, NALCO, Sharda, Time, SJS, Shilchar and Gravita.
4. Final enterprise-value bridge for cash-heavy companies.
```

## Important Research Boundary

This mapping is a research verification layer. It is not investment advice, financial advice, or a buy/sell recommendation.
