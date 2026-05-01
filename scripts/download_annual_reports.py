"""Download FY2025 annual-report PDFs listed in the manifest.

This script downloads only rows marked as direct_pdf and ready_for_download in
`data/verification/annual_report_download_manifest.csv`.

Rows marked pending_manual_pdf_url are intentionally skipped until a direct PDF
URL is added to the manifest. This avoids saving HTML pages as fake PDFs.

Usage:
    python scripts/download_annual_reports.py

Output:
    data/annual_reports/*.pdf
    outputs/verification/annual_report_download_log.csv
"""

from __future__ import annotations

from pathlib import Path
import time
import urllib.request
import urllib.error

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "verification" / "annual_report_download_manifest.csv"
LOG_PATH = ROOT / "outputs" / "verification" / "annual_report_download_log.csv"


def is_pdf_file(path: Path) -> bool:
    if not path.exists() or path.stat().st_size < 1024:
        return False
    with path.open("rb") as file:
        return file.read(4) == b"%PDF"


def download_file(url: str, destination: Path) -> tuple[str, str]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 research-script annual-report-downloader",
            "Accept": "application/pdf,text/html,*/*",
        },
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            content = response.read()
            content_type = response.headers.get("content-type", "")
    except urllib.error.HTTPError as exc:
        return "failed", f"HTTP error {exc.code}: {exc.reason}"
    except urllib.error.URLError as exc:
        return "failed", f"URL error: {exc.reason}"
    except TimeoutError:
        return "failed", "timeout"

    destination.write_bytes(content)

    if not is_pdf_file(destination):
        destination.unlink(missing_ok=True)
        return "failed", f"Downloaded content is not a valid PDF; content-type={content_type}"

    return "downloaded", f"valid PDF; bytes={len(content)}; content-type={content_type}"


def main() -> None:
    manifest = pd.read_csv(MANIFEST_PATH)
    rows: list[dict[str, str]] = []

    for _, row in manifest.iterrows():
        company = str(row["company"])
        ticker = str(row["ticker"])
        url = str(row["annual_report_source_url"])
        source_type = str(row["source_type"])
        status = str(row["download_status"])
        local_path = ROOT / str(row["preferred_local_pdf_path"])

        if source_type != "direct_pdf" or status != "ready_for_download":
            rows.append(
                {
                    "company": company,
                    "ticker": ticker,
                    "local_path": str(local_path.relative_to(ROOT)),
                    "result": "skipped",
                    "details": "Manifest row is not a confirmed direct PDF URL",
                }
            )
            continue

        if is_pdf_file(local_path):
            rows.append(
                {
                    "company": company,
                    "ticker": ticker,
                    "local_path": str(local_path.relative_to(ROOT)),
                    "result": "already_exists",
                    "details": "Valid PDF already present",
                }
            )
            continue

        result, details = download_file(url, local_path)
        rows.append(
            {
                "company": company,
                "ticker": ticker,
                "local_path": str(local_path.relative_to(ROOT)),
                "result": result,
                "details": details,
            }
        )
        time.sleep(1)

    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(LOG_PATH, index=False)
    print(f"Download log saved to {LOG_PATH}")


if __name__ == "__main__":
    main()
