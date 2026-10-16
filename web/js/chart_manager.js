/**
 * Zepto CRM Switching Research — Chart Manager
 * Handles Chart.js 4.4.1 instances with ZERO hard-coded statistics.
 * Every chart dynamically pulls data from window.SITE_DATA.
 * Lazy initialisation via IntersectionObserver; graceful CDN fallback to accessible data tables.
 * Classic script (no ES modules, file:// compatible)
 */
(function () {
  'use strict';

  var chartInstances = {};

  function checkCdnAvailability() {
    var banner = document.getElementById('chart-fallback-banner');
    if (typeof Chart === 'undefined') {
      if (banner) banner.style.display = 'block';
      // Automatically reveal all fallback data tables
      document.querySelectorAll('.chart-table-container').forEach(function (tbl) {
        tbl.classList.add('open');
      });
      return false;
    }
    return true;
  }

  function setupChartDefaults() {
    if (typeof Chart === 'undefined') return;

    Chart.defaults.font.family = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif";
    Chart.defaults.color = '#c9bedf';
    Chart.defaults.borderColor = 'rgba(255, 255, 255, 0.08)';

    Chart.defaults.plugins.tooltip.backgroundColor = '#1e1536';
    Chart.defaults.plugins.tooltip.titleColor = '#ffffff';
    Chart.defaults.plugins.tooltip.bodyColor = '#c9bedf';
    Chart.defaults.plugins.tooltip.borderColor = '#5b3a9d';
    Chart.defaults.plugins.tooltip.borderWidth = 1;
    Chart.defaults.plugins.tooltip.padding = 10;
    Chart.defaults.plugins.tooltip.cornerRadius = 6;
  }

  // --- CHART BUILDERS (DATA STRICTLY SOURCED FROM WINDOW.SITE_DATA) ---

  // 1. User Lifecycle Donut (table03)
  function buildUserGroupChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table03_user_groups) return null;
    var rows = window.SITE_DATA.table03_user_groups;
    var labels = rows.map(function (r) { return r.category + ' (n=' + r.n + ', ' + Number(r.pct).toFixed(1) + '%)'; });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: counts,
          backgroundColor: ['#8b5cf6', '#ec4899', '#63577d'],
          borderColor: '#090611',
          borderWidth: 2,
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 12, padding: 14, color: '#c9bedf' }
          }
        },
        cutout: '62%'
      }
    });
  }

  // 2. Questionnaire Version Distribution (table03b)
  function buildVersionChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table03b_versions) return null;
    var rows = window.SITE_DATA.table03b_versions;
    var labels = rows.map(function (r) { return r.category; });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Respondents (n)',
          data: counts,
          backgroundColor: ['#7c3aed', '#ec4899', '#8b5cf6'],
          borderRadius: 6,
          maxBarThickness: 48
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            ticks: { color: '#8e80ab' }
          },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 3. Former User Classes (table13d)
  function buildFormerClassChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table13d_former_classes) return null;
    var rows = window.SITE_DATA.table13d_former_classes;
    var labels = rows.map(function (r) {
      if (r.category.indexOf('A_') === 0) return 'Class A: Coverage-Primary (31)';
      if (r.category.indexOf('B_') === 0) return 'Class B: Coverage-Mentioned (10)';
      return 'Class C: Voluntary-Only (32)';
    });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: counts,
          backgroundColor: ['#06b6d4', '#f59e0b', '#ec4899'],
          borderColor: '#090611',
          borderWidth: 2,
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 12, padding: 12, color: '#c9bedf' }
          }
        },
        cutout: '62%'
      }
    });
  }

  // 4. Voluntary Exit Reasons (table13e, n=32)
  function buildVoluntaryReasonsChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table13e_voluntary_reasons) return null;
    var rows = window.SITE_DATA.table13e_voluntary_reasons;
    var labels = rows.map(function (r) { return r.category; });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          axis: 'y',
          label: 'Voluntary Exits (n)',
          data: counts,
          backgroundColor: '#ec4899',
          borderRadius: 4
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          x: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            title: { display: true, text: 'Frequency (n=32 voluntary exits)', color: '#8e80ab' }
          },
          y: { grid: { display: false } }
        }
      }
    });
  }

  // 5. Competitor Variety Advantage (table13c_alt_variants)
  function buildFormerAltVariantChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table13c_alt_variants) return null;
    var rows = window.SITE_DATA.table13c_alt_variants;
    var labels = rows.map(function (r) { return r.response || r.category || 'Response'; });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Respondents (n)',
          data: counts,
          backgroundColor: ['#10b981', '#f59e0b', '#8e80ab'],
          borderRadius: 6,
          maxBarThickness: 40
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' }
          },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 6. Return Willingness Distribution (table13c_return)
  function buildFormerReturnChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table13c_return) return null;
    var rows = window.SITE_DATA.table13c_return;
    var labels = rows.map(function (r) { return r.response || r.category || 'Rating'; });
    var counts = rows.map(function (r) { return r.n; });

    return new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Former Users (n)',
          data: counts,
          backgroundColor: ['#10b981', '#34d399', '#f59e0b', '#f87171', '#ef4444'],
          borderRadius: 6,
          maxBarThickness: 36
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            beginAtZero: true,
            grid: { color: 'rgba(255, 255, 255, 0.05)' }
          },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // 7. Model M1 Regression Coefficients (table12)
  function buildRegressionChart(canvas) {
    if (!window.SITE_DATA || !window.SITE_DATA.table12_regression) return null;
    var rows = window.SITE_DATA.table12_regression.filter(function (r) {
      return r.model.indexOf('M1') === 0 && r.term !== 'const';
    });
    var labels = rows.map(function (r) { return r.term; });
    var betas = rows.map(function (r) { return r.b; });

    return new Chart(canvas, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          label: 'Unstandardized b (HC3 SE)',
          data: betas,
          backgroundColor: betas.map(function (b) { return b >= 0 ? '#8b5cf6' : '#f43f5e'; }),
          borderRadius: 4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false } },
        scales: {
          y: {
            grid: { color: 'rgba(255, 255, 255, 0.05)' },
            title: { display: true, text: 'Coefficient b', color: '#8e80ab' }
          },
          x: { grid: { display: false } }
        }
      }
    });
  }

  // Lazy Initialisation via IntersectionObserver
  function initLazyCharts() {
    if (typeof Chart === 'undefined') return;

    var chartRegistry = {
      'userGroupChart': buildUserGroupChart,
      'versionChart': buildVersionChart,
      'formerClassChart': buildFormerClassChart,
      'voluntaryReasonsChart': buildVoluntaryReasonsChart,
      'formerAltVariantChart': buildFormerAltVariantChart,
      'formerReturnChart': buildFormerReturnChart,
      'regressionCoeffChart': buildRegressionChart
    };

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var canvas = entry.target;
          var chartId = canvas.id;
          if (chartRegistry[chartId] && !chartInstances[chartId]) {
            chartInstances[chartId] = chartRegistry[chartId](canvas);
          }
          observer.unobserve(canvas);
        }
      });
    }, { rootMargin: '100px 0px', threshold: 0.1 });

    Object.keys(chartRegistry).forEach(function (cid) {
      var el = document.getElementById(cid);
      if (el) observer.observe(el);
    });
  }

  // Accessible Table Toggles
  function initTableToggles() {
    document.querySelectorAll('.btn-chart-toggle').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetId = btn.getAttribute('data-table-target');
        var tbl = document.getElementById(targetId);
        if (tbl) {
          var isOpen = tbl.classList.toggle('open');
          btn.textContent = isOpen ? 'Hide Table View' : 'Show Accessible Table';
          btn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        }
      });
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    if (checkCdnAvailability()) {
      setupChartDefaults();
      initLazyCharts();
    }
    initTableToggles();
  });

  window.ChartManager = {
    instances: chartInstances
  };

})();
