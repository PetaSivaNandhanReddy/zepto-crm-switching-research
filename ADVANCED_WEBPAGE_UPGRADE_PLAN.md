# ADVANCED WEBPAGE UPGRADE PLAN
**Project:** Zepto CRM Switching Research — presentation layer
**Status:** PLAN ONLY. No code has been changed. Awaiting your approval (see "Decisions I need from you" in §0.6).

---

## 0. Repository inspection record (read this first)

### 0.1 What I actually read
| Item | Status |
|---|---|
| Repo landing page + README | Read |
| `final_report.md` (583 lines, all sections incl. H1–H10, E01–E25, M01–M11, L01–L17, triangulation, R1–R5, appendices) | Read in full |
| `index.html` (1,506 lines) | Read lines ~1–1000 (hero, sections 01–07 incl. hypotheses, robustness, former users, UDRHP tabs, media register). **Not read:** Literature, Triangulation, CRM, Findings sections |
| `app.js`, `styles.css` | **Not read** (blocked by fetch tool) |
| `src/`, `outputs/`, `documentation/` (incl. CHECKPOINT_1–4), `literature/`, `secondary_data/` | **Not read** (folder pages blocked by GitHub robots rules) |

So this plan is built on the finalized report plus the first two-thirds of the existing page. Anything marked **VERIFY** must be checked by Antigravity against `outputs/` before it is shown. If you can paste/upload `app.js`, the rest of `index.html`, the four CHECKPOINT files and the aggregate tables (`table01, 07, 08, 12, 12a, 13, 13e, 18, 19, 21, 22`), I will tighten the plan. These contain only aggregates, no respondent-level data.

### 0.2 Source-of-truth hierarchy (rule for the whole upgrade)
1. `outputs/tables/*.csv` and `outputs/statistical_results/*` (pipeline output)
2. `final_report.md`
3. `documentation/CHECKPOINT_*.md`
4. Existing `index.html`

If (1) and (2) agree and (4) differs → correct the page and log it. If (1) and (2) disagree → STOP and ask you. If a value exists only in (4) → do not carry it forward until you confirm a source (hide, log, do not delete from backup).

### 0.3 Discrepancy register: existing page vs finalized report
These are the most important findings of the inspection. They are **flagged, not auto-fixed**, but the upgrade cannot be faithful until they are resolved. Several would be noticed by an examiner.

| ID | Sev | Existing page says | Finalized report says | Proposed handling |
|---|---|---|---|---|
| D01 | High | Questionnaire versions "V1 n=75 / V2 n=109"; "Mann-Whitney U=346.5, p=0.6014 confirms measurement invariance across versions" | V1 n=16, V1.5 n=6, V2 n=162. U=346.5, p=0.6014 is **H9** (intention: shifted n=29 vs not n=22), not a version test | Replace version chart with 16/6/162. Remove "invariance verified". Show U/p only under H9 |
| D02 | High | Return-willingness table over n=73; voluntary 10/32 = 31.3% | Return intention measured on n=68 (5 structurally missing in V1). H10: Class A n=28 (median 4.0) vs Class C n=30 (median 3.5), U=496.0, p=0.2137. R3 cites 15/30 voluntary willing to return | Rebuild from `table13*`/H10 outputs; hide current table until reconciled |
| D03 | High | UDRHP IDs and amounts differ (e.g. tech ₹3,200M "E21", branding ₹10,000M "E20", ATU "E06/E07", retention "E08") | Register E01–E25: capex ₹16,289.75M = E07 (pp.143–145); leases ₹17,349.41M = E08; cloud/tech ₹4,000.00M = E09 (pp.154–156); marketing ₹5,200.00M = E10 (pp.156–157); ATU = E11/E12; SKUs = E13; stores = E14; cohorts = E20 | Rebuild every UDRHP card from `table16_zepto_secondary_evidence.csv` |
| D04 | High | Demographics: age 72.8/20.7/4.3/2.2%, occupation (students 64.1%), geography (146 metro / 38 non-metro) | Age 59.8% (18–24), 27.2% (25–34), 13.0% (35+); spend bands 48.2/33.9/17.9%; location/spend descriptives n=168. No occupation/geography in report | Use `table01_demographics.csv` only; hide occupation/geography unless in table01 |
| D05 | High | 7-predictor "hierarchical OLS" table (coefficients, SEs, VIF), adj R²=.648, F(7,43)=14.07, block ΔR² (Pull 0.672 / Mooring 0.018 / Push 0.006) | M1 = SAT, PULL composite, SWEFFORT, FAM; R²=.696; F(4,46)=26.27; HC3 SEs; PULL composite alone R²=.672. **Internal inconsistency on the page:** SWEFFORT t=2.634 implies a unique contribution ≈0.049, which is larger than the stated Mooring block ΔR²=0.018, impossible if the block enters last | Take regression only from `table12_regression_results.csv`. Do not carry the 7-predictor table unless it exists there |
| D06 | High | Class A "Involuntary Relocation", Class B "Non-serviceable… lifestyle shifted", "geofencing" CRM text | A = coverage-primary ("not available in my area", 31/73); B = partial coverage overlap (10/73); C = voluntary-only (32/73) | Use report/table13 definitions. The "relocation" story is unsupported |
| D07 | Med | "stock-outs (n=8)" | "Product Availability 8/32" | Keep the survey's label unless `table13e` option text literally says stock-out. "Availability in my area" is the **coverage** item, "product availability" is a different item |
| D08 | Med | "proving +0.721 was a methodological artifact"; PROMO "Partially Robust"; "switching is pull-driven rather than grievance-driven"; "Dissatisfaction is not the primary driver" | "Diagnosed as measurement overlap/bias… barriers inconclusive, not negligible". PROMO centered CI [−0.05, +0.48] spans zero | Replace with report wording; always show CIs; no "proving", no causal verbs |
| D09 | Med | Column "p-value" for H1–H7 | Report values are **Holm-adjusted** (H1, H6, H7 all 0.2492 — plausible under Holm step-down). H6 and H7 share ρ=+0.248 with different n (51 vs 46) and CIs | Label "Holm-adjusted p". VERIFY H6/H7 ρ in `table12a`; show raw p if available |
| D10 | Med | H7 listed with n=51 | Appendix: H7 and HTMT use complete cases n=46 | Show n per row |
| D11 | Med | UDRHP "Draft Red Herring Prospectus… May 2026" | **Updated** DRHP-I, filed with SEBI 8 June 2026, 690 printed pages | Correct wording and date |
| D12 | Med | HTMT absent from sections I read | HTMT 0.92 (intention overlap; SWEFFORT triangulation row; H8 text) and 0.94 ("high HTMT overlap", competitor-pull row). Pairs not named for each | Read `table22`; label the exact construct pair for each value. Your brief's "≈0.92 SWEFFORT–intention" must be confirmed there |
| D13 | Low | — | Wilson CI for 31/73 given as [32.0%, 53.6%]; standard Wilson (z=1.96) recomputes to ≈[31.8%, 53.9%] | Display the pipeline's value; tell the pipeline owner (you) to check method/rounding |
| D14 | Low | — | Literature tiers: report says Level B n=10 but names 8; A=2, C=3, Unverified=2 → 15 enumerated vs 17 tracked; L03, L14 in reference list but absent from the table | Build cards from the literature CSV; show only what exists; preserve tiers |
| D15 | Low | Retention chart uses cohort points | Report's ASCII chart shows Q2 51.5%, Q4 48.0%, Q8 46.5% with no source tag; only Q12 45.2%, Q15 44.3%, FY24-Q1 49.8% @Q9 and band 44.3–54.0% (pp.253–254) are cited | Chart only points traceable to `table16`/`secondary_data` |
| D16 | Low | — | Mixed denominators in triangulation/R5 (PROMO "5/73", delivery "7/73", app "6/73") vs voluntary-only breakdown (n=32) | Label every denominator; VERIFY in `table13/13e` |
| D17 | Low | Capex "through FY30" | Report: "FY27–FY29" in one place, "through FY30" for leases | Quote the exact filing text from `table16` |
| D18 | Low | Raw `$n = 51$`, `$\rho$` strings in HTML | — | No MathJax/KaTeX is loaded in the part of `<head>` I read, so these likely display as literal dollar-sign text unless `app.js` handles them. Replace with proper HTML (`<i>n</i>`, `ρ`) |

