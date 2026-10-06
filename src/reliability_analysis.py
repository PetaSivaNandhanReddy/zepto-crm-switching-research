"""Composite scores, reliability, item analysis, factorability (exploratory)."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C
from .stats_utils import rng


def cronbach_alpha(X: pd.DataFrame):
    X = X.dropna()
    k = X.shape[1]
    if k < 2 or len(X) < 3:
        return np.nan
    v = X.var(axis=0, ddof=1).sum()
    t = X.sum(axis=1).var(ddof=1)
    return k / (k - 1) * (1 - v / t) if t > 0 else np.nan


def add_composites(cur: pd.DataFrame) -> pd.DataFrame:
    d = cur.copy()
    for name, spec in C.CONSTRUCTS.items():
        items = spec["items"]
        req = 4 if name == "PULL" else 1
        cnt = d[items].notna().sum(axis=1)
        d[name] = d[items].mean(axis=1).where(cnt >= req)
    d["VAR_single_item"] = d["VAR2"].isna() & d["VAR1"].notna()
    return d


def reliability_table(d: pd.DataFrame) -> pd.DataFrame:
    rows = []
    sets = {"SAT (Push)": ["SAT1", "SAT2"], "ALT (Pull)": ["ALT1", "ALT2"], "VAR (Pull)": ["VAR1", "VAR2"],
            "SWEFFORT (Mooring)": ["SC1", "SC2"], "INT (Outcome)": ["INT1", "INT2", "INT3"],
            "PULL5 (Pull composite)": ["ALT1", "ALT2", "VAR1", "VAR2", "PROMO1"],
            "Mooring-3 (SC1,FAM1,SC2) [tested for pooling]": ["SC1", "FAM1", "SC2"],
            "Habit-2 (FAM1,INERT1) [tested for pooling]": ["FAM1", "INERT1"]}
    for lab, items in sets.items():
        X = d[items].dropna()
        k = len(items)
        a = cronbach_alpha(X)
        cm = X.corr(method="pearson")
        iir = cm.values[np.triu_indices(k, 1)].mean() if k > 1 else np.nan
        row = dict(scale=lab, n_items=k, n_complete=len(X), alpha=a, mean_inter_item_r=iir)
        if k == 2 and len(X) > 3:
            r = cm.iloc[0, 1]
            row["spearman_brown"] = 2 * r / (1 + r)
        for it in items:
            rest = X.drop(columns=it).sum(axis=1)
            row[f"itemtotal_{it}"] = stats.pearsonr(X[it], rest)[0] if k > 2 else np.nan
            row[f"alpha_if_deleted_{it}"] = cronbach_alpha(X.drop(columns=it)) if k > 2 else np.nan
        rows.append(row)
    return pd.DataFrame(rows)


def kmo_bartlett(X: pd.DataFrame):
    X = X.dropna()
    n, p = X.shape
    R = np.corrcoef(X.values, rowvar=False)
    detR = np.linalg.det(R)
    chi2 = -(n - 1 - (2 * p + 5) / 6) * np.log(detR)
    dof = p * (p - 1) / 2
    pval = 1 - stats.chi2.cdf(chi2, dof)
    inv = np.linalg.pinv(R)
    d = np.sqrt(np.outer(np.diag(inv), np.diag(inv)))
    pc = -inv / d
    np.fill_diagonal(pc, 0)
    R0 = R.copy(); np.fill_diagonal(R0, 0)
    kmo_all = (R0**2).sum(axis=0) / ((R0**2).sum(axis=0) + (pc**2).sum(axis=0))
    kmo = (R0**2).sum() / ((R0**2).sum() + (pc**2).sum())
    return dict(n=n, p_items=p, item_to_respondent=f"1:{n/p:.1f}", kmo=kmo, bartlett_chi2=chi2, bartlett_df=dof, bartlett_p=pval,
                det_R=detR), pd.Series(kmo_all, index=X.columns)


def parallel_analysis(X: pd.DataFrame, B=1000):
    X = X.dropna()
    n, p = X.shape
    ev = np.sort(np.linalg.eigvalsh(np.corrcoef(X.values, rowvar=False)))[::-1]
    g = rng()
    sim = np.empty((B, p))
    for b in range(B):
        Z = g.standard_normal((n, p))
        sim[b] = np.sort(np.linalg.eigvalsh(np.corrcoef(Z, rowvar=False)))[::-1]
    thr = np.percentile(sim, 95, axis=0)
    return ev, thr, int((ev > thr).sum())


def varimax(L, gamma=1.0, q=50, tol=1e-6):
    p, k = L.shape
    R = np.eye(k)
    d = 0
    for _ in range(q):
        d_old = d
        Lr = L @ R
        u, s, vh = np.linalg.svd(L.T @ (Lr**3 - gamma / p * Lr @ np.diag(np.diag(Lr.T @ Lr))))
        R = u @ vh
        d = s.sum()
        if d_old != 0 and d / d_old < 1 + tol:
            break
    return L @ R


def exploratory_structure(d: pd.DataFrame):
    items = ["SAT1", "SAT2", "PUSH_consider", "ALT1", "ALT2", "VAR1", "PROMO1", "SC1", "FAM1", "SC2", "INT1", "INT2", "INT3"]
    X = d[items].dropna()
    info, kmo_items = kmo_bartlett(X)
    ev, thr, nfac = parallel_analysis(X)
    k = max(1, nfac)
    w, V = np.linalg.eigh(np.corrcoef(X.values, rowvar=False))
    idx = np.argsort(w)[::-1]
    w, V = w[idx], V[:, idx]
    L = V[:, :k] * np.sqrt(w[:k])
    Lr = varimax(L) if k > 1 else L
    load = pd.DataFrame(Lr, index=items, columns=[f"PC{i+1}" for i in range(k)])
    load["communality"] = (L**2).sum(axis=1)
    eig = pd.DataFrame({"component": range(1, len(ev) + 1), "eigenvalue": ev, "parallel_95pct": thr})
    return info, kmo_items, eig, load, nfac


def run(cur: pd.DataFrame):
    d = add_composites(cur)
    d.to_csv(C.PROC_DIR / "analysis_current_with_constructs.csv", index=False)
    rel = reliability_table(d)
    rel.to_csv(C.TABLES / "table08_reliability.csv", index=False)
    info, kmo_items, eig, load, nfac = exploratory_structure(d)
    pd.DataFrame([info]).to_csv(C.STATS / "factorability_kmo_bartlett.csv", index=False)
    kmo_items.rename("kmo_msa").to_csv(C.STATS / "factorability_item_msa.csv")
    eig.to_csv(C.STATS / "eigenvalues_parallel_analysis.csv", index=False)
    load.to_csv(C.TABLES / "table09_exploratory_pca_loadings.csv")
    return d, rel, info, eig, load, nfac
