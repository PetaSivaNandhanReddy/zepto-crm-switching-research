/**
 * Zepto CRM Switching Research — Interactive Components
 * Filters, Detail Drawers, Dumbbell Toggle, Search & Accessibility
 * Classic script (no ES modules, file:// compatible)
 */
(function () {
  'use strict';

  // 1. Hypothesis Lab Filters & Drawers
  function initHypothesisLab() {
    var filterBtns = document.querySelectorAll('.hypo-filter-btn');
    var hypoRows = document.querySelectorAll('.hypo-table-row');

    filterBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        filterBtns.forEach(function (b) { b.classList.remove('active'); });
        this.classList.add('active');
        var filter = this.getAttribute('data-filter');

        hypoRows.forEach(function (row) {
          var dim = row.getAttribute('data-ppm');
          if (filter === 'all' || dim === filter) {
            row.style.display = '';
          } else {
            row.style.display = 'none';
          }
        });
      });
    });

    // Detail drawers toggle
    document.querySelectorAll('.btn-hypo-drawer').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetId = btn.getAttribute('data-target');
        var drawer = document.getElementById(targetId);
        if (drawer) {
          var isOpen = drawer.classList.toggle('open');
          btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
          btn.textContent = isOpen ? 'Close Details ▴' : 'View Details ▾';
        }
      });
    });
  }

  // 2. Dumbbell Toggle: Updates BOTH Chart and Narrative Interpretation
  function initDumbbellToggle() {
    var toggle = document.getElementById('dumbbell-mode-toggle');
    var narrativeEl = document.getElementById('dumbbell-interpretation-text');
    var dotWhiskerSvg = document.getElementById('centering-dumbbell-svg');

    if (!toggle || !narrativeEl) return;

    toggle.addEventListener('change', function () {
      var isCentered = this.checked;
      if (isCentered) {
        narrativeEl.innerHTML = '<strong>Within-Person Centered Mode:</strong> Eliminates individual response-style elevation (positivity bias). All pull factors attenuate drastically: Alternative Attractiveness (ALT) collapses from +0.685 to <strong>-0.026</strong> (CI [-0.34, +0.31]), and Variety (VAR1) drops from +0.731 to <strong>+0.305</strong>. Switching Effort (SWEFFORT) attenuates from +0.721 to <strong>+0.054</strong>. Satisfaction shifts to a negative association (<strong>-0.588</strong>), aligning with theoretical expectations.';
        narrativeEl.style.borderLeftColor = 'var(--accent-purple)';
      } else {
        narrativeEl.innerHTML = '<strong>Raw Bivariate Correlation Mode:</strong> Reflects unadjusted Spearman rank correlations across current users (n=51). Strong pull factors are observed: ALT (+0.685), VAR (+0.694 composite / +0.731 VAR1), PROMO (+0.700). Switching Effort (SWEFFORT) displays an anomalous positive association (+0.721), while Satisfaction (+0.170) is statistically non-significant (inconclusive).';
        narrativeEl.style.borderLeftColor = 'var(--accent-magenta)';
      }

      // Also trigger PPM diagram mode if present
      var ppmBtn = document.querySelector(`.ppm-mode-btn[data-mode="${isCentered ? 'centered' : 'raw'}"]`);
      if (ppmBtn) ppmBtn.click();
    });
  }

  // 3. Media Claims Filter
  function initMediaFilter() {
    var chips = document.querySelectorAll('#media-filter-bar .filter-btn');
    var rows = document.querySelectorAll('#media-claims-table tbody tr');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        var filter = this.getAttribute('data-filter');

        rows.forEach(function (row) {
          var status = row.getAttribute('data-status');
          if (filter === 'all' || status === filter) {
            row.style.display = '';
          } else {
            row.style.display = 'none';
          }
        });
      });
    });
  }

  // 4. Literature Tier Filter
  function initLitFilter() {
    var chips = document.querySelectorAll('#lit-filter-bar .filter-btn');
    var cards = document.querySelectorAll('#literature-cards-container .lit-card');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        var filter = this.getAttribute('data-filter');

        cards.forEach(function (card) {
          var tier = card.getAttribute('data-tier');
          if (filter === 'all' || tier === filter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 5. CRM Strategy Filter
  function initCrmFilter() {
    var chips = document.querySelectorAll('#crm-filter-bar .filter-btn');
    var cards = document.querySelectorAll('.crm-rec-card');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        chips.forEach(function (c) { c.classList.remove('active'); });
        this.classList.add('active');
        var filter = this.getAttribute('data-filter');

        cards.forEach(function (card) {
          var status = card.getAttribute('data-status');
          if (filter === 'all' || status === filter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // 6. Generic Drawers & Accordions
  function initAccordions() {
    document.querySelectorAll('.drawer-toggle-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetId = btn.getAttribute('data-drawer-target');
        var drawer = document.getElementById(targetId);
        if (drawer) {
          var isOpen = drawer.classList.toggle('open');
          btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        }
      });
    });
  }

  // 7. E01-E25 Evidence Search & Filter
  function initEvidenceSearch() {
    var searchInput = document.getElementById('evidence-search-input');
    var constructSelect = document.getElementById('evidence-construct-select');
    var cards = document.querySelectorAll('.evidence-card');

    function applyFilter() {
      var query = searchInput ? searchInput.value.toLowerCase().trim() : '';
      var construct = constructSelect ? constructSelect.value : 'all';

      cards.forEach(function (card) {
        var text = card.textContent.toLowerCase();
        var cardConstruct = card.getAttribute('data-construct') || '';
        var matchText = !query || text.indexOf(query) !== -1;
        var matchConstruct = construct === 'all' || cardConstruct.indexOf(construct) !== -1;

        if (matchText && matchConstruct) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    }

    if (searchInput) searchInput.addEventListener('input', applyFilter);
    if (constructSelect) constructSelect.addEventListener('change', applyFilter);
  }

  document.addEventListener('DOMContentLoaded', function () {
    initHypothesisLab();
    initDumbbellToggle();
    initMediaFilter();
    initLitFilter();
    initCrmFilter();
    initAccordions();
    initEvidenceSearch();
  });

})();
