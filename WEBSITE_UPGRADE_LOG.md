# Website Upgrade Verification Log

**Project:** Zepto CRM Switching Research Webpage Upgrade  
**Safety Tag:** `site-v1-pre-upgrade`  
**Active Branch:** `site-upgrade`  
**Date:** 2026-10-07  
**Status:** Verification Complete — All 18 Discrepancies Resolved against Output Tables and Final Report

---

## 1. Discrepancy Verification Register (D01 – D18)

| ID | Item | Status | Verified Truth (from `outputs/` & `final_report.md`) | Resolution for Upgraded Webpage |
|:---|:---|:---|:---|:---|
| **D01** | Questionnaire Versions & Invariance | **CONFIRMED & RESOLVED** | `table03b_questionnaire_versions.csv`: V1 $n=16$ (8.70%), V1.5 $n=6$ (3.26%), V2 $n=162$ (88.04%). Total $N=184$. Mann–Whitney $U=346.5, p=0.6014$ is the H9 partial shift test (`outputs/statistical_results/hypothesis_test_H9.csv`), not a questionnaire invariance test. | Update version distribution to V1: 16, V1.5: 6, V2: 162. Remove mislabeled "invariance verified" text. Show $U=346.5, p=0.6014$ strictly under H9 extension test. |
| **D02** | Former User Return Intention | **CONFIRMED & RESOLVED** | `table13c_former_return.csv`: Measured on $n=68$ (5 V1 former users structurally missing). Definitely Yes: 14 (20.6%), Probably Yes: 27 (39.7%), Not Sure: 20 (29.4%), Probably no: 5 (7.4%), Definitely No: 2 (2.9%). Total answering = 68. Class breakdown (`table15b_return_by_class.csv`): Class A $n=28$ (median 4.0), Class B $n=10$ (median 4.0), Class C voluntary $n=30$ (median 3.5). H10 test (`hypothesis_test_H10.csv`): Class A vs C $U=496.0, p=0.2137$. Voluntary return willingness: 15/30 (50.0%). | Rebuild return intention display strictly from `table13c` ($n=68$), `table15b`, and H10 output. Label denominator as 68 former users. |
| **D04** | Demographics | **CONFIRMED & RESOLVED** | `table01_respondent_profile.csv`: Age 18–24: 157 (85.3%), 25–34: 23 (12.5%), 35+: 4 (2.2%) ($N=184$). Occupation: Student 118 (64.1%), Employed 52 (28.3%), Self-employed/Other 14 (7.6%) ($N=184$). Location ($n=168$): Metro 134 (79.8%), Non-metro 34 (20.2%). Spend ($n=168$): <₹1,000: 81 (48.2%), ₹1,000–₹3,000: 57 (33.9%), >₹3,000: 30 (17.9%). | Use exact counts and percentages from `table01` with explicit base sizes ($N=184$ and $n=168$ with note on 16 early-version omissions). |
| **D03** | UDRHP Register (E01–E25) | **CONFIRMED & RESOLVED** | `table16_zepto_secondary_evidence.csv` & `secondary_data/udrhp_evidence_working.csv`: E07 ₹16,289.75M dark store capex (pp. 143–145); E08 ₹17,349.41M lease liabilities; E09 ₹4,000.00M cloud & tech (pp. 154–156); E10 ₹5,200.00M marketing (pp. 156–157); E11 4.88M ATU (p. 240); E12 5.86M ATU (p. 240); E13 13,000+ SKUs (p. 239); E14 935 dark stores (p. 238); E20 mature cohort retention 44.3%–54.0% (pp. 253–254). | Rebuild every UDRHP evidence card and timeline marker directly from `table16` and `udrhp_evidence_working.csv`. |
| **D05** | Regression Models (M1 & M2) | **CONFIRMED & RESOLVED** | `table12_regression_results.csv` and `table12c_regression_diagnostics.csv`: Pre-specified Model M1 ($k=4$, $n=51$): $R^2=0.696$, Adjusted $R^2=0.670$, $F(4,46)=26.27, p<0.0001$, HC3 SEs (SAT $b=-0.084$, PULL $b=0.581$, SWEFFORT $b=0.337$, FAM $b=-0.097$). Exploratory Model M2 ($k=6$, $n=51$): $R^2=0.707$, Adjusted $R^2=0.667$, $F(6,44)=17.70, p<0.0001$. | Replace old 7-predictor table with official pre-specified Model M1 and exploratory Model M2 from `table12` and `table12c`. Note HC3 heteroskedasticity-consistent standard errors. |
| **D06** | Former User Exit Reason Classification | **CONFIRMED & RESOLVED** | `table13_former_main_reason.csv` & `table13d_former_coverage_vs_voluntary.csv`: Class A Coverage-primary: 31/73 (42.5%, 95% Wilson CI [31.8%, 53.9%]); Class B Coverage-overlap: 10/73 (13.7%, 95% Wilson CI [7.6%, 23.4%]); Class C Voluntary-only: 32/73 (43.8%, 95% Wilson CI [33.0%, 55.2%]). | Standardize terminology to Class A (Coverage-primary), Class B (Coverage-overlap), and Class C (Voluntary-only). Remove unsupported "lifestyle relocation" narrative. |
| **D07** | Voluntary Exit Reason Terminology | **CONFIRMED & RESOLVED** | `table13e_voluntary_only_main_reason.csv`: Survey option is literally `"Product availability"` (8/32, 25.0%) and `"Product variety / choice"` (8/32, 25.0%). Combined availability + variety = 16/32 (50.0%). | Label items as `"Product availability (8/32)"` and `"Product variety / choice (8/32)"` with combined bracket $16/32 = 50.0\%$. |
| **D08** | Non-Causal Academic Language | **CONFIRMED & RESOLVED** | `final_report.md` §6.3: Within-person centering sensitivity demonstrates correlation collapse (ALT $-0.03$, VAR $+0.31$, PROMO $+0.23$, SWEFFORT $+0.05$). HTMT $=0.923$ for SWEFFORT-INT. | Replace all overclaiming text with exact cautious phrasing: "Diagnosed as measurement overlap/response style sensitivity... switching barriers remain inconclusive, not negligible". |
| **D09** | Holm-Adjusted p-Values | **CONFIRMED & RESOLVED** | `table12a_hypothesis_results.csv`: H1 ($p_{unadj}=0.2341, p_{Holm}=0.2492$), H2–H5 ($p_{unadj}<0.0001, p_{Holm}<0.0001$), H6 ($p_{unadj}=0.0831, p_{Holm}=0.2492$), H7 ($p_{unadj}=0.0897, p_{Holm}=0.2492$). | Explicitly label hypothesis table and cards with `"Holm-adjusted p"` and provide unadjusted p in tooltips/details. |
| **D10** | H7 Sample Size | **CONFIRMED & RESOLVED** | `table12a_hypothesis_results.csv` and `analysis_n_register.csv`: H7 (INERT1) has complete-case $n=46$ (5 early-version respondents did not receive INERT1). | Display $n=46$ prominently for H7 and HTMT analysis. |
| **D11** | UDRHP Document Title & Date | **CONFIRMED & RESOLVED** | `secondary_data/sources.csv` (S01): Updated Draft Red Herring Prospectus-I (UDRHP-I), filed with SEBI on 8 June 2026, 690 printed pages. | Update all references to "Updated Draft Red Herring Prospectus-I (UDRHP-I), 8 June 2026 (690 pages)". |
| **D12** | HTMT Construct Pairs | **CONFIRMED & RESOLVED** | `table22_discriminant_validity_htmt.csv` ($n=46$): SWEFFORT–INT $=0.923$, ALT–VAR $=0.943$, VAR–INT $=0.896$, ALT–INT $=0.874$. | Display exact construct pairs for each HTMT value with the $0.85$ discriminant validity guideline threshold. |
| **D13** | Wilson Score Confidence Interval | **CONFIRMED & RESOLVED** | `table13_former_main_reason.csv`: Coverage-primary 31/73 ($42.47\%$) Wilson 95% CI is $[31.78\%, 53.90\%]$. | Display exact pipeline interval $[31.8\%, 53.9\%]$. |
| **D14** | Literature Register Tiers | **CONFIRMED & RESOLVED** | `literature/references.csv`: 17 total tracked records: Tier A (Full text): 2 (L05, L10); Tier B (Abstract/database verified): 8 (L01, L02, L04, L06, L08, L11, L12, L13); Tier C (Bibliographic record): 5 (L03, L14, L15, L16, L17); UNVERIFIED / Excluded: 2 (L07, L09). | Build literature UI directly from `literature/references.csv` displaying verification tier badges. |
| **D15** | Cohort Retention Data Points | **CONFIRMED & RESOLVED** | `secondary_data/udrhp_evidence_working.csv` (E20, pp. 253–254): FY24-Q1 cohort @ Q9 $= 49.8\%$; FY22 cohort @ Q12 $= 45.2\%$, @ Q15 $= 44.3\%$; mature cohort range $= 44.3\%–54.0\%$. | Plot only verified data points from `table16` and `udrhp_evidence_working.csv`. |
| **D16** | Explicit Denominators | **CONFIRMED & RESOLVED** | `analysis_n_register.csv`: Total $N=184$, Current $n=51$, Current complete-cases $n=46$, Former $n=73$, Former evaluating alternatives $n=68$, Former in H10 test $n=58$, Voluntary former $n=32$, Never $n=60$. | Add explicit denominator chips/labels to every metric, table, card, and chart. |
| **D17** | Filing Capex Period | **CONFIRMED & RESOLVED** | E07 (pp. 143–145): ₹16,289.75M dark store capex is allocated across FY27–FY29; E08 (pp. 143–145): ₹17,349.41M dark store lease liabilities through FY30. | Distinguish FY27–FY29 dark store capex from through-FY30 lease obligations. |
| **D18** | LaTeX String Sanitization | **CONFIRMED & RESOLVED** | Unrendered LaTeX markers like `$n = 51$` or `$\rho$` replaced with semantic HTML `<i>n</i> = 51` and `ρ`. | Clean HTML and Unicode entities used across all components. |

