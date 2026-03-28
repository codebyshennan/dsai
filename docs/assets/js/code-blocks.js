/**
 * Wraps Rouge / GFM code blocks with a header (language label + copy) and optional
 * terminal / output styling. Idempotent: skips blocks inside [data-code-block].
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
   * Gutter column with 1..n — matches logical lines in `code` (same rules as code-explainer).
   * Skipped for output/log blocks where line refs are usually noise.
   */
  function buildLineNumbersColumn(codeEl) {
    var text = codeEl.textContent || '';
    var lines = text.split(/\r\n|\r|\n/);
    var col = document.createElement('div');
    var digits = Math.max(2, String(lines.length).length);
    var frag = document.createDocumentFragment();
    var i;
    var span;

    col.className = 'code-block__line-numbers';
    col.setAttribute('aria-hidden', 'true');
    col.style.minWidth = digits + 1 + 'ch';

    for (i = 0; i < lines.length; i += 1) {
      span = document.createElement('span');
      span.className = 'code-block__line-number';
      span.textContent = String(i + 1);
      frag.appendChild(span);
    }
    col.appendChild(frag);
    return col;
  }

  function findRoots() {
    var body = document.querySelector('.markdown-body');
    if (!body) return [];

    var seen = new Set();
    var out = [];

    body.querySelectorAll('.highlighter-rouge').forEach(function (el) {
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
    var wrapper = document.createElement('div');
    wrapper.setAttribute('data-code-block', '');
    wrapper.className = 'code-block';

    if (TERMINAL_LANGS[lang]) wrapper.classList.add('code-block--terminal');
    if (OUTPUT_LANGS[lang]) wrapper.classList.add('code-block--output');

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
    if (!OUTPUT_LANGS[lang]) {
      inner.appendChild(buildLineNumbersColumn(code));
    }
    inner.appendChild(root);
    wrapper.appendChild(header);
    wrapper.appendChild(inner);

    btn.addEventListener('click', function () {
      var text = code.textContent || '';
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
