# Zepto switching-behaviour analysis (reproducible pipeline)

## Run in VS Code
1. Install Python 3.10+ and open this folder in VS Code.
2. Terminal: `python -m venv .venv`, then activate it (Windows: `.venv\Scripts\activate`; macOS/Linux: `source .venv/bin/activate`).
3. `pip install -r requirements.txt`
4. `python run_analysis.py`

The run ends with an independent verification step (recomputes key results from the raw CSV) and a consistency check; it stops with an error if either fails.

Outputs: `outputs/tables`, `outputs/figures`, `outputs/statistical_results`, `outputs/reports/final_report.md`, `documentation/*`, `data/cleaned`, `data/processed`, `secondary_data`, `literature`.

The raw CSV in `data/raw` is never modified. Literature and secondary-source files are curated records of what was actually retrieved (with verification levels), not regenerated from the web.
