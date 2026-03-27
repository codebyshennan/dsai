#!/usr/bin/env python3
"""
Replace generic code-callout placeholders using title + data-lines + simple heuristics.

Processes Markdown under docs/2-data-wrangling/ (recursive). Skips callouts that already
have substantive bodies (no 'follow this band' placeholder).

Usage from docs/:
  uv run python scripts/enrich_code_callout_bodies.py
"""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent
ROOT = DOCS / "2-data-wrangling"

# Match one code-callout block with the placeholder paragraph
CALLOUT_RE = re.compile(
    r'(\s*<div class="code-callout" data-lines="([^"]+)"[^>]*>\s*'
    r'<div class="code-callout__meta">\s*'
    r'<span class="code-callout__lines"></span>\s*'
    r'<span class="code-callout__title">([^<]*)</span>\s*'
    r"</div>\s*"
    r'<div class="code-callout__body">\s*)'
    r"<p>Lines [0-9–]+: follow this band in the snippet\.</p>",
    re.MULTILINE,
)


def paragraph_for(title: str, line_range: str) -> str:
    t = (title or "").strip() or "This band"
    tl = t.lower()

    # Keyword hints (SQL + pandas)
    if tl.startswith("bad") or "bad:" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range} in the snippet. '
            f"Contrast this with the alternative below; the goal is to avoid accidental cartesian products, "
            f"non-sargable predicates, or silent data loss.</p>"
        )
    if "join" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"Trace the <code>ON</code> predicates and join type: they decide which rows survive and whether "
            f"unmatched keys appear as <code>NULL</code> (outer joins).</p>"
        )
    if "group" in tl or "aggregate" in tl or "count" in tl or "sum" in tl or "having" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"Aggregation collapses rows after <code>FROM</code>/<code>WHERE</code>; "
            f"<code>GROUP BY</code> defines one output row per group, and <code>HAVING</code> filters those groups.</p>"
        )
    if "window" in tl or "over (" in tl or "rank()" in tl or "lag" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"Window functions compute per-row values using a frame without collapsing groups—"
            f"check <code>PARTITION BY</code> and <code>ORDER BY</code> inside <code>OVER</code>.</p>"
        )
    if "with " in tl or "recursive" in tl or "cte" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"The <code>WITH</code> clause names intermediate result sets; the outer query reads from them like views. "
            f"Recursive CTEs union the base case with repeated expansion.</p>"
        )
    if "explain" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"<code>EXPLAIN</code> (or <code>EXPLAIN ANALYZE</code>) shows the plan: scan types, join order, and cost estimates.</p>"
        )
    if "python" in tl or "def " in tl or "import " in tl or "pandas" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"Walk this block top to bottom: imports, inputs, then the transformation or plot that uses them.</p>"
        )
    if "create table" in tl or tl.startswith("create ") or "new table" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"DDL: column types, <code>PRIMARY KEY</code>/<code>UNIQUE</code>, <code>NOT NULL</code>, "
            f"<code>DEFAULT</code>, and <code>REFERENCES</code> define structure before any data is loaded.</p>"
        )
    if "insert" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"<code>INSERT</code> targets columns explicitly; <code>VALUES</code> lists one or many rows—match column order to the insert list.</p>"
        )
    if "update" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"<code>UPDATE</code> sets new values; <code>WHERE</code> limits which rows change—omit <code>WHERE</code> only when you intend to touch every row.</p>"
        )
    if "delete" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"<code>DELETE</code> removes rows matching <code>WHERE</code>; always sanity-check the predicate before running on production data.</p>"
        )
    if "alter" in tl:
        return (
            f'<p><strong>{t}</strong> — lines {line_range}. '
            f"<code>ALTER TABLE</code> evolves schema (add/drop columns, constraints); may lock large tables depending on engine settings.</p>"
        )

    return (
        f'<p><strong>{t}</strong> — lines {line_range} in the highlighted code. '
        f"Identify what this band does: DDL (table/column definitions), row changes "
        f"(<code>INSERT</code>/<code>UPDATE</code>/<code>DELETE</code>), or a <code>SELECT</code> pipeline—then read joins and predicates in snippet order.</p>"
    )


def process_file(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    if "follow this band in the snippet" not in text:
        return 0

    def repl(m: re.Match[str]) -> str:
        prefix, line_range, title = m.group(1), m.group(2), m.group(3)
        return prefix + paragraph_for(title, line_range)

    new_text, n = CALLOUT_RE.subn(repl, text)
    if n:
        path.write_text(new_text, encoding="utf-8")
    return n


def main() -> None:
    total = 0
    for path in sorted(ROOT.rglob("*.md")):
        n = process_file(path)
        if n:
            print(f"{n:4d}  {path.relative_to(DOCS)}")
            total += n
    print(f"Total callouts replaced: {total}")


if __name__ == "__main__":
    main()
