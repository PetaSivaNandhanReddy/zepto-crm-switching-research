/**
 * Zepto CRM Switching Research — Application State & Utilities
 * Classic script (no ES modules, file:// compatible)
 */
(function () {
  'use strict';

  window.AppState = {
    activeSection: 'overview',
    currentStage: 1,
    vivaActive: false,
    vivaStep: 0,
    filters: {
      hypothesisPpm: 'all',
      evidenceConstruct: 'all',
      mediaStatus: 'all'
    },
    
    // Check data integrity
    hasData: function () {
      return Boolean(window.SITE_DATA && window.SITE_DATA.metadata);
    },

    // Format numbers safely
    formatNumber: function (num, decimals) {
      if (num === null || num === undefined || isNaN(num)) return 'n/a';
      return Number(num).toLocaleString(undefined, {
        minimumFractionDigits: decimals || 0,
        maximumFractionDigits: decimals || 0
      });
    },

    formatCoeff: function (val, decimals) {
      if (val === null || val === undefined || isNaN(val)) return 'n/a';
      var d = decimals !== undefined ? decimals : 3;
      var num = Number(val);
      var sign = num > 0 ? '+' : '';
      return sign + num.toFixed(d);
    },

    formatP: function (p) {
      if (p === null || p === undefined || isNaN(p)) return 'n/a';
      var num = Number(p);
      if (num < 0.0001) return '< 0.0001';
      return num.toFixed(4);
    }
  };

})();
