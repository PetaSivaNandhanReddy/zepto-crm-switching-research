"""Measurement diagnostics: H5 anomaly (switching effort), discriminant validity (HTMT), within-person centering, R2 overlap."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C
from .stats_utils import rng, spearman_boot

SHARED = ["SAT1", "SAT2", "PUSH_consider", "ALT1", "ALT2", "VAR1", "PROMO1", "SC1", "FAM1", "SC2", "INT1", "INT2", "INT3"]


def _sp(x, y):
    r = spearman_boot(x, y, B=2000)
    return r


def h5_item_table(d):
    rows = []
    spec = [("SC1", "Switching effort item 1 ('would require additional time and effort')", "-"),
            ("SC2", "Switching effort item 2 ('effort ... makes me less likely to switch')", "-"),
            ("SWEFFORT", "Switching effort composite (SC1, SC2)", "-"),
            ("FAM1", "Familiarity ('makes me less likely to switch')", "-"),
            ("INERT1", "Inertia ('would continue using Zepto')", "-"),
            ("SAT1", "Satisfaction item 1", "-"), ("SAT2", "Satisfaction item 2", "-"), ("SAT", "Satisfaction composite", "-")]
    for v, lab, exp in spec:
        r = _sp(d[v], d["INT"])
        rows.append(dict(variable=v, description=lab, expected_sign_with_intention=exp, n=r["n"], spearman_rho=r["rho"],
                         ci_boot_low=r["ci_boot_low"], ci_boot_high=r["ci_boot_high"], p=r["p"],
                         observed_sign="+" if r["rho"] > 0 else "-", matches_expected=(r["rho"] < 0)))
    return pd.DataFrame(rows)


def h5_extra(d):
    out = {}
    out["n_retention_keyed_constructs_positive_with_intention"] = int(sum(stats.spearmanr(d[v], d["INT"], nan_policy="omit")[0] > 0 for v in ["SAT", "SWEFFORT", "FAM", "INERT"]))
    out["n_retention_keyed_constructs_total"] = 4
    a = d[d.SC2 >= 4]
    out["SC2_agree_n"] = int(len(a)); out["SC2_agree_and_INT_ge_3.5_n"] = int((a.INT >= 3.5).sum())
    out["SC2_agree_and_INT_ge_3.5_pct"] = 100 * (a.INT >= 3.5).mean()
    for lab, sub in [("excl_straightliners", d[~d.flag_straightline]), ("V2_only", d[d.questionnaire_version == "V2"]),
                     ("excl_Q1_inconsistent", d[~d.flag_q1_inconsistent])]:
        r = _sp(sub["SWEFFORT"], sub["INT"]); out[f"rho_SWEFFORT_INT_{lab}"] = r["rho"]; out[f"n_{lab}"] = r["n"]; out[f"p_{lab}"] = r["p"]
    # partial Spearman controlling PULL and SAT
    m = d[["SWEFFORT", "INT", "PULL", "SAT"]].dropna().rank()
    X = np.column_stack([np.ones(len(m)), m.PULL, m.SAT])
    rx = m.SWEFFORT - X @ np.linalg.lstsq(X, m.SWEFFORT, rcond=None)[0]
    ry = m.INT - X @ np.linalg.lstsq(X, m.INT, rcond=None)[0]
    pr = stats.pearsonr(rx, ry); out["partial_rho_SWEFFORT_INT_given_PULL_SAT"] = pr[0]; out["partial_p"] = pr[1]; out["partial_n"] = len(m)
    return pd.DataFrame([out])


def ipsatized(d):
    X = d[SHARED].astype(float)
    cen = X.sub(X.mean(axis=1), axis=0)
    cons = pd.DataFrame({"SAT": cen[["SAT1", "SAT2"]].mean(axis=1), "ALT": cen[["ALT1", "ALT2"]].mean(axis=1), "VAR(VAR1 only)": cen["VAR1"],
                         "PROMO": cen["PROMO1"], "SWEFFORT": cen[["SC1", "SC2"]].mean(axis=1), "FAM": cen["FAM1"],
                         "INT": cen[["INT1", "INT2", "INT3"]].mean(axis=1)})
    raw = pd.DataFrame({"SAT": d.SAT, "ALT": d.ALT, "VAR(VAR1 only)": d.VAR1, "PROMO": d.PROMO1, "SWEFFORT": d.SWEFFORT, "FAM": d.FAM, "INT": d.INT})
    rows = []
    for k in [c for c in cons.columns if c != "INT"]:
        r0 = _sp(raw[k], raw["INT"]); r1 = _sp(cons[k], cons["INT"])
        rows.append(dict(construct=k, n=r0["n"], rho_raw=r0["rho"], p_raw=r0["p"], rho_within_person_centered=r1["rho"],
                         ci_low_centered=r1["ci_boot_low"], ci_high_centered=r1["ci_boot_high"], p_centered=r1["p"]))
    return pd.DataFrame(rows)


def htmt(d):
    S = {"SAT": ["SAT1", "SAT2"], "ALT": ["ALT1", "ALT2"], "VAR": ["VAR1", "VAR2"], "SWEFFORT": ["SC1", "SC2"], "INT": ["INT1", "INT2", "INT3"]}
    allit = sum(S.values(), [])
    data = d[allit].dropna()
    g = rng()

    def calc(df, a, b):
        A = df[S[a] + S[b]].corr().abs()
        het = A.loc[S[a], S[b]].values.mean()
        wa = A.loc[S[a], S[a]].values[np.triu_indices(len(S[a]), 1)].mean()
        wb = A.loc[S[b], S[b]].values[np.triu_indices(len(S[b]), 1)].mean()
        return het / np.sqrt(wa * wb)
    rows = []
    keys = list(S)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            pt = calc(data, a, b)
            bs = []
            for _ in range(2000):
                s = data.iloc[g.integers(0, len(data), len(data))]
                try:
                    bs.append(calc(s, a, b))
                except Exception:
                    pass
            lo, hi = np.nanpercentile(bs, [2.5, 97.5])
            rows.append(dict(pair=f"{a} - {b}", n=len(data), HTMT=pt, ci_low=lo, ci_high=hi,
                             verdict="discriminant validity NOT established (HTMT >= 0.85)" if pt >= 0.85 else
                             ("borderline (0.80-0.85)" if pt >= 0.80 else "below 0.80")))
    return pd.DataFrame(rows)


def overlap(d):
    m = d[["INT", "PULL", "SAT", "SWEFFORT", "FAM"]].dropna()
    y = m.INT.values
    def r2(cols):
        X = np.column_stack([np.ones(len(m))] + [m[c].values for c in cols])
        b = np.linalg.lstsq(X, y, rcond=None)[0]; res = y - X @ b
        return 1 - res.var() * len(y) / ((y - y.mean()) ** 2).sum()
    from .reliability_analysis import cronbach_alpha
    pooled = d[["ALT1", "ALT2", "VAR1", "PROMO1", "INT1", "INT2", "INT3"]].dropna()
    return pd.DataFrame([dict(n=len(m), R2_PULL_alone=r2(["PULL"]), R2_M1_full=r2(["SAT", "PULL", "SWEFFORT", "FAM"]),
                              R2_gain_from_SAT_SWEFFORT_FAM=r2(["SAT", "PULL", "SWEFFORT", "FAM"]) - r2(["PULL"]),
                              spearman_PULL_INT=stats.spearmanr(m.PULL, m.INT)[0],
                              alpha_pull4_plus_intention3_pooled=cronbach_alpha(pooled), n_pooled=len(pooled))])


def run(d):
    a = h5_item_table(d); b = h5_extra(d); c = ipsatized(d); e = htmt(d); f = overlap(d)
    a.to_csv(C.TABLES / "table20_h5_item_diagnostics.csv", index=False)
    b.to_csv(C.STATS / "h5_additional_diagnostics.csv", index=False)
    c.to_csv(C.TABLES / "table21_within_person_centering_sensitivity.csv", index=False)
    e.to_csv(C.TABLES / "table22_discriminant_validity_htmt.csv", index=False)
    f.to_csv(C.STATS / "regression_overlap_diagnostics.csv", index=False)
    return a, b, c, e, f
