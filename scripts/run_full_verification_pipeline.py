"""Run the full SSRN verification pipeline locally.

This script chains the current automated verification steps:

1. Download direct-PDF annual reports listed in the manifest.
2. Scan downloaded PDFs for candidate page references.
3. Build a compact status report showing what is ready and what is still pending.

Usage:
    python scripts/run_full_verification_pipeline.py

Outputs:
    outputs/verification/annual_report_download_log.csv
    outputs/verification/annual_report_page_candidates.csv
    outputs/verification/verification_pipeline_status.md
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DOWNLOAD_LOG = ROOT / "outputs" / "verification" / "annual_report_download_log.csv"
PAGE_CANDIDATES = ROOT / "outputs" / "verification" / "annual_report_page_candidates.csv"
STATUS_REPORT = ROOT / "outputs" / "verification" / "verification_pipeline_status.md"
MANIFEST = ROOT / "data" / "verification" / "annual_report_download_manifest.csv"


def run_step(command: list[str]) -> None:
    print("Running:", " ".join(command))
    subprocess.run(command, cwd=ROOT, check=True)


def build_status_report() -> None:
    manifest = pd.read_csv(MANIFEST)
    direct_ready = manifest[manifest["download_status"] == "ready_for_download"].shape[0]
    pending_direct = manifest[manifest["download_status"] != "ready_for_download"].shape[0]

    download_summary = "Download log not created."
    if DOWNLOAD_LOG.exists():
        log = pd.read_csv(DOWNLOAD_LOG)
        download_summary = log["result"].value_counts(dropna=False).to_string()

    candidate_summary = "Candidate page map not created."
    if PAGE_CANDIDATES.exists():
        candidates = pd.read_csv(PAGE_CANDIDATES)
        candidate_summary = (
            candidates.groupby("company")["data_item"]
            .count()
            .sort_values(ascending=False)
            .to_string()
        )

    report = f"""# Verification Pipeline Status

## Pipeline Result

The local verification pipeline has been executed.

## Annual Report Manifest Status

```text
Direct PDF rows ready for download: {direct_ready}
Rows still requiring direct PDF confirmation: {pending_direct}
```

## Download Log Summary

```text
{download_summary}
```

## Candidate Page Mapping Summary

```text
{candidate_summary}
```

## Important Interpretation

Candidate pages are not final citations. They are machine-generated candidates that must be manually reviewed before the SSRN paper is marked ready.

## Remaining SSRN Gates

```text
[ ] Confirm missing direct PDF URLs
[ ] Review annual_report_page_candidates.csv manually
[ ] Fill page_level_mapping_master_template.csv with confirmed page numbers
[ ] Refresh market data using one common date
[ ] Populate peer multiple table
[ ] Generate final charts
[ ] Rewrite final SSRN manuscript with formal citations
```
"""
    STATUS_REPORT.parent.mkdir(parents=True, exist_ok=True)
    STATUS_REPORT.write_text(report, encoding="utf-8")
    print(f"Saved status report to {STATUS_REPORT}")


def main() -> None:
    run_step([sys.executable, "scripts/download_annual_reports.py"])
    run_step([sys.executable, "scripts/verify_annual_report_pages.py"])
    build_status_report()


if __name__ == "__main__":
    main()
