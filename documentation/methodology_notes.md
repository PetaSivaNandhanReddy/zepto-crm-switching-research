# Methodology notes
1. Raw data `data/raw/Quick-Commerce_Survey.csv` is never modified. Groups from Q4 (current, former, never). Never-users are excluded from switching-away analyses.
2. Questionnaire versions: V1 = responses 1-16, V1.5 = 17-22, V2 = 23-184. Items added later are structural missingness (NaN, never zero).
3. Routing leaks: 15 unique respondents (22 block-level incidents), flagged, removed from primary datasets, reported as supplementary.
4. Straight-lining is ambiguous on a mixed-polarity item set; respondents retained; sensitivity analyses with/without.
5. Hypotheses frozen in `src/config.py` and hashed in `documentation/hypothesis_registry.json` at the start of each run; decision rule Holm p < .05 with correct direction; labels Supported / Inconclusive / Anomalous.
6. Regression is exploratory/associational; R2 is inflated by item overlap (see `regression_overlap_diagnostics.csv`).
7. Measurement diagnostics: HTMT, within-person centering, H5 item diagnostics.
8. Independent verification recomputes key results from the raw CSV (`src/verification.py`); consistency checks in `src/consistency_check.py`.
9. Secondary evidence: only retrieved sources recorded; verification levels and coverage limits stated in `secondary_data/sources.csv`.
10. Random seed: 20260929.
11. Source IDs: S01 (UDRHP-I), S09 (Draft Abridged Prospectus), S02 (commissioned Redseer report, not opened), S03-S05 (public Redseer articles, read in full). S06, S07, S10 are media sources kept in `secondary_data/media_sources_not_evidence.csv` / `media_claims_register.csv` (M01-M08). S08 was retired (an earlier generic media-summary entry, superseded by the media-claims register); the gap is intentional.
12. Literature/source lists are curated in `src/secondary_analysis.py` (source of truth); triangulation, hypothesis matrix and CRM logic are in `src/synthesis.py`. Edit those files and re-run `run_analysis.py`; do not edit generated CSVs.
