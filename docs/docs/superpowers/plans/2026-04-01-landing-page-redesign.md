# Landing Page Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the landing page from a flat card grid into a visual timeline with a full-width hero, color-coded module nodes, and staggered CSS animations.

**Architecture:** Two files change — `index.md` (HTML markup swap from grid to timeline) and `style.css` (remove old grid styles, add timeline + hero styles). No JS, no layout template changes.

**Tech Stack:** Jekyll/Liquid, CSS custom properties, CSS animations, HTML

---

## File Map

| File | Action | Responsibility |
|------|--------|----------------|
| `docs/index.md` | Modify (lines 15-65) | Replace `.module-grid` nav with `.module-timeline` nav |
| `docs/assets/css/style.css` | Modify (lines 1830-1936) | Replace grid/card styles with timeline styles; update hero for full-width |

---

### Task 1: Add module color tokens to CSS `:root`

**Files:**
- Modify: `docs/assets/css/style.css:1-21` (`:root` block)
- Modify: `docs/assets/css/style.css:23-40` (`:root[data-theme="dark"]` block)

- [ ] **Step 1: Add light-mode module color tokens**

In `docs/assets/css/style.css`, add the following lines at the end of the `:root` block (before the closing `}`), after the `--table-row-hover` line:

```css
    /* Module timeline colors */
    --mod-0: #6e7781;
    --mod-1: #0969da;
    --mod-2: #0e8a6e;
    --mod-3: #8250df;
    --mod-4: #bf6b00;
    --mod-5: #1a7f37;
    --mod-6: #cf222e;
    --timeline-line: rgba(9, 105, 218, 0.25);
```

- [ ] **Step 2: Add dark-mode module color tokens**

In `docs/assets/css/style.css`, add the following lines at the end of the `:root[data-theme="dark"]` block (before the closing `}`), after the `--table-row-hover` line:

```css
    /* Module timeline colors */
    --mod-0: #8b949e;
    --mod-1: #58a6ff;
    --mod-2: #3fb68b;
    --mod-3: #b87fff;
    --mod-4: #d29922;
    --mod-5: #56d364;
    --mod-6: #f47067;
    --timeline-line: rgba(88, 166, 255, 0.25);
```

- [ ] **Step 3: Verify Jekyll rebuilds without errors**

Run: `curl -s -o /dev/null -w "%{http_code}" http://localhost:4000/tamkeen-data/`
Expected: `200`

- [ ] **Step 4: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "style: add module color tokens for timeline landing page"
```

---

### Task 2: Restyle hero as full-width gradient banner

**Files:**
- Modify: `docs/assets/css/style.css:1831-1860` (`.home-hero` and children)

- [ ] **Step 1: Replace the `.home-hero` block**

In `docs/assets/css/style.css`, replace the entire `.home-page .home-hero` rule (lines 1831-1838) with:

```css
.home-page .home-hero {
    margin: 0 -1.25rem 2rem;
    padding: 2.75rem 1.25rem 2.5rem;
    border-radius: 0;
    border: none;
    border-bottom: 1px solid var(--border);
    background: radial-gradient(ellipse at 50% 0%, rgba(9, 105, 218, 0.08) 0%, transparent 70%),
                linear-gradient(180deg, var(--bg-card) 0%, var(--bg-page) 100%);
    box-shadow: none;
    text-align: center;
}

:root[data-theme="dark"] .home-page .home-hero {
    background: radial-gradient(ellipse at 50% 0%, rgba(88, 166, 255, 0.1) 0%, transparent 70%),
                linear-gradient(180deg, var(--bg-card) 0%, var(--bg-page) 100%);
}
```

- [ ] **Step 2: Update the hero h1 styles**

Replace the `.home-page .home-hero h1` rule (lines 1840-1846) with:

```css
.home-page .home-hero h1 {
    margin: 0 0 0.65rem;
    font-size: clamp(2rem, 5vw, 2.75rem);
    font-weight: 700;
    letter-spacing: -0.025em;
    line-height: 1.15;
}
```

- [ ] **Step 3: Update lead and meta text**

Replace the `.home-page .home-hero__lead` rule (lines 1848-1853) with:

```css
.home-page .home-hero__lead {
    margin: 0 auto 0.85rem;
    font-size: 1.1rem;
    color: var(--text);
    max-width: min(42rem, 100%);
    line-height: 1.55;
}
```

Replace the `.home-page .home-hero__meta` rule (lines 1855-1860) with:

```css
.home-page .home-hero__meta {
    margin: 0 auto;
    font-size: 0.9rem;
    color: var(--text-muted);
    max-width: min(44rem, 100%);
}
```

- [ ] **Step 4: Verify in browser**

Open `http://localhost:4000/tamkeen-data/` — hero should span full width with subtle blue radial glow, centered text. Check both light and dark modes (toggle in header).