### 0.4 Methods: what the repository actually evidences
**Verified in `final_report.md`:** Spearman ρ with 5,000-rep bootstrap 95% CI (seed 42); Holm–Bonferroni across H1–H7; exploratory OLS with HC3 SEs; Mann–Whitney U (H9, H10); Wilson CI; Cronbach's α and McDonald's ω (`table08`); HTMT (`table22`); within-person centering / ipsatization (`table21`); routing-leak isolation (15 respondents, 22 blocks); structural missingness with complete-case analysis (n=46); straight-lining sensitivity.
**Not found in the report (VERIFY in `documentation/` and `outputs/` before showing):** PCA, KMO, Bartlett's test, MSA, VIF, Fisher's exact test, "factor diagnostics". The existing page shows VIF, the report does not. These get an `if_verified` flag in the config; if not found they are **not displayed** and are logged.

Two technical accuracy notes for the formula panels:
- With Likert data (many ties), software computes Spearman as the Pearson correlation of ranks. The shortcut ρ = 1 − 6Σd²/n(n²−1) is exact only without ties. Show both with that caveat.
- HTMT needs monotrait–heteromethod correlations, which do not exist for single-item constructs (PROMO1, FAM1, INERT1). Cronbach's α likewise cannot be computed for them. VERIFY in `table08`/`table22` how the pipeline handled this and show "single-item" badges.

### 0.5 Concept map of the finalized study (for my own consistency, and for Antigravity)
N=184 → Current 51 (27.7%), Former 73 (39.7%), Never 60 (32.6%). Never-users are non-adopters, excluded from all switching analyses; contextual only (37/60 = 61.7% cite unserved locality).
Current-user raw ρ with intention: SAT +0.165, ALT +0.685, VAR +0.694, PROMO +0.700, SWEFFORT +0.721, FAM +0.248, INERT +0.248. Centered: ALT −0.03, VAR +0.10, PROMO +0.23, SWEFFORT +0.05 (CIs in report).
Former users: 31/73 = 42.5% coverage-primary; voluntary n=32: availability 8, variety 8 = 16/32 = 50.0%; 41/68 = 60.3% rival had products not easily found on Zepto (18/68 "Maybe").

### 0.6 Decisions I need from you
1. **Site-only content** (D04 occupation/geography, D05 7-predictor table, D02 return table): hide until sourced (my recommendation), or do you have the source?
2. **Which statistics source wins** if `outputs/` and `final_report.md` disagree: stop and ask (default) — OK?
3. **Optional recommendation, not auto-applied:** add a short "Methods not used" note (no SEM/PLS-SEM because n=51). Include or skip?
4. **Vendor Chart.js locally** (works offline at the viva) — yes/no?
5. **Dark mode** — include or skip (default: skip, light only, lower risk)?

---

## A. Current website assessment (from what I read)

**Strengths to keep:** clear numbered sections; KPI strip; non-causal warnings already present; Chart.js charts for group split, hypotheses, raw-vs-centered, voluntary reasons, competitor advantage, five UDRHP views; tabbed UDRHP; filterable M01–M11 register with page references (a genuinely good, examiner-friendly feature); tables with exact parameters.

**Weaknesses:**
- No visible research story or methodology; an examiner cannot see *how* the study was done.
- Methods (HTMT, Holm, bootstrap CI, HC3, Wilson CI) are not surfaced as methods.
- Heavy tables; little hierarchy between headline findings and diagnostics.
- Inline `style=` heights and inline `onclick` handlers; tabs lack ARIA roles; emoji used as semantic icons.
- Several wording/number problems (D01–D18).
- Navigation has 11 flat links and no phase grouping.

## B. Current architecture
Static site at repo root: `index.html` (1,506 lines), `styles.css`, `app.js`; Chart.js 4.4.1 from jsDelivr; Google Fonts (Inter, Outfit, JetBrains Mono). Data hard-coded in HTML tables and (presumably) arrays in `app.js`. Python pipeline (`run_analysis.py`, `src/`) is separate and ends with independent verification and a consistency check. `.gitignore` excludes raw data and UDRHP PDFs.

## C. Research-content architecture
Every content block carries metadata, rendered as a small source line and badges:

`evidence_layer` ∈ {raw_association, robustness, former_user_reported, company_secondary, literature, triangulated, crm}
`source_ref` (table file / report section / UDRHP page / L-ID), `n`, `denominator`, `analysis_type` ∈ {descriptive, inferential, exploratory}, `data_origin` ∈ {survey, company_disclosure, literature}, `verification_tier` (A/B/C/Company-cited) where applicable.

This makes the seven-layer distinction (raw → robustness → former-user → company → literature → triangulated → CRM) a structural property of the page, not a styling choice.

## D. Visual design system
- Light-first, quiet academic canvas (lavender-tinted off-white), violet as structure colour, magenta only for emphasis, green/amber/red strictly semantic.
- Cards: 1px borders, small radius (6–10 px), soft shadow on hover only; no glassmorphism except the sticky nav (subtle blur).
- Large mono numerals for headline metrics; every number accompanied by its n.
- Motion: 150–250 ms transitions, section reveals via IntersectionObserver, all disabled under `prefers-reduced-motion`.
- Evidence states use **icon + text + pattern**, never colour alone.

## E. Colour palette
See `design_tokens.css` (§X). Summary: deep violet `#5B21B6` / ink `#2E1065` / electric `#7C3AED` / lavender `#EDE9FE`; magenta accent `#A21CAF` (text-safe) and `#D946EF` (graphics only); charcoal text `#1A1523`; muted `#575062`; success `#166534`, warning `#92400E`, danger `#991B1B` with tinted backgrounds. PPM colours: Push teal `#0E7490`, Pull magenta `#A21CAF`, Mooring violet `#5B21B6`. Antigravity must compute and log WCAG contrast for every text/background pair (target ≥ 4.5:1 body, ≥ 3:1 large text/graphics).

## F. Typography
Three families only: **Inter** (UI/body), **Source Serif 4** (section titles, pull-quotes: the academic voice; replaces Outfit), **JetBrains Mono** (statistics, IDs, page refs). Base 17–18 px desktop / 16 px minimum mobile; line-height 1.6; max line length ~70ch; tabular numerals for stats.

## G. Proposed page structure
Sticky top bar with 5 phase groups and a progress rail. Section IDs in brackets.

