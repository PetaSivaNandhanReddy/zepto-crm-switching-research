"""Small, dependency-light statistical helpers (numpy/scipy only)."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C


def rng():
    return np.random.default_rng(C.SEED)


def wilson_ci(k, n, z=1.959964):
    if n == 0:
        return (np.nan, np.nan)
    p = k / n
    d = 1 + z**2 / n
    c = (p + z**2 / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / d
    return (max(0, c - h), min(1, c + h))


def freq_table(s: pd.Series, order=None, denom=None):
    """Frequency table with Wilson 95% CI. denom defaults to non-missing n."""
    s = s.dropna()
    n = denom if denom is not None else len(s)
    vc = s.value_counts()
    if order is not None:
        vc = vc.reindex(order).fillna(0).astype(int)
    rows = []
    for k, v in vc.items():
        lo, hi = wilson_ci(v, n)
        rows.append(dict(category=k, n=int(v), pct=100 * v / n if n else np.nan, ci_low=100 * lo, ci_high=100 * hi, base_n=n))
    return pd.DataFrame(rows)


def holm(pvals):
    p = np.asarray(pvals, float)
    m = len(p)
    order = np.argsort(p)
    adj = np.empty(m)
    run = 0.0
    for rank, idx in enumerate(order):
        val = (m - rank) * p[idx]
        run = max(run, val)
        adj[idx] = min(1.0, run)
    return adj


def spearman_boot(x, y, B=None):
    x = np.asarray(x, float); y = np.asarray(y, float)
    m = ~(np.isnan(x) | np.isnan(y)); x, y = x[m], y[m]
    n = len(x)
    r, p = stats.spearmanr(x, y)
    g = rng()
    B = B or C.BOOT
    bs = np.empty(B)
    for i in range(B):
        idx = g.integers(0, n, n)
        if np.ptp(x[idx]) == 0 or np.ptp(y[idx]) == 0:
            bs[i] = np.nan
        else:
            bs[i] = stats.spearmanr(x[idx], y[idx])[0]
    lo, hi = np.nanpercentile(bs, [2.5, 97.5])
    # Fisher-z approximate CI as well
    z = np.arctanh(r); se = 1.06 / np.sqrt(n - 3)
    return dict(n=n, rho=r, p=p, ci_boot_low=lo, ci_boot_high=hi,
                ci_fisher_low=np.tanh(z - 1.96 * se), ci_fisher_high=np.tanh(z + 1.96 * se))


def min_detectable_r(n, alpha=0.05, power=0.8):
    if n <= 3:
        return np.nan
    za = stats.norm.ppf(1 - alpha / 2); zb = stats.norm.ppf(power)
    return float(np.tanh((za + zb) / np.sqrt(n - 3)))


def mann_whitney(a, b):
    a = pd.Series(a).dropna().astype(float); b = pd.Series(b).dropna().astype(float)
    if len(a) < 2 or len(b) < 2:
        return dict(n1=len(a), n2=len(b), U=np.nan, p=np.nan, rank_biserial=np.nan, med1=np.nan, med2=np.nan)
    U, p = stats.mannwhitneyu(a, b, alternative="two-sided", method="auto")
    rb = 2 * U / (len(a) * len(b)) - 1  # rank-biserial (positive => a > b)
    return dict(n1=len(a), n2=len(b), U=U, p=p, rank_biserial=rb, med1=a.median(), med2=b.median(), mean1=a.mean(), mean2=b.mean())


def kruskal(groups: dict):
    g = {k: pd.Series(v).dropna().astype(float) for k, v in groups.items()}
    g = {k: v for k, v in g.items() if len(v) >= 2}
    if len(g) < 2:
        return dict(k=len(g), n=sum(len(v) for v in g.values()), H=np.nan, p=np.nan, eps2=np.nan)
    H, p = stats.kruskal(*g.values())
    n = sum(len(v) for v in g.values())
    eps2 = H * (n + 1) / (n**2 - 1)
    return dict(k=len(g), n=n, H=H, p=p, eps2=eps2)


def cramers_v(ct):
    chi2 = stats.chi2_contingency(ct, correction=False)[0]
    n = ct.values.sum()
    r, k = ct.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1))) if min(r, k) > 1 else np.nan


def _chi2_from_codes(xc, yc, kx, ky):
    tab = np.bincount(xc * ky + yc, minlength=kx * ky).reshape(kx, ky).astype(float)
    exp = np.outer(tab.sum(1), tab.sum(0)) / tab.sum()
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.nansum((tab - exp) ** 2 / exp)


def perm_chi2(x, y, B=5000):
    """Monte-Carlo permutation chi-square test (valid with sparse cells). Uses integer codes (numpy)."""
    d = pd.DataFrame({"x": pd.Series(x).astype(object), "y": pd.Series(y).astype(object)}).dropna()
    ct = pd.crosstab(d.x, d.y)
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return dict(n=len(d), chi2=np.nan, dof=np.nan, p_asymptotic=np.nan, p_perm=np.nan, cramers_v=np.nan, min_expected=np.nan, pct_cells_lt5=np.nan)
    chi2, p_as, dof, exp = stats.chi2_contingency(ct, correction=False)
    xc, xl = pd.factorize(d.x.astype(str)); yc, yl = pd.factorize(d.y.astype(str))
    xc = np.asarray(xc, dtype=np.int64); yc = np.asarray(yc, dtype=np.int64)
    g = rng()
    obs = _chi2_from_codes(xc, yc, len(xl), len(yl))
    cnt = 0
    for _ in range(B):
        cnt += _chi2_from_codes(xc, g.permutation(yc), len(xl), len(yl)) >= obs - 1e-9
    return dict(n=len(d), chi2=chi2, dof=dof, p_asymptotic=p_as, p_perm=(cnt + 1) / (B + 1),
                cramers_v=cramers_v(ct), min_expected=exp.min(), pct_cells_lt5=100 * (exp < 5).mean())


def fisher_2x2(a, b):
    d = pd.DataFrame({"a": a, "b": b}).dropna()
    ct = pd.crosstab(d.a, d.b)
    if ct.shape != (2, 2):
        return dict(n=len(d), odds_ratio=np.nan, p=np.nan)
    o, p = stats.fisher_exact(ct.values)
    return dict(n=len(d), odds_ratio=o, p=p, table=ct.values.tolist())