- [ ] **Step 5: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "style: make landing hero full-width gradient banner"
```

---

### Task 3: Replace module grid markup with timeline in index.md

**Files:**
- Modify: `docs/index.md:15-65` (the `<nav class="module-grid">` section)

- [ ] **Step 1: Replace the module grid HTML**

In `docs/index.md`, replace everything from `<nav class="module-grid"` through the closing `</nav>` (lines 15-65) with:

```html
<nav class="module-timeline" aria-label="Course modules">
  <div class="timeline-module" style="--module-color: var(--mod-0); --i: 0">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">0</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 0-prep/README.md %}">
      <span class="timeline-card__title">Preparation</span>
      <span class="timeline-card__desc">Environment, notebooks, and optional tools</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-1); --i: 1">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">1</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 1-data-fundamentals/README.md %}">
      <span class="timeline-card__title">Data fundamentals</span>
      <span class="timeline-card__desc">Python, statistics, NumPy, pandas</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-2); --i: 2">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">2</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 2-data-wrangling/2.1-sql/README.md %}">
      <span class="timeline-card__title">Data wrangling</span>
      <span class="timeline-card__desc">SQL, quality, EDA, engineering basics</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-3); --i: 3">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">3</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 3-data-visualization/README.md %}">
      <span class="timeline-card__title">Data visualization</span>
      <span class="timeline-card__desc">Principles, Python viz, BI, storytelling</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-4); --i: 4">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">4</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 4-stat-analysis/README.md %}">
      <span class="timeline-card__title">Statistical analysis</span>
      <span class="timeline-card__desc">Inference, testing, regression, modelling</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-5); --i: 5">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">5</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 5-ml-fundamentals/5.1-intro-to-ml/README.md %}">
      <span class="timeline-card__title">Machine learning</span>
      <span class="timeline-card__desc">Workflows, models, unsupervised learning, evaluation</span>
    </a>
  </div>
  <div class="timeline-module" style="--module-color: var(--mod-6); --i: 6">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">6</span>
    </div>
    <a class="timeline-card" href="{{ site.baseurl }}{% link 6-capstone/README.md %}">
      <span class="timeline-card__title">Capstone</span>
      <span class="timeline-card__desc">End-to-end project guidelines</span>
    </a>
  </div>
</nav>
```

- [ ] **Step 2: Verify page loads (markup will be unstyled)**

Run: `curl -s -o /dev/null -w "%{http_code}" http://localhost:4000/tamkeen-data/`
Expected: `200`

- [ ] **Step 3: Commit**

```bash
git add docs/index.md
git commit -m "markup: replace module grid with timeline structure on landing page"
```

---

### Task 4: Add timeline CSS (layout, nodes, cards, connectors)

**Files:**
- Modify: `docs/assets/css/style.css:1862-1936` (replace old `.module-grid` / `.module-card` rules)

- [ ] **Step 1: Replace the old grid and card styles**

In `docs/assets/css/style.css`, replace the `## Start here` heading rule and all `.module-grid` / `.module-card` rules (from `.home-page h2` at line 1862 through `.home-page .module-card__desc` ending at line 1936) with the following:

```css
.home-page h2 {
    margin-top: 0.5rem;
    margin-bottom: 1.5rem;
    font-size: 1.15rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.04em;
    text-align: center;
}

/* --- Timeline layout --- */
.home-page .module-timeline {
    position: relative;
    margin: 0 0 2rem;
    padding: 0;
    list-style: none;
}

/* Vertical line */
.home-page .module-timeline::before {
    content: "";
    position: absolute;
    left: 1.25rem;
    top: 1.25rem;
    bottom: 1.25rem;
    width: 2px;
    background: var(--timeline-line);
    border-radius: 1px;
}

/* Each module row */
.home-page .timeline-module {
    position: relative;
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 0.5rem 0;
    padding-left: 0;
}

/* Node (circle on the line) */
.home-page .timeline-node {
    position: relative;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 50%;
    background: var(--module-color);
    z-index: 1;
    box-shadow: 0 0 0 4px var(--bg-page);
}

.home-page .timeline-node__number {
    font-size: 0.95rem;
    font-weight: 700;
    color: #fff;
    line-height: 1;
}

/* Connector: horizontal line from node to card */
.home-page .timeline-module::after {
    content: "";
    position: absolute;
    left: 2.5rem;
    top: calc(0.5rem + 1.25rem - 1px);
    width: 1rem;
    height: 2px;
    background: var(--timeline-line);
}

/* Card */
.home-page .timeline-card {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 0.3rem;
    padding: 1.15rem 1.25rem;
    margin-left: 1rem;
    border-radius: 10px;
    border: 1px solid var(--border);
    border-left: 3px solid var(--module-color);
    background: var(--bg-card);
    text-decoration: none;
    color: inherit;
    box-shadow: 0 1px 2px var(--shadow);
    transition: border-color 0.15s ease, box-shadow 0.15s ease, transform 0.15s ease;
}

.home-page .timeline-card:hover {
    border-color: var(--module-color);
    border-left-color: var(--module-color);
    box-shadow: 0 4px 14px var(--shadow);
    transform: translateY(-2px);
}

.home-page .timeline-card:focus-visible {
    outline: 2px solid var(--module-color);
    outline-offset: 2px;
}

.home-page .timeline-card__title {
    font-weight: 600;
    font-size: 1.05rem;
    color: var(--text);
}

.home-page .timeline-card__desc {
    font-size: 0.875rem;
    line-height: 1.45;
    color: var(--text-muted);
}
```

