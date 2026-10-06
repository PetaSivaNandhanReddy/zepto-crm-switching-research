"""Hypothesis matrix, n-register, triangulation, factor evidence and CRM matrices (numbers read from result files)."""
import numpy as np
import pandas as pd
from . import config as C


def _t(n): return pd.read_csv(C.TABLES / n)
def _s(n): return pd.read_csv(C.STATS / n)


def build_matrices():
    h = _s("hypothesis_tests_H1_H7.csv"); h9 = _s("hypothesis_test_H9.csv").iloc[0]; h10 = _s("hypothesis_test_H10.csv").iloc[0]
    ips = _t("table21_within_person_centering_sensitivity.csv").set_index("construct")
    ipmap = {"ALT": "ALT", "VAR": "VAR(VAR1 only)", "PROMO": "PROMO", "SWEFFORT": "SWEFFORT", "FAM": "FAM", "SAT": "SAT"}
    litev = pd.read_csv(C.LIT / "hypothesis_evidence.csv").set_index("H")
    rows = []
    for _, r in h.iterrows():
        ic = ips.loc[ipmap[r.construct]] if r.construct in ipmap else None
        rob = "n/a (single-item, n=46)" if ic is None else (f"Within-person-centered rho = {ic.rho_within_person_centered:+.2f} [{ic.ci_low_centered:+.2f}, {ic.ci_high_centered:+.2f}] (exploratory; ipsatization can bias)")
        rows.append(dict(H=r.H, Construct=r.construct, PPM=r.ppm, Relationship=r.text, Literature_rationale=litev.loc[r.H, "supporting"],
                         Literature_mixed_or_contrary=litev.loc[r.H, "mixed_or_contrary"], Literature_evidence_class=litev.loc[r.H, "evidence_class"],
                         Survey_items=r["items"], Expected_direction=r.expected, Planned_test="Spearman rho (bootstrap CI, 5000 reps, fixed seed); Holm across H1-H7",
                         n=int(r.n), Coefficient=round(r.spearman_rho, 3), CI95=f"[{r.ci_boot_low:.2f}, {r.ci_boot_high:.2f}]", p_unadjusted=round(r.p_unadjusted, 4),
                         p_Holm=round(r.p_holm_H1_H7, 4), Decision_rule_result=r.decision, Evidence_label=r.evidence_label, Robustness_note=rob))
    rows.append(dict(H="H8", Construct="SAT, PULL, SWEFFORT, FAM jointly", PPM="Push+Pull+Mooring", Relationship=C.EXTENSION_HYPOTHESES[0]["text"],
                     Literature_rationale=litev.loc["H8", "supporting"], Literature_mixed_or_contrary="none", Literature_evidence_class=litev.loc["H8", "evidence_class"], Survey_items="SAT1-2, ALT1-2, VAR1-2, PROMO1, SC1-2, FAM1",
                     Expected_direction="joint", Planned_test="OLS (HC3 SE, bootstrap CI); exploratory", n=51, Coefficient="see regression table", CI95="", p_unadjusted="", p_Holm="n/a",
                     Decision_rule_result="Model significant (F-test) but exploratory", Evidence_label="Exploratory / associational only (item overlap)", Robustness_note="R2 driven mainly by PULL (see overlap diagnostics)"))
    rows.append(dict(H="H9", Construct="Partial switching (Q19) vs intention", PPM="Outcome link", Relationship=C.EXTENSION_HYPOTHESES[1]["text"], Literature_rationale=litev.loc["H9", "supporting"],
                     Literature_mixed_or_contrary="n/a", Literature_evidence_class=litev.loc["H9", "evidence_class"], Survey_items="INT1-3; shifted_any", Expected_direction="Yes > No", Planned_test="Mann-Whitney U",
                     n=int(h9.n1 + h9.n2), Coefficient=f"rank-biserial {h9.rank_biserial:.2f}; medians {h9.med1:.2f} vs {h9.med2:.2f}", CI95="not computed", p_unadjusted=round(h9.p, 4), p_Holm="n/a (separate test)",
                     Decision_rule_result=h9.decision, Evidence_label="Not supported / inconclusive", Robustness_note=""))
    rows.append(dict(H="H10", Construct="Return willingness: coverage-primary (A) vs voluntary-only (C)", PPM="Retention (former users)", Relationship=C.EXTENSION_HYPOTHESES[2]["text"], Literature_rationale=litev.loc["H10", "supporting"],
                     Literature_mixed_or_contrary="n/a", Literature_evidence_class=litev.loc["H10", "evidence_class"], Survey_items="fu_main_reason, Q21 area option, fu_return", Expected_direction="A > C", Planned_test="Mann-Whitney U",
                     n=int(h10.n1 + h10.n2), Coefficient=f"rank-biserial {h10.rank_biserial:.2f}; medians {h10.med1:.1f} vs {h10.med2:.1f}", CI95="not computed", p_unadjusted=round(h10.p, 4), p_Holm="n/a (separate test)",
                     Decision_rule_result=h10.decision, Evidence_label="Not supported / inconclusive", Robustness_note="Former users only; return item missing for 5 V1 respondents"))
    hm = pd.DataFrame(rows)
    with pd.ExcelWriter(C.DOCS / "hypothesis_matrix.xlsx") as xw:
        hm.to_excel(xw, sheet_name="hypothesis_matrix", index=False)
        _s("regression_coefficients.csv").to_excel(xw, sheet_name="regression", index=False)
    hm.to_csv(C.TABLES / "table12a_hypothesis_results.csv", index=False)
    _s("regression_coefficients.csv").to_csv(C.TABLES / "table12_regression_results.csv", index=False)
    _s("regression_diagnostics.csv").to_csv(C.TABLES / "table12c_regression_diagnostics.csv", index=False)
    pd.read_csv(C.LIT / "hypothesis_evidence.csv").to_csv(C.TABLES / "table07_literature_hypothesis_evidence.csv", index=False)

    reg = _s("regression_diagnostics.csv"); lg = _s("logistic_partial_shift_diag.csv").iloc[0]
    nreg = pd.DataFrame([
        ("Respondent profile / group distribution", "All respondents", 184, ""),
        ("Location and monthly-spend descriptives", "All respondents asked (V1.5 and V2)... V1 not asked", 168, "16 structurally missing (V1)"),
        ("Group x profile tests", "All (location/spend: 168)", "184 / 168", ""),
        ("Current-user descriptives, H1-H6", "Current users", 51, "VAR uses VAR1 only for 5 V1 respondents"),
        ("H7 inertia", "Current users with INERT1", 46, "5 structurally missing (V1)"),
        ("HTMT discriminant-validity analysis", "Current users with all items incl. VAR2", 46, "complete cases"),
        ("M1 regression (SAT, PULL, SWEFFORT, FAM)", "Current users", int(reg.iloc[0].n), f"{reg.iloc[0].cases_per_predictor:.1f} cases/predictor"),
        ("M2 regression (6 predictors)", "Current users", int(reg.iloc[1].n), f"{reg.iloc[1].cases_per_predictor:.1f} cases/predictor (exploratory)"),
        ("Logistic partial shift (3 predictors)", "Current users", int(lg.n), f"{int(lg.events)} events / {int(lg.nonevents)} non-events"),
        ("Sensitivity: excl. straight-liners", "Current users", 39, ""), ("Sensitivity: V2 only", "Current users", 44, ""),
        ("Sensitivity: excl. Q1-inconsistent", "Current users", 39, ""), ("Sensitivity: straight-liners and V1/V1.5 excluded", "Current users", 33, ""),
        ("Former reasons/destination", "Former users", 73, ""), ("Former alt variants / return intention", "Former users", 68, "5 structurally missing (V1)"),
        ("H10 (class A vs C)", "Former users, class A (28) and C (30)", 58, "Return item missing for 5 V1 former users; class B (n=10) descriptive only"),
        ("Never-user reasons", "Never-users", 60, ""), ("Never-user preferred-platform reason / help items", "Never-users", 54, "6 missing (branch/version)"),
        ("Supplementary: current users' out-of-branch reasons", "Current users (leaked)", 7, "descriptive only"),
    ], columns=["analysis", "sample", "n", "note"])
    nreg.loc[nreg.analysis.str.startswith("Location"), "sample"] = "All respondents who were asked (V1.5 and V2)"
    nreg.to_csv(C.STATS / "analysis_n_register.csv", index=False)

    ret = _t("table13c_former_return.csv"); alt = _t("table13c_former_alt_variants.csv"); m = _t("table13b_former_all_reasons_multiselect.csv").set_index("reason")
    main = _t("table13_former_main_reason.csv").set_index("category"); cls = _t("table13d_former_coverage_vs_voluntary.csv").set_index("category")
    vol = _t("table13e_voluntary_only_main_reason.csv").set_index("category"); nvr = _t("table16b_never_reason.csv").set_index("category")
    ds = _t("table10_descriptive_statistics_current.csv").set_index("variable")
    ips = _t("table21_within_person_centering_sensitivity.csv").set_index("construct")
    frm = pd.read_csv(C.PROC_DIR / "analysis_former_users.csv")
    rc = frm.groupby("fu_class").fu_return_num.agg(["count", lambda x: int((x >= 4).sum())]); rc.columns = ["n", "ge4"]
    hh = h.set_index("construct")
    nv_area = int(nvr.loc["Zepto is not available in my area", "n"])
    pav = int(m.loc["Product availability", "n_mentions"]); var = int(m.loc["Product variety / choice", "n_mentions"])
    volpv = int(vol.loc["Product availability", "n"] + vol.loc["Product variety / choice", "n"]); nvol = int(cls.loc["C_voluntary_only", "n"])
    altyes = int(alt.loc[alt.category == "Yes", "n"].iloc[0]); altmaybe = int(alt.loc[alt.category == "Maybe", "n"].iloc[0])
    A = int(cls.loc["A_coverage_primary", "n"])

    tri = pd.DataFrame([
        dict(Factor="Service coverage (Zepto not available in respondent's area)", PPM="Outside standard PPM (structural/involuntary)",
             Academic="Insufficient: no verified PPM study addresses service coverage constraints",
             Zepto_evidence="[Primary, S01] pp.143-145: Rs 16,289.75M earmarked for dark-store network expansion across FY27-FY29; p.163: 1,139 dark stores across 66 cities at 31 Mar 2026. Company capital allocation and KPI disclosure.",
             Industry_evidence="[Redseer S04, full article] smaller-city quick commerce shows weaker demand maturity and Redseer advises prioritising cities; descriptive industry context",
             Current_users="Not measured",
             Former_users=f"Main reason for {A}/73 ({main.loc['Availability in my area','pct']:.1f}%); Q21 'not available in my area' ticked by {int(m.loc['Zepto was not available in my area','n_mentions'])}/73; never-users: {nv_area}/60 (context only; never-users not switchers)",
             Statistical="Descriptive frequencies with Wilson CIs only (no inferential test)",
             Classification="Partial",
             Interpretation="Survey evidence identifies coverage/serviceability as a major reported barrier, while the UDRHP independently documents substantial dark-store expansion intended to extend serviceability and geographic reach. Frequencies and expansion statements align, but do not establish causality for individual past exits.",
             CRM="R1 serviceability waitlist"),
        dict(Factor="Competitor pull: alternative attractiveness and product choice/variety", PPM="Pull",
             Academic="Direct support for alternative attractiveness (L05 A, L10 A, L16 B); indirect support for variety (scale content)",
             Zepto_evidence="[Primary, S01] p.162: store-level unique SKUs grew from 12,312 (FY24) to 46,623 (FY26) and 49,602 in Q4 FY26 (KPI disclosure); p.31: competitor promotions and wider assortment disclosed as business risks (Risk Factor 6); p.538: management strategy links SKU depth to user retention",
             Industry_evidence="[Redseer S03] competitive pressure building, challengers growing faster at platform level; [S05] hyperlocal assortment is a brand lever",
             Current_users=f"ALT rho={hh.loc['ALT','spearman_rho']:.2f}, VAR rho={hh.loc['VAR','spearman_rho']:.2f} (n=51, Holm p<.001) but ALT centered rho={ips.loc['ALT','rho_within_person_centered']:+.2f}; HTMT ALT-VAR 0.94",
             Former_users=f"Availability mentioned by {pav}/73, variety by {var}/73; voluntary-only exits (n={nvol}): availability+variety = {volpv}/{nvol} as main reason; {altyes}/68 say the alternative had products not easily found on Zepto ('Maybe': {altmaybe})",
             Statistical="Supported on raw scores only; constructs not empirically distinct; fragile to response-style adjustment",
             Classification="Partial",
             Interpretation="Compatible direction across literature, current-user raw associations, voluntary former-user reasons, and UDRHP SKU growth. The survey cannot separate variety from general attractiveness, and filing risks represent corporate disclosures rather than causal findings.",
             CRM="R2 assortment-gap alerts; R3 reason-specific win-back"),
        dict(Factor="Competitor promotions / price", PPM="Pull",
             Academic="Indirect: promotions are one item in L05's attractiveness scale; no isolated effect verified",
             Zepto_evidence="[Primary, S01] p.31: Risk Factor 6 names competitor promotions, incentives, and alternative pricing models as risk factors; p.34: risk disclosure that higher user fees may decrease transaction frequency; p.234: company Everyday Low Price (EDLP) operating philosophy",
             Industry_evidence="[Redseer S05] describes users as more time- than price-sensitive (general, not Zepto-specific)",
             Current_users=f"PROMO rho={hh.loc['PROMO','spearman_rho']:.2f} (n=51, single item); centered rho {ips.loc['PROMO','rho_within_person_centered']:+.2f}, CI includes 0",
             Former_users=f"Discounts/promotions {int(m.loc['Discounts / promotions','n_mentions'])}/73 mentions, pricing {int(m.loc['Pricing','n_mentions'])}/73; main reason 5/73 and 3/73",
             Statistical="Supported on raw single-item scores; fragile", Classification="Partial",
             Interpretation="Association with intention on raw scores is not matched by exit-reason frequency among former users. UDRHP identifies competitor pricing as a strategic risk, but provides no evidence that promotions drive switching causally.",
             CRM="No direct promotion intervention recommended (R2/R3 priority)"),
        dict(Factor="Switching effort (mooring)", PPM="Mooring",
             Academic="Mixed: theory expects a negative effect; L10 (A) found a positive switching-cost coefficient with items about the effort of changing to the alternative; L06 (B) not significant",
             Zepto_evidence="[Primary, S01] pp.27-28, 56: delivery partners and merchant partners multi-home freely across platforms; no structural barrier disclosed for consumer multi-platform usage",
             Industry_evidence="None retrieved",
             Current_users=f"SWEFFORT rho={hh.loc['SWEFFORT','spearman_rho']:+.2f} (n=51), opposite to H5; centered rho {ips.loc['SWEFFORT','rho_within_person_centered']:+.2f}; HTMT with intention 0.92",
             Former_users="Not measured", Statistical="Anomalous / inconclusive (measurement and overlap concerns)", Classification="Contradictory",
             Interpretation="Contradicts the hypothesised negative direction. UDRHP discloses delivery-partner and merchant multi-homing risks, while consumer multi-app usage is common. The survey positive correlation reflects perceived difficulty of switching away or common response bias rather than actionable structural lock-in. Switching costs remain inconclusive rather than proven negligible.",
             CRM="None (R4)"),
        dict(Factor="Satisfaction / expectation fulfilment (push)", PPM="Push",
             Academic="Mixed: L05 (A) and L10 (A) report non-significant effects; L16 (B) reports significant service/product-problem push factors",
             Zepto_evidence="[Primary, S01] p.13: S.Q.A.P. framework and ZAP customer support tool definitions; p.260: store densification to optimize delivery speed",
             Industry_evidence="None retrieved",
             Current_users=f"SAT mean {ds.loc['SAT','mean']:.2f}; rho with intention={hh.loc['SAT','spearman_rho']:.2f} (n=51), Holm p={hh.loc['SAT','p_holm_H1_H7']:.2f}",
             Former_users=f"Delivery {int(m.loc['Delivery experience','n_mentions'])}, app {int(m.loc['App experience','n_mentions'])}, customer service {int(m.loc['Customer service','n_mentions'])}, quality {int(m.loc['Product quality','n_mentions'])} of 73 mentions",
             Statistical="Inconclusive (CI includes zero and moderate effects)", Classification="Insufficient / Contextual",
             Interpretation="Satisfaction: Insufficient / Contextual — survey relationship was non-significant; UDRHP describes service-speed positioning but does not directly test satisfaction-driven switching.",
             CRM="Monitor only (R5)"),
        dict(Factor="Familiarity / inertia (mooring)", PPM="Mooring",
             Academic="Abstract-level only: L15 (B) inertia negatively affects intention; L11 (B) habit; L08 (B) inertia as moderator",
             Zepto_evidence="[Primary, S01] p.252: users expand from ~6 categories in Month 1 to 18 categories in Year 2; p.258: Zepto Pass subscription program",
             Industry_evidence="[Redseer S05] general remark that quick-commerce habits solidify (not Zepto-specific)",
             Current_users=f"FAM rho={hh.loc['FAM','spearman_rho']:.2f} (n=51); INERT rho={hh.loc['INERT','spearman_rho']:.2f} (n=46); both positive (unexpected sign), not significant",
             Former_users="Not measured", Statistical="Inconclusive (minimum detectable |rho| about 0.38-0.40)", Classification="Insufficient",
             Interpretation="Survey estimates are imprecise with unexpected signs. UDRHP shows category breadth expands with tenure, but does not provide causal evidence that habit prevents switching.",
             CRM="None (R4)"),
    ])
    tri.to_csv(C.SEC / "triangulation_matrix.csv", index=False); tri.to_csv(C.TABLES / "table18_triangulation.csv", index=False)
    fem = tri[["Factor", "PPM", "Academic", "Zepto_evidence", "Industry_evidence", "Current_users", "Former_users", "Statistical", "Classification", "CRM"]].copy()
    fem["Effect_size_note"] = ["frequency only", "rho ~0.69 (raw), fragile", "rho ~0.70 (raw), fragile", "rho ~+0.72, anomalous", "rho ~0.17, n.s.", "rho ~0.25, n.s."]
    fem.to_csv(C.SEC / "factor_evidence_matrix.csv", index=False)

    crm = pd.DataFrame([
        dict(ID="R1", Status="Recommended (conditional, testable)", Confidence="Moderate (descriptive; n=73 former, n=60 never)",
             Problem="Coverage-driven exit and non-adoption",
             Evidence=f"Primary survey: Area is the main exit reason for {A}/73 former users and the main never-use reason for {nv_area}/60; {int(rc.loc['A_coverage_primary','ge4'])}/{int(rc.loc['A_coverage_primary','n'])} coverage-primary leavers state return willingness. Secondary filing: Zepto earmarks Rs 16,289.75M for dark-store network expansion across FY27-FY29 (S01 pp. 143-145).",
             Segment="Residents of unserved localities (former class A; never-users citing area)",
             Mechanism="Serviceability waitlist; expansion-triggered reactivation; pin-code-based messaging (CRM interpretation/inference)",
             Implementation="Capture pin code at install/registration and on failed-serviceability screens; trigger a message when a dark store covering that pin code goes live; suppress if already served",
             Expected="Higher first-order conversion after a coverage launch (to be tested, not assumed)",
             KPI="Waitlist size; waitlist-to-first-order conversion; 30/90-day repeat rate of reactivated users",
             Limitations="Exit was involuntary, so this is demand capture rather than retention; item wording ambiguity; stated intention overstates behaviour"),
        dict(ID="R2", Status="Conditional (pilot with control group)", Confidence="Low-moderate (former-user descriptives; current-user association fragile)",
             Problem="Competitor pull and assortment gaps",
             Evidence=f"Primary survey: Among {nvol} voluntary-only former users, availability+variety = {volpv}/{nvol} main reasons; {altyes}/68 say the alternative had products not easily found on Zepto; H2/H3 supported on raw scores only. Secondary filing: Store-level SKUs expanded from 12,312 to 49,602 (S01 p. 162, p. 538); in-house ML recommendation engine active (p. 246).",
             Segment="Current users with repeated failed searches or out-of-stock views; multi-platform users",
             Mechanism="Restock/availability alerts; substitution recommendations; pin-code assortment personalisation (CRM interpretation/inference)",
             Implementation="Log failed searches and out-of-stock views per user; notify on restock; rank close substitutes using the existing recommendations engine (S01 p. 246 confirms capability)",
             Expected="Fewer abandoned baskets and less shifting of regular items to rivals (to be tested in pilot)",
             KPI="Repeat rate among stock-out-affected users vs control; notify-me conversion; share of regular items bought on Zepto",
             Limitations="Associational survey evidence; variety not separable from general attractiveness; recommendation engine effectiveness is a proposed test, not a proven outcome"),
        dict(ID="R3", Status="Conditional (small n; reasons with adequate counts only)", Confidence="Low",
             Problem="Win-back of voluntary former users",
             Evidence=f"Primary survey: Voluntary-only former users n={nvol}; {int(rc.loc['C_voluntary_only','ge4'])}/{int(rc.loc['C_voluntary_only','n'])} state return willingness; main reasons: availability 8, variety 8, delivery 4, app 3, discounts 3. Secondary filing: Cross-category expansion depth reaches 18 categories at 2 years (S01 p. 252).",
             Segment="Former users whose main reason was product availability or variety (n=16)",
             Mechanism="Reason-specific win-back message when the relevant category is restocked or the range is widened (CRM interpretation/inference)",
             Implementation="Match the stored exit reason (or inferred stock-out history) to a trigger; no win-back for reasons with counts of 1-3 (insufficient evidence)",
             Expected="Reactivation among the matched segment (to be tested in pilot)",
             KPI="Reactivation rate vs control; 30/90-day repeat after reactivation",
             Limitations=f"n=16 for the matched segment; stated return intention only; all-reason incentives not supported ({int(m.loc['Discounts / promotions','n_mentions'])}/73 mention discounts)"),
        dict(ID="R4", Status="Not recommended on current evidence — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure switching barriers with a validated scale before designing lock-in interventions", Confidence="-",
             Problem="Switching-cost or habit lock-in",
             Evidence="Primary survey: H5 anomalous (positive, uninterpretable rho=+0.72); H6-H7 inconclusive. Secondary filing: Delivery and merchant partner multi-homing risk disclosures (S01 pp. 27-28, 30); Zepto Pass active (p. 258). Literature: Mixed evidence on switching costs.",
             Segment="-", Mechanism="None",
             Implementation="Re-measure with a validated, reverse-worded scale before designing lock-in mechanisms",
             Expected="-", KPI="-",
             Limitations="Not recommended on current evidence — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure switching barriers with a validated scale before designing lock-in interventions"),
        dict(ID="R5", Status="Monitor only (trigger-based service recovery as a safeguard)", Confidence="Low",
             Problem="Service experience (delivery, app, support, quality)",
             Evidence=f"Primary survey: Satisfaction not significantly related to intention (inconclusive); experience reasons are minority mentions (delivery {int(m.loc['Delivery experience','n_mentions'])}/73, app {int(m.loc['App experience','n_mentions'])}/73, support {int(m.loc['Customer service','n_mentions'])}/73). Secondary filing: Store densification targets <10-15 min delivery (S01 p. 260); ZAP support tool active (p. 13).",
             Segment="Whole base",
             Mechanism="Trigger-based service recovery on failed orders using existing support processes (Operational safeguard)",
             Implementation="Track complaint-to-churn linkage before investing in dedicated service recovery programs",
             Expected="Early warning only",
             KPI="Complaint resolution time; repeat rate after a complaint",
             Limitations="Sample may under-represent service-driven exits; service recovery is a hygienic operational safeguard"),
    ])
    crm.to_csv(C.TABLES / "table19_crm_recommendations.csv", index=False); crm.to_csv(C.SEC / "crm_recommendation_matrix.csv", index=False)
    return hm, nreg, tri, crm


def run():
    return build_matrices()
