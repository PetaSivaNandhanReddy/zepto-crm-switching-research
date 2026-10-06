"""Former-user behavioural analysis, coverage vs voluntary split, never-user context."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C
from .stats_utils import freq_table, wilson_ci, mann_whitney, perm_chi2, fisher_2x2, holm

REASON_LABELS = ["Product availability", "Product variety / choice", "Pricing", "Discounts / promotions", "Delivery experience",
                 "App experience", "Product quality", "Customer service", "Return / refund experience",
                 "Zepto was not available in my area", "I preferred another quick-commerce platform"]


def run_former(f: pd.DataFrame, supp_cur: pd.DataFrame):
    n = len(f)
    # Table 13
    main = freq_table(f["fu_main_reason"]); main.to_csv(C.TABLES / "table13_former_main_reason.csv", index=False)
    rows = []
    for lab in REASON_LABELS:
        k = f["fu_reasons"].fillna("").apply(lambda t: lab in [x.strip() for x in t.split(";")]).sum()
        lo, hi = wilson_ci(k, n)
        rows.append(dict(reason=lab, n_mentions=int(k), pct=100 * k / n, ci_low=100 * lo, ci_high=100 * hi, base_n=n))
    multi = pd.DataFrame(rows).sort_values("n_mentions", ascending=False)
    multi.to_csv(C.TABLES / "table13b_former_all_reasons_multiselect.csv", index=False)
    n_reasons = f["fu_reasons"].str.count(";") + 1
    dest = freq_table(f["fu_destination"]); dest.to_csv(C.TABLES / "table14_switching_destination.csv", index=False)
    other = {name: freq_table(f[col], order=order) for name, col, order in [
        ("increased_other", "fu_increased_other", ["Yes", "No", "Not sure"]),
        ("alt_variants", "fu_alt_variants", ["Yes", "Maybe", "No"]),
        ("return", "fu_return", ["Definitely Yes", "Probably Yes", "Not Sure", "Probably no", "Definitely No"])]}
    for k_, v_ in other.items():
        v_.to_csv(C.TABLES / f"table13c_former_{k_}.csv", index=False)
    cls = freq_table(f["fu_class"]); cls.to_csv(C.TABLES / "table13d_former_coverage_vs_voluntary.csv", index=False)
    # voluntary reasons breakdown (class C main reason)
    freq_table(f.loc[f.fu_class == "C_voluntary_only", "fu_main_reason"]).to_csv(C.TABLES / "table13e_voluntary_only_main_reason.csv", index=False)
    freq_table(f.loc[f.fu_class == "B_coverage_mentioned_other_primary", "fu_main_reason"]).to_csv(C.TABLES / "table13f_classB_main_reason.csv", index=False)
    # H10: return intention coverage-primary (A) vs voluntary-only (C); B descriptive
    A = f.loc[f.fu_class == "A_coverage_primary", "fu_return_num"]; Cc = f.loc[f.fu_class == "C_voluntary_only", "fu_return_num"]
    h10 = mann_whitney(A, Cc); h10["H"] = "H10"; h10["expected"] = "A > C"
    h10["decision"] = "Supported" if (h10["p"] < C.ALPHA and h10["rank_biserial"] > 0) else "Not supported / insufficient evidence"
    pd.DataFrame([h10]).to_csv(C.STATS / "hypothesis_test_H10.csv", index=False)
    ret_by = f.groupby("fu_class")["fu_return_num"].agg(["count", "mean", "median"]).reset_index()
    ret_by.to_csv(C.TABLES / "table15b_return_by_class.csv", index=False)
    # class x profile / destination / variants
    tests = []
    for var in ["fu_destination", "fu_alt_variants", "fu_increased_other", "age_group", "occupation", "location_type", "qc_frequency"]:
        r = perm_chi2(f[var], f["fu_class"]); r["variable"] = var; tests.append(r)
    t = pd.DataFrame(tests); t["p_perm_holm"] = holm(t.p_perm.values); t.to_csv(C.STATS / "former_class_crosstab_tests.csv", index=False)
    pd.crosstab(f["fu_class"], f["fu_destination"]).to_csv(C.TABLES / "table14b_class_by_destination.csv")
    pd.crosstab(f["fu_class"], f["location_type"].fillna("Not asked (V1)")).to_csv(C.TABLES / "table15c_class_by_location.csv")
    # coverage-primary vs metro
    m = f.dropna(subset=["metro"]).copy(); m["cov"] = (m.fu_class == "A_coverage_primary").astype(int)
    fi = fisher_2x2(m["cov"], m["metro"]); pd.DataFrame([fi]).astype(str).to_csv(C.STATS / "former_coverage_by_metro_fisher.csv", index=False)
    # profile crosstabs of former main reason group
    pd.crosstab(f["age_group"], f["fu_class"]).to_csv(C.TABLES / "table15d_class_by_age.csv")
    pd.crosstab(f["occupation"], f["fu_class"]).to_csv(C.TABLES / "table15e_class_by_occupation.csv")
    # leaked current users' former-block (supplementary, n=7)
    supp = supp_cur.copy(); supp.to_csv(C.TABLES / "table13g_supp_current_users_leaked_reasons.csv", index=False)
    summary = dict(n_former=n, mean_reasons_selected=n_reasons.mean(), median_reasons=n_reasons.median(),
                   n_area_primary=int((f.fu_class == "A_coverage_primary").sum()),
                   n_area_any=int(f["fu_reasons"].fillna("").str.contains("not available in my area").sum()),
                   n_class_B=int((f.fu_class == "B_coverage_mentioned_other_primary").sum()),
                   n_class_C=int((f.fu_class == "C_voluntary_only").sum()),
                   n_inconsistent_q21_q23=int(f.fu_reason_main_inconsistent.sum()))
    pd.DataFrame([summary]).to_csv(C.STATS / "former_summary.csv", index=False)
    return dict(main=main, multi=multi, dest=dest, cls=cls, h10=h10, ret_by=ret_by, summary=summary, tests=t, fisher=fi, other=other)


def run_never(nv: pd.DataFrame):
    freq_table(nv["nu_reason"]).to_csv(C.TABLES / "table16b_never_reason.csv", index=False)
    freq_table(nv["nu_platform"]).to_csv(C.TABLES / "table16c_never_platform.csv", index=False)
    freq_table(nv["nu_pref_reason"]).to_csv(C.TABLES / "table16d_never_pref_reason.csv", index=False)
    rows = []
    for c in ["nu_current_better", "nu_consider_trying"]:
        s = nv[c].dropna(); k = int((s >= 4).sum()); lo, hi = wilson_ci(k, len(s))
        rows.append(dict(item=c, n=len(s), mean=s.mean(), sd=s.std(ddof=1), median=s.median(), pct_agree=100 * k / len(s), ci_low=100 * lo, ci_high=100 * hi))
    pd.DataFrame(rows).to_csv(C.TABLES / "table16e_never_likert.csv", index=False)
    w = [c for c in nv.columns if c.startswith("nu_w_")]
    base = int(nv["nu_what_would"].notna().sum())
    pd.DataFrame([dict(option=c.replace("nu_w_", ""), n=int(nv[c].sum()), pct=100 * nv[c].sum() / base, base_n=base) for c in w]).sort_values("n", ascending=False).to_csv(C.TABLES / "table16f_never_what_would_help.csv", index=False)
    m = nv.dropna(subset=["metro"]).copy(); m["area"] = (m.nu_reason == "Zepto is not available in my area").astype(int)
    fi = fisher_2x2(m["area"], m["metro"]); pd.DataFrame([fi]).astype(str).to_csv(C.STATS / "never_area_by_metro_fisher.csv", index=False)
    pd.crosstab(nv["nu_reason"], nv["location_type"].fillna("Not asked (V1)")).to_csv(C.TABLES / "table16g_never_reason_by_location.csv")
    return fi
