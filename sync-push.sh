#!/bin/bash
VAULT="$HOME/brantham-vault"
LOG="$VAULT/_system/sync-push.log"

mkdir -p "$VAULT/_system"

while true; do
    cd "$VAULT" || exit 1

    if [ -n "$(git status --porcelain)" ]; then
        TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
        git add -A
        git commit -m "sync: $TIMESTAMP"
        git push origin $(git rev-parse --abbrev-ref HEAD) >> "$LOG" 2>&1
        echo "[$TIMESTAMP] Push effectué" >> "$LOG"
    fi

    sleep 30
done
