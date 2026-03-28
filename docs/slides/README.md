# Reveal.js slide builder

Slides are authored as JSON and compiled to a single `slides/index.html` per submodule. The generator merges `data.json` into `template.html` (Reveal.js 4.3.1 from CDN).

## Build

From the `docs/` directory:

```bash
node slides/build.js <path-to-module>
```

Examples:

```bash
node slides/build.js 0-prep
node slides/build.js 2-data-wrangling/2.1-sql
```

Or use the `Makefile` targets (`make prep`, `make python`, etc.). See the root `CLAUDE.md` for the full list.

`make build` currently runs **0-prep** and **module 1 (data fundamentals)** only. To rebuild every deck:

```bash
make build-all-slides
```

## `data.json` shape

- Top level: `title` (string, used for `<title>` and validation) and `slides` (array).
- Each slide has `type`:
  - `title`: `title`, optional `subtitle` (plain text or `**bold**` segments).
  - `content`: `title`, optional `content` object with optional `title`, `items` (string array), and optional `ordered` (use `<ol>` instead of `<ul>`).

Optional fields on `content` (for long lists — avoids overflow):

- **`chunkSize`** (number): max items per slide before splitting into multiple sections with titles like `Your Title (2/5)`. Default is **10**. Set to **`false`** or **`0`** to keep all items on one slide (use sparingly).
- **`columns`** (`2` or `3`): force a multi-column list layout. If omitted, the builder may use 2 columns when a chunk has **8+** items, or 3 columns when a chunk has **18+** items.
- Ordered lists (`ordered: true`) use correct `<ol start="…">` continuation across columns.

List item strings support inline `**emphasis**` only (rendered as `<strong>`). Other markdown is not parsed; use plain text or HTML entities if needed.

## Editing

- Edit `slides/data.json` in the submodule.
- Regenerate `slides/index.html` with the commands above. Do not hand-edit `index.html` (it is overwritten).

## Implementation notes

- Text is HTML-escaped, then `**...**` is converted to `<strong>`.
- Unknown `slide.type` values are skipped with a console warning.
