# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Data Science and AI educational course repository (Tamkeen program by Skills Union). It's a Jekyll-based static site with 6 progressive modules covering data fundamentals through machine learning, plus interactive Reveal.js slide presentations.

**Live site**: https://codebyshennan.github.io/tamkeen-data

## Build Commands

### Slide Generation
```bash
# Default: 0-prep + module 1 (data fundamentals) slide decks only
make build

# Every submodule that has slides/data.json (full course)
make build-all-slides

# Build specific modules
make prep                    # Module 0: Setup/preparation
make data-fundamentals       # Module 1: All submodules
make python                  # Module 1.2 only
make stats                   # Module 1.3 only
make linear-algebra          # Module 1.4 only
make pandas                  # Module 1.5 only

# Build any module directly
node slides/build.js <module-path>
# Example: node slides/build.js 2-data-wrangling/2.1-sql

# Clean generated slide HTML (*/slides/index.html only)
make clean
make clean-module MODULE=<path-under-docs>

# Regenerate one module (path is relative to docs/, any module)
make regenerate MODULE=2-data-wrangling/2.1-sql
```

See `slides/README.md` for `data.json` format and implementation details.

### Jekyll (Local Development)

Use the same gem stack as [GitHub Pages](https://pages.github.com/versions/) (see `Gemfile`). **Ruby 3.1+** is required for current `github-pages` / `nokogiri`. `.ruby-version` pins a **3.3.x** patch for local tools (rbenv/RVM); any 3.3.x is fine—GitHub Pages may use a slightly newer patch than your laptop.

```bash
cd docs
bundle install
bundle exec jekyll serve    # or: bundle exec jekyll build
```

### GitHub Pages and lesson Markdown

GitHub Pages builds with the `github-pages` gem, which enables (among others) **`jekyll-optional-front-matter`** and **`jekyll-default-layout`**. Lesson files **do not need** a `---` YAML block: they are still turned into HTML and get the default layout. **`jekyll-relative-links`** rewrites relative links like `[x](lesson.md)` to the built `.html` URLs.

If you run plain `jekyll` without `bundle exec` and without those plugins, lesson files may look “unprocessed”—always use `bundle exec` from `docs/` after `bundle install`.

## Architecture

### Directory Structure
- `0-prep/` through `6-capstone/` - Course modules (numbered for progression)
- `meta/` - Maintainer-only docs (deploy checklist, writing guidelines); excluded from Jekyll
- Each module contains:
  - Markdown content files (tutorials, concepts)
  - `slides/data.json` - Slide definitions for Reveal.js
  - `slides/index.html` - Generated presentations (do not edit directly)
  - `_assignments/` - Practical exercises

### Slide Generation System
1. Define slides in `<module>/slides/data.json` with type (`title` or `content`)
2. Run `node slides/build.js <module-path>`
3. Script reads `slides/template.html` and generates `slides/index.html`

### Content Patterns
- Module overviews in `README.md`
- Concept files follow kebab-case: `concept-name.md`
- MathJax loaded in the layout for equations (GFM does not emit kramdown’s math spans; raw `$$` usually still works with MathJax)
- Python is the default syntax highlighting language

## Key Configuration

- **Package manager**: pnpm
- **Jekyll theme**: primer (remote theme)
- **Markdown**: GFM (`markdown: GFM`) with Rouge for fenced code blocks
- **Presentations**: Reveal.js v4.3.1 (CDN-based)
