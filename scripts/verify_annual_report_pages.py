"""Annual-report page-mapping helper for SSRN verification.

This script searches locally saved FY2025 annual-report PDFs for key financial
statement terms and creates a candidate page-reference file. It does not replace
manual verification; it creates the first pass that must be reviewed before SSRN
publication.

Expected input files:
    data/verification/company_source_registry.csv
    data/annual_reports/<company>_fy2025.pdf

Output:
    outputs/verification/annual_report_page_candidates.csv

Usage:
    pip install pymupdf
    python scripts/verify_annual_report_pages.py
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyMuPDF is required for PDF scanning. Install with: pip install pymupdf"
    ) from exc

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "data" / "verification" / "company_source_registry.csv"
OUTPUT_PATH = ROOT / "outputs" / "verification" / "annual_report_page_candidates.csv"

SEARCH_TERMS = {
    "revenue_from_operations": [
        "Revenue from operations",
        "Net sales",
        "Income from operations",
        "Sale of products",
    ],
    "ebitda_or_operating_profit": [
        "EBITDA",
        "Operating profit",
        "Profit before finance cost",
        "Profit before depreciation",
    ],
    "depreciation_and_amortisation": [
        "Depreciation and amortisation",
        "Depreciation and amortization",
        "Depreciation",
    ],
    "finance_cost": ["Finance costs", "Finance cost", "Interest expense"],
    "pbt": ["Profit before tax", "PBT"],
    "tax_expense": ["Tax expense", "Current tax", "Deferred tax"],
    "pat": ["Profit after tax", "PAT", "Profit for the year"],
    "capex": [
        "Purchase of property, plant and equipment",
        "Purchase of PPE",
        "Capital expenditure",
        "Capital work-in-progress",
    ],
    "cash_and_investments": [
        "Cash and cash equivalents",
        "Bank balances",
        "Current investments",
        "Investments",
    ],
    "debt_or_borrowings": ["Borrowings", "Debt", "Lease liabilities"],
    "working_capital": ["Trade receivables", "Inventories", "Trade payables"],
    "shares_outstanding": ["Equity share capital", "Number of shares", "Paid-up equity"],
}


def normalize_text(text: str) -> str:
    return " ".join(text.replace("\n", " ").split()).lower()


def find_terms_in_pdf(pdf_path: Path, terms: Iterable[str]) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    with fitz.open(pdf_path) as doc:
        for page_index, page in enumerate(doc, start=1):
            text = normalize_text(page.get_text("text"))
            for term in terms:
                term_norm = term.lower()
                if term_norm in text:
                    location = text.find(term_norm)
                    snippet = text[max(0, location - 120) : location + 220]
                    findings.append(
                        {
                            "page_number_pdf_order": page_index,
                            "matched_term": term,
                            "snippet": snippet,
                        }
                    )
    return findings


def main() -> None:
    registry = pd.read_csv(REGISTRY_PATH)
    rows: list[dict[str, object]] = []

    for _, company in registry.iterrows():
        pdf_path = ROOT / str(company["annual_report_pdf_path"])
        if not pdf_path.exists():
            rows.append(
                {
                    "company": company["company"],
                    "ticker": company["ticker"],
                    "data_item": "PDF missing",
                    "candidate_page": "",
                    "matched_term": "",
                    "snippet": "",
                    "source_pdf": str(pdf_path.relative_to(ROOT)),
                    "verification_status": "PDF file not found; download official annual report first",
                }
            )
            continue

        for data_item, terms in SEARCH_TERMS.items():
            findings = find_terms_in_pdf(pdf_path, terms)
            if not findings:
                rows.append(
                    {
                        "company": company["company"],
                        "ticker": company["ticker"],
                        "data_item": data_item,
                        "candidate_page": "",
                        "matched_term": "",
                        "snippet": "",
                        "source_pdf": str(pdf_path.relative_to(ROOT)),
                        "verification_status": "No candidate found; manual review required",
                    }
                )
                continue

            # Keep first five candidate pages for manual review.
            for finding in findings[:5]:
                rows.append(
                    {
                        "company": company["company"],
                        "ticker": company["ticker"],
                        "data_item": data_item,
                        "candidate_page": finding["page_number_pdf_order"],
                        "matched_term": finding["matched_term"],
                        "snippet": finding["snippet"],
                        "source_pdf": str(pdf_path.relative_to(ROOT)),
                        "verification_status": "Candidate only; manually confirm page and line item",
                    }
                )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(OUTPUT_PATH, index=False)
    print(f"Saved candidate page map to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
