/**
 * Side-by-side code + callouts: highlights line ranges on the code block and
 * links them to notes (hover sync). Expects `.code-block` from code-blocks.js.
 */
(function () {
  'use strict';

  function parseLines(attr) {
    if (!attr || !String(attr).trim()) return null;
    var s = String(attr).trim();
    var range = s.match(/^(\d+)\s*-\s*(\d+)$/);
    if (range) {
      return { start: parseInt(range[1], 10), end: parseInt(range[2], 10) };
    }
    var one = s.match(/^(\d+)$/);
    if (one) {
      var n = parseInt(one[1], 10);
      return { start: n, end: n };
    }
    return null;
  }

  function lineCountFromPre(pre) {
    var t = pre.textContent || '';
    if (!t) return 0;
    return t.split(/\r\n|\r|\n/).length;
  }

  function measureLineHeightPx(pre) {
    var st = window.getComputedStyle(pre);
    var lh = st.lineHeight;
    var fs = parseFloat(st.fontSize) || 13;
    if (!lh || lh === 'normal') {
      return fs * 1.55;
    }
    var px = parseFloat(lh);
    return isNaN(px) ? fs * 1.55 : px;
  }

  function offsetWithin(el, ancestor) {
    var y = 0;
    var n = el;
    while (n && n !== ancestor) {
      y += n.offsetTop;
      n = n.parentElement;
    }
    return y;
  }

  function formatLineLabel(range) {
    if (!range) return '';
    if (range.start === range.end) return 'Line ' + range.start;
    return 'Lines ' + range.start + '–' + range.end;
  }

  function ensureLineLabel(callout, range) {
    var meta = callout.querySelector('.code-callout__lines');
    if (meta && range && !meta.textContent.trim()) {
      meta.textContent = formatLineLabel(range);
    }
  }

  function applyHighlightGeometry(hl, container, pre, start, end) {
    var preTop = offsetWithin(pre, container);
    var padTop = parseFloat(window.getComputedStyle(pre).paddingTop) || 0;
    var lineHeight = measureLineHeightPx(pre);
    var lineCount = lineCountFromPre(pre);

    var s = Math.max(1, Math.min(start, lineCount));
    var e = Math.max(s, Math.min(end, lineCount));

    hl.style.top = preTop + padTop + (s - 1) * lineHeight + 'px';
    hl.style.height = (e - s + 1) * lineHeight + 'px';
  }

  function buildOverlay(container, pre, ranges) {
    var overlay = document.createElement('div');
    overlay.className = 'code-explainer__highlights';
    overlay.setAttribute('aria-hidden', 'true');

    ranges.forEach(function (item) {
      var range = item.range;
      var tint = item.tint;
      var idx = item.index;
      if (!range) return;

      var hl = document.createElement('div');
      hl.className =
        'code-explainer__line-highlight code-explainer__line-highlight--tint-' + tint;
      hl.dataset.calloutIndex = String(idx);
      hl.dataset.startLine = String(range.start);
      hl.dataset.endLine = String(range.end);

      applyHighlightGeometry(hl, container, pre, range.start, range.end);

      overlay.appendChild(hl);

      item.el.dataset.calloutIndex = String(idx);

      item.el.addEventListener('mouseenter', function () {
        hl.classList.add('is-active');
      });
      item.el.addEventListener('mouseleave', function () {
        hl.classList.remove('is-active');
      });
    });

    return overlay;
  }

  function relayout(container, pre, overlay) {
    if (!overlay || !overlay.parentNode) return;

    overlay.querySelectorAll('.code-explainer__line-highlight').forEach(function (hl) {
      var start = parseInt(hl.dataset.startLine || '1', 10);
      var end = parseInt(hl.dataset.endLine || String(start), 10);
      applyHighlightGeometry(hl, container, pre, start, end);
    });
  }

  function initExplainer(root) {
    if (root.getAttribute('data-code-explainer-init') === '1') return;

    var codeCol = root.querySelector('.code-explainer__code');
    if (!codeCol) return;

    var container =
      codeCol.querySelector('.code-block__body') || codeCol.querySelector('.highlighter-rouge');
    if (!container) return;

    var pre = container.querySelector('pre');
    if (!pre) return;

    // Mark inited only once language/copy chrome and body exist (see code-blocks.js).
    root.setAttribute('data-code-explainer-init', '1');

    if (window.getComputedStyle(container).position === 'static') {
      container.style.position = 'relative';
    }

    var calloutEls = root.querySelectorAll('.code-explainer__callouts .code-callout');
    var ranges = [];
    calloutEls.forEach(function (callout, idx) {
      var range = parseLines(callout.getAttribute('data-lines') || '');
      var tint = parseInt(callout.getAttribute('data-tint') || String((idx % 4) + 1), 10);
      if (tint < 1 || tint > 4) tint = (idx % 4) + 1;
      ensureLineLabel(callout, range);
      ranges.push({ el: callout, range: range, tint: tint, index: idx });
    });

    var hasHighlights = ranges.some(function (r) {
      return r.range !== null;
    });
    if (!hasHighlights) return;

    var overlay = buildOverlay(container, pre, ranges);
    if (overlay.children.length) {
      container.appendChild(overlay);
    }

    var ro;
    if (window.ResizeObserver) {
      ro = new ResizeObserver(function () {
        relayout(container, pre, overlay);
      });
      ro.observe(pre);
      ro.observe(container);
    }

    window.addEventListener(
      'resize',
      function () {
        relayout(container, pre, overlay);
      },
      { passive: true }
    );
  }

  function run() {
    var body = document.querySelector('.markdown-body');
    if (!body) return;
    body.querySelectorAll('.code-explainer').forEach(initExplainer);
  }

  /**
   * Exposed for code-blocks.js: must run after `.code-block` wrappers exist so the language bar,
   * copy button, and `.code-block__body` are present and line overlays align to the `pre`.
   */
  window.tamkeenInitCodeExplainers = function () {
    if (typeof requestAnimationFrame === 'function') {
      requestAnimationFrame(run);
    } else {
      setTimeout(run, 0);
    }
  };

  // If the first pass ran before highlight markup was ready, retry once after full load.
  window.addEventListener('load', function () {
    var body = document.querySelector('.markdown-body');
    if (!body) return;
    var pending = false;
    body.querySelectorAll('.code-explainer').forEach(function (el) {
      if (el.getAttribute('data-code-explainer-init') !== '1') pending = true;
    });
    if (pending) {
      run();
    }
  });
})();
