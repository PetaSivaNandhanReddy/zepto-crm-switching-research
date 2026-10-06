# Checkpoint 2: Secondary Architecture Harmonization Report (QC Revisions Applied)

**Status:** Completed & QC-Approved  
**Date:** 2026-10-04  
**Scope:** Integration of verified UDRHP-I organizational evidence (`E01`–`E25`), media claim register updates (`M01`–`M11`), disciplined factor triangulation, testable CRM recommendation refinement (`R1`–`R5`), and strict preservation of frozen primary survey data and analyses.

---

## 1. QC Audit Corrections Implemented

In response to the Checkpoint 2 QC review, the following mandatory corrections were executed:

1. **Evidence ID Alignment & Removal of Spurious `E26`/`E27` References:**
   - The UDRHP-I primary filing evidence dataset contains strictly **25 records (`E01`–`E25`)**.
   - Company-cited Redseer industry material quoted within UDRHP-I Section IV (Industry Overview, pp. 194–205) is correctly identified as **`E15`** (Market scale) and **`E16`** (Category diversification).
   - All references to `E26` and `E27` were removed from all documentation, code, and secondary data files.
   - `PRIMARY_ITEMS` in `src/secondary_analysis.py` maps 1-to-1 to `E01`–`E25`.

2. **R4 Switching-Cost Language Refinement:**
   - Unsupported assertions that *"structural switching costs in quick commerce are negligible"* have been completely removed.
   - Replaced with disciplined, evidence-based language:
     > *"Not recommended on current evidence — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure switching barriers with a validated scale before designing lock-in interventions."*
   - Strict distinctions are maintained between:
     - `M01` not verified as worded
     - Supply-side partner multi-homing risk disclosures (Risk Factors 10 & 13)
     - Anomalous `H5` survey result ($\rho = +0.72$)
     - Actual consumer switching costs (which remain unproven/inconclusive rather than proven negligible)

3. **Satisfaction Factor Triangulation Re-Classification:**
   - Reclassified from *"Partial (Convergent Null)"* to:
     > **`Satisfaction: Insufficient / Contextual`** — *"Survey relationship was non-significant; UDRHP describes service-speed positioning but does not directly test satisfaction-driven switching."*
   - The operational <10–15 minute dark-store delivery SLA disclosure is not used as evidence explaining the survey null.

4. **Strict Evidence Taxonomy Audit:**
   - All 25 evidence records (`E01`–`E25`) preserve exact section classifications and factual integrity:
     - *Risk Factors (pp. 23–63):* **Company risk disclosure** (`E01`–`E06`)
     - *Objects of the Offer (pp. 143–157):* **Offer/object disclosure** (`E07`–`E10`)
     - *Basis for Offer Price / KPIs (pp. 158–181):* **Company KPI** (`E11`–`E14`)
     - *Industry Overview (pp. 189–231):* **Company-Cited Industry Evidence** (`E15`–`E16`)
     - *Our Business (pp. 232–276):* **Company Business Disclosure** (`E17`–`E19`, `E21`–`E22`) & **Company KPI** (`E20`)
     - *MD&A (pp. 529–575):* **Company/MD&A Disclosure** (`E23`–`E25`)
     - *CRM Interpretations:* Explicitly designated with `(CRM interpretation/inference)`.

5. **Execution & File Audit:**
   - Only `secondary_analysis.run()` and `synthesis.build_matrices()` were executed to generate secondary tables.
   - **`run_analysis.py` was NOT executed.**

---

## 2. Files Modified & Generated

