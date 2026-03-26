#!/bin/bash
#
# Install git hooks for this repository
# This sets up pre-commit validation to prevent Jekyll build errors
#

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}Installing Git hooks...${NC}"

# Get repository root
REPO_ROOT=$(git rev-parse --show-toplevel)
HOOKS_SOURCE="$REPO_ROOT/.githooks"
HOOKS_DEST="$REPO_ROOT/.git/hooks"

# Check if source hooks directory exists
if [ ! -d "$HOOKS_SOURCE" ]; then
    echo "Error: Hooks directory not found at $HOOKS_SOURCE"
    exit 1
fi

# Configure git to use our hooks directory
git config core.hooksPath "$HOOKS_SOURCE"

echo -e "${GREEN}✓ Git hooks installed successfully!${NC}"
echo ""
echo "The following hooks are now active:"
echo "  - pre-commit: Validates Jekyll/GitHub Pages compatibility"
echo ""
echo "To disable hooks temporarily, use: git commit --no-verify"
echo "To uninstall: git config --unset core.hooksPath"
