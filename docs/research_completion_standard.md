# Research Completion Standard

## Purpose

This document defines what "complete research" means for this GitHub project before it can be converted into an SSRN working paper.

The current project should not be treated as complete merely because a DCF model and Monte Carlo summary exist. A company is only complete when the research pack includes verified data, transparent assumptions, source logs, valuation outputs, sensitivity analysis, and audit notes.

## Company Research Completion Levels

### Level 0 — Not Started

No company-specific research folder exists.

### Level 1 — Model Scaffold Complete

The company has a folder with preliminary files:

- company README
- preliminary historical financials
- source log
- assumption log
- assumptions template
- deterministic DCF output
- Monte Carlo summary
- valuation note

This level is useful for GitHub structure but is not enough for SSRN-level research.

### Level 2 — Public-Source Research Complete

A company reaches Level 2 only after:

1. annual report and/or official filings are reviewed,
2. historical financials are reconciled,
3. revenue, EBIT, EBITDA, tax, D&A, capex, working capital, cash, debt, and share count are checked,
4. source log includes official and public-source references,
5. assumption log explains bear/base/bull inputs,
6. DCF output is regenerated using checked inputs,
7. Monte Carlo output is regenerated using checked distributions,
8. sensitivity analysis is added,
9. risk matrix is added,
10. peer sanity-check framework is added,
11. research completion audit is added.

### Level 3 — SSRN-Ready Research Pack

A company reaches Level 3 only after:

1. valuation date is locked,
2. market price is locked from a date-consistent source,
3. beta regression and WACC are refreshed,
4. shares outstanding and net debt/cash are verified,
5. probability of undervaluation/overvaluation is calculated,
6. charts and tables are finalized,
7. limitations are clearly documented,
8. the company section is ready to be included in a working paper.

## Required Company Files

Each company folder should eventually contain:

```text
company_readme.md
historical_financials.csv
source_log.md
assumption_log.md
assumptions_template.csv
dcf_output_summary.csv
monte_carlo_summary.csv
sensitivity_summary.csv
risk_matrix.md
peer_framework.md
valuation_note.md
research_completion_audit.md
```

## Research Principle

No company should be marked complete unless the research pack explains:

```text
What data was used
Where it came from
What assumptions were made
Why those assumptions were reasonable
What the valuation output shows
What remains uncertain
What must be verified before publication
```

## Important Boundary

This GitHub project is for education, research practice, and portfolio demonstration. It does not provide investment advice or buy/sell recommendations.
