# Cash, Debt and Working-Capital Reconciliation Notes

## Purpose

This file records the first reconciliation pass for cash, debt, capex and working-capital definitions for the uploaded FY2024-25 annual reports of Triveni Turbine, Polycab India and JB Chemicals and Pharmaceuticals.

The purpose is to separate annual-report evidence from model assumptions before the final SSRN-ready manuscript stage.

## Current Status

| Company | Reconciliation Status | SSRN Use Status |
|---|---|---|
| Triveni Turbine | Partial | Needs deeper note-level review for capex, cash, debt and working capital |
| Polycab India | Substantially reconciled | Needs final net-cash definition check versus model assumption |
| JB Chemicals and Pharmaceuticals | Substantially reconciled | Needs final net-cash definition check versus model assumption |

## Triveni Turbine

### What is already mapped

The uploaded FY2024-25 annual report provides a clear operating-performance bridge in the Directors' Report / financial performance section.

| Item | Annual-report mapping status | Evidence currently mapped |
|---|---|---|
| Revenue from operations | Mapped | Consolidated revenue from operations of Rs 20,058 million |
| EBITDA | Mapped | EBITDA / operating profit of Rs 5,177 million |
| Depreciation and amortisation | Mapped | Depreciation and amortisation of Rs 263 million |
| Finance cost | Mapped | Finance cost of Rs 29 million |
| PBT | Mapped | Profit before tax of Rs 4,886 million |
| Tax expense | Mapped | Tax expense of Rs 1,300 million |
| PAT | Mapped | Profit after tax of Rs 3,586 million |
| Share capital | Mapped candidate | BRSR / general disclosures provide paid-up capital candidate |

### Still requiring final review

| Item | Reason |
|---|---|
| Capex | Needs exact cash-flow statement line-item confirmation |
| Cash and investments | Needs balance-sheet and notes mapping |
| Borrowings / debt | Needs balance-sheet and notes mapping |
| Working capital | Needs receivables, inventories and payables note-level mapping |

### SSRN treatment

Triveni should remain marked as `Partial verified` until capex, cash, debt and working-capital pages are confirmed directly from the consolidated financial statement notes.

## Polycab India

### What is already mapped

Polycab's uploaded FY2024-25 integrated annual report provides strong mapping across operating results, P&L, cash flow, capex, debt and share capital.

| Item | Annual-report mapping status | Evidence currently mapped |
|---|---|---|
| Revenue from operations | Mapped | Rs 224,083 million |
| EBITDA | Mapped | Rs 29,602 million |
| Depreciation and amortisation | Mapped | Rs 2,981.03 million |
| Finance cost | Mapped | Rs 1,689.28 million |
| PBT | Mapped | Rs 27,008.45 million |
| Tax expense | Mapped | Rs 6,553.08 million |
| PAT | Mapped | Rs 20,455.37 million |
| Capex | Mapped | Approximately Rs 9,583 million; PPE additions schedule also mapped |
| Cash / net cash | Mapped | Net cash disclosure and cash/cash equivalents mapping available |
| Borrowings | Mapped | Borrowings note mapped |
| Working capital | Mapped candidate | Cash-flow working-capital movement and inventory note mapped |
| Shares outstanding | Mapped | 150,425,898 shares |

### Reconciliation caution

Polycab has both ordinary borrowings and working-capital-related acceptances / cash-credit style financing disclosures. For the final SSRN model, the equity-value bridge should clearly define whether net cash is based on:

1. cash and cash equivalents only,
2. cash plus current investments,
3. net cash disclosed by the company,
4. gross debt excluding acceptances,
5. gross debt including acceptances.

### SSRN treatment

Polycab can be treated as `Substantially mapped`, but not final SSRN-ready until the model's net-cash bridge is reconciled to the chosen annual-report definition.

## JB Chemicals and Pharmaceuticals

### What is already mapped

The uploaded FY2024-25 annual report provides the correct annual-report period and maps the key operating and financial statement items.

| Item | Annual-report mapping status | Evidence currently mapped |
|---|---|---|
| Revenue from operations | Mapped | Total operating revenue Rs 391,798.86 lakhs / revenue from operations Rs 391,799 lakhs |
| Operating EBITDA | Mapped | Operating EBITDA excluding ESOP cost Rs 108,674 lakhs; reported EBITDA Rs 103,184 lakhs |
| Depreciation and amortisation | Mapped | Rs 17,103.69 lakhs |
| Finance cost | Mapped | Rs 1,172.90 lakhs |
| PBT | Mapped | Rs 88,739.16 lakhs |
| Tax expense | Mapped | Rs 22,780.98 lakhs |
| PAT | Mapped | Rs 65,958.21 lakhs |
| Capex | Mapped | Purchase of PPE Rs 9,758.76 lakhs plus purchase of intangible assets Rs 2,271.85 lakhs |
| Cash and investments | Mapped | Cash and equivalents Rs 11,509.10 lakhs plus current investments Rs 31,710.85 lakhs |
| Borrowings | Mapped | Current borrowings Rs 1,380.38 lakhs; no non-current borrowings noted in mapped balance-sheet section |
| Working capital | Mapped candidate | Inventories, trade receivables, trade payables and movement in working capital mapped |
| Shares outstanding | Mapped | 155,677,208 shares / equity share capital Rs 1,556.77 lakhs |

### Reconciliation caution

The Level 2 model used a broad cash and investments proxy of Rs 689 crore and debt proxy of Rs 136 crore. The annual-report mapping suggests a more precise starting point should be constructed from:

```text
Cash and cash equivalents
+ current investments
- current borrowings
- any other debt-like obligations selected for the model
```

This means the final SSRN version should recalculate the JB Pharma equity bridge using annual-report definitions rather than the earlier Level 2 proxy.

### SSRN treatment

JB Pharma can be treated as `Substantially mapped`, but the final valuation model should be refreshed after reconciling cash, current investments and borrowings.

## Cross-Company Implication

The uploaded reports resolved the most difficult annual-report source gap. However, the following gates remain before final SSRN-ready status:

```text
[ ] Triveni note-level cash/debt/capex/working-capital mapping
[ ] Polycab net-cash bridge reconciliation
[ ] JB Pharma net-cash bridge reconciliation
[ ] Market-data refresh using one common data date
[ ] Peer-multiple refresh
[ ] Final DCF update if cash/debt/share-count values change materially
[ ] Final chart generation
[ ] Academic rewrite with citations
```

## Research Boundary

This file is part of the SSRN verification workflow and is not investment advice, financial advice, or a buy/sell recommendation.
