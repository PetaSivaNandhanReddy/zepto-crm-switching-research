# Investigating Customer Switching Behaviour in India's Quick-Commerce Industry: An Empirical Case Study of Zepto

**Academic Research Monograph & Strategic CRM Report**  
*Authoritative Final Report — Harmonized with UDRHP-I Primary Filing Evidence and Empirical Survey Analysis*  
*Methodological Note: Cross-sectional, non-probability sample ($N=184$). All survey statistical findings represent associations, not econometric causal proofs. Questionnaire Versions: V1 ($n=16$), V1.5 ($n=6$), V2 ($n=162$). Secondary evidence based on the full 690-page SEBI UDRHP-I Master Filing (8 June 2026).*

---

## 1. Title Page & Executive Summary

### Executive Summary

**Context & Problem:** The rapid expansion of India's quick-commerce sector (projected by company-commissioned industry research to reach ~₹963 billion by CY2025) has intensified platform competition. Understanding why consumers switch away from or multi-home across quick-commerce providers—and whether customer relationship management (CRM) interventions can mitigate churn—represents a pivotal managerial and academic challenge. This empirical study investigates customer switching behaviour focusing on Zepto Limited, integrating a primary consumer survey ($N=184$) within the Push-Pull-Mooring (PPM) framework, triangulated against verified disclosures from Zepto's 690-page Updated Draft Red Herring Prospectus (UDRHP-I, 8 June 2026) and peer-reviewed service-switching literature.

**Primary Sample Partition ($N=184$):**
- **Current Users ($n=51$):** Explored for switching intention, perceived alternative attractiveness, competitor variety, promotional pull, satisfaction, switching effort, familiarity, and inertia.
- **Former Users ($n=73$):** Analyzed for behavioural exit drivers, destination platforms, competitor assortment advantages, and return willingness.
- **Never-Users ($n=60$):** Maintained strictly as a non-adoption baseline; **never-users are not switchers and are strictly excluded from switching-away analyses**.

**Key Findings:**
1. **Former-User Behavioural Exits ($n=73$):** The single most prevalent primary reason for discontinuing Zepto usage was service coverage constraints (*"Zepto was not available in my area"*, $31/73 = 42.5\%$, $95\%$ Wilson CI $[32.0\%, 53.6\%]$). This represents an involuntary structural barrier rather than competitive platform preference. Among voluntary-only former leavers ($n=32$), product unavailability ($8/32$) and lack of product variety ($8/32$) together accounted for $50.0\%$ ($16/32$) of primary exit drivers.
2. **Current-User Intention & Fragility of Raw Associations ($n=51$):** On unadjusted raw scores, switching intention exhibited strong positive rank correlations with competitor pull factors: Alternative Attractiveness (H2: $\rho = +0.685$, Holm $p < .001$), Product Variety (H3: $\rho = +0.694$, Holm $p < .001$), and Competitor Promotions (H4: $\rho = +0.700$, Holm $p < .001$). However, within-person centering sensitivity analysis attenuated these relationships substantially (centered ALT $\rho = -0.03$, $[-0.31, +0.25]$; centered VAR $\rho = +0.10$, $[-0.18, +0.37]$; centered PROMO $\rho = +0.23$, $[-0.05, +0.48]$), demonstrating that raw pull correlations reflect general response-style elevation and conceptual item overlap rather than robust, isolated causal effects.
3. **Anomalous Switching Effort Result (H5):** Perceived switching effort correlated positively with switching intention (raw $\rho = +0.721$, Holm $p < .001$), contradicting the theoretical PPM hypothesis ($H5: -$ sign). Following within-person centering, the correlation collapsed to $+0.05$ ($[-0.23, +0.32]$). This result is diagnosed as measurement overlap/bias rather than evidence of beneficial switching friction. Switching barriers in quick commerce remain inconclusive rather than proven negligible.
4. **Non-Significant Push & Mooring Factors:** Neither customer satisfaction (H1: $\rho = +0.165, p = 0.25$), brand familiarity (H6: $\rho = +0.248, p = 0.25$), nor consumer inertia (H7: $\rho = +0.248, p = 0.25$) showed statistically significant associations with switching intention, aligning with published full-text literature indicating that platform satisfaction acts as a baseline hygienic factor rather than a churn differentiator.
5. **Secondary UDRHP Triangulation (`E01`–`E25`):** Zepto's filing confirms strategic alignment: ₹16,289.75M is allocated toward dark-store expansion across FY27–FY29 to eliminate coverage gaps (`E07`, pp. 143–145); store-level SKUs expanded from 12,312 (FY24) to 49,602 (Q4 FY26) (`E13`/`E24`, p. 162, p. 538); and multi-year user cohorts demonstrate ~50% initial attrition before stabilizing between 44.3% and 54.0% active ordering (`E20`, pp. 253–254). While filing disclosures independently corroborate the operational relevance of network coverage and catalog depth, corporate strategy disclosures do not constitute causal proof of individual consumer exit mechanics.

**CRM Strategic Implications ($R1$–$R5$):**
- **R1 (Coverage Waitlist & Pin-Code Demand Capture):** Recommended (conditional, testable) — capture pin-code demand on failed serviceability screens and trigger automated launch notifications.
- **R2 (Assortment Personalization & Restock Alerts):** Conditional (pilot with control group) — utilize existing ML infrastructure (`E18`) to log stock-out searches and recommend algorithmic substitutes.
- **R3 (Reason-Matched Voluntary Win-Back):** Conditional (small $n=16$) — deploy category-specific restock notifications for matched availability/variety leavers; suppress indiscriminate discounting.
- **R4 (Switching Lock-In Interventions):** **Not recommended on current evidence** — switching-barrier evidence is inconclusive and the current measurement is problematic; re-measure with a validated scale before designing lock-in mechanisms.
- **R5 (Trigger-Based Service Recovery):** Monitor only — maintain automated SLA breach service credits as a hygienic operational safeguard.

---

## 2. Research Context

### 2.1 India's Quick-Commerce Landscape
The Indian retail ecosystem has undergone an unprecedented transformation with the advent of quick commerce—hyperlocal delivery of groceries, perishables, and everyday essentials within 10 to 15 minutes. Propelled by dense urban populations, increasing digital penetration, and dark-store infrastructure, quick commerce has expanded beyond impulse grocery purchases into broader merchandise categories including beauty, personal care, electronics, and general merchandise (UDRHP Section IV, pp. 202–205).

Unlike traditional e-commerce models characterized by 24- to 72-hour delivery cycles and substantial basket sizes, quick commerce operates on high transaction frequencies, compressed fulfillment windows, and multi-platform accessibility. Consumers typically install multiple competing applications (e.g., Zepto, Blinkit, Swiggy Instamart, BigBasket Now) on a single smartphone device, enabling instant comparative browsing for product availability, delivery speed, and pricing.

