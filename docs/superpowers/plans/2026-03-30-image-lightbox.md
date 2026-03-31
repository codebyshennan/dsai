# Image Lightbox Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Allow users to click any inline image in a lesson to expand it fullscreen with a dark translucent overlay; clicking anywhere or pressing Escape closes it.

**Architecture:** A self-contained vanilla-JS IIFE (`image-lightbox.js`) attaches click handlers to all `img` elements inside `.markdown-body` that are not already wrapped in an `<a>` tag. It creates a single overlay `<div>` lazily on first open and toggles an `is-open` class. Styles live in a dedicated `lightbox.css` loaded in `<head>`. Both files follow existing site conventions (IIFE pattern, separate CSS file per feature, `defer` scripts).

**Tech Stack:** Vanilla JS (ES5-compatible IIFE), plain CSS, Jekyll Liquid for wiring into `_layouts/default.html`.

---

## File Map

| Action | Path | Responsibility |
|--------|------|----------------|
| Create | `assets/css/lightbox.css` | All lightbox visual styles |
| Create | `assets/js/image-lightbox.js` | Overlay creation, open/close logic, event binding |
| Modify | `_layouts/default.html:29` | Add `<link>` for `lightbox.css` after `callouts.css` |
| Modify | `_layouts/default.html:84` | Add `<script>` for `image-lightbox.js` after `search-ui.js` |

---

### Task 1: Write lightbox CSS

**Files:**
- Create: `assets/css/lightbox.css`

- [ ] **Step 1: Create the CSS file**

```css
/* ─── Lightbox ────────────────────────────────────────────────────── */

/* Clickable images inside lesson content */
.markdown-body img:not(a img) {
  cursor: zoom-in;
}

/* Full-screen overlay */
.lightbox-overlay {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.85);
  z-index: 9000;
  cursor: zoom-out;
  align-items: center;
  justify-content: center;
}

.lightbox-overlay.is-open {
  display: flex;
}

/* Expanded image */
.lightbox-overlay__img {
  max-width: 90vw;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 8px 40px rgba(0, 0, 0, 0.6);
  /* pointer-events: none lets clicks fall through to overlay for close */
  pointer-events: none;
}
```

- [ ] **Step 2: Verify file was saved**

Open `assets/css/lightbox.css` in an editor and confirm it contains the `.lightbox-overlay` rule. No build step needed for CSS.

- [ ] **Step 3: Commit**

```bash
git add assets/css/lightbox.css
git commit -m "feat: add lightbox CSS styles"
```

---

### Task 2: Write image-lightbox.js

**Files:**
- Create: `assets/js/image-lightbox.js`

- [ ] **Step 1: Create the JS file**

```js
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
```

- [ ] **Step 2: Verify file was saved**

Open `assets/js/image-lightbox.js` and confirm the IIFE wrapper and `openLightbox` / `closeLightbox` functions are present.

- [ ] **Step 3: Commit**

```bash
git add assets/js/image-lightbox.js
git commit -m "feat: add image lightbox JS"
```

---

### Task 3: Wire CSS and JS into default.html

**Files:**
- Modify: `_layouts/default.html:29` (CSS link, after `callouts.css`)
- Modify: `_layouts/default.html:84` (script tag, after `search-ui.js`)

- [ ] **Step 1: Add the CSS `<link>` in `<head>`**

In `_layouts/default.html`, find this line (line 29):

```html
  <link rel="stylesheet" href="{{ '/assets/css/callouts.css' | relative_url }}">
```

Add the lightbox link immediately after it:

```html
  <link rel="stylesheet" href="{{ '/assets/css/callouts.css' | relative_url }}">
  <link rel="stylesheet" href="{{ '/assets/css/lightbox.css' | relative_url }}">
```

- [ ] **Step 2: Add the `<script>` tag at the bottom of `<body>`**

In `_layouts/default.html`, find this line (line 84):

```html
  <script src="{{ '/assets/js/search-ui.js' | relative_url }}" defer></script>
```

Add the lightbox script immediately after it:

```html
  <script src="{{ '/assets/js/search-ui.js' | relative_url }}" defer></script>
  <script src="{{ '/assets/js/image-lightbox.js' | relative_url }}" defer></script>
```

- [ ] **Step 3: Commit**

```bash
git add _layouts/default.html
git commit -m "feat: wire image-lightbox CSS and JS into default layout"
```

---

### Task 4: Manual verification

- [ ] **Step 1: Start the local Jekyll server**

```bash
cd docs
make dev
```

Expected: Server starts at `http://localhost:4000` (or `http://127.0.0.1:4000`).

- [ ] **Step 2: Open a lesson page that has images**

Navigate to any lesson with inline images, e.g.:

```
http://localhost:4000/3-data-visualization/3.1-intro-data-viz/matplotlib-basics
```

- [ ] **Step 3: Verify cursor changes on hover**

Hover over an image inside the lesson content. The cursor should change to `zoom-in` (magnifying glass with +).

- [ ] **Step 4: Verify lightbox opens on click**

Click an image. Expected:
- Page scroll locks (body overflow hidden)
- Dark semi-transparent overlay covers the full viewport
- The clicked image is centered and fills up to 90% of the screen

- [ ] **Step 5: Verify click-to-close**

While the lightbox is open, click anywhere on the dark overlay. Expected:
- Overlay disappears
- Page scroll is restored

- [ ] **Step 6: Verify Escape-to-close**

Open the lightbox again, then press the `Escape` key. Expected:
- Overlay disappears
- Page scroll is restored

- [ ] **Step 7: Verify linked images are unaffected**

If any images are wrapped in `<a href="…">` links, clicking them should follow the link — not open the lightbox.

- [ ] **Step 8: Verify dark-mode overlay**

Toggle to dark mode (top-right theme button). Open the lightbox again. The overlay background should still be visibly distinct from the dark page background (it's `rgba(0,0,0,0.85)` which works in both modes).

- [ ] **Step 9: Final commit (if any tweaks made)**

```bash
git add -p
git commit -m "fix: lightbox manual review tweaks"
```
