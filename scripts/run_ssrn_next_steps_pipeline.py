"""Run the next SSRN verification preparation steps.

This script chains the next pending non-destructive tasks after uploaded-report
mapping:

1. Refresh common-date market data using Yahoo Finance.
2. Build expanded peer-multiple template.
3. Generate cross-company charts from the consolidated summary.
4. Write a status report summarizing outputs and remaining manual review items.

Usage:
    python scripts/run_ssrn_next_steps_pipeline.py

Automation note:
    This file is included in the GitHub Actions path trigger for the SSRN
    Next Steps Pipeline workflow.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "outputs" / "research_tracker" / "ssrn_next_steps_pipeline_status.md"

COMMANDS = [
    [sys.executable, "scripts/refresh_market_data.py"],
    [sys.executable, "scripts/build_peer_multiple_template_expanded.py"],
    [sys.executable, "scripts/generate_cross_company_charts.py"],
]

EXPECTED_OUTPUTS = [
    "outputs/market_data/final_market_data_refresh_filled.csv",
    "outputs/market_data/market_data_refresh_status.md",
    "outputs/peer_tables/peer_multiple_refresh_expanded_template.csv",
    "outputs/charts/median_fair_value_vs_market_price.png",
    "outputs/charts/median_margin_of_safety.png",
    "outputs/charts/valuation_gap_by_company.png",
]


def run_command(command: list[str]) -> tuple[str, str]:
    process = subprocess.run(
        command,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    status = "success" if process.returncode == 0 else "failed"
    output = (process.stdout or "") + (process.stderr or "")
    return status, output.strip()


def main() -> None:
    rows = []
    for command in COMMANDS:
        status, output = run_command(command)
        rows.append((" ".join(command), status, output[:2000]))

    output_checks = []
    for rel_path in EXPECTED_OUTPUTS:
        path = ROOT / rel_path
        output_checks.append((rel_path, "exists" if path.exists() else "missing"))

    report_lines = [
        "# SSRN Next Steps Pipeline Status",
        "",
        "## Pipeline Steps",
        "",
        "| Command | Status | Notes |",
        "|---|---|---|",
    ]
    for command, status, output in rows:
        safe_output = output.replace("|", "/").replace("\n", "<br>") or "No output"
        report_lines.append(f"| `{command}` | {status} | {safe_output} |")

    report_lines.extend([
        "",
        "## Expected Output Checks",
        "",
        "| File | Status |",
        "|---|---|",
    ])
    for rel_path, status in output_checks:
        report_lines.append(f"| `{rel_path}` | {status} |")

    report_lines.extend([
        "",
        "## Remaining Manual Gates",
        "",
        "```text",
        "[ ] Review market data output and add India 10Y G-sec rate for the same date",
        "[ ] Decide whether to use Yahoo Finance EV or manually recalculated EV",
        "[ ] Fill peer multiples using verified data sources",
        "[ ] Finish annual-report page-level mapping for remaining companies",
        "[ ] Review generated charts and cite them in the paper draft",
        "[ ] Rewrite final SSRN manuscript with citations and limitations",
        "```",
        "",
        "## Research Boundary",
        "",
        "This pipeline prepares research outputs. It does not create investment advice or buy/sell recommendations.",
    ])

    STATUS.parent.mkdir(parents=True, exist_ok=True)
    STATUS.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Saved status report to {STATUS}")


if __name__ == "__main__":
    main()
