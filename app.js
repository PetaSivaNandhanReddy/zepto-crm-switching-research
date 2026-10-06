/*
  Customer Switching Behaviour in India's Quick-Commerce Industry
  Authoritative Academic Research Dashboard JavaScript (app.js)
*/

document.addEventListener('DOMContentLoaded', () => {
  initCharts();
});

function initCharts() {
  // Common Chart.js Defaults
  Chart.defaults.font.family = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif";
  Chart.defaults.color = '#475569';
  Chart.defaults.plugins.tooltip.padding = 10;
  Chart.defaults.plugins.tooltip.cornerRadius = 6;

  // 1. User Lifecycle Group Distribution Donut
  const ctxUserGroup = document.getElementById('userGroupChart')?.getContext('2d');
  if (ctxUserGroup) {
    new Chart(ctxUserGroup, {
      type: 'doughnut',
      data: {
        labels: ['Current Users (n=51)', 'Former Users (n=73)', 'Never-Users (n=60)'],
        datasets: [{
          data: [51, 73, 60],
          backgroundColor: ['#2563eb', '#7c3aed', '#94a3b8'],
          borderWidth: 2,
          borderColor: '#ffffff',
          hoverOffset: 4
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 12, padding: 15, font: { size: 12, weight: '500' } }
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                const total = 184;
                const val = context.raw;
                const pct = ((val / total) * 100).toFixed(1);
                return ` ${context.label}: ${val} respondents (${pct}%)`;
              }
            }
          }
        },
        cutout: '62%'
      }
    });
  }

  // 2. Version Distribution Bar
  const ctxVersion = document.getElementById('versionChart')?.getContext('2d');
  if (ctxVersion) {
    new Chart(ctxVersion, {
      type: 'bar',
      data: {
        labels: ['Version 1 (Feb 2026)', 'Version 2 (Mar 2026)'],
        datasets: [{
          label: 'Respondents (n)',
          data: [75, 109],
          backgroundColor: ['#3b82f6', '#0d9488'],
          borderRadius: 6,
          maxBarThickness: 50
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function(context) {
                return context.dataIndex === 0 ? '40.8% of total sample' : '59.2% of total sample (Mann-Whitney U = 346.5, p = 0.6014)';
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 130,
            grid: { color: '#f1f5f9' },
            ticks: { font: { size: 11 } }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 12, weight: '500' } }
          }
        }
      }
    });
  }

  // 3. Hypotheses Chart (H1–H7 Spearman Correlations)
  const ctxHypo = document.getElementById('hypothesesChart')?.getContext('2d');
  if (ctxHypo) {
    new Chart(ctxHypo, {
      type: 'bar',
      data: {
        labels: [
          'H1: SAT (Push)',
          'H2: ALT (Pull)',
          'H3: VAR (Pull)',
          'H4: PROMO (Pull)',
          'H5: SWEFFORT (Mooring)*',
          'H6: FAM (Mooring)',
          'H7: INERT (Mooring)'
        ],
        datasets: [{
          label: 'Observed Spearman ρ with Switching Intention',
          data: [0.165, 0.685, 0.694, 0.700, 0.721, 0.248, 0.248],
          backgroundColor: [
            '#94a3b8', // H1 Not Sig
            '#2563eb', // H2 Sig
            '#2563eb', // H3 Sig
            '#0d9488', // H4 Highest Pull
            '#e11d48', // H5 Anomalous
            '#94a3b8', // H6 Not Sig
            '#94a3b8'  // H7 Not Sig
          ],
          borderRadius: 6,
          maxBarThickness: 32
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
              afterLabel: function(context) {
                const notes = [
                  'Expected (-), Observed +0.165, p = 0.2492 (Not Supported)',
                  'Expected (+), Observed +0.685, p < 0.001 (Supported Raw)',
                  'Expected (+), Observed +0.694, p < 0.001 (Supported Raw)',
                  'Expected (+), Observed +0.700, p < 0.001 (Supported Raw)',
                  'Expected (-), Observed +0.721, p < 0.001 (CONTRADICTED/ANOMALOUS)',
                  'Expected (-), Observed +0.248, p = 0.2492 (Not Supported)',
                  'Expected (-), Observed +0.248, p = 0.2492 (Not Supported)'
                ];
                return notes[context.dataIndex];
              }
            }
          }
        },
        scales: {
          x: {
            min: 0,
            max: 0.9,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return '+' + val.toFixed(2); },
              font: { size: 11 }
            }
          },
          y: {
            grid: { display: false },
            ticks: { font: { size: 12, weight: '600' } }
          }
        }
      }
    });
  }

  // 4. Robustness Check: Raw vs Within-Person Centered rho
  const ctxRobust = document.getElementById('robustnessChart')?.getContext('2d');
  if (ctxRobust) {
    new Chart(ctxRobust, {
      type: 'bar',
      data: {
        labels: [
          'ALT (Alternative Appeal)',
          'VAR (Product Variety)',
          'PROMO (Promotions/Pricing)',
          'SWEFFORT (Switching Effort)'
        ],
        datasets: [
          {
            label: 'Raw Spearman ρ',
            data: [0.685, 0.694, 0.700, 0.721],
            backgroundColor: '#3b82f6',
            borderRadius: 6,
            maxBarThickness: 28
          },
          {
            label: 'Within-Person Centered ρ',
            data: [-0.030, 0.100, 0.230, 0.050],
            backgroundColor: '#f43f5e',
            borderRadius: 6,
            maxBarThickness: 28
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            position: 'top',
            labels: { boxWidth: 12, padding: 12, font: { size: 12, weight: '600' } }
          },
          tooltip: {
            callbacks: {
              afterLabel: function(context) {
                const decays = [
                  'ALT: +0.685 -> -0.030 (Complete collapse / sign flip)',
                  'VAR: +0.694 -> +0.100 (85.6% attenuation)',
                  'PROMO: +0.700 -> +0.230 (67.1% attenuation, residual effect)',
                  'SWEFFORT: +0.721 -> +0.050 (93.1% collapse, confirms artifact)'
                ];
                return decays[context.dataIndex];
              }
            }
          }
        },
        scales: {
          y: {
            min: -0.15,
            max: 0.85,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return val.toFixed(2); },
              font: { size: 11 }
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // 5. Voluntary Reasons Chart (Class C, n=32)
  const ctxVoluntary = document.getElementById('voluntaryReasonsChart')?.getContext('2d');
  if (ctxVoluntary) {
    new Chart(ctxVoluntary, {
      type: 'bar',
      data: {
        labels: [
          'Frequent Out-of-Stock (Catalog)',
          'Limited Product Variety (Catalog)',
          'High Delivery Charges / Fees',
          'Higher Prices vs Rivals',
          'Slow Delivery / Service Delays',
          'App / Payment Glitches'
        ],
        datasets: [{
          label: 'Count (n)',
          data: [8, 8, 7, 4, 3, 2],
          backgroundColor: [
            '#d97706', // OOS (Catalog)
            '#d97706', // Variety (Catalog)
            '#3b82f6', // Delivery fees
            '#3b82f6', // Pricing
            '#64748b', // Speed
            '#94a3b8'  // App
          ],
          borderRadius: 6,
          maxBarThickness: 24
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
              afterLabel: function(context) {
                const pct = ((context.raw / 32) * 100).toFixed(1);
                return `${pct}% of voluntary leavers (n = 32). Catalog factors total 50.0%.`;
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            max: 10,
            grid: { color: '#f1f5f9' },
            ticks: { font: { size: 11 } }
          },
          y: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // 6. Competitor Advantage Chart (n=68)
  const ctxAdvantage = document.getElementById('competitorAdvantageChart')?.getContext('2d');
  if (ctxAdvantage) {
    new Chart(ctxAdvantage, {
      type: 'bar',
      data: {
        labels: [
          'Items Not Found on Zepto',
          'Better Discounts / Deals',
          'Lower / Zero Minimum Order',
          'Faster Delivery Speeds',
          'Better App Experience'
        ],
        datasets: [{
          label: 'Reported Advantage (%)',
          data: [60.3, 44.1, 32.4, 26.5, 20.6],
          backgroundColor: ['#7c3aed', '#0d9488', '#3b82f6', '#64748b', '#94a3b8'],
          borderRadius: 6,
          maxBarThickness: 24
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
              label: function(context) {
                return ` ${context.raw}% of former users surveyed (n = 68)`;
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            max: 70,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return val + '%'; },
              font: { size: 11 }
            }
          },
          y: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // UDRHP Tab Charts
  initUdrhpCharts();
}

let udrhpChartsInitialized = false;
function initUdrhpCharts() {
  if (udrhpChartsInitialized) return;
  udrhpChartsInitialized = true;

  // SKU Growth Chart
  const ctxSku = document.getElementById('udrhpSkuChart')?.getContext('2d');
  if (ctxSku) {
    new Chart(ctxSku, {
      type: 'bar',
      data: {
        labels: ['FY24', 'FY25', 'FY26', 'Q4 FY26'],
        datasets: [{
          label: 'Average SKUs per Dark Store',
          data: [12312, 44341, 46623, 49602],
          backgroundColor: '#0d9488',
          borderRadius: 6,
          maxBarThickness: 45
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) { return ` ${context.raw.toLocaleString()} SKUs`; }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 55000,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return (val / 1000) + 'k'; },
              font: { size: 11 }
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 12, weight: '500' } }
          }
        }
      }
    });
  }

  // Dark Store Count Chart
  const ctxStore = document.getElementById('udrhpStoreChart')?.getContext('2d');
  if (ctxStore) {
    new Chart(ctxStore, {
      type: 'bar',
      data: {
        labels: ['FY24 (31 Mar 24)', 'FY25 (31 Mar 25)', 'FY26 (31 Mar 26)'],
        datasets: [{
          label: 'Closing Operational Dark Stores',
          data: [337, 1029, 1139],
          backgroundColor: '#2563eb',
          borderRadius: 6,
          maxBarThickness: 50
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              afterLabel: function(context) {
                return context.dataIndex === 2 ? 'Active across 66 Indian cities' : '';
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 1300,
            grid: { color: '#f1f5f9' },
            ticks: { font: { size: 11 } }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 12, weight: '500' } }
          }
        }
      }
    });
  }

  // ATU Trajectory Chart
  const ctxAtu = document.getElementById('udrhpAtuChart')?.getContext('2d');
  if (ctxAtu) {
    new Chart(ctxAtu, {
      type: 'line',
      data: {
        labels: ['FY24 (31 Mar 24)', 'FY25 (31 Mar 25)', 'Q3 FY26 (31 Dec 25)', 'FY26 (31 Mar 26)'],
        datasets: [{
          label: 'Annual Transacting Users (Millions)',
          data: [10.57, 38.38, 49.54, 47.97],
          borderColor: '#7c3aed',
          backgroundColor: 'rgba(124, 58, 237, 0.1)',
          fill: true,
          tension: 0.3,
          pointRadius: 6,
          pointHoverRadius: 8,
          pointBackgroundColor: '#7c3aed'
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) { return ` ${context.raw} Million ATU`; },
              afterLabel: function(context) {
                if (context.dataIndex === 3) return 'Minor TTM dip while daily orders rose 28.6% QoQ';
                return '';
              }
            }
          }
        },
        scales: {
          y: {
            beginAtZero: true,
            max: 60,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return val + 'M'; },
              font: { size: 11 }
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // Retention Chart
  const ctxRet = document.getElementById('udrhpRetentionChart')?.getContext('2d');
  if (ctxRet) {
    new Chart(ctxRet, {
      type: 'bar',
      data: {
        labels: [
          'FY23 Q2 (Year 3 / Q12)',
          'FY23 Q2 (Quarter 15)',
          'FY23 Q3 (Quarter 14)',
          'FY24 Q1 (Quarter 9)'
        ],
        datasets: [{
          label: 'Cohort Retention Rate (%)',
          data: [45.2, 44.3, 48.1, 49.8],
          backgroundColor: '#059669',
          borderRadius: 6,
          maxBarThickness: 45
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: { display: false },
          tooltip: {
            callbacks: {
              label: function(context) { return ` ${context.raw}% active retention`; }
            }
          }
        },
        scales: {
          y: {
            min: 30,
            max: 60,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return val + '%'; },
              font: { size: 11 }
            }
          },
          x: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }

  // Capital Proceeds Allocation Chart
  const ctxCap = document.getElementById('udrhpCapitalChart')?.getContext('2d');
  if (ctxCap) {
    new Chart(ctxCap, {
      type: 'bar',
      data: {
        labels: [
          'Dark Store CapEx (~1,900 stores)',
          'Store Lease Rentals (thru FY30)',
          'Brand Building & Marketing',
          'Tech & ML Infrastructure'
        ],
        datasets: [{
          label: 'Allocated IPO Proceeds (₹ Millions)',
          data: [16289.75, 17349.41, 10000.00, 3200.00],
          backgroundColor: ['#2563eb', '#3b82f6', '#93c5fd', '#bfdbfe'],
          borderRadius: 6,
          maxBarThickness: 36
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
              label: function(context) {
                const cr = (context.raw / 10).toFixed(1);
                return ` ₹${context.raw.toLocaleString()} M (~₹${cr} Cr)`;
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true,
            max: 20000,
            grid: { color: '#f1f5f9' },
            ticks: {
              callback: function(val) { return '₹' + (val / 1000) + 'k M'; },
              font: { size: 11 }
            }
          },
          y: {
            grid: { display: false },
            ticks: { font: { size: 11, weight: '500' } }
          }
        }
      }
    });
  }
}

// UDRHP Tab Switching
function switchUdrhpTab(tabName) {
  const tabs = ['sku', 'network', 'atu', 'retention', 'capital'];
  tabs.forEach(t => {
    const el = document.getElementById(`tab-${t}`);
    if (el) el.style.display = (t === tabName) ? 'block' : 'none';
  });

  const buttons = document.querySelectorAll('.tab-btn');
  buttons.forEach(btn => {
    if (btn.getAttribute('onclick')?.includes(`'${tabName}'`)) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  // Re-trigger layout calculation for Chart.js
  window.dispatchEvent(new Event('resize'));
}

// Media Claim Filtering
function filterMediaClaims(filter) {
  const rows = document.querySelectorAll('#mediaTable tbody tr');
  const buttons = document.querySelectorAll('.filter-bar .filter-btn');

  buttons.forEach(btn => {
    if (btn.getAttribute('onclick')?.includes(`'${filter}'`)) {
      btn.classList.add('active');
    } else {
      btn.classList.remove('active');
    }
  });

  rows.forEach(row => {
    const status = row.getAttribute('data-status');
    if (filter === 'all' || status === filter) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}
