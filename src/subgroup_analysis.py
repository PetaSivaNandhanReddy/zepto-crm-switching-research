"""Segment/profile differences in switching intention (current users) - limited, pre-declared tests."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C
from .stats_utils import mann_whitney, holm, spearman_boot


def run(d: pd.DataFrame):
    rows = []
    def add(label, base_n_note, res, kind, extra=None):
        r = dict(comparison=label, test=kind, note=base_n_note); r.update(res)
        if extra: r.update(extra)
        rows.append(r)
    a = d.loc[d.age_18_24 == 1, "INT"]; b = d.loc[d.age_18_24 == 0, "INT"]
    add("INT: age 18-24 vs 25+", "", mann_whitney(a, b), "Mann-Whitney U")
    a = d.loc[d.is_student == 1, "INT"]; b = d.loc[d.is_student == 0, "INT"]
    add("INT: student vs non-student", "", mann_whitney(a, b), "Mann-Whitney U")
    m = d.dropna(subset=["metro"])
    add("INT: metro vs non-metro (location not asked in V1)", "n limited by structural missingness",
        mann_whitney(m.loc[m.metro == 1, "INT"], m.loc[m.metro == 0, "INT"]), "Mann-Whitney U")
    sp = spearman_boot(d["spend_ord"], d["INT"]); add("INT ~ monthly spend (ordinal)", "n limited by structural missingness", dict(n1=sp["n"], rho=sp["rho"], p=sp["p"], ci_boot_low=sp["ci_boot_low"], ci_boot_high=sp["ci_boot_high"]), "Spearman")
    sp = spearman_boot(d["freq_ord"], d["INT"]); add("INT ~ QC frequency (ordinal)", "", dict(n1=sp["n"], rho=sp["rho"], p=sp["p"], ci_boot_low=sp["ci_boot_low"], ci_boot_high=sp["ci_boot_high"]), "Spearman")
    t = pd.DataFrame(rows)
    t["p_holm_5tests"] = holm(t.p.values)
    t.to_csv(C.TABLES / "table15_segment_findings_current_users.csv", index=False)
    # cell sizes for transparency
    cells = pd.concat([d.age_group.value_counts().rename("age"), d.occupation.value_counts().rename("occupation"),
                       d.location_type.value_counts().rename("location")], axis=1)
    cells.to_csv(C.STATS / "segment_cell_sizes_current.csv")
    return t
