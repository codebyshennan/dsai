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
    var codeEl = pre.querySelector('code');
    if (codeEl) {
      var codeLineEls = codeEl.querySelectorAll('.code-line');
      if (codeLineEls.length > 0) return codeLineEls.length;
    }
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

  /**
   * Map a character offset in `root`'s aggregated text (tree order) to a text node + offset.
   */
  function findNodeAtOffset(root, offset) {
    var walk = 0;
    var tw = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    var textNode;
    while ((textNode = tw.nextNode())) {
      var len = textNode.nodeValue.length;
      if (walk + len >= offset) {
        return { node: textNode, offset: offset - walk };
      }
      walk += len;
    }
    return null;
  }

  /**
   * Half-open [start, end) character indices for logical lines startLine..endLine (1-based).
   * When `lineLengths` is provided (from `.code-line` spans, no \n in textContent),
   * offsets are computed from those lengths directly instead of splitting by \n.
   */
  function charRangeForLogicalLines(text, startLine, endLine, lineLengths) {
    if (lineLengths && lineLengths.length > 0) {
      var n2 = lineLengths.length;
      var s2 = Math.max(1, Math.min(startLine, n2));
      var e2 = Math.max(s2, Math.min(endLine, n2));
      var start2 = 0;
      for (var ii = 0; ii < s2 - 1; ii++) start2 += lineLengths[ii];
      var end2 = start2;
      for (var jj = s2 - 1; jj <= e2 - 1; jj++) end2 += lineLengths[jj];
      return { start: start2, end: end2 };
    }
    var lines = text.split(/\r\n|\r|\n/);
    var n = lines.length;
    if (n === 0) return null;
    var s = Math.max(1, Math.min(startLine, n));
    var e = Math.max(s, Math.min(endLine, n));
    var start = 0;
    var i;
    for (i = 0; i < s - 1; i++) {
      start += lines[i].length + 1;
    }
    var end = start;
    for (i = s - 1; i <= e - 1; i++) {
      end += lines[i].length;
      if (i < e - 1) {
        end += 1;
      }
    }
    return { start: start, end: end };
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

  /**
   * Place the highlight band using the real layout of the code (Rouge spans, wrapped lines).
   * Falls back to one line-height per logical line only if the Range API yields no box.
   */
  function applyHighlightGeometry(hl, container, pre, start, end) {
    var lineHeight = measureLineHeightPx(pre);
    var lineCount = lineCountFromPre(pre);
    var s = Math.max(1, Math.min(start, lineCount));
    var e = Math.max(s, Math.min(end, lineCount));

    var codeEl = pre.querySelector('code') || pre;
    var text = codeEl.textContent || '';
    var charRange = charRangeForLogicalLines(text, s, e);
    if (charRange && text.length > 0) {
      charRange.start = Math.max(0, Math.min(charRange.start, text.length));
      charRange.end = Math.max(charRange.start, Math.min(charRange.end, text.length));
    }
    var cr = container.getBoundingClientRect();
    var scrollTop = container.scrollTop || 0;
    var padTop = parseFloat(window.getComputedStyle(pre).paddingTop) || 0;

    if (charRange && charRange.end > charRange.start && document.createRange) {
      var startPos = findNodeAtOffset(codeEl, charRange.start);
      var endPos = findNodeAtOffset(codeEl, charRange.end);
      if (startPos && endPos) {
        try {
          var rng = document.createRange();
          rng.setStart(startPos.node, startPos.offset);
          rng.setEnd(endPos.node, endPos.offset);
          var rr = rng.getBoundingClientRect();
          if (rr.height > 0.5) {
            hl.style.top = rr.top - cr.top + scrollTop + 'px';
            hl.style.height = rr.height + 'px';
            return;
          }
        } catch (_e) {
          /* fall through */
        }
      }
    }

    /* Collapsed or empty range: at least one line-height so the band is visible */
    if (charRange && charRange.end <= charRange.start) {
      var probe = findNodeAtOffset(codeEl, charRange.start);
      if (probe && document.createRange) {
        try {
          var r2 = document.createRange();
          r2.setStart(probe.node, probe.offset);
          r2.setEnd(probe.node, Math.min(probe.offset + 1, probe.node.nodeValue.length));
          var r2b = r2.getBoundingClientRect();
          if (r2b.height > 0.5) {
            hl.style.top = r2b.top - cr.top + scrollTop + 'px';
            hl.style.height = Math.max(lineHeight, r2b.height) + 'px';
            return;
          }
        } catch (_e2) {
          /* fall through */
        }
      }
    }

    /* Legacy fallback: uniform line height (wrong when lines wrap) */
    var preRect = pre.getBoundingClientRect();
    hl.style.top = preRect.top - cr.top + scrollTop + padTop + (s - 1) * lineHeight + 'px';
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

    var shell =
      codeCol.querySelector('.code-block__body') ||
      codeCol.querySelector('.highlighter-rouge') ||
      codeCol.querySelector('figure.highlight');
    if (!shell) return;

    var pre = shell.querySelector('pre');
    if (!pre) return;

    // Overlay sits on the Rouge block so line bands align with code only (not the line-number gutter).
    // Use div.highlight (not .highlight) to avoid matching pre.highlight — appending a <div> inside
    // <pre> is invalid HTML and browsers eject it, breaking the position:relative coordinate system.
    var overlayParent = pre.closest('div.highlight, div.highlighter-rouge') || shell;

    // Mark inited only once language/copy chrome and body exist (see code-blocks.js).
    root.setAttribute('data-code-explainer-init', '1');

    if (window.getComputedStyle(overlayParent).position === 'static') {
      overlayParent.style.position = 'relative';
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

    var overlay = buildOverlay(overlayParent, pre, ranges);
    if (overlay.children.length) {
      overlayParent.appendChild(overlay);
    }

    var ro;
    if (window.ResizeObserver) {
      ro = new ResizeObserver(function () {
        relayout(overlayParent, pre, overlay);
      });
      ro.observe(pre);
      ro.observe(overlayParent);
    }

    window.addEventListener(
      'resize',
      function () {
        relayout(overlayParent, pre, overlay);
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