| # | Section | Phase | Notes |
|---|---|---|---|
| 0 | Hero | — | Title, N=184 with 51/73/60 split bar, Push·Pull·Mooring, one-sentence research statement, evidence-equation strip (Survey + Analytics + UDRHP + Literature + Triangulation = CRM strategy), "what this study does not claim" chip |
| 1 | Question & Objectives `[question]` | Design | RQ, SQ1–SQ4, Objectives 1–4 |
| 2 | Research Design: Methodology Flowchart `[method]` | Design | The centrepiece (§H) + Methods Library |
| 3 | Primary Survey & Segmentation `[survey]` | Design | Group split, V1/V1.5/V2, demographics, routing/missingness notes, analysis-n register |
| 4 | PPM Framework & Measurement `[ppm]` | Design | Interactive PPM (§I), constructs/items, reliability, HTMT |
| 5 | Current Users: H1–H7 `[current]` | Evidence | §K |
| 6 | Robustness & Measurement Diagnostics `[robustness]` | Diagnostics | §L, visually prominent |
| 7 | Former Users `[former]` | Evidence | §M |
| 8 | Never-Users (context) `[never]` | Evidence | Small, explicitly "not switchers" |
| 9 | Secondary Evidence: UDRHP + Media register `[udrhp]` | Evidence | §N, M01–M11 retained |
| 10 | Literature `[literature]` | Evidence | §O |
| 11 | Triangulation `[triangulation]` | Synthesis | §P |
| 12 | CRM Strategy `[crm]` | Action | §Q |
| 13 | Final Interpretation `[findings]` | Synthesis | Answer to "What does this study actually tell us?", claims ledger (supported / cautious / not claimable), limitations |
| 14 | Sources & Reproducibility `[sources]` | — | Report links, repo, pipeline command, verification tiers |

## H. Methodology flowchart design
**Form:** hybrid HTML + SVG. Desktop: horizontal "swim-lane" with 5 phase bands (Design · Data & Measurement · Analysis · Evidence Synthesis · Action) and a vertical flow inside each band. Mobile: vertical stepper, nodes as accordions, no horizontal scroll.

**Nodes** (from `research_flow.json`, §X): START Research Problem → Objectives → PPM Framework → Primary Survey (N=184; V1 16 / V1.5 6 / V2 162) → Segmentation (Current 51 / Former 73 / Never 60) → Data preparation & measurement → Current-user analysis → Former-user analysis → Never-user analysis → Secondary evidence → Literature → Triangulation → CRM recommendations (R1–R5) → FINAL INTERPRETATION.

