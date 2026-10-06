"""Pre-specified hypothesis tests H1-H9 (current users) + correlation matrix."""
import numpy as np
import pandas as pd
from scipy import stats
from . import config as C
from .stats_utils import spearman_boot, holm, min_detectable_r, mann_whitney


def write_registry():
    """Freeze the hypothesis definitions (SHA-256) so reported hypotheses can be checked against config.py."""
    import hashlib, json, datetime
    payload = json.dumps([C.HYPOTHESES, C.EXTENSION_HYPOTHESES], sort_keys=True, ensure_ascii=False)
    reg = dict(sha256=hashlib.sha256(payload.encode("utf-8")).hexdigest(), n_hypotheses=len(C.HYPOTHESES) + len(C.EXTENSION_HYPOTHESES),
               decision_rule="Supported iff direction as hypothesised AND Holm-adjusted p < .05 within H1-H7",
               note="Hypotheses are defined in src/config.py and written to this registry BEFORE any test is executed in the same run. "
                    "They were written after the Phase-1 audit, in which item-level descriptive correlations had been shown; specification was theory-led but not blind to those descriptives.",
               written_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
               hypotheses=C.HYPOTHESES + C.EXTENSION_HYPOTHESES)
    (C.DOCS / "hypothesis_registry.json").write_text(json.dumps(reg, indent=2, ensure_ascii=False), encoding="utf-8")
    return reg["sha256"]


def run(d: pd.DataFrame):
    write_registry()
    rows = []
    for h in C.HYPOTHESES:
        r = spearman_boot(d[h["construct"]], d[h["outcome"]])
        pear = stats.pearsonr(*d[[h["construct"], h["outcome"]]].dropna().T.values)
        rows.append(dict(H=h["id"], construct=h["construct"], ppm=h["ppm"], expected=h["expected"], n=r["n"],
                         spearman_rho=r["rho"], ci_boot_low=r["ci_boot_low"], ci_boot_high=r["ci_boot_high"],
                         p_unadjusted=r["p"], pearson_r=pear[0], pearson_p=pear[1],
                         min_detectable_abs_r_80pct_power=min_detectable_r(r["n"])))
    t = pd.DataFrame(rows)
    t["p_holm_H1_H7"] = holm(t.p_unadjusted.values)
    def decide(r):
        dir_ok = (r.spearman_rho < 0) if r.expected == "-" else (r.spearman_rho > 0)
        if r.p_holm_H1_H7 < C.ALPHA and dir_ok:
            return "Supported"
        if r.p_holm_H1_H7 < C.ALPHA and not dir_ok:
            return "Not supported (significant, opposite direction)"
        return "Not supported / insufficient evidence"
    t["decision"] = t.apply(decide, axis=1)

    def label(r):
        if r.decision == "Supported":
            return "Supported (raw scores)"
        if r.decision.startswith("Not supported (significant"):
            return "Anomalous / inconclusive (significant, opposite to hypothesised direction)"
        if r.ci_boot_low < 0 < r.ci_boot_high and max(abs(r.ci_boot_low), abs(r.ci_boot_high)) >= 0.30:
            return "Inconclusive (not significant; CI includes zero and moderate effects)"
        return "Not supported"
    t["evidence_label"] = t.apply(label, axis=1)
    meta = pd.DataFrame(C.HYPOTHESES)[["id", "text", "literature", "items"]].rename(columns={"id": "H"})
    t = meta.merge(t, on="H")
    t.to_csv(C.STATS / "hypothesis_tests_H1_H7.csv", index=False)

    # H9: intention by partial-switching behaviour (current users)
    a = d.loc[d.shifted_any_num == 1, "INT"]; b = d.loc[d.shifted_any_num == 0, "INT"]
    h9 = mann_whitney(a, b)
    h9.update(H="H9", expected="Yes > No", decision=None)
    h9["decision"] = "Supported" if (h9["p"] < C.ALPHA and h9["rank_biserial"] > 0) else "Not supported / insufficient evidence"
    pd.DataFrame([h9]).to_csv(C.STATS / "hypothesis_test_H9.csv", index=False)

    # correlation matrix (Spearman), pairwise n
    vars_ = ["INT", "SAT", "PUSH_consider", "ALT", "VAR", "PROMO", "SWEFFORT", "FAM", "INERT"]
    rho = pd.DataFrame(index=vars_, columns=vars_, dtype=float)
    pv = rho.copy(); nn = rho.copy()
    for i in vars_:
        for j in vars_:
            m = d[[i, j]].dropna()
            rr = stats.spearmanr(m[i], m[j]) if i != j else (1.0, 0.0)
            rho.loc[i, j], pv.loc[i, j], nn.loc[i, j] = rr[0], rr[1], len(m)
    rho.to_csv(C.TABLES / "table11_spearman_matrix.csv"); pv.to_csv(C.STATS / "spearman_matrix_p.csv"); nn.to_csv(C.STATS / "spearman_matrix_n.csv")
    return t, pd.DataFrame([h9]), rho, pv, nn
