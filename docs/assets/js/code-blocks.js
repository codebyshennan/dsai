/**
 * Wraps Rouge / GFM code blocks with a header (language label + copy) and optional
 * terminal / output styling. Idempotent: skips blocks inside [data-code-block].
 * Supports VS Code-style code folding: click the chevron in the gutter to collapse
 * a function/class/block body and show only its opening line.
 */
(function () {
  'use strict';

  var TERMINAL_LANGS = {
    bash: true,
    shell: true,
    sh: true,
    zsh: true,
    console: true,
    powershell: true,
    ps1: true,
    pwsh: true,
    cmd: true,
    fish: true,
    terminal: true,
  };

  var OUTPUT_LANGS = {
    output: true,
    stdout: true,
    stderr: true,
    'terminal-output': true,
    log: true,
  };

  var LANG_LABELS = {
    js: 'JavaScript',
    javascript: 'JavaScript',
    mjs: 'JavaScript',
    ts: 'TypeScript',
    tsx: 'TSX',
    jsx: 'JSX',
    py: 'Python',
    python: 'Python',
    rb: 'Ruby',
    rs: 'Rust',
    go: 'Go',
    sh: 'Shell',
    bash: 'Bash',
    zsh: 'Zsh',
    shell: 'Shell',
    yml: 'YAML',
    yaml: 'YAML',
    md: 'Markdown',
    html: 'HTML',
    css: 'CSS',
    scss: 'SCSS',
    sql: 'SQL',
    json: 'JSON',
    toml: 'TOML',
    xml: 'XML',
    console: 'Console',
    powershell: 'PowerShell',
    pwsh: 'PowerShell',
    text: 'Plain text',
    plaintext: 'Plain text',
    output: 'Output',
    stdout: 'Output',
    stderr: 'Output',
    'terminal-output': 'Output',
    log: 'Log',
    diff: 'Diff',
    dockerfile: 'Dockerfile',
    makefile: 'Makefile',
  };

  /**
   * Rouge often puts `language-*` on the outer `.highlighter-rouge` div, not on `<code>`.
   * Also check `data-lang` / walk a few ancestors for fenced-block language classes.
   */
  function extractLangFromClassAttr(classAttr) {
    if (!classAttr) return '';
    var m = String(classAttr).match(/(?:^|\s)language-([\w-]+)/);
    return m ? m[1].toLowerCase() : '';
  }

  function getLang(codeEl, rootEl) {
    var lang = extractLangFromClassAttr(codeEl.getAttribute('class'));
    if (lang) return lang;

    var dataLang = codeEl.getAttribute('data-lang') || codeEl.getAttribute('data-language');
    if (dataLang) return String(dataLang).toLowerCase().trim();

    var el;
    var depth;
    if (rootEl) {
      lang = extractLangFromClassAttr(rootEl.getAttribute('class'));
      if (lang) return lang;
      el = rootEl.parentElement;
      depth = 0;
      while (el && depth < 4) {
        lang = extractLangFromClassAttr(el.getAttribute('class'));
        if (lang) return lang;
        el = el.parentElement;
        depth += 1;
      }
    }
    return '';
  }

  function displayLabel(lang) {
    if (!lang) return 'Code';
    if (LANG_LABELS[lang]) return LANG_LABELS[lang];
    return lang.replace(/[-_]/g, ' ').replace(/\b\w/g, function (c) {
      return c.toUpperCase();
    });
  }

  /**
   * Split the `<code>` element's content into individual `.code-line` block spans,
   * one per logical line. Preserves Rouge syntax-highlight spans by cloning them.
   * After this call the code element contains only `.code-line` elements; its
   * textContent is the concatenation of all line texts (no \n separators).
   * Returns the array of `.code-line` elements.
   */
  function splitIntoLines(codeEl) {
    var lines = [];
    var pending = []; // nodes accumulating for the current line

    function flush() {
      var span = document.createElement('span');
      span.className = 'code-line';
      for (var k = 0; k < pending.length; k++) span.appendChild(pending[k]);
      lines.push(span);
      pending = [];
    }

    function walk(node) {
      if (node.nodeType === 3 /* TEXT_NODE */) {
        var parts = node.textContent.split('\n');
        for (var i = 0; i < parts.length; i++) {
          if (i > 0) flush();
          if (parts[i]) pending.push(document.createTextNode(parts[i]));
        }
      } else if (node.nodeType === 1 /* ELEMENT_NODE */) {
        // Rouge never puts \n inside highlight spans, so deep-clone is safe.
        pending.push(node.cloneNode(true));
      }
    }

    var children = Array.prototype.slice.call(codeEl.childNodes);
    for (var i = 0; i < children.length; i++) walk(children[i]);
    if (pending.length > 0) flush();

    // Drop trailing empty line (common trailing \n in Rouge output).
    while (lines.length > 0 && lines[lines.length - 1].textContent === '') {
      lines.pop();
    }

    // Replace the code element's children with the new line spans.
    while (codeEl.firstChild) codeEl.removeChild(codeEl.firstChild);
    for (var j = 0; j < lines.length; j++) codeEl.appendChild(lines[j]);

    return lines;
  }

  /**
   * Detect foldable regions in the line array.
   * A foldable region starts at a line whose trimmed content ends with `:` or `{`
   * and is followed by at least two lines with greater indentation.
   * Returns an array of { start, end } objects (0-based indices into `codeLines`).
   */
  function detectFoldRegions(codeLines) {
    var regions = [];
    var texts = [];
    for (var k = 0; k < codeLines.length; k++) {
      texts.push(codeLines[k].textContent);
    }
    var n = texts.length;

    function indentOf(s) {
      var m = s.match(/^([ \t]*)/);
      return m ? m[1].length : 0;
    }

    for (var i = 0; i < n - 1; i++) {
      var trimmed = texts[i].replace(/\s+$/, '');
      if (!trimmed || !/[:{]\s*$/.test(trimmed)) continue;

      var base = indentOf(texts[i]);
      var end = -1;

      for (var j = i + 1; j < n; j++) {
        if (!texts[j].trim()) continue; // blank lines don't end the region
        if (indentOf(texts[j]) > base) {
          end = j;
        } else {
          break;
        }
      }

      // Only create a fold if there are at least 2 lines to hide (otherwise not worth it).
      if (end >= i + 2) {
        regions.push({ start: i, end: end });
      }
    }

    return regions;
  }

  /**
   * Build the gutter column with line numbers and optional fold chevrons.
   * `foldRegions` is an array of { start, end } (0-based) from detectFoldRegions.
   * Returns { col, cells } where cells[i] is the line-number cell for codeLines[i].
   */
  function buildLineNumbersColumn(codeLines, foldRegions) {
    var n = codeLines.length;
    var digits = Math.max(2, String(n).length);
    var col = document.createElement('div');
    col.className = 'code-block__line-numbers';
    col.setAttribute('aria-hidden', 'true');
    // Extra ch for the fold chevron area.
    col.style.minWidth = digits + 3 + 'ch';

    var foldMap = {};
    for (var r = 0; r < foldRegions.length; r++) {
      foldMap[foldRegions[r].start] = foldRegions[r].end;
    }

    var cells = [];
    var frag = document.createDocumentFragment();
    for (var i = 0; i < n; i++) {
      var cell = document.createElement('span');
      cell.className = 'code-block__line-number';

      if (foldMap[i] !== undefined) {
        cell.classList.add('code-block__line-number--foldable');
        var chevron = document.createElement('button');
        chevron.type = 'button';
        chevron.className = 'code-fold-btn';
        chevron.setAttribute('aria-expanded', 'true');
        chevron.setAttribute('aria-label', 'Fold section');
        chevron.textContent = '▾';
        cell.appendChild(chevron);
      }

      var numSpan = document.createElement('span');
      numSpan.className = 'code-block__line-number-text';
      numSpan.textContent = String(i + 1);
      cell.appendChild(numSpan);

      cells.push(cell);
      frag.appendChild(cell);
    }
    col.appendChild(frag);
    return { col: col, cells: cells };
  }

  function findRoots() {
    var body = document.querySelector('.markdown-body');
    if (!body) return [];

    var seen = new Set();
    var out = [];

    body.querySelectorAll('.highlighter-rouge, figure.highlight').forEach(function (el) {
      if (el.closest('[data-code-block]')) return;
      if (seen.has(el)) return;
      seen.add(el);
      out.push(el);
    });

    if (out.length) return out;

    body.querySelectorAll('pre').forEach(function (pre) {
      if (pre.closest('[data-code-block]')) return;
      if (!pre.querySelector('code')) return;
      if (seen.has(pre)) return;
      seen.add(pre);
      out.push(pre);
    });

    return out;
  }

  function enhanceRoot(root) {
    var code = root.querySelector('code');
    if (!code) return;

    var lang = getLang(code, root);
    // Mermaid runs on the raw `<pre><code class="language-mermaid">` text; wrapping (line
    // numbers, copy chrome) can confuse some diagram parsers—leave blocks untouched.
    if (lang === 'mermaid') return;

    // Split code into line spans before building the wrapper so fold detection works.
    var codeLines = splitIntoLines(code);
    var isOutput = OUTPUT_LANGS[lang];
    var foldRegions = (!isOutput && codeLines.length >= 3) ? detectFoldRegions(codeLines) : [];

    var wrapper = document.createElement('div');
    wrapper.setAttribute('data-code-block', '');
    wrapper.className = 'code-block';

    if (TERMINAL_LANGS[lang]) wrapper.classList.add('code-block--terminal');
    if (isOutput) wrapper.classList.add('code-block--output');

    var header = document.createElement('div');
    header.className = 'code-block__header';

    var title = document.createElement('span');
    title.className = 'code-block__title';
    title.textContent = displayLabel(lang);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'code-block__copy';
    btn.setAttribute('aria-label', 'Copy code to clipboard');
    btn.textContent = 'Copy';

    header.appendChild(title);
    header.appendChild(btn);

    var inner = document.createElement('div');
    inner.className = 'code-block__body';

    var parent = root.parentNode;
    parent.insertBefore(wrapper, root);

    var gutterCol = null;
    var gutterCells = [];
    if (!isOutput) {
      var gutter = buildLineNumbersColumn(codeLines, foldRegions);
      gutterCol = gutter.col;
      gutterCells = gutter.cells;
      inner.appendChild(gutterCol);
    }
    inner.appendChild(root);
    wrapper.appendChild(header);
    wrapper.appendChild(inner);

    // Copy always includes the full source, even when some lines are folded.
    btn.addEventListener('click', function () {
      var text = '';
      for (var i = 0; i < codeLines.length; i++) {
        text += (i > 0 ? '\n' : '') + codeLines[i].textContent;
      }
      navigator.clipboard.writeText(text).then(
        function () {
          btn.textContent = 'Copied';
          btn.classList.add('is-copied');
          setTimeout(function () {
            btn.textContent = 'Copy';
            btn.classList.remove('is-copied');
          }, 2000);
        },
        function () {
          btn.textContent = 'Failed';
          setTimeout(function () {
            btn.textContent = 'Copy';
          }, 2000);
        }
      );
    });

    // Wire up fold chevrons.
    if (gutterCol && foldRegions.length > 0) {
      var chevrons = gutterCol.querySelectorAll('.code-fold-btn');
      for (var ri = 0; ri < chevrons.length; ri++) {
        (function (chevron, region) {
          chevron.addEventListener('click', function () {
            var expanded = chevron.getAttribute('aria-expanded') === 'true';
            var nowExpanded = !expanded;
            chevron.setAttribute('aria-expanded', String(nowExpanded));
            chevron.textContent = nowExpanded ? '▾' : '▸';
            chevron.setAttribute('aria-label', nowExpanded ? 'Fold section' : 'Unfold section');

            for (var i = region.start + 1; i <= region.end; i++) {
              codeLines[i].classList.toggle('code-line--hidden', !nowExpanded);
            }
            // Show/hide the "..." ellipsis appended after the opening line.
            codeLines[region.start].classList.toggle('code-line--fold-collapsed', !nowExpanded);
          });
        })(chevrons[ri], foldRegions[ri]);
      }
    }
  }

  function run() {
    findRoots().forEach(enhanceRoot);
    // Code explainers must run after every block is wrapped (header + copy + .code-block__body).
    if (typeof window.tamkeenInitCodeExplainers === 'function') {
      window.tamkeenInitCodeExplainers();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
