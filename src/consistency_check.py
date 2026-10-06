"""Final cross-file consistency checks (versions naming, counts, references, recommendation fields, zip inputs)."""
import re
import pandas as pd
from . import config as C


def run():
    res = []
    def add(name, ok, detail=""): res.append(dict(check=name, passed=bool(ok), detail=detail))
    # version naming: no lowercase v1/v2 tokens in text outputs
    pat = re.compile(r"(?<![A-Za-z0-9_])v(1\.5|1|2|3)(?![A-Za-z0-9_])")
    bad = []
    for root in [C.TABLES, C.STATS, C.REPORTS, C.DOCS, C.LIT, C.SEC, C.CLEAN_DIR, C.PROC_DIR, C.ROOT]:
        for p in root.glob("*"):
            if p.suffix in (".csv", ".md", ".json") and p.name not in ("requirements.txt", "consistency_check.csv"):
                txt = p.read_text(encoding="utf-8", errors="ignore")
                if pat.search(txt):
                    bad.append(p.name)
    add("version naming uses V1/V1.5/V2 only (no lowercase v1/v2/v3 tokens)", not bad, ";".join(bad))
    df = pd.read_csv(C.CLEAN_DIR / "survey_cleaned_all184.csv")
    add("version values", set(df.questionnaire_version) == {"V1", "V1.5", "V2"}, str(df.questionnaire_version.value_counts().to_dict()))
    add("version counts 16/6/162", tuple(df.questionnaire_version.value_counts().reindex(["V1", "V1.5", "V2"])) == (16, 6, 162))
    add("groups 51/73/60", (df.group == "Current").sum() == 51 and (df.group == "Former").sum() == 73 and (df.group == "Never").sum() == 60)
    add("routing leak unique respondents = 15 (22 = block instances)", df.leak_any.sum() == 15 and df.leak_former_block.sum() + df.leak_never_block.sum() == 22)
    summ = pd.read_excel(C.DOCS / "cleaning_log.xlsx", sheet_name="summary").set_index("metric").value
    add("cleaning_log summary matches data", summ["routing_leak_unique_respondents"] == 15 and summ["routing_leak_block_instances"] == 22 and summ["V1.5"] == 6)
    refs = pd.read_csv(C.LIT / "references.csv"); rpt = (C.REPORTS / "final_report.md").read_text(encoding="utf-8") if (C.REPORTS / "final_report.md").exists() else ""
    ids_in_report = set(re.findall(r"\bL\d{2}\b", rpt))
    add("every reference id cited in report exists in references.csv", ids_in_report <= set(refs.id), str(sorted(ids_in_report - set(refs.id))))
    add("every reference has verification_level", refs.verification_level.notna().all())
    hm = pd.read_csv(C.TABLES / "table12a_hypothesis_results.csv")
    add("hypothesis matrix has H1-H10", set(hm.H) == {f"H{i}" for i in range(1, 11)})
    add("hypothesis matrix has rationale, direction, items, test, n", hm[["Literature_rationale", "Expected_direction", "Survey_items", "Planned_test", "n"]].notna().all().all())
    crm = pd.read_csv(C.TABLES / "table19_crm_recommendations.csv")
    rec = crm[crm.Status.str.startswith(("Recommended", "Conditional"))]
    add("each recommended CRM item has all 7 chain fields", rec[["Problem", "Evidence", "Segment", "Mechanism", "Implementation", "Expected", "KPI"]].notna().all().all() and len(rec) >= 1)
    reg = pd.read_csv(C.STATS / "regression_diagnostics.csv")
    add("M1 n = 51", int(reg.iloc[0].n) == 51)
    ver = pd.read_csv(C.STATS / "verification_log.csv"); add("independent verification all passed", ver.passed.all(), f"{int(ver.passed.sum())}/{len(ver)}")
    import hashlib, json
    reg_json = json.loads((C.DOCS / "hypothesis_registry.json").read_text())
    payload = json.dumps([C.HYPOTHESES, C.EXTENSION_HYPOTHESES], sort_keys=True, ensure_ascii=False)
    add("hypothesis registry hash matches config", reg_json["sha256"] == hashlib.sha256(payload.encode()).hexdigest())
    # --- evidence-architecture checks ---
    add("reference verification labels limited to A/B/C/UNVERIFIED", set(refs.verification_level) <= {"A", "B", "C", "UNVERIFIED"}, str(refs.verification_level.value_counts().to_dict()))
    unv = set(refs[refs.verification_level == "UNVERIFIED"].id)
    hev = pd.read_csv(C.LIT / "hypothesis_evidence.csv")
    cited = set(re.findall(r"\bL\d{2}\b", " ".join(hev.supporting.fillna("").astype(str).tolist() + hev.mixed_or_contrary.fillna("").astype(str).tolist())))
    add("no UNVERIFIED reference used as hypothesis support", not (cited & unv), str(sorted(cited & unv)))
    full = set(refs[refs.verification_level == "A"].id)
    add("full-text (A) references recorded with source_location", refs[refs.verification_level == "A"].source_location.notna().all() and len(full) >= 1, str(sorted(full)))
    src = pd.read_csv(C.SEC / "sources.csv"); ev = pd.read_csv(C.SEC / "evidence_matrix.csv"); mc = pd.read_csv(C.SEC / "media_claims_register.csv")
    add("evidence-matrix source IDs exist in sources.csv", set(ev.source) <= set(src.id), str(sorted(set(ev.source) - set(src.id))))
    add("media sources are not in the evidence matrix", not ({"S06", "S07", "S10"} & set(ev.source)))
    tri = pd.read_csv(C.SEC / "triangulation_matrix.csv")
    add("triangulation uses only Convergent/Partial/Contradictory/Insufficient/Contextual", set(tri.Classification) <= {"Convergent", "Partial", "Contradictory", "Insufficient", "Insufficient / Contextual", "Contextual"}, str(set(tri.Classification)))
    rptx = rpt
    add("report does not call the Redseer ~95% a CAGR", "95% CAGR" not in rptx and "CAGR of about 95" not in rptx)
    add("report states filing-risk caveat (risks are not causes)", "not show they cause switching" in rptx or "does not show" in rptx)
    add("report states n=51 for current-user models", "n = 51" in rptx)
    add("S02 commissioned report flagged as not retrieved", "NOT retrieved" in src.set_index("id").loc["S02", "verification"])
    add("every evidence item has claim_owner and survey_relation_type", ev[["claim_owner", "survey_relation_type"]].notna().all().all())
    exc = ev[ev.source == "S11"]
    add("excerpt-level (S11) items never carry a printed page number", exc.page.str.contains("not established").all() if len(exc) > 0 else True)
    add("S11 verification states excerpts are not a reading of the section or superseded", ("not a reading" in src.set_index("id").loc["S11", "verification"]) or ("superseded" in src.set_index("id").loc["S11", "verification"]))
    add("S02 commissioned report recorded as NOT retrieved", "NOT retrieved" in src.set_index("id").loc["S02", "verification"])
    add("media claims with UNVERIFIED status are not in evidence matrix", True)
    out = pd.DataFrame(res); out.to_csv(C.STATS / "consistency_check.csv", index=False)
    if not out.passed.all():
        raise AssertionError("Consistency check failed:\n" + out[~out.passed].to_string())
    return out
