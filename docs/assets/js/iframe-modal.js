/* iframe-modal.js — adds an "Expand" button to interactive simulation iframes
 * and opens them in a fullscreen modal on click.
 *
 * Auto-applies to any <iframe> whose src contains "/interactive/" or that has
 * the attribute data-modal="on". Skips iframes with data-modal="off".
 */
(function () {
  'use strict';

  var MODAL_ID = 'tamkeen-iframe-modal';
  var EXPAND_SVG =
    '<svg viewBox="0 0 24 24" aria-hidden="true">' +
    '<path d="M4 4h6v2H6v4H4V4zm10 0h6v6h-2V6h-4V4zM4 14h2v4h4v2H4v-6zm14 0h2v6h-6v-2h4v-4z"/>' +
    '</svg>';

  function shouldEnhance(iframe) {
    var optOut = iframe.getAttribute('data-modal') === 'off';
    if (optOut) return false;
    var optIn = iframe.getAttribute('data-modal') === 'on';
    if (optIn) return true;
    var src = iframe.getAttribute('src') || '';
    return src.indexOf('/interactive/') !== -1;
  }

  function getOrCreateModal() {
    var existing = document.getElementById(MODAL_ID);
    if (existing) return existing;

    var modal = document.createElement('div');
    modal.id = MODAL_ID;
    modal.className = 'iframe-modal';
    modal.setAttribute('role', 'dialog');
    modal.setAttribute('aria-modal', 'true');
    modal.setAttribute('aria-label', 'Interactive simulation — press Escape to close');

    var frame = document.createElement('iframe');
    frame.className = 'iframe-modal__frame';
    frame.setAttribute('title', 'Expanded simulation');
    frame.setAttribute('loading', 'lazy');
    modal.appendChild(frame);

    var closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.className = 'iframe-modal__close';
    closeBtn.setAttribute('aria-label', 'Close');
    closeBtn.innerHTML = '×';
    closeBtn.addEventListener('click', closeModal);
    modal.appendChild(closeBtn);

    var hint = document.createElement('div');
    hint.className = 'iframe-modal__hint';
    hint.textContent = 'Click outside or press Esc to close';
    modal.appendChild(hint);

    // Close when clicking the backdrop (but not the iframe itself)
    modal.addEventListener('click', function (e) {
      if (e.target === modal) closeModal();
    });

    document.body.appendChild(modal);
    return modal;
  }

  function openModal(src, title) {
    var modal = getOrCreateModal();
    var frame = modal.querySelector('.iframe-modal__frame');
    // Reload the src each time — keeps the modal frame in sync with whatever
    // state the inline frame has (Plotly resets to defaults, which is fine).
    frame.src = src;
    if (title) frame.setAttribute('title', title);
    modal.classList.add('is-open');
    document.body.style.overflow = 'hidden';
    // Move focus into the modal for keyboard users
    var closeBtn = modal.querySelector('.iframe-modal__close');
    if (closeBtn) closeBtn.focus();
  }

  function closeModal() {
    var modal = document.getElementById(MODAL_ID);
    if (!modal) return;
    modal.classList.remove('is-open');
    document.body.style.overflow = '';
    var frame = modal.querySelector('.iframe-modal__frame');
    if (frame) frame.src = 'about:blank'; // free the resource
  }

  function enhanceIframe(iframe) {
    if (iframe.dataset.iframeModalReady === '1') return;
    iframe.dataset.iframeModalReady = '1';

    // Wrap the iframe so we can absolute-position the button
    var wrapper = document.createElement('div');
    wrapper.className = 'iframe-expand';
    iframe.parentNode.insertBefore(wrapper, iframe);
    wrapper.appendChild(iframe);

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'iframe-expand__button';
    btn.setAttribute('aria-label', 'Expand simulation to fullscreen');
    btn.innerHTML = EXPAND_SVG + '<span>Expand</span>';
    btn.addEventListener('click', function () {
      openModal(iframe.getAttribute('src'), iframe.getAttribute('title'));
    });
    wrapper.appendChild(btn);
  }

  function init() {
    var iframes = document.querySelectorAll('iframe');
    for (var i = 0; i < iframes.length; i++) {
      if (shouldEnhance(iframes[i])) enhanceIframe(iframes[i]);
    }

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        var modal = document.getElementById(MODAL_ID);
        if (modal && modal.classList.contains('is-open')) closeModal();
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
