/* image-lightbox.js – click-to-expand images in lesson content */
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
    overlay.setAttribute('aria-label', 'Image viewer – press Escape or click to close');

    var img = document.createElement('img');
    img.className = 'lightbox-overlay__img';
    img.setAttribute('alt', '');
    overlay.appendChild(img);

    overlay.addEventListener('click', closeLightbox);
    document.body.appendChild(overlay);
    return overlay;
  }

  function openLightbox(src, alt) {
    var overlay = getOrCreateOverlay();
    var img = overlay.querySelector('img');
    img.src = src;
    img.alt = alt || '';
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    var overlay = document.getElementById(OVERLAY_ID);
    if (!overlay) return;
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
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
        openLightbox(img.src, img.alt);
      });
    });

    document.addEventListener('keydown', handleKeydown);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