- [ ] **Step 2: Verify in browser**

Open `http://localhost:4000/tamkeen-data/` — should see a vertical timeline with colored nodes on the left, connector lines, and cards to the right. Each card should have a colored left border matching its node.

- [ ] **Step 3: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "style: add timeline layout with color-coded nodes and cards"
```

---

### Task 5: Add staggered fade-in animation

**Files:**
- Modify: `docs/assets/css/style.css` (append after the timeline card styles from Task 4)

- [ ] **Step 1: Add the keyframe and animation rules**

In `docs/assets/css/style.css`, immediately after the `.home-page .timeline-card__desc` rule (the last rule added in Task 4), add:

```css
/* --- Timeline fade-in animation --- */
@keyframes timeline-fade-in {
    from {
        opacity: 0;
        transform: translateY(16px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.home-page .timeline-module {
    opacity: 0;
    animation: timeline-fade-in 0.4s ease both;
    animation-delay: calc(var(--i) * 80ms);
}

@media (prefers-reduced-motion: reduce) {
    .home-page .timeline-module {
        opacity: 1;
        animation: none;
    }
}
```

- [ ] **Step 2: Verify in browser**

Open `http://localhost:4000/tamkeen-data/` — modules should fade in sequentially from top to bottom on page load. Hard-refresh (Cmd+Shift+R) to replay. Toggle "reduce motion" in system accessibility settings to verify the fallback (all cards visible immediately, no animation).

- [ ] **Step 3: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "style: add staggered fade-in animation for timeline modules"
```

---

### Task 6: Add mobile responsive styles

**Files:**
- Modify: `docs/assets/css/style.css` (append after the animation rules from Task 5)

- [ ] **Step 1: Add the mobile media query**

In `docs/assets/css/style.css`, immediately after the `prefers-reduced-motion` media query from Task 5, add:

```css
/* --- Timeline mobile --- */
@media (max-width: 640px) {
    .home-page .module-timeline::before {
        left: 0.875rem;
    }

    .home-page .timeline-module {
        gap: 0.65rem;
    }

    .home-page .timeline-node {
        width: 1.75rem;
        height: 1.75rem;
    }

    .home-page .timeline-node__number {
        font-size: 0.8rem;
    }

    .home-page .timeline-module::after {
        left: 1.75rem;
        top: calc(0.5rem + 0.875rem - 1px);
        width: 0.65rem;
    }

    .home-page .timeline-card {
        margin-left: 0.65rem;
        padding: 0.9rem 1rem;
    }

    .home-page .home-hero {
        padding: 2rem 1.25rem 1.75rem;
    }
}
```

- [ ] **Step 2: Verify in browser**

Open `http://localhost:4000/tamkeen-data/` and resize to <640px (or use Chrome DevTools responsive mode). Timeline should compact: smaller nodes, tighter spacing, cards still readable. Hero should have slightly less vertical padding.

- [ ] **Step 3: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "style: add mobile responsive timeline layout"
```

---

### Task 7: Clean up removed CSS and verify final state

**Files:**
- Modify: `docs/assets/css/style.css` (remove dead code if any old `.module-grid`/`.module-card` rules remain)

- [ ] **Step 1: Search for orphaned selectors**

Search `style.css` for any remaining `.module-grid` or `.module-card` selectors. If Tasks 4 replaced them fully, there should be zero matches. If any remain, delete them.

Run: `grep -n "module-grid\|module-card" docs/assets/css/style.css`
Expected: no output

- [ ] **Step 2: Search for orphaned HTML**

Search `index.md` for any remaining `module-grid` or `module-card` class references. Should be zero.

Run: `grep -n "module-grid\|module-card" docs/index.md`
Expected: no output

- [ ] **Step 3: Full visual check**

Open `http://localhost:4000/tamkeen-data/` and verify:
1. Full-width gradient hero with centered text
2. "START HERE" label centered below hero
3. Vertical timeline with 7 color-coded nodes (0-6)
4. Horizontal connector lines from nodes to cards
5. Cards have colored left borders matching their nodes
6. Staggered fade-in animation on load
7. Hover: cards lift, border intensifies
8. Dark mode: toggle theme, all colors adapt
9. Mobile (<640px): nodes shrink, layout compacts
10. `prefers-reduced-motion`: no animation

- [ ] **Step 4: Commit cleanup (if any changes were made)**

```bash
git add docs/assets/css/style.css docs/index.md
git commit -m "chore: clean up orphaned grid/card styles from landing page"
```
