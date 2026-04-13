#!/bin/bash
# Setup cron jobs for Twitter Agent
# Run once: chmod +x setup-crons.sh && ./setup-crons.sh

SYSTEM_DIR="/Users/paul/vault/twitter/system"
PYTHON="$SYSTEM_DIR/.venv/bin/python"
LOG_DIR="/Users/paul/twitter-agent/logs"

mkdir -p "$LOG_DIR"

CURRENT=$(crontab -l 2>/dev/null || echo "")

NEW_JOBS=$(cat <<EOF

# === Twitter Agent ===
# Scrape feed: 08:00, 13:00, 19:30
0 8 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1
0 13 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1
30 19 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1

# Generate drafts: 07:30
30 7 * * * cd $SYSTEM_DIR && $PYTHON main.py draft >> $LOG_DIR/drafter.log 2>&1

# Find reply opportunities: 09:00, 14:00, 18:00
0 9 * * * cd $SYSTEM_DIR && $PYTHON main.py replies >> $LOG_DIR/replies.log 2>&1
0 14 * * * cd $SYSTEM_DIR && $PYTHON main.py replies >> $LOG_DIR/replies.log 2>&1
0 18 * * * cd $SYSTEM_DIR && $PYTHON main.py replies >> $LOG_DIR/replies.log 2>&1

# Embed new tweets: 21:00 daily
0 21 * * * cd $SYSTEM_DIR && $PYTHON main.py embed >> $LOG_DIR/embedder.log 2>&1

# Track metrics: 22:00 daily
0 22 * * * cd $SYSTEM_DIR && $PYTHON main.py track >> $LOG_DIR/tracker.log 2>&1

# Retrain model: Sunday 23:30 (once enough data)
30 23 * * 0 cd $SYSTEM_DIR && $PYTHON main.py train >> $LOG_DIR/train.log 2>&1

# Weekly style analysis: Monday 06:00
0 6 * * 1 cd $SYSTEM_DIR && $PYTHON main.py style >> $LOG_DIR/style.log 2>&1
# === End Twitter Agent ===
EOF
)

if echo "$CURRENT" | grep -q "Twitter Agent"; then
    echo "Cron jobs already installed."
    echo "To update: crontab -e"
else
    (echo "$CURRENT"; echo "$NEW_JOBS") | crontab -
    echo "Cron jobs installed!"
    echo ""
    echo "Schedule:"
    echo "  07:30 — Generate drafts"
    echo "  08:00 — Morning scrape"
    echo "  09:00 — Find reply opportunities"
    echo "  13:00 — Midday scrape"
    echo "  14:00 — Midday replies"
    echo "  18:00 — Evening replies"
    echo "  19:30 — Evening scrape"
    echo "  21:00 — Embed new tweets"
    echo "  22:00 — Track metrics"
    echo "  Sunday 23:30 — Retrain model"
    echo "  Monday 06:00 — Weekly style analysis"
fi

echo ""
echo "WEEK 1 — Run this first:"
echo "  cd $SYSTEM_DIR && $PYTHON main.py week1"
echo ""
echo "Then daily:"
echo "  Review: open /Users/paul/twitter-agent/drafts/\$(date +%Y-%m-%d).md"
echo "  Post:   $PYTHON main.py post"