### 2.2 Zepto Corporate Background & Growth Trajectory
Founded in 2021, Zepto Limited has emerged as one of the primary hyper-growth platforms in the Indian quick-commerce market. To finance physical infrastructure expansion and cloud technology, Zepto filed its Updated Draft Red Herring Prospectus (UDRHP-I) with the Securities and Exchange Board of India (SEBI) on 8 June 2026 (S01, 690 printed pages). Key audited parameters disclosed in the filing include:
- **Annual Transacting Users (ATU):** Expanded from 10.57 million (FY24) to 38.38 million (FY25) and reached 47.97 million as of 31 March 2026 (p. 160). Trailing-12-month ATU stabilized slightly from 49.54 million (31 December 2025) while quarterly transaction velocity increased +28.6% QoQ to 2.33 million orders per day in Q4 FY26 (p. 161).
- **Physical Network Scale:** Grew from 337 dark stores across 11 cities (FY24) to 1,029 stores across 43 cities (FY25) and 1,139 dark stores across 66 cities by 31 March 2026 (p. 163).
- **Catalog Breadth:** Store-level unique SKUs rose from 12,312 (FY24) to 44,341 (FY25), 46,623 (FY26), and reached 49,602 in Q4 FY26 (p. 162, p. 538).
- **Financial Structure:** Revenue increased from ₹44,545.16M (FY24) to ₹226,235.84M (FY26), alongside restated net losses of ₹59,051.92M in FY26 driven by dark-store infrastructure rollout and delivery partner costs (p. 24).

### 2.3 Research Problem & Customer Switching in Quick Commerce
Despite exponential top-of-funnel customer acquisition, quick-commerce platforms face severe structural retention challenges. Because app download and setup friction is minimal, consumers multi-home across competing services with negligible technical barriers. Consequently, customer switching behaviour manifests not only as complete account abandonment (dormancy/churn) but also as partial purchase shifting (allocating specific basket categories to rival platforms based on localized product availability or promotions).

Understanding the precise antecedents of customer switching—and separating operational constraints (such as dark-store coverage gaps) from competitive pull factors (such as product assortment and pricing)—is critical for developing evidence-based CRM strategies.

---

## 3. Research Objectives & Questions

### Research Questions
1. **Primary Research Question:** Which push, pull, and mooring factors are significantly associated with customer switching behaviour and switching intentions among quick-commerce users, focusing on Zepto?
2. **Sub-Question 1 (Behavioural Exits):** What primary reasons drive former users to discontinue using Zepto, and how do involuntary coverage constraints compare against voluntary competitive exits?
3. **Sub-Question 2 (Intention & Sensitivity):** How robust are the statistical associations between competitor pull factors and switching intentions when subjected to response-style centering and discriminant validity diagnostics?
4. **Sub-Question 3 (Organizational Triangulation):** How do Zepto's official capital allocations, risk factors, and KPI disclosures in its UDRHP-I filing contextualize the empirical survey findings?
5. **Sub-Question 4 (Managerial CRM Translation):** What testable, conditional CRM interventions can be formulated to address verified churn drivers without relying on unsupported causal assumptions?

### Research Objectives
- **Objective 1:** Formulate and empirically test a conceptual PPM switching model across satisfaction (push), alternative attractiveness, variety, promotions (pull), switching effort, familiarity, and inertia (mooring).
- **Objective 2:** Quantify exit reasons among former users and establish empirical baselines for voluntary vs. involuntary churn.
- **Objective 3:** Synthesize primary survey results with verified corporate disclosures from the SEBI UDRHP-I filing.
- **Objective 4:** Establish actionable, testable CRM recommendations with defined target segments, mechanisms, implementation roadmaps, and measurable KPIs.

---

## 4. Conceptual Framework & Literature Review

### 4.1 The Push-Pull-Mooring (PPM) Framework
Originally derived from human migration theory (Moon, 1995; Bansal et al., 2005), the Push-Pull-Mooring framework posits that service-switching decisions are governed by three interacting forces:
- **Push Factors:** Negative factors at the incumbent service provider that motivate consumers to leave (e.g., service dissatisfaction, delivery delays, poor customer support).
- **Pull Factors:** Positive attributes of alternative providers that attract consumers (e.g., superior product assortment, attractive promotional discounts, lower prices).
- **Mooring Factors:** Personal, psychological, or structural variables that hold consumers to the incumbent or moderate the switching decision (e.g., brand familiarity, habitual inertia, perceived switching effort).

```
+-------------------------------------------------------------------------------+
|                       PUSH-PULL-MOORING SWITCHING MODEL                       |
+-------------------------------------------------------------------------------+
|                                                                               |
|   PUSH FACTORS (Incumbent Provider)                                           |
|   - Customer Dissatisfaction / Low Expectation Fulfilment (H1: -)             |
|                                                                               |
|   PULL FACTORS (Alternative Quick-Commerce Competitors)                       |
|   - Perceived Alternative Attractiveness (H2: +)                              |
|   - Competitor Product Choice / Variety (H3: +)                               |
|   - Competitor Pricing / Promotional Incentives (H4: +)                       |
|                                                                               |
|   MOORING FACTORS (Individual / Structural Anchors)                           |
|   - Perceived Switching Effort / Structural Costs (H5: -)                     |
|   - Incumbent Brand Familiarity (H6: -)                                       |
|   - Habitual Inertia (H7: -)                                                  |
|                                                                               |
|                                     |                                         |
|                                     v                                         |
|                       SWITCHING INTENTION & BEHAVIOUR                         |
|   - Behavioral Exit / Churn (Former Users, n=73)                              |
|   - Switching Intention & Purchase Shifting (Current Users, n=51)             |
|                                                                               |
+-------------------------------------------------------------------------------+
```

### 4.2 Distinguishing Switching Costs from Subjective Norms in Mooring
Academic literature reveals critical distinctions within the mooring construct. While foundational conceptualizations (Burnham et al., 2003; Bansal et al., 2005) emphasized switching costs as structural friction, empirical studies in digital platform settings show diverging patterns:
- In online food delivery platform-to-platform switching in Taiwan ($N=441$), Chang et al. (2023, L05 [Level A]) identified **subjective norms** ($\beta = -0.405, p < .001$) as the primary mooring inhibitor, while **satisfaction push was non-significant** ($\beta = 0.071, p > .05$) and attractive alternatives exerted a strong pull effect ($\beta = 0.328, p < .001$).
- In e-grocery channel-switching in Jakarta ($N=252$), Monoarfa et al. (2023, L10 [Level A]) observed an empirical **positive** coefficient for switching costs ($\beta = +0.294, p = .017$) when items measured the perceived time/effort of adopting the alternative platform, demonstrating that survey measures of perceived switching difficulty frequently capture cognitive burden rather than structural lock-in.

