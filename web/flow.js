/**
 * web/flow.js — Interactive Visualizations for Research Dashboard
 * Includes:
 * 1. Interactive Methodology Flowchart with Phase Bands & Evidence Trace
 * 2. Interactive PPM Framework Diagram with Metric State Toggles
 * 3. Custom SVG Dot-and-Whisker Plot for H1–H7 with Bootstrap CIs
 * 4. Custom SVG Dumbbell Plot for Robustness & Centering Sensitivity
 * 
 * Fully accessible (ARIA, keyboard navigation, reduced motion compliant)
 */

(function () {
  'use strict';

  // --- 1. METHODOLOGY FLOWCHART ---
  function initFlowchart() {
    const container = document.getElementById('flowchart-canvas');
    const detailPanel = document.getElementById('flow-detail-content');
    if (!container || !window.SITE_DATA || !window.SITE_DATA.flow_config) return;

    const config = window.SITE_DATA.flow_config;
    const phases = config.phases;
    const nodes = config.nodes;
    const traceMap = config.trace;

    let html = '<div class="flow-swimlanes">';

    phases.forEach((phase) => {
      html += `
        <div class="flow-phase-band" data-phase="${phase.id}">
          <div class="flow-phase-header">
            <span class="flow-phase-tag">${phase.label}</span>
          </div>
          <div class="flow-phase-nodes">
      `;

      const phaseNodes = nodes.filter((n) => n.phase === phase.id);
      phaseNodes.forEach((node) => {
        const metricHtml = node.metric ? `<span class="flow-node-metric">${node.metric}</span>` : '';
        const subHtml = node.sub ? `<ul class="flow-node-sub">${node.sub.map(s => `<li>${s}</li>`).join('')}</ul>` : '';
        
        let branchHtml = '';
        if (node.branches) {
          branchHtml = `<div class="flow-node-branches">${node.branches.map(b => `
            <span class="flow-branch-chip"><strong>${b.label}</strong>: ${b.n}</span>
          `).join('')}</div>`;
        }

        html += `
          <button type="button" class="flow-node-card" id="flow-node-${node.id}" data-node-id="${node.id}" aria-expanded="false">
            <div class="flow-node-header">
              <span class="flow-node-title">${node.label}</span>
              ${metricHtml}
            </div>
            ${subHtml}
            ${branchHtml}
            <div class="flow-node-footer">
              <span class="flow-node-source">${node.source || ''}</span>
              <span class="flow-node-action">Click to inspect →</span>
            </div>
          </button>
        `;
      });

      html += `
          </div>
        </div>
      `;
    });

    html += '</div>';
    container.innerHTML = html;

    // Attach interaction listeners
    const nodeCards = container.querySelectorAll('.flow-node-card');
    nodeCards.forEach((card) => {
      card.addEventListener('click', function () {
        const nodeId = this.getAttribute('data-node-id');
        selectFlowNode(nodeId);
      });
    });

    // Setup evidence trace buttons
    const traceButtons = document.querySelectorAll('.trace-btn');
    traceButtons.forEach((btn) => {
      btn.addEventListener('click', function () {
        const rId = this.getAttribute('data-trace-r');
        traceEvidencePath(rId);
      });
    });

    // Select first node by default
    if (nodes.length > 0) {
      selectFlowNode(nodes[0].id);
    }
  }

  function selectFlowNode(nodeId) {
    const config = window.SITE_DATA.flow_config;
    const node = config.nodes.find((n) => n.id === nodeId);
    const detailPanel = document.getElementById('flow-detail-content');
    const allCards = document.querySelectorAll('.flow-node-card');

    allCards.forEach((c) => {
      c.classList.remove('is-active');
      c.setAttribute('aria-expanded', 'false');
    });

    const activeCard = document.getElementById(`flow-node-${nodeId}`);
    if (activeCard) {
      activeCard.classList.add('is-active');
      activeCard.setAttribute('aria-expanded', 'true');
    }

    if (!node || !detailPanel) return;

    let methodsHtml = '';
    if (node.sub && node.sub.length > 0) {
      methodsHtml = `
        <div class="detail-block">
          <h4>Core Analytical Methods & Diagnostics</h4>
          <ul class="detail-list">
            ${node.sub.map(s => `<li>${s}</li>`).join('')}
          </ul>
        </div>
      `;
    }

    let branchesHtml = '';
    if (node.branches) {
      branchesHtml = `
        <div class="detail-block">
          <h4>Sample Partitioning</h4>
          <div class="detail-grid">
            ${node.branches.map(b => `
              <div class="detail-cell">
                <strong>${b.label}</strong>
                <span class="cell-val">${b.n}</span>
                ${b.note ? `<span class="cell-note">${b.note}</span>` : ''}
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    detailPanel.innerHTML = `
      <div class="flow-detail-header">
        <span class="flow-detail-phase-tag">${node.phase.toUpperCase()} PHASE</span>
        <h3 class="flow-detail-title">${node.label}</h3>
        ${node.metric ? `<span class="flow-detail-badge">${node.metric}</span>` : ''}
      </div>
      <p class="flow-detail-desc">${node.detail}</p>
      ${branchesHtml}
      ${methodsHtml}
      <div class="flow-detail-meta">
        <div class="meta-row">
          <span class="meta-label">Primary Report Reference:</span>
          <span class="meta-value">${node.source || 'N/A'}</span>
        </div>
        ${node.anchor ? `
        <div class="meta-row">
          <span class="meta-label">Direct Section:</span>
          <a href="${node.anchor}" class="meta-link">Navigate to dashboard section ↓</a>
        </div>` : ''}
      </div>
    `;
  }

  function traceEvidencePath(recId) {
    const config = window.SITE_DATA.flow_config;
    const traceMap = config.trace;
    const targetNodes = traceMap[recId] || [];
    const allCards = document.querySelectorAll('.flow-node-card');
    const allTraceBtns = document.querySelectorAll('.trace-btn');

    allTraceBtns.forEach((b) => b.classList.remove('is-active'));
    const activeBtn = document.querySelector(`.trace-btn[data-trace-r="${recId}"]`);
    if (activeBtn) activeBtn.classList.add('is-active');

    allCards.forEach((c) => {
      const nId = c.getAttribute('data-node-id');
      if (targetNodes.includes(nId) || nId === 'crm') {
        c.classList.add('is-traced');
        c.classList.remove('is-dimmed');
      } else {
        c.classList.remove('is-traced');
        c.classList.add('is-dimmed');
      }
    });

    const statusEl = document.getElementById('trace-status-msg');
    if (statusEl) {
      statusEl.textContent = `Tracing empirical lineage for Recommendation ${recId} (${targetNodes.join(' → ')} → CRM).`;
    }
  }

  // --- 2. INTERACTIVE PPM SVG DIAGRAM ---
  function initPPMDiagram() {
    const container = document.getElementById('ppm-interactive-diagram');
    if (!container || !window.SITE_DATA) return;

    const hypotheses = window.SITE_DATA.table12a_hypotheses || [];
    const centering = window.SITE_DATA.table21_centering || [];

    function renderPPM(mode) {
      // mode: 'hypothesised', 'raw', 'centered'
      const getVal = (hCode, construct) => {
        const hObj = hypotheses.find((h) => h.H === hCode);
        const cObj = centering.find((c) => c.construct === construct || c.construct.startsWith(construct));
        
        if (mode === 'hypothesised') {
          return { label: hObj ? hObj.Expected_direction : 'N/A', tone: 'neutral' };
        } else if (mode === 'raw') {
          return { label: hObj ? `ρ = +${hObj.Coefficient.toFixed(3)}` : 'N/A', tone: hObj && hObj.Decision_rule_result.includes('Supported') ? 'success' : 'danger' };
        } else {
          if (cObj) {
            const val = cObj.rho_within_person_centered;
            const sign = val >= 0 ? '+' : '';
            return { label: `Centered ρ = ${sign}${val.toFixed(2)}`, tone: Math.abs(val) < 0.15 ? 'warning' : 'neutral' };
          }
          return { label: 'No multi-item scale', tone: 'muted' };
        }
      };

      const satVal = getVal('H1', 'SAT');
      const altVal = getVal('H2', 'ALT');
      const varVal = getVal('H3', 'VAR');
      const promoVal = getVal('H4', 'PROMO');
      const scVal = getVal('H5', 'SWEFFORT');
      const famVal = getVal('H6', 'FAM');
      const inertVal = getVal('H7', 'INERT');

      container.innerHTML = `
        <div class="ppm-visual-grid">
          <!-- PUSH COLUMN -->
          <div class="ppm-col ppm-push-col">
            <div class="ppm-col-header">
              <span class="ppm-col-tag push-tag">PUSH FACTOR</span>
              <h4>Dissatisfaction & Service Quality</h4>
            </div>
            <div class="ppm-card ppm-push-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H1 (SAT)</span>
                <span class="ppm-item-code">SAT1, SAT2</span>
              </div>
              <p class="ppm-card-title">Satisfaction with Zepto</p>
              <div class="ppm-stat-pill tone-${satVal.tone}">${satVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.170 (p=0.249) · Centered: ρ = -0.59</span>
            </div>
          </div>

          <!-- PULL COLUMN -->
          <div class="ppm-col ppm-pull-col">
            <div class="ppm-col-header">
              <span class="ppm-col-tag pull-tag">PULL FACTORS</span>
              <h4>Competitor Attractiveness</h4>
            </div>
            <div class="ppm-card ppm-pull-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H2 (ALT)</span>
                <span class="ppm-item-code">ALT1, ALT2</span>
              </div>
              <p class="ppm-card-title">Alternative Platform Attractiveness</p>
              <div class="ppm-stat-pill tone-${altVal.tone}">${altVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.685 · Centered: ρ = -0.03</span>
            </div>
            <div class="ppm-card ppm-pull-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H3 (VAR)</span>
                <span class="ppm-item-code">VAR1, VAR2</span>
              </div>
              <p class="ppm-card-title">Product Variety & Range</p>
              <div class="ppm-stat-pill tone-${varVal.tone}">${varVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.694 · Centered: ρ = +0.31</span>
            </div>
            <div class="ppm-card ppm-pull-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H4 (PROMO)</span>
                <span class="ppm-single-tag">Single-item</span>
              </div>
              <p class="ppm-card-title">Deals & Promotional Pricing</p>
              <div class="ppm-stat-pill tone-${promoVal.tone}">${promoVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.700 · Centered CI spans 0</span>
            </div>
          </div>

          <!-- MOORING COLUMN -->
          <div class="ppm-col ppm-mooring-col">
            <div class="ppm-col-header">
              <span class="ppm-col-tag mooring-tag">MOORING FACTORS</span>
              <h4>Switching Barriers & Inertia</h4>
            </div>
            <div class="ppm-card ppm-mooring-card ppm-card-alert">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H5 (SWEFFORT)</span>
                <span class="ppm-item-code">SC1, SC2</span>
              </div>
              <p class="ppm-card-title">Switching Effort / Barriers</p>
              <div class="ppm-stat-pill tone-${scVal.tone}">${scVal.label}</div>
              <div class="ppm-alert-box">
                <strong>Opposite Sign:</strong> Raw ρ = +0.721 (HTMT = 0.923). Collapses to ρ = +0.05 post-centering. Inconclusive barrier.
              </div>
            </div>
            <div class="ppm-card ppm-mooring-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H6 (FAM)</span>
                <span class="ppm-single-tag">Single-item</span>
              </div>
              <p class="ppm-card-title">Platform Familiarity</p>
              <div class="ppm-stat-pill tone-${famVal.tone}">${famVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.245 · Holm p = 0.249 (Not supported)</span>
            </div>
            <div class="ppm-card ppm-mooring-card">
              <div class="ppm-card-top">
                <span class="ppm-h-code">H7 (INERT)</span>
                <span class="ppm-n-tag">n=46</span>
              </div>
              <p class="ppm-card-title">Habitual Inertia</p>
              <div class="ppm-stat-pill tone-${inertVal.tone}">${inertVal.label}</div>
              <span class="ppm-card-note">Raw: ρ = +0.253 · Holm p = 0.249 (Complete-case n=46)</span>
            </div>
          </div>

          <!-- OUTCOME TARGET -->
          <div class="ppm-outcome-col">
            <div class="ppm-outcome-card">
              <span class="ppm-outcome-tag">DEPENDENT CONSTRUCT</span>
              <h3>Switching Intention</h3>
              <p class="ppm-outcome-sub">Current Users (n=51) · Scale: INT1, INT2, INT3</p>
              <div class="ppm-model-stats">
                <div class="model-stat-row">
                  <span>Pre-specified OLS Model (M1):</span>
                  <strong>R² = 0.696, F(4,46) = 26.27</strong>
                </div>
                <div class="model-stat-row">
                  <span>Standard Errors:</span>
                  <strong>HC3 Heteroskedasticity-Consistent</strong>
                </div>
              </div>
              <p class="ppm-caveat-text">
                * Note: Connectors represent pre-specified theoretical directions, not confirmed causal paths.
              </p>
            </div>
          </div>
        </div>
      `;
    }

    renderPPM('raw');

    const toggles = document.querySelectorAll('.ppm-mode-btn');
    toggles.forEach((btn) => {
      btn.addEventListener('click', function () {
        toggles.forEach((b) => b.classList.remove('is-active'));
        this.classList.add('is-active');
        const mode = this.getAttribute('data-mode');
        renderPPM(mode);
      });
    });
  }

  // --- 3. CUSTOM SVG DOT-AND-WHISKER PLOT (H1–H7) ---
  function initDotWhiskerPlot() {
    const container = document.getElementById('hypotheses-dot-whisker-svg');
    if (!container || !window.SITE_DATA) return;

    const data = window.SITE_DATA.table12a_hypotheses || [];
    const hList = data.filter((d) => ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7'].includes(d.H));

    const width = 760;
    const height = 360;
    const margin = { top: 30, right: 40, bottom: 50, left: 160 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    // Scale from -0.3 to +1.0
    const xMin = -0.3;
    const xMax = 1.0;
    const xScale = (val) => margin.left + ((val - xMin) / (xMax - xMin)) * innerWidth;
    const yScale = (idx) => margin.top + (idx + 0.5) * (innerHeight / hList.length);

    let svg = `<svg viewBox="0 0 ${width} ${height}" class="dot-whisker-svg" role="img" aria-label="Dot and whisker plot of Spearman correlation coefficients for hypotheses H1 through H7">`;

    // Zero reference line
    const zeroX = xScale(0);
    svg += `<line x1="${zeroX}" y1="${margin.top}" x2="${zeroX}" y2="${height - margin.bottom}" stroke="#C4B5E8" stroke-width="1.5" stroke-dasharray="4,4" />`;
    svg += `<text x="${zeroX}" y="${margin.top - 8}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#796E8A">0.0 (Null)</text>`;

    // Grid lines & X axis ticks
    [-0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0].forEach((tick) => {
      const tx = xScale(tick);
      svg += `<line x1="${tx}" y1="${margin.top}" x2="${tx}" y2="${height - margin.bottom}" stroke="#F0EBFA" stroke-width="1" />`;
      svg += `<text x="${tx}" y="${height - margin.bottom + 18}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#584F66">${tick >= 0 ? '+' : ''}${tick.toFixed(1)}</text>`;
    });

    // Rows
    hList.forEach((h, idx) => {
      const y = yScale(idx);
      const coeff = parseFloat(h.Coefficient);
      
      // Parse CI e.g. "[-0.12, 0.44]"
      let ciLow = coeff - 0.15;
      let ciHigh = coeff + 0.15;
      if (h.CI95 && h.CI95.includes(',')) {
        const parts = h.CI95.replace('[', '').replace(']', '').split(',');
        ciLow = parseFloat(parts[0].trim());
        ciHigh = parseFloat(parts[1].trim());
      }

      const xPoint = xScale(coeff);
      const xLow = xScale(ciLow);
      const xHigh = xScale(ciHigh);

      const isSupported = h.Decision_rule_result.includes('Supported') && !h.Decision_rule_result.includes('opposite');
      const isOpposite = h.Decision_rule_result.includes('opposite');
      const pointColor = isOpposite ? '#B91C1C' : isSupported ? '#15803D' : '#6B7280';

      // Row label
      svg += `<text x="${margin.left - 12}" y="${y + 4}" text-anchor="end" font-family="Inter" font-weight="600" font-size="12" fill="#1A1326">${h.H}: ${h.Construct} (${h.PPM})</text>`;

      // Whisker bar (95% CI)
      svg += `<line x1="${xLow}" y1="${y}" x2="${xHigh}" y2="${y}" stroke="${pointColor}" stroke-width="2.5" stroke-linecap="round" />`;
      svg += `<line x1="${xLow}" y1="${y - 4}" x2="${xLow}" y2="${y + 4}" stroke="${pointColor}" stroke-width="2" />`;
      svg += `<line x1="${xHigh}" y1="${y - 4}" x2="${xHigh}" y2="${y + 4}" stroke="${pointColor}" stroke-width="2" />`;

      // Central point
      svg += `<circle cx="${xPoint}" cy="${y}" r="5.5" fill="${pointColor}" stroke="#FFFFFF" stroke-width="2" />`;

      // Value label
      svg += `<text x="${xHigh + 8}" y="${y + 4}" font-family="JetBrains Mono" font-size="11" fill="#1A1326">ρ = ${coeff >= 0 ? '+' : ''}${coeff.toFixed(3)}</text>`;
    });

    svg += '</svg>';
    container.innerHTML = svg;
  }

  // --- 4. CUSTOM SVG DUMBBELL PLOT (ROBUSTNESS & CENTERING) ---
  function initDumbbellPlot() {
    const container = document.getElementById('centering-dumbbell-svg');
    if (!container || !window.SITE_DATA) return;

    const centeringData = window.SITE_DATA.table21_centering || [];
    const width = 760;
    const height = 300;
    const margin = { top: 30, right: 50, bottom: 50, left: 160 };
    const innerWidth = width - margin.left - margin.right;
    const innerHeight = height - margin.top - margin.bottom;

    const xMin = -0.8;
    const xMax = 0.9;
    const xScale = (val) => margin.left + ((val - xMin) / (xMax - xMin)) * innerWidth;
    const yScale = (idx) => margin.top + (idx + 0.5) * (innerHeight / centeringData.length);

    let svg = `<svg viewBox="0 0 ${width} ${height}" class="dumbbell-svg" role="img" aria-label="Dumbbell plot comparing raw vs within-person centered Spearman correlations">`;

    // Zero reference line
    const zeroX = xScale(0);
    svg += `<line x1="${zeroX}" y1="${margin.top}" x2="${zeroX}" y2="${height - margin.bottom}" stroke="#C4B5E8" stroke-width="1.5" stroke-dasharray="4,4" />`;
    svg += `<text x="${zeroX}" y="${margin.top - 8}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#796E8A">0.0 (Null)</text>`;

    // Grid ticks
    [-0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8].forEach((tick) => {
      const tx = xScale(tick);
      svg += `<line x1="${tx}" y1="${margin.top}" x2="${tx}" y2="${height - margin.bottom}" stroke="#F0EBFA" stroke-width="1" />`;
      svg += `<text x="${tx}" y="${height - margin.bottom + 18}" text-anchor="middle" font-family="JetBrains Mono" font-size="11" fill="#584F66">${tick >= 0 ? '+' : ''}${tick.toFixed(1)}</text>`;
    });

    centeringData.forEach((row, idx) => {
      const y = yScale(idx);
      const rawVal = parseFloat(row.rho_raw);
      const centVal = parseFloat(row.rho_within_person_centered);
      const ciLow = parseFloat(row.ci_low_centered);
      const ciHigh = parseFloat(row.ci_high_centered);

      const xRaw = xScale(rawVal);
      const xCent = xScale(centVal);
      const xCiLow = xScale(ciLow);
      const xCiHigh = xScale(ciHigh);

      // Label
      svg += `<text x="${margin.left - 12}" y="${y + 4}" text-anchor="end" font-family="Inter" font-weight="600" font-size="12" fill="#1A1326">${row.construct}</text>`;

      // Centered CI band (hollow area)
      svg += `<line x1="${xCiLow}" y1="${y}" x2="${xCiHigh}" y2="${y}" stroke="#7C3AED" stroke-width="1.5" stroke-dasharray="2,2" opacity="0.7" />`;

      // Connecting connector between raw and centered
      svg += `<line x1="${xRaw}" y1="${y}" x2="${xCent}" y2="${y}" stroke="#B45309" stroke-width="2.5" stroke-linecap="round" />`;

      // Raw dot (Solid Magenta)
      svg += `<circle cx="${xRaw}" cy="${y}" r="6" fill="#A21CAF" stroke="#FFFFFF" stroke-width="2" />`;

      // Centered dot (Hollow Electric Violet)
      svg += `<circle cx="${xCent}" cy="${y}" r="6" fill="#FFFFFF" stroke="#5B21B6" stroke-width="2.5" />`;

      // Value annotation
      svg += `<text x="${Math.max(xRaw, xCent) + 12}" y="${y + 4}" font-family="JetBrains Mono" font-size="11" fill="#584F66">${rawVal.toFixed(2)} → ${centVal.toFixed(2)}</text>`;
    });

    svg += '</svg>';
    container.innerHTML = svg;
  }

  // --- INITIALIZE ALL COMPONENTS ON DOM READY ---
  document.addEventListener('DOMContentLoaded', function () {
    initFlowchart();
    initPPMDiagram();
    initDotWhiskerPlot();
    initDumbbellPlot();
  });

})();
