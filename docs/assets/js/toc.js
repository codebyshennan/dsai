/**
 * Builds "On this page" TOC from h2/h3 inside #lesson-article. Desktop: sticky sidebar.
 */
(function () {
  'use strict';

  var TOC_MIN_HEADINGS = 2;

  function slugify(text) {
    return text
      .toLowerCase()
      .replace(/[^\w\u00fc\u00e4\u00f6\u00df-\s-]/g, '')
      .trim()
      .replace(/\s+/g, '-');
  }

  function build() {
    var article = document.getElementById('lesson-article');
    var slot = document.getElementById('toc-slot');
    if (!article || !slot) return;

    var heads = article.querySelectorAll('h2, h3');
    if (heads.length < TOC_MIN_HEADINGS) return;

    var used = Object.create(null);
    var nav = document.createElement('nav');
    nav.className = 'page-toc__nav';
    nav.setAttribute('aria-label', 'On this page');

    var title = document.createElement('p');
    title.className = 'page-toc__title';
    title.textContent = 'On this page';
    nav.appendChild(title);

    var ul = document.createElement('ul');
    ul.className = 'page-toc__list';

    heads.forEach(function (h) {
      var text = h.textContent.replace(/\s+/g, ' ').trim();
      if (!text) return;

      var id = h.id;
      if (!id) {
        id = slugify(text);
        var base = id;
        var n = 0;
        while (used[id] || document.getElementById(id)) {
          n += 1;
          id = base + '-' + n;
        }
        used[id] = true;
        h.id = id;
      } else {
        used[id] = true;
      }

      var li = document.createElement('li');
      li.className = 'page-toc__item page-toc__item--' + h.tagName.toLowerCase();
      var a = document.createElement('a');
      a.href = '#' + id;
      a.textContent = text;
      a.className = 'page-toc__link';
      li.appendChild(a);
      ul.appendChild(li);
    });

    if (!ul.children.length) return;

    nav.appendChild(ul);

    var details = document.createElement('details');
    details.className = 'page-toc__details';
    if (window.matchMedia('(min-width: 1100px)').matches) {
      details.setAttribute('open', '');
    }
    var summary = document.createElement('summary');
    summary.className = 'page-toc__summary';
    summary.textContent = 'Contents';
    details.appendChild(summary);
    details.appendChild(nav);
    slot.appendChild(details);
    slot.hidden = false;

    var links = ul.querySelectorAll('a');
    var obs = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          var id = entry.target.id;
          links.forEach(function (a) {
            a.classList.toggle('is-active', a.getAttribute('href') === '#' + id);
          });
        });
      },
      { rootMargin: '-20% 0px -70% 0px', threshold: 0 }
    );
    heads.forEach(function (h) {
      obs.observe(h);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