### 4.3 Verified Literature Base & Hypothesis Foundation
The literature register incorporates 17 tracked studies categorized by rigorous verification tiers:
- **Level A (Full-Text Inspected, $n=2$):** Chang et al. (2023, L05), Monoarfa et al. (2023, L10).
- **Level B (Publisher / Database Record Inspected, $n=10$):** Bansal et al. (2005, L01), Guan et al. (2024, L06), Cui et al. (2026, L08), Hung et al. (2024, L11), Celiker et al. (2024, L14), Chen et al. (2023, L15), Singh & Rosengren (2020, L16), Haridasan et al. (2021, L17).
- **Level C (Bibliographic Entry, $n=3$):** Moon (1995, L02), Hsieh et al. (2012, L03), Burnham et al. (2003, L04).
- **UNVERIFIED ($n=2$, Withdrawn):** L07, L09 (withdrawn from evidence base due to unconfirmed metadata).

---

## 5. Methodology

### 5.1 Survey Design, Sampling & Administration
The empirical investigation utilized a structured online questionnaire administered to urban Indian consumers across three deployment iterations:
- **Version 1 (V1, $n=16$):** Initial deployment establishing core screening, demographic, and PPM item batteries.
- **Version 1.5 (V1.5, $n=6$):** Added localized geographic spend and pin-code capture.
- **Version 2 (V2, $n=162$):** Comprehensive final deployment including granular out-of-stock items, expanded mooring batteries, and former-user return intentions.

Total responses collected: **$N=184$**.

```
+-------------------------------------------------------------------------------+
|                       SAMPLE PARTITION ARCHITECTURE (N=184)                   |
+-------------------------------------------------------------------------------+
|                                                                               |
|   TOTAL SAMPLE: N = 184                                                       |
|                                                                               |
|   +-----------------------+-----------------------+-----------------------+   |
|   |                       |                       |                       |   |
|   v                       v                       v                       |   |
|   CURRENT USERS           FORMER USERS            NEVER-USERS             |   |
|   n = 51 (27.7%)          n = 73 (39.7%)          n = 60 (32.6%)          |   |
|   - Active purchasers     - Discontinued usage    - Never used Zepto      |   |
|   - Switching Intention   - Exit Driver Analysis  - Non-adoption baseline |   |
|   - H1-H8 PPM Models      - Return Intent (H10)   - NOT switchers         |   |
|                                                                               |
+-------------------------------------------------------------------------------+
```

### 5.2 Data Cleaning, Validation & Routing Leak Segregation
A strict data-cleaning protocol was implemented in `src/cleaning.py`:
- **Routing Leak Isolation:** 15 unique respondents completed 22 question blocks outside their designated user branch due to legacy survey branching in early form versions. These records were systematically isolated and transferred to supplementary tables (`table05b`, `table16b`), ensuring zero contamination of primary analytical datasets.
- **Missing Value Handling:** Version-specific item additions (e.g., `INERT1` missing in V1) were treated as structural missingness ($NaN$) and evaluated via complete-case analysis ($n=46$ for H7 and HTMT) rather than imputation.
- **Straight-Lining Sensitivity:** Analyzed with and without straight-lining profiles ($n=39$) to ensure response consistency.

### 5.3 Measurement Constructs & Statistical Procedures
- **Constructs:** Satisfaction (`SAT1-2`), Alternative Attractiveness (`ALT1-2`), Product Variety (`VAR1-2`), Competitor Promotions (`PROMO1`), Switching Effort (`SC1-2`), Familiarity (`FAM1`), Inertia (`INERT1`), Switching Intention (`INT1-3`), Partial Shift (`shifted_any`), Return Willingness (`fu_return`).
- **Inferential Testing:** Non-parametric Spearman rank correlation ($\rho$) with 5,000-repetition bootstrap confidence intervals (fixed seed $42$); Family-Wise Error Rate controlled via Holm-Bonferroni correction across H1–H7; exploratory OLS regression with HC3 heteroskedasticity-consistent standard errors; Mann-Whitney $U$ tests for two-group nonparametric comparisons (H9, H10).

---

## 6. Primary Survey Results

### 6.1 Sample Distribution & Demographic Profile
Across the $N=184$ verified sample:
- **User Groups:** Current Users $n=51$ ($27.7\%$), Former Users $n=73$ ($39.7\%$), Never-Users $n=60$ ($32.6\%$).
- **Age Distribution:** $18\text{--}24$ years ($59.8\%$), $25\text{--}34$ years ($27.2\%$), $35+$ years ($13.0\%$).
- **Quick-Commerce Spend:** $\le ₹2,000/\text{month}$ ($48.2\%$), $₹2,001\text{--}₹5,000/\text{month}$ ($33.9\%$), $>₹5,000/\text{month}$ ($17.9\%$).

### 6.2 Core Hypotheses Results ($H1$–$H7$)

```
========================================================================================
                          CORE HYPOTHESIS TESTING MATRIX (n=51)
========================================================================================
Hypothesis  Construct  Expected  Spearman rho  95% Bootstrap CI   Holm p   Decision Status
----------------------------------------------------------------------------------------
H1          SAT           -        +0.165       [-0.12, +0.44]    0.2492   Not supported (Null)
H2          ALT           +        +0.685       [+0.51, +0.81]   <0.0001   Supported (Raw)
H3          VAR           +        +0.694       [+0.52, +0.82]   <0.0001   Supported (Raw)
H4          PROMO         +        +0.700       [+0.53, +0.83]   <0.0001   Supported (Raw)
H5          SWEFFORT      -        +0.721       [+0.56, +0.84]   <0.0001   Anomalous (Opposite)
H6          FAM           -        +0.248       [-0.03, +0.50]    0.2492   Not supported (Null)
H7          INERT         -        +0.248       [-0.05, +0.50]    0.2492   Not supported (Null)
========================================================================================
```

### 6.3 Robustness Check: Within-Person Centering Sensitivity Analysis
To test whether the strong raw pull correlations reflected substantive construct relationships or common-method response elevation, an exploratory within-person centering (ipsatization) analysis was performed:

```
========================================================================================
                 WITHIN-PERSON CENTERING SENSITIVITY ANALYSIS (table21)
========================================================================================
Construct     Raw Spearman rho    Within-Person Centered rho    Centered 95% Bootstrap CI
----------------------------------------------------------------------------------------
ALT               +0.685                   -0.03                    [-0.31, +0.25]
VAR               +0.694                   +0.10                    [-0.18, +0.37]
PROMO             +0.700                   +0.23                    [-0.05, +0.48]
SWEFFORT          +0.721                   +0.05                    [-0.23, +0.32]
========================================================================================
```
*Methodological Evaluation:* When individual mean response tendencies are removed, the correlation between alternative attractiveness and switching intention collapses to $-0.03$, while competitor variety and promotions attenuate to near-zero with confidence intervals spanning zero. This demonstrates that raw pull associations must be interpreted cautiously as associational indicators rather than isolated causal drivers.

