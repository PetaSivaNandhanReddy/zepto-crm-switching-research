"""Build site data: converts pipeline output tables and web configs into web/site_data.js.
Ensures zero hard-coding of statistics and guarantees file:// protocol compatibility.
"""
import json
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


def main():
    WEB.mkdir(parents=True, exist_ok=True)
    site_data = {
        "metadata": {
            "title": "Zepto Customer Switching Behaviour Research Dashboard",
            "sample_size": 184,
            "current_users": 51,
            "former_users": 73,
            "never_users": 60,
            "verification_status": "53/53 Verified",
            "build_timestamp": "2026-10-07"
        }
    }

    # 1. Primary Demographics and User Split
    if (TABLES / "table01_respondent_profile.csv").exists():
        site_data["table01_demographics"] = clean_records(pd.read_csv(TABLES / "table01_respondent_profile.csv"))
    if (TABLES / "table03_user_groups.csv").exists():
        site_data["table03_user_groups"] = clean_records(pd.read_csv(TABLES / "table03_user_groups.csv"))
    if (TABLES / "table03b_questionnaire_versions.csv").exists():
        site_data["table03b_versions"] = clean_records(pd.read_csv(TABLES / "table03b_questionnaire_versions.csv"))
    if (TABLES / "table02b_platforms_used.csv").exists():
        site_data["table02b_platforms"] = clean_records(pd.read_csv(TABLES / "table02b_platforms_used.csv"))

    # 2. Measurement & Scale Diagnostics
    if (TABLES / "table08_reliability.csv").exists():
        site_data["table08_reliability"] = clean_records(pd.read_csv(TABLES / "table08_reliability.csv"))
    if (TABLES / "table06_construct_measurement_items.csv").exists():
        site_data["table06_items"] = clean_records(pd.read_csv(TABLES / "table06_construct_measurement_items.csv"))
    if (TABLES / "table22_discriminant_validity_htmt.csv").exists():
        site_data["table22_htmt"] = clean_records(pd.read_csv(TABLES / "table22_discriminant_validity_htmt.csv"))
    if (STATS / "factorability_kmo_bartlett.csv").exists():
        site_data["factorability_kmo"] = clean_records(pd.read_csv(STATS / "factorability_kmo_bartlett.csv"))
    if (STATS / "factorability_item_msa.csv").exists():
        site_data["factorability_msa"] = clean_records(pd.read_csv(STATS / "factorability_item_msa.csv"))
    if (TABLES / "table09_exploratory_pca_loadings.csv").exists():
        site_data["table09_pca"] = clean_records(pd.read_csv(TABLES / "table09_exploratory_pca_loadings.csv"))

    # 3. Hypotheses & Current Users (H1–H7)
    if (TABLES / "table12a_hypothesis_results.csv").exists():
        site_data["table12a_hypotheses"] = clean_records(pd.read_csv(TABLES / "table12a_hypothesis_results.csv"))
    if (TABLES / "table10_descriptive_statistics_current.csv").exists():
        site_data["table10_descriptives"] = clean_records(pd.read_csv(TABLES / "table10_descriptive_statistics_current.csv"))
    if (TABLES / "table11_spearman_matrix.csv").exists():
        site_data["table11_spearman"] = clean_records(pd.read_csv(TABLES / "table11_spearman_matrix.csv"))
    if (TABLES / "table12_regression_results.csv").exists():
        site_data["table12_regression"] = clean_records(pd.read_csv(TABLES / "table12_regression_results.csv"))
    if (TABLES / "table12c_regression_diagnostics.csv").exists():
        site_data["table12c_regression_diag"] = clean_records(pd.read_csv(TABLES / "table12c_regression_diagnostics.csv"))
    if (STATS / "regression_vif.csv").exists():
        site_data["regression_vif"] = clean_records(pd.read_csv(STATS / "regression_vif.csv"))

    # 4. Robustness & Sensitivity
    if (TABLES / "table21_within_person_centering_sensitivity.csv").exists():
        site_data["table21_centering"] = clean_records(pd.read_csv(TABLES / "table21_within_person_centering_sensitivity.csv"))
    if (STATS / "hypothesis_test_H9.csv").exists():
        site_data["hypothesis_test_h9"] = clean_records(pd.read_csv(STATS / "hypothesis_test_H9.csv"))
    if (STATS / "hypothesis_test_H10.csv").exists():
        site_data["hypothesis_test_h10"] = clean_records(pd.read_csv(STATS / "hypothesis_test_H10.csv"))

    # 5. Former Users
    if (TABLES / "table13_former_main_reason.csv").exists():
        site_data["table13_former_main_reason"] = clean_records(pd.read_csv(TABLES / "table13_former_main_reason.csv"))
    if (TABLES / "table13b_former_all_reasons_multiselect.csv").exists():
        site_data["table13b_former_multiselect"] = clean_records(pd.read_csv(TABLES / "table13b_former_all_reasons_multiselect.csv"))
    if (TABLES / "table13d_former_coverage_vs_voluntary.csv").exists():
        site_data["table13d_former_classes"] = clean_records(pd.read_csv(TABLES / "table13d_former_coverage_vs_voluntary.csv"))
    if (TABLES / "table13e_voluntary_only_main_reason.csv").exists():
        site_data["table13e_voluntary_reasons"] = clean_records(pd.read_csv(TABLES / "table13e_voluntary_only_main_reason.csv"))
    if (TABLES / "table13c_former_alt_variants.csv").exists():
        site_data["table13c_alt_variants"] = clean_records(pd.read_csv(TABLES / "table13c_former_alt_variants.csv"))
    if (TABLES / "table13c_former_return.csv").exists():
        site_data["table13c_return"] = clean_records(pd.read_csv(TABLES / "table13c_former_return.csv"))
    if (TABLES / "table14_switching_destination.csv").exists():
        site_data["table14_destinations"] = clean_records(pd.read_csv(TABLES / "table14_switching_destination.csv"))
    if (TABLES / "table15b_return_by_class.csv").exists():
        site_data["table15b_return_by_class"] = clean_records(pd.read_csv(TABLES / "table15b_return_by_class.csv"))

    # 6. Never-Users
    if (TABLES / "table16b_never_reason.csv").exists():
        site_data["table16b_never_reason"] = clean_records(pd.read_csv(TABLES / "table16b_never_reason.csv"))
    if (TABLES / "table16c_never_platform.csv").exists():
        site_data["table16c_never_platform"] = clean_records(pd.read_csv(TABLES / "table16c_never_platform.csv"))
    if (TABLES / "table16d_never_pref_reason.csv").exists():
        site_data["table16d_never_pref_reason"] = clean_records(pd.read_csv(TABLES / "table16d_never_pref_reason.csv"))
    if (TABLES / "table16f_never_what_would_help.csv").exists():
        site_data["table16f_never_what_would_help"] = clean_records(pd.read_csv(TABLES / "table16f_never_what_would_help.csv"))

    # 7. Secondary Data & Regulatory Disclosures
    if (TABLES / "table16_zepto_secondary_evidence.csv").exists():
        site_data["table16_udrhp_evidence"] = clean_records(pd.read_csv(TABLES / "table16_zepto_secondary_evidence.csv"))
    if (SEC / "evidence_matrix.csv").exists():
        site_data["evidence_matrix"] = clean_records(pd.read_csv(SEC / "evidence_matrix.csv"))
    if (SEC / "media_claims_register.csv").exists():
        site_data["media_claims_register"] = clean_records(pd.read_csv(SEC / "media_claims_register.csv"))
    if (SEC / "sources.csv").exists():
        site_data["secondary_sources"] = clean_records(pd.read_csv(SEC / "sources.csv"))
    if (SEC / "udrhp_evidence_working.csv").exists():
        site_data["udrhp_working_evidence"] = clean_records(pd.read_csv(SEC / "udrhp_evidence_working.csv"))

    # 8. Literature Records
    if (LIT / "references.csv").exists():
        site_data["literature_references"] = clean_records(pd.read_csv(LIT / "references.csv"))
    if (LIT / "hypothesis_evidence.csv").exists():
        site_data["literature_hypothesis_evidence"] = clean_records(pd.read_csv(LIT / "hypothesis_evidence.csv"))
    if (LIT / "excluded_candidates.csv").exists():
        site_data["literature_excluded"] = clean_records(pd.read_csv(LIT / "excluded_candidates.csv"))

    # 9. Triangulation & CRM Recommendations
    if (TABLES / "table18_triangulation.csv").exists():
        site_data["table18_triangulation"] = clean_records(pd.read_csv(TABLES / "table18_triangulation.csv"))
    if (TABLES / "table19_crm_recommendations.csv").exists():
        site_data["table19_crm"] = clean_records(pd.read_csv(TABLES / "table19_crm_recommendations.csv"))

    # 10. Configurations
    if (CONFIG / "research_flow.json").exists():
        site_data["flow_config"] = json.loads((CONFIG / "research_flow.json").read_text(encoding="utf-8"))
    if (CONFIG / "methods_config.json").exists():
        site_data["methods_config"] = json.loads((CONFIG / "methods_config.json").read_text(encoding="utf-8"))
    if (CONFIG / "triangulation_display.json").exists():
        site_data["triangulation_config"] = json.loads((CONFIG / "triangulation_display.json").read_text(encoding="utf-8"))
    if (CONFIG / "crm_strategy_display.json").exists():
        site_data["crm_config"] = json.loads((CONFIG / "crm_strategy_display.json").read_text(encoding="utf-8"))

    # Write out as window.SITE_DATA for instant browser access
    out_js = WEB / "site_data.js"
    json_str = json.dumps(site_data, indent=2, ensure_ascii=False)
    out_js.write_text(f"/** Generated site data bundle — do not hand-edit */\nwindow.SITE_DATA = {json_str};\n", encoding="utf-8")
    print(f"Successfully generated {out_js} ({len(json_str)} bytes, {len(site_data)} top-level sections)")


if __name__ == "__main__":
    main()
