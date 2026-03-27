/**
 * KaTeX auto-render for lesson article only. Delimiters: $$, \\[\\], \\(\\).
 * Skips $ single delimiter to avoid false positives in prose.
 */
(function () {
  'use strict';

  function run() {
    if (typeof renderMathInElement === 'undefined') return;
    var el = document.getElementById('lesson-article');
    if (!el) return;
    renderMathInElement(el, {
      delimiters: [
        { left: '$$', right: '$$', display: true },
        { left: '\\[', right: '\\]', display: true },
        { left: '\\(', right: '\\)', display: false },
      ],
      ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
      strict: false,
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