### 6.4 Exploratory Regression & Extension Hypotheses ($H8$–$H10$)
- **H8 (M1 PPM Joint Model, $n=51$):** Regressing switching intention on `SAT`, `PULL`, `SWEFFORT`, and `FAM` yielded $R^2 = 0.696$ ($F(4, 46) = 26.27, p < .001$). However, variance decomposition confirms that the `PULL` composite alone explains $R^2 = 0.672$, and high discriminant overlap (`HTMT` with intention = $0.92$) indicates substantial item collinearity.
- **H9 (Intention vs. Partial Shift, $n=51$):** Switching intention did not differ significantly between current users who had shifted purchases to rival platforms ($n_1=29$, median $3.67$) versus those who had not ($n_2=22$, median $3.33$; Mann-Whitney $U = 346.5, p = 0.6014$).
- **H10 (Return Willingness by Former User Class, $n=58$):** Return willingness did not differ significantly between coverage-primary leavers (Class A, $n_1=28$, median $4.0$) and voluntary leavers (Class C, $n_2=30$, median $3.5$; Mann-Whitney $U = 496.0, p = 0.2137$).

### 6.5 Former-User Behavioural Exit Analysis ($n=73$)

```
+-------------------------------------------------------------------------------+
|                    FORMER-USER EXIT REASON TAXONOMY (n=73)                    |
+-------------------------------------------------------------------------------+
|                                                                               |
|   CLASS A: Coverage-Primary (Involuntary Exit)                                |
|   - 31 / 73 (42.5%, 95% Wilson CI: 32.0% - 53.6%)                             |
|   - Primary barrier: "Zepto was not available in my area"                     |
|                                                                               |
|   CLASS B: Partial Coverage Overlap                                           |
|   - 10 / 73 (13.7%)                                                           |
|   - Citing area unserviceability alongside secondary service/price factors    |
|                                                                               |
|   CLASS C: Voluntary-Only Competitive Exits                                   |
|   - 32 / 73 (43.8%)                                                           |
|   - Breakdown of Primary Reasons (n=32):                                      |
|     * Product Availability: 8 / 32 (25.0%)  \  Combined Catalog Gaps:         |
|     * Product Variety:      8 / 32 (25.0%)  /  16 / 32 (50.0%)                |
|     * Delivery Experience:  4 / 32 (12.5%)                                    |
|     * Pricing:              3 / 32 (9.4%)                                     |
|     * Discounts/Promotions: 3 / 32 (9.4%)                                     |
|     * App Experience:       3 / 32 (9.4%)                                     |
|     * Customer Support:     2 / 32 (6.3%)                                     |
|     * Product Quality:      1 / 32 (3.1%)                                     |
|                                                                               |
+-------------------------------------------------------------------------------+
```
Furthermore, among former users who evaluated alternative platforms ($n=68$), **$60.3\%$ ($41/68$) confirmed that the rival platform carried products not easily found on Zepto**, with an additional $26.5\%$ ($18/68$) responding *"Maybe"*, corroborating catalog breadth as a primary competitive vulnerability.

---

## 7. Secondary Evidence — Zepto UDRHP (`E01`–`E25`)

The 25 verified evidence records extracted from the full 690-page master filing (`Zepto Limited - UDRHP-I-1780938548.pdf`) are organized across eight strategic themes:

```
========================================================================================================================
                             ZEPTO UDRHP-I AUTHORITATIVE EVIDENCE REGISTER (E01-E25)
========================================================================================================================
ID   Printed Page  Filing Section           Evidence Classification   Factual Disclosed Parameter
------------------------------------------------------------------------------------------------------------------------
E01  p. 24         Section II: Risk Factors  Company risk disclosure   Revenue grew to Rs 226,235.84M; restated loss Rs 59,051.92M
E02  pp. 27-28     Section II: Risk Factors  Company risk disclosure   Active delivery fleet 221,667; delivery cost 12.28% of NRV
E03  p. 30         Section II: Risk Factors  Company risk disclosure   Merchant partners multi-home across competing platforms
E04  p. 31         Section II: Risk Factors  Company risk disclosure   Competitor discounts, pricing models, assortment cited as risks
E05  p. 34         Section II: Risk Factors  Company risk disclosure   Increases in user fees may decrease transaction frequency
E06  p. 44         Section II: Risk Factors  Company risk disclosure   Dark store network expansion execution and deployment risks
E07  pp. 143-145   Section III: Objects      Offer/object disclosure   Rs 16,289.75M gross proceeds for dark store network expansion
E08  pp. 148-150   Section III: Objects      Offer/object disclosure   Rs 17,349.41M allocated for dark store lease rentals through FY30
E09  pp. 154-156   Section III: Objects      Offer/object disclosure   Rs 4,000.00M allocated for cloud and technology infrastructure
E10  pp. 156-157   Section III: Objects      Offer/object disclosure   Rs 5,200.00M allocated for marketing and business promotion
E11  p. 160        Section III: Basis Price  Company KPI               Annual Transacting Users (ATU) 10.57M -> 38.38M -> 47.97M
E12  p. 161        Section III: Basis Price  Company KPI               Orders/day +28.6% QoQ to 2,333,488; ATU dipped 3.2% from 49.54M
E13  p. 162        Section III: Basis Price  Company KPI               Store SKUs grew: 12,312 (FY24) -> 44,341 -> 46,623 (FY26) (M02)
E14  p. 163        Section III: Basis Price  Company KPI               Dark stores expanded: 337 (11 cities) -> 1,029 -> 1,139 (66 cities)
E15  pp. 194-196   Section IV: Industry      Company-Cited Industry    Quick commerce market grew ~Rs 133B to ~Rs 963B (~95% growth)
E16  pp. 202-205   Section IV: Industry      Company-Cited Industry    Consumer adoption expanding beyond grocery into beauty & electronics
E17  pp. 234-235   Section IV: Business      Company Business Discl.   S.Q.A.P. customer experience framework & EDLP operating philosophy
E18  pp. 246-247   Section IV: Business      Company Business Discl.   In-house ML search and recommendation query parsing engine
E19  p. 252        Section IV: Business      Company Business Discl.   Categories purchased: ~6 in Month 1 -> >12 Year 1 -> 18 Year 2 (M10)
E20  pp. 253-254   Section IV: Business      Company KPI               Cohort active ordering stabilizes between 44.3% and 54.0% (M03)
E21  pp. 258-259   Section IV: Business      Company Business Discl.   Zepto Pass official subscription program; "Zepto Club" absent (M04)
E22  pp. 260-261   Section IV: Business      Company Business Discl.   Dark store densification reduces radius for <10-15 min delivery SLA
E23  pp. 530-532   Section V: MD&A           Company/MD&A Disclosure   Supply Chain Variable Cost per Order defines fulfillment cost floor
E24  p. 538        Section V: MD&A           Company/MD&A Disclosure   Management links SKU depth (49,602 Q4 FY26) + EDLP to retention
E25  pp. 545-547   Section V: MD&A           Company/MD&A Disclosure   Advertising and sales promotion spend tracked across city rollouts
========================================================================================================================
```

