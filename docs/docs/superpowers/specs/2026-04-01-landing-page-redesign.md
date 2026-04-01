# Landing Page Visual Redesign

**Date:** 2026-04-01
**Status:** Approved
**Scope:** Visual polish of the landing page at `/tamkeen-data/` — no new content, no JS, no layout template changes.

## Context

The current landing page has a hero section and a 7-card module grid. It is functional but visually flat. The audience is enrolled Tamkeen students who need a clear, inviting entry point. The modules are sequential (0-6) and should read as a progression/timeline.

## Design

### 1. Full-Width Gradient Hero

The `.home-hero` breaks out of `.container-lg` to span edge-to-edge using negative margins, with internal padding to keep text aligned with the content column.

- **Light mode:** soft radial gradient — white center fading to light blue edges
- **Dark mode:** deep navy center with subtle blue glow at edges
- Title: `clamp(2rem, 5vw, 2.75rem)`, weight 700, letter-spacing `-0.025em`
- Subtitle and meta text get slightly more vertical spacing

### 2. Vertical Timeline Layout

Replace `.module-grid` (CSS grid) with a vertical timeline.

**Structure (HTML in `index.md`):**

```html
<nav class="module-timeline" aria-label="Course modules">
  <div class="timeline-module" style="--module-color: var(--mod-0)">
    <div class="timeline-node" aria-hidden="true">
      <span class="timeline-node__number">0</span>
    </div>
    <a class="timeline-card" href="...">
      <span class="timeline-card__title">Preparation</span>
      <span class="timeline-card__desc">Environment, notebooks, and optional tools</span>
    </a>
  </div>
  <!-- repeat for modules 1-6 -->
</nav>
```

**Timeline line:** A `::before` pseudo-element on `.module-timeline`, positioned absolutely on the left. 2px wide, accent color (`var(--link)` at 30% opacity). Starts at the center of the first node, ends at the center of the last node.

**Nodes:** 2.5rem circles on the timeline line, filled with `var(--module-color)`, containing the module number in white/dark text. Each module gets a unique color via CSS custom properties:

| Module | Token | Light value | Dark value |
|--------|-------|-------------|------------|
| 0 Prep | `--mod-0` | `#6e7781` | `#8b949e` |
| 1 Fundamentals | `--mod-1` | `#0969da` | `#58a6ff` |
| 2 Wrangling | `--mod-2` | `#0e8a6e` | `#3fb68b` |
| 3 Visualization | `--mod-3` | `#8250df` | `#b87fff` |
| 4 Statistics | `--mod-4` | `#bf6b00` | `#d29922` |
| 5 ML | `--mod-5` | `#1a7f37` | `#56d364` |
| 6 Capstone | `--mod-6` | `#cf222e` | `#f47067` |

**Cards:** Positioned to the right of the node. Same content as current cards (title + description). Styled similarly to current `.module-card` but with a 3px left-border in `var(--module-color)`. Slightly more vertical padding (1.15rem). Hover: lift + border-color intensifies + shadow deepens.

**Connector:** A short horizontal line (CSS pseudo-element on `.timeline-module`) connecting the node circle to the card's left edge. Same color as the timeline line.

### 3. Staggered Fade-In Animation

Pure CSS `@keyframes` animation on `.timeline-module`:

```css
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
```

Each `.timeline-module` gets `animation: timeline-fade-in 0.4s ease both` with an incremental `animation-delay` set via `--i` custom property (0 through 6). Delay formula: `calc(var(--i) * 80ms)`. The `--i` is set inline in the HTML (`style="--i: 0"`, etc.) alongside `--module-color`.

Respects `prefers-reduced-motion`: animation disabled, elements render immediately.

### 4. "Start Here" Section Header

The `## Start here` heading remains as uppercase, letter-spaced label text. A thin `1px` horizontal rule sits below it, matching `var(--border)`. No other changes.

### 5. Responsive Behavior

**Desktop (>640px):**
- Timeline line is ~3rem from the left edge of the content area
- Nodes centered on the line
- Cards fill remaining width to the right

**Mobile (<=640px):**
- Timeline line shifts to 1.25rem from left
- Nodes shrink to 2rem
- Cards take full width below/right of node with reduced left margin
- Connector line hidden (node sits directly adjacent to card)

## Files Changed

| File | Change |
|------|--------|
| `docs/index.md` | Replace `.module-grid` markup with `.module-timeline` markup |
| `docs/assets/css/style.css` | Remove `.module-grid` / `.module-card` styles, add timeline styles, update `.home-hero` for full-width |

No changes to `_layouts/default.html`, no new JS files.

## Out of Scope

- New content sections (prerequisites, duration, "what you'll learn")
- Interactive progress tracking
- SVG or image icons on modules
- Changes to any page other than the landing page
