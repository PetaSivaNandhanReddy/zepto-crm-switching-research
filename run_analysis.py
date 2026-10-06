"""Run the whole pipeline: python run_analysis.py"""
import sys, traceback
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from src import config as C
for d in [C.CLEAN_DIR, C.PROC_DIR, C.TABLES, C.FIGS, C.STATS, C.REPORTS, C.DOCS, C.LIT, C.SEC]:
    d.mkdir(parents=True, exist_ok=True)
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
from src import (data_cleaning, reliability_analysis, hypothesis_testing, regression, descriptive_analysis,
                 subgroup_analysis, former_never_analysis, secondary_analysis, variable_mapping, visualization, synthesis, report_builder, measurement_diagnostics, verification, consistency_check)


def main():
    step = "start"
    try:
        step = "cleaning"; df, cur, frm, nev, sc, sf, log = data_cleaning.run()
        step = "codebook"; variable_mapping.run(df)
        step = "reliability"; d, rel, info, eig, load, nfac = reliability_analysis.run(cur)
        step = "descriptive"; descriptive_analysis.run(df, d)
        step = "hypotheses"; hypothesis_testing.run(d)
        step = "regression"; regression.run(d)
        step = "measurement diagnostics"; measurement_diagnostics.run(d)
        step = "subgroups"; subgroup_analysis.run(d)
        step = "former"; former_never_analysis.run_former(frm, sc)
        step = "never"; former_never_analysis.run_never(nev)
        step = "secondary"; secondary_analysis.run({})
        step = "figures"; visualization.run(df, d)
        step = "synthesis"; synthesis.run()
        step = "verification"; verification.run()
        step = "report"; report_builder.run()
        step = "consistency"; consistency_check.run()
    except Exception:
        print(f"PIPELINE FAILED at step: {step}")
        traceback.print_exc()
        sys.exit(1)
    print("Pipeline completed. n:", len(df), "current", len(cur), "former", len(frm), "never", len(nev))


if __name__ == "__main__":
    main()