---

## 8. Secondary Evidence Visualizations & Corporate Trajectories

```
========================================================================================
1. STORE-LEVEL SKU EXPANSION TRAJECTORY (E13 / E24, p. 162, p. 538)
FY24:       [12,312 SKUs]   ==================
FY25:       [44,341 SKUs]   ====================================================
FY26:       [46,623 SKUs]   =======================================================
Q4 FY26:    [49,602 SKUs]   ==========================================================
*Corporate metric: Documents strategic catalog deepening; does not prove causal exit reduction.*

2. PHYSICAL DARK STORE FOOTPRINT EXPANSION (E14, p. 163)
FY24:       [337 Stores / 11 Cities]    =============
FY25:       [1,029 Stores / 43 Cities]  ========================================
FY26:       [1,139 Stores / 66 Cities]  ============================================

3. ANNUAL TRANSACTING USERS (ATU) ADOPTION SCALE (E11 / E12, pp. 160-161)
FY24:       [10.57 Million ATU]  =========
FY25:       [38.38 Million ATU]  ================================
FY26:       [47.97 Million ATU]  ========================================
*Note: Platform adoption KPI; trailing 12-month unique user count, not individual retention.*

4. COHORT RETENTION STABILIZATION BENCHMARK (E20, pp. 253-254)
Month 1:    [100.0%]  ==================================================================
Quarter 2:  [ 51.5%]  ==================================
Quarter 4:  [ 48.0%]  ================================
Quarter 8:  [ 46.5%]  ===============================
Quarter 12: [ 45.2%]  ==============================  (FY23 Q2 Cohort Year 3 Retention)
Quarter 15: [ 44.3%]  =============================   (FY23 Q2 Cohort Year 4 Retention)
*Note: Longitudinal benchmark shows ~50% initial attrition before cohort stabilization.*
========================================================================================
```

---

## 9. Media Claim Verification Register (`M01`–`M11`)

```
========================================================================================================================
                               MEDIA CLAIMS VERIFICATION REGISTER (M01-M11)
========================================================================================================================
ID   Media Stated Proposition               UDRHP Verification Finding & Location                     Final Status
------------------------------------------------------------------------------------------------------------------------
M01  Zepto acknowledges low switching costs  Risk Factor 6 (pp. 30-32) discloses competitor pricing,  NOT VERIFIED AS WORDED /
                                            incentives, and multi-homing; literal claim absent       CONTEXTUALIZED
M02  SKUs rose from 12,312 to 46,623         Verified on p. 162 & p. 538: reached 49,602 in Q4 FY26   VERIFIED - PRIMARY KPI
M03  45.2%-49.8% active after 3 years        Verified on pp. 253-254: FY23 Q2 was 45.2% at Q12,       VERIFIED - PRIMARY COHORT
                                            FY24 Q1 was 49.8% at Q9; multi-year band 44.3%-54.0%     EVIDENCE
M04  Zepto Club paid membership launched     Filing establishes "Zepto Pass" (p. 13, p. 258);         DISPROVED / CONTRADICTED
                                            "Zepto Club" is not established in the filing
M05  1,139 stores vs 1,029 (FY25) & 337 (24) Verified on p. 163 and S09 p. 13 across 66 cities       VERIFIED - PRIMARY KPI
M06  ATU reached 47.97M at 31 Mar 2026       Verified on p. 160: 10.57M (24) -> 38.38M -> 47.97M      VERIFIED - PRIMARY KPI
M07  Order volume CAGR about 119.5%          Verified on p. 3 quoting commissioned Redseer Report     VERIFIED - COMPANY-CITED
M08  Rs 1,629 cr stores; Rs 1,735 cr leases  Verified on pp. 143, 148 (Rs 16,289.75M & Rs 17,349.41M) VERIFIED - OFFER DISCL.
M09  Active base dipped from 49.54M to 47.97M Verified on p. 161 (trailing ATU dipped 3.2% in Q4)     VERIFIED - PRIMARY KPI
M10  Retained users buy 18+ categories       Verified on p. 252 (6 categories M1 -> 12 Y1 -> 18 Y2)  VERIFIED - BUSINESS DISCL.
M11  Delivery partners multi-home freely     Verified on pp. 27-28, 56 (Risk Factor 13)               VERIFIED - RISK DISCLOSURE
========================================================================================================================
```

---

## 10. Literature Evidence Synthesis

```
========================================================================================================================
                               VERIFIED LITERATURE EVIDENCE BASE (L01-L17)
========================================================================================================================
ID   Authors & Year         Context & Sample           Framework   Key Verified Finding                  Tier
------------------------------------------------------------------------------------------------------------------------
L01  Bansal et al. (2005)   Service consumers (~700)   PPM         PPM outpredicts alternative models;   Level B (Abstract)
                                                                   push, pull, mooring direct effects
L02  Moon (1995)            Migration theory (N/A)     Mooring     Conceptual origin of mooring          Level C (Biblio)
L04  Burnham et al. (2003)  Switching cost typology    Mooring     Typology of procedural/relational     Level C (Biblio)
L05  Chang et al. (2023)    Food delivery, Taiwan (441) PLS-SEM     Pull significant (0.328);             Level A (Full Text)
                                                                   Satisfaction n.s. (0.071); Mooring=SN
L06  Guan et al. (2024)     Retailers, Group Buying (365) PPM      Push & pull significant;              Level B (Abstract)
                                                                   switching cost non-significant
L08  Cui et al. (2026)      Video e-commerce           PPM         Inertia acts as moderator             Level B (Abstract)
L10  Monoarfa et al. (2023) E-Grocery, Jakarta (252)   CB-SEM      Pull (0.314); Dissatisfaction n.s.;   Level A (Full Text)
                                                                   Switching cost POSITIVE (+0.294)
L11  Hung et al. (2024)     Electronics, Vietnam (1,104) PPM       Habit lessens switching (-0.136)      Level B (Abstract)
L15  Chen et al. (2023)     Smart lockers, parcel senders PPM      Inertia reduces switching intention   Level B (Abstract)
L16  Singh & Rosengren (20) Online grocery shoppers    PPM         Pull & push factors significant       Level B (Abstract)
L17  Haridasan et al. (21)  Cross-channel switching (456) PPM      Low switching costs strengthen pull   Level B (Abstract)
========================================================================================================================
```

