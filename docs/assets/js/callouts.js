/**
 * Annotates blockquotes whose first bold label matches a known pattern with
 * data-callout-type + callout--typed so CSS can show tinted accents and icons.
 * CommonMark does not support attributes on blockquotes; this runs client-side.
 */
(function () {
  function getMarkdownBody(container) {
    if (!container) return null;
    if (container.classList && container.classList.contains('markdown-body')) {
      return container;
    }
    return container.querySelector('.markdown-body');
  }

  var root = document.getElementById('lesson-article');
  if (!root) return;
  var md = getMarkdownBody(root);
  if (!md) return;

  var matchers = [
    /* Specific labels before generic Note:/Tip: */
    {
      type: 'figure',
      test: function (s) {
        return /^on screen\s*:/i.test(s);
      },
    },
    {
      type: 'note',
      test: function (s) {
        return /^note\s+for\s+beginners\s*:/i.test(s);
      },
    },
    {
      type: 'tip',
      test: function (s) {
        return /^tip\s+for\s+beginners\s*:/i.test(s);
      },
    },
    {
      type: 'warning',
      test: function (s) {
        return /^troubleshooting\s*:/i.test(s);
      },
    },
    { type: 'warning', test: function (s) { return /^warning\s*:/i.test(s); } },
    { type: 'important', test: function (s) { return /^important\s*:/i.test(s); } },
    { type: 'note', test: function (s) { return /^note\s*:/i.test(s); } },
    { type: 'tip', test: function (s) { return /^tip\s*:/i.test(s); } },
    { type: 'time', test: function (s) { return /^time needed\s*:/i.test(s); } },
    {
      type: 'figure',
      test: function (s) {
        return /^figure\s*\(/i.test(s) || /^figure\s*:/i.test(s);
      },
    },
    { type: 'takeaway', test: function (s) { return /^takeaway\s*:/i.test(s); } },
    {
      type: 'teacher',
      test: function (s) {
        return /^teacher'?s\s+note\s*:?/i.test(s);
      },
    },
    {
      type: 'example',
      test: function (s) {
        return /^real[-\s]world\s+example\s*:/i.test(s);
      },
    },
    { type: 'best-practice', test: function (s) { return /^best practice\s*:/i.test(s); } },
    { type: 'reflect', test: function (s) { return /^reflect\s*:/i.test(s); } },
    { type: 'pitfall', test: function (s) { return /^common pitfall\s*:/i.test(s); } },
  ];

  function firstLabelText(bq) {
    var p = bq.querySelector('p');
    if (!p) return '';
    var strong = p.querySelector('strong');
    if (strong) return strong.textContent.trim();
    return p.textContent.trim().slice(0, 160);
  }

  function detectType(label) {
    for (var i = 0; i < matchers.length; i++) {
      if (matchers[i].test(label)) return matchers[i].type;
    }
    return null;
  }

  var bqs = md.querySelectorAll('blockquote');
  for (var j = 0; j < bqs.length; j++) {
    var bq = bqs[j];
    if (bq.hasAttribute('data-callout-type')) continue;
    if (bq.closest('.code-explainer')) continue;
    var t = detectType(firstLabelText(bq));
    if (!t) continue;
    bq.setAttribute('data-callout-type', t);
    bq.classList.add('callout--typed');
    if (!bq.getAttribute('role')) bq.setAttribute('role', 'note');
  }

  /**
   * Wrap the "Gotchas" h2 and its following siblings up to the next h2 in
   * <section.lesson-section--gotchas> (0-prep README). Requires md above.
   */
  function wrapGotchasSection() {
    var h2s = md.querySelectorAll('h2');
    var start = null;
    for (var k = 0; k < h2s.length; k++) {
      if (h2s[k].textContent.trim() === 'Gotchas') {
        start = h2s[k];
        break;
      }
    }
    if (!start || start.closest('.lesson-section--gotchas')) return;

    if (!start.id) start.id = 'gotchas';

    var nodes = [];
    var el = start;
    while (el) {
      nodes.push(el);
      var next = el.nextElementSibling;
      if (next && next.tagName === 'H2') break;
      el = next;
    }

    var section = document.createElement('section');
    section.className = 'lesson-section lesson-section--gotchas';
    section.setAttribute('aria-labelledby', start.id);

    var parent = start.parentNode;
    parent.insertBefore(section, start);
    for (var n = 0; n < nodes.length; n++) {
      section.appendChild(nodes[n]);
    }
  }

  wrapGotchasSection();
})();
