# Lesson Jump Navigation Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a "Jump to lesson" `<select>` dropdown in the lesson nav bar so learners can jump directly to any lesson in the current submodule, consistently across all pages.

**Architecture:** The existing `_includes/lesson-nav.html` already computes the ordered list of pages (`order` from `_data/lesson_nav_order.yml`, or `sibs` fallback). We add a `<select>` element to the existing `lesson-nav__meta` row using the same data, rendered server-side by Liquid — no JS file needed beyond an inline `onchange`. CSS additions go to `assets/css/style.css`.

**Tech Stack:** Jekyll/Liquid templating, CSS custom properties (already in use), inline JS `onchange`.

---

## File Map

| File | Change |
|------|--------|
| `docs/_includes/lesson-nav.html` | Add `<select>` dropdown to `lesson-nav__meta` using `order`/`sibs` data |
| `docs/assets/css/style.css` | Add `.lesson-nav__jump` styles (light/dark, sizing, focus ring) |

---

### Task 1: Add the jump dropdown to lesson-nav.html

**Files:**
- Modify: `docs/_includes/lesson-nav.html`

The dropdown must work for both data sources:
- When `order` exists (from `lesson_nav_order.yml`): iterate `order`, look up each page via `site.pages | where: 'path'`
- When falling back to `sibs`: iterate `sibs` directly

It must be placed inside the existing `lesson-nav__meta` div (after the progress span), so it appears just above the fixed bottom bar and is consistent on every lesson page.

- [ ] **Step 1: Open and read the current lesson-nav.html**

File: `docs/_includes/lesson-nav.html` (already read — 156 lines)

- [ ] **Step 2: Replace the `lesson-nav__meta` block**

Find this block (lines 123–138):

```liquid
  {% assign prog_cur = '' %}
  {% assign prog_tot = '' %}
  {% if idx > -1 %}
    {% assign prog_cur = idx | plus: 1 %}
    {% assign prog_tot = order | size %}
  {% elsif sidx > -1 %}
    {% assign prog_cur = sidx | plus: 1 %}
    {% assign prog_tot = sibs | size %}
  {% endif %}

<nav class="lesson-nav" aria-label="Lesson navigation">
  {% if prog_cur != '' %}
  <div class="lesson-nav__meta">
    <span class="lesson-nav__progress">Lesson {{ prog_cur }} of {{ prog_tot }}</span>
  </div>
  {% endif %}
```

Replace with:

```liquid
  {% assign prog_cur = '' %}
  {% assign prog_tot = '' %}
  {% if idx > -1 %}
    {% assign prog_cur = idx | plus: 1 %}
    {% assign prog_tot = order | size %}
  {% elsif sidx > -1 %}
    {% assign prog_cur = sidx | plus: 1 %}
    {% assign prog_tot = sibs | size %}
  {% endif %}

<nav class="lesson-nav" aria-label="Lesson navigation">
  {% if prog_cur != '' %}
  <div class="lesson-nav__meta">
    <span class="lesson-nav__progress">Lesson {{ prog_cur }} of {{ prog_tot }}</span>
    <select class="lesson-nav__jump" aria-label="Jump to lesson" onchange="if(this.value)location.href=this.value">
      {% if idx > -1 %}
        {% for f in order %}
          {% assign _jpath = dir_key | append: '/' | append: f %}
          {% assign _jpage = site.pages | where: 'path', _jpath | first %}
          {% if _jpage %}
            <option value="{{ _jpage.url | relative_url }}"{% if f == page.name %} selected{% endif %}>{{ _jpage.title | default: f | replace: '-', ' ' | replace: '.md', '' }}</option>
          {% endif %}
        {% endfor %}
      {% elsif sidx > -1 %}
        {% for p in sibs %}
          <option value="{{ p.url | relative_url }}"{% if p.name == page.name %} selected{% endif %}>{{ p.title | default: p.name | replace: '-', ' ' | replace: '.md', '' }}</option>
        {% endfor %}
      {% endif %}
    </select>
  </div>
  {% endif %}
```

- [ ] **Step 3: Verify the file looks right**

The full `lesson-nav.html` after edits should have the `<select>` inside `.lesson-nav__meta`, and the rest of the file (the `lesson-nav__inner` buttons block) unchanged. Confirm visually.

- [ ] **Step 4: Commit**

```bash
cd /Users/wongshennan/Documents/personal/career/work/skillsunion/dsai/tamkeen
git add docs/_includes/lesson-nav.html
git commit -m "feat: add lesson jump dropdown to nav bar"
```

---

### Task 2: Style the jump dropdown

**Files:**
- Modify: `docs/assets/css/style.css`

The dropdown must:
- Inherit the page's color tokens (light + dark)
- Not break the flex layout of `.lesson-nav__meta`
- Have a visible focus ring (accessibility)
- Be readable at small font sizes

- [ ] **Step 1: Find the insertion point**

In `style.css`, locate `.lesson-nav__progress` (around line 1309). Add the new rule immediately after `.lesson-nav__progress { … }`.

- [ ] **Step 2: Add the CSS**

After the closing `}` of `.lesson-nav__progress`, insert:

```css
.lesson-nav__jump {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text);
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.25rem 0.5rem;
    cursor: pointer;
    max-width: 260px;
}

.lesson-nav__jump:focus-visible {
    outline: 2px solid var(--link);
    outline-offset: 2px;
}
```

- [ ] **Step 3: Verify dark mode works**

The dropdown uses `var(--text)`, `var(--code-bg)`, and `var(--border)` — all of which are already defined under `:root[data-theme="dark"]`. No extra dark-mode rules needed.

- [ ] **Step 4: Commit**

```bash
cd /Users/wongshennan/Documents/personal/career/work/skillsunion/dsai/tamkeen
git add docs/assets/css/style.css
git commit -m "style: lesson jump dropdown"
```

---

### Task 3: Smoke-test with Jekyll

**Files:** none (verification only)

- [ ] **Step 1: Build the site**

```bash
cd /Users/wongshennan/Documents/personal/career/work/skillsunion/dsai/tamkeen/docs
make dev
```

Expected: Jekyll starts with no errors.

- [ ] **Step 2: Open a mid-sequence lesson page**

Navigate to any lesson that has a `lesson_nav_order.yml` entry with 3+ pages (e.g. `http://localhost:4000/1-data-fundamentals/1.2-intro-python/functions/`).

Expected:
- "Lesson N of M" appears in the meta row
- A dropdown appears next to it showing all lessons in the submodule
- The current lesson is pre-selected in the dropdown
- Choosing a different lesson navigates to it

- [ ] **Step 3: Check a fallback page**

Navigate to a page whose directory is NOT in `lesson_nav_order.yml` (relies on `sibs` fallback).

Expected: Dropdown still appears with siblings listed, current page selected.

- [ ] **Step 4: Check the module root (README) page**

Navigate to a submodule `README.md` page (which has `lesson_nav: false` implied by the `show_lesson_nav` logic... actually README.md does show the nav bar, it just sets `root_label` differently).

Expected: Dropdown appears with full lesson list, first lesson (README) selected.

- [ ] **Step 5: Check dark mode**

Toggle dark mode via the site header toggle.

Expected: Dropdown background/text adapts correctly to dark theme.
