#!/usr/bin/env python3
"""
Heuristic audit for docs/5-ml-fundamentals Markdown:
- Consecutive code fences with only whitespace between (orphan pair risk)
- Python fences whose preceding prose may lack Purpose:/**Purpose:**

Run from docs/: uv run python scripts/audit_ml_fundamentals_code_blocks.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "5-ml-fundamentals"

SKIP_NAMES = frozenset({"GENERATED_RESOURCES_SUMMARY.md", "module-assignment-key.md"})
SKIP_PARTS = ("assignment-key",)


def iter_md_files() -> list[Path]:
    out: list[Path] = []
    for p in sorted(MODULE.rglob("*.md")):
        if p.name in SKIP_NAMES:
            continue
        if any(part in p.parts for part in SKIP_PARTS):
            continue
        out.append(p)
    return out


def has_purpose_context(lines_before: list[str]) -> bool:
    text = "\n".join(lines_before[-12:])
    return bool(
        re.search(r"(?i)\*\*purpose:\*\*|^purpose:", text, re.MULTILINE)
        or re.search(r"(?i)captured stdout|expected output", text)
    )


def audit_file(path: Path) -> tuple[list[str], list[str]]:
    """Returns (orphan_pair_reports, purpose_warnings)."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    orphans: list[str] = []
    purpose: list[str] = []

    # Risky pair: a fence closes, then after only blanks the next fence opens with a
    # *language* (not bare stdout). Bare ``` ... ``` is usually injected stdout.
    i = 0
    while i < len(lines):
        if lines[i].strip() == "```":
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines):
                nxt = lines[j].strip()
                if nxt.startswith("```") and len(nxt) > 3:
                    between = "\n".join(lines[i + 1 : j])
                    if not re.search(
                        r"(?i)captured stdout|expected output|purpose:",
                        between,
                    ):
                        rel = path.relative_to(ROOT)
                        orphans.append(
                            f"{rel}:{j + 1} code fence follows previous fence "
                            f"({nxt}) with no caption between — add Purpose or "
                            f"Captured stdout label"
                        )
        i += 1

    # Python blocks: find ```python
    for idx, line in enumerate(lines):
        if line.strip() != "```python":
            continue
        before = lines[max(0, idx - 15) : idx]
        if not has_purpose_context(before):
            rel = path.relative_to(ROOT)
            purpose.append(f"{rel}:{idx + 1} ```python may need Purpose/title (heuristic)")

    return orphans, purpose


def main() -> int:
    if not MODULE.is_dir():
        print("Expected", MODULE, file=sys.stderr)
        return 1

    all_orphans: list[str] = []
    all_purpose: list[str] = []
    for path in iter_md_files():
        o, p = audit_file(path)
        all_orphans.extend(o)
        all_purpose.extend(p)

    print("=== Consecutive fence pairs (review for captions) ===")
    if not all_orphans:
        print("(none detected)")
    else:
        for x in all_orphans:
            print(x)

    print("\n=== Python fences without nearby Purpose/stdout label (heuristic) ===")
    print(f"Count: {len(all_purpose)}")
    for x in all_purpose[:200]:
        print(x)
    if len(all_purpose) > 200:
        print(f"... and {len(all_purpose) - 200} more")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
