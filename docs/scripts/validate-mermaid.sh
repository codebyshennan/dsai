#!/usr/bin/env bash
# Validate all .mmd files in the docs directory using mmdc.
# Exits non-zero if any diagram fails.
set -euo pipefail

DOCS_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MMDC="$(node -e "
  const p = require('path');
  const root = p.join('$DOCS_ROOT', 'node_modules', '.bin', 'mmdc');
  require('fs').existsSync(root) ? process.stdout.write(root) : process.stdout.write('mmdc');
" 2>/dev/null || echo mmdc)"

fail=0
count=0

while IFS= read -r -d '' file; do
  relfile="${file#$DOCS_ROOT/}"
  if "$MMDC" -i "$file" > /dev/null 2>&1; then
    count=$((count + 1))
  else
    echo "✗ $relfile"
    "$MMDC" -i "$file" 2>&1 | sed 's/^/  /'
    fail=1
  fi
done < <(find "$DOCS_ROOT" \
  -name "*.mmd" \
  -not -path "*/node_modules/*" \
  -not -path "*/_site/*" \
  -print0 | sort -z)

echo "Validated $count diagram(s)"
[ $fail -eq 0 ] && echo "✓ All passed" || echo "✗ Some failed"
exit $fail