---

## 11. Integrated Triangulation Matrix

```
========================================================================================================================
                                    INTEGRATED FACTOR-BY-FACTOR TRIANGULATION
========================================================================================================================
Factor: Service Coverage (Zepto not available in respondent's area)
- Primary Evidence:    31/73 former users (42.5%) cite area as main exit; 37/60 never-users cite unserved locality.
- Secondary Evidence:  [S01 pp. 143-145] Rs 16,289.75M earmarked for dark store network rollout across FY27-FY29 (E07).
- Literature Evidence: Insufficient: standard PPM literature models voluntary provider choice, omitting coverage barriers.
- Statistical Result:  Descriptive frequency with Wilson CI [32.0%, 53.6%]. Non-inferential.
- Overall Class:       PARTIAL / CONVERGENT CONTEXT (Non-Causal)
- Strategic CRM:       R1: Serviceability waitlist and pin-code demand capture; expansion-triggered notifications.
------------------------------------------------------------------------------------------------------------------------
Factor: Competitor Pull: Alternative Attractiveness & Product Choice/Variety
- Primary Evidence:    ALT rho=+0.69, VAR rho=+0.69 (raw, p<.001); 16/32 voluntary former leavers cite availability/variety.
- Secondary Evidence:  [S01 p. 162, p. 538] Store SKUs expanded from 12,312 to 49,602 (E13, E24); competitor risk (E04).
- Literature Evidence: L05 (Level A) and L10 (Level A) confirm strong pull effects of attractive alternatives.
- Statistical Result:  Supported on raw scores; fragile to centering (ALT centered rho=-0.03); high HTMT overlap (0.94).
- Overall Class:       PARTIAL
- Strategic CRM:       R2: Stock-out query logging, restock alerts, and algorithmic substitute recommendations via ML.
------------------------------------------------------------------------------------------------------------------------
Factor: Competitor Promotions / Pricing
- Primary Evidence:    PROMO raw rho=+0.70 (p<.001); but cited as main exit reason by only 5/73 former users.
- Secondary Evidence:  [S01 p. 31, p. 34] Competitor discounts/fees disclosed as strategic risk (E04, E05); EDLP policy (E17).
- Literature Evidence: Indirect support: promotional deals embedded as sub-items in alternative attraction scales (L05).
- Statistical Result:  Supported on raw single item; centered rho=+0.23 (CI spans zero).
- Overall Class:       PARTIAL
- Strategic CRM:       Suppression of indiscriminate platform-wide discounts; priority on catalog availability.
------------------------------------------------------------------------------------------------------------------------
Factor: Switching Effort (Mooring)
- Primary Evidence:    SWEFFORT rho=+0.72 (raw, p<.001, opposite to H5); centered rho=+0.05.
- Secondary Evidence:  [S01 pp. 27-28, 56] Delivery and merchant partners multi-home freely; consumer multi-app usage common.
- Literature Evidence: Mixed: L10 (Level A) observed positive switching-cost sign; L06 (Level B) non-significant.
- Statistical Result:  Contradictory / Anomalous. Collapses to zero after centering. High HTMT with intention (0.92).
- Overall Class:       CONTRADICTORY
- Strategic CRM:       R4: No lock-in interventions recommended on current evidence. Re-measure with validated scale.
------------------------------------------------------------------------------------------------------------------------
Factor: Satisfaction / Expectation Fulfilment (Push)
- Primary Evidence:    SAT mean 3.88; rho with intention = +0.165 (Holm p=0.25, non-significant). Experience issues minority.
- Secondary Evidence:  [S01 p. 13, p. 260] S.Q.A.P. framework; store densification targeting <10-15 min delivery SLA (E17, E22).
- Literature Evidence: Full-text studies L05 (Level A, p=0.071) and L10 (Level A, p=0.069) confirm non-significant push.
- Statistical Result:  Inconclusive / Null.
- Overall Class:       INSUFFICIENT / CONTEXTUAL
- Strategic CRM:       R5: Monitor-only operational safeguard; trigger-based service credits on SLA breaches.
------------------------------------------------------------------------------------------------------------------------
Factor: Familiarity / Habitual Inertia (Mooring)
- Primary Evidence:    FAM rho=+0.248 (p=0.25), INERT rho=+0.248 (p=0.25) (unexpected signs, non-significant).
- Secondary Evidence:  [S01 p. 252] Cohort purchasing expands from 6 to 18 categories over 2 years (E19).
- Literature Evidence: Abstract-level only: L11 (habit, -0.136), L15 (inertia negative).
- Statistical Result:  Inconclusive / Insufficient.
- Overall Class:       INSUFFICIENT
- Strategic CRM:       No loyalty lock-in recommended without empirical behavioral validation.
========================================================================================================================
```

---

## 12. Integrated Interpretation & Final Findings

### Direct Answer to the Research Question
The empirical evidence indicates that customer switching in quick commerce is driven by a hierarchy of structural, competitive, and operational factors:

1. **Structural Coverage Constraints Dominate Behavioural Exits:** Service coverage unserviceability is the single largest reported exit factor ($42.5\%$ of former users, $61.7\%$ of never-users). When dark-store delivery boundaries do not encompass a consumer's locality, exit is involuntary and structural rather than a rejection of brand or service quality.
2. **Catalog Depth & Availability are Primary Voluntary Levers:** Among voluntary leavers, product availability and assortment breadth represent $50.0\%$ ($16/32$) of primary exit drivers. While raw survey correlations between pull factors and switching intention are elevated ($\rho \approx 0.69\text{--}0.70$), within-person centering demonstrates that these reflect shared response tendencies rather than standalone causal drivers.
3. **Satisfaction Operates as a Baseline Hygiene Factor:** In concordance with verified full-text literature (L05, L10), platform satisfaction does not exhibit a significant negative relationship with switching intention ($\rho = +0.165, p = 0.25$). High satisfaction does not insulate quick-commerce platforms from churn if a competitor offers broader assortment or localized speed advantages.
4. **Switching Costs are Inconclusive, Not Negligible:** The anomalous positive correlation for switching effort (H5: $\rho = +0.721$) reflects respondent interpretation of the effort required to adopt alternative workflows rather than structural lock-in. While platform multi-homing is structurally frictionless on mobile devices, consumer switching barriers cannot be definitively characterized as negligible without validated behavioral experimentation.
5. **Organizational Triangulation:** Zepto's UDRHP filing confirms that corporate resource allocation directly mirrors these empirical dynamics (allocating ₹16,289.75M to dark-store rollout and expanding SKUs to 49,602). However, filing disclosures describe corporate strategic intentions and KPIs rather than econometric proofs of individual switching causes.

---

## 13. Strategic CRM Recommendations (`R1`–`R5`)

