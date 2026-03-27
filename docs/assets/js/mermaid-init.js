/**
 * Mermaid 11+: render diagrams after DOM is ready (deferred load).
 */
(function () {
  'use strict';

  async function run() {
    var pres = document.querySelectorAll(
      'pre code.language-mermaid, pre code.language-mermaid diagram'
    );
    if (!pres.length) return;
    try {
      var mod = await import(
        'https://cdn.jsdelivr.net/npm/mermaid@11.4.0/dist/mermaid.esm.min.mjs'
      );
      var mermaid = mod.default;
      mermaid.initialize({
        startOnLoad: false,
        theme: 'forest',
        flowchart: { useMaxWidth: true, htmlLabels: true },
        securityLevel: 'loose',
      });
      var nodes = [];
      document.querySelectorAll('pre code.language-mermaid').forEach(function (code) {
        if (code.parentElement) nodes.push(code.parentElement);
      });
      if (nodes.length) await mermaid.run({ nodes: nodes });
    } catch (e) {
      console.warn('Mermaid failed to load or render', e);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
