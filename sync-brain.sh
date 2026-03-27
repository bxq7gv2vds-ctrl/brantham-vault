#!/usr/bin/env bash
# Daemon: watch vault for .md changes and auto-commit + push
# Managed by LaunchAgent com.paul.vault-sync
# Manual: ./sync-brain.sh
# Logs: ~/.cache/vault-sync.log
set -euo pipefail

VAULT_DIR="$(cd "$(dirname "$0")" && pwd)"
DEBOUNCE=10

cd "$VAULT_DIR"

echo "[$(date)] vault-sync started — watching $VAULT_DIR"

fswatch -0 \
    -e ".*" -i "\\.md$" \
    -e "\\.git/" -e "\\.qmd/" -e "\\.obsidian/" \
    --latency "$DEBOUNCE" \
    "$VAULT_DIR" | while read -d "" event; do

    # Stage all changes (md + new files like scripts, templates)
    git add -A 2>/dev/null || true

    # Nothing to commit? skip
    if git diff --cached --quiet 2>/dev/null; then
        continue
    fi

    TIMESTAMP=$(date "+%Y-%m-%d %H:%M")
    COUNT=$(git diff --cached --name-only | wc -l | tr -d ' ')
    MSG="vault: sync ${COUNT} file(s) — ${TIMESTAMP}"

    if git commit -m "$MSG" --no-gpg-sign 2>&1; then
        # Pull remote changes first to avoid rejection
        git pull --rebase origin main 2>&1 || {
            echo "[${TIMESTAMP}] ERROR: pull --rebase failed, aborting rebase"
            git rebase --abort 2>/dev/null
            continue
        }
        if git push origin main 2>&1; then
            echo "[${TIMESTAMP}] Pushed ${COUNT} file(s)"
        else
            echo "[${TIMESTAMP}] ERROR: push failed (will retry on next change)"
        fi
    else
        echo "[${TIMESTAMP}] ERROR: commit failed"
    fi
done
