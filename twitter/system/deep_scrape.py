"""
Deep scrape specific accounts — 24 monthly windows, all tweets.
"""
import time, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from db import init_db
from mass_collector import scrape_account_windowed, load_progress, save_progress

TARGETS = [
    "Hesamation",
    "gregisenberg",
    "Frenchie_",
    "poetengineer__",   # top up
    "BrivaelFr",        # top up
]

def run():
    init_db()
    progress = load_progress()
    for handle in TARGETS:
        done = len(progress.get("account_windows_done", {}).get(handle, []))
        if done >= 24:
            print(f"@{handle}: already complete ({done} windows)")
            continue
        print(f"@{handle}: scraping 24 months...")
        n = scrape_account_windowed(handle, months_back=24, progress=progress)
        progress.setdefault("account_windows_done", {})[handle] = progress["account_windows_done"].get(handle, [])
        save_progress(progress)
        print(f"  → {n} tweets stored")
        time.sleep(2)

if __name__ == "__main__":
    run()
