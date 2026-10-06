"""Data cleaning: raw CSV -> cleaned dataset + analysis datasets + cleaning log.

Raw CSV is never modified. Structural missingness is kept as NaN (never zero).
"""
import re
import numpy as np
import pandas as pd
from . import config as C


def load_raw() -> pd.DataFrame:
    raw = pd.read_csv(C.RAW_CSV)
    if raw.shape[1] != len(C.COLS):
        raise ValueError(f"Expected {len(C.COLS)} columns, found {raw.shape[1]}")
    return raw


def clean(raw: pd.DataFrame):
    log = []

    def add(step, rule, ids, action, why):
        ids = list(map(int, ids))
        log.append(dict(step=step, rule=rule, n_rows=len(ids),
                        response_ids=";".join(map(str, ids)) if len(ids) <= 60 else f"{len(ids)} rows (see cleaned data flag)",
                        action=action, rationale=why))

    df = raw.copy()
    orig_cols = list(df.columns)
    # 1. standardise names (raw header whitespace stripped, mapped to short names)
    stripped = [c.strip() for c in orig_cols]
    exp = [t.strip().lstrip(". ").strip() for _, t in C.COLS]
    got = [s.lstrip(". ").strip() for s in stripped]
    if got != exp:
        raise ValueError("Column headers differ from expected questionnaire; check config.COLS")
    df.columns = C.CLEAN_NAMES
    add("C01", "Header standardisation", [], "Renamed 37 columns to short names; whitespace/leading '. ' removed",
        "10 headers carried stray spaces; original text preserved in codebook")

    df.insert(0, "resp_id", np.arange(1, len(df) + 1))
    df["timestamp_dt"] = pd.to_datetime(df["timestamp"].str.replace(" GMT+5:30", "", regex=False),
                                        format="%Y/%m/%d %I:%M:%S %p")
    if not df["timestamp_dt"].is_monotonic_increasing:
        raise ValueError("Timestamps not chronological; version assignment by row order invalid")
    df["questionnaire_version"] = df["resp_id"].map(C.version_of)
    add("C02", "Questionnaire version", df.index[df.questionnaire_version != "V2"] + 1,
        "Added questionnaire_version (V1: 1-16; V1.5: 17-22; V2: 23-184)",
        "Version boundaries from timestamps (21 Aug vs 11 Sep) and observed item availability")

    df["group"] = df["ever_used_zepto"].map(C.GROUP_MAP)
    if df["group"].isna().any():
        raise ValueError("Unmapped Zepto-usage category")

    # 2. whitespace trim in text cells
    for c in df.select_dtypes(include=["object", "string"]).columns:
        df[c] = df[c].astype("object").where(df[c].isna(), df[c].astype(str).str.strip())

    # 3. duplicates
    dup = df.drop(columns=["resp_id", "timestamp", "timestamp_dt"]).duplicated(keep=False)
    add("C03", "Duplicate check (all answer columns)", df.index[dup] + 1, "None found; no rows removed",
        "0 duplicate answer patterns; timestamps unique")

    # 4. Likert validation
    bad = []
    for c in C.CURRENT_LIKERT + ["nu_current_better", "nu_consider_trying"]:
        v = df[c].dropna()
        if not v.between(1, 5).all() or not (v == v.round()).all():
            bad.append(c)
    add("C04", "Likert range check (1-5 integers)", [], f"Invalid columns: {bad or 'none'}", "No impossible values")

    # 5. structural missingness flags
    df["sm_added_later"] = df["questionnaire_version"].isin(["V1", "V1.5"]) & df["resp_id"].le(16)
    df["missing_VAR2_INERT1_structural"] = (df["group"] == "Current") & df["VAR2"].isna() & df["INERT1"].isna()
    df["missing_loc_spend_structural"] = df["location_type"].isna() & df["monthly_spend"].isna() & df["resp_id"].le(16)
    df["missing_fu_ext_structural"] = (df["group"] == "Former") & df["fu_alt_variants"].isna() & df["fu_return"].isna()
    ids = df.index[df.missing_VAR2_INERT1_structural] + 1
    add("C05", "Structural missing: VAR2 & INERT1 not asked in V1", ids, "Left as NaN; flagged", "Items added after V1; not zero, not respondent error")
    ids = df.index[df.missing_fu_ext_structural] + 1
    add("C06", "Structural missing: fu_alt_variants & fu_return not asked in V1", ids, "Left as NaN; flagged", "Items added after V1")
    ids = df.index[df.missing_loc_spend_structural] + 1
    add("C07", "Structural missing: location_type & monthly_spend not asked in V1", ids, "Left as NaN; flagged", "Items added after V1 (all 16 V1 respondents)")

    # 6. routing leaks
    df["leak_former_block"] = (df["group"] == "Current") & df[C.FORMER_BLOCK].notna().any(axis=1)
    df["leak_never_block"] = df["group"].isin(["Current", "Former"]) & df[C.NEVER_BLOCK].notna().any(axis=1)
    df["leak_any"] = df.leak_former_block | df.leak_never_block
    add("C08", "Routing leak: current users answered former-user block (Q21-26)", df.index[df.leak_former_block] + 1,
        "Cells kept in cleaned data with flag; removed from primary analysis datasets; reported as supplementary (n=7)",
        "Out-of-branch answers cannot be pooled with former users, but may describe partial switching by current users")
    add("C09", "Routing leak: current/former users answered never-user block (Q27-32)",
        df.index[df.leak_never_block] + 1,
        "Cells kept with flag; excluded from never-user analysis and from models (15 respondents: 7 current + 8 former)",
        "Out-of-branch; never-user items are about a platform other than Zepto")
    add("C09b", "Routing leak reconciliation: UNIQUE respondents affected (leak_any)", df.index[df.leak_any] + 1,
        "15 unique respondents (all among responses 2-22). The 7 current users who answered the former-user block ALSO answered the never-user block, so block-level instances = 7 + 15 = 22, but unique respondents = 15",
        "Earlier '22 routing leaks' counted block-level incidents (double-counting the 7); 22 also coincides with the size of V1+V1.5 by chance")
    df["q1_zepto_ticked"] = df["platforms_used"].fillna("").str.contains("Zepto")
    df["flag_q1_inconsistent"] = ((df.group.isin(["Current", "Former"])) & ~df.q1_zepto_ticked & df.platforms_used.notna()) | \
                                 ((df.group == "Never") & df.q1_zepto_ticked)
    add("C10", "Q1 inconsistency (Zepto not listed by current/former; listed by never-users)",
        df.index[df.flag_q1_inconsistent] + 1, "Flagged; retained; sensitivity analysis", "Q1 is not used in inferential models; may reflect wording ('used' vs 'currently use')")
    df["flag_q1_none"] = df["platforms_used"].fillna("").str.contains("None") & df["platforms_used"].fillna("").str.contains("Zepto")
    add("C11", "Contradictory multi-select ('Zepto;None')", df.index[df.flag_q1_none] + 1, "Flagged; retained", "Single contradictory tick; Q1 descriptive only")
    df["flag_nu_platform_contradiction"] = (df["qc_frequency"].str.contains("don't currently")) & df["nu_platform"].notna() & \
                                            ~df["nu_platform"].fillna("").str.contains("don't regularly")
    add("C12", "Never-user says no QC use (Q2) yet names a platform used most (Q28)", df.index[df.flag_nu_platform_contradiction] + 1,
        "Flagged; retained", "Ambiguous rather than impossible ('currently' vs 'most often')")

    # 7. straight-lining (current users, 13 shared Likert items; exclude VAR2/INERT1 structurally missing items)
    sl_items = ["SAT1", "SAT2", "PUSH_consider", "ALT1", "ALT2", "VAR1", "PROMO1", "SC1", "FAM1", "SC2", "INT1", "INT2", "INT3"]
    cur = df["group"] == "Current"
    sl = df.loc[cur, sl_items].nunique(axis=1).eq(1)
    df["flag_straightline"] = False
    df.loc[sl[sl].index, "flag_straightline"] = True
    df["straightline_value"] = np.nan
    df.loc[sl[sl].index, "straightline_value"] = df.loc[sl[sl].index, "SAT1"]
    add("C13", "Straight-lining across 13 current-user Likert items", df.index[df.flag_straightline] + 1,
        "Flagged; retained; sensitivity analysis with/without",
        "Item set mixes satisfaction (positive), barrier and switching-propensity wording, so a constant pattern is ambiguous (neutrality vs acquiescence)")

    # 8. multi-select splits
    for src, prefix in [("fu_reasons", "fu_r_"), ("platforms_used", "used_"), ("nu_what_would", "nu_w_")]:
        s = df[src].dropna().str.split(";")
        levels = sorted({x.strip() for lst in s for x in lst})
        for lv in levels:
            col = prefix + re.sub(r"[^a-z0-9]+", "_", lv.lower()).strip("_")
            df[col] = np.where(df[src].isna(), np.nan, df[src].fillna("").apply(lambda t: float(lv in [x.strip() for x in t.split(";")])))
    add("C14", "Multi-select splitting", [], "Indicator columns created for platforms_used, fu_reasons, nu_what_would",
        "Enables frequency tables; source columns retained")

    # 9. ordinal encodings
    df["fu_return_num"] = df["fu_return"].map(C.RETURN_MAP)
    df["age_ord"] = df["age_group"].map({a: i for i, a in enumerate(C.AGE_ORDER)})
    df["spend_ord"] = df["monthly_spend"].map({a: i for i, a in enumerate(C.SPEND_ORDER)})
    df["freq_ord"] = df["qc_frequency"].map({a: i for i, a in enumerate(C.FREQ_ORDER)})
    df["shifted_any_num"] = df["shifted_any"].map({"Yes": 1, "No": 0})
    df["is_student"] = (df["occupation"] == "Student").astype(int)
    df["age_18_24"] = (df["age_group"] == "18–24").astype(int)
    df["metro"] = np.where(df["location_type"].isna(), np.nan, (df["location_type"] == "Metro city").astype(float))
    add("C15", "Ordinal/binary encodings", [], "fu_return_num (1-5), age_ord, spend_ord, freq_ord, shifted_any_num, is_student, metro",
        "Missing stays NaN")

    # 10. former-user reason classification (coverage vs voluntary)
    f = df["group"] == "Former"
    area_any = df["fu_reasons"].fillna("").str.contains("not available in my area")
    area_primary = df["fu_main_reason"] == "Availability in my area"
    df["fu_class"] = np.select(
        [f & area_primary, f & area_any & ~area_primary, f & ~area_any & ~area_primary],
        ["A_coverage_primary", "B_coverage_mentioned_other_primary", "C_voluntary_only"], default=None)
    df.loc[~f, "fu_class"] = np.nan
    df["fu_reason_main_inconsistent"] = f & area_primary & ~area_any
    add("C16", "Former-user classification: coverage-driven vs voluntary", df.index[f] + 1,
        "A=area is single most important reason; B=area mentioned in Q21 but other main reason; C=no area mention and other main reason",
        "Separates service-coverage constraint from voluntary platform choice. 'Availability in my area' may be read as product availability locally; ambiguity noted")

    # 11. exclusions
    add("C17", "Exclusions", [], "NONE of 184 responses excluded", "No duplicates, impossible values or empty responses; issues flagged and handled by sensitivity analysis")

    # analysis datasets
    cur_df = df[df.group == "Current"].copy()
    cur_df["oob_former_block_present"] = cur_df.leak_former_block
    supp_cur_leak = cur_df.loc[cur_df.leak_former_block, ["resp_id", "questionnaire_version", "shifted_any"] + C.FORMER_BLOCK_EXT].copy()
    cur_df[C.FORMER_BLOCK_EXT + C.NEVER_BLOCK] = np.nan  # out-of-branch cells not used in primary analysis
    frm_df = df[df.group == "Former"].copy()
    supp_frm_leak = frm_df.loc[frm_df.leak_never_block, ["resp_id", "questionnaire_version"] + C.NEVER_BLOCK].copy()
    frm_df[C.NEVER_BLOCK] = np.nan
    nev_df = df[df.group == "Never"].copy()
    return df, cur_df, frm_df, nev_df, supp_cur_leak, supp_frm_leak, pd.DataFrame(log)


