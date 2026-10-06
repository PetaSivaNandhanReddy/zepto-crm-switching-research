# Checkpoint 3: Controlled Pipeline Execution Audit Report

**Date:** 2026-10-04  
**Status:** Completed & Fully Audited  
**Environment:** Python 3.11.9 (`.venv\Scripts\python.exe`)  
**Scope:** Pre-execution verification, full consistency check audit, main pipeline execution (`run_analysis.py`), post-execution statistical audit, and verification of frozen scope.

---

## 1. Pre-Execution Verification Summary

Prior to executing the pipeline, all research assets were audited and verified:
- **Primary Survey Datasets:** `data/raw/Quick-Commerce_Survey.csv` (184 raw responses) and `data/processed/` datasets remain 100% untouched and frozen.
- **Primary Analysis Code:** `src/primary_analysis.py`, `src/cleaning.py`, and `src/survey_utils.py` remain 100% untouched.
- **Final Report:** Root `final_report.md` has **NOT** been modified.
- **Master PDF:** `Zepto Limited - UDRHP-I-1780938548.pdf` (690 pages) is unchanged and preserved as the master source.
- **Secondary Evidence Dataset:** Contains strictly **25 UDRHP records (`E01`–`E25`)** and 4 independent Redseer records. Zero references to `E26` or `E27` exist in the project.

---

## 2. Automated Consistency Check Results (All 29 Rules)

Command executed:
```powershell
.\.venv\Scripts\python.exe -m src.consistency_check
```

### Complete Rule-by-Rule Consistency Results:

| Check # | Consistency Check Rule Description | Status | Verification Detail / Metric Value |
| :---: | :--- | :---: | :--- |
| **01** | Version naming uses V1/V1.5/V2 only (no lowercase v1/v2/v3 tokens) | **PASS** | No invalid tokens in any output text/table files |
| **02** | Questionnaire version values set | **PASS** | `{'V2': 162, 'V1': 16, 'V1.5': 6}` |
| **03** | Questionnaire version counts match 16 / 6 / 162 | **PASS** | Exact match: 16 (V1), 6 (V1.5), 162 (V2) |
| **04** | User group partition matches 51 / 73 / 60 | **PASS** | Current $n=51$, Former $n=73$, Never $n=60$ ($N=184$) |
| **05** | Routing leak isolation (15 unique respondents = 22 block instances) | **PASS** | `leak_any == 15`, `leak_former + leak_never == 22` |
| **06** | Cleaning log summary matches processed data | **PASS** | Log summary reconciles across all parameters |
| **07** | Every reference ID cited in report exists in `references.csv` | **PASS** | `[]` (zero unmapped references) |
| **08** | Every reference has an explicit `verification_level` | **PASS** | 100% populated |
| **09** | Hypothesis matrix contains all hypotheses $H1$–$H10$ | **PASS** | Complete set $\{H1, H2, \dots, H10\}$ |
| **10** | Hypothesis matrix contains rationale, direction, items, test, $n$ | **PASS** | All fields non-null across all rows |
| **11** | Each recommended CRM item has all 7 chain fields | **PASS** | Problem, Evidence, Segment, Mechanism, Implementation, Expected, KPI populated |
| **12** | Model M1 sample size $n = 51$ | **PASS** | Exact match: $n = 51$ |
| **13** | Independent mathematical verification passed | **PASS** | **53 / 53** independent calculations verified |
| **14** | Hypothesis registry hash matches config | **PASS** | SHA256 checksum validated |
| **15** | Reference verification labels limited to A/B/C/UNVERIFIED | **PASS** | `{'A': 2, 'B': 8, 'C': 5, 'UNVERIFIED': 2}` |
| **16** | No UNVERIFIED reference used as hypothesis support | **PASS** | `[]` (L07, L09 strictly isolated) |
| **17** | Full-text (`A`) references recorded with exact `source_location` | **PASS** | `['L05', 'L10']` |
| **18** | Evidence matrix source IDs exist in `sources.csv` | **PASS** | All sources mapped |
| **19** | Media sources are not in the evidence matrix | **PASS** | `{'S06', 'S07', 'S10'}` strictly segregated |
| **20** | Triangulation uses only disciplined classification categories | **PASS** | `{'Partial', 'Contradictory', 'Insufficient', 'Insufficient / Contextual'}` |
| **21** | Report does not call the Redseer ~95% a CAGR | **PASS** | Validated |
| **22** | Report states filing risk caveat (disclosed risks are not causes) | **PASS** | Validated |
| **23** | Report states $n=51$ for current-user models | **PASS** | Validated |
| **24** | S02 commissioned report flagged as not retrieved independently | **PASS** | Validated |
| **25** | Every evidence item has `claim_owner` and `survey_relation_type` | **PASS** | 100% populated |
| **26** | Excerpt-level (S11) items never carry a printed page number | **PASS** | Validated |
| **27** | S11 verification states excerpts are superseded or not a full reading | **PASS** | Validated |
| **28** | S02 commissioned report recorded as NOT retrieved | **PASS** | Validated |
| **29** | Media claims with UNVERIFIED status are not in evidence matrix | **PASS** | Validated |

