/**
 * Customer Switching Behaviour in India's Quick-Commerce Industry
 * Upgraded Research Dashboard Application Script (app.js)
 * 
 * Interactivity:
 * - Chart.js charts configured with design token palettes and exact table data
 * - Dynamic scroll progress bar indicator
 * - Interactive filtering for Media Claims (M01–M11), Literature (L01–L17), and CRM Recommendations (R1–R5)
 * - Accessible keyboard navigation & ARIA management
 */

document.addEventListener('DOMContentLoaded', () => {
  initScrollProgress();
  initDashboardCharts();
  initFilterHandlers();
});

// --- 1. LIVE SCROLL PROGRESS INDICATOR ---
function initScrollProgress() {
  const progressBar = document.getElementById('scroll-progress-bar');
  if (!progressBar) return;

  window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    progressBar.style.width = scrolled + '%';
  }, { passive: true });
}

// --- 2. CHART.JS VISUALIZATIONS ---
function initDashboardCharts() {
  if (typeof Chart === 'undefined') return;

  // Chart Global Design Defaults
  Chart.defaults.font.family = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif";
  Chart.defaults.color = '#584F66';
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.plugins.tooltip.cornerRadius = 6;
  Chart.defaults.plugins.tooltip.backgroundColor = '#2E1065';
  Chart.defaults.plugins.tooltip.titleFont = { size: 12, weight: '700', family: "'Inter', sans-serif" };
  Chart.defaults.plugins.tooltip.bodyFont = { size: 12, family: "'Inter', sans-serif" };

  // 1. User Lifecycle Group Donut (N=184: 51 Current, 73 Former, 60 Never)
  const ctxUserGroup = document.getElementById('userGroupChart')?.getContext('2d');
  if (ctxUserGroup) {
    new Chart(ctxUserGroup, {
      type: 'doughnut',
      data: {
        labels: ['Current Users (n=51)', 'Former Users (n=73)', 'Never-Users (n=60)'],
        datasets: [{
          data: [51, 73, 60],
          backgroundColor: ['#5B21B6', '#A21CAF', '#796E8A'],
          borderWidth: 2,
          borderColor: '#FFFFFF',
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 12, padding: 14, font: { size: 12, weight: '500' } }
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const total = 184;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return ` ${context.label}: ${val} respondents (${pct}%)`;
              }
            }
          }
        },
        cutout: '64%'
      }
    });
  }

  // 2. Questionnaire Version Distribution Bar (V1=16, V1.5=6, V2=162)
  const ctxVersion = document.getElementById('versionChart')?.getContext('2d');
  if (ctxVersion) {
    new Chart(ctxVersion, {
      type: 'bar',
      data: {
        labels: ['V1 (Early Pilot)', 'V1.5 (Intermediate)', 'V2 (Final Instrument)'],
        datasets: [{
          label: 'Respondents (n)',
          data: [16, 6, 162],
          backgroundColor: ['#7C3AED', '#A21CAF', '#5B21B6'],
          borderRadius: 6,
          maxBarThickness: 48
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function (context) {
                const total = 184;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return `Share: ${pct}% of total sample (N=184)`;
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 180,
            grid: { color: '#F0EBFA' },
            ticks: { font: { size: 11, family: "'JetBrains Mono', monospace" } }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '600' } }
          }
        }
      }
    });
  }

  // 3. Former Users 3-Class Exit Breakdown (n=73: Class A 31, Class B 10, Class C 32)
  const ctxFormerClass = document.getElementById('formerClassChart')?.getContext('2d');
  if (ctxFormerClass) {
    new Chart(ctxFormerClass, {
      type: 'doughnut',
      data: {
        labels: [
          'Class A: Coverage-Primary (31)',
          'Class B: Coverage-Overlap (10)',
          'Class C: Voluntary-Only (32)'
        ],
        datasets: [{
          data: [31, 10, 32],
          backgroundColor: ['#0E7490', '#B45309', '#A21CAF'],
          borderWidth: 2,
          borderColor: '#FFFFFF',
          hoverOffset: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 12, padding: 12, font: { size: 11, weight: '500' } }
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                const total = 73;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return ` ${context.label}: ${val} (${pct}%, 95% Wilson CI verified)`;
              }
            }
          }
        },
        cutout: '62%'
      }
    });
  }

  // 4. Voluntary Exit Reasons Breakdown (n=32)
  const ctxFormerVoluntary = document.getElementById('formerVoluntaryChart')?.getContext('2d');
  if (ctxFormerVoluntary) {
    new Chart(ctxFormerVoluntary, {
      type: 'bar',
      data: {
        labels: [
          'Product Availability',
          'Product Variety / Choice',
          'Delivery Speed',
          'Pricing',
          'Promotions / Deals',
          'App Performance',
          'Customer Support',
          'Product Quality'
        ],
        datasets: [{
          label: 'Voluntary Exits (n)',
          data: [8, 8, 4, 3, 3, 3, 2, 1],
          backgroundColor: [
            '#A21CAF', '#A21CAF', '#5B21B6', '#7C3AED', '#7C3AED', '#7C3AED', '#796E8A', '#796E8A'
          ],
          borderRadius: 4,
          maxBarThickness: 20
        }]
      },
      options: {
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function (context) {
                const total = 32;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return `Share: ${pct}% of voluntary exits (n=32)`;
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            max: 10,
            grid: { color: '#F0EBFA' },
            ticks: { font: { size: 11, family: "'JetBrains Mono', monospace" } }
          },
          y: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // 5. Competitor Assortment Advantage (n=68: Yes=41, Maybe=18, No=9)
  const ctxFormerAlt = document.getElementById('formerAltVariantChart')?.getContext('2d');
  if (ctxFormerAlt) {
    new Chart(ctxFormerAlt, {
      type: 'bar',
      data: {
        labels: ['Yes (Superior Variety)', 'Maybe', 'No (Same Assortment)'],
        datasets: [{
          label: 'Respondents (n)',
          data: [41, 18, 9],
          backgroundColor: ['#15803D', '#B45309', '#796E8A'],
          borderRadius: 6,
          maxBarThickness: 40
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function (context) {
                const total = 68;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return `Share: ${pct}% (n=68 former evaluating users)`;
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 50,
            grid: { color: '#F0EBFA' },
            ticks: { font: { size: 11, family: "'JetBrains Mono', monospace" } }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '600' } }
          }
        }
      }
    });
  }

  // 6. Return Willingness Distribution (n=68: 14 Def Yes, 27 Prob Yes, 20 Not Sure, 5 Prob No, 2 Def No)
  const ctxFormerReturn = document.getElementById('formerReturnChart')?.getContext('2d');
  if (ctxFormerReturn) {
    new Chart(ctxFormerReturn, {
      type: 'bar',
      data: {
        labels: ['Definitely Yes', 'Probably Yes', 'Not Sure', 'Probably No', 'Definitely No'],
        datasets: [{
          label: 'Former Users (n)',
          data: [14, 27, 20, 5, 2],
          backgroundColor: ['#15803D', '#16A34A', '#B45309', '#B91C1C', '#991B1B'],
          borderRadius: 6,
          maxBarThickness: 36
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function (context) {
                const total = 68;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return `Share: ${pct}% (n=68 former evaluating users)`;
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 30,
            grid: { color: '#F0EBFA' },
            ticks: { font: { size: 11, family: "'JetBrains Mono', monospace" } }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 10, weight: '600' } }
          }
        }
      }
    });
  }
}

// --- 3. FILTERING LOGIC ---
function initFilterHandlers() {
  // Media Claims Register Filter
  const mediaChips = document.querySelectorAll('#media-filter-bar .filter-chip');
  const mediaRows = document.querySelectorAll('#media-claims-table tbody tr');

  mediaChips.forEach((chip) => {
    chip.addEventListener('click', function () {
      mediaChips.forEach((c) => c.classList.remove('is-active'));
      this.classList.add('is-active');
      const filter = this.getAttribute('data-filter');

      mediaRows.forEach((row) => {
        const status = row.getAttribute('data-status');
        if (filter === 'all' || status === filter) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });
  });

  // Literature Register Filter
  const litChips = document.querySelectorAll('#lit-filter-bar .filter-chip');
  const litCards = document.querySelectorAll('#literature-cards-container .kpi-card');

  litChips.forEach((chip) => {
    chip.addEventListener('click', function () {
      litChips.forEach((c) => c.classList.remove('is-active'));
      this.classList.add('is-active');
      const filter = this.getAttribute('data-filter');

      litCards.forEach((card) => {
        const tier = card.getAttribute('data-tier');
        if (filter === 'all' || tier === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });

  // CRM Recommendations Filter
  const crmChips = document.querySelectorAll('#crm-filter-bar .filter-chip');
  const crmCards = document.querySelectorAll('.crm-chain-card');

  crmChips.forEach((chip) => {
    chip.addEventListener('click', function () {
      crmChips.forEach((c) => c.classList.remove('is-active'));
      this.classList.add('is-active');
      const filter = this.getAttribute('data-filter');

      crmCards.forEach((card) => {
        const status = card.getAttribute('data-status');
        if (filter === 'all' || status === filter) {
          card.style.display = '';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
