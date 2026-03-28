/**
 * Wraps lesson tables in .table-scroll for horizontal overflow and consistent chrome.
 */
(function () {
  'use strict';

  function isNestedInTable(table) {
    var el = table.parentElement;
    while (el) {
      if (el.tagName === 'TABLE') return true;
      el = el.parentElement;
    }
    return false;
  }

  function wrapTables() {
    var article = document.getElementById('lesson-article');
    if (!article) return;

    var tables = article.querySelectorAll('table');
    for (var i = 0; i < tables.length; i++) {
      var table = tables[i];
      if (table.closest('.table-scroll')) continue;
      if (table.closest('.highlight, .code-block')) continue;
      if (isNestedInTable(table)) continue;

      var wrap = document.createElement('div');
      wrap.className = 'table-scroll';
      wrap.setAttribute('role', 'region');
      wrap.setAttribute('aria-label', 'Scrollable table');
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', wrapTables);
  } else {
    wrapTables();
  }
})();
