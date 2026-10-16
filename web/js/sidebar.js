/**
 * Zepto CRM Switching Research — Sidebar Navigation & Stage Progress
 * Classic script (no ES modules, file:// compatible)
 */
(function () {
  'use strict';

  // Section to Research Stage mapping
  var STAGE_MAP = {
    'overview': { stage: 1, name: 'Stage 1: Inception & Context', progress: 10 },
    'design': { stage: 1, name: 'Stage 1: Methodology Pipeline', progress: 20 },
    'survey': { stage: 2, name: 'Stage 2: Survey Data & Cleaning', progress: 35 },
    'ppm': { stage: 3, name: 'Stage 3: PPM Construct Framework', progress: 48 },
    'hypothesis': { stage: 3, name: 'Stage 3: Hypothesis Testing Lab', progress: 60 },
    'statistics': { stage: 4, name: 'Stage 4: Regression & Robustness', progress: 72 },
    'former': { stage: 4, name: 'Stage 4: Exit & Non-Adoption', progress: 82 },
    'udrhp': { stage: 5, name: 'Stage 5: Regulatory Evidence (UDRHP)', progress: 90 },
    'triangulation': { stage: 5, name: 'Stage 5: Evidence Triangulation', progress: 95 },
    'recommendations': { stage: 5, name: 'Stage 5: Evidence-Based CRM', progress: 100 }
  };

  function initScrollProgress() {
    var progressBar = document.getElementById('scroll-progress-line');
    if (!progressBar) return;

    window.addEventListener('scroll', function () {
      var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      progressBar.style.width = scrolled + '%';
    }, { passive: true });
  }

  function initScrollSpy() {
    var sections = document.querySelectorAll('.dashboard-section[id]');
    var navLinks = document.querySelectorAll('.sidebar-nav .nav-link');
    var stageNameEl = document.getElementById('stage-name');
    var stageFillEl = document.getElementById('stage-bar-fill');
    var stageStepEl = document.getElementById('stage-step-num');

    if (!sections.length || !navLinks.length) return;

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var id = entry.target.id;
          window.AppState.activeSection = id;

          // Update active link
          navLinks.forEach(function (link) {
            var href = link.getAttribute('href');
            if (href === '#' + id) {
              link.classList.add('active');
              link.setAttribute('aria-current', 'true');
            } else {
              link.classList.remove('active');
              link.removeAttribute('aria-current');
            }
          });

          // Update stage progress
          var stageInfo = STAGE_MAP[id] || { stage: 1, name: 'Stage 1: Overview', progress: 10 };
          if (stageNameEl) stageNameEl.textContent = stageInfo.name;
          if (stageFillEl) stageFillEl.style.width = stageInfo.progress + '%';
          if (stageStepEl) stageStepEl.textContent = stageInfo.stage + '/5';
        }
      });
    }, {
      rootMargin: '-15% 0px -75% 0px',
      threshold: 0
    });

    sections.forEach(function (sec) {
      observer.observe(sec);
    });
  }

  function initMobileMenu() {
    var toggleBtn = document.getElementById('mobile-menu-btn');
    var sidebar = document.getElementById('app-sidebar');
    if (!toggleBtn || !sidebar) return;

    toggleBtn.addEventListener('click', function () {
      var isOpen = sidebar.classList.toggle('open');
      toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close on nav link click in mobile
    sidebar.addEventListener('click', function (e) {
      if (e.target.closest('.nav-link') && window.innerWidth <= 960) {
        sidebar.classList.remove('open');
        toggleBtn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    initScrollProgress();
    initScrollSpy();
    initMobileMenu();
  });

})();