---

## 2. Locked Research Facts Baseline

All statistics are frozen and validated against `outputs/tables/` and `final_report.md`:
- Total Sample: $N = 184$ (Current: $51$, Former: $73$, Never: $60$)
- Questionnaire Versions: V1 ($16$), V1.5 ($6$), V2 ($162$)
- Routing Leaks Isolated: $15$ respondents, $22$ block instances
- Hypotheses: H1 ($\rho = +0.17$), H2 ($\rho = +0.685$), H3 ($\rho = +0.694$), H4 ($\rho = +0.700$), H5 ($\rho = +0.721$), H6 ($\rho = +0.245$), H7 ($\rho = +0.253, n=46$)
- Within-Person Centered: ALT ($-0.03$), VAR ($+0.31$), PROMO ($+0.23$), SWEFFORT ($+0.05$)
- Regression M1: $R^2 = 0.696$, Adjusted $R^2 = 0.670$, $F(4,46) = 26.27$, $p < 0.0001$
- Former Users: Coverage-primary $31/73$ ($42.5\%$), Coverage-overlap $10/73$ ($13.7\%$), Voluntary $32/73$ ($43.8\%$)
- Voluntary Reasons: Product availability $8/32$ ($25.0\%$), Product variety $8/32$ ($25.0\%$), Combined $16/32$ ($50.0\%$)
- Competitor Advantage: $41/68$ ($60.3\%$) found products/variants not on Zepto; $18/68$ ($26.5\%$) Maybe
- Triangulation States: Service coverage (Partial/Convergent Context), Competitor Pull (Partial), Promotions (Partial), Switching Effort (Contradictory), Satisfaction (Insufficient/Contextual), Familiarity/Inertia (Insufficient)
- CRM Recommendations: R1 (Recommended, conditional), R2 (Conditional pilot), R3 (Conditional, $n=16$), R4 (Not recommended on current evidence — re-measure barriers), R5 (Monitor only)
