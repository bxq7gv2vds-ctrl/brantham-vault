"""
Rich feature extraction — 57 features per tweet.
Text + structural + linguistic + temporal + account features.
"""
import re
import numpy as np
from datetime import datetime
from typing import Optional


FEATURE_NAMES = [
    # --- Length features ---
    "char_len", "word_count", "sentence_count", "avg_word_len",
    "avg_sentence_len", "max_sentence_len", "min_sentence_len",
    # --- Structural features ---
    "line_breaks", "has_list", "has_numbered_list", "paragraph_count",
    "starts_lowercase", "ends_with_period", "ends_with_question",
    "ends_with_exclaim", "has_quotes", "has_parentheses",
    # --- Linguistic features ---
    "has_numbers", "specific_numbers", "pct_numbers",
    "caps_ratio", "has_caps_word", "has_all_caps_line",
    "exclamation_count", "question_count", "comma_count",
    "dot_dot_dot", "dash_count",
    # --- Content features ---
    "has_code_ref", "has_ai_ref", "has_builder_ref", "has_tool_ref",
    "has_url", "has_mention", "has_media_ref",
    # --- Style features ---
    "is_franglais", "is_hot_take", "is_prediction", "is_builder_flex",
    "is_contrarian", "is_observation", "is_humor", "is_question_tweet",
    "is_list_tweet", "is_thread_opener",
    # --- Hook features ---
    "hook_starts_with_i", "hook_starts_direct", "hook_has_number",
    "hook_has_question", "hook_length",
    # --- Temporal features ---
    "hour", "day_of_week", "is_morning", "is_afternoon",
    "is_evening", "is_late_night", "is_weekend",
]

assert len(FEATURE_NAMES) == 57, f"Expected 57 features, got {len(FEATURE_NAMES)}"