**Interactions**
- Each node is a real `<button>` (keyboard-focusable); Enter/Space opens a detail panel (what was done, n, methods used, outputs file, source line, "what this step cannot show").
- Hover/focus tooltip with one-line summary.
- "Trace evidence" mode: click an R1–R5 node and the path back to its sources lights up (links come only from the report's own R-field evidence lists).
- Stage progress indicator synced with scroll; "Play path" button (optional, off by default, respects reduced motion).
- Branch nodes (segmentation, current/former/never) drawn as forks; "if_verified" nodes (PCA/KMO/Bartlett/MSA, VIF, Fisher) render only if the config flag is true.

**Visual rules:** thin 1.5px connectors, square-ish nodes, number badges for stage order, phase colours from tokens, no icons-as-meaning without text. Not gimmicky: no bouncing, no particle effects.

## I. PPM visualization design
Three-column SVG (Push | Pull | Mooring) feeding a "Switching intention (current users, n=51)" box. Each construct tile shows: label, item codes (SAT1–2, ALT1–2, VAR1–2, PROMO1, SC1–2 [SWEFFORT], FAM1, INERT1), hypothesised sign, observed raw ρ, centered ρ (where in `table21`), Holm p, n, and a "single-item" badge where applicable.
- Toggle: **Hypothesised / Raw / Centered**. Centered state greys out constructs without centered results.
- H5 tile carries a "sign opposite to hypothesis" tag and an "HTMT 0.92, inconclusive" tag.
- Connectors are dashed and labelled "hypothesised direction (PPM)"; legend states "not estimated causal paths". No path-coefficient styling.
- A second small panel shows the former-user outcome (exit reason classes) separately, so intention and behaviour are not visually merged.

## J. Statistical-method visualization
"Methods Library" (inside Section 2): cards with badge, one-line purpose, where used, n, status chip (`Verified in report` / `Verify in outputs`), and an expandable "View formula" panel.

Cards (final list depends on D-checks in §0.4): Spearman ρ + bootstrap CI; Holm–Bonferroni; OLS (HC3); Cronbach's α / McDonald's ω; HTMT; within-person centering; Mann–Whitney U; Wilson CI; routing-leak isolation & structural missingness; straight-lining sensitivity. Conditional: PCA/KMO/Bartlett/MSA, VIF, Fisher's exact.

Formulas (expandable; Unicode/HTML by default, KaTeX optional): Spearman (with tie note), OLS, α, HTMT (with single-item note), Wilson interval, Holm step-down. **Within-person centering:** formula shown only after Antigravity confirms the exact definition in `src/` (don't guess).

## K. Primary-results visualization improvements
- Replace the correlation bar chart with a **dot-and-whisker plot** (custom SVG): ρ with 95% bootstrap CI for H1–H7, vertical zero line, hypothesised direction marker, fixed hypothesis order (not sorted by size), n per row (H7: 46 if confirmed). Pull factors and SWEFFORT are tagged "Raw association"; no star colouring suggesting importance.
- Result cards H1–H7 (accordion): finding, ρ, CI, Holm p, n, interpretation, caution badge, link to the robustness row.
- Always paired view: "Raw ρ" beside "Centered ρ" when available.
- Regression: one compact card from `table12` (M1, R², F, HC3, n/predictor ratio 12.8) labelled **Exploratory**, with the note that PULL composite alone gives R²=.672 and HTMT overlap exists. No "variance dominance" language.
- H8–H10 as "Extension tests" with their exact n and null results.

## L. Robustness / diagnostics visualization
Four-step explainer: **Raw correlation → Within-person centering → Association weakens → Interpretation becomes cautious.**
- **Dumbbell chart** (SVG): for ALT, VAR, PROMO, SWEFFORT raw ρ (filled) → centered ρ (hollow) with centered CI bars crossing zero.
- **HTMT panel:** value shown on a neutral 0–1 axis for the pair confirmed in `table22`, with text "raises discriminant-validity / measurement-overlap concern". Threshold lines only if the repository documents the cut-off reference; otherwise a recommendation (see §Y R-rec 2).
- **Callout "Switching barriers remain inconclusive"**: H5 opposite sign + centered collapse + HTMT + literature mix (L10 positive coefficient, L06 non-significant). Explicit non-statement: "This does not mean switching costs are unimportant."
- Presented as a methodological strength: "Why we tested this", "What we found", "What follows".

## M. Former-user visualization
1. **Segmented bar (n=73):** A coverage-primary 31 (42.5%, Wilson CI per output) | B partial coverage overlap 10 (13.7%) | C voluntary-only 32 (43.8%). Two visually distinct treatments: *Coverage / non-serviceability* (hatched, structural) vs *Voluntary competitive exit* (solid). Text labels + pattern, not colour only.
2. **Voluntary reasons (n=32):** horizontal bars, sorted by count, with a bracket "Product availability 8 + Variety 8 = 16/32 (50.0%)". Other reasons: delivery 4, pricing 3, discounts/promotions 3, app 3, support 2, quality 1.
3. **Destination evidence (n=68):** 41/68 (60.3%) "rival carried products not easily found on Zepto"; 18/68 (26.5%) "Maybe". Denominator tag: "68 former users who evaluated alternatives".
4. **Return intention (n=68; H10 n=58):** show only after D02 reconciliation.
Source line each time; "self-reported, retrospective" caution badge.

## N. UDRHP evidence visualization
- **Evidence cards** grouped by theme, each with: E-ID, page chip (printed page), filing section, classification (company risk / offer / KPI / industry / business / MD&A), disclosed value, "contextualises → [triangulation factor]", and "does not show: individual consumer causality".
- Themes → IDs (from the report register): dark-store expansion & execution (E06, E07, E08, E14); densification (E22); SKU/assortment (E13, E24); ATU & orders/day (E11, E12); cohort retention (E20); search/recommendation tech (E18); category breadth (E19); Zepto Pass (E21); merchant multi-homing (E03); delivery-partner risks (E02); competitor promotions/fees (E04, E05, E25); technology & marketing allocations (E09, E10); industry context (E15, E16 — company-cited Redseer).
- **Timeline strip** FY24 → FY25 → FY26 → Q4 FY26 as three small multiples (SKUs, stores/cities, ATU) on shared x. Retention: only traceable points (D15).
- Persistent banner: "Company disclosure. Contextual/secondary evidence. Does not independently prove the survey relationships."
- M01–M11 register retained as a filterable table, plus a status legend (verified KPI / contextualised / disproved / company-cited).

## O. Literature visualization
Filter chips: PPM framework · Switching intention · Pull factors · Mooring/switching costs · Online grocery/e-grocery · CRM implications (theme mapping comes from the literature CSV; where absent, a card appears under "Unclassified", not guessed).
Card fields: Author(s), year, context, sample, method/framework, main finding, "informs this study how", verification tier badge (A full text / B abstract-database / C bibliographic / Unverified withdrawn). Missing fields render "Not recorded in repository". Highlight pair L05 + L10 (Level A) as the only full-text anchors. L07/L09 shown only in an "excluded" disclosure.

## P. Triangulation visualization
Matrix: rows = 6 factors; columns = Primary survey | Former-user evidence | UDRHP | Literature | **Integrated conclusion**. Cells contain the report's text (short) with expand. **Only the Integrated column gets a state chip**, taken from the report:

| Factor | Integrated state |
|---|---|
| Service coverage | PARTIAL / CONVERGENT CONTEXT (non-causal) |
| Competitor pull: alternative attractiveness & variety | PARTIAL |
| Competitor promotions / pricing | PARTIAL |
| Switching effort | CONTRADICTORY |
| Satisfaction | INSUFFICIENT / CONTEXTUAL |
| Familiarity / inertia | INSUFFICIENT |

Per-cell states are not given in the report; inventing them would be fabrication, so they are not shown (optional later if `table18` has them). Filters by state; legend with icon + text + pattern. Contradictory is never softened: Switching effort has its own annotated card.

## Q. CRM recommendation visualization
Horizontal chain per recommendation: **Evidence → Customer problem → CRM action → Test design → KPI → Risk/limitation**, using the report's Problem/Evidence/Segment/Mechanism/Implementation/Expected outcome/KPI/Limitations fields. Evidence chips link back to the flowchart "trace" and to E-IDs.
Status badges (exact report wording): R1 *Recommended (conditional, testable)*; R2 *Conditional pilot (control group)*; R3 *Conditional, small n (16)*; R4 *Not recommended on current evidence — re-measure switching barriers with a validated scale first*; R5 *Monitor only*. R4 is styled as a "stop" card, not an action card. "Test design" is only populated where the report states one (R2 A/B pilot; R1 waitlist-to-order conversion tracked); otherwise "To be designed". Filter by status.

## R. Interactive features (priority)
Must: sticky nav with phase groups + progress rail; interactive methodology flowchart; PPM toggle; method badges/formula panels; "What does this mean?" expanders; triangulation/CRM/literature/media filters; chart hover details; reduced-motion support.
Should: evidence-trace from R1–R5; "claims ledger" at the end; print stylesheet for viva handout.
Could: guided "viva mode" (stage-by-stage walk), copy-citation button for source lines.

## S. Accessibility
Semantic landmarks (`header/nav/main/section/footer`), one `h1`, ordered headings; skip link; ARIA roles for tabs/accordions/filters (`tablist`, `aria-expanded`, `aria-pressed`, `aria-live` for filter counts); visible focus ring; every chart has a text alternative and a data-table toggle; state chips = icon + text + pattern; contrast verified; `prefers-reduced-motion`; minimum 16 px text; touch targets ≥ 44 px; no information in hover only.

## T. Mobile strategy
Single column; nav collapses to a phase drawer with progress; flowchart becomes vertical accordion stepper; dot-and-whisker and dumbbell charts keep ≥ 320 px viewBox and scale down; tables become card lists or horizontally scrollable inside their own container; triangulation matrix becomes per-factor accordions; sticky "source" chips never overlap content.

## U. Technical implementation plan
- No framework. Keep Chart.js 4.4.1 for bar/line charts. Custom SVG (hand-rolled, small) for dot-and-whisker, dumbbell, PPM and flowchart connectors.
- **No ES modules and no `fetch` for local data**, because both fail on `file://` in common browsers. Data is delivered as `window.SITE_DATA` in a generated classic script (`web/site_data.js`), so double-clicking `index.html` still works.
- `src/build_site_data.py` reads `outputs/tables/*.csv` + `web_config/*.json` and writes `web/site_data.js`. Numbers on the page come from here, not from hand-typed HTML. (Matches your existing rule: change source/config, rerun, don't hand-edit generated outputs.)
- `src/verify_site.py` scans `index.html`, `app.js`, `web/site_data.js` for numeric tokens in a locked-facts list and fails if any differs from the tables. Add as an optional final step, do **not** weaken or reorder the existing verification in `run_analysis.py`.
- Section reveal and progress with IntersectionObserver; charts lazy-init when visible.
- Optional: vendor Chart.js to `web/vendor/chart.umd.min.js` (pin version, keep license header).
- Keep existing element IDs and anchors so report links don't break; add redirects (`<span id="old-id">`) for any renamed section.

## V. Files to modify
`index.html` (restructure, add sections, ARIA, remove inline handlers/styles, fix D-items), `styles.css` (import tokens, new components), `app.js` (reorganise by section; keep working chart code; add tab/accordion/filter handling), `README.md` (add "Website" section and the build/verify commands).

## W. New files
`web/design_tokens.css`, `web/flow.js` (flowchart + PPM + SVG charts), `web/site_data.js` (generated), `web_config/*.json` (below), `src/build_site_data.py`, `src/verify_site.py`, `WEBSITE_UPGRADE_LOG.md`, `SITE_CORRECTION_LOG.md`. Backup = git branch `site-upgrade` + tag `site-v1-pre-upgrade` (no duplicate folders).

## X. Supporting data/configuration files
Hand-written configs hold **structure and wording only**. All statistics/pages/denominators are pulled from tables by the build script.
Not created by me, to be generated from tables: `literature_display` and `evidence_visualization_data` (I haven't seen those CSVs; hand-typing them would risk errors).

### X.1 `web/design_tokens.css` (place in `web/`; `@import`/link before `styles.css`)
```css
:root{
  /* Brand / structure */
  --primary:#5B21B6; --primary-dark:#2E1065; --primary-mid:#7C3AED; --primary-light:#EDE9FE;
  --accent:#A21CAF;            /* text-safe magenta */
  --accent-bright:#D946EF;     /* graphics/highlights only, never body text */
  /* Surfaces */
  --background:#FAF8FF; --surface:#FFFFFF; --surface-alt:#F3EFFC;
  --border:#E3DDF2; --border-strong:#C9BFE3;
  /* Text */
  --text:#1A1523; --text-muted:#575062; --text-on-primary:#FFFFFF;
  /* Semantic (restrained) */
  --success:#166534; --success-bg:#DCFCE7;
  --warning:#92400E; --warning-bg:#FEF3C7;
  --danger:#991B1B;  --danger-bg:#FEE2E2;
  /* PPM */
  --ppm-push:#0E7490; --ppm-pull:#A21CAF; --ppm-mooring:#5B21B6;
  /* Evidence states (always paired with icon + text + pattern) */
  --state-convergent:var(--success);  --state-partial:var(--warning);
  --state-contradictory:var(--danger); --state-insufficient:var(--text-muted);
  /* Type */
  --font-ui:"Inter",system-ui,-apple-system,"Segoe UI",sans-serif;
  --font-serif:"Source Serif 4",Georgia,"Times New Roman",serif;
  --font-mono:"JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;
  --fs-base:1.0625rem; --lh-base:1.6;
  /* Shape / elevation / motion */
  --radius-sm:6px; --radius-md:10px;
  --shadow-sm:0 1px 2px rgba(46,16,101,.06);
  --shadow-md:0 6px 20px rgba(46,16,101,.10);
  --ease:cubic-bezier(.2,.7,.2,1); --t-fast:150ms; --t-med:250ms;
  --space-1:.25rem; --space-2:.5rem; --space-3:1rem; --space-4:1.5rem; --space-5:2.5rem; --space-6:4rem;
  --focus-ring:0 0 0 3px rgba(124,58,237,.45);
}
*:focus-visible{outline:none;box-shadow:var(--focus-ring);border-radius:var(--radius-sm)}
@media (prefers-reduced-motion:reduce){
  *{animation:none!important;transition:none!important;scroll-behavior:auto!important}
}
```

### X.2 `web_config/research_flow.json` (drives the flowchart)
`display: "if_verified"` nodes appear only if `src/build_site_data.py` finds the method in `documentation/` or `outputs/`.
```json
{
  "phases": [
    {"id":"design","label":"Design"},
    {"id":"data","label":"Data & Measurement"},
    {"id":"analysis","label":"Analysis"},
    {"id":"synthesis","label":"Evidence Synthesis"},
    {"id":"action","label":"Action"}
  ],
  "nodes": [
    {"id":"problem","phase":"design","label":"Research Problem","detail":"Customer switching and multi-homing in Indian quick commerce; coverage constraints must be separated from competitive pull.","source":"final_report §2.3, §3","anchor":"#question"},
    {"id":"objectives","phase":"design","label":"Research Objectives","detail":"Four objectives: test PPM model; quantify exit reasons; synthesise with UDRHP-I; formulate testable CRM actions.","source":"final_report §3","anchor":"#question"},
    {"id":"ppm","phase":"design","label":"Push–Pull–Mooring Framework","sub":["Push: Satisfaction","Pull: Alternative attractiveness, Variety, Promotions","Mooring: Switching effort, Familiarity, Inertia"],"detail":"Hypotheses H1–H7 fixed before testing.","source":"final_report §4.1","anchor":"#ppm"},
    {"id":"survey","phase":"design","label":"Primary Survey","metric":"N = 184","sub":["V1 n=16","V1.5 n=6","V2 n=162"],"detail":"Cross-sectional, non-probability online questionnaire; three deployment versions.","source":"final_report §5.1","anchor":"#survey"},
    {"id":"segment","phase":"design","label":"Respondent Segmentation","branches":[{"id":"current","label":"Current users","n":"n = 51"},{"id":"former","label":"Former users","n":"n = 73"},{"id":"never","label":"Never-users","n":"n = 60","note":"Not switchers; contextual only"}],"detail":"Branching logic separates intention (current), behaviour (former) and non-adoption (never).","source":"final_report §5.1","anchor":"#survey"},
    {"id":"prep","phase":"data","label":"Data Preparation","sub":["Routing-leak isolation (15 respondents, 22 blocks)","Structural missingness, complete-case (n=46 for H7/HTMT)","Straight-lining sensitivity","Questionnaire-version handling"],"detail":"Early-version items treated as structurally missing, not imputed.","source":"final_report §5.2","anchor":"#survey"},
    {"id":"measure","phase":"data","label":"Measurement & Data Quality","sub":["Cronbach's alpha / McDonald's omega","HTMT discriminant validity"],"conditional":[{"label":"PCA / KMO / Bartlett / MSA","display":"if_verified"}],"detail":"Single-item constructs (PROMO1, FAM1, INERT1) cannot have alpha.","source":"final_report App.2 (table08, table22)","anchor":"#ppm"},
    {"id":"current_an","phase":"analysis","label":"Current-User Analysis","metric":"n = 51","sub":["Spearman ρ + 5,000-rep bootstrap CI","H1–H7, Holm-adjusted p","Exploratory OLS (HC3)","Within-person centering sensitivity"],"conditional":[{"label":"VIF","display":"if_verified"}],"detail":"Raw associations first; robustness second.","source":"final_report §5.3, §6.2–6.4","anchor":"#current"},
    {"id":"robust","phase":"analysis","label":"Robustness & Diagnostics","sub":["Raw → centered ρ","HTMT overlap","H9 partial-shift test"],"detail":"Pull associations weaken substantially after centering; H5 inconclusive.","source":"final_report §6.3","anchor":"#robustness"},
    {"id":"former_an","phase":"analysis","label":"Former-User Analysis","metric":"n = 73","sub":["Exit-reason frequencies","Coverage vs voluntary classification","Alternative-destination item (n=68)","Return intention (H10, Mann–Whitney)"],"conditional":[{"label":"Fisher's exact test","display":"if_verified"}],"detail":"Descriptive with Wilson CI; self-reported.","source":"final_report §6.5","anchor":"#former"},
    {"id":"never_an","phase":"analysis","label":"Never-User Context","metric":"n = 60","detail":"Non-adoption baseline; 37/60 cite unserved locality. Excluded from switching analyses.","source":"final_report §11 (coverage row)","anchor":"#never"},
    {"id":"secondary","phase":"synthesis","label":"Secondary Evidence","sub":["Zepto UDRHP-I (E01–E25, 690 pp.)","Media claim register M01–M11","Company-cited Redseer industry data"],"detail":"Company disclosure: contextual, not independent proof.","source":"final_report §7–9","anchor":"#udrhp"},
    {"id":"lit","phase":"synthesis","label":"Literature Evidence","sub":["Switching behaviour","PPM","Online/e-grocery switching","Switching-cost / retention"],"detail":"17 tracked records with verification tiers A/B/C/Unverified.","source":"final_report §4.3, §10","anchor":"#literature"},
    {"id":"tri","phase":"synthesis","label":"Triangulation","sub":["Academic literature","Primary survey","Former-user evidence","Company evidence"],"detail":"Integrated classes: Partial / Contradictory / Insufficient.","source":"final_report §11","anchor":"#triangulation"},
    {"id":"crm","phase":"action","label":"CRM Recommendations","sub":["R1 Coverage demand capture","R2 Assortment / stock-out recovery","R3 Reason-matched win-back","R4 Switching-barrier measurement (not lock-in)","R5 Service recovery monitoring"],"detail":"Conditional and testable; no causal assumptions.","source":"final_report §13","anchor":"#crm"},
    {"id":"final","phase":"action","label":"Final Interpretation","detail":"Cautious, evidence-based CRM strategy; what can and cannot be claimed.","source":"final_report §12","anchor":"#findings"}
  ],
  "edges": [
    ["problem","objectives"],["objectives","ppm"],["ppm","survey"],["survey","segment"],
    ["segment","prep"],["prep","measure"],
    ["measure","current_an"],["measure","former_an"],["segment","never_an"],
    ["current_an","robust"],
    ["robust","secondary"],["former_an","secondary"],["never_an","secondary"],
    ["secondary","lit"],["lit","tri"],["tri","crm"],["crm","final"]
  ],
  "trace": {
    "R1":["former_an","never_an","secondary"],
    "R2":["current_an","former_an","secondary"],
    "R3":["former_an","secondary"],
    "R4":["current_an","robust","lit"],
    "R5":["current_an","former_an","secondary"]
  }
}
```

### X.3 `web_config/methods_config.json`
```json
{
  "methods": [
    {"id":"spearman","badge":"Spearman's ρ","purpose":"Rank-based association","where":"H1–H7, current users","status":"verified_in_report","notes":"5,000-rep bootstrap 95% CI, seed 42. Computed as Pearson correlation of ranks; shortcut formula exact only without ties."},
    {"id":"holm","badge":"Holm–Bonferroni","purpose":"Family-wise error control","where":"H1–H7","status":"verified_in_report"},
    {"id":"ols","badge":"OLS regression (HC3)","purpose":"Exploratory explanatory model","where":"M1, n=51","status":"verified_in_report","notes":"Exploratory; 12.8 cases per predictor."},
    {"id":"alpha","badge":"Cronbach's α / McDonald's ω","purpose":"Scale reliability","where":"Multi-item constructs only","status":"verified_in_report","notes":"Not computable for single-item constructs."},
    {"id":"htmt","badge":"HTMT","purpose":"Discriminant-validity diagnostic","where":"table22","status":"verified_in_report","notes":"Confirm how single-item constructs were handled."},
    {"id":"centering","badge":"Within-person centering","purpose":"Response-style / common-pattern sensitivity","where":"table21","status":"verified_in_report","notes":"Show formula only after exact definition confirmed in src/."},
    {"id":"mwu","badge":"Mann–Whitney U","purpose":"Two-group nonparametric comparison","where":"H9, H10","status":"verified_in_report"},
    {"id":"wilson","badge":"Wilson interval","purpose":"Proportion uncertainty","where":"Former-user shares","status":"verified_in_report","notes":"Report value for 31/73 [32.0, 53.6] differs slightly from standard recomputation; display pipeline value."},
    {"id":"routing","badge":"Routing-leak isolation","purpose":"Prevent branch contamination","where":"Data cleaning","status":"verified_in_report"},
    {"id":"missing","badge":"Structural missingness","purpose":"Version-specific items, complete-case","where":"H7, HTMT (n=46)","status":"verified_in_report"},
    {"id":"straight","badge":"Straight-lining sensitivity","purpose":"Response-quality check","where":"Current-user models","status":"verified_in_report"},
    {"id":"pca","badge":"PCA / KMO / Bartlett / MSA","status":"verify_in_outputs","display":"if_verified"},
    {"id":"vif","badge":"VIF","status":"verify_in_outputs","display":"if_verified"},
    {"id":"fisher","badge":"Fisher's exact test","status":"verify_in_outputs","display":"if_verified"}
  ]
}
```

### X.4 `web_config/triangulation_display.json` (wording from report §11; short text, expand for full)
```json
{
  "states": {
    "CONVERGENT":{"icon":"✓","label":"Convergent"},
    "PARTIAL":{"icon":"◐","label":"Partial"},
    "CONTRADICTORY":{"icon":"✕","label":"Contradictory"},
    "INSUFFICIENT":{"icon":"?","label":"Insufficient"}
  },
  "factors": [
    {"id":"coverage","label":"Service coverage","integrated":"PARTIAL","integrated_note":"Convergent context, non-causal","crm":"R1"},
    {"id":"pull","label":"Competitor pull: alternative attractiveness & variety","integrated":"PARTIAL","crm":"R2"},
    {"id":"promo","label":"Competitor promotions / pricing","integrated":"PARTIAL","crm":"No indiscriminate discounting; availability first"},
    {"id":"effort","label":"Switching effort","integrated":"CONTRADICTORY","crm":"R4"},
    {"id":"satisfaction","label":"Satisfaction (push)","integrated":"INSUFFICIENT","integrated_note":"Contextual","crm":"R5"},
    {"id":"inertia","label":"Familiarity / inertia","integrated":"INSUFFICIENT","crm":"No loyalty lock-in without behavioural validation"}
  ],
  "cell_text_source": "outputs/tables/table18_triangulation.csv",
  "per_cell_states": false
}
```

### X.5 `web_config/crm_strategy_display.json`
```json
{
  "status_labels": {
    "R1":{"label":"Recommended (conditional, testable)","tone":"success"},
    "R2":{"label":"Conditional pilot (control group)","tone":"warning"},
    "R3":{"label":"Conditional, small evidence base (n=16)","tone":"warning"},
    "R4":{"label":"Not recommended on current evidence","tone":"danger","stop_card":true,
          "instead":"Re-measure switching barriers with a validated scale before designing retention interventions around them. Do not deploy artificial lock-in."},
    "R5":{"label":"Monitor only","tone":"neutral"}
  },
  "chain": ["Evidence","Customer problem","CRM action","Test design","KPI","Risk / limitation"],
  "field_map": {
    "Evidence":"Evidence","Customer problem":"Problem","CRM action":"Mechanism",
    "Test design":"Implementation (only if a test is stated; else 'To be designed')",
    "KPI":"KPI & Metrics","Risk / limitation":"Limitations"
  },
  "text_source": "outputs/tables/table19_crm_recommendations.csv",
  "rules": ["No outcome is stated as proven","R3 must show n=16 prominently","R4 never styled as an action"]
}
```

---

## Y. Risks / things that must NOT be changed
**Never:** change N, group sizes, ρ, CIs, p, R², HTMT, percentages, page refs, E/M/L IDs, verification tiers; imply causation; treat never-users as switchers; soften H5 to "switching costs don't matter"; style R4 as an action; invent per-cell triangulation states, literature fields, chart points, or methods; weaken `.gitignore`; add respondent-level data, credentials or UDRHP PDFs; reorder or bypass the pipeline's verification step; hand-edit generated CSVs.
**Recommendations (not applied automatically):**
- R-rec 1: Re-check the Wilson CI for 31/73 (D13).
- R-rec 2: If HTMT cut-off lines are shown, add the cut-off source to the reference list (it is not in the repository's literature register).
- R-rec 3: Reconcile the literature tier counts (D14).
- R-rec 4: Add raw p alongside Holm p in `table12a` if not present.
- R-rec 5: Add a short "Methods not used and why" note (e.g., no SEM/PLS-SEM at n=51).
**Technical risks:** `file://` breaking via modules/fetch (mitigated); CDN dependency (optional vendoring); renamed anchors breaking links (preserve IDs); chart accessibility.

## Z. Implementation order (with gates)
0. Branch `site-upgrade`, tag `site-v1-pre-upgrade`; run `python run_analysis.py` and confirm the existing verification passes.
1. Inventory: read `app.js`, `styles.css`, remaining `index.html`, CHECKPOINT_1–4, tables. Write `WEBSITE_UPGRADE_LOG.md`. **Gate 1: report D-register status (confirmed / resolved / needs user).**
2. Build `src/build_site_data.py` → `web/site_data.js`; build `src/verify_site.py`. Run on the *existing* page to produce a baseline mismatch list.
3. Tokens + typography + layout shell + nav/progress + hero. **Gate 2: screenshots desktop/tablet/mobile.**
4. Methodology flowchart + Methods Library.
5. PPM + current-user results (dot-and-whisker) + robustness (dumbbell, HTMT panel).
6. Former users, never-users.
7. UDRHP cards/timeline + media register; literature cards.
8. Triangulation matrix; CRM chains; final interpretation + claims ledger.
9. Fix D-items per your decisions; write `SITE_CORRECTION_LOG.md`.
10. QA: `verify_site.py`, link check, accessibility pass (keyboard, contrast, reduced motion), Lighthouse, responsive screenshots. Final audit report.

---

## ANTIGRAVITY IMPLEMENTATION PROMPT
Copy everything inside the fence.

~~~~
ROLE
You are implementing an approved upgrade of the research webpage in the public GitHub repo "zepto-crm-switching-research" (Zepto customer-switching study, Push–Pull–Mooring). The research is FINALIZED. The website is a presentation layer. Your job is to make it a premium, academically credible research dashboard WITHOUT changing any research value, interpretation or claim.

NON-NEGOTIABLE RULES
1. Do not change sample sizes, statistics, CIs, p-values, hypothesis decisions, percentages, page references, evidence IDs (E01–E25, M01–M11, L01–L17), verification tiers, or the PPM interpretation.
2. Never imply causation. Never claim availability, competitor attractiveness, promotions or anything else CAUSED switching. Never treat never-users (n=60) as switchers.
3. H5 / switching effort: raw ρ=+0.721 is opposite to the hypothesised sign; centered ρ≈+0.05; HTMT ≈0.92 (confirm the construct pair in table22). The site must say "Switching barriers remain inconclusive" and must NOT say switching costs are unimportant, and must NOT use words like "proves"/"proving"/"artifact" for it.
4. Do not invent: findings, sources, literature fields, chart data, per-cell triangulation states, statistical methods. If a field is missing show "Not recorded in repository".
5. Do not request, add or expose respondent-level data, credentials, or the excluded UDRHP PDFs. Do not weaken .gitignore. Do not modify data/raw. Do not hand-edit generated CSVs.
6. Do not weaken, reorder or bypass the independent verification and consistency steps in run_analysis.py.
7. Work on a branch. Do not push to main.

SOURCE-OF-TRUTH HIERARCHY
(1) outputs/tables/*.csv and outputs/statistical_results/*; (2) final_report.md; (3) documentation/CHECKPOINT_1..4; (4) existing index.html.
If (1) and (2) agree and the page differs → correct the page and log it in SITE_CORRECTION_LOG.md.
If (1) and (2) disagree → STOP and report to the user.
If a value exists only in the old page (no source in 1–3) → hide it, log it, do not delete it from the backup tag, ask the user.

STEP 0 — SAFETY & BASELINE
- git checkout -b site-upgrade; git tag site-v1-pre-upgrade (on current main HEAD).
- Create venv, pip install -r requirements.txt, run `python run_analysis.py`. It must pass its own verification. If it fails, stop and report.

STEP 1 — INSPECT (do not code yet)
Read fully: README.md, final_report.md, index.html, styles.css, app.js, src/, documentation/ (esp. CHECKPOINT_1_UDRHP_AUDIT.md, CHECKPOINT_2_SECONDARY_HARMONIZATION.md, CHECKPOINT_3_PIPELINE_AUDIT.md, CHECKPOINT_4_FINAL_INTEGRATION_AUDIT.md), literature/, secondary_data/, outputs/ (tables 01, 07, 08, 10, 12, 12a, 13, 13e, 16, 17, 18, 19, 21, 22, analysis_n_register.csv).
Also read the supplied plan file ADVANCED_WEBPAGE_UPGRADE_PLAN.md and its configs (design_tokens.css, research_flow.json, methods_config.json, triangulation_display.json, crm_strategy_display.json). Place them at: web/design_tokens.css and web_config/*.json.
Write WEBSITE_UPGRADE_LOG.md with: architecture found, every Chart.js chart and its data source, every hard-coded number in index.html/app.js, and the status of each discrepancy below.

KNOWN DISCREPANCIES TO RESOLVE (verify each against outputs; do not assume which side is right)
D01 page says versions V1 n=75/V2 n=109 and shows U=346.5,p=0.6014 as "version invariance"; report says V1 16 / V1.5 6 / V2 162 and U=346.5,p=0.6014 is H9 (shifted n=29 vs not n=22).
D02 page return-willingness table over n=73 with voluntary 10/32; report: return intention n=68; H10 Class A n=28 vs Class C n=30, U=496.0, p=0.2137; R3 cites 15/30.
D03 page UDRHP IDs/amounts differ from report E01–E25 register (e.g. tech ₹4,000.00M E09 pp.154–156; marketing ₹5,200.00M E10 pp.156–157; capex ₹16,289.75M E07 pp.143–145; leases ₹17,349.41M E08; SKUs E13; stores E14; ATU E11/E12; cohorts E20). Rebuild from table16.
D04 page demographics (age 72.8/20.7/4.3/2.2, occupation, geography) vs report (59.8/27.2/13.0; spend bands; n=168). Use table01 only.
D05 page 7-predictor regression and block ΔR² vs report M1 (SAT, PULL composite, SWEFFORT, FAM; R²=.696; F(4,46)=26.27; HC3). The page's SWEFFORT t=2.634 is inconsistent with its Mooring ΔR²=0.018. Use table12 only.
D06 page "Class A involuntary relocation / Class B non-serviceable lifestyle" vs report A coverage-primary 31/73 ("not available in my area"), B partial coverage overlap 10/73, C voluntary-only 32/73.
D07 "stock-outs" vs "Product Availability" (table13e option text decides).
D08 overclaiming wording ("proving", "artifact", "Partially Robust", "pull-driven rather than grievance-driven"); replace with report wording; show CIs (PROMO centered CI spans zero).
D09 label p-values "Holm-adjusted p"; verify H6/H7 rho in table12a; show per-row n (H7 n=46 if confirmed).
D11 "Draft Red Herring Prospectus May 2026" → Updated DRHP-I (UDRHP-I), filed with SEBI 8 June 2026, 690 printed pages.
D12 identify the exact construct pair behind each HTMT value (0.92, 0.94) in table22.
D13 Wilson CI for 31/73: report [32.0%,53.6%]; standard recomputation ≈[31.8%,53.9%]. Display pipeline value; flag only.
D14 literature tier counts inconsistent in report; build from literature CSV, preserve tiers.
D15 chart only retention points traceable to table16/secondary_data.
D16 label every denominator (73 / 68 / 58 / 32 / 51 / 46).
D18 raw "$n = 51$" LaTeX-style strings: replace with proper HTML/Unicode.
Report all of these in the log with status {confirmed, resolved, needs-user}. For needs-user, apply the safe default (hide) and list it for the user.

STEP 2 — DATA LAYER
- Create src/build_site_data.py: reads outputs/tables/*.csv + web_config/*.json, writes web/site_data.js as `window.SITE_DATA = {...};` (classic script, NO ES modules, NO fetch — the site must work by double-clicking index.html on file://).
- Create src/verify_site.py: extracts every number/percentage/ID in a locked-facts list from index.html, app.js and web/site_data.js and compares to the tables; exit non-zero on any mismatch. Include in the locked list at least: 184, 51, 73, 60, 27.7%, 39.7%, 32.6%, 31/73, 42.5%, 10/73, 32/73, 8/32, 16/32, 50.0%, 41/68, 60.3%, 18/68, 26.5%, ρ raw (+0.165, +0.685, +0.694, +0.700, +0.721, +0.248), centered (−0.03, +0.10, +0.23, +0.05), R²=0.696, F(4,46)=26.27, HTMT values, E-IDs/pages, ₹ amounts.
- Run verify_site.py on the OLD page first and save the baseline mismatch list.

STEP 3 — VISUAL SYSTEM
- Link web/design_tokens.css before styles.css. Use only the tokens; no hard-coded colours.
- Fonts: Inter (UI), Source Serif 4 (headings/pull-quotes), JetBrains Mono (statistics). Base ≥16px.
- Compute and log WCAG contrast for all text/background pairs (≥4.5:1 body, ≥3:1 large/graphics). Fix tokens if any fail.
- Cards: 1px border, radius 6–10px, soft shadow on hover. Motion 150–250ms; IntersectionObserver section reveals; everything disabled under prefers-reduced-motion.
- Evidence states are icon + text + pattern, never colour only.

STEP 4 — PAGE STRUCTURE (preserve existing element IDs/anchors; add new ones)
Hero → question → methodology flowchart (+ Methods Library) → primary survey & segmentation → PPM & measurement → current users H1–H7 → robustness & measurement diagnostics → former users → never-users (context) → UDRHP + media register → literature → triangulation → CRM → final interpretation (claims ledger: supported / cautious / not claimable; limitations) → sources & reproducibility.
Sticky nav grouped into phases (Design · Evidence · Diagnostics · Synthesis · Action) with progress rail. Mobile: collapsible drawer.
Hero: title, N=184 with 51/73/60 split bar, "Push • Pull • Mooring", one-sentence research statement, equation strip (Survey + Analytics + UDRHP + Literature + Triangulation = CRM strategy), non-causality chip.

STEP 5 — COMPONENTS
5a Methodology flowchart (web/flow.js, HTML+SVG, driven by web_config/research_flow.json): phase bands; nodes are <button>s; detail panel (what was done, n, methods, output file, source line, what it cannot show); tooltips; "trace evidence" for R1–R5 using the `trace` map; stage progress synced to scroll; mobile = vertical accordion stepper. Nodes marked display:"if_verified" render only if the method is found in documentation/ or outputs/ (PCA/KMO/Bartlett/MSA, VIF, Fisher). Not gimmicky.
5b Methods Library: badge cards from methods_config.json with status chips and expandable formula panels. Spearman: show 1−6Σd²/n(n²−1) AND state computed as Pearson correlation of ranks (tie-safe). Include α, HTMT (note single-item limitation), OLS, Wilson, Holm. Within-person centering: show a formula ONLY after confirming the exact definition in src/.
5c Interactive PPM SVG: Push | Pull | Mooring → switching intention (current n=51). Tiles show items, hypothesised sign, raw ρ, centered ρ (if in table21), Holm p, n, single-item badge. Toggle Hypothesised/Raw/Centered. H5 tile: "opposite to hypothesised sign" + "HTMT ≈0.92 — inconclusive". Dashed connectors labelled "hypothesised direction, not estimated causal paths". Separate panel for former-user exit classes.
5d Current-user results: custom SVG dot-and-whisker (ρ + 95% bootstrap CI, zero line, hypothesised-direction marker, fixed H1–H7 order, n per row). H1–H7 accordion cards: finding, ρ, CI, Holm p, n, interpretation, caution badge. Regression card from table12 labelled Exploratory (HC3). H8–H10 as extension tests.
5e Robustness section (visually prominent): four-step explainer (Raw → Centered → Weakens → Cautious interpretation); SVG dumbbell chart raw→centered ρ with centered CIs for ALT, VAR, PROMO, SWEFFORT; HTMT panel for the confirmed pair; callout "Switching barriers remain inconclusive" (H5 opposite sign + centered collapse + HTMT + mixed literature: L10 positive coefficient, L06 non-significant). Present as a methodological strength.
5f Former users: segmented bar n=73 (A coverage-primary 31 | B partial coverage overlap 10 | C voluntary-only 32) with COVERAGE/NON-SERVICEABILITY (hatched) vs VOLUNTARY COMPETITIVE EXIT (solid); voluntary reasons n=32 with bracket 8+8=16/32; destination item 41/68 and 18/68 with denominator "68 former users who evaluated alternatives"; return intention only after D02 is reconciled; caution badge "self-reported, retrospective".
5g Never-users: small contextual card, "not switchers", 37/60 unserved locality (verify in outputs).
5h UDRHP: evidence cards from table16 (E-ID, printed-page chip, filing section, classification, value, "contextualises → factor", "does not show: individual causality"); timeline small-multiples (SKUs, stores/cities, ATU); only traceable retention points; persistent banner "Company disclosure — contextual/secondary evidence; does not independently prove survey relationships". Keep M01–M11 filterable register with correct status legend.
5i Literature: filter chips by theme; cards (author, year, context, sample, method, finding, how it informs this study, tier badge). Missing → "Not recorded in repository". L07/L09 only in an "excluded (unverified)" disclosure.
5j Triangulation: 6 factors × (Primary | Former-user | UDRHP | Literature | Integrated). State chip ONLY on Integrated: Coverage = PARTIAL (convergent context, non-causal); Competitor pull & assortment = PARTIAL; Promotions/price = PARTIAL; Switching effort = CONTRADICTORY; Satisfaction = INSUFFICIENT/CONTEXTUAL; Familiarity/inertia = INSUFFICIENT. Cell text from table18. Filter by state. Never soften CONTRADICTORY.
5k CRM: chain Evidence → Customer problem → CRM action → Test design → KPI → Risk/limitation from table19; statuses per crm_strategy_display.json; R4 is a stop card ("re-measure switching barriers with a validated scale; no artificial lock-in"); R3 shows n=16 prominently; "Test design" only where the report states one, else "To be designed"; filter by status; evidence chips link to flowchart trace and E-IDs.
5l Final interpretation: answer "What does this study actually tell us about customer switching behaviour toward Zepto?" in 9 points: (1) switching is multidimensional; (2) current-user raw associations point to alternative attractiveness, variety, promotions; (3) robustness shows they are not stable enough for causal interpretation; (4) former-user evidence points strongly to coverage and, among voluntary exits, availability + variety; (5) UDRHP gives contextual company evidence; (6) literature supports theory but doesn't replace primary evidence; (7) triangulation supports a cautious CRM strategy; (8) priority is not "more discounts"; (9) coverage, assortment/stock-out recovery, reason-matched win-back, re-measure barriers, monitor service recovery. Plus a "What should NOT be claimed" panel.
Every chart/evidence block gets a source line (e.g. "Source: Primary survey, current users, n=51"), denominator, unit, descriptive/inferential tag, survey/secondary tag. No 3D charts, no dual axes, no pie charts where a bar is clearer.

STEP 6 — ACCESSIBILITY & MOBILE
Semantic landmarks, single h1, skip link, ARIA for tabs/accordions/filters (tablist, aria-expanded, aria-pressed, aria-live), visible focus ring, text alternative + "view data table" toggle for every chart, ≥44px touch targets, no hover-only information, reduced-motion support. Mobile: single column, nav drawer, flowchart → accordion stepper, tables → card lists or contained horizontal scroll, matrix → per-factor accordions.

STEP 7 — TECHNICAL CONSTRAINTS
No framework. Keep Chart.js 4.4.1 for bar/line charts (optionally vendor to web/vendor/ if the user approves). Custom SVG for dot-and-whisker, dumbbell, PPM, connectors. Classic scripts only; works on file://. Remove inline onclick/style attributes. Keep working charts, tables, report links and anchors. Add README section "Website" with build/verify commands.

STEP 8 — QA (all required)
- python run_analysis.py (must still pass); python src/build_site_data.py; python src/verify_site.py (must pass; compare with the old-page baseline).
- Link check for all internal anchors and report links; no console errors.
- Test desktop (1440), tablet (820), mobile (390) and screenshot each major section.
- Keyboard-only pass of nav, flowchart, accordions, filters; reduced-motion pass; contrast log; Lighthouse accessibility/performance.
- Confirm no research number changed: produce a table "locked fact | source table | value on site | match".
- Confirm .gitignore unchanged and no respondent-level files added.

STEP 9 — DELIVERABLES
WEBSITE_UPGRADE_LOG.md, SITE_CORRECTION_LOG.md (every correction: old text → new text → source table → reason), final implementation audit (what changed, what was hidden pending user, what was flagged as recommendation only, test results, screenshots). List every needs-user item at the top.

STOP CONDITIONS
Stop and ask the user if: outputs and final_report.md disagree; a required table is missing; a number on the site cannot be traced to a source; verify_site.py fails and the cause is not a clear page error.
~~~~