```
========================================================================================================================
                                      ACTIONABLE CRM RECOMMENDATION MATRIX
========================================================================================================================
RECOMMENDATION R1: Localized Serviceability Waitlist & Demand Capture (Conditional, Testable)
- Problem:          Coverage-driven churn and non-adoption (31/73 former users, 37/60 never-users).
- Evidence:         Primary survey confirms coverage as dominant barrier; UDRHP earmarks Rs 16,289.75M for dark stores (E07).
- Target Segment:   Consumers in unserved pin codes who downloaded the app or former users who moved to unserved areas.
- Mechanism:        Pin-code capture on failed serviceability screens; automated SMS/push notification upon dark store rollout.
- Implementation:   Capture pin code at install; match against dark store expansion pipeline; trigger launch promotion.
- Expected Outcome: Increased first-order conversion upon geographic launch (to be tested, not assumed).
- KPI & Metrics:    Waitlist registration volume; waitlist-to-first-order conversion rate; 30/90-day repeat frequency.
- Limitations:      Captures latent demand rather than repairing voluntary brand switching; stated return intent overstates action.
------------------------------------------------------------------------------------------------------------------------
RECOMMENDATION R2: Assortment-Gap Notification & Algorithmic Substitution (Conditional Pilot)
- Problem:          Product unavailability and variety gaps driving voluntary competitor switching (16/32 former leavers).
- Evidence:         Survey H2/H3 raw associations; UDRHP confirms 49,602 SKUs and in-house ML recommendation engine (E18, E24).
- Target Segment:   Active current users experiencing repeated out-of-stock search queries or zero-result search terms.
- Mechanism:        Automated "Notify Me on Restock" triggers and algorithmic nearest-substitute ranking via existing ML engine.
- Implementation:   A/B pilot testing personalized substitute recommendations vs control group with standard out-of-stock screen.
- Expected Outcome: Reduction in search abandonment and basket abandonment to rival platforms (to be tested in pilot).
- KPI & Metrics:    Notify-me opt-in conversion; repeat order rate among stock-out affected users; substitute acceptance rate.
- Limitations:      Associational survey evidence; recommendation engine effectiveness is a proposed test, not a proven outcome.
------------------------------------------------------------------------------------------------------------------------
RECOMMENDATION R3: Reason-Matched Voluntary Former-User Win-Back (Conditional, Small n)
- Problem:          Voluntary churn among users leaving due to catalog limitations (n=16 availability/variety leavers).
- Evidence:         15/30 voluntary former users express willingness to return; UDRHP shows category breadth reaching 18 (E19).
- Target Segment:   Former users whose recorded exit reason or last failed search history was product availability/variety.
- Mechanism:        Category-specific reactivation alerts when the relevant product line is expanded; suppress generic discounts.
- Implementation:   Map dormant account historical stock-out logs to newly onboarded merchant SKUs; deploy targeted alert.
- Expected Outcome: Incremental reactivation without eroding unit economics through platform-wide discounts (pilot test).
- KPI & Metrics:    Reactivation conversion rate vs control; 30/60/90-day post-reactivation repeat rate; margin per reactivated cart.
- Limitations:      Small sample segment (n=16); all-reason discount incentives not supported by survey evidence.
------------------------------------------------------------------------------------------------------------------------
RECOMMENDATION R4: Switching-Cost / Habit Lock-In (NOT RECOMMENDED ON CURRENT EVIDENCE)
- Problem:          Theoretical desire to build customer lock-in and switching barriers.
- Evidence:         Survey H5 anomalous (rho=+0.721); within-person centering collapses to zero; UDRHP notes multi-homing (E03).
- Target Segment:   None.
- Mechanism:        NONE. Do not deploy structural friction or punitive exit barriers.
- Implementation:   Re-measure switching barriers with a validated, reverse-worded scale before designing lock-in interventions.
- Expected Outcome: Avoid misallocating capital into artificial lock-in mechanisms that generate consumer resistance.
- KPI & Metrics:    N/A.
- Limitations:      Switching-barrier evidence is inconclusive and the current measurement is problematic.
------------------------------------------------------------------------------------------------------------------------
RECOMMENDATION R5: Operational Service Recovery Safeguard (Monitor Only)
- Problem:          Service, app, and delivery SLA failures creating negative experiential push factors (minority exit driver).
- Evidence:         Satisfaction null correlation; service issues represent minority mentions (delivery 7/73, app 6/73).
- Target Segment:   All transacting users experiencing delivery delays (>15 min SLA breach) or damaged goods.
- Mechanism:        Trigger-based automated customer support credits using existing ZAP customer service infrastructure (E17, E22).
- Implementation:   Automated SLA monitoring; immediate app credit issuance for breached orders without manual ticket friction.
- Expected Outcome: Prevents catastrophic single-incident churn; acts as hygienic operational safeguard.
- KPI & Metrics:    Breach-to-credit resolution time; repeat order retention within 14 days of an SLA breach.
- Limitations:      Hygienic safeguard; will not serve as a primary competitive differentiator against rival catalog breadth.
========================================================================================================================
```

---

## 14. Academic & Managerial Implications

### Academic Contributions
1. **Separation of Structural Coverage from Choice-Driven Switching:** Demonstrates that in emerging hyperlocal logistics platforms, geographic serviceability must be modeled as an exogenous structural boundary rather than a conventional push or mooring construct.
2. **Methodological Critique of PPM Item Overlap:** Highlights the empirical fragility of self-report pull correlations in digital service settings, demonstrating that within-person centering and discriminant validity checks (HTMT) are essential to prevent inflated effect-size claims.
3. **Mooring Construct Nuance:** Corroborates recent empirical findings (Monoarfa et al., 2023) that perceived switching effort measures cognitive adoption burden rather than structural switching costs.

### Managerial Takeaways for Quick-Commerce Executives
1. **Prioritize Catalog Availability over Price Wars:** Voluntary switching is primarily driven by missing products and lack of variety rather than promotional discounts. Indiscriminate discount subsidies erode unit economics without addressing root-cause churn.
2. **Leverage Demand Capture for Network Expansion:** Dark-store rollout planning should directly incorporate pin-code waitlist demand data to ensure rapid first-order conversion upon store launch.
3. **Operationalize ML Recommendation Systems as CRM Retention Tools:** Transform recommendation engines from merchandising tools into active churn-mitigation mechanisms that handle stock-out events through intelligent substitute ranking.

---

## 15. Limitations & Boundary Conditions

