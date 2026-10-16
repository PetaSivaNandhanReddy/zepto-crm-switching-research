# Statistical Reconciliation & Discrepancy Ledger (DISCREPANCIES.md)

**Project:** `zepto-crm-switching-research`  
**Repository Directory:** `C:\Users\user\Downloads\crm_project_ZEPTO`  
**Governing Rule:** Source of Truth Hierarchy  
1. `outputs/tables/*.csv` and `outputs/statistical_results/*` (Authoritative Empirical Truth)  
2. `final_report.md` (Academic Monograph)  
3. `documentation/CHECKPOINT_*.md` (Historical Research Audits)  
4. Current Page Content (`index.html`)  

> [!IMPORTANT]
> **Source Reconciliation Principle:**
> Tables strictly supersede reports, checkpoints, upgrade plans, or webpage text whenever numerical conflicts arise. No statistic may appear on the upgraded dashboard unless its provenance is traced directly to the canonical CSV tables or result registers.

---

## 1. Executive Reconciliation Summary

During the research pipeline lifecycle, slight differences arose between early drafting text in `final_report.md`, intermediate audit logs (such as `ADVANCED_WEBPAGE_UPGRADE_PLAN.md`), and the final deterministic output CSV tables produced by `run_analysis.py`. 

This ledger documents every verified discrepancy, the competing values, their provenance in the code, and the canonical resolution adopted for the dashboard data layer (`web/site_data.js`).

---

## 2. Itemized Discrepancy Ledger