def run():
    C.CLEAN_DIR.mkdir(parents=True, exist_ok=True)
    C.PROC_DIR.mkdir(parents=True, exist_ok=True)
    C.DOCS.mkdir(parents=True, exist_ok=True)
    raw = load_raw()
    df, cur, frm, nev, sc, sf, log = clean(raw)
    df.to_csv(C.CLEAN_DIR / "survey_cleaned_all184.csv", index=False)
    cur.to_csv(C.PROC_DIR / "analysis_current_users.csv", index=False)
    frm.to_csv(C.PROC_DIR / "analysis_former_users.csv", index=False)
    nev.to_csv(C.PROC_DIR / "analysis_never_users.csv", index=False)
    sc.to_csv(C.PROC_DIR / "supplementary_current_users_leaked_former_block.csv", index=False)
    sf.to_csv(C.PROC_DIR / "supplementary_former_users_leaked_never_block.csv", index=False)
    with pd.ExcelWriter(C.DOCS / "cleaning_log.xlsx") as xw:
        log.to_excel(xw, sheet_name="cleaning_log", index=False)
        summ = pd.DataFrame({
            "metric": ["rows", "columns_raw", "current", "former", "never", "V1", "V1.5", "V2", "routing_leak_unique_respondents", "routing_leak_block_instances", "routing_leak_former_block_respondents", "routing_leak_never_block_respondents", "straight_liners",
                       "q1_inconsistent", "exclusions"],
            "value": [len(df), raw.shape[1], (df.group == "Current").sum(), (df.group == "Former").sum(), (df.group == "Never").sum(),
                      (df.questionnaire_version == "V1").sum(), (df.questionnaire_version == "V1.5").sum(),
                      (df.questionnaire_version == "V2").sum(), df.leak_any.sum(), int(df.leak_former_block.sum() + df.leak_never_block.sum()),
                      df.leak_former_block.sum(), df.leak_never_block.sum(), df.flag_straightline.sum(),
                      df.flag_q1_inconsistent.sum(), 0]})
        summ.to_excel(xw, sheet_name="summary", index=False)
    log.to_csv(C.TABLES / "table04_data_cleaning_log.csv", index=False)
    summ.to_csv(C.TABLES / "table04_data_cleaning_summary.csv", index=False)
    return df, cur, frm, nev, sc, sf, log