1. **Sample Size & Cross-Sectional Design:** The current-user sample ($n=51$) provides limited statistical power for complex structural equation modeling. All reported correlations represent cross-sectional associations, not causal relationships.
2. **Measurement Overlap & Response Styles:** Strong raw pull correlations are susceptible to general response elevation, as evidenced by within-person centering attenuation.
3. **Self-Reported Exit Motivations:** Former-user exit reasons ($n=73$) represent retrospective self-reports that may be subject to recall bias.
4. **Secondary Data Constraints:** UDRHP-I disclosures represent company-reported metrics and strategic intentions prepared for regulatory compliance, not independent causal evaluations of consumer behavior.
5. **Commissioned Research Caveat:** Redseer report figures quoted in the UDRHP represent company-commissioned industry research and must not be interpreted as independent third-party evaluations.

---

## 16. Conclusion

This study provides an empirically grounded, multi-method investigation of customer switching behaviour in Indian quick commerce. By integrating primary consumer survey data with verified disclosures from Zepto's SEBI UDRHP-I filing, the findings demonstrate that quick-commerce churn is bifurcated: involuntary exits are governed by dark-store coverage boundaries, while voluntary competitive switching is driven by catalog depth and product availability. Strategic CRM must move away from generic price subsidies and artificial lock-in mechanisms, focusing instead on localized demand capture, real-time stock-out notifications, and algorithmic catalog personalization.

---

## 17. References

- Bansal, H. S., Taylor, S. F., & St. James, Y. (2005). 'Migrating' to new service providers: Toward a unifying framework of consumers' switching behaviors. *Journal of the Academy of Marketing Science*, 33(1), 96–115. [Level B]
- Burnham, T. A., Frels, J. K., & Mahajan, V. (2003). Consumer switching costs: A typology, antecedents, and consequences. *Journal of the Academy of Marketing Science*, 31(2), 109–126. [Level C]
- Celiker, O., Ozen, U., & Bolen, M. C. (2024). Understanding Consumers' Switching Intention from e-Commerce to Social Commerce: A Mixed Methods Study. *International Journal of Innovation and Technology Management*, 21(1). [Level B]
- Chang, I.-C., Shiau, W.-M., Lin, C.-Y., & Shih, D.-H. (2023). Consumer Intentions to Switch On-Demand Food Delivery Platforms: A Perspective from Push-Pull-Mooring Theory. *Journal of Theoretical and Applied Electronic Commerce Research*, 18(4), 2217–2232. [Level A - Full Text]
- Chen, L., Wu, P., Dou, Y., & Wu, Y. (2023). Investigating senders' switching intention to smart lockers: An extension of push-pull-mooring model. *Journal of Retailing and Consumer Services*, 74, 103414. [Level B]
- Cui, Y., Yao, X., Zhao, D., & Li, J. (2026). The influence of information processing on consumer switching intention from traditional to short video e-commerce: a structural equation modelling study. *Asia Pacific Journal of Marketing and Logistics*. [Level B]
- Guan, Z., Shi, X., Ying, H., Xue, R., & Qiao, X. (2024). An empirical study on traditional offline retailer's switching intention towards community-based group buying program: A push-pull-mooring model. *Electronic Markets*, 34(1), article 18. [Level B]
- Haridasan, A. C., Fernando, A. G., & Balakrishnan, S. (2021). Investigation of consumers' cross-channel switching intention. *Journal of Consumer Behaviour*, 20(6), 1545–1560. [Level B]
- Hsieh, J.-K., Hsieh, Y.-C., Chiu, H.-C., & Feng, Y.-C. (2012). Post-adoption switching behavior for online service substitutes: A perspective of the push-pull-mooring framework. *Computers in Human Behavior*, 28(5), 1912–1920. [Level C]
- Hung, P. D., Thong, V. H., Tuan, P. V., Khoa, N. H. D., & Trang, N. Q. (2024). Switching intention to online channel in Vietnam - A case study of consumer electronics goods. *Cogent Business & Management*, 11(1), 2291861. [Level B]
- Monoarfa, T. A., Sumarwan, U., Suroso, A. I., & Wulandari, R. (2023). Switch or Stay? Applying a Push-Pull-Mooring Framework to Evaluate Behavior in E-Grocery Shopping. *Sustainability*, 15(7), 6018. [Level A - Full Text]
- Moon, B. (1995). Paradigms in migration research: Exploring 'mooring' as a schema. *Progress in Human Geography*, 19(4), 504–524. [Level C]
- Redseer Strategy Consultants. (2026). *India's Quick-Commerce Industry: Market Structure and Growth Drivers* (Commissioned by Zepto Limited; cited in UDRHP-I). [Company-Cited]
- Singh, R., & Rosengren, S. (2020). Why do online grocery shoppers switch? An empirical investigation. *Journal of Retailing and Consumer Services*, 53, 101962. [Level B]
- Zepto Limited. (2026). *Updated Draft Red Herring Prospectus - I (UDRHP-I)*. Securities and Exchange Board of India (SEBI), 690 printed pages. [Master Filing Source S01]

---

## 18. Appendices

### Appendix 1: Analysis Sample-Size Register (`analysis_n_register.csv`)
- Total Respondent Profile / Distribution: $N = 184$
- Location & Spend Descriptives: $n = 168$ (16 structurally missing in V1)
- Current-User Models (H1–H6): $n = 51$
- Current-User Models with Inertia (H7) & HTMT complete cases: $n = 46$
- M1 PPM Regression Model: $n = 51$ ($12.8$ cases per predictor)
- Former-User Exit Drivers: $n = 73$
- Former-User Return Intentions: $n = 68$ (5 structurally missing in V1)
- Never-User Non-Adoption Analysis: $n = 60$
- Supplementary Leaked Branch Incidents: $n = 7$ current users ($15$ unique respondents overall)

### Appendix 2: Authoritative Statistical Tables Cross-Reference
- `table01_demographics.csv`: Demographic partition across user groups.
- `table07_literature_hypothesis_evidence.csv`: Literature evidence classes per hypothesis.
- `table08_reliability.csv`: Cronbach's alpha and McDonald's omega reliability coefficients.
- `table10_descriptive_statistics_current.csv`: Means, medians, standard deviations, and IQR for current users ($n=51$).
- `table12a_hypothesis_results.csv`: Complete empirical results for hypotheses H1–H10.
- `table12_regression_results.csv`: OLS HC3 regression models M1 and M2.
- `table13_former_main_reason.csv`: Primary exit reason breakdown for former users ($n=73$).
- `table13e_voluntary_only_main_reason.csv`: Granular breakdown of voluntary exits ($n=32$).
- `table16_zepto_secondary_evidence.csv`: All 25 UDRHP evidence items (`E01`–`E25`).
- `table17_industry_secondary_evidence.csv`: Independent Redseer secondary publications.
- `table18_triangulation.csv`: Multi-factor integrated triangulation matrix.
- `table19_crm_recommendations.csv`: Actionable CRM recommendations R1–R5.
- `table21_within_person_centering_sensitivity.csv`: Centered correlation sensitivity analysis.
- `table22_discriminant_validity_htmt.csv`: Heterotrait-Monotrait discriminant validity matrix.
