import os
from pathlib import Path

# Paths
VAULT = Path("/Users/paul/vault/twitter")
AGENT = VAULT / "agent"
DIGESTS = VAULT / "digests"
DRAFTS = AGENT / "drafts"
METRICS = AGENT / "metrics"
PATTERNS_DIR = AGENT / "patterns"
KG = Path("/Users/paul/vault/twitter/knowledge-graph")

# Knowledge graph files
DB_PATH = KG / "tweets.db"
PATTERNS_JSON = KG / "patterns.json"
TOPICS_JSON = KG / "topics.json"

# Agent config files
VOICE_CARD = AGENT / "voice-card.md"
BLACKLIST = AGENT / "blacklist.md"
TOPICS_RANKING = AGENT / "niche" / "topics-ranking.md"
HOOKS_PATTERNS = PATTERNS_DIR / "hooks-that-work.md"

# clix binary
CLIX = "clix"

# Twitter handle (Paul's account — set in env or hardcode here)
TWITTER_HANDLE = os.getenv("TWITTER_HANDLE", "")

# Drafts per day target
DRAFTS_PER_DAY = 7

# Ensure dirs exist
for d in [DIGESTS, DRAFTS, METRICS, KG]:
    d.mkdir(parents=True, exist_ok=True)
