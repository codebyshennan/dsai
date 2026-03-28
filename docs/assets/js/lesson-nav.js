(function () {
  'use strict';

  function init() {
    var wrap = document.getElementById('lesson-nav-dropdown');
    if (!wrap) return;
    var btn = wrap.querySelector('.lesson-nav__dropdown-btn');
    var list = document.getElementById('lesson-nav-list');
    if (!btn || !list) return;

    function open() {
      btn.setAttribute('aria-expanded', 'true');
      list.hidden = false;
      var cur = list.querySelector('.lesson-nav__dropdown-item--current a');
      if (cur) cur.scrollIntoView({ block: 'nearest' });
    }

    function close() {
      btn.setAttribute('aria-expanded', 'false');
      list.hidden = true;
    }

    btn.addEventListener('click', function () {
      btn.getAttribute('aria-expanded') === 'true' ? close() : open();
    });

    document.addEventListener('click', function (e) {
      if (!wrap.contains(e.target)) close();
    });

    wrap.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { close(); btn.focus(); }
    });
  }

  document.readyState === 'loading'
    ? document.addEventListener('DOMContentLoaded', init)
    : init();
})();
