#!/usr/bin/env python3
"""
Migrate inline ```mermaid``` blocks to external .mmd files.

For each markdown file with mermaid blocks:
  - Creates a diagrams/ directory alongside the file
  - Writes each block to <file-stem>-<n>.mmd
  - Replaces the fenced block with {% include mermaid-diagram.html src="..." %}

The src= path is relative to the docs root so that Jekyll's relative_url
filter produces the correct absolute URL.

Usage:
  uv run python scripts/migrate-mermaid.py [--dry-run] [path-glob]

  path-glob: optional, filter to specific subdir (e.g. "3-data-visualization/3.1*")
  --dry-run: print what would change without writing

Examples:
  uv run python scripts/migrate-mermaid.py --dry-run
  uv run python scripts/migrate-mermaid.py 3-data-visualization/3.1-intro-data-viz
  uv run python scripts/migrate-mermaid.py
"""
import re
import sys
import os
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent.resolve()
MERMAID_RE = re.compile(r'^```mermaid\n(.*?)^```', re.MULTILINE | re.DOTALL)

def should_skip(path: Path) -> bool:
    parts = path.parts
    return any(p in ('_site', 'node_modules', 'slides') for p in parts)

def get_md_files(filter_prefix: str | None = None) -> list[Path]:
    files = []
    for path in sorted(DOCS_ROOT.rglob('*.md')):
        if should_skip(path):
            continue
        if filter_prefix:
            rel = path.relative_to(DOCS_ROOT)
            if not str(rel).startswith(filter_prefix):
                continue
        files.append(path)
    return files

def migrate_file(md_path: Path, dry_run: bool) -> int:
    content = md_path.read_text(encoding='utf-8')
    blocks = MERMAID_RE.findall(content)
    if not blocks:
        return 0

    diagrams_dir = md_path.parent / 'diagrams'
    stem = md_path.stem
    count = 0

    def replacer(m: re.Match) -> str:
        nonlocal count
        count += 1
        diagram_text = m.group(1)
        filename = f'{stem}-{count}.mmd'
        mmd_path = diagrams_dir / filename
        rel_src = mmd_path.relative_to(DOCS_ROOT)

        if not dry_run:
            diagrams_dir.mkdir(exist_ok=True)
            mmd_path.write_text(diagram_text, encoding='utf-8')

        return '{{% include mermaid-diagram.html src="{}" %}}'.format(str(rel_src))

    new_content = MERMAID_RE.sub(replacer, content)

    if new_content != content:
        label = '[dry-run] ' if dry_run else ''
        print(f'{label}Migrated {md_path.relative_to(DOCS_ROOT)} ({count} diagram(s))')
        if not dry_run:
            md_path.write_text(new_content, encoding='utf-8')

    return count

def main():
    args = sys.argv[1:]
    dry_run = '--dry-run' in args
    args = [a for a in args if a != '--dry-run']
    filter_prefix = args[0] if args else None

    files = get_md_files(filter_prefix)
    total_diagrams = 0
    total_files = 0

    for f in files:
        n = migrate_file(f, dry_run)
        if n:
            total_diagrams += n
            total_files += 1

    print(f'\nDone: {total_files} file(s), {total_diagrams} diagram(s)')

if __name__ == '__main__':
    main()
