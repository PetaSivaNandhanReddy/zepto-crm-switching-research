"""Figures (matplotlib only)."""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from . import config as C

plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False, "figure.dpi": 130})
COL = {"Current": "#2b6cb0", "Former": "#c05621", "Never": "#718096"}


def _save(fig, name):
    fig.tight_layout(); fig.savefig(C.FIGS / name, bbox_inches="tight"); plt.close(fig)


def run(df, cur):
    t = lambda n: pd.read_csv(C.TABLES / n)
    s = lambda n: pd.read_csv(C.STATS / n)
    # F1 composition
    g = t("table03_user_groups.csv")
    fig, ax = plt.subplots(1, 2, figsize=(8, 3))
    ax[0].bar(g.category, g.n, color=[COL[c] for c in g.category])
    for i, r in g.iterrows(): ax[0].text(i, r.n + 1, f"{r.n} ({r.pct:.0f}%)", ha="center")
    ax[0].set_title("Respondent groups (n = 184)"); ax[0].set_ylabel("Respondents")
    ct = pd.crosstab(df.questionnaire_version, df.group)[["Current", "Former", "Never"]]
    ct.plot(kind="bar", stacked=True, ax=ax[1], color=[COL[c] for c in ct.columns], rot=0)
    ax[1].set_title("Questionnaire version by group"); ax[1].set_xlabel(""); ax[1].legend(frameon=False)
    _save(fig, "fig01_respondent_composition.png")
    # F2 former reasons
    m = t("table13_former_main_reason.csv").sort_values("n")
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.barh(m.category, m.n, color="#c05621", xerr=[m.n - m.ci_low * 73 / 100, m.ci_high * 73 / 100 - m.n], ecolor="#999", capsize=2)
    ax.set_xlabel("Former users, n = 73 (bars: 95% Wilson CI)")
    ax.set_title("Former users: main reason for leaving")
    _save(fig, "fig02_former_main_reasons.png")
    # F3 destination
    d = t("table14_switching_destination.csv").sort_values("n")
    fig, ax = plt.subplots(figsize=(5.5, 3))
    ax.barh(d.category, d.n, color="#c05621"); ax.set_xlabel("Former users, n = 73"); ax.set_title("Primary destination platform")
    _save(fig, "fig03_switching_destination.png")
    # F4 coverage vs voluntary
    c = t("table13d_former_coverage_vs_voluntary.csv")
    lab = {"A_coverage_primary": "A: area = main reason", "B_coverage_mentioned_other_primary": "B: area mentioned,\nother main reason", "C_voluntary_only": "C: voluntary only"}
    fig, ax = plt.subplots(figsize=(5.5, 3))
    ax.bar([lab[x] for x in c.category], c.n, color=["#dd6b20", "#ecc94b", "#2b6cb0"])
    for i, r in c.iterrows(): ax.text(i, r.n + .5, f"{r.n} ({r.pct:.0f}%)", ha="center")
    ax.set_title("Former users: coverage-driven vs voluntary exits (n = 73)")
    _save(fig, "fig04_coverage_vs_voluntary.png")
    # F5 construct means
    ds = t("table10_descriptive_statistics_current.csv").set_index("variable").loc[["INT", "SAT", "ALT", "VAR", "PROMO", "SWEFFORT", "FAM", "INERT"]]
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.errorbar(ds["mean"], range(len(ds)), xerr=[ds["mean"] - ds.ci95_low, ds.ci95_high - ds["mean"]], fmt="o", color="#2b6cb0", capsize=3)
    ax.set_yticks(range(len(ds))); ax.set_yticklabels([f"{i} (n={int(n)})" for i, n in zip(ds.index, ds.n)]); ax.invert_yaxis()
    ax.axvline(3, ls="--", c="#aaa"); ax.set_xlim(1, 5); ax.set_xlabel("Mean (1-5) with 95% CI"); ax.set_title("Current users: construct means")
    _save(fig, "fig05_construct_means_current.png")
    # F6 correlations with intention
    h = s("hypothesis_tests_H1_H7.csv")
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ok = h.decision.eq("Supported")
    ax.errorbar(h.spearman_rho, range(len(h)), xerr=[h.spearman_rho - h.ci_boot_low, h.ci_boot_high - h.spearman_rho], fmt="none", ecolor="#888", capsize=3)
    ax.scatter(h.spearman_rho, range(len(h)), c=np.where(ok, "#2b6cb0", np.where(h.p_holm_H1_H7 < .05, "#c53030", "#a0aec0")), zorder=3)
    ax.set_yticks(range(len(h))); ax.set_yticklabels([f"{a} {b} (n={n})" for a, b, n in zip(h.H, h.construct, h.n)]); ax.invert_yaxis()
    ax.axvline(0, c="k", lw=.6); ax.set_xlabel("Spearman rho with switching intention (bootstrap 95% CI)")
    ax.set_title("Blue = supported; red = significant, opposite direction; grey = not supported")
    _save(fig, "fig06_hypothesis_correlations.png")
    # F7 regression coefficients M1
    r = s("regression_coefficients.csv"); r = r[(r.model.str.startswith("M1 PPM")) & (r.term != "const")]
    fig, ax = plt.subplots(figsize=(5.5, 2.8))
    ax.errorbar(r.b, range(len(r)), xerr=[r.b - r.ci_boot_low, r.ci_boot_high - r.b], fmt="o", color="#2b6cb0", capsize=3)
    ax.set_yticks(range(len(r))); ax.set_yticklabels(r.term); ax.invert_yaxis(); ax.axvline(0, c="k", lw=.6)
    ax.set_xlabel(f"Unstandardised b (bootstrap 95% CI); n = {int(r.n.iloc[0])}"); ax.set_title("Model M1: predictors of switching intention")
    _save(fig, "fig07_regression_M1.png")
    # F8 conceptual model
    fig, ax = plt.subplots(figsize=(8, 3.6)); ax.axis("off")
    def box(x, y, w, h, txt, fc): ax.add_patch(plt.Rectangle((x, y), w, h, fc=fc, ec="#333")); ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=8)
    box(.02, .62, .26, .3, "PUSH\nSatisfaction / expectations\n(SAT1-2)", "#fed7d7")
    box(.02, .25, .26, .3, "PULL\nAlternative attractiveness, variety,\npromotions (ALT, VAR, PROMO)", "#c6f6d5")
    box(.02, -.12, .26, .3, "MOORING\nSwitching effort, familiarity,\ninertia (SC, FAM, INERT)", "#bee3f8")
    box(.42, .3, .2, .3, "Switching\nintention\n(INT1-3, n=51)", "#faf089")
    box(.75, .5, .23, .3, "Self-reported partial shift\n(current users, n=51)", "#e2e8f0")
    box(.75, .05, .23, .3, "Actual exit: former users\n(n=73): coverage-driven vs\nvoluntary", "#e2e8f0")
    for y in (.77, .4, .03): ax.annotate("", xy=(.42, .45), xytext=(.28, y), arrowprops=dict(arrowstyle="->"))
    ax.annotate("", xy=(.75, .65), xytext=(.62, .48), arrowprops=dict(arrowstyle="->", ls="--"))
    ax.annotate("", xy=(.75, .2), xytext=(.62, .4), arrowprops=dict(arrowstyle="->", ls=":"))
    ax.set_xlim(0, 1); ax.set_ylim(-.15, 1)
    ax.set_title("Conceptual model (associations only; cross-sectional). Dashed/dotted = descriptive links, not tested as a single model")
    _save(fig, "fig08_conceptual_model.png")
