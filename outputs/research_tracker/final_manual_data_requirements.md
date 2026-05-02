# Final Manual Data Requirements Before SSRN-Ready Status

## Purpose

This file records the remaining items that cannot be honestly marked complete without verified source data.

## What Has Been Completed

- Level 2 company research for all 12 companies
- SSRN draft structure
- Citation maps for all 12 companies
- Uploaded annual-report mapping for Triveni Turbine, Polycab India, and JB Chemicals and Pharmaceuticals
- SSRN next-steps pipeline execution and artifact review
- Market-data first pass for all 12 companies
- Draft beta/WACC normalization table
- Enterprise-value bridge priority table
- Draft chart generation
- Draft risk-free rate lock at 7.01% for the May 2026 market-data review date

## Items Still Requiring Verified Data

### 1. Peer Multiples

Peer multiples cannot be marked as verified until numerical values are collected from a consistent source and date. The current peer file is a structure/template, not a final verified peer table.

Required fields include:

- market capitalization
- enterprise value
- revenue
- EBITDA
- PAT
- EV/Sales
- EV/EBITDA
- P/E
- P/B where meaningful
- ROCE/ROE where meaningful
- source and data date

### 2. Remaining Annual-Report Page Mapping

Exact page-level mapping is still pending for the companies whose FY2024-25 annual reports are not uploaded into the chat/review environment:

- Hero MotoCorp
- Fiem Industries
- NALCO
- Sharda Cropchem
- Time Technoplast
- Bharat Electronics
- SJS Enterprises
- Shilchar Technologies
- Gravita India

The repo already contains scripts and manifests to support this step, but exact page mapping requires the actual PDF files or successful GitHub Actions artifacts.

### 3. Enterprise-Value Bridge Reconciliation

The high-priority EV bridge companies are:

- Hero MotoCorp
- NALCO
- Bharat Electronics
- Polycab India
- JB Chemicals and Pharmaceuticals

Polycab and JB Pharma have annual-report evidence mapped. Hero, NALCO and BEL still require annual-report page-level balance-sheet mapping before final EV bridge lock.

### 4. Final Manuscript Update

The final manuscript should not be marked SSRN-ready until the above data items are verified and the paper is rewritten with formal citations and exhibit references.

## Practical Next Step

To complete the remaining annual-report mapping, upload the FY2024-25 annual reports for the 9 pending companies listed above, or run the Annual Report Verification GitHub Actions workflow and provide the output artifact.

## Research Boundary

This file is part of the SSRN verification workflow. It is not investment advice, financial advice, or a buy/sell recommendation.
