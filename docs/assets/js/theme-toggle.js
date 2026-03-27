/**
 * Light / dark theme: prefers-color-scheme, localStorage, toggle button.
 */
(function () {
  'use strict';

  var STORAGE_KEY = 'tamkeen-theme';

  function getStored() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (e) {
      return null;
    }
  }

  function setStored(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (e) {}
  }

  function resolve() {
    var s = getStored();
    if (s === 'light' || s === 'dark') return s;
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)
      return 'dark';
    return 'light';
  }

  function apply(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    var meta = document.querySelector('meta[name="theme-color"]');
    if (meta) {
      meta.setAttribute('content', theme === 'dark' ? '#0d1117' : '#ffffff');
    }
    document.documentElement.style.colorScheme = theme === 'dark' ? 'dark' : 'light';
  }

  function toggle() {
    var cur = document.documentElement.getAttribute('data-theme') || resolve();
    var next = cur === 'dark' ? 'light' : 'dark';
    apply(next);
    setStored(next);
  }

  function init() {
    apply(resolve());

    var btn = document.getElementById('theme-toggle');
    if (btn) btn.addEventListener('click', toggle);

    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        if (!getStored()) apply(resolve());
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
