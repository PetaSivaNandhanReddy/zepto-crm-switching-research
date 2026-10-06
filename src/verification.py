"""Independent re-computation of key results from the RAW csv (csv module + numpy/scipy), compared with saved outputs."""
import csv
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
from . import config as C


def _num(x):
    x = x.strip()
    return float(x) if x != "" else np.nan


def run():
    with open(C.RAW_CSV, newline="", encoding="utf-8") as f:
        rows = list(csv.reader(f))
    hdr, data = rows[0], rows[1:]
    log = []

    def check(name, expected, observed, tol=1e-9):
        ok = (abs(float(expected) - float(observed)) <= tol) if isinstance(expected, (int, float, np.floating, np.integer)) else expected == observed
        log.append(dict(check=name, independent_value=expected, pipeline_value=observed, passed=bool(ok)))

    check("raw rows", len(data), 184); check("raw columns", len(hdr), 37)
    grp = [r[4].strip() for r in data]
    cur = [r for r in data if r[4].strip() == "Yes, I currently use Zepto"]
    frm = [r for r in data if r[4].strip().startswith("Yes, I used Zepto previously")]
    nev = [r for r in data if r[4].strip() == "No, I have never used Zepto"]
    df = pd.read_csv(C.CLEAN_DIR / "survey_cleaned_all184.csv")
    check("current n", len(cur), int((df.group == "Current").sum())); check("former n", len(frm), int((df.group == "Former").sum())); check("never n", len(nev), int((df.group == "Never").sum()))
    # leaks from raw positions
    fb = [i for i, r in enumerate(data) if r[4].strip() == "Yes, I currently use Zepto" and any(r[j].strip() for j in range(21, 25))]
    nb = [i for i, r in enumerate(data) if not r[4].strip().startswith("No") and any(r[j].strip() for j in range(27, 33))]
    check("leak: current users answering former block (respondents)", len(fb), int(df.leak_former_block.sum()))
    check("leak: current+former answering never block (respondents)", len(nb), int(df.leak_never_block.sum()))
    check("leak: UNIQUE respondents", len(set(fb) | set(nb)), int(df.leak_any.sum()))
    check("leak: block-level instances (7+15)", len(fb) + len(nb), 22)
    check("all leaking respondents within responses 1-22", int(max(set(fb) | set(nb)) + 1 <= 22), 1)
    # composites from raw
    def col(rows_, j): return np.array([_num(r[j]) for r in rows_])
    SAT = np.nanmean([col(cur, 5), col(cur, 6)], axis=0); ALT = np.nanmean([col(cur, 8), col(cur, 9)], axis=0)
    VAR = np.nanmean([col(cur, 10), col(cur, 11)], axis=0); PROMO = col(cur, 12); SW = np.nanmean([col(cur, 13), col(cur, 15)], axis=0)
    FAM = col(cur, 14); INERT = col(cur, 20); INT = np.nanmean([col(cur, 16), col(cur, 17), col(cur, 18)], axis=0)
    PULL = np.nanmean([col(cur, 8), col(cur, 9), col(cur, 10), col(cur, 11), col(cur, 12)], axis=0)
    h = pd.read_csv(C.STATS / "hypothesis_tests_H1_H7.csv").set_index("construct")
    ind = {}
    p_un = []
    for k, v in [("SAT", SAT), ("ALT", ALT), ("VAR", VAR), ("PROMO", PROMO), ("SWEFFORT", SW), ("FAM", FAM), ("INERT", INERT)]:
        m = ~(np.isnan(v) | np.isnan(INT))
        r, p = stats.spearmanr(v[m], INT[m]); ind[k] = (r, p, int(m.sum()))
        check(f"{k} rho (independent)", r, h.loc[k, "spearman_rho"], 1e-9); check(f"{k} n", int(m.sum()), int(h.loc[k, "n"]))
        p_un.append(p)
    adj = multipletests(p_un, method="holm")[1]
    for (k, _), a in zip([("SAT", 0), ("ALT", 0), ("VAR", 0), ("PROMO", 0), ("SWEFFORT", 0), ("FAM", 0), ("INERT", 0)], adj):
        check(f"{k} Holm p (statsmodels)", a, h.loc[k, "p_holm_H1_H7"], 1e-9)
    # alpha (covariance formula)
    def alpha(X):
        X = np.asarray(X).T; X = X[~np.isnan(X).any(axis=1)]; k = X.shape[1]
        S = np.cov(X, rowvar=False); return k / (k - 1) * (1 - np.trace(S) / S.sum())
    rel = pd.read_csv(C.TABLES / "table08_reliability.csv").set_index("scale")
    check("alpha INT", alpha([col(cur, 16), col(cur, 17), col(cur, 18)]), rel.loc["INT (Outcome)", "alpha"], 1e-9)
    check("alpha ALT", alpha([col(cur, 8), col(cur, 9)]), rel.loc["ALT (Pull)", "alpha"], 1e-9)
    check("alpha SWEFFORT", alpha([col(cur, 13), col(cur, 15)]), rel.loc["SWEFFORT (Mooring)", "alpha"], 1e-9)
    # OLS M1 normal equations
    X = np.column_stack([np.ones(len(cur)), SAT, PULL, SW, FAM]); m = ~np.isnan(X).any(axis=1) & ~np.isnan(INT)
    b = np.linalg.solve(X[m].T @ X[m], X[m].T @ INT[m])
    reg = pd.read_csv(C.STATS / "regression_coefficients.csv"); r1 = reg[reg.model.str.startswith("M1 PPM")].set_index("term")
    for nme, bb in zip(["const", "SAT", "PULL", "SWEFFORT", "FAM"], b):
        check(f"M1 coefficient {nme}", bb, r1.loc[nme, "b"], 1e-8)
    check("M1 n", int(m.sum()), int(r1.n.iloc[0]))
    res = INT[m] - X[m] @ b; r2 = 1 - (res ** 2).sum() / ((INT[m] - INT[m].mean()) ** 2).sum()
    check("M1 R2", r2, pd.read_csv(C.STATS / "regression_diagnostics.csv").iloc[0].r2, 1e-9)
    # straight-liners
    items = [5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18]
    sl = sum(len({r[j].strip() for j in items}) == 1 for r in cur)
    check("straight-liners", sl, int(df.flag_straightline.sum()))
    # subgroup tests recomputed
    ag = np.array([r[33].strip() == "18–24" for r in cur]); oc = np.array([r[34].strip() == "Student" for r in cur])
    seg = pd.read_csv(C.TABLES / "table15_segment_findings_current_users.csv").set_index("comparison")
    for lab, mask in [("INT: age 18-24 vs 25+", ag), ("INT: student vs non-student", oc)]:
        U, p = stats.mannwhitneyu(INT[mask], INT[~mask], alternative="two-sided")
        check(f"{lab} p", p, seg.loc[lab, "p"], 1e-9); check(f"{lab} n1", int(mask.sum()), int(seg.loc[lab, "n1"])); check(f"{lab} n2", int((~mask).sum()), int(seg.loc[lab, "n2"]))
    # former classes
    area_any = np.array(["not available in my area" in r[21] for r in frm]); area_pri = np.array([r[23].strip() == "Availability in my area" for r in frm])
    check("former class A", int(area_pri.sum()), int((df.fu_class == "A_coverage_primary").sum()))
    check("former class B", int((area_any & ~area_pri).sum()), int((df.fu_class == "B_coverage_mentioned_other_primary").sum()))
    check("former class C", int((~area_any & ~area_pri).sum()), int((df.fu_class == "C_voluntary_only").sum()))
    rmap = C.RETURN_MAP
    A = [rmap[r[26].strip()] for r, a in zip(frm, area_pri) if a and r[26].strip() in rmap]
    Cc = [rmap[r[26].strip()] for r, a, b_ in zip(frm, area_any, area_pri) if (not a) and (not b_) and r[26].strip() in rmap]
    U, p = stats.mannwhitneyu(A, Cc, alternative="two-sided")
    check("H10 p", p, pd.read_csv(C.STATS / "hypothesis_test_H10.csv").iloc[0].p, 1e-9); check("H10 n", len(A) + len(Cc), 58)
    out = pd.DataFrame(log)
    out.to_csv(C.STATS / "verification_log.csv", index=False)
    if not out.passed.all():
        raise AssertionError("Verification failed:\n" + out[~out.passed].to_string())
    return out