---

## 3. Main Pipeline Execution Status

Command executed:
```powershell
.\.venv\Scripts\python.exe run_analysis.py
```
- **Exit Code:** `0` (Success)
- **Output:** `Pipeline completed. n: 184 current 51 former 73 never 60`

---

## 4. Post-Execution Primary Statistics Verification

A strict check was performed confirming 100% numerical fidelity between frozen primary research results and regenerated outputs:

### A. Core Hypotheses ($H1$–$H7$) on Current Users ($n=51$)

| Hypothesis | Construct | Expected Sign | Spearman $\rho$ | 95% Bootstrap CI | Holm $p$-value | Decision Result | Discrepancy |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| **H1** | SAT | $-$ | $+0.165$ | $[-0.12, 0.44]$ | $0.2492$ | Not supported / insufficient evidence | **None** |
| **H2** | ALT | $+$ | $+0.685$ | $[0.51, 0.81]$ | $1.16 \times 10^{-7}$ | Supported (raw) | **None** |
| **H3** | VAR | $+$ | $+0.694$ | $[0.52, 0.82]$ | $8.36 \times 10^{-8}$ | Supported (raw) | **None** |
| **H4** | PROMO | $+$ | $+0.700$ | $[0.53, 0.83]$ | $6.67 \times 10^{-8}$ | Supported (raw) | **None** |
| **H5** | SWEFFORT | $-$ | **$+0.721$** | $[0.56, 0.84]$ | $1.74 \times 10^{-8}$ | **Not supported (anomalous, opposite direction)** | **None** |
| **H6** | FAM | $-$ | $+0.248$ | $[-0.03, 0.50]$ | $0.2492$ | Not supported / insufficient evidence | **None** |
| **H7** | INERT | $-$ | $+0.248$ | $[-0.05, 0.50]$ | $0.2492$ | Not supported / insufficient evidence | **None** |

### B. Extension Hypotheses ($H8$–$H10$)

| Hypothesis | Test Description | Sample Sizes | Test Statistic | $p$-value | Decision Result | Discrepancy |
| :--- | :--- | :--- | :---: | :---: | :--- | :---: |
| **H8** | M1 PPM Joint Regression | $n=51$ | $R^2 = 0.696$ | $F=26.27, p < .001$ | Exploratory (item overlap) | **None** |
| **H9** | Mann-Whitney U: Partial Shift | $n_1=29, n_2=22$ | $U=346.5$ | $p = 0.6014$ | Not supported / inconclusive | **None** |
| **H10** | Mann-Whitney U: Return Intent | $n_1=28, n_2=30$ | $U=496.0$ | $p = 0.2137$ | Not supported / inconclusive | **None** |

### C. Within-Person Centering Sensitivity Analysis (`table21`)

