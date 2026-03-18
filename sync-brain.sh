#!/usr/bin/env bash
# Watch vault for .md changes and auto-commit + push
# Usage: ./sync-brain.sh (runs in background)
# Stop: kill the process or Ctrl+C
set -e

VAULT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEBOUNCE=10  # seconds to wait after last change before pushing

cd "$VAULT_DIR"

echo "Watching $VAULT_DIR for .md changes..."
echo "Auto-commit + push every ${DEBOUNCE}s after changes."
echo "Press Ctrl+C to stop."

fswatch -0 -e ".*" -i "\\.md$" -e "\\.git/" -e "\\.qmd/" -e "\\.obsidian/" --latency "$DEBOUNCE" "$VAULT_DIR" | while read -d "" event; do
    # Stage all markdown changes
    git add -A "*.md" 2>/dev/null || true

    # Check if there's anything to commit
    if ! git diff --cached --quiet 2>/dev/null; then
        TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
        COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')
        git commit -m "vault: sync ${COUNT} file(s) — ${TIMESTAMP}" --no-gpg-sign
        git push origin main
        echo "[${TIMESTAMP}] Pushed ${COUNT} file(s)"

        # Re-index QMD
        qmd update 2>/dev/null || true
        qmd embed 2>/dev/null || true
    fi
done