def extract(text: str, created_at: Optional[str] = None) -> np.ndarray:
    if not text:
        return np.zeros(len(FEATURE_NAMES), dtype=np.float32)

    t = text.strip()
    words = t.split()
    sentences = [s.strip() for s in re.split(r'[.!?]+', t) if s.strip()]
    lines = t.split('\n')
    hook = t[:100]

    # Length
    char_len = len(t)
    word_count = len(words)
    sentence_count = max(1, len(sentences))
    avg_word_len = np.mean([len(w) for w in words]) if words else 0
    avg_sent_len = word_count / sentence_count
    max_sent_len = max((len(s.split()) for s in sentences), default=0)
    min_sent_len = min((len(s.split()) for s in sentences), default=0)

    # Structural
    line_breaks = t.count('\n')
    has_list = int(bool(re.search(r'^[•\-\*]', t, re.MULTILINE)))
    has_numbered = int(bool(re.search(r'^\d+[\.\)]\s', t, re.MULTILINE)))
    paragraph_count = max(1, len([l for l in t.split('\n\n') if l.strip()]))
    starts_lower = int(t[0].islower() if t else False)
    ends_period = int(t.rstrip().endswith('.'))
    ends_question = int(t.rstrip().endswith('?'))
    ends_exclaim = int(t.rstrip().endswith('!'))
    has_quotes = int('"' in t or '\u201c' in t or '\u201d' in t)
    has_parens = int('(' in t and ')' in t)

    # Linguistic
    numbers = re.findall(r'\d+', t)
    has_numbers = int(bool(numbers))
    specific_numbers = int(bool(re.findall(r'\b\d{3,}\b', t)))
    pct_numbers = len(''.join(re.findall(r'\d', t))) / max(1, char_len)
    caps_chars = sum(1 for c in t if c.isupper())
    caps_ratio = caps_chars / max(1, char_len)
    has_caps_word = int(bool(re.search(r'\b[A-Z]{3,}\b', t)))
    has_all_caps_line = int(any(l == l.upper() and len(l) > 10 and l.strip() for l in lines))
    excl_count = t.count('!')
    quest_count = t.count('?')
    comma_count = t.count(',')
    dot_dot = int('...' in t)
    dash_count = t.count('-') + t.count('\u2014')

    # Content
    tl = t.lower()
    has_code = int(bool(re.search(r'\b(claude|gpt|llm|api|python|js|react|fastapi|django|docker|git|deploy|ship|cursor|copilot|anthropic|openai)\b', tl)))
    has_ai = int(bool(re.search(r'\b(ai|agent|model|training|inference|embedding|rag|prompt|token|context|llm|ml|neural)\b', tl)))
    has_builder = int(bool(re.search(r'\b(build|built|ship|shipped|launch|deploy|code|dev|startup|founder|solo)\b', tl)))
    has_tool = int(bool(re.search(r'\b(tool|app|product|feature|saas|workflow|automation|pipeline|script)\b', tl)))
    has_url = int('http' in t)
    has_mention = int('@' in t[5:])
    has_media = int(bool(re.search(r'\b(image|video|screenshot|photo|demo|gif|thread)\b', tl)))

    # Style
    is_franglais = int(bool(re.search(r'\b(le|la|les|je|tu|on|en|de|du|des|un|une|c\'est|j\'ai|pas|plus|avec|pour|dans|sur|truc|genre|vraiment|surtout)\b', tl)))
    is_hot_take = int(bool(re.search(r'\b(wrong|unpopular|nobody|stop|don\'t|nope|actually|no one|faux|personne)\b', tl)))
    is_prediction = int(bool(re.search(r'\b(calling it|mark my words|in \d+ months|dans \d+ mois|prediction|will be|va etre|future)\b', tl)))
    is_builder_flex = int(bool(re.search(r'\b(built|shipped|launched|just deployed|j\'ai build|j\'ai ship|finished|done|live)\b', tl)))
    is_contrarian = int(bool(re.search(r'\b(actually|but|however|contrary|disagree|wrong|faux|mais en vrai|en fait non)\b', tl)))
    is_observation = int(bool(re.search(r'\b(genuinely|fascinating|interesting that|wild|le truc c\'est|en vrai|j\'ai remarque)\b', tl)))
    is_humor = int(bool(re.search(r'\b(lol|mdr|ah oui|3h du mat|localhost|crash|encore|wtf|bruh|mes freres)\b', tl)))
    is_question = int(quest_count >= 1 and quest_count <= 2 and char_len < 200)
    is_list = int(has_list or has_numbered or line_breaks >= 3)
    is_thread = int(bool(re.search(r'(thread|🧵|\(1\/|\[1\/)', t)))

    # Hook (first 100 chars)
    hook_i = int(hook.lower().startswith('i ') or hook.lower().startswith("i'"))
    hook_direct = int(not hook_i and not hook.lower().startswith('the ') and not hook.startswith('A '))
    hook_number = int(bool(re.search(r'^\d+', hook.strip())))
    hook_question = int('?' in hook)
    hook_len = len(hook.split())

    # Temporal
    hour, dow, is_morn, is_after, is_eve, is_late, is_wknd = 12, 1, 0, 0, 1, 0, 0
    if created_at:
        try:
            dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            hour = dt.hour
            dow = dt.weekday()
            is_morn = int(6 <= hour < 12)
            is_after = int(12 <= hour < 17)
            is_eve = int(17 <= hour < 22)
            is_late = int(hour >= 22 or hour < 6)
            is_wknd = int(dow >= 5)
        except (ValueError, AttributeError):
            pass

    return np.array([
        char_len, word_count, sentence_count, avg_word_len,
        avg_sent_len, max_sent_len, min_sent_len,
        line_breaks, has_list, has_numbered, paragraph_count,
        starts_lower, ends_period, ends_question,
        ends_exclaim, has_quotes, has_parens,
        has_numbers, specific_numbers, pct_numbers,
        caps_ratio, has_caps_word, has_all_caps_line,
        excl_count, quest_count, comma_count,
        dot_dot, dash_count,
        has_code, has_ai, has_builder, has_tool,
        has_url, has_mention, has_media,
        is_franglais, is_hot_take, is_prediction, is_builder_flex,
        is_contrarian, is_observation, is_humor, is_question,
        is_list, is_thread,
        hook_i, hook_direct, hook_number,
        hook_question, hook_len,
        hour, dow, is_morn, is_after,
        is_eve, is_late, is_wknd,
    ], dtype=np.float32)


def extract_batch(texts: list[str], created_ats: list[str] = None) -> np.ndarray:
    if created_ats is None:
        created_ats = [None] * len(texts)
    return np.stack([extract(t, ca) for t, ca in zip(texts, created_ats)])
