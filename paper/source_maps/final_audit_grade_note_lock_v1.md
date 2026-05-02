# Final Audit-Grade Balance-Sheet Note Lock V1

## Purpose

This file records the highest-priority balance-sheet and cash-flow evidence needed for the final research packet. The focus is on companies where cash, investments, borrowings, share capital or capex materially affect the enterprise-value bridge.

## Companies Reviewed

- Hero MotoCorp
- NALCO
- Bharat Electronics
- Gravita India

## Hero MotoCorp

| Item | FY2024-25 evidence | Source section |
|---|---:|---|
| Cash and cash equivalents | Rs 383.56 crore | Consolidated cash-flow statement |
| Current borrowings movement | Rs 456.76 crore current borrowings plus Rs 3.79 crore interest expense on financial liabilities | Consolidated cash-flow / financing-liability reconciliation |
| Capex / PPE and intangible cash outflow | Rs 856.63 crore | Consolidated cash-flow investing activities |
| Current investments | Approx. Rs 6,636.00 crore from current investment note categories | Investment note |
| Non-current investments | Material, including FVTPL / amortised-cost investments and associates | Investment note |

EV bridge treatment: use a manual EV bridge. Current investments and associates are material, so provider EV should not be used without reconciliation.

## NALCO

| Item | FY2024-25 evidence | Source section |
|---|---:|---|
| Cash and cash equivalents | Rs 121.40 crore | Consolidated balance sheet and Note 16.A |
| Bank balances other than cash and cash equivalents | Rs 5,305.33 crore | Consolidated balance sheet and Note 16.B |
| Deposit accounts with original maturity between 3-12 months | Rs 5,298.46 crore | Note 16.B |
| Earmarked balances with scheduled banks | Rs 6.87 crore | Note 16.B |
| Current investments / mutual funds | Rs 514.92 crore | Current investments note |
| Non-current investments in joint ventures | Rs 259.26 crore | Consolidated balance sheet investment note |
| Other non-current investments | Rs 0.03 crore | Consolidated balance sheet investment note |
| Current borrowings | Rs 124.22 crore | Borrowings note; liabilities towards bills discounted |
| Debt-equity ratio | Nil / no conventional long-term borrowings identified | Analytical ratio and balance-sheet review |

Conservative EV bridge treatment:

```text
Cash-like assets = cash and cash equivalents + other bank balances + current investments
                 = 121.40 + 5,305.33 + 514.92
                 = 5,941.65 crore

Net cash after current borrowings = 5,941.65 - 124.22
                                  = 5,817.43 crore
```

Broader financial-assets bridge including non-current investments:

```text
Broader financial assets = 5,941.65 + 259.29
                         = 6,200.94 crore

Broader net cash / financial assets after current borrowings = 6,200.94 - 124.22
                                                             = 6,076.72 crore
```

Recommended treatment: use the conservative cash-like bridge for the primary EV adjustment and disclose broader financial assets separately.

## Bharat Electronics

| Item | FY2024-25 evidence | Source section |
|---|---:|---|
| Cash and cash equivalents | Rs 71,345 lakh / Rs 713.45 crore | Consolidated balance sheet and cash-flow statement |
| Bank balances other than cash and cash equivalents | Rs 8,83,165 lakh / Rs 8,831.65 crore | Consolidated balance sheet |
| Non-current investments | Rs 58,161 lakh / Rs 581.61 crore | Consolidated balance sheet and Note 6 |
| Non-current borrowings | Nil | Consolidated balance sheet |
| Current borrowings | Nil | Consolidated balance sheet |
| Debt-equity ratio | Nil | Financial performance / ratio disclosure |
| Equity share capital | Rs 73,098 lakh | Standalone balance sheet |
| Capex | Rs 908 crore | Financial capital disclosure |
| Revenue from operations | Rs 23,65,801 lakh | Financial/operational performance disclosure |
| EBITDA | Rs 6,76,759 lakh | Financial/operational performance disclosure |
| PAT | Rs 5,28,825 lakh | Financial/operational performance disclosure |

Conservative EV bridge treatment:

```text
Cash-like assets = cash and cash equivalents + bank balances other than cash and cash equivalents
                 = 713.45 + 8,831.65
                 = 9,545.10 crore

Borrowings = 0.00 crore

Net cash = 9,545.10 crore
```

Broader financial-assets bridge including non-current investments:

```text
Broader financial assets = 9,545.10 + 581.61
                         = 10,126.71 crore

Borrowings = 0.00 crore

Broader net financial assets = 10,126.71 crore
```

Recommended treatment: use the conservative cash-like bridge for the primary EV adjustment and disclose non-current investments separately.

## Gravita India

| Item | FY2024-25 evidence | Source section |
|---|---:|---|
| Cash and cash equivalents | Rs 94.61 crore | Consolidated cash-flow statement |
| Bank balances other than cash and equivalents | Rs 312.66 crore | Financial instruments note |
| Investments | Rs 170.79 crore amortised cost plus Rs 357.15 crore FVTPL | Financial instruments note |
| Non-current borrowings | Rs 190.19 crore | Borrowings note / capital management table |
| Current borrowings | Rs 92.14 crore | Borrowings note / capital management table |
| Total debt | Rs 282.33 crore | Capital management table |
| Equity share capital | Rs 14.76 crore | Capital management table |
| Planned capex | Rs 1,500 crore by FY28 | Capex discipline section |

EV bridge treatment: use annual-report reconstruction because the capital structure changed materially during the year. The final model should disclose which financial assets are treated as cash-like.

## Remaining Note-Lock Risk

| Company | Remaining issue |
|---|---|
| Hero MotoCorp | Decide treatment of associates and non-current investments versus cash-like current investments |
| Gravita India | Decide whether all financial investments and bank balances are cash-like or only selected categories |

The previously open NALCO and Bharat Electronics cash/investment note gaps have now been numerically locked.

## Status

```text
Hero MotoCorp: substantially locked for cash flow and investment note evidence
NALCO: cash/investment/debt note lock complete
Bharat Electronics: cash/investment/debt/share-capital/capex note lock complete
Gravita India: cash/debt/equity/capital management substantially locked
```
