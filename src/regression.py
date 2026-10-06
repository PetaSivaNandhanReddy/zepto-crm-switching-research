"""Pre-specified regression models on current users + sensitivity analyses."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats
from . import config as C
from .stats_utils import rng

M1 = ["SAT", "PULL", "SWEFFORT", "FAM"]          # PPM-level, pre-specified (k=4)
M2 = ["SAT", "ALT", "VAR", "PROMO", "SWEFFORT", "FAM"]   # disaggregated, exploratory (k=6)


def ols_block(d, preds, y="INT", label="", boot=True):
    m = d[[y] + preds].dropna()
    X = sm.add_constant(m[preds]); Y = m[y]
    fit = sm.OLS(Y, X).fit()
    rob = sm.OLS(Y, X).fit(cov_type="HC3")
    zs = (m - m.mean()) / m.std(ddof=1)
    beta = sm.OLS(zs[y], zs[preds]).fit().params
    g = rng()
    bs = np.empty((C.BOOT, len(preds) + 1))
    Xv, Yv = X.values, Y.values
    for i in range(C.BOOT):
        idx = g.integers(0, len(m), len(m))
        try:
            bs[i] = np.linalg.lstsq(Xv[idx], Yv[idx], rcond=None)[0]
        except Exception:
            bs[i] = np.nan
    lo, hi = np.nanpercentile(bs, [2.5, 97.5], axis=0)
    rows = []
    for j, nme in enumerate(["const"] + preds):
        rows.append(dict(model=label, term=nme, n=len(m), b=fit.params[nme], se_ols=fit.bse[nme], se_hc3=rob.bse[nme],
                         p_ols=fit.pvalues[nme], p_hc3=rob.pvalues[nme], ci_boot_low=lo[j], ci_boot_high=hi[j],
                         std_beta=beta.get(nme, np.nan)))
    coef = pd.DataFrame(rows)
    vif = pd.DataFrame({"term": preds, "VIF": [variance_inflation_factor(X.values, i + 1) for i in range(len(preds))]})
    infl = fit.get_influence()
    diag = dict(model=label, n=len(m), k=len(preds), cases_per_predictor=len(m) / len(preds), r2=fit.rsquared, adj_r2=fit.rsquared_adj,
                F=fit.fvalue, F_p=fit.f_pvalue, rmse=np.sqrt(fit.mse_resid), shapiro_resid_p=stats.shapiro(fit.resid)[1],
                breusch_pagan_p=het_breuschpagan(fit.resid, X)[1], max_cooks_d=np.max(infl.cooks_distance[0]),
                max_vif=vif.VIF.max(), cond_no=np.linalg.cond(X.values))
    # rank-based robustness (OLS on ranks)
    rk = m.rank()
    rfit = sm.OLS(rk[y], sm.add_constant(rk[preds])).fit(cov_type="HC3")
    coef["p_rank_ols_hc3"] = [rfit.pvalues[t] for t in coef.term]
    return coef, vif, diag, fit


def logit_block(d, preds, y="shifted_any_num", label="Logit"):
    m = d[[y] + preds].dropna()
    X = sm.add_constant(m[preds])
    fit = sm.Logit(m[y], X).fit(disp=0)
    ci = fit.conf_int()
    out = pd.DataFrame({"model": label, "term": fit.params.index, "n": len(m), "events": int(m[y].sum()),
                        "log_odds": fit.params.values, "odds_ratio": np.exp(fit.params.values),
                        "or_ci_low": np.exp(ci[0].values), "or_ci_high": np.exp(ci[1].values), "p": fit.pvalues.values})
    lr = dict(model=label, n=len(m), events=int(m[y].sum()), nonevents=int((1 - m[y]).sum()), k=len(preds),
              events_per_predictor=min(m[y].sum(), (1 - m[y]).sum()) / len(preds), mcfadden_r2=fit.prsquared,
              LR_chi2=fit.llr, LR_p=fit.llr_pvalue)
    return out, lr


def run(d: pd.DataFrame):
    res = {}
    c1, v1, g1, f1 = ols_block(d, M1, label="M1 PPM composites (pre-specified)")
    c2, v2, g2, f2 = ols_block(d, M2, label="M2 disaggregated pull (exploratory)")
    coefs = pd.concat([c1, c2]); diags = pd.DataFrame([g1, g2])
    vifs = pd.concat([v1.assign(model="M1"), v2.assign(model="M2")])
    coefs.to_csv(C.STATS / "regression_coefficients.csv", index=False)
    diags.to_csv(C.STATS / "regression_diagnostics.csv", index=False)
    vifs.to_csv(C.STATS / "regression_vif.csv", index=False)
    # M1 with inertia (n=46) - extension
    c3, v3, g3, _ = ols_block(d, M1 + ["INERT"], label="M1+INERT (n limited by structural missingness)")
    pd.concat([c3]).to_csv(C.STATS / "regression_M1_plus_inertia.csv", index=False)
    pd.DataFrame([g3]).to_csv(C.STATS / "regression_M1_plus_inertia_diag.csv", index=False)
    # Sensitivity analyses on M1
    sets = {
        "All current users": d,
        "Excl. straight-liners": d[~d.flag_straightline],
        "V2 only (excl. V1/V1.5)": d[d.questionnaire_version == "V2"],
        "Excl. Q1-inconsistent": d[~d.flag_q1_inconsistent],
        "Excl. straight-liners & V1/V1.5": d[(~d.flag_straightline) & (d.questionnaire_version == "V2")],
    }
    srows = []
    for lab, sub in sets.items():
        c, _, g, _ = ols_block(sub, M1, label=lab)
        for _, r in c[c.term != "const"].iterrows():
            srows.append(dict(sample=lab, n=r.n, term=r.term, b=r.b, ci_boot_low=r.ci_boot_low, ci_boot_high=r.ci_boot_high,
                              p_hc3=r.p_hc3, std_beta=r.std_beta, r2=g["r2"], adj_r2=g["adj_r2"]))
    sens = pd.DataFrame(srows)
    sens.to_csv(C.TABLES / "table12b_sensitivity_M1.csv", index=False)
    # Early-version comparability: shared items current early vs later
    from .stats_utils import mann_whitney
    early = d[d.questionnaire_version != "V2"]; late = d[d.questionnaire_version == "V2"]
    cmp = []
    for c in ["SAT", "ALT", "PROMO", "SWEFFORT", "FAM", "INT", "PUSH_consider"]:
        r = mann_whitney(early[c], late[c]); r["variable"] = c; cmp.append(r)
    pd.DataFrame(cmp).to_csv(C.STATS / "early_vs_late_current_comparison.csv", index=False)
    # Logistic on partial-shift behaviour
    lo, lr = logit_block(d, ["SAT", "PULL", "SWEFFORT"], label="Logit shifted_any ~ SAT+PULL+SWEFFORT")
    lo.to_csv(C.STATS / "logistic_partial_shift.csv", index=False); pd.DataFrame([lr]).to_csv(C.STATS / "logistic_partial_shift_diag.csv", index=False)
    return coefs, diags, vifs, sens, lo, lr, pd.DataFrame(cmp), c3, g3
