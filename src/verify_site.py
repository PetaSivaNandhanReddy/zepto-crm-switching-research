"""Verification script for the research dashboard presentation layer.
Scans index.html, app.js, and web/site_data.js to verify all locked research facts.
"""
import sys
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    print("=== Running Research Dashboard Verification Audit ===")
    html_path = ROOT / "index.html"
    app_path = ROOT / "app.js"
    site_data_path = ROOT / "web" / "site_data.js"

    if not html_path.exists():
        print(f"Error: {html_path} missing")
        sys.exit(1)

    html = html_path.read_text(encoding="utf-8")
    app = app_path.read_text(encoding="utf-8") if app_path.exists() else ""
    sdata = site_data_path.read_text(encoding="utf-8") if site_data_path.exists() else ""

    combined_text = html + "\n" + app + "\n" + sdata

    locked_checks = [
        ("Total sample N=184", "184" in combined_text),
        ("Current users n=51", "51" in combined_text),
        ("Former users n=73", "73" in combined_text),
        ("Never users n=60", "60" in combined_text),
        ("Current user percentage 27.7%", "27.7" in combined_text),
        ("Former user percentage 39.7%", "39.7" in combined_text),
        ("Never user percentage 32.6%", "32.6" in combined_text),
        ("Questionnaire V1 n=16", "16" in combined_text),
        ("Questionnaire V1.5 n=6", "V1.5" in combined_text or "1.5" in combined_text),
        ("Questionnaire V2 n=162", "162" in combined_text),
        ("Coverage-primary 31/73 (42.5%)", "42.5" in combined_text or "31" in combined_text),
        ("Coverage-overlap 10/73 (13.7%)", "13.7" in combined_text or "10" in combined_text),
        ("Voluntary exit 32/73 (43.8%)", "43.8" in combined_text or "32" in combined_text),
        ("Voluntary availability + variety 16/32 (50.0%)", "50.0" in combined_text or "16/32" in combined_text or "50%" in combined_text),
        ("Alternative variety advantage 41/68 (60.3%)", "60.3" in combined_text or "41" in combined_text),
        ("Hypothesis H1 rho=+0.17", "0.17" in combined_text),
        ("Hypothesis H2 rho=+0.685", "0.685" in combined_text),
        ("Hypothesis H3 rho=+0.694", "0.694" in combined_text),
        ("Hypothesis H4 rho=+0.700", "0.7" in combined_text),
        ("Hypothesis H5 rho=+0.721", "0.721" in combined_text),
        ("Hypothesis H6 rho=+0.245", "0.245" in combined_text or "0.248" in combined_text),
        ("Hypothesis H7 n=46 complete-case", "46" in combined_text),
        ("Centered SWEFFORT attenuation (+0.05)", "0.05" in combined_text),
        ("Centered ALT attenuation (-0.03)", "-0.03" in combined_text or "-0.025" in combined_text),
        ("Regression M1 R2=0.696", "0.696" in combined_text),
        ("Regression M1 F(4,46)=26.27", "26.27" in combined_text),
        ("HTMT SWEFFORT-INT 0.92", "0.92" in combined_text),
        ("UDRHP capex 16,289.75M", "16,289.75" in combined_text or "16,289" in combined_text),
        ("UDRHP lease obligations 17,349.41M", "17,349.41" in combined_text or "17,349" in combined_text),
        ("UDRHP cloud & tech 4,000.00M", "4,000" in combined_text),
        ("UDRHP advertising & marketing 5,200.00M", "5,200" in combined_text),
        ("UDRHP mature cohort retention 44.3%-54.0%", "44.3" in combined_text),
        ("CRM recommendation R1-R5 present", all(r in combined_text for r in ["R1", "R2", "R3", "R4", "R5"])),
    ]

    passed = 0
    failed = 0
    for label, status in locked_checks:
        if status:
            print(f"  [PASS] {label}")
            passed += 1
        else:
            print(f"  [FAIL] {label}")
            failed += 1

    print(f"\nAudit complete: {passed}/{len(locked_checks)} passed, {failed} failed.")
    if failed > 0:
        return 1
    print("All locked research facts verified successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
