/**
 * Zepto CRM Switching Research — Application Coordinator (app.js)
 * Coordinates modular scripts (sidebar.js, chart_manager.js, components.js, viva_mode.js)
 * Zero hard-coded statistics. Strict file:// compatibility.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    console.log('[Zepto Research Dashboard] Initialized cleanly under file:// protocol.');
    if (!window.SITE_DATA) {
      console.warn('[Zepto Research Dashboard] window.SITE_DATA not loaded. Check web/site_data.js.');
    }

    // Anchor & URL query parameter auto-scroll support
    var hash = window.location.hash;
    var params = new URLSearchParams(window.location.search);
    var targetSec = params.get('section') || (hash ? hash.replace('#', '') : null);
    if (targetSec) {
      setTimeout(function () {
        var el = document.getElementById(targetSec);
        if (el) el.scrollIntoView({ behavior: 'auto', block: 'start' });
      }, 80);
    }
  });

})();
