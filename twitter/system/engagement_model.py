"""
Engagement Model — predicts whether a tweet will perform well.
Trains on the corpus of collected tweets (engagement_rate as target).
Self-improves weekly as more data accumulates from posted tweets.

Features: text features + metadata → engagement score (0-1)
Model: GradientBoosting (sklearn) — lightweight, interpretable, fast on M5
"""
import json
import re
import pickle
import sqlite3
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Optional

from config import DB_PATH, KG

MODEL_PATH = KG / "engagement_model.pkl"
FEATURE_STATS_PATH = KG / "feature_stats.json"

# Accounts with big audiences — their features don't translate to small accounts
EXCLUDE_MEGA_ACCOUNTS = {"claudeai", "openai", "anthropic", "sama", "elonmusk"}


# ─── Feature Extraction ───────────────────────────────────────────────

def extract_features(text: str, metadata: dict = None) -> dict:
    """Extract features from a tweet text + optional metadata."""
    m = metadata or {}

    # Text features
    length = len(text)
    word_count = len(text.split())
    has_numbers = bool(re.search(r'\d+', text))
    has_specific_numbers = bool(re.search(r'\b\d{2,}\b', text))  # 2+ digit numbers
    has_question = '?' in text
    has_caps_word = bool(re.search(r'\b[A-Z]{3,}\b', text))  # CAPS word
    has_code_ref = bool(re.search(r'(claude|gpt|llm|api|python|code|agent|deploy|ship)', text.lower()))
    has_at_mention = '@' in text[10:]  # mention after first 10 chars = reply
    has_url = 'http' in text
    has_colon_list = ': ' in text and any(c in text for c in ['•', '-', '\n'])
    line_breaks = text.count('\n')
    starts_with_lowercase = text[0].islower() if text else False
    franglais = bool(re.search(r'\b(le|la|les|je|tu|il|mon|ton|son|on|en|de|du|des|un|une|c\'est|j\'ai|pas|plus|avec|pour|dans|sur)\b', text.lower()))
    ends_with_period = text.rstrip().endswith('.')
    sentence_count = max(1, text.count('.') + text.count('!') + text.count('?'))
    avg_sentence_len = word_count / sentence_count

    # Hook type features
    text_lower = text.lower()[:100]
    is_builder_flex = bool(re.search(r'\b(built|shipped|launched|j\'ai build|j\'ai ship|deployed|finished)\b', text_lower))
    is_prediction = bool(re.search(r'\b(calling it|mark my words|in \d+ months|dans \d+ mois|prediction)\b', text_lower))
    is_contrarian = bool(re.search(r'\b(wrong|unpopular|nobody|stop|don\'t|ne pas|stop de)\b', text_lower))
    is_observation = bool(re.search(r'\b(genuinely|wild|fascinating|interesting that|le truc|en vrai)\b', text_lower))
    is_humor = bool(re.search(r'\b(lol|mdr|ah oui|3h du mat|localhost|crash|encore)\b', text_lower))

    # Engagement signals from metadata
    author_followers = m.get("author_followers", 1000)  # default assumption
    hour_posted = m.get("hour", 12)
    day_of_week = m.get("day_of_week", 1)  # 0=Monday

    return {
        "length": length,
        "word_count": word_count,
        "has_numbers": int(has_numbers),
        "has_specific_numbers": int(has_specific_numbers),
        "has_question": int(has_question),
        "has_caps_word": int(has_caps_word),
        "has_code_ref": int(has_code_ref),
        "has_at_mention": int(has_at_mention),
        "has_url": int(has_url),
        "has_colon_list": int(has_colon_list),
        "line_breaks": min(line_breaks, 10),
        "starts_lowercase": int(starts_with_lowercase),
        "is_franglais": int(franglais),
        "ends_with_period": int(ends_with_period),
        "avg_sentence_len": avg_sentence_len,
        "is_builder_flex": int(is_builder_flex),
        "is_prediction": int(is_prediction),
        "is_contrarian": int(is_contrarian),
        "is_observation": int(is_observation),
        "is_humor": int(is_humor),
        "hour_posted": hour_posted,
        "day_of_week": day_of_week,
    }


FEATURE_NAMES = list(extract_features("sample text").keys())


def features_to_array(features: dict) -> np.ndarray:
    return np.array([features[k] for k in FEATURE_NAMES], dtype=np.float32)


# ─── Training Data ────────────────────────────────────────────────────

