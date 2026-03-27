#!/usr/bin/env python3
"""
Replace generic code-callout placeholders in order (handles duplicate titles).

Usage from docs/:
  uv run python scripts/patch_code_explainer_callouts.py
"""
from __future__ import annotations

import re
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent

PLACEHOLDER_RE = re.compile(
    r"<p>Lines [0-9–]+: follow this band in the snippet\.</p>"
)

# 2.1-sql/intro-databases.md — 30 callouts top to bottom
INTRO_DATABASES_BODIES: list[str] = [
    "<p>Two tables: <code>customers</code> owns identities; <code>orders</code> references <code>customer_id</code> so each order belongs to one customer—classic parent/child FK pattern.</p>",
    "<p><code>products</code> and <code>categories</code> are linked by a junction table <code>product_categories</code> with a composite primary key—standard many-to-many modeling.</p>",
    "<p>Junction row: both columns are foreign keys; together they form the primary key so the same pair cannot be inserted twice.</p>",
    "<p>Contrasts a packed text list of products with one row per product line—atomic values enable joins and counts.</p>",
    "<p>Anti-pattern: <code>product_name</code> depends only on <code>product_id</code>, not the full composite key. The fix splits <code>products</code> out.</p>",
    "<p>Clean <code>order_items</code> holds only keys and quantity; product names live solely in <code>products</code>.</p>",
    "<p>Redundant <code>department_name</code> on every employee row duplicates data tied to <code>department_id</code>.</p>",
    "<p>Department attributes live in one place; employees reference <code>department_id</code> only—removes transitive dependency.</p>",
    "<p>Sketch of ACID-related features: explicit <code>BEGIN</code>/<code>COMMIT</code>, <code>GRANT</code> for privileges—syntax varies by engine; backup lines are illustrative.</p>",
    "<p>Creates a btree index for lookups, mentions <code>EXPLAIN ANALYZE</code> for plans, and <code>work_mem</code> for sort/hash workspace—tune per workload.</p>",
    "<p><code>CREATE DATABASE</code>, optional <code>SCHEMA</code>, and <code>search_path</code> so unqualified names resolve predictably.</p>",
    "<p><code>UNIQUE</code>, <code>NOT NULL</code>, regex <code>CHECK</code> on email, and defaults—constraints enforce rules at insert time.</p>",
    "<p><code>ALTER TABLE</code> adds columns and constraints; <code>CREATE VIEW</code> exposes a filtered “active users” subset.</p>",
    "<p>Standard <code>INSERT</code>, conditional <code>UPDATE</code>, and scoped <code>DELETE</code>—always pair mutating statements with a selective <code>WHERE</code>.</p>",
    "<p>Defines an <code>user_events</code> fact table (JSONB for flexible payloads) and a materialized view aggregating funnel metrics per product.</p>",
    "<p>Outer query joins events to products and computes conversion-style rates—typical engagement dashboard SQL.</p>",
    "<p>Illustrative DDL with <code>ENCRYPTED</code> markers—real systems use column encryption or vaults; shows versioning fields on medical records.</p>",
    "<p>Row-level security policy example: only certain roles see rows—Postgres-style; wire-up depends on your auth model.</p>",
    "<p>Contrasts btree, hash, GiST, and GIN—pick the access pattern (equality vs text search vs geometry).</p>",
    "<p>Parent <code>metrics</code> table partitioned by timestamp; child tables hold monthly ranges—prune partitions when dropping old data.</p>",
    "<p><code>LIST</code> partitioning splits <code>sales</code> by region into separate physical tables behind one logical name.</p>",
    "<p>Monthly revenue CTE, then <code>LAG</code> for prior month—month-over-month growth pattern.</p>",
    "<p>Computes percent growth from <code>LAG</code>; guard divide-by-zero on the first month.</p>",
    "<p>Contrasts leaking connections with pooling—pseudo-SQL; real clients use poolers or context managers in app code.</p>",
    "<p>Two bare <code>UPDATE</code>s vs a transactional block with savepoints—illustrates atomic transfers and rollback on failure.</p>",
    "<p>Continuation of PL/pgSQL-style error handling (dialect-specific); nested checks before <code>COMMIT</code>.</p>",
    "<p><code>generate_series</code> builds synthetic customers; cohort CTE groups by signup month and running sum for cumulative count.</p>",
    "<p>Cohort query outer <code>SELECT</code>: orders cohort rows by month and applies a windowed cumulative sum.</p>",
    "<p>Randomized bulk insert for stress testing; windowed <code>NTILE</code> buckets products by revenue quartile.</p>",
    "<p>Aggregates random sales per product: counts, units, revenue, average ticket, and quartile rank—typical product leaderboard query.</p>",
]


def patch_ordered(path: Path, bodies: list[str]) -> int:
    text = path.read_text(encoding="utf-8")
    matches = list(PLACEHOLDER_RE.finditer(text))
    if len(matches) != len(bodies):
        raise SystemExit(
            f"{path.name}: expected {len(bodies)} placeholders, found {len(matches)}"
        )
    out: list[str] = []
    pos = 0
    for m, body in zip(matches, bodies, strict=True):
        out.append(text[pos : m.start()])
        out.append(body)
        pos = m.end()
    out.append(text[pos:])
    path.write_text("".join(out), encoding="utf-8")
    return len(bodies)


def main() -> None:
    p = DOCS / "2-data-wrangling/2.1-sql/intro-databases.md"
    n = patch_ordered(p, INTRO_DATABASES_BODIES)
    print(f"Patched {n} callouts in {p.relative_to(DOCS)}")


if __name__ == "__main__":
    main()
