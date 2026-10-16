/**
 * Zepto CRM Switching Research — Guided Viva Mode
 * 10-Step Interactive Walkthrough for Academic Examination
 * Classic script (no ES modules, file:// compatible)
 */
(function () {
  'use strict';

  var VIVA_STEPS = [
    {
      step: 1,
      sectionId: 'overview',
      title: '1. Executive Overview & Reconciliation',
      body: 'This empirical mixed-methods study investigates switching intentions and catalog-driven attrition in Indian quick commerce. All statistics strictly follow the canonical CSV tables (superseding early report drafts as documented in DISCREPANCIES.md).',
      caveat: 'Caveat: Cross-sectional survey associations indicate perceptual relationships, never causation.'
    },
    {
      step: 2,
      sectionId: 'design',
      title: '2. Research Design & Method Pipeline',
      body: 'The 5-stage research design connects problem formulation to survey microdata (N=184), scale diagnostics, 690-page UDRHP-I secondary evidence extraction, and CRM strategy synthesis.',
      caveat: 'Caveat: No respondent exclusions were made (N=184 complete); straight-liner and version sensitivity checks are reported.'
    },
    {
      step: 3,
      sectionId: 'survey',
      title: '3. Sample Quality & Lifecycle Partitioning',
      body: 'The verified sample partitions into 51 Current Users (27.7%), 73 Former Users (39.7%), and 60 Never-Users (32.6%). Version rollout: V1 (16), V1.5 (6), V2 (162). Complete-case analysis uses n=46 for items added in V2.',
      caveat: 'Caveat: Never-users (n=60) are non-adopters and are strictly excluded from all switching analyses.'
    },
    {
      step: 4,
      sectionId: 'ppm',
      title: '4. Push–Pull–Mooring Construct Framework',
      body: 'Adapting Bansal et al. (2005) to quick commerce: Push represents satisfaction (SAT); Pull captures alternative attractiveness (ALT), product variety (VAR), and promotions (PROMO); Mooring reflects switching effort (SWEFFORT), familiarity (FAM), and inertia (INERT).',
      caveat: 'Caveat: Single-item constructs (PROMO1, FAM1, INERT1) exhibit inherent measurement limitations.'
    },
    {
      step: 5,
      sectionId: 'hypothesis',
      title: '5. Hypothesis Lab (H1–H10 Results)',
      body: 'H2 (ALT, rho=+0.685), H3 (VAR composite, rho=+0.694), and H4 (PROMO, rho=+0.700) are supported on raw scores. H1 (SAT, rho=+0.170, Holm p=0.2492), H6 (FAM, rho=+0.245), and H7 (INERT, rho=+0.253, n=46) are inconclusive.',
      caveat: 'Critical finding: H5 (SWEFFORT, rho=+0.721) is anomalous (positive sign contrary to theory), reflecting that users perceive high effort precisely when contemplating switching to rivals.'
    },
    {
      step: 6,
      sectionId: 'statistics',
      title: '6. Regression & Collinearity Diagnostics',
      body: 'Model M1 regression yields R2=0.7057, F(4,46)=27.58 (HC3 SEs). However, variance decomposition demonstrates that the PULL composite alone accounts for R2=0.6356, while SAT+SWEFFORT+FAM together add only +0.0701.',
      caveat: 'Caveat: HTMT overlap (0.92 with intention) reveals that pull perceptions and switching intentions capture overlapping evaluative constructs.'
    },
    {
      step: 7,
      sectionId: 'statistics',
      title: '7. Within-Person Centering Attenuation',
      body: 'Within-person centering (Table 21) causes pull correlations to attenuate sharply: ALT (+0.685 -> -0.026), VAR1 (+0.731 -> +0.305), and SWEFFORT (+0.721 -> +0.054). SAT shifts from +0.170 to -0.588.',
      caveat: 'Method note: Centering isolates relative priorities from general response elevation, demonstrating that raw scores reflect common-method positivity.'
    },
    {
      step: 8,
      sectionId: 'former',
      title: '8. Former User Exit Breakdown',
      body: 'Former users (n=73) classify into: Class A Coverage-primary (31, 42.5%), Class B Coverage-mentioned (10, 13.7%), and Class C Voluntary-only (32, 43.8%). Among 32 voluntary exits, Product Availability (8) and Variety (8) account for 50.0%.',
      caveat: 'Caveat: 56.2% of former users cited dark-store unserviceability (involuntary exit), meaning churn is primarily logistical, not platform rejection.'
    },
    {
      step: 9,
      sectionId: 'udrhp',
      title: '9. Zepto UDRHP-I Secondary Evidence',
      body: 'Triangulation with Zepto’s 690-page IPO filing (E01–E25) confirms capital deployment: Rs 16,289.75M for dark stores, Rs 17,349.41M for leases, Rs 4,000.00M for cloud/ML, Rs 5,200.00M for marketing. Dark stores expanded to 1,139 across 66 cities; SKUs reached 46,623.',
      caveat: 'Standard: Regulatory disclosures document company capacity and risk disclosures, not individual consumer-level retention causality.'
    },
    {
      step: 10,
      sectionId: 'recommendations',
      title: '10. Evidence-Based CRM Recommendations',
      body: 'Synthesized strategy: R1 Serviceability waitlist (High impact), R2 Restock & substitution alerts (Assortment mitigation), R3 Segmented win-back for availability leavers (n=16 pilot), R5 Hygienic service recovery. Note: R4 lock-in is NOT RECOMMENDED on current evidence.',
      caveat: 'Final Viva Precaution: R4 is excluded because switching-barrier scales must be validated before locking mechanisms are deployed.'
    }
  ];

  function showVivaStep(index) {
    if (index < 0 || index >= VIVA_STEPS.length) return;
    window.AppState.vivaStep = index;
    var stepData = VIVA_STEPS[index];

    var dock = document.getElementById('viva-dock');
    var badge = document.getElementById('viva-step-badge');
    var title = document.getElementById('viva-dock-title');
    var body = document.getElementById('viva-dock-body');
    var prevBtn = document.getElementById('viva-prev-btn');
    var nextBtn = document.getElementById('viva-next-btn');

    if (!dock) return;

    dock.style.display = 'block';
    if (badge) badge.textContent = 'Step ' + stepData.step + ' of ' + VIVA_STEPS.length;
    if (title) title.textContent = stepData.title;
    if (body) {
      body.innerHTML = '<div>' + stepData.body + '</div>' +
        '<div style="margin-top: 6px; padding: 6px 10px; background: rgba(245, 158, 11, 0.1); border-left: 3px solid var(--accent-amber); font-size: 0.76rem; color: #fbbf24;">' +
        '<strong>Methodological Note:</strong> ' + stepData.caveat +
        '</div>';
    }

    if (prevBtn) prevBtn.disabled = index === 0;
    if (nextBtn) {
      nextBtn.textContent = index === VIVA_STEPS.length - 1 ? 'Finish Walkthrough' : 'Next Step →';
    }

    // Scroll smoothly to the target section
    var targetSec = document.getElementById(stepData.sectionId);
    if (targetSec) {
      targetSec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function initVivaMode() {
    var triggerBtn = document.getElementById('viva-trigger-btn');
    var triggerTop = document.getElementById('viva-trigger-top');
    var closeBtn = document.getElementById('viva-close-btn');
    var prevBtn = document.getElementById('viva-prev-btn');
    var nextBtn = document.getElementById('viva-next-btn');
    var dock = document.getElementById('viva-dock');

    function startWalkthrough() {
      window.AppState.vivaActive = true;
      showVivaStep(0);
    }

    if (triggerBtn) triggerBtn.addEventListener('click', startWalkthrough);
    if (triggerTop) triggerTop.addEventListener('click', startWalkthrough);

    if (closeBtn && dock) {
      closeBtn.addEventListener('click', function () {
        dock.style.display = 'none';
        window.AppState.vivaActive = false;
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function () {
        if (window.AppState.vivaStep > 0) {
          showVivaStep(window.AppState.vivaStep - 1);
        }
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function () {
        if (window.AppState.vivaStep < VIVA_STEPS.length - 1) {
          showVivaStep(window.AppState.vivaStep + 1);
        } else {
          if (dock) dock.style.display = 'none';
          window.AppState.vivaActive = false;
        }
      });
    }
  }

  document.addEventListener('DOMContentLoaded', initVivaMode);

})();
