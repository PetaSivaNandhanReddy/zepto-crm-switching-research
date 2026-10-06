"""Codebook / data dictionary generation."""
import pandas as pd
from . import config as C

ROLE = {
 "timestamp": ("Metadata", "-", "ID", "Timestamp; used for version assignment"),
 "platforms_used": ("Usage", "-", "Profile", "Multi-select; split into used_* indicators; descriptive only"),
 "qc_frequency": ("Usage", "-", "Profile/control", "Ordinal (6 levels) -> freq_ord"),
 "choice_factor": ("Choice drivers", "-", "Descriptive", "Nominal, all 184"),
 "ever_used_zepto": ("Group", "-", "Group definition", "Current/Former/Never"),
 "SAT1": ("Satisfaction", "Push", "Predictor", "Likert 1-5"), "SAT2": ("Satisfaction", "Push", "Predictor", "Likert 1-5"),
 "PUSH_consider": ("Push (single item)", "Push", "Descriptive/sensitivity", "Overlaps conceptually with intention; not in models"),
 "ALT1": ("Alternative attractiveness", "Pull", "Predictor", "Likert 1-5"), "ALT2": ("Alternative attractiveness", "Pull", "Predictor", "Likert 1-5"),
 "VAR1": ("Competitor variety", "Pull", "Predictor", "Likert 1-5"), "VAR2": ("Competitor variety", "Pull", "Predictor", "Added after V1 (structural missing n=5)"),
 "PROMO1": ("Promotional attractiveness", "Pull", "Predictor", "Single item"),
 "SC1": ("Switching effort", "Mooring", "Predictor", "Likert 1-5"), "SC2": ("Switching effort", "Mooring", "Predictor", "Likert 1-5"),
 "FAM1": ("Familiarity", "Mooring", "Predictor", "Single item"), "INERT1": ("Inertia", "Mooring", "Predictor (extension)", "Added after V1 (n=46)"),
 "INT1": ("Switching intention", "Outcome", "Outcome", "Likert 1-5"), "INT2": ("Switching intention", "Outcome", "Outcome", "Likert 1-5"), "INT3": ("Switching intention", "Outcome", "Outcome", "Likert 1-5"),
 "shifted_any": ("Partial switching behaviour", "Outcome", "Outcome (behavioural)", "Binary; current users only"),
 "fu_reasons": ("Reasons for stopping", "-", "Descriptive", "Multi-select; former users; split to fu_r_*"),
 "fu_destination": ("Destination platform", "-", "Descriptive", "Former users"),
 "fu_main_reason": ("Main reason", "-", "Descriptive / classification", "Former users; basis of coverage vs voluntary class"),
 "fu_increased_other": ("Increased use of other platform", "-", "Descriptive", "Former users"),
 "fu_alt_variants": ("Alternative offered products not found on Zepto", "Pull (behavioural)", "Descriptive", "Added after V1 (former n=68)"),
 "fu_return": ("Willingness to return", "Retention", "Outcome (former)", "Ordinal -> fu_return_num; added after V1"),
 "nu_reason": ("Reason for never using", "-", "Supplementary", "Never-users"), "nu_platform": ("Platform used most", "-", "Supplementary", "Never-users"),
 "nu_pref_reason": ("Why prefer current platform", "-", "Supplementary", "Never-users"), "nu_current_better": ("Current platform better", "-", "Supplementary", "Likert; never-users"),
 "nu_consider_trying": ("Would consider trying Zepto", "-", "Supplementary", "Likert; never-users"), "nu_what_would": ("What would make you try Zepto", "-", "Supplementary", "Multi-select"),
 "age_group": ("Age", "-", "Profile/control", "Ordinal"), "occupation": ("Occupation", "-", "Profile/control", "Nominal"),
 "location_type": ("Location", "-", "Profile/control", "Added after V1 (n=168)"), "monthly_spend": ("Monthly QC spend", "-", "Profile/control", "Ordinal; added after V1 (n=168)"),
}
SCALE = {"Likert": "1=Strongly disagree ... 5=Strongly agree"}


def run(df):
    rows = []
    for i, (clean, raw) in enumerate(C.COLS):
        con, ppm, role, note = ROLE.get(clean, ("", "", "", ""))
        col = df[clean]
        vals = col.dropna()
        likert = clean in C.CURRENT_LIKERT or clean in ("nu_current_better", "nu_consider_trying")
        rows.append(dict(raw_column_position=i + 1, original_column=raw, clean_variable=clean,
                         variable_type="Likert (ordinal 1-5)" if likert else ("binary" if clean == "shifted_any" else "categorical/text"),
                         response_scale=SCALE["Likert"] if likert else "", n_non_missing=len(vals), n_unique=vals.nunique(),
                         coding="as recorded (1-5)" if likert else "text; see derived columns", construct=con, ppm_dimension=ppm,
                         role=role, missing_treatment="Structural NaN by branch or questionnaire version; never coded as zero",
                         analysis_usage=note, inclusion_reason="Used in the analytical sample named in role/notes" if role else ""))
    dd = pd.DataFrame(rows)
    derived = pd.DataFrame([
        ("resp_id", "Row order = chronological order (1-184)"), ("questionnaire_version", "V1 (1-16), V1.5 (17-22), V2 (23-184)"),
        ("group", "Current/Former/Never"), ("leak_former_block / leak_never_block / leak_any", "Out-of-branch answers flagged"),
        ("flag_q1_inconsistent", "Zepto tick inconsistent with group"), ("flag_straightline", "Same answer on 13 current-user Likert items"),
        ("fu_class", "A coverage primary / B coverage mentioned, other primary / C voluntary only"),
        ("SAT, ALT, VAR, PROMO, SWEFFORT, FAM, INERT, PULL, INT", "Item-mean composites (PULL needs >=4 of 5 items)"),
        ("fu_return_num", "Definitely No=1 ... Definitely Yes=5"), ("age_ord, spend_ord, freq_ord", "Ordinal codes"),
        ("shifted_any_num", "Yes=1, No=0"), ("metro", "Metro city=1; other=0; NaN if not asked (V1)"),
    ], columns=["derived_variable", "definition"])
    with pd.ExcelWriter(C.DOCS / "data_dictionary.xlsx") as xw:
        dd.to_excel(xw, sheet_name="codebook", index=False)
        derived.to_excel(xw, sheet_name="derived_variables", index=False)
    dd.to_csv(C.TABLES / "table05_codebook_summary.csv", index=False)
    cons = pd.DataFrame([dict(construct=k, label=v["label"], ppm=v["ppm"], items=", ".join(v["items"]), n_items=len(v["items"])) for k, v in C.CONSTRUCTS.items()])
    cons.to_csv(C.TABLES / "table06_construct_measurement_items.csv", index=False)
    return dd
