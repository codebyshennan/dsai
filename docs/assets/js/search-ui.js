/**
 * Pagefind UI (global PagefindUI from pagefind-ui.js). Loads script on first open.
 */
(function () {
  'use strict';

  var dialog = document.getElementById('site-search-dialog');
  var openBtn = document.getElementById('site-search-open');
  var closeBtn = document.getElementById('site-search-close');
  var backdrop = document.getElementById('site-search-backdrop');
  var hint = document.getElementById('pagefind-unavailable');
  var uiStarted = false;
  var scriptRequested = false;

  function ensurePagefindCss() {
    if (document.querySelector('link[data-tamkeen-pagefind-css]')) return;
    var href = document.body && document.body.getAttribute('data-pagefind-css');
    if (!href) return;
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = href;
    link.setAttribute('data-tamkeen-pagefind-css', '1');
    document.head.appendChild(link);
  }

  function showHint() {
    if (hint) hint.hidden = false;
  }

  function initPagefind() {
    if (uiStarted) return;
    var PF = window.PagefindUI;
    if (typeof PF !== 'function') {
      showHint();
      return;
    }
    uiStarted = true;
    try {
      var bundle = document.body.getAttribute('data-pagefind-bundle') || '/pagefind/';
      new PF({
        element: '#pagefind-ui-root',
        bundlePath: bundle,
        showSubResults: true,
        showImages: false,
        autofocus: true,
        resetStyles: false,
      });
    } catch (e) {
      uiStarted = false;
      showHint();
    }
  }

  function loadScript(cb) {
    ensurePagefindCss();
    if (window.PagefindUI) {
      initPagefind();
      if (cb) cb();
      return;
    }
    if (scriptRequested) return;
    var src = document.body.getAttribute('data-pagefind-ui');
    if (!src) {
      showHint();
      return;
    }
    scriptRequested = true;
    var s = document.createElement('script');
    s.src = src;
    s.async = true;
    s.setAttribute('data-tamkeen-pagefind', '1');
    s.onload = function () {
      initPagefind();
      if (cb) cb();
    };
    s.onerror = function () {
      scriptRequested = false;
      showHint();
    };
    document.head.appendChild(s);
  }

  function open() {
    if (!dialog) return;
    ensurePagefindCss();
    dialog.hidden = false;
    document.body.classList.add('site-search-open');
    if (window.PagefindUI) {
      initPagefind();
    } else {
      loadScript(function () {
        var input = dialog.querySelector('.pagefind-ui__search-input');
        if (input) input.focus();
      });
    }
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    if (!dialog) return;
    dialog.hidden = true;
    document.body.classList.remove('site-search-open');
    if (openBtn) openBtn.focus();
  }

  if (openBtn) openBtn.addEventListener('click', open);
  if (closeBtn) closeBtn.addEventListener('click', close);
  if (backdrop) backdrop.addEventListener('click', close);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && dialog && !dialog.hidden) close();
  });
})();
