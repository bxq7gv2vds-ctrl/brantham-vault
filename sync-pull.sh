#!/bin/bash
VAULT="$HOME/brantham-vault"
LOG="$VAULT/_system/sync-pull.log"

mkdir -p "$VAULT/_system"

while true; do
    cd "$VAULT" || exit 1
    git fetch origin main 2>/dev/null || git fetch origin master 2>/dev/null

    LOCAL=$(git rev-parse HEAD)
    REMOTE=$(git rev-parse @{u} 2>/dev/null)

    if [ "$LOCAL" != "$REMOTE" ]; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        git pull --rebase origin $(git rev-parse --abbrev-ref HEAD) >> "$LOG" 2>&1
        echo "[$TIMESTAMP] Pull effectué" >> "$LOG"
    fi

    sleep 30
done
