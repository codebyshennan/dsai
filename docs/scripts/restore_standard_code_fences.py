#!/usr/bin/env python3
"""
Restore standard fenced code blocks: ```<lang> on the opening line, closing ```.

Reverses the format where the opening fence was plain ``` and the language
appeared on the line below the closing fence as `lang` (inline code).

Only processes Markdown under course module roots (0-prep … 6-capstone).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PLAIN_OPEN = re.compile(r"^(\s*)```\s*$")
CLOSE_RE = re.compile(r"^\s*```\s*$")
LANG_LINE = re.compile(r"^(\s*)`([A-Za-z0-9][A-Za-z0-9+_-]*)`\s*$")

EXCLUDE_DIR_NAMES = frozenset(
    {"meta", "node_modules", ".git", "vendor", ".jekyll-cache", "_site"}
)
EXCLUDE_FILES = frozenset({"CLAUDE.md"})

MODULE_ROOTS = frozenset(
    {
        "0-prep",
        "1-data-fundamentals",
        "2-data-wrangling",
        "3-data-visualization",
        "4-stat-analysis",
        "5-ml-fundamentals",
        "6-capstone",
    }
)


def _is_under_course_module(path: Path, docs_root: Path) -> bool:
    try:
        rel = path.relative_to(docs_root)
    except ValueError:
        return False
    return len(rel.parts) > 0 and rel.parts[0] in MODULE_ROOTS


def transform(content: str) -> str:
    lines = content.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = PLAIN_OPEN.match(line)
        if m:
            indent = m.group(1)
            j = i + 1
            body: list[str] = []
            while j < len(lines):
                if CLOSE_RE.match(lines[j]):
                    k = j + 1
                    while k < len(lines) and lines[k].strip() == "":
                        k += 1
                    if k < len(lines):
                        lm = LANG_LINE.match(lines[k])
                        if lm and lm.group(1) == indent:
                            lang = lm.group(2)
                            out.append(f"{indent}```{lang}\n")
                            out.extend(body)
                            out.append(lines[j])
                            i = k + 1
                            break
                    out.append(line)
                    out.extend(body)
                    out.append(lines[j])
                    i = j + 1
                    break
                body.append(lines[j])
                j += 1
            else:
                out.append(line)
                i += 1
            continue
        out.append(line)
        i += 1
    return "".join(out)


def main() -> None:
    docs_root = Path(__file__).resolve().parents[1]
    md_files: list[Path] = []
    for p in docs_root.rglob("*.md"):
        if any(part in EXCLUDE_DIR_NAMES for part in p.parts):
            continue
        if p.name in EXCLUDE_FILES:
            continue
        if not _is_under_course_module(p, docs_root):
            continue
        md_files.append(p)
    changed = 0
    for path in sorted(md_files):
        raw = path.read_text(encoding="utf-8")
        new = transform(raw)
        if new != raw:
            path.write_text(new, encoding="utf-8", newline="\n")
            changed += 1
            print(path)
    print(f"Updated {changed} files.", file=sys.stderr)


if __name__ == "__main__":
    main()
