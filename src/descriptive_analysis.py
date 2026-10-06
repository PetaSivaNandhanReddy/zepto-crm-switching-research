"""Descriptive analysis: whole sample profile, groups, construct descriptives."""
import numpy as np
import pandas as pd
from . import config as C
from .stats_utils import freq_table, wilson_ci, perm_chi2, holm


def crosstab_pct(df, var, order=None):
    ct = pd.crosstab(df[var], df["group"])
    if order is not None:
        ct = ct.reindex(order).fillna(0).astype(int)
    ct = ct[[c for c in ["Current", "Former", "Never"] if c in ct.columns]]
    ct["All"] = ct.sum(axis=1)
    return ct


def run(df: pd.DataFrame, d_cur: pd.DataFrame):
    out = {}
    # Table 3 group distribution
    g = freq_table(df["group"], order=["Current", "Former", "Never"])
    g.to_csv(C.TABLES / "table03_user_groups.csv", index=False)
    v = freq_table(df["questionnaire_version"], order=["V1", "V1.5", "V2"])
    v.to_csv(C.TABLES / "table03b_questionnaire_versions.csv", index=False)
    pd.crosstab(df["questionnaire_version"], df["group"]).to_csv(C.TABLES / "table03c_version_by_group.csv")
    # Table 1 profile (all 184) with group columns
    prof = []
    for var, order, label in [("age_group", C.AGE_ORDER, "Age group"), ("occupation", None, "Occupation"),
                              ("location_type", None, "Location type (n=168)"), ("monthly_spend", C.SPEND_ORDER, "Monthly QC spend (n=168)")]:
        ct = crosstab_pct(df, var, order)
        ct.insert(0, "variable", label); ct.index.name = "category"
        prof.append(ct.reset_index())
    prof = pd.concat(prof)
    prof.to_csv(C.TABLES / "table01_respondent_profile.csv", index=False)
    # Table 2 usage
    use = []
    for var, order, label in [("qc_frequency", C.FREQ_ORDER[::-1], "QC frequency"), ("choice_factor", None, "Most important choice factor")]:
        ct = crosstab_pct(df, var, order); ct.insert(0, "variable", label); ct.index.name = "category"; use.append(ct.reset_index())
    plat = pd.DataFrame([{"category": c.replace("used_", ""), "n": int(df[c].sum()), "pct_of_184_with_Q1": 100 * df[c].sum() / df[c].notna().sum(),
                          "base_n": int(df[c].notna().sum())} for c in df.columns if c.startswith("used_")])
    pd.concat(use).to_csv(C.TABLES / "table02_usage_characteristics.csv", index=False)
    plat.to_csv(C.TABLES / "table02b_platforms_used.csv", index=False)
    # group x profile association tests
    tests = []
    for var, lab in [("age_group", "Age group"), ("occupation", "Occupation"), ("location_type", "Location type"),
                     ("monthly_spend", "Monthly spend"), ("qc_frequency", "QC frequency")]:
        r = perm_chi2(df[var], df["group"]); r["variable"] = lab; tests.append(r)
    t = pd.DataFrame(tests); t["p_perm_holm"] = holm(t.p_perm.values)
    t.to_csv(C.STATS / "group_by_profile_tests.csv", index=False)
    # Table 10 construct descriptives (current users)
    rows = []
    for name in ["INT", "INT1", "INT2", "INT3", "SAT", "SAT1", "SAT2", "PUSH_consider", "ALT", "VAR", "PROMO", "SWEFFORT", "FAM", "INERT", "PULL"]:
        s = d_cur[name].dropna()
        k = int((s >= 4).sum() if name in C.CURRENT_LIKERT else (s >= 3.5).sum())
        lo, hi = wilson_ci(k, len(s))
        sd = s.std(ddof=1)
        rows.append(dict(variable=name, n=len(s), mean=s.mean(), sd=sd, ci95_low=s.mean() - 1.96 * sd / np.sqrt(len(s)) if len(s) > 1 else np.nan,
                         ci95_high=s.mean() + 1.96 * sd / np.sqrt(len(s)) if len(s) > 1 else np.nan, median=s.median(), min=s.min(), max=s.max(),
                         pct_agree=100 * k / len(s), pct_agree_ci_low=100 * lo, pct_agree_ci_high=100 * hi,
                         skew=s.skew(), agree_rule=">=4 (items) / >=3.5 (composites)"))
    pd.DataFrame(rows).to_csv(C.TABLES / "table10_descriptive_statistics_current.csv", index=False)
    # current users partial shifting
    freq_table(d_cur["shifted_any"], order=["Yes", "No"]).to_csv(C.TABLES / "table10b_current_partial_shift.csv", index=False)
    return g, prof, t