### A. Source Code Modified
- [`src/secondary_analysis.py`](file:///c:/Users/user/Downloads/crm_project_ZEPTO/src/secondary_analysis.py): `PRIMARY_ITEMS` aligned 1-to-1 with `E01`–`E25`; `INDUSTRY_ITEMS` mapped to independent external articles (`S03`, `S04`, `S05`); taxonomy standardized.
- [`src/synthesis.py`](file:///c:/Users/user/Downloads/crm_project_ZEPTO/src/synthesis.py): Factor 4 (Switching effort), Factor 5 (Satisfaction `Insufficient / Contextual`), and `R4` recommendation status/limitations updated.

### B. Secondary Data & Output Files Generated / Overwritten
- **By `secondary_analysis.run()`:**
  - `secondary_data/evidence_matrix.csv` (25 UDRHP `E01`–`E25` + 4 external Redseer = 29 records)
  - `secondary_data/media_claims_register.csv` (11 claims `M01`–`M11`)
  - `secondary_data/sources.csv` (7 tracked sources)
  - `secondary_data/media_sources_not_evidence.csv` (3 media items)
  - `secondary_data/statistics_register.csv` (12 verified statistics)
  - `literature/references.csv`, `literature/excluded_candidates.csv`, `literature/hypothesis_evidence.csv`
  - `outputs/tables/table16_zepto_secondary_evidence.csv` (25 UDRHP items)
  - `outputs/tables/table17_industry_secondary_evidence.csv` (4 external items)
- **By `synthesis.build_matrices()`:**
  - `secondary_data/triangulation_matrix.csv` & `outputs/tables/table18_triangulation.csv` (6 factors)
  - `secondary_data/crm_recommendation_matrix.csv` & `outputs/tables/table19_crm_recommendations.csv` (5 recommendations `R1`–`R5`)
  - `secondary_data/factor_evidence_matrix.csv`
  - `outputs/stats/analysis_n_register.csv`
  - `outputs/tables/table12a_hypothesis_results.csv`, `table12_regression_results.csv`, `table12c_regression_diagnostics.csv`, `table07_literature_hypothesis_evidence.csv`
  - `documentation/hypothesis_matrix.xlsx`

---

## 3. Authoritative Evidence Taxonomy (`E01`–`E25`)

| ID | Printed Page | Section | Evidence Classification | Factual Claim Summary |
| :--- | :--- | :--- | :--- | :--- |
| **E01** | p. 24 | Section II: Risk Factors | Company risk disclosure | Rapid scaling resulted in net losses; revenue grew to Rs 226,235.84M while restated loss was Rs 59,051.92M (FY26). |
| **E02** | pp. 27–28 | Section II: Risk Factors | Company risk disclosure | Delivery partner retention challenges; 221,667 active partners; delivery expense at 12.28% of NRV. |
| **E03** | p. 30 | Section II: Risk Factors | Company risk disclosure | Merchant partners multi-home across competing platforms and may reduce inventory on Zepto. |
| **E04** | p. 31 | Section II: Risk Factors | Company risk disclosure | Competitor discounts, promotions, user incentives, and alternative pricing models disclosed as strategic threats. |
| **E05** | p. 34 | Section II: Risk Factors | Company risk disclosure | Increases in user-facing operating or logistics fees may decrease transaction frequency. |
| **E06** | p. 44 | Section II: Risk Factors | Company risk disclosure | Dark store network must be expanded cost-effectively; failure to deploy capital impairs growth. |
| **E07** | pp. 143–145 | Section III: Objects of Offer | Offer/object disclosure | Gross proceeds earmarked include Rs 16,289.75M for new dark stores over FY27–FY29. |
| **E08** | pp. 148–150 | Section III: Objects of Offer | Offer/object disclosure | Net proceeds allocated include Rs 17,349.41M for dark store lease rentals through FY30. |
| **E09** | pp. 154–156 | Section III: Objects of Offer | Offer/object disclosure | Net proceeds allocated include Rs 4,000.00M for cloud/tech infrastructure supporting search & recommendations. |
| **E10** | pp. 156–157 | Section III: Objects of Offer | Offer/object disclosure | Net proceeds allocated include Rs 5,200.00M for marketing and business promotion. |
| **E11** | p. 160 | Section III: Basis for Offer Price | Company KPI | Annual Transacting Users (ATU) grew from 10.57M (FY24) to 38.38M (FY25) to 47.97M (FY26). |
| **E12** | p. 161 | Section III: Basis for Offer Price | Company KPI | Orders per day rose +28.6% QoQ to 2,333,488 in Q4 FY26 while trailing ATU dipped 3.2% from 49.54M to 47.97M. |
| **E13** | p. 162 | Section III: Basis for Offer Price | Company KPI | Store-level unique SKUs grew from 12,312 (FY24) to 44,341 (FY25) to 46,623 (FY26) (M02 verified). |
| **E14** | p. 163 | Section III: Basis for Offer Price | Company KPI | Dark store network expanded from 337 (FY24) to 1,029 (FY25) to 1,139 across 66 cities (FY26). |
| **E15** | pp. 194–196 | Section IV: Industry Overview | Company-Cited Industry Evidence | Indian quick commerce grew from ~Rs 133B (CY22) to ~Rs 963B (CY25); accounts for >2/3 of online grocery. |
| **E16** | pp. 202–205 | Section IV: Industry Overview | Company-Cited Industry Evidence | Consumer adoption expanding beyond grocery into beauty, electronics, and general merchandise. |
| **E17** | pp. 234–235 | Section IV: Our Business | Company Business Disclosure | Platform operates on S.Q.A.P. framework (Speed, Quality, Assortment, Price) supported by EDLP philosophy. |
| **E18** | pp. 246–247 | Section IV: Our Business | Company Business Disclosure | In-house ML search and recommendation engine for intent parsing and catalog ranking. |
| **E19** | p. 252 | Section IV: Our Business | Company Business Disclosure | Cohort category expansion: ~6 categories in Month 1 to >12 in Year 1 and 18 categories in Year 2 (M10 verified). |
| **E20** | pp. 253–254 | Section IV: Our Business | Company KPI | Cohort retention matrix shows active ordering stabilizes between 44.3% and 54.0% across multi-year cohorts (M03 verified). |
| **E21** | pp. 258–259 | Section IV: Our Business | Company Business Disclosure | Zepto Pass is the official subscription membership program; "Zepto Club" is not established. |
| **E22** | pp. 260–261 | Section IV: Our Business | Company Business Disclosure | Dark store densification reduces average delivery radius, targeting under 10–15 min fulfillment. |
| **E23** | pp. 530–532 | Section V: MD&A | Company/MD&A Disclosure | Supply Chain Variable Cost per Order defines variable fulfillment and delivery costs per order. |
| **E24** | p. 538 | Section V: MD&A | Company/MD&A Disclosure | Management explicitly links assortment growth (reaching 49,602 SKUs in Q4 FY26) + EDLP pricing to retention. |
| **E25** | pp. 545–547 | Section V: MD&A | Company/MD&A Disclosure | Advertising and promotion expenses tracked across city rollouts to drive customer acquisition. |

---

## 4. Media Claims Final Status (`M01`–`M11`)

- **`M01`:** **`NOT VERIFIED AS WORDED / CONTEXTUALIZED`** (Risk disclosures on pp. 30–32 establish competitor pricing threats, but literal phrase *"low switching costs"* is absent).
- **`M02`:** **`VERIFIED — PRIMARY UDRHP KPI`** (SKUs: 12,312 $\rightarrow$ 44,341 $\rightarrow$ 46,623 $\rightarrow$ 49,602, p. 162, p. 538).
- **`M03`:** **`VERIFIED — PRIMARY UDRHP COHORT EVIDENCE`** (Exact observations: FY23 Q2 was 45.2% in Q12 and 44.3% in Q15; FY24 Q1 was 49.8% in Q9, pp. 253–254; descriptive range 44.3%–54.0%).
- **`M04`:** **`DISPROVED/CONTRADICTED`** (Official program is "Zepto Pass", pp. 13, 258; "Zepto Club" is absent).
- **`M05`:** **`VERIFIED — PRIMARY UDRHP KPI`** (Stores: 337 $\rightarrow$ 1,029 $\rightarrow$ 1,139 across 66 cities, p. 163).
- **`M06`:** **`VERIFIED — PRIMARY UDRHP KPI`** (ATU: 10.57M $\rightarrow$ 38.38M $\rightarrow$ 47.97M, p. 160).
- **`M07`:** **`VERIFIED — COMPANY-CITED REDSEER INDUSTRY EVIDENCE`** (Order volume CAGR ~119.5%, p. 3).
- **`M08`:** **`VERIFIED — PRIMARY UDRHP OFFER/OBJECT DISCLOSURE`** (₹16,289.75M expansion; ₹17,349.41M lease rentals, pp. 143, 148).
- **`M09`:** **`VERIFIED — PRIMARY UDRHP KPI`** (ATU dip 49.54M $\rightarrow$ 47.97M alongside +28.6% orders/day QoQ growth, p. 161).
- **`M10`:** **`VERIFIED — PRIMARY UDRHP BUSINESS DISCLOSURE`** (Category expansion: 6 $\rightarrow$ 12 $\rightarrow$ 18 categories in 2 years, p. 252).
- **`M11`:** **`VERIFIED — COMPANY RISK DISCLOSURE`** (Delivery partner multi-homing across platforms, pp. 27–28, 56).

---

## 5. Triangulation Matrix Final Classifications

1. **Service Coverage (`Partial` / Convergent Context):** Non-causal alignment between survey reported barrier (42.5% former exits) and ₹16,289.75M expansion capital.
2. **Competitor Pull & Assortment (`Partial`):** Raw survey correlations compatible with literature and SKU depth (12,312 $\rightarrow$ 49,602), but constructs are not empirically distinct and fragile to centering.
3. **Competitor Promotions / Price (`Partial`):** Single-item correlation fragile and not matched by exit frequencies; UDRHP discloses pricing as strategic risk without causal evidence.
4. **Switching Effort (`Contradictory`):** Anomalous survey positive correlation ($\rho=+0.72$) contradicts theoretical expectations. UDRHP discloses supply-side multi-homing. Switching costs remain inconclusive rather than proven negligible.
5. **Satisfaction Push (`Insufficient / Contextual`):** Survey relationship was non-significant ($\rho=0.17, p=0.25$); UDRHP describes service-speed positioning but does not directly test satisfaction-driven switching.
6. **Familiarity / Inertia (`Insufficient`):** Survey estimates imprecise; UDRHP category depth provides no causal lock-in evidence.

---

## 6. CRM Recommendations Matrix (`R1`–`R5`)

- **`R1` (Coverage / Non-Adoption):** **Recommended (conditional, testable)** — Pin-code capture on failed-serviceability screens; automated notification upon dark-store rollout.
- **`R2` (Assortment & Stock-Outs):** **Conditional (pilot with control group)** — Restock alerts and algorithmic substitution recommendations using existing ML capabilities (`E18`).
- **`R3` (Voluntary Win-Back):** **Conditional (small $n=16$; matched reasons only)** — Reason-matched restock messages; generic discount incentives suppressed.
- **`R4` (Switching Lock-In):** **Not recommended on current evidence — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure switching barriers with a validated scale before designing lock-in interventions.**
- **`R5` (Service Recovery):** **Monitor only (operational safeguard)** — Trigger-based service recovery on SLA breach as a hygienic safeguard.

---

## 7. Verification of Frozen Primary Analysis

- **Primary Datasets Untouched:** Raw survey data (`data/raw/`) and cleaned survey data (`data/processed/`) remain completely unmodified.
- **Sample Sizes Preserved:** $N=184$ (Current $n=51$, Former $n=73$, Never $n=60$).
- **Never-Users Preserved:** Never-users ($n=60$) remain strictly segregated outside switching analyses.
- **Primary Code Untouched:** `src/primary_analysis.py`, `src/cleaning.py`, `src/survey_utils.py` were not modified.
- **Pipeline Execution:** `run_analysis.py` was **NOT executed**.
- **Final Report:** `final_report.md` was **NOT modified** (reserved for Checkpoint 4).
- **Master Files:** Master PDF (`Zepto Limited - UDRHP-I-1780938548.pdf`) and working PDF remain preserved.
