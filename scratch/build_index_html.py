"""Generate the complete upgraded index.html for Zepto CRM Switching Research.
Ensures zero hard-coded statistics, persistent left sidebar, research stage progress tracker,
guided viva mode floating dock, accessible chart wrappers, stable section IDs, and old anchor redirects.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

cards_html = (ROOT / "scratch/cards_e01_e25.html").read_text(encoding="utf-8")
media_rows_html = (ROOT / "scratch/media_rows.html").read_text(encoding="utf-8")
lit_cards_html = (ROOT / "scratch/lit_cards.html").read_text(encoding="utf-8")
triangulation_html = (ROOT / "scratch/triangulation_table.html").read_text(encoding="utf-8")
crm_flow_html = (ROOT / "scratch/crm_flow.html").read_text(encoding="utf-8")
crm_cards_html = (ROOT / "scratch/crm_cards.html").read_text(encoding="utf-8")
claims_ledger_html = (ROOT / "scratch/claims_ledger.html").read_text(encoding="utf-8")
limitations_html = (ROOT / "scratch/limitations.html").read_text(encoding="utf-8")
demo_viz_html = (ROOT / "scratch/demographics_visualizations.html").read_text(encoding="utf-8")
udrhp_viz_html = (ROOT / "scratch/udrhp_visualizations.html").read_text(encoding="utf-8")
stat_viz_html = (ROOT / "scratch/statistical_visualizations.html").read_text(encoding="utf-8")

html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Customer Switching Behaviour in India's Quick-Commerce Industry — Zepto Case Study</title>
  <meta name="description" content="An empirical mixed-methods investigation into customer switching intentions, catalog-driven attrition, and evidence-based CRM strategy in Indian quick commerce using survey micro-data (N=184) and Zepto's UDRHP regulatory disclosures (E01–E25).">

  <!-- Typography: Inter, JetBrains Mono, Source Serif 4 -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400..700;1,8..60,400..700&display=swap" rel="stylesheet">

  <!-- Local Vendored Chart.js 4.4.1 (with CDN fallback for zero-network file:// compatibility) -->
  <script src="web/vendor/chart.umd.min.js"></script>
  <script>
    if (typeof Chart === 'undefined') {
      document.write('<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"><\\/script>');
    }
  </script>

  <!-- Modular Stylesheet Hierarchy -->
  <link rel="stylesheet" href="web/design_tokens.css">
  <link rel="stylesheet" href="web/css/theme.css">
  <link rel="stylesheet" href="web/css/layout.css">
  <link rel="stylesheet" href="web/css/components.css">
  <link rel="stylesheet" href="web/css/charts.css">
</head>
<body>

  <!-- Accessible Skip Link -->
  <a href="#overview" class="skip-link">Skip to main research content</a>

  <!-- Main Application Shell -->
  <div class="app-shell">

    <!-- Persistent Left Sidebar -->
    <aside class="app-sidebar" id="app-sidebar" aria-label="Research Navigation">
      <div class="sidebar-header">
        <div class="brand-badge">Academic Research Dashboard</div>
        <h1 class="brand-title">Zepto Switching Behaviour</h1>
        <p class="brand-subtitle">Empirical Mixed-Methods Investigation</p>
      </div>

      <!-- Research Stage Progress Tracker -->
      <div class="stage-tracker" aria-label="Research Stage Progress">
        <div class="stage-tracker-title">
          <span>Research Stage</span>
          <span id="stage-step-num">1/5</span>
        </div>
        <div class="stage-bar-rail" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="20">
          <div class="stage-bar-fill" id="stage-bar-fill" style="width: 20%;"></div>
        </div>
        <div class="stage-name" id="stage-name">Stage 1: Inception & Context</div>
      </div>

      <!-- Sidebar Navigation Links (10 Core Sections) -->
      <nav class="sidebar-nav" role="navigation" aria-label="Sections">
        <div class="nav-section-label">Pipeline Sections</div>
        <a href="#overview" class="nav-link active" aria-current="true">
          <span class="nav-num">01</span>
          <span class="nav-title">Executive Overview</span>
        </a>
        <a href="#design" class="nav-link">
          <span class="nav-num">02</span>
          <span class="nav-title">Research Design</span>
        </a>
        <a href="#survey" class="nav-link">
          <span class="nav-num">03</span>
          <span class="nav-title">Survey & Data Quality</span>
        </a>
        <a href="#ppm" class="nav-link">
          <span class="nav-num">04</span>
          <span class="nav-title">PPM Framework</span>
        </a>
        <a href="#hypothesis" class="nav-link">
          <span class="nav-num">05</span>
          <span class="nav-title">Hypothesis Lab</span>
        </a>
        <a href="#statistics" class="nav-link">
          <span class="nav-num">06</span>
          <span class="nav-title">Statistical Results</span>
        </a>
        <a href="#former" class="nav-link">
          <span class="nav-num">07</span>
          <span class="nav-title">Exit Analysis</span>
        </a>
        <a href="#udrhp" class="nav-link">
          <span class="nav-num">08</span>
          <span class="nav-title">UDRHP Evidence</span>
        </a>
        <a href="#triangulation" class="nav-link">
          <span class="nav-num">09</span>
          <span class="nav-title">Triangulation</span>
        </a>
        <a href="#recommendations" class="nav-link">
          <span class="nav-num">10</span>
          <span class="nav-title">CRM Recommendations</span>
        </a>
      </nav>

      <!-- Sidebar Footer Controls -->
      <div class="sidebar-footer">
        <button type="button" class="btn-viva-trigger" id="viva-trigger-btn" aria-label="Start Guided Viva Mode">
          <span>🎓</span> Guided Viva Mode
        </button>
        <a href="DISCREPANCIES.md" target="_blank" class="btn-discrepancy-link" title="Open Statistical Reconciliation Ledger">
          <span>📋</span> Reconciliation Ledger
        </a>
      </div>
    </aside>

    <!-- Main Content Area -->
    <div class="app-main">

      <!-- Sticky Top Control Rail -->
      <header class="top-rail" role="banner">
        <div class="scroll-progress-line" id="scroll-progress-line" aria-hidden="true"></div>
        <div class="top-bar-inner">
          <div class="top-left-status">
            <button type="button" class="mobile-menu-toggle" id="mobile-menu-btn" aria-label="Toggle navigation menu" aria-expanded="false">
              ☰ Menu
            </button>
            <a href="DISCREPANCIES.md" target="_blank" class="discrepancy-alert-chip" title="View Discrepancy Ledger">
              ⚠️ Report superseded where it differs from tables; see DISCREPANCIES.md
            </a>
          </div>
          <div class="top-right-controls">
            <button type="button" class="filter-btn" id="viva-trigger-top" aria-label="Launch viva walkthrough">
              🎓 Viva Walkthrough
            </button>
          </div>
        </div>

        <!-- Chart.js CDN Fallback Notice -->
        <div class="chart-fallback-banner" id="chart-fallback-banner" role="alert">
          <strong>Notice:</strong> Chart.js library is unavailable (offline mode). Interactive charts have fallen back to accessible data tables below each figure.
        </div>
      </header>

      <!-- Guided Viva Mode Floating Dock -->
      <aside class="viva-dock" id="viva-dock" role="region" aria-label="Guided Viva Walkthrough" aria-live="polite">
        <div class="viva-dock-header">
          <span class="viva-step-badge" id="viva-step-badge">Step 1 of 10</span>
          <button type="button" class="btn-viva-close" id="viva-close-btn" aria-label="Exit Viva Mode">✕ Exit</button>
        </div>
        <h4 class="viva-dock-title" id="viva-dock-title">1. Executive Overview</h4>
        <div class="viva-dock-body" id="viva-dock-body">Loading walkthrough content...</div>
        <div class="viva-dock-actions">
          <button type="button" class="btn-viva-nav" id="viva-prev-btn">← Previous</button>
          <div class="viva-btn-group">
            <button type="button" class="btn-viva-nav primary" id="viva-next-btn">Next Step →</button>
          </div>
        </div>
      </aside>

      <!-- Main Research Content Container -->
      <main class="content-container" role="main">

        <!-- ===================================================================
             01. EXECUTIVE OVERVIEW
             Old Anchor Aliases: #hero, #findings
             =================================================================== -->
        <section class="dashboard-section" id="overview">
          <span id="hero" class="anchor-target" aria-hidden="true"></span>
          <span id="findings" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 1 · Inception & Overview</span>
          </div>
          <h2 class="section-title">Customer Switching Behaviour in Indian Quick Commerce</h2>
          <p class="section-description">
            An empirical mixed-methods investigation into customer switching intentions, catalog-driven attrition, and evidence-based CRM strategy in Indian quick commerce. Survey micro-data (<i>N</i> = 184) is triangulated with Zepto's 690-page Updated Draft Red Herring Prospectus (UDRHP-I) regulatory disclosures (E01–E25) and academic Push–Pull–Mooring literature.
          </p>

          <!-- Crucial Epistemological Precaution Box -->
          <div class="callout-box warning" role="note">
            <div class="callout-header">
              <span>⚠️</span> Methodological Precaution & Epistemological Boundaries
            </div>
            <div class="callout-body">
              This research adheres strictly to disciplined, non-causal empirical standards. Cross-sectional survey correlations reflect statistical associations among self-reported perceptual measures and do not demonstrate causal mechanisms. Operational metrics from Zepto's regulatory disclosures (UDRHP-I) describe firm-level network capacity and financial constraints without establishing individual customer retention causality. Never-users (<i>n</i> = 60) are non-adopters and remain strictly segregated from former-user switching analyses.
            </div>
          </div>

          <!-- Primary Empirical Summary Stat Cards -->
          <div class="stat-grid">
            <div class="stat-card">
              <div class="stat-card-label">
                <span>Total Sample</span>
                <span class="badge badge-verified">Cleaned</span>
              </div>
              <div class="stat-card-value">N = 184</div>
              <div class="stat-card-sub">51 Current · 73 Former · 60 Never</div>
              <div class="stat-card-meta">Table 03 · Zero exclusions</div>
            </div>

            <div class="stat-card">
              <div class="stat-card-label">
                <span>Model M1 Fit</span>
                <span class="badge badge-verified">HC3 SE</span>
              </div>
              <div class="stat-card-value">R² = 0.7057</div>
              <div class="stat-card-sub">Adj R² = 0.6802 · F(4,46) = 27.58</div>
              <div class="stat-card-meta">Table 12c · SAT, PULL, SWEFFORT, FAM</div>
            </div>

            <div class="stat-card">
              <div class="stat-card-label">
                <span>PULL-Alone R²</span>
                <span class="badge badge-caution">Item Overlap</span>
              </div>
              <div class="stat-card-value">R² = 0.6356</div>
              <div class="stat-card-sub">SAT+SWEFFORT+FAM gain: +0.0701</div>
              <div class="stat-card-meta">Regression Overlap Diagnostics</div>
            </div>

            <div class="stat-card">
              <div class="stat-card-label">
                <span>Former Exit Driver</span>
                <span class="badge badge-verified">56.2% Logistic</span>
              </div>
              <div class="stat-card-value">41 / 73 Exits</div>
              <div class="stat-card-sub">Class A (31) + Class B (10) Coverage</div>
              <div class="stat-card-meta">Table 13d · Unserved pin codes</div>
            </div>
          </div>

          <!-- Discrepancy Reconciliation Summary Banner -->
          <div class="callout-box info">
            <div class="callout-header">
              <span>📋</span> Source Reconciliation Principle (Outputs Supersede Reports)
            </div>
            <div class="callout-body">
              Whenever text in historical report drafts or upgrade notes conflicted with deterministic output CSV tables, the tables strictly governed the displayed result. Authoritative canonical values: H1 &rho; = +0.170 (Holm <i>p</i> = 0.2492); H6 &rho; = +0.245; H7 &rho; = +0.253 (<i>n</i> = 46 complete-case); Model M1 <i>R</i>&sup2; = 0.7057; PULL-alone <i>R</i>&sup2; = 0.6356; H9 <i>p</i> = 0.6029; H10 <i>p</i> = 0.2141; Centered VAR &rho; = +0.305 (VAR1 only); Voluntary exits (availability 8, variety 8, delivery 4, app 3, discounts 3, pricing 2, preferred 2, quality 1, refund 1). See <a href="DISCREPANCIES.md" target="_blank" style="color: var(--accent-magenta); font-weight: 600;">DISCREPANCIES.md</a> for full provenance.
            </div>
          </div>
        </section>

        <!-- ===================================================================
             02. RESEARCH DESIGN & METHODOLOGY PIPELINE
             Old Anchor Aliases: #question, #method
             =================================================================== -->
        <section class="dashboard-section" id="design">
          <span id="question" class="anchor-target" aria-hidden="true"></span>
          <span id="method" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 1 · Methodology</span>
          </div>
          <h2 class="section-title">Research Design & Evidence Lineage Pipeline</h2>
          <p class="section-description">
            The study employs a disciplined 5-stage mixed-methods architecture connecting foundational PPM theory, primary consumer micro-data, measurement diagnostics, regulatory IPO disclosures, and synthesized CRM strategy.
          </p>

          <!-- Interactive Methodology Flowchart Canvas -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Methodology Lineage & Traceability Pipeline</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Unit: Multi-Stage Research Architecture</span>
                  <span class="chart-meta-tag">Denominator: N=184 respondents, 690-page UDRHP-I</span>
                  <span class="chart-meta-tag">Source: web_config/research_flow.json</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <span class="stat-card-meta" id="trace-status-msg">Click any stage node to inspect empirical inputs and lineage.</span>
              </div>
            </div>

            <!-- Trace Buttons for CRM Recommendations -->
            <div class="filter-bar" style="margin-top: 1rem; margin-bottom: 1rem;">
              <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">Trace Evidence Lineage:</span>
              <button type="button" class="trace-btn filter-btn" data-trace-r="R1">Trace R1 (Waitlist)</button>
              <button type="button" class="trace-btn filter-btn" data-trace-r="R2">Trace R2 (Restock Alerts)</button>
              <button type="button" class="trace-btn filter-btn" data-trace-r="R3">Trace R3 (Assortment Win-Back)</button>
              <button type="button" class="trace-btn filter-btn" data-trace-r="R4">Trace R4 (Lock-In Evaluated)</button>
              <button type="button" class="trace-btn filter-btn" data-trace-r="R5">Trace R5 (Service Recovery)</button>
              <button type="button" class="trace-btn filter-btn" data-trace-r="reset">Reset Highlights</button>
            </div>

            <!-- Flowchart Container (rendered by flow.js) -->
            <div id="flowchart-canvas" class="flowchart-container" style="min-height: 240px;"></div>
            <div id="flow-detail-content" class="flow-detail-drawer" style="margin-top: 1rem;"></div>
          </div>

          <!-- Data Cleaning & Quality Summary Table -->
          <div class="table-wrapper">
            <table class="data-table" aria-label="Data cleaning and sample quality summary">
              <thead>
                <tr>
                  <th>Audit Metric</th>
                  <th class="num-cell">Observed Value</th>
                  <th>Methodological Treatment & Integrity Rule</th>
                  <th>Impact on Analysis</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="cell-highlight">Raw Survey Submissions</td>
                  <td class="num-cell">184</td>
                  <td>Deterministic ingest from primary survey responses</td>
                  <td>Full sample base <i>N</i> = 184</td>
                </tr>
                <tr>
                  <td class="cell-highlight">Case Exclusions</td>
                  <td class="num-cell">0</td>
                  <td>Strict zero-exclusion policy to avoid researcher degree of freedom bias</td>
                  <td>Preserves all 184 collected records</td>
                </tr>
                <tr>
                  <td>Identified Straight-Liners</td>
                  <td class="num-cell">12</td>
                  <td>Retained in primary analysis; tested in sensitivity analysis (<i>n</i> = 39 current)</td>
                  <td>Correlations robust to exclusion (Table 12b)</td>
                </tr>
                <tr>
                  <td>Q1-Inconsistent Cases</td>
                  <td class="num-cell">40</td>
                  <td>Respondents citing contradictory multi-platform choices; tested in sensitivity</td>
                  <td>Substantive conclusions unaffected</td>
                </tr>
                <tr>
                  <td>Routing Branch Leaks</td>
                  <td class="num-cell">15</td>
                  <td>Google Forms branching flaws allowing cross-branch item completion (7 former, 15 never)</td>
                  <td>Quarantined; descriptive only, omitted from hypothesis tests</td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>

        <!-- ===================================================================
             03. SURVEY AND DATA QUALITY
             Anchor: #survey
             =================================================================== -->
        <section class="dashboard-section" id="survey">
          <div class="section-eyebrow">
            <span>Stage 2 · Sample & Quality</span>
          </div>
          <h2 class="section-title">Survey Partitioning & Measurement Quality</h2>
          <p class="section-description">
            Analysis of the primary sample (<i>N</i> = 184) across user lifecycle segments, questionnaire rollout iterations, demographic distributions, and platform multi-homing characteristics.
          </p>

          <div class="stat-grid" style="grid-template-columns: 1fr 1fr;">
            <!-- Lifecycle Composition Donut -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Lifecycle Partitioning</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Total: N = 184</span>
                    <span class="chart-meta-tag">Source: table03_user_groups.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-user-groups" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 240px;">
                <canvas id="userGroupChart" role="img" aria-label="Donut chart showing Current Users 51, Former Users 73, Never Users 60"></canvas>
              </div>

              <!-- Accessible Fallback Table -->
              <div class="chart-table-container" id="table-user-groups">
                <table class="data-table">
                  <thead>
                    <tr><th>Lifecycle Group</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th><th>Analytical Role</th></tr>
                  </thead>
                  <tbody>
                    <tr><td class="cell-highlight">Current Users</td><td class="num-cell">51</td><td class="num-cell">27.7%</td><td>Evaluated for switching intentions (H1–H7, M1)</td></tr>
                    <tr><td class="cell-highlight">Former Users</td><td class="num-cell">73</td><td class="num-cell">39.7%</td><td>Evaluated for realized exit reasons & return willingness</td></tr>
                    <tr><td class="cell-highlight">Never-Users</td><td class="num-cell">60</td><td class="num-cell">32.6%</td><td>Non-adopter contextual baseline (Coverage barrier)</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">Note: Never-users are non-adopters and are strictly excluded from switching-away analyses.</p>
            </div>

            <!-- Questionnaire Rollout Iterations -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Questionnaire Rollout Versions</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Total: N = 184</span>
                    <span class="chart-meta-tag">Source: table03b_questionnaire_versions.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-versions" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 240px;">
                <canvas id="versionChart" role="img" aria-label="Bar chart showing V1 16, V1.5 6, V2 162 respondents"></canvas>
              </div>

              <!-- Accessible Fallback Table -->
              <div class="chart-table-container" id="table-versions">
                <table class="data-table">
                  <thead>
                    <tr><th>Version</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th><th>Instrument Changes</th></tr>
                  </thead>
                  <tbody>
                    <tr><td>V1 (Pilot)</td><td class="num-cell">16</td><td class="num-cell">8.7%</td><td>Initial 5-point scale; lacked VAR2, INERT1, location, spend items</td></tr>
                    <tr><td>V1.5</td><td class="num-cell">6</td><td class="num-cell">3.3%</td><td>Added location and spend items</td></tr>
                    <tr><td>V2 (Final)</td><td class="num-cell">162</td><td class="num-cell">88.0%</td><td>Complete instrument including VAR2 and INERT1 items</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">Items added in V2 yield <i>n</i> = 46 complete cases among Current Users (5 V1 respondents lacked INERT1).</p>
            </div>
          </div>

          <!-- DEMOGRAPHICS_VISUALIZATIONS_PLACEHOLDER -->

          <!-- Platform Multi-Homing & Ordering Characteristics (Table 02 & Table 02b) -->
          <div class="stat-grid" style="grid-template-columns: 1fr 1fr; margin-top: 1.5rem;">
            <div class="table-wrapper">
              <table class="data-table" aria-label="Platforms used by respondents">
                <thead>
                  <tr>
                    <th>Quick-Commerce Platform</th>
                    <th class="num-cell">Users (n)</th>
                    <th class="num-cell">Adoption Share (%)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td class="cell-highlight">Blinkit</td><td class="num-cell">149</td><td class="num-cell">81.9%</td></tr>
                  <tr><td class="cell-highlight">Swiggy Instamart</td><td class="num-cell">119</td><td class="num-cell">65.4%</td></tr>
                  <tr><td class="cell-highlight">Zepto</td><td class="num-cell">91</td><td class="num-cell">50.0%</td></tr>
                  <tr><td class="cell-highlight">BigBasket Now</td><td class="num-cell">88</td><td class="num-cell">48.4%</td></tr>
                  <tr><td>Other Platforms</td><td class="num-cell">16</td><td class="num-cell">8.8%</td></tr>
                  <tr><td>None</td><td class="num-cell">1</td><td class="num-cell">0.5%</td></tr>
                </tbody>
              </table>
              <p class="chart-caption">Table 02b: Base <i>n</i> = 182 (2 missing Q1). Multi-select reveals intense multi-homing across rival platforms.</p>
            </div>

            <div class="table-wrapper">
              <table class="data-table" aria-label="Primary choice factors">
                <thead>
                  <tr>
                    <th>Most Important Choice Factor</th>
                    <th class="num-cell">Total (N=184)</th>
                    <th class="num-cell">Current</th>
                    <th class="num-cell">Former</th>
                    <th class="num-cell">Never</th>
                  </tr>
                </thead>
                <tbody>
                  <tr><td class="cell-highlight">Product availability</td><td class="num-cell">59</td><td class="num-cell">18</td><td class="num-cell">24</td><td class="num-cell">17</td></tr>
                  <tr><td class="cell-highlight">Discounts / promotions</td><td class="num-cell">33</td><td class="num-cell">10</td><td class="num-cell">12</td><td class="num-cell">11</td></tr>
                  <tr><td class="cell-highlight">Availability in locality</td><td class="num-cell">23</td><td class="num-cell">4</td><td class="num-cell">10</td><td class="num-cell">9</td></tr>
                  <tr><td>Delivery experience</td><td class="num-cell">19</td><td class="num-cell">7</td><td class="num-cell">6</td><td class="num-cell">6</td></tr>
                  <tr><td>Price</td><td class="num-cell">19</td><td class="num-cell">6</td><td class="num-cell">6</td><td class="num-cell">7</td></tr>
                  <tr><td>Product variety</td><td class="num-cell">10</td><td class="num-cell">2</td><td class="num-cell">5</td><td class="num-cell">3</td></tr>
                  <tr><td>App convenience</td><td class="num-cell">8</td><td class="num-cell">2</td><td class="num-cell">5</td><td class="num-cell">1</td></tr>
                </tbody>
              </table>
              <p class="chart-caption">Table 02: Product availability and promotions lead choice determinants across all lifecycle segments.</p>
            </div>
          </div>
        </section>

        <!-- ===================================================================
             04. PPM FRAMEWORK
             Anchor: #ppm
             =================================================================== -->
        <section class="dashboard-section" id="ppm">
          <div class="section-eyebrow">
            <span>Stage 3 · Construct Architecture</span>
          </div>
          <h2 class="section-title">Push–Pull–Mooring (PPM) Theoretical Framework</h2>
          <p class="section-description">
            Adapted from Bansal et al. (2005) and Chang et al. (2023) to quick commerce. Push factors drive abandonment; Pull factors attract customers to rivals; Mooring factors inhibit or govern transition velocity.
          </p>

          <!-- Interactive PPM Construct SVG Canvas -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Interactive PPM Construct Model</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Unit: Multi-Item Likert Constructs (1–5)</span>
                  <span class="chart-meta-tag">Current Users: n=51 (H1–H6), n=46 (H7)</span>
                  <span class="chart-meta-tag">Source: table06 & table08</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <div class="filter-bar" style="margin-bottom: 0;">
                  <button type="button" class="ppm-mode-btn filter-btn is-active" data-mode="raw">Raw Correlation</button>
                  <button type="button" class="ppm-mode-btn filter-btn" data-mode="centered">Centered &rho;</button>
                  <button type="button" class="ppm-mode-btn filter-btn" data-mode="hypothesised">Hypothesised Direction</button>
                </div>
              </div>
            </div>

            <!-- SVG Container (rendered by flow.js) -->
            <div id="ppm-interactive-diagram" class="ppm-diagram-container" style="min-height: 380px;"></div>
          </div>

          <!-- Measurement Items & Scale Reliability Diagnostics -->
          <div class="table-wrapper">
            <table class="data-table" aria-label="Measurement items and scale reliability">
              <thead>
                <tr>
                  <th>Construct</th>
                  <th>PPM Role</th>
                  <th>Survey Items</th>
                  <th class="num-cell">Items</th>
                  <th class="num-cell">Complete n</th>
                  <th class="num-cell">Cronbach &alpha;</th>
                  <th class="num-cell">Spearman-Brown</th>
                  <th>Reliability Assessment</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="cell-highlight">SAT</td>
                  <td><span class="badge badge-push">Push</span></td>
                  <td>SAT1 (Delivery & quality expectations), SAT2 (Overall satisfaction)</td>
                  <td class="num-cell">2</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">0.721</td>
                  <td class="num-cell">0.722</td>
                  <td><span class="badge badge-verified">Acceptable (&ge; 0.70)</span></td>
                </tr>
                <tr>
                  <td class="cell-highlight">ALT</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>ALT1 (Rival service attractiveness), ALT2 (Rival experience preference)</td>
                  <td class="num-cell">2</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">0.848</td>
                  <td class="num-cell">0.851</td>
                  <td><span class="badge badge-verified">Good (&ge; 0.80)</span></td>
                </tr>
                <tr>
                  <td class="cell-highlight">VAR</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>VAR1 (Rival catalog breadth), VAR2 (Rival niche item availability)</td>
                  <td class="num-cell">2</td>
                  <td class="num-cell">46</td>
                  <td class="num-cell">0.901</td>
                  <td class="num-cell">0.904</td>
                  <td><span class="badge badge-verified">Excellent (&ge; 0.90)</span></td>
                </tr>
                <tr>
                  <td class="cell-highlight">PROMO</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>PROMO1 (Rival discounts and promo pricing)</td>
                  <td class="num-cell">1</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">n/a</td>
                  <td class="num-cell">n/a</td>
                  <td>Single-item construct</td>
                </tr>
                <tr>
                  <td class="cell-highlight">SWEFFORT</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>SC1 (Time & effort to switch apps), SC2 (App setup friction)</td>
                  <td class="num-cell">2</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">0.792</td>
                  <td class="num-cell">0.795</td>
                  <td><span class="badge badge-verified">Acceptable (&ge; 0.70)</span></td>
                </tr>
                <tr>
                  <td class="cell-highlight">FAM</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>FAM1 (Familiarity with Zepto app interface & routine)</td>
                  <td class="num-cell">1</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">n/a</td>
                  <td class="num-cell">n/a</td>
                  <td>Single-item construct</td>
                </tr>
                <tr>
                  <td class="cell-highlight">INERT</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>INERT1 (Habitual continued use tendency)</td>
                  <td class="num-cell">1</td>
                  <td class="num-cell">46</td>
                  <td class="num-cell">n/a</td>
                  <td class="num-cell">n/a</td>
                  <td>Single-item construct (V2 only, <i>n</i> = 46)</td>
                </tr>
                <tr>
                  <td class="cell-highlight">INT</td>
                  <td><strong>Outcome</strong></td>
                  <td>INT1 (Explore rivals), INT2 (Shift purchases), INT3 (Active switching)</td>
                  <td class="num-cell">3</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">0.909</td>
                  <td class="num-cell">n/a</td>
                  <td><span class="badge badge-verified">Excellent (&ge; 0.90)</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <p class="chart-caption">Provenance rule: Scale reliability was computed via Cronbach's &alpha; and Spearman-Brown coefficients only; McDonald's &omega; is not present in canonical outputs.</p>
        </section>

        <!-- ===================================================================
             05. HYPOTHESIS LAB
             Old Anchor Alias: #current
             =================================================================== -->
        <section class="dashboard-section" id="hypothesis">
          <span id="current" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 3 · Empirical Testing</span>
          </div>
          <h2 class="section-title">Hypothesis Testing Laboratory (H1–H10)</h2>
          <p class="section-description">
            Complete register of formal hypothesis tests evaluated across primary survey respondents. Filterable by PPM dimension with expandable methodology drawers.
          </p>

          <!-- Filter Controls -->
          <div class="filter-bar">
            <span style="font-size: 0.8rem; color: var(--text-muted); font-weight: 600;">Filter by Dimension:</span>
            <button type="button" class="hypo-filter-btn filter-btn active" data-filter="all">All (H1–H10)</button>
            <button type="button" class="hypo-filter-btn filter-btn" data-filter="Push">Push (H1)</button>
            <button type="button" class="hypo-filter-btn filter-btn" data-filter="Pull">Pull (H2–H4)</button>
            <button type="button" class="hypo-filter-btn filter-btn" data-filter="Mooring">Mooring (H5–H7)</button>
            <button type="button" class="hypo-filter-btn filter-btn" data-filter="Outcome">Joint / Outcome (H8–H10)</button>
          </div>

          <!-- Comprehensive Hypothesis Register Table -->
          <div class="table-wrapper">
            <table class="data-table" aria-label="Hypothesis testing results">
              <thead>
                <tr>
                  <th>Hypothesis</th>
                  <th>Construct</th>
                  <th>PPM Dimension</th>
                  <th>Direction</th>
                  <th class="num-cell">Sample (n)</th>
                  <th class="num-cell">Coefficient / Result</th>
                  <th class="num-cell">95% Bootstrap CI</th>
                  <th class="num-cell">Holm p</th>
                  <th>Empirical Decision</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <!-- H1 -->
                <tr class="hypo-table-row" data-ppm="Push">
                  <td class="cell-highlight"><strong>H1</strong></td>
                  <td>SAT</td>
                  <td><span class="badge badge-push">Push</span></td>
                  <td>Negative (&minus;)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.170</td>
                  <td class="num-cell">[-0.12, +0.44]</td>
                  <td class="num-cell">0.2492</td>
                  <td><span class="badge badge-inconclusive">Inconclusive / Not Supported</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H1">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H1" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Satisfaction/expectation fulfilment is negatively associated with switching intention.</p>
                    <p><strong>Literature Precedent:</strong> Mixed evidence. L16 (B) noted significant push effects in online grocery, whereas L05 (A) found satisfaction &rarr; intention path (0.071) non-significant.</p>
                    <p><strong>Planned Test:</strong> Spearman &rho; with 5,000 bootstrap replicates; Holm multiple testing adjustment across H1–H7.</p>
                    <p><strong>Within-Person Centering Note:</strong> Centered &rho; = &minus;0.588 [CI &minus;0.77, &minus;0.32], indicating that relative dissatisfaction emerges only once common positivity bias is controlled.</p>
                  </div>
                </td></tr>

                <!-- H2 -->
                <tr class="hypo-table-row" data-ppm="Pull">
                  <td class="cell-highlight"><strong>H2</strong></td>
                  <td>ALT</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>Positive (+)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.685</td>
                  <td class="num-cell">[+0.49, +0.83]</td>
                  <td class="num-cell">&lt; 0.0001</td>
                  <td><span class="badge badge-verified">Supported (Raw Scores)</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H2">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H2" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Alternative attractiveness is positively associated with switching intention.</p>
                    <p><strong>Literature Precedent:</strong> Direct empirical support. L05 (A) path = 0.328; L10 (A) path = 0.314; L16 (B) significant.</p>
                    <p><strong>Robustness Warning:</strong> Centered &rho; collapses to &minus;0.026 [CI &minus;0.34, +0.31], demonstrating that raw association is driven by general elevation rather than relative platform preference.</p>
                  </div>
                </td></tr>

                <!-- H3 -->
                <tr class="hypo-table-row" data-ppm="Pull">
                  <td class="cell-highlight"><strong>H3</strong></td>
                  <td>VAR (VAR1+VAR2)</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>Positive (+)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.694</td>
                  <td class="num-cell">[+0.49, +0.85]</td>
                  <td class="num-cell">&lt; 0.0001</td>
                  <td><span class="badge badge-verified">Supported (Raw Scores)</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H3">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H3" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Perceived competitor product variety is positively associated with switching intention.</p>
                    <p><strong>Item Definition Rule:</strong> H3 evaluates the 2-item composite VAR1+VAR2 (&rho; = +0.694, <i>n</i> = 51 in table12a). Table 21 centering uses VAR1 only (&rho; = +0.731 raw &rarr; +0.305 centered) to preserve <i>n</i> = 51 across V1 respondents.</p>
                    <p><strong>Decision:</strong> Supported on raw scores; attenuated but positive under within-person centering (+0.305).</p>
                  </div>
                </td></tr>

                <!-- H4 -->
                <tr class="hypo-table-row" data-ppm="Pull">
                  <td class="cell-highlight"><strong>H4</strong></td>
                  <td>PROMO</td>
                  <td><span class="badge badge-pull">Pull</span></td>
                  <td>Positive (+)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.700</td>
                  <td class="num-cell">[+0.51, +0.84]</td>
                  <td class="num-cell">&lt; 0.0001</td>
                  <td><span class="badge badge-verified">Supported (Raw Scores)</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H4">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H4" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Competitor promotional attractiveness is positively associated with switching intention.</p>
                    <p><strong>Robustness:</strong> Centered &rho; = +0.233 [CI &minus;0.10, +0.55]. Evaluated on single-item PROMO1.</p>
                  </div>
                </td></tr>

                <!-- H5 -->
                <tr class="hypo-table-row" data-ppm="Mooring">
                  <td class="cell-highlight"><strong>H5</strong></td>
                  <td>SWEFFORT</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>Negative (&minus;)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.721</td>
                  <td class="num-cell">[+0.51, +0.87]</td>
                  <td class="num-cell">&lt; 0.0001</td>
                  <td><span class="badge badge-anomalous">Anomalous (Positive Sign)</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H5">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H5" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Switching effort was hypothesised to inhibit switching (&minus;), but yielded a strong positive correlation (+0.721).</p>
                    <p><strong>Epistemological Diagnosis:</strong> This anomalous finding reflects item framing: respondents who actively contemplate switching are acutely cognizant of the procedural effort required to adopt rival apps (verified precedent in L10: switching cost &rarr; intention +0.294).</p>
                    <p><strong>CRM Impact:</strong> Interventions predicated on switching barriers are unviable; Recommendation R4 is strictly NOT RECOMMENDED on current evidence.</p>
                  </div>
                </td></tr>

                <!-- H6 -->
                <tr class="hypo-table-row" data-ppm="Mooring">
                  <td class="cell-highlight"><strong>H6</strong></td>
                  <td>FAM</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>Negative (&minus;)</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">+0.245</td>
                  <td class="num-cell">[-0.09, +0.54]</td>
                  <td class="num-cell">0.2492</td>
                  <td><span class="badge badge-inconclusive">Inconclusive / Not Supported</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H6">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H6" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Familiarity with Zepto was hypothesised to inhibit switching.</p>
                    <p><strong>Result:</strong> Statistically non-significant (Holm <i>p</i> = 0.2492); bootstrap CI spans zero [-0.09, +0.54].</p>
                    <p><strong>Centering:</strong> Centered &rho; = &minus;0.406 [CI &minus;0.67, &minus;0.08].</p>
                  </div>
                </td></tr>

                <!-- H7 -->
                <tr class="hypo-table-row" data-ppm="Mooring">
                  <td class="cell-highlight"><strong>H7</strong></td>
                  <td>INERT</td>
                  <td><span class="badge badge-mooring">Mooring</span></td>
                  <td>Negative (&minus;)</td>
                  <td class="num-cell">46</td>
                  <td class="num-cell">+0.253</td>
                  <td class="num-cell">[-0.09, +0.57]</td>
                  <td class="num-cell">0.2492</td>
                  <td><span class="badge badge-inconclusive">Inconclusive / Not Supported</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H7">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H7" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Inertia (habitual use tendency) was hypothesised to inhibit switching.</p>
                    <p><strong>Complete-Case Sample:</strong> Evaluated on <i>n</i> = 46 complete cases (5 V1 respondents lacked INERT1).</p>
                    <p><strong>Result:</strong> Statistically non-significant after Holm adjustment (Holm <i>p</i> = 0.2492).</p>
                  </div>
                </td></tr>

                <!-- H8 -->
                <tr class="hypo-table-row" data-ppm="Outcome">
                  <td class="cell-highlight"><strong>H8</strong></td>
                  <td>Joint PPM (M1)</td>
                  <td><strong>Joint Model</strong></td>
                  <td>Joint F-test</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">R² = 0.7057</td>
                  <td class="num-cell">F(4,46) = 27.58</td>
                  <td class="num-cell">&lt; 0.0001</td>
                  <td><span class="badge badge-verified">Significant Model (Exploratory)</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H8">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H8" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Relationship:</strong> Push, Pull, and Mooring composites jointly explain variance in switching intention.</p>
                    <p><strong>Critical Overlap Caveat:</strong> Model M1 is overall significant, but variance decomposition demonstrates that PULL alone accounts for <i>R</i>&sup2; = 0.6356. Adding SAT, SWEFFORT, and FAM provides an incremental gain of only &Delta;<i>R</i>&sup2; = +0.0701.</p>
                  </div>
                </td></tr>

                <!-- H9 -->
                <tr class="hypo-table-row" data-ppm="Outcome">
                  <td class="cell-highlight"><strong>H9</strong></td>
                  <td>Partial Shift (Q19)</td>
                  <td><strong>Behavioral Link</strong></td>
                  <td>Shifted &gt; Not</td>
                  <td class="num-cell">51</td>
                  <td class="num-cell">U = 346.5</td>
                  <td class="num-cell">Medians: 3.67 vs 3.17</td>
                  <td class="num-cell">0.6029</td>
                  <td><span class="badge badge-inconclusive">Inconclusive / Not Supported</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H9">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H9" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Test:</strong> Mann–Whitney <i>U</i> comparing switching intention between users reporting shifted purchases (<i>n</i> = 29) vs those who have not (<i>n</i> = 22).</p>
                    <p><strong>Result:</strong> <i>U</i> = 346.5, <i>p</i> = 0.6029, rank-biserial <i>r</i> = 0.086. Medians: 3.67 vs 3.17. Stated intention does not reliably separate self-reported partial switchers.</p>
                  </div>
                </td></tr>

                <!-- H10 -->
                <tr class="hypo-table-row" data-ppm="Outcome">
                  <td class="cell-highlight"><strong>H10</strong></td>
                  <td>Return Willingness</td>
                  <td><strong>Retention Class</strong></td>
                  <td>Class A &gt; Class C</td>
                  <td class="num-cell">58</td>
                  <td class="num-cell">U = 496.0</td>
                  <td class="num-cell">Medians: 4.0 vs 3.5</td>
                  <td class="num-cell">0.2141</td>
                  <td><span class="badge badge-inconclusive">Inconclusive / Not Supported</span></td>
                  <td><button type="button" class="btn-hypo-drawer filter-btn" data-target="drawer-H10">View Details ▾</button></td>
                </tr>
                <tr id="drawer-H10" class="drawer-content"><td colspan="10">
                  <div style="padding: 0.5rem 0;">
                    <p><strong>Test:</strong> Mann–Whitney <i>U</i> comparing willingness to return between Coverage-primary (Class A, <i>n</i> = 28) and Voluntary-only (Class C, <i>n</i> = 30) former users.</p>
                    <p><strong>Result:</strong> <i>U</i> = 496.0, <i>p</i> = 0.2141, rank-biserial <i>r</i> = 0.181. Medians: 4.0 (Class A) vs 3.5 (Class C). Difference is directionally consistent but statistically non-significant.</p>
                    <p><strong>Sample Note:</strong> 5 V1 former users lacked the return item, leaving 58 valid former users in Class A and C.</p>
                  </div>
                </td></tr>
              </tbody>
            </table>
          </div>

          <!-- How Was This Calculated Accordion -->
          <button type="button" class="drawer-toggle-btn" data-drawer-target="hypo-method-accordion" aria-expanded="false" style="margin-top: 1rem;">
            <span>🔬 How Were These Statistics Calculated? (Methodology & Formulas)</span>
            <span class="arrow-icon">▼</span>
          </button>
          <div class="drawer-content" id="hypo-method-accordion">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; padding: 0.5rem 0;">
              <div>
                <h4 style="color: var(--text-primary); font-size: 0.9rem; margin-bottom: 4px;">Spearman Rank Correlation (&rho;)</h4>
                <p>Non-parametric monotonic association metric computed across ordinal Likert items. Robust against non-normal skewness. Bootstrapped with 5,000 resamples using a fixed deterministic seed to establish 95% confidence intervals.</p>
              </div>
              <div>
                <h4 style="color: var(--text-primary); font-size: 0.9rem; margin-bottom: 4px;">Holm-Bonferroni Step-Down</h4>
                <p>Controls Family-Wise Error Rate (FWER) across the family of 7 correlation tests (H1–H7). Sorts unadjusted <i>p</i>-values in ascending order and adjusts thresholds by <i>p</i> &times; (8 &minus; rank), preventing spurious alpha inflation.</p>
              </div>
              <div>
                <h4 style="color: var(--text-primary); font-size: 0.9rem; margin-bottom: 4px;">Mann–Whitney U Non-Parametric Test</h4>
                <p>Used for two-group medians comparison (H9: Shifted vs Not Shifted; H10: Class A vs Class C). Effect size quantified via rank-biserial correlation <i>r</i> = 1 &minus; (2U / n1n2).</p>
              </div>
            </div>
          </div>
        </section>

        <!-- ===================================================================
             06. STATISTICAL RESULTS & ROBUSTNESS
             Old Anchor Alias: #robustness
             =================================================================== -->
        <section class="dashboard-section" id="statistics">
          <span id="robustness" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 4 · Statistical Modeling</span>
          </div>
          <h2 class="section-title">Statistical Results & Robustness Diagnostics</h2>
          <p class="section-description">
            Rigorous statistical evaluations: 95% bootstrap confidence intervals for H1–H7, raw-vs-centered correlation dumbbell sensitivity, Model M1 multiple regression with HC3 standard errors, and HTMT discriminant validity.
          </p>

          <!-- 1. Correlation Dot-and-Whisker Plot -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Spearman Correlation Dot-and-Whisker Plot (H1–H7)</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Estimator: Spearman &rho; with 95% Bootstrap CI (5,000 reps)</span>
                  <span class="chart-meta-tag">Current Users: n=51 (H1–H6), n=46 (H7)</span>
                  <span class="chart-meta-tag">Source: table12a_hypothesis_results.csv</span>
                </div>
              </div>
            </div>
            <!-- SVG Container (rendered by flow.js) -->
            <div id="hypotheses-dot-whisker-svg" class="svg-chart-container" style="min-height: 360px;"></div>
            <p class="chart-caption">Green points indicate statistically supported hypotheses on raw scores (H2, H3, H4). Red point denotes H5 (anomalous positive sign). Grey points denote inconclusive tests with CIs spanning zero (H1, H6, H7).</p>
          </div>

          <!-- STATISTICAL_HEATMAP_PLACEHOLDER -->

          <!-- 2. Raw vs Within-Person Centered Dumbbell Plot (Interactive Toggle) -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Raw vs Within-Person Centered Dumbbell Sensitivity</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Sensitivity Diagnostic: Ipsatization / Within-Person Centering</span>
                  <span class="chart-meta-tag">Sample: n=51 (VAR evaluated on VAR1 only)</span>
                  <span class="chart-meta-tag">Source: table21_within_person_centering_sensitivity.csv</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <label class="toggle-control" for="dumbbell-mode-toggle">
                  <span style="font-size: 0.78rem; font-weight: 600;">Within-Person Centered View</span>
                  <div class="toggle-switch">
                    <input type="checkbox" id="dumbbell-mode-toggle">
                    <span class="toggle-slider"></span>
                  </div>
                </label>
              </div>
            </div>

            <!-- SVG Container (rendered by flow.js) -->
            <div id="centering-dumbbell-svg" class="svg-chart-container" style="min-height: 300px;"></div>

            <!-- Narrative Box dynamically updated by toggle -->
            <div class="callout-box info" id="dumbbell-interpretation-text" style="margin-top: 1rem;">
              <strong>Raw Bivariate Correlation Mode:</strong> Reflects unadjusted Spearman rank correlations across current users (n=51). Strong pull factors are observed: ALT (+0.685), VAR (+0.694 composite / +0.731 VAR1), PROMO (+0.700). Switching Effort (SWEFFORT) displays an anomalous positive association (+0.721), while Satisfaction (+0.170) is statistically non-significant (inconclusive).
            </div>
            <p class="chart-caption">Methodological note: Table 21 centering uses VAR1 only to preserve <i>n</i> = 51 across all respondents.</p>
          </div>

          <!-- 3. Model M1 Regression Coefficients & Overlap Diagnostics -->
          <div class="stat-grid" style="grid-template-columns: 1fr 1fr;">
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Model M1 Regression Coefficients</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">OLS with HC3 Standard Errors</span>
                    <span class="chart-meta-tag">Sample: n=51</span>
                    <span class="chart-meta-tag">Source: table12_regression_results.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-m1-reg" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 240px;">
                <canvas id="regressionCoeffChart" role="img" aria-label="Bar chart showing M1 regression coefficients"></canvas>
              </div>

              <!-- Accessible Table -->
              <div class="chart-table-container" id="table-m1-reg">
                <table class="data-table">
                  <thead>
                    <tr><th>Term</th><th class="num-cell">b (Coeff)</th><th class="num-cell">HC3 SE</th><th class="num-cell">p (HC3)</th><th>95% Boot CI</th></tr>
                  </thead>
                  <tbody>
                    <tr><td class="cell-highlight">PULL</td><td class="num-cell">+0.581</td><td class="num-cell">0.152</td><td class="num-cell">0.0001</td><td>[+0.292, +0.856]</td></tr>
                    <tr><td class="cell-highlight">SWEFFORT</td><td class="num-cell">+0.337</td><td class="num-cell">0.135</td><td class="num-cell">0.0126</td><td>[+0.087, +0.583]</td></tr>
                    <tr><td>FAM</td><td class="num-cell">&minus;0.097</td><td class="num-cell">0.113</td><td class="num-cell">0.3924</td><td>[&minus;0.321, +0.109]</td></tr>
                    <tr><td>SAT</td><td class="num-cell">&minus;0.084</td><td class="num-cell">0.100</td><td class="num-cell">0.4051</td><td>[&minus;0.263, +0.136]</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">Full Model: <i>R</i>&sup2; = 0.7057, Adj <i>R</i>&sup2; = 0.6802, <i>F</i>(4,46) = 27.58, <i>p</i> &lt; 0.0001.</p>
            </div>

            <!-- Discriminant Validity & Overlap Box -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Variance Decomposition & Overlap</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Construct Overlap Diagnostic</span>
                    <span class="chart-meta-tag">Source: regression_overlap_diagnostics.csv</span>
                  </div>
                </div>
              </div>
              <div style="padding: 0.5rem 0;">
                <div class="stat-card" style="margin-bottom: 0.75rem; background: var(--bg-surface-elevated);">
                  <div class="stat-card-label">PULL Composite Alone</div>
                  <div class="stat-card-value">R² = 0.6356</div>
                  <div class="stat-card-sub">Spearman correlation with INT: &rho; = 0.768</div>
                </div>
                <div class="stat-card" style="margin-bottom: 0.75rem; background: var(--bg-surface-elevated);">
                  <div class="stat-card-label">Incremental Gain from SAT + SWEFFORT + FAM</div>
                  <div class="stat-card-value">&Delta;R² = +0.0701</div>
                  <div class="stat-card-sub">Explains only 7.0% additional variance beyond PULL</div>
                </div>
                <p class="chart-caption">HTMT Discriminant Validity: The HTMT ratio between SWEFFORT/PULL and Switching Intention reaches <strong>0.92</strong>, indicating severe conceptual overlap between perceived attractiveness and switching intent.</p>
              </div>
            </div>
          </div>

          <!-- Complete HTMT Discriminant Validity Matrix (Table 22) -->
          <div class="table-wrapper" style="margin-top: 1rem;">
            <table class="data-table" aria-label="HTMT discriminant validity ratios">
              <thead>
                <tr>
                  <th>Construct Pair</th>
                  <th class="num-cell">Complete n</th>
                  <th class="num-cell">HTMT Ratio</th>
                  <th class="num-cell">95% Bootstrap CI</th>
                  <th>Discriminant Validity Verdict</th>
                </tr>
              </thead>
              <tbody>
                <tr><td class="cell-highlight">ALT &minus; VAR</td><td class="num-cell">46</td><td class="num-cell">0.943</td><td class="num-cell">[0.808, 1.041]</td><td><span class="badge badge-anomalous">Not Established (&ge; 0.85)</span></td></tr>
                <tr><td class="cell-highlight">SWEFFORT &minus; INT</td><td class="num-cell">46</td><td class="num-cell">0.923</td><td class="num-cell">[0.739, 1.157]</td><td><span class="badge badge-anomalous">Not Established (&ge; 0.85)</span></td></tr>
                <tr><td class="cell-highlight">VAR &minus; INT</td><td class="num-cell">46</td><td class="num-cell">0.896</td><td class="num-cell">[0.724, 1.021]</td><td><span class="badge badge-anomalous">Not Established (&ge; 0.85)</span></td></tr>
                <tr><td class="cell-highlight">ALT &minus; INT</td><td class="num-cell">46</td><td class="num-cell">0.874</td><td class="num-cell">[0.723, 0.989]</td><td><span class="badge badge-anomalous">Not Established (&ge; 0.85)</span></td></tr>
                <tr><td>VAR &minus; SWEFFORT</td><td class="num-cell">46</td><td class="num-cell">0.792</td><td class="num-cell">[0.580, 0.946]</td><td><span class="badge badge-verified">Acceptable (&lt; 0.80)</span></td></tr>
                <tr><td>ALT &minus; SWEFFORT</td><td class="num-cell">46</td><td class="num-cell">0.767</td><td class="num-cell">[0.521, 0.982]</td><td><span class="badge badge-verified">Acceptable (&lt; 0.80)</span></td></tr>
                <tr><td>SAT &minus; ALT</td><td class="num-cell">46</td><td class="num-cell">0.391</td><td class="num-cell">[0.163, 0.710]</td><td><span class="badge badge-verified">Well Established (&lt; 0.80)</span></td></tr>
                <tr><td>SAT &minus; SWEFFORT</td><td class="num-cell">46</td><td class="num-cell">0.379</td><td class="num-cell">[0.122, 0.756]</td><td><span class="badge badge-verified">Well Established (&lt; 0.80)</span></td></tr>
                <tr><td>SAT &minus; INT</td><td class="num-cell">46</td><td class="num-cell">0.242</td><td class="num-cell">[0.070, 0.573]</td><td><span class="badge badge-verified">Well Established (&lt; 0.80)</span></td></tr>
                <tr><td>SAT &minus; VAR</td><td class="num-cell">46</td><td class="num-cell">0.231</td><td class="num-cell">[0.053, 0.615]</td><td><span class="badge badge-verified">Well Established (&lt; 0.80)</span></td></tr>
              </tbody>
            </table>
            <p class="chart-caption">Table 22: Strict HTMT0.85 conservative criterion (Henseler et al., 2015). High HTMT values (&ge; 0.85) between pull constructs and intention indicate substantial conceptual collinearity.</p>
          </div>
        </section>

        <!-- ===================================================================
             07. FORMER-USER EXIT ANALYSIS & NEVER-USERS
             Old Anchor Alias: #never
             =================================================================== -->
        <section class="dashboard-section" id="former">
          <span id="never" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 4 · Customer Attrition</span>
          </div>
          <h2 class="section-title">Former-User Exit Dynamics & Non-Adopter Baseline</h2>
          <p class="section-description">
            Analysis of 73 former users partitioned into 3 behavioral classes, itemized breakdown of 32 voluntary exits, and strict segregation of never-user non-adopters.
          </p>

          <div class="stat-grid" style="grid-template-columns: 1fr 1fr;">
            <!-- 3-Class Exit Breakdown -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Former User 3-Class Exit Partitioning</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Former Users: n = 73</span>
                    <span class="chart-meta-tag">Source: table13d_former_coverage_vs_voluntary.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-former-classes" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 240px;">
                <canvas id="formerClassChart" role="img" aria-label="Donut chart of former user classes: A 31, B 10, C 32"></canvas>
              </div>

              <!-- Accessible Table -->
              <div class="chart-table-container" id="table-former-classes">
                <table class="data-table">
                  <thead>
                    <tr><th>Exit Class</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th><th>95% Wilson CI</th><th>Primary Nature</th></tr>
                  </thead>
                  <tbody>
                    <tr><td class="cell-highlight">Class A: Coverage-Primary</td><td class="num-cell">31</td><td class="num-cell">42.5%</td><td>[31.8%, 53.9%]</td><td>Involuntary (Unserved pin code / dark store relocation)</td></tr>
                    <tr><td class="cell-highlight">Class B: Coverage-Mentioned</td><td class="num-cell">10</td><td class="num-cell">13.7%</td><td>[7.6%, 23.4%]</td><td>Involuntary Overlap (Area cited with secondary reasons)</td></tr>
                    <tr><td class="cell-highlight">Class C: Voluntary-Only</td><td class="num-cell">32</td><td class="num-cell">43.8%</td><td>[33.0%, 55.2%]</td><td>Voluntary Platform Choice (Product, service, app)</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">56.2% of former users (Class A + B, 41/73) cited dark-store unserviceability, demonstrating that attrition is largely infrastructural rather than dissatisfaction-driven.</p>
            </div>

            <!-- Voluntary Exit Reasons (n=32) -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Voluntary Exit Main Reasons (n=32)</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Class C Only: n = 32</span>
                    <span class="chart-meta-tag">Source: table13e_voluntary_only_main_reason.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-voluntary-reasons" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 240px;">
                <canvas id="voluntaryReasonsChart" role="img" aria-label="Horizontal bar chart showing voluntary exit reasons"></canvas>
              </div>

              <!-- Accessible Table -->
              <div class="chart-table-container" id="table-voluntary-reasons">
                <table class="data-table">
                  <thead>
                    <tr><th>Reason Category</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th><th>95% Wilson CI</th></tr>
                  </thead>
                  <tbody>
                    <tr><td class="cell-highlight">Product availability</td><td class="num-cell">8</td><td class="num-cell">25.0%</td><td>[13.3%, 42.1%]</td></tr>
                    <tr><td class="cell-highlight">Product variety / choice</td><td class="num-cell">8</td><td class="num-cell">25.0%</td><td>[13.3%, 42.1%]</td></tr>
                    <tr><td>Delivery experience</td><td class="num-cell">4</td><td class="num-cell">12.5%</td><td>[5.0%, 28.1%]</td></tr>
                    <tr><td>App experience</td><td class="num-cell">3</td><td class="num-cell">9.4%</td><td>[3.2%, 24.2%]</td></tr>
                    <tr><td>Discounts / promotions</td><td class="num-cell">3</td><td class="num-cell">9.4%</td><td>[3.2%, 24.2%]</td></tr>
                    <tr><td>Pricing</td><td class="num-cell">2</td><td class="num-cell">6.3%</td><td>[1.7%, 20.1%]</td></tr>
                    <tr><td>Preferred another platform</td><td class="num-cell">2</td><td class="num-cell">6.3%</td><td>[1.7%, 20.1%]</td></tr>
                    <tr><td>Product quality</td><td class="num-cell">1</td><td class="num-cell">3.1%</td><td>[0.6%, 15.7%]</td></tr>
                    <tr><td>Return / refund experience</td><td class="num-cell">1</td><td class="num-cell">3.1%</td><td>[0.6%, 15.7%]</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">Product Availability and Variety combined account for exactly 50.0% (16/32) of voluntary customer departures.</p>
            </div>
          </div>

          <!-- Secondary Behavioral Plots: Assortment Advantage & Return Willingness -->
          <div class="stat-grid" style="grid-template-columns: 1fr 1fr;">
            <!-- Competitor Variety Advantage -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Competitor Variety Advantage</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Evaluating Former Users: n = 68</span>
                    <span class="chart-meta-tag">Source: table13c_former_alt_variants.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-alt-variants" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 200px;">
                <canvas id="formerAltVariantChart" role="img" aria-label="Bar chart of competitor variety advantage"></canvas>
              </div>
              <div class="chart-table-container" id="table-alt-variants">
                <table class="data-table">
                  <thead><tr><th>Response</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th></tr></thead>
                  <tbody>
                    <tr><td>Yes (Competitor had better variety)</td><td class="num-cell">41</td><td class="num-cell">60.3%</td></tr>
                    <tr><td>Maybe / Not Sure</td><td class="num-cell">18</td><td class="num-cell">26.5%</td></tr>
                    <tr><td>No (Similar variety)</td><td class="num-cell">9</td><td class="num-cell">13.2%</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">60.3% (41/68) of evaluating former users confirmed that competing platforms carried products they could not readily find on Zepto.</p>
            </div>

            <!-- Return Willingness Distribution -->
            <div class="chart-card">
              <div class="chart-header">
                <div class="chart-header-main">
                  <h3 class="chart-title">Return Willingness Distribution</h3>
                  <div class="chart-meta-row">
                    <span class="chart-meta-tag">Former Users: n = 68 (5 missing in V1)</span>
                    <span class="chart-meta-tag">Source: table13c_former_return.csv</span>
                  </div>
                </div>
                <div class="chart-controls-row">
                  <button type="button" class="btn-chart-toggle" data-table-target="table-return-dist" aria-expanded="false">
                    Show Table
                  </button>
                </div>
              </div>
              <div class="chart-canvas-wrapper" style="height: 200px;">
                <canvas id="formerReturnChart" role="img" aria-label="Bar chart of return willingness distribution"></canvas>
              </div>
              <div class="chart-table-container" id="table-return-dist">
                <table class="data-table">
                  <thead><tr><th>Rating Category</th><th class="num-cell">n</th><th class="num-cell">Share (%)</th></tr></thead>
                  <tbody>
                    <tr><td>Definitely Yes</td><td class="num-cell">14</td><td class="num-cell">20.6%</td></tr>
                    <tr><td>Probably Yes</td><td class="num-cell">27</td><td class="num-cell">39.7%</td></tr>
                    <tr><td>Not Sure</td><td class="num-cell">20</td><td class="num-cell">29.4%</td></tr>
                    <tr><td>Probably No</td><td class="num-cell">5</td><td class="num-cell">7.4%</td></tr>
                    <tr><td>Definitely No</td><td class="num-cell">2</td><td class="num-cell">2.9%</td></tr>
                  </tbody>
                </table>
              </div>
              <p class="chart-caption">60.3% (41/68) express positive willingness to return (Definitely or Probably Yes), confirming strong latent reactivation potential.</p>
            </div>
          </div>

          <!-- Segregated Never-Users Panel -->
          <div class="callout-box" id="never-users-panel" style="border-left-color: var(--accent-cyan); background: rgba(6, 182, 212, 0.04);">
            <div class="callout-header">
              <span>📍</span> Never-Users Non-Adopter Segment (n = 60 Baseline)
            </div>
            <div class="callout-body">
              <p>Never-users represent non-adopters rather than switched customers. Primary barrier to adoption is dark-store serviceability: <strong>37 out of 60 (61.7%)</strong> never-users cited lack of delivery coverage in their residential pin codes as their primary reason for never ordering (Table 16b). When asked what would encourage adoption, <strong>34 out of 54 (63.0%)</strong> cited serviceability expansion into their locality (Table 16f).</p>
            </div>
          </div>
        </section>

        <!-- ===================================================================
             08. ZEPTO UDRHP-I EVIDENCE EXPLORER
             Old Anchor Alias: #literature
             =================================================================== -->
        <section class="dashboard-section" id="udrhp">
          <span id="literature" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 5 · Secondary Disclosures</span>
          </div>
          <h2 class="section-title">Zepto UDRHP-I Regulatory Evidence Explorer (E01–E25)</h2>
          <p class="section-description">
            Extraction and analysis of official disclosures from Zepto Limited's 690-page Updated Draft Red Herring Prospectus (UDRHP-I, June 2026), tracked media claims (M01–M11), and academic literature verification tiers (L01–L17).
          </p>

          <!-- UDRHP_VISUALIZATIONS_PLACEHOLDER -->

          <!-- Searchable Evidence Explorer (E01–E25) -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Regulatory Disclosures Explorer (25 Verified Items)</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Source: Zepto Limited UDRHP-I (SEBI Filing)</span>
                  <span class="chart-meta-tag">Catalog: table16_zepto_secondary_evidence.csv</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <input type="text" id="evidence-search-input" class="filter-search-input" placeholder="Search claims, metrics, pages...">
                <select id="evidence-construct-select" class="filter-search-input" style="width: 170px;">
                  <option value="all">All Constructs</option>
                  <option value="Coverage">Coverage & Dark Stores</option>
                  <option value="assortment">Assortment & SKUs</option>
                  <option value="promotions">Promotions & Fees</option>
                  <option value="retention">Retention & Cohorts</option>
                  <option value="CRM">Technology & CRM</option>
                  <option value="operational">Financial & Logistics</option>
                </select>
              </div>
            </div>

            <!-- Evidence Cards Container -->
            <div class="card-grid" id="udrhp-cards-container">
<!-- UDRHP_CARDS_PLACEHOLDER -->
            </div>
          </div>

          <!-- Media Claims Register<!-- Media Claims Register (M01–M11) -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Media Claims Verification Register (M01–M11)</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Tracked Claims: 11 Items</span>
                  <span class="chart-meta-tag">Rule: Media claims are non-evidence; checked against UDRHP</span>
                  <span class="chart-meta-tag">Source: secondary_data/media_claims_register.csv</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <div class="filter-bar" id="media-filter-bar" style="margin-bottom: 0;">
                  <button type="button" class="filter-btn active" data-filter="all">All</button>
                  <button type="button" class="filter-btn" data-filter="VERIFIED">Verified</button>
                  <button type="button" class="filter-btn" data-filter="DISPROVED">Disproved</button>
                  <button type="button" class="filter-btn" data-filter="NOT VERIFIED">Not Verified</button>
                </div>
              </div>
            </div>

            <div class="table-wrapper">
              <table class="data-table" id="media-claims-table" aria-label="Media claims verification register">
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Media Source</th>
                    <th>Reported Claim</th>
                    <th>UDRHP Verification Finding</th>
                    <th>Status</th>
                  </tr>
                </thead>
                <tbody>
<!-- MEDIA_ROWS_PLACEHOLDER -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- Academic Literature Verification Tiers (L01–L17) -->
          <div class="chart-card">
            <div class="chart-header">
              <div class="chart-header-main">
                <h3 class="chart-title">Academic Literature Verification Register (L01–L17)</h3>
                <div class="chart-meta-row">
                  <span class="chart-meta-tag">Tracked Sources: 17 Records</span>
                  <span class="chart-meta-tag">Tier A: Full Text (2) · Tier B: Abstract (8) · Tier C: Background (5) · Unverified (2)</span>
                  <span class="chart-meta-tag">Source: literature/references.csv</span>
                </div>
              </div>
              <div class="chart-controls-row">
                <div class="filter-bar" id="lit-filter-bar" style="margin-bottom: 0;">
                  <button type="button" class="filter-btn active" data-filter="all">All</button>
                  <button type="button" class="filter-btn" data-filter="A">Tier A (Full Text)</button>
                  <button type="button" class="filter-btn" data-filter="B">Tier B (Abstract)</button>
                  <button type="button" class="filter-btn" data-filter="C">Tier C (Background)</button>
                  <button type="button" class="filter-btn" data-filter="UNVERIFIED">Unverified (Withdrawn)</button>
                </div>
              </div>
            </div>

            <div class="card-grid" id="literature-cards-container">
<!-- LIT_CARDS_PLACEHOLDER -->
            </div>
          </div>
        </section>

        <!-- ===================================================================
             09. EVIDENCE TRIANGULATION
             Anchor: #triangulation
             =================================================================== -->
        <section class="dashboard-section" id="triangulation">
          <div class="section-eyebrow">
            <span>Stage 5 · Synthesis</span>
          </div>
          <h2 class="section-title">Multi-Source Evidence Triangulation</h2>
          <p class="section-description">
            Synthesis matrix reconciling primary consumer survey findings, secondary UDRHP-I regulatory disclosures, and academic literature across 6 operational dimensions.
          </p>

<!-- TRIANGULATION_TABLE_PLACEHOLDER -->

<!-- CRM_FLOW_PLACEHOLDER -->
        </section>

        <!-- ===================================================================
             10. CRM RECOMMENDATIONS & BOUNDARIES
             Old Anchor Aliases: #crm, #sources, #findings
             =================================================================== -->
        <section class="dashboard-section" id="recommendations">
          <span id="crm" class="anchor-target" aria-hidden="true"></span>
          <span id="sources" class="anchor-target" aria-hidden="true"></span>
          <span id="findings" class="anchor-target" aria-hidden="true"></span>

          <div class="section-eyebrow">
            <span>Stage 5 · Actionable Strategy</span>
          </div>
          <h2 class="section-title">Evidence-Based CRM Recommendations (R1–R5)</h2>
          <p class="section-description">
            Pragmatic CRM strategic recommendations derived strictly from converged primary survey and regulatory evidence. Evaluated with statistical confidence tiers.
          </p>

<!-- CRM_CARDS_PLACEHOLDER -->

<!-- CLAIMS_LEDGER_PLACEHOLDER -->

<!-- LIMITATIONS_PLACEHOLDER -->

          <!-- Academic Source Register --><!-- Academic Source Register -->
          <div class="callout-box" style="margin-top: 2rem;">
            <div class="callout-header">
              <span>📚</span> Authoritative Sources & Regulatory Documents
            </div>
            <div class="callout-body">
              <p>Primary data: Deterministic survey output tables in <code>outputs/tables/</code> (Tables 01–22) and statistical registers in <code>outputs/statistical_results/</code>. Secondary corporate disclosures: Zepto Limited Updated Draft Red Herring Prospectus (UDRHP-I, 690 pages, filed with SEBI, June 2026). Academic PPM framework: Bansal et al. (2005, <i>JAMS</i>), Moon (1995), Chang et al. (2023, <i>JTAER</i>), and Monoarfa et al. (2023, <i>Sustainability</i>).</p>
            </div>
          </div>
        </section>

      </main>
    </div>
  </div>

  <!-- Application Script Pipeline (Classic Scripts, file:// compatible) -->
  <script src="web/site_data.js"></script>
  <script src="web/js/app_state.js"></script>
  <script src="web/js/sidebar.js"></script>
  <script src="web/js/chart_manager.js"></script>
  <script src="web/js/components.js"></script>
  <script src="web/js/viva_mode.js"></script>
  <script src="web/flow.js"></script>
  <script src="app.js"></script>
</body>
</html>
'''

html_content = html_content.replace('<!-- UDRHP_CARDS_PLACEHOLDER -->', cards_html)
html_content = html_content.replace('<!-- MEDIA_ROWS_PLACEHOLDER -->', media_rows_html)
html_content = html_content.replace('<!-- LIT_CARDS_PLACEHOLDER -->', lit_cards_html)
html_content = html_content.replace('<!-- TRIANGULATION_TABLE_PLACEHOLDER -->', triangulation_html)
html_content = html_content.replace('<!-- CRM_FLOW_PLACEHOLDER -->', crm_flow_html)
html_content = html_content.replace('<!-- CRM_CARDS_PLACEHOLDER -->', crm_cards_html)
html_content = html_content.replace('<!-- CLAIMS_LEDGER_PLACEHOLDER -->', claims_ledger_html)
html_content = html_content.replace('<!-- LIMITATIONS_PLACEHOLDER -->', limitations_html)
html_content = html_content.replace('<!-- DEMOGRAPHICS_VISUALIZATIONS_PLACEHOLDER -->', demo_viz_html)
html_content = html_content.replace('<!-- UDRHP_VISUALIZATIONS_PLACEHOLDER -->', udrhp_viz_html)
html_content = html_content.replace('<!-- STATISTICAL_HEATMAP_PLACEHOLDER -->', stat_viz_html)

(ROOT / "index.html").write_text(html_content, encoding="utf-8")
print(f"[SUCCESS] Upgraded index.html generated successfully ({len(html_content):,} bytes).")
