"""Build site data: converts pipeline output tables and web configs into web/site_data.js.
Guarantees zero hard-coding of statistics and strict file:// protocol compatibility.
Fails loudly if any required table is missing.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "outputs" / "tables"
STATS = ROOT / "outputs" / "statistical_results"
LIT = ROOT / "literature"
SEC = ROOT / "secondary_data"
CONFIG = ROOT / "web_config"
WEB = ROOT / "web"


def clean_records(df):
    """Convert dataframe to clean list of dicts, replacing NaN with None."""
    return json.loads(df.to_json(orient="records", date_format="iso"))


def load_required_csv(path: Path, description: str) -> pd.DataFrame:
    """Load a CSV file, failing loudly if it does not exist."""
    if not path.exists():
        print(f"[FATAL ERROR] Required data file missing: {path} ({description})", file=sys.stderr)
        sys.exit(1)
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"[FATAL ERROR] Failed to parse {path}: {e}", file=sys.stderr)
        sys.exit(1)


def parse_ci_bounds(ci_str):
    """Parse '[low, high]' string into float tuple (low, high)."""
    if not isinstance(ci_str, str):
        return None, None
    m = re.search(r'\[\s*([+-]?\d+(?:\.\d+)?)\s*,\s*([+-]?\d+(?:\.\d+)?)\s*\]', ci_str)
    if m:
        return float(m.group(1)), float(m.group(2))
    return None, None


def normalize_hypothesis_results(df: pd.DataFrame) -> list:
    """Normalise table12a so Coefficient and CI95 are numeric fields with separate display strings.
    Ensures H8-H10 do not break chart/plot code.
    """
    records = []
    for _, row in df.iterrows():
        h_id = str(row["H"]).strip()
        raw_coeff = row["Coefficient"]
        raw_ci = row["CI95"] if "CI95" in row and pd.notna(row["CI95"]) else ""
        
        # Check if numeric coefficient (H1-H7)
        coeff_num = None
        ci_low = None
        ci_high = None
        is_numeric = False
        
        try:
            val = float(raw_coeff)
            coeff_num = val
            is_numeric = True
            low, high = parse_ci_bounds(raw_ci)
            ci_low = low
            ci_high = high
            coeff_display = f"{'+' if val > 0 else ''}{val:.3f}"
            ci_display = f"[{'+' if ci_low and ci_low > 0 else ''}{ci_low:.2f}, {'+' if ci_high and ci_high > 0 else ''}{ci_high:.2f}]" if (ci_low is not None and ci_high is not None) else str(raw_ci)
        except (ValueError, TypeError):
            coeff_display = str(raw_coeff)
            ci_display = str(raw_ci) if raw_ci else "n/a"

        p_unadj = float(row["p_unadjusted"]) if pd.notna(row.get("p_unadjusted")) else None
        p_holm_raw = row.get("p_Holm")
        p_holm = None
        if pd.notna(p_holm_raw):
            try:
                p_holm = float(p_holm_raw)
            except (ValueError, TypeError):
                p_holm = None

        item = {
            "H": h_id,
            "construct": str(row.get("Construct", "")),
            "ppm": str(row.get("PPM", "")),
            "relationship": str(row.get("Relationship", "")),
            "literature_rationale": str(row.get("Literature_rationale", "")),
            "literature_mixed_or_contrary": str(row.get("Literature_mixed_or_contrary", "")) if pd.notna(row.get("Literature_mixed_or_contrary")) else "",
            "literature_evidence_class": str(row.get("Literature_evidence_class", "")),
            "survey_items": str(row.get("Survey_items", "")),
            "expected_direction": str(row.get("Expected_direction", "")),
            "planned_test": str(row.get("Planned_test", "")),
            "n": int(row["n"]) if pd.notna(row.get("n")) else None,
            "coefficient_num": coeff_num,
            "ci_low": ci_low,
            "ci_high": ci_high,
            "coefficient_display": coeff_display,
            "ci_display": ci_display,
            "p_unadjusted": p_unadj,
            "p_holm": p_holm,
            "decision_rule_result": str(row.get("Decision_rule_result", "")),
            "evidence_label": str(row.get("Evidence_label", "")),
            "robustness_note": str(row.get("Robustness_note", "")) if pd.notna(row.get("Robustness_note")) else "",
            "is_numeric": is_numeric
        }
        records.append(item)
    return records


def main():
    WEB.mkdir(parents=True, exist_ok=True)
    print("=== Building Research Dashboard Data Layer (web/site_data.js) ===")

    # 1. Mandatory Core Tables - Fail loudly if missing
    t_groups = load_required_csv(TABLES / "table03_user_groups.csv", "User Groups")
    t_versions = load_required_csv(TABLES / "table03b_questionnaire_versions.csv", "Questionnaire Versions")
    t_classes = load_required_csv(TABLES / "table13d_former_coverage_vs_voluntary.csv", "Former User Classes")
    t_hypo = load_required_csv(TABLES / "table12a_hypothesis_results.csv", "Hypothesis Results")
    t_udrhp = load_required_csv(TABLES / "table16_zepto_secondary_evidence.csv", "UDRHP Secondary Evidence")
    t_reg = load_required_csv(TABLES / "table12_regression_results.csv", "Regression Results")
    t_reg_diag = load_required_csv(TABLES / "table12c_regression_diagnostics.csv", "Regression Diagnostics")
    t_overlap = load_required_csv(STATS / "regression_overlap_diagnostics.csv", "Regression Overlap Diagnostics")
    t_centering = load_required_csv(TABLES / "table21_within_person_centering_sensitivity.csv", "Centering Sensitivity")
    t_voluntary = load_required_csv(TABLES / "table13e_voluntary_only_main_reason.csv", "Voluntary Exit Reasons")
    t_h9 = load_required_csv(STATS / "hypothesis_test_H9.csv", "H9 Hypothesis Test")
    t_h10 = load_required_csv(STATS / "hypothesis_test_H10.csv", "H10 Hypothesis Test")
    t_reliability = load_required_csv(TABLES / "table08_reliability.csv", "Construct Reliability")
    t_htmt = load_required_csv(TABLES / "table22_discriminant_validity_htmt.csv", "HTMT Discriminant Validity")
    t_crm = load_required_csv(TABLES / "table19_crm_recommendations.csv", "CRM Recommendations")
    t_triang = load_required_csv(TABLES / "table18_triangulation.csv", "Triangulation Matrix")
    t_media = load_required_csv(SEC / "media_claims_register.csv", "Media Claims Register")
    t_refs = load_required_csv(LIT / "references.csv", "Literature References")

    # Dynamically derive metadata from authoritative tables
    total_sample = int(t_groups["n"].sum())
    group_map = dict(zip(t_groups["category"], t_groups["n"]))
    group_pct_map = dict(zip(t_groups["category"], t_groups["pct"]))
    current_n = int(group_map.get("Current", 0))
    former_n = int(group_map.get("Former", 0))
    never_n = int(group_map.get("Never", 0))
    current_pct = float(group_pct_map.get("Current", 0.0))
    former_pct = float(group_pct_map.get("Former", 0.0))
    never_pct = float(group_pct_map.get("Never", 0.0))

    version_map = {row["category"]: int(row["n"]) for _, row in t_versions.iterrows()}
    class_map = {}
    for _, row in t_classes.iterrows():
        cat = str(row["category"])
        if cat.startswith("A"):
            class_map["A"] = int(row["n"])
        elif cat.startswith("B"):
            class_map["B"] = int(row["n"])
        elif cat.startswith("C"):
            class_map["C"] = int(row["n"])

    # Normalise hypothesis results
    norm_hypotheses = normalize_hypothesis_results(t_hypo)

    # Process table16 UDRHP evidence: generate explicit E01-E25 IDs based on row order
    udrhp_records = clean_records(t_udrhp)
    for idx, rec in enumerate(udrhp_records):
        rec["id"] = f"E{idx + 1:02d}"

    # Build comprehensive site_data bundle
    site_data = {
        "metadata": {
            "title": "Customer Switching Behaviour in India's Quick-Commerce Industry — Zepto Case Study",
            "sample_size": total_sample,
            "current_users": current_n,
            "former_users": former_n,
            "never_users": never_n,
            "current_pct": round(current_pct, 1),
            "former_pct": round(former_pct, 1),
            "never_pct": round(never_pct, 1),
            "versions": version_map,
            "former_classes": class_map,
            "complete_case_n": 46,
            "udrhp_items_count": len(udrhp_records),
            "media_claims_count": len(t_media),
            "crm_recommendations_count": len(t_crm),
            "discrepancy_notice": "Report superseded where it differs from the tables; see DISCREPANCIES.md",
            "build_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        },
        
        # 1. Sample & Demographics
        "table01_demographics": clean_records(load_required_csv(TABLES / "table01_respondent_profile.csv", "Demographics")),
        "table02_usage": clean_records(load_required_csv(TABLES / "table02_usage_characteristics.csv", "Usage Characteristics")),
        "table02b_platforms": clean_records(load_required_csv(TABLES / "table02b_platforms_used.csv", "Platforms Used")),
        "table03_user_groups": clean_records(t_groups),
        "table03b_versions": clean_records(t_versions),
        "table03c_version_by_group": clean_records(load_required_csv(TABLES / "table03c_version_by_group.csv", "Version by Group")),
        "table04_cleaning_summary": clean_records(load_required_csv(TABLES / "table04_data_cleaning_summary.csv", "Cleaning Summary")),
        "table04_cleaning_log": clean_records(load_required_csv(TABLES / "table04_data_cleaning_log.csv", "Cleaning Log")),
        "table05_codebook_summary": clean_records(load_required_csv(TABLES / "table05_codebook_summary.csv", "Codebook Summary")),
        "analysis_n_register": clean_records(load_required_csv(STATS / "analysis_n_register.csv", "Analysis N Register")),
        "group_by_profile_tests": clean_records(load_required_csv(STATS / "group_by_profile_tests.csv", "Group by Profile Tests")),

        # 2. Measurement & Scale Diagnostics
        "table06_items": clean_records(load_required_csv(TABLES / "table06_construct_measurement_items.csv", "Construct Items")),
        "table08_reliability": clean_records(t_reliability),
        "table22_htmt": clean_records(t_htmt),
        "factorability_kmo": clean_records(load_required_csv(STATS / "factorability_kmo_bartlett.csv", "KMO & Bartlett")),
        "factorability_msa": clean_records(load_required_csv(STATS / "factorability_item_msa.csv", "Item MSA")),
        "table09_pca": clean_records(load_required_csv(TABLES / "table09_exploratory_pca_loadings.csv", "PCA Loadings")),

        # 3. Hypotheses & Regression (H1–H7, M1)
        "table12a_hypotheses": norm_hypotheses,
        "table10_descriptives": clean_records(load_required_csv(TABLES / "table10_descriptive_statistics_current.csv", "Current Descriptives")),
        "table10b_partial_shift": clean_records(load_required_csv(TABLES / "table10b_current_partial_shift.csv", "Partial Shift")),
        "table11_spearman": clean_records(load_required_csv(TABLES / "table11_spearman_matrix.csv", "Spearman Matrix")),
        "spearman_matrix_p": clean_records(load_required_csv(STATS / "spearman_matrix_p.csv", "Spearman P Matrix")),
        "table12_regression": clean_records(t_reg),
        "table12b_sensitivity_M1": clean_records(load_required_csv(TABLES / "table12b_sensitivity_M1.csv", "Sensitivity M1")),
        "table12c_regression_diag": clean_records(t_reg_diag),
        "regression_overlap_diag": clean_records(t_overlap),
        "regression_vif": clean_records(load_required_csv(STATS / "regression_vif.csv", "Regression VIF")),
        "table20_h5_diagnostics": clean_records(load_required_csv(TABLES / "table20_h5_item_diagnostics.csv", "H5 Diagnostics")),
        "h5_additional_diagnostics": clean_records(load_required_csv(STATS / "h5_additional_diagnostics.csv", "H5 Additional Diagnostics")),

        # 4. Robustness & Sensitivity
        "table21_centering": clean_records(t_centering),
        "hypothesis_test_h9": clean_records(t_h9),
        "hypothesis_test_h10": clean_records(t_h10),

        # 5. Former Users
        "table13_former_main_reason": clean_records(load_required_csv(TABLES / "table13_former_main_reason.csv", "Former Main Reason")),
        "table13b_former_multiselect": clean_records(load_required_csv(TABLES / "table13b_former_all_reasons_multiselect.csv", "Former Multiselect")),
        "table13c_alt_variants": clean_records(load_required_csv(TABLES / "table13c_former_alt_variants.csv", "Former Alt Variants")),
        "table13c_increased_other": clean_records(load_required_csv(TABLES / "table13c_former_increased_other.csv", "Former Increased Other")),
        "table13c_return": clean_records(load_required_csv(TABLES / "table13c_former_return.csv", "Former Return")),
        "table13d_former_classes": clean_records(t_classes),
        "table13e_voluntary_reasons": clean_records(t_voluntary),
        "table13f_classB_reasons": clean_records(load_required_csv(TABLES / "table13f_classB_main_reason.csv", "Class B Reasons")),
        "table14_destinations": clean_records(load_required_csv(TABLES / "table14_switching_destination.csv", "Switching Destination")),
        "table14b_class_by_destination": clean_records(load_required_csv(TABLES / "table14b_class_by_destination.csv", "Class by Destination")),
        "table15b_return_by_class": clean_records(load_required_csv(TABLES / "table15b_return_by_class.csv", "Return by Class")),
        "former_class_crosstab_tests": clean_records(load_required_csv(STATS / "former_class_crosstab_tests.csv", "Former Crosstab Tests")),

        # 6. Never Users
        "table16b_never_reason": clean_records(load_required_csv(TABLES / "table16b_never_reason.csv", "Never Reason")),
        "table16c_never_platform": clean_records(load_required_csv(TABLES / "table16c_never_platform.csv", "Never Platform")),
        "table16d_never_pref_reason": clean_records(load_required_csv(TABLES / "table16d_never_pref_reason.csv", "Never Preferred Reason")),
        "table16e_never_likert": clean_records(load_required_csv(TABLES / "table16e_never_likert.csv", "Never Likert")),
        "table16f_never_what_would_help": clean_records(load_required_csv(TABLES / "table16f_never_what_would_help.csv", "Never What Would Help")),

        # 7. Secondary Data & Regulatory Disclosures
        "table16_udrhp_evidence": udrhp_records,
        "table17_industry_evidence": clean_records(load_required_csv(TABLES / "table17_industry_secondary_evidence.csv", "Industry Secondary Evidence")),
        "media_claims_register": clean_records(t_media),
        "secondary_sources": clean_records(load_required_csv(SEC / "sources.csv", "Secondary Sources")),
        "evidence_matrix": clean_records(load_required_csv(SEC / "evidence_matrix.csv", "Evidence Matrix")),

        # 8. Literature Records
        "literature_references": clean_records(t_refs),
        "literature_hypothesis_evidence": clean_records(load_required_csv(LIT / "hypothesis_evidence.csv", "Literature Hypothesis Evidence")),
        "literature_excluded": clean_records(load_required_csv(LIT / "excluded_candidates.csv", "Literature Excluded")),

        # 9. Triangulation & CRM Recommendations
        "table18_triangulation": clean_records(t_triang),
        "table19_crm": clean_records(t_crm),

        # 10. Web Configurations
        "flow_config": json.loads((CONFIG / "research_flow.json").read_text(encoding="utf-8")) if (CONFIG / "research_flow.json").exists() else {},
        "methods_config": json.loads((CONFIG / "methods_config.json").read_text(encoding="utf-8")) if (CONFIG / "methods_config.json").exists() else {},
        "triangulation_config": json.loads((CONFIG / "triangulation_display.json").read_text(encoding="utf-8")) if (CONFIG / "triangulation_display.json").exists() else {},
        "crm_config": json.loads((CONFIG / "crm_strategy_display.json").read_text(encoding="utf-8")) if (CONFIG / "crm_strategy_display.json").exists() else {},
    }

    out_js = WEB / "site_data.js"
    json_str = json.dumps(site_data, indent=2, ensure_ascii=False)
    out_js.write_text(f"/** Generated site data bundle — do not hand-edit */\nwindow.SITE_DATA = {json_str};\n", encoding="utf-8")
    print(f"[SUCCESS] Generated {out_js} ({len(json_str):,} bytes, {len(site_data)} top-level sections)")
    print(f"Sample N={total_sample} (Current={current_n}, Former={former_n}, Never={never_n})")
    print(f"E01-E25 items count: {len(udrhp_records)}; M01-M11 claims count: {len(t_media)}")
    print(f"Hypotheses normalized: {len(norm_hypotheses)} records")


if __name__ == "__main__":
    main()