| Discrepancy ID | Statistical Construct / Metric | Stale / Conflicting Claim (Report / Old Page / Plan) | Verified Canonical Truth (`outputs/tables/` & `statistical_results/`) | Provenance & Generating Script | Verification Status & Dashboard Resolution |
|:---|:---|:---|:---|:---|:---|
| **DISC-01** | **H1: Satisfaction $\rightarrow$ Switching Intention ($\rho$)** | $\rho = +0.165$ (reported in some drafts) | **$\rho = +0.170$** ($+0.169604$), unadjusted $p = 0.2341$, Holm-adjusted $p = 0.2492$, 95% bootstrap CI $[-0.12, +0.44]$, $n = 51$. | `src/hypothesis_testing.py` $\rightarrow$ `outputs/tables/table12a_hypothesis_results.csv` & `outputs/statistical_results/hypothesis_tests_H1_H7.csv` | **RESOLVED:** Display exact $+0.170$, Holm $p = 0.2492$, CI $[-0.12, +0.44]$. Labeled *"Inconclusive / Insufficient evidence"*. |
| **DISC-02** | **H6: Familiarity $\rightarrow$ Switching Intention ($\rho$)** | $\rho = +0.248$ (reported in early summary) | **$\rho = +0.245$** ($+0.245063$), unadjusted $p = 0.0831$, Holm-adjusted $p = 0.2492$, 95% bootstrap CI $[-0.09, +0.54]$, $n = 51$. | `src/hypothesis_testing.py` $\rightarrow$ `outputs/tables/table12a_hypothesis_results.csv` | **RESOLVED:** Display $+0.245$, Holm $p = 0.2492$, CI $[-0.09, +0.54]$. Labeled *"Inconclusive / Insufficient evidence"*. |
| **DISC-03** | **H7: Inertia $\rightarrow$ Switching Intention ($\rho$)** | $\rho = +0.248, n=51$ (reported in early draft) | **$\rho = +0.253$** ($+0.252655$), unadjusted $p = 0.0897$, Holm-adjusted $p = 0.2492$, 95% bootstrap CI $[-0.09, +0.57]$, **valid complete-case $n = 46$**. | `src/hypothesis_testing.py` $\rightarrow$ `outputs/tables/table12a_hypothesis_results.csv` | **RESOLVED:** Display $+0.253$, Holm $p = 0.2492$, CI $[-0.09, +0.57]$, base $n = 46$ (5 V1 respondents lacked `INERT1`). |
| **DISC-04** | **Model M1 Full Regression Fit ($R^2$)** | $R^2 = 0.696$ (stated in old text & Checkpoint 3) | **$R^2 = 0.7057$** ($0.705746$), Adj $R^2 = 0.6802$, $F(4, 46) = 27.57$, $p < 0.0001$, HC3 SEs ($n = 51$). | `src/regression.py` $\rightarrow$ `outputs/statistical_results/regression_diagnostics.csv` & `outputs/tables/table12_regression_results.csv` | **RESOLVED:** Display exact $R^2 = 0.7057$ (or 0.706). Model M1 uses 4 predictors: SAT, PULL, SWEFFORT, FAM. |
| **DISC-05** | **PULL Composite Alone Explanatory Power ($R^2$)** | $R^2 = 0.672$ (speculative block $\Delta R^2$ in old text) | **$R^2 = 0.6356$** ($0.636$), spearman $\rho = 0.768$, pooled $\alpha = 0.934$. Incremental gain from SAT+SWEFFORT+FAM is only $+0.0701$ (7.0%). | `src/measurement_diagnostics.py` $\rightarrow$ `outputs/statistical_results/regression_overlap_diagnostics.csv` | **RESOLVED:** Display $R^2_{\text{PULL alone}} = 0.636$ and incremental $\Delta R^2 = 0.070$ to demonstrate severe item overlap with switching intention. |
| **DISC-06** | **H9: Partial Switching vs Intention (Mann–Whitney $U$)** | $p = 0.6014$, medians 3.33 vs 3.33 (early draft) | **Mann–Whitney $U = 346.5$, $p = 0.6029$**, rank-biserial $r = 0.09$, medians **3.67 (Shifted) vs 3.17 (Not shifted)**, $n = 51$ (29 shifted vs 22 not shifted). | `src/hypothesis_testing.py` $\rightarrow$ `outputs/statistical_results/hypothesis_test_H9.csv` & `table10b_current_partial_shift.csv` | **RESOLVED:** Display exact $p = 0.6029$, medians 3.67 vs 3.17. Labeled *"Inconclusive / Insufficient evidence"*. |
| **DISC-07** | **H10: Willingness to Return (Class A vs C)** | $p = 0.2137$, medians 4.0 vs 3.5 (early draft) | **Mann–Whitney $U = 496.0$, $p = 0.2141$**, rank-biserial $r = 0.18$, medians **4.0 (Class A) vs 3.5 (Class C)**, $n = 58$ (28 Class A vs 30 Class C). | `src/former_never_analysis.py` $\rightarrow$ `outputs/statistical_results/hypothesis_test_H10.csv` | **RESOLVED:** Display exact $p = 0.2141$, medians 4.0 vs 3.5. 10 Class B former users excluded from primary test. |
| **DISC-08** | **Within-Person Centering Sensitivity for VAR** | Stated as $\rho_{\text{centered}} = +0.10$ in upgrade plan | **$\rho_{\text{centered}} = +0.305$** ($+0.305440$), $p = 0.0293$, 95% CI $[-0.004, +0.617]$. Raw $\rho = +0.731$. Evaluated on VAR1 only ($n = 51$). | `src/measurement_diagnostics.py` $\rightarrow$ `outputs/tables/table21_within_person_centering_sensitivity.csv` | **RESOLVED:** Display exact centered $\rho = +0.305$ and raw $+0.731$. Note explicitly that Table 21 uses `VAR1 only` to preserve $n=51$. |
| **DISC-09** | **Construct VAR Items: H3 vs Table 21** | Conflating 2-item composite with single item | **H3 Hypothesis:** Uses 2-item composite `VAR1 + VAR2` ($\rho_{\text{raw}} = +0.694$, $n = 46$ complete cases).<br>**Table 21 Centering:** Uses `VAR1 only` ($\rho_{\text{raw}} = +0.731$, $\rho_{\text{centered}} = +0.305$, $n = 51$). | `src/config.py`, `src/hypothesis_testing.py`, `src/measurement_diagnostics.py` | **RESOLVED:** Explicitly label both: H3 displays $+0.694$ ($n=46$), while sensitivity dumbbell displays $+0.731 \rightarrow +0.305$ ($n=51$, VAR1 only). Never mix them. |
| **DISC-10** | **Construct Scale Reliability Metrics** | Mentioned McDonald's $\omega$ in text/report | **Only Cronbach's $\alpha$ and Spearman-Brown coefficients exist in canonical outputs.** SAT $\alpha = 0.721$, ALT $\alpha = 0.848$, VAR $\alpha = 0.901$, SWEFFORT $\alpha = 0.792$, INT $\alpha = 0.909$, PULL5 $\alpha = 0.916$. | `src/reliability_analysis.py` $\rightarrow$ `outputs/tables/table08_reliability.csv` | **RESOLVED:** Display exact Cronbach's $\alpha$ and Spearman-Brown values from Table 08. Remove references to McDonald's $\omega$. |
| **DISC-11** | **Voluntary Former User Exit Breakdown ($n=32$)** | Vague groupings (e.g. "stock-outs n=8") | **Exact 9 Categories from Table 13e ($n=32$):**<br>1. Product availability: 8 (25.0%) [13.3%–42.1%]<br>2. Product variety / choice: 8 (25.0%) [13.3%–42.1%]<br>3. Delivery experience: 4 (12.5%) [5.0%–28.1%]<br>4. App experience: 3 (9.4%) [3.2%–24.2%]<br>5. Discounts / promotions: 3 (9.4%) [3.2%–24.2%]<br>6. Pricing: 2 (6.25%) [1.7%–20.1%]<br>7. Preferred another platform: 2 (6.25%) [1.7%–20.1%]<br>8. Product quality: 1 (3.1%) [0.6%–15.7%]<br>9. Return / refund experience: 1 (3.1%) [0.6%–15.7%] | `src/former_never_analysis.py` $\rightarrow$ `outputs/tables/table13e_voluntary_only_main_reason.csv` | **RESOLVED:** Display all 9 categories with exact counts, percentages, and Wilson 95% CIs. Product availability + variety combined is $16/32 = 50.0\%$. |
| **DISC-12** | **Secondary Evidence Catalog (`E01`–`E25`)** | Arbitrary numbering in old web text | **25 Verified Records (`E01`–`E25`):** Table 16 has 25 rows and lacks an ID column. Sequential row order defines `E01` to `E25`. | `src/secondary_analysis.py` $\rightarrow$ `outputs/tables/table16_zepto_secondary_evidence.csv` | **RESOLVED:** `build_site_data.py` programmatically injects sequential `E01`–`E25` IDs based on exact Table 16 row order. |
| **DISC-13** | **Media Claims Register (`M01`–`M11`)** | Inconsistent counts (M01–M08 vs M11) | **11 Tracked Records (`M01`–`M11`):** S06, S07, S10 media claims tracked in dedicated register. | `src/secondary_analysis.py` $\rightarrow$ `secondary_data/media_claims_register.csv` | **RESOLVED:** Display all 11 media claims with verification actions and note that media claims are non-evidence. |
| **DISC-14** | **Literature Verification Tiers** | Vague literature count | **17 Tracked Sources:** Tier A (2 full text: L05, L10), Tier B (8 abstract: L06, L08, L11, L14, L15, L16, L17, etc.), Tier C (5 bibliographic: L01, L02, L03, L04, L12, L13), UNVERIFIED (2: L07, L09). | `literature/references.csv` | **RESOLVED:** Display exact 17 records with verification badges. Highlight that UNVERIFIED records (L07, L09) are strictly barred from supporting hypotheses. |
| **DISC-15** | **CRM Strategy Status for R4** | Stated as "active recommendation" in some text | **Status in Table 19:** `Not recommended on current evidence (switching-barrier evidence inconclusive)`. SWEFFORT $\rho = +0.721$ is uninterpretable/anomalous; lock-in interventions are not recommended. | `src/synthesis.py` $\rightarrow$ `outputs/tables/table19_crm_recommendations.csv` | **RESOLVED:** Explicitly flag R4 as *"Not recommended on current evidence"*, explaining that switching barriers are uninterpretable and require re-measurement. |

---

## 3. Discrepancy Notice for Dashboard

The following disclaimer banner is required on the research dashboard:
> *"Report superseded where it differs from the tables; see DISCREPANCIES.md for the complete reconciliation ledger."*