def load_training_data() -> tuple[np.ndarray, np.ndarray]:
    """Load tweets with engagement data as training set."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    # Use feed_tweets where we have real engagement
    rows = conn.execute("""
        SELECT text, likes, retweets, bookmarks, views,
               engagement_rate, author_handle, created_at
        FROM feed_tweets
        WHERE is_retweet = 0
          AND views > 100
          AND text IS NOT NULL
          AND length(text) > 20
          AND author_handle NOT IN ('claudeai', 'openai', 'anthropic')
    """).fetchall()

    # Also use posted_tweets (ground truth for Paul's account)
    posted = conn.execute("""
        SELECT content as text, likes, retweets, bookmarks, impressions as views,
               engagement_rate, time_posted as created_at
        FROM posted_tweets
        WHERE views > 0
    """).fetchall()

    conn.close()

    all_rows = [dict(r) for r in rows] + [dict(r) for r in posted]
    if len(all_rows) < 20:
        print(f"[engagement_model] Not enough training data yet ({len(all_rows)} samples, need 20+)")
        return None, None

    X, y = [], []
    for row in all_rows:
        text = row.get("text") or ""
        try:
            created_at = datetime.fromisoformat((row.get("created_at") or "").replace("Z", "+00:00"))
            hour = created_at.hour
            day = created_at.weekday()
        except (ValueError, AttributeError):
            hour, day = 12, 1

        feats = extract_features(text, {"hour": hour, "day_of_week": day})
        eng_rate = float(row.get("engagement_rate") or 0)

        X.append(features_to_array(feats))
        y.append(eng_rate)

    return np.array(X), np.array(y)


# ─── Training ─────────────────────────────────────────────────────────

def train() -> dict:
    """Train the engagement model. Returns training metrics."""
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.model_selection import cross_val_score
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    X, y = load_training_data()
    if X is None:
        return {"error": "Not enough data"}

    print(f"[engagement_model] Training on {len(X)} samples...")

    # Log-transform target (engagement rates are skewed)
    y_log = np.log1p(y)

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("gbm", GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=4,
            subsample=0.8,
            random_state=42,
        ))
    ])

    # Cross-validation score
    if len(X) >= 50:
        cv_scores = cross_val_score(model, X, y_log, cv=5, scoring="r2")
        r2_mean = cv_scores.mean()
        print(f"[engagement_model] CV R² = {r2_mean:.3f} ± {cv_scores.std():.3f}")
    else:
        r2_mean = 0.0

    model.fit(X, y_log)

    # Feature importance
    gbm = model.named_steps["gbm"]
    importances = sorted(
        zip(FEATURE_NAMES, gbm.feature_importances_),
        key=lambda x: x[1], reverse=True
    )

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    metrics = {
        "trained_at": datetime.now().isoformat(),
        "n_samples": len(X),
        "r2_cv": round(r2_mean, 4),
        "top_features": [{"name": k, "importance": round(v, 4)} for k, v in importances[:10]],
    }

    with open(FEATURE_STATS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"[engagement_model] Model saved → {MODEL_PATH}")
    print(f"[engagement_model] Top features: {[f['name'] for f in metrics['top_features'][:5]]}")
    return metrics


# ─── Prediction ───────────────────────────────────────────────────────

def load_model():
    if not MODEL_PATH.exists():
        return None
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def predict_score(text: str, metadata: dict = None) -> float:
    """
    Predict engagement score for a tweet text.
    Returns a score from 0.0 to 1.0 (relative performance prediction).
    Returns 0.5 if model not trained yet.
    """
    model = load_model()
    if model is None:
        return 0.5

    feats = extract_features(text, metadata or {})
    X = features_to_array(feats).reshape(1, -1)
    log_pred = model.predict(X)[0]
    raw = float(np.expm1(log_pred))

    # Normalize to 0-1 range based on observed distribution
    stats = {}
    if FEATURE_STATS_PATH.exists():
        try:
            stats = json.loads(FEATURE_STATS_PATH.read_text())
        except json.JSONDecodeError:
            pass

    # Cap at reasonable max
    score = min(1.0, max(0.0, raw / 10.0))
    return round(score, 3)


def score_drafts(drafts: list[dict]) -> list[dict]:
    """Score a list of drafts and sort by predicted engagement."""
    scored = []
    for d in drafts:
        content = d.get("content") or d.get("text", "")
        score = predict_score(content)
        scored.append({**d, "engagement_score": score})

    scored.sort(key=lambda x: x["engagement_score"], reverse=True)
    return scored


def get_model_status() -> str:
    if not MODEL_PATH.exists():
        return "not trained"
    if not FEATURE_STATS_PATH.exists():
        return "trained (no stats)"
    stats = json.loads(FEATURE_STATS_PATH.read_text())
    return (
        f"trained — {stats.get('n_samples',0)} samples, "
        f"R²={stats.get('r2_cv',0):.3f}, "
        f"top feature: {stats.get('top_features',[{}])[0].get('name','?')}"
    )


if __name__ == "__main__":
    import sys
    if "--predict" in sys.argv:
        idx = sys.argv.index("--predict")
        text = sys.argv[idx + 1] if idx + 1 < len(sys.argv) else "test tweet"
        score = predict_score(text)
        print(f"Score: {score:.3f} — '{text[:80]}'")
    else:
        metrics = train()
        print(json.dumps(metrics, indent=2))
