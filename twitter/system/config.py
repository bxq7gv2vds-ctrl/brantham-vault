import os
from pathlib import Path

# ============================================================
# Twitter Agent — paths OUTSIDE the Brantham vault
# Knowledge graph and agent data live in /Users/paul/twitter-agent/
# ============================================================

# /Users/paul/twitter-agent/ is a standalone Obsidian vault (separate from Brantham vault)
BASE = Path("/Users/paul/twitter-agent")

DIGESTS = BASE / "digests"
DRAFTS = BASE / "drafts"        # daily draft queues — readable in Obsidian
METRICS = BASE / "metrics"      # daily + weekly reports — readable in Obsidian
PATTERNS_DIR = BASE / "patterns"  # style analyses — readable in Obsidian
ACCOUNTS_DIR = BASE / "accounts"  # account analyses — readable in Obsidian
LEARNING_DIR = BASE / "learning"  # model progress — readable in Obsidian
KG = BASE / "knowledge-graph"   # SQLite + pkl (binary, not Obsidian-readable)

# Knowledge graph files
DB_PATH = KG / "tweets.db"
PATTERNS_JSON = KG / "patterns.json"
TOPICS_JSON = KG / "topics.json"

# Agent config files (voice card etc. stay in vault/twitter/agent/ — that's fine)
AGENT_VAULT = Path("/Users/paul/vault/twitter/agent")
VOICE_CARD = AGENT_VAULT / "voice-card.md"
BLACKLIST = AGENT_VAULT / "blacklist.md"
TOPICS_RANKING = AGENT_VAULT / "niche" / "topics-ranking.md"
HOOKS_PATTERNS = AGENT_VAULT / "patterns" / "hooks-that-work.md"

# clix binary
CLIX = "clix"

# Twitter handle
TWITTER_HANDLE = os.getenv("TWITTER_HANDLE", "")

# Drafts per day
DRAFTS_PER_DAY = 7

# Ensure dirs exist
for d in [DIGESTS, DRAFTS, METRICS, PATTERNS_DIR, ACCOUNTS_DIR, LEARNING_DIR, KG]:
    d.mkdir(parents=True, exist_ok=True)
