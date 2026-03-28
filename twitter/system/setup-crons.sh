#!/bin/bash
# Setup cron jobs for the Twitter agent
# Run once: chmod +x setup-crons.sh && ./setup-crons.sh

PYTHON="python3"
SYSTEM_DIR="/Users/paul/vault/twitter/system"
LOG_DIR="/Users/paul/vault/twitter/logs"

mkdir -p "$LOG_DIR"

# Current crontab
CURRENT=$(crontab -l 2>/dev/null || echo "")

# New jobs
NEW_JOBS=$(cat <<EOF

# === Twitter Agent ===
# Scrape feed: 08:00, 13:00, 19:00
0 8 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1
0 13 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1
0 19 * * * cd $SYSTEM_DIR && $PYTHON main.py scrape >> $LOG_DIR/scraper.log 2>&1

# Generate drafts: 07:30 (before first scrape window)
30 7 * * * cd $SYSTEM_DIR && $PYTHON main.py draft >> $LOG_DIR/drafter.log 2>&1

# Note: posting uses clix schedule (native Twitter scheduling), no cron needed for posting
# Just run "python main.py post" after approving drafts in the morning

# Track metrics: 22:00 daily
0 22 * * * cd $SYSTEM_DIR && $PYTHON main.py track >> $LOG_DIR/tracker.log 2>&1

# Weekly analysis: Sunday 23:00
0 23 * * 0 cd $SYSTEM_DIR && $PYTHON main.py analyze >> $LOG_DIR/analyst.log 2>&1
# === End Twitter Agent ===
EOF
)

# Add to crontab if not already present
if echo "$CURRENT" | grep -q "Twitter Agent"; then
    echo "Cron jobs already configured. To update, run: crontab -e"
else
    (echo "$CURRENT"; echo "$NEW_JOBS") | crontab -
    echo "Cron jobs installed successfully!"
    echo ""
    echo "Schedule:"
    echo "  07:30 — Generate drafts (Claude API)"
    echo "  08:00 — First scrape"
    echo "  08:30-23:00 — Post approved tweets every 30min"
    echo "  13:00 — Midday scrape"
    echo "  19:00 — Evening scrape"
    echo "  22:00 — Track metrics"
    echo "  Sunday 23:00 — Weekly pattern analysis"
fi

echo ""
echo "Next steps:"
echo "  1. cp .env.example .env && edit .env (add ANTHROPIC_API_KEY + TWITTER_HANDLE)"
echo "  2. python main.py scrape  (test the scraper)"
echo "  3. python main.py draft   (generate first drafts)"
echo "  4. python main.py review  (read the drafts)"
echo "  5. Edit vault/twitter/agent/drafts/$(date +%Y-%m-%d).md (approve with [A])"
echo "  6. python main.py post --dry (dry run)"
echo "  7. python main.py post (post for real)"
