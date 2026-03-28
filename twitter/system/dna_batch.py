"""
Batch DNA extraction for all high-value accounts.
Analyzes existing DB data first, scrapes missing accounts after.

Usage:
  python dna_batch.py          — analyze all (scrape if needed)
  python dna_batch.py --quick  — analyze only accounts already in DB
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from db import get_conn
from reply_style_analyzer import analyze_account, get_all_tweets, DNA_DIR, scrape_account_replies

# All accounts to analyze
ALL_ACCOUNTS = {
    # Already in DB — enough data
    "levelsio":       {"niche": "indie_builder",     "lang": "en", "why": "OG solo builder, direct/no-hedge, 24K max likes"},
    "steipete":       {"niche": "dev_tools",          "lang": "en", "why": "Dev tools, opinionated, 6K max likes"},
    "buccocapital":   {"niche": "finance_builder",    "lang": "en", "why": "Finance + tech, 19K max likes, very regular"},
    "zostaff":        {"niche": "ai_builder",         "lang": "en", "why": "AI builder, 149 replies analyzed"},
    "poetengineer__": {"niche": "ai_engineer",        "lang": "en", "why": "AI engineer, 843 avg likes, very niche"},
    "lydiahallie":    {"niche": "dev_educator",       "lang": "en", "why": "Dev educator, 12K max likes"},
    "BrivaelFr":      {"niche": "fr_builder",         "lang": "fr", "why": "French builder/crypto, 3K max likes"},
    "swyx":           {"niche": "ai_dev",             "lang": "en", "why": "AI educator, adds depth"},
    "Frenchiee":      {"niche": "fr_crypto_builder",  "lang": "fr", "why": "French crypto builder"},
    "gregisenberg":   {"niche": "community_builder",  "lang": "en", "why": "Community + startups, frameworks"},
    "DeItaone":       {"niche": "breaking_news",      "lang": "en", "why": "Breaking news style, 4K max likes"},
    "noahzweben":     {"niche": "ai_builder",         "lang": "en", "why": "AI builder niche"},
    # Need scraping
    "karpathy":       {"niche": "ml_research",        "lang": "en", "why": "ML legend, 37K max likes"},
    "Hesamation":     {"niche": "ai_builder",         "lang": "en", "why": "35K max likes, exploded recently"},
    "alexalbert__":   {"niche": "ai_anthropic",       "lang": "en", "why": "Anthropic, 2K avg likes"},
    "melvynx":        {"niche": "fr_ai_builder",      "lang": "fr", "why": "French AI builder, closest to Paul"},
    "tibo_maker":     {"niche": "fr_saas_builder",    "lang": "fr", "why": "French SaaS builder"},
    "0xDesigner":     {"niche": "ai_design",          "lang": "en", "why": "AI/design, anonymous builder"},
}

MIN_TWEETS = 10  # minimum tweets to run analysis


def check_db_coverage() -> dict:
    conn = get_conn()
    coverage = {}
    for handle in ALL_ACCOUNTS:
        n = conn.execute(
            "SELECT COUNT(*) FROM feed_tweets WHERE LOWER(author_handle)=LOWER(?) AND is_retweet=0",
            (handle,)
        ).fetchone()[0]
        coverage[handle] = n
    conn.close()
    return coverage


def run(quick: bool = False):
    DNA_DIR.mkdir(parents=True, exist_ok=True)
    coverage = check_db_coverage()

    print(f"\n{'='*55}")
    print(f"DNA BATCH — {len(ALL_ACCOUNTS)} accounts")
    print(f"{'='*55}\n")

    results = {}
    to_scrape = []

    for handle, meta in ALL_ACCOUNTS.items():
        n = coverage.get(handle, 0)

        if n >= MIN_TWEETS:
            print(f"[analyze] @{handle} ({n} tweets)...", end=" ", flush=True)
            tweets = get_all_tweets(handle)
            if len(tweets) < MIN_TWEETS:
                print("skip (filtered)")
                continue
            dna = analyze_account(handle, meta)
            if dna.get("error"):
                print(f"error: {dna['error']}")
            else:
                path = DNA_DIR / f"{handle.lower()}.json"
                path.write_text(json.dumps(dna, indent=2, ensure_ascii=False))
                results[handle] = dna
                winning = "/".join(dna.get("winning_structures", [])[:2])
                print(f"ok  ({dna['sample_size']} tweets, {dna['avg_reply_length']}c avg, {winning})")
        else:
            print(f"[skip]    @{handle} — only {n} tweets in DB → needs scraping")
            to_scrape.append(handle)

    if to_scrape and not quick:
        print(f"\n[scrape] {len(to_scrape)} accounts need data: {', '.join(to_scrape)}")
        for handle in to_scrape:
            print(f"\n[scrape] @{handle}...")
            try:
                n = scrape_account_replies(handle, n_windows=4)
                print(f"  → {n} tweets scraped")
                if n >= MIN_TWEETS:
                    meta = ALL_ACCOUNTS[handle]
                    dna = analyze_account(handle, meta)
                    if not dna.get("error"):
                        path = DNA_DIR / f"{handle.lower()}.json"
                        path.write_text(json.dumps(dna, indent=2, ensure_ascii=False))
                        results[handle] = dna
                        print(f"  → DNA saved")
            except Exception as e:
                print(f"  → error: {e}")
            time.sleep(3)

    # Summary
    print(f"\n{'='*55}")
    print(f"RESULTS — {len(results)} DNA files generated\n")
    print(f"{'Handle':20} {'Lang':5} {'Tweets':>7} {'Avg L':>7} {'Winning structures'}")
    print("-"*65)
    for handle, dna in sorted(results.items(), key=lambda x: x[1].get('sample_size', 0), reverse=True):
        lang = dna.get('lang', '?')
        n = dna.get('sample_size', 0)
        avg_l = dna.get('avg_reply_length', 0)
        structs = "/".join(dna.get('winning_structures', [])[:2])
        print(f"@{handle:19} {lang:5} {n:>7} {avg_l:>7} {structs}")

    print(f"\nDNA files → {DNA_DIR}")
    return results


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    run(quick=quick)
