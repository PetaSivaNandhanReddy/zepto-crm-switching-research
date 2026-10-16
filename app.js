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
  });

})();
