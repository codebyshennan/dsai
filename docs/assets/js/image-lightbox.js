/* image-lightbox.js – click-to-expand images and Mermaid diagrams in lesson content */
(function () {
  'use strict';

  var OVERLAY_ID = 'tamkeen-lightbox';

  function getOrCreateOverlay() {
    var existing = document.getElementById(OVERLAY_ID);
    if (existing) return existing;

    var overlay = document.createElement('div');
    overlay.id = OVERLAY_ID;
    overlay.className = 'lightbox-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Viewer – press Escape or click to close');

    var img = document.createElement('img');
    img.className = 'lightbox-overlay__img';
    img.setAttribute('alt', '');
    overlay.appendChild(img);

    var svgWrap = document.createElement('div');
    svgWrap.className = 'lightbox-overlay__svg-wrap';
    overlay.appendChild(svgWrap);

    overlay.addEventListener('click', closeLightbox);
    document.body.appendChild(overlay);
    return overlay;
  }

  function openLightbox(src, alt) {
    var overlay = getOrCreateOverlay();
    var img = overlay.querySelector('img');
    var svgWrap = overlay.querySelector('.lightbox-overlay__svg-wrap');
    img.src = src;
    img.alt = alt || '';
    img.style.display = '';
    svgWrap.style.display = 'none';
    svgWrap.innerHTML = '';
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function openSvgLightbox(containerEl) {
    var svgEl = containerEl.querySelector('svg');
    if (!svgEl) return;
    try {
      var clone = svgEl.cloneNode(true);
      // Inject white background so the diagram is readable on any overlay colour
      var bg = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      bg.setAttribute('width', '100%');
      bg.setAttribute('height', '100%');
      bg.setAttribute('fill', '#ffffff');
      clone.insertBefore(bg, clone.firstChild);
      var svgData = new XMLSerializer().serializeToString(clone);
      var b64 = btoa(unescape(encodeURIComponent(svgData)));
      openLightbox('data:image/svg+xml;base64,' + b64, 'Diagram');
    } catch (e) {
      console.warn('Lightbox SVG serialization failed:', e);
    }
  }

  function closeLightbox() {
    var overlay = document.getElementById(OVERLAY_ID);
    if (!overlay) return;
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
    var svgWrap = overlay.querySelector('.lightbox-overlay__svg-wrap');
    if (svgWrap) {
      svgWrap.style.display = 'none';
      svgWrap.innerHTML = '';
    }
    var img = overlay.querySelector('img');
    if (img) img.style.display = '';
  }

  function handleKeydown(e) {
    if (e.key === 'Escape') closeLightbox();
  }

  function init() {
    var content = document.querySelector('.markdown-body');
    if (!content) return;

    content.querySelectorAll('img').forEach(function (img) {
      // Skip images that are already a link – those navigate on click
      if (img.closest('a')) return;
      img.addEventListener('click', function () {
        // Skip broken / not-yet-loaded images
        if (!img.complete || img.naturalWidth === 0) return;
        openLightbox(img.src, img.alt);
      });
    });

    document.addEventListener('keydown', handleKeydown);
  }

  // Expose openSvgLightbox for mermaid-init.js to call after async rendering
  window.tamkeenLightbox = { openSvg: openSvgLightbox };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