| Construct | Raw Spearman $\rho$ | Within-Person Centered $\rho$ | Centered 95% Bootstrap CI | Interpretation | Discrepancy |
| :--- | :---: | :---: | :---: | :--- | :---: |
| **ALT** | $+0.69$ | **$-0.03$** | $[-0.31, +0.25]$ | Raw association disappears after centering | **None** |
| **VAR** | $+0.69$ | **$+0.10$** | $[-0.18, +0.37]$ | Raw association attenuated; CI spans zero | **None** |
| **PROMO** | $+0.70$ | **$+0.23$** | $[-0.05, +0.48]$ | Raw association attenuated; CI spans zero | **None** |
| **SWEFFORT** | $+0.72$ | **$+0.05$** | $[-0.23, +0.32]$ | Anomalous raw association collapses to zero | **None** |

### D. Sample Segregation & Exclusions

- **Total Sample:** $N = 184$
- **Current Users:** $n = 51$
- **Former Users:** $n = 73$ (Class A Coverage-Primary $n=31$, Class B Partial Coverage $n=10$, Class C Voluntary-Only $n=32$)
- **Never-Users:** $n = 60$ (**strictly excluded** from switching-intention and switching-behaviour models; 37/60 cite unserved locality as main reason)
- **Routing Leaks:** 15 unique respondents (22 block instances) segregated into supplementary tables.

---

## 5. Secondary Evidence, Media Claims, & Triangulation Post-Run Audit

1. **Secondary Evidence Matrix (`secondary_data/evidence_matrix.csv`):**
   - Strictly **25 UDRHP records (`E01`–`E25`)** and 4 independent Redseer records (`S03` x2, `S04`, `S05`).
   - `E15` and `E16` are Company-Cited Industry Evidence (Redseer Report quoted in UDRHP).
   - Zero references to `E26` or `E27`.
   - All original printed page numbers preserved.

2. **Media Claims Register (`secondary_data/media_claims_register.csv`):**
   - `M01` = `NOT VERIFIED AS WORDED / CONTEXTUALIZED`
   - `M02` = `VERIFIED - PRIMARY UDRHP KPI`
   - `M03` = `VERIFIED - PRIMARY UDRHP COHORT EVIDENCE`
   - `M04` = `DISPROVED/CONTRADICTED`
   - `M05`, `M06`, `M08`, `M09`, `M10`, `M11` = `VERIFIED`

3. **Triangulation Matrix (`secondary_data/triangulation_matrix.csv`):**
   - Factor 1 (Coverage): `Partial` (Convergent Context, non-causal)
   - Factor 2 (Competitor pull / assortment): `Partial`
   - Factor 3 (Competitor promotions / price): `Partial`
   - Factor 4 (Switching effort): `Contradictory` (anomalous survey correlation vs multi-homing context)
   - Factor 5 (Satisfaction): **`Insufficient / Contextual`** (*"Satisfaction: Insufficient / Contextual — survey relationship was non-significant; UDRHP describes service-speed positioning but does not directly test satisfaction-driven switching."*)
   - Factor 6 (Familiarity / inertia): `Insufficient`

4. **CRM Recommendations Matrix (`secondary_data/crm_recommendation_matrix.csv`):**
   - `R1`: Recommended (conditional, testable) — pin-code demand capture / waitlist
   - `R2`: Conditional (pilot with control group) — stock-out alerts & substitute ranking via existing ML
   - `R3`: Conditional (small $n=16$) — reason-matched voluntary win-back
   - `R4`: **Not recommended on current evidence — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure switching barriers with a validated scale before designing lock-in interventions.**
   - `R5`: Monitor only — operational safeguard

---

## 6. Freeze & Scope Confirmation

- **Root `final_report.md`:** **100% UNTOUCHED and unmodified** (reserved for Checkpoint 4).
- **Primary Survey Datasets:** **100% UNTOUCHED**.
- **Primary Code:** **100% UNTOUCHED**.
- **Discrepancies:** **Zero discrepancies** detected.

---

**Checkpoint 3 is complete and verified. STOPPING here and awaiting review before Checkpoint 4.**
