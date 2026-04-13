"""
Engagement Neural Network — PyTorch multi-task model.
Predicts [log_likes, log_retweets, log_bookmarks] jointly.

Input: tweet embedding (384) + text features (57) = 441 dims
Architecture: 441 → 512 → 256 → 128 → 3
Training: MSE loss, Adam, MPS (Apple Silicon) if available
"""
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np
import sqlite3
import pickle
import json
from pathlib import Path
from datetime import datetime

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))
from config import KG, DB_PATH
from pipeline.features import extract, FEATURE_NAMES

MODEL_PATH = KG / "engagement_net.pt"
SCALER_PATH = KG / "engagement_net_scaler.pkl"
METRICS_PATH = KG / "engagement_net_metrics.json"

INPUT_DIM = 384 + len(FEATURE_NAMES)  # 384 + 57 = 441
DEVICE = (
    torch.device("mps") if torch.backends.mps.is_available()
    else torch.device("cuda") if torch.cuda.is_available()
    else torch.device("cpu")
)


class EngagementNet(nn.Module):
    def __init__(self, input_dim: int = INPUT_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.BatchNorm1d(512),
            nn.ReLU(),
            nn.Dropout(0.3),

            nn.Linear(512, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.2),

            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.1),

            nn.Linear(128, 64),
            nn.ReLU(),

            nn.Linear(64, 3),  # [log_likes, log_rt, log_bookmarks]
        )

    def forward(self, x):
        return self.net(x)


class TweetDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.FloatTensor(X)
        self.y = torch.FloatTensor(y)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


def load_training_data() -> tuple[np.ndarray, np.ndarray]:
    """Load tweets with engagement data. Requires embeddings."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT text, likes, retweets, bookmarks, views,
               created_at, embedding
        FROM feed_tweets
        WHERE embedding IS NOT NULL
          AND views > 100
          AND likes IS NOT NULL
          AND text IS NOT NULL
          AND length(text) > 20
          AND is_retweet = 0
    """).fetchall()

    posted = conn.execute("""
        SELECT content as text, likes, retweets, bookmarks,
               impressions as views, time_posted as created_at, NULL as embedding
        FROM posted_tweets
        WHERE likes IS NOT NULL AND likes > 0
    """).fetchall()
    conn.close()

    all_rows = [dict(r) for r in rows] + [dict(r) for r in posted]

    if len(all_rows) < 30:
        print(f"[engagement_net] Need 30+ samples, got {len(all_rows)}")
        return None, None

    X, y = [], []
    for row in all_rows:
        text = row.get("text") or ""
        created_at = row.get("created_at") or ""

        # Text features
        text_feats = extract(text, created_at)

        # Embedding
        emb_blob = row.get("embedding")
        if emb_blob and len(emb_blob) == 384 * 4:
            emb = np.frombuffer(emb_blob, dtype=np.float32)
        else:
            emb = np.zeros(384, dtype=np.float32)

        x = np.concatenate([emb, text_feats])

        # Targets: log-transform to handle skew
        likes = max(0, row.get("likes") or 0)
        rt = max(0, row.get("retweets") or 0)
        bm = max(0, row.get("bookmarks") or 0)
        y_vec = np.array([
            np.log1p(likes),
            np.log1p(rt),
            np.log1p(bm),
        ], dtype=np.float32)

        X.append(x)
        y.append(y_vec)

    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)


def normalize_features(X: np.ndarray, fit: bool = True):
    """StandardScaler equivalent."""
    from sklearn.preprocessing import StandardScaler
    if fit:
        scaler = StandardScaler()
        X_norm = scaler.fit_transform(X)
        with open(SCALER_PATH, "wb") as f:
            pickle.dump(scaler, f)
    else:
        with open(SCALER_PATH, "rb") as f:
            scaler = pickle.load(f)
        X_norm = scaler.transform(X)
    return X_norm.astype(np.float32)


def train(epochs: int = 100, batch_size: int = 64, lr: float = 1e-3) -> dict:
    print(f"[engagement_net] Device: {DEVICE}")

    X, y = load_training_data()
    if X is None:
        return {"error": "insufficient data"}

    print(f"[engagement_net] Training on {len(X)} samples, {X.shape[1]} features")

    X = normalize_features(X, fit=True)

    # Train/val split
    n_val = max(1, int(len(X) * 0.15))
    idx = np.random.permutation(len(X))
    X_train, y_train = X[idx[n_val:]], y[idx[n_val:]]
    X_val, y_val = X[idx[:n_val]], y[idx[:n_val]]

    train_ds = TweetDataset(X_train, y_train)
    val_ds = TweetDataset(X_val, y_val)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size)

    model = EngagementNet(input_dim=X.shape[1]).to(DEVICE)
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)
    criterion = nn.HuberLoss()

    best_val_loss = float('inf')
    best_state = None
    history = []

    for epoch in range(epochs):
        # Train
        model.train()
        train_loss = 0.0
        for xb, yb in train_loader:
            xb, yb = xb.to(DEVICE), yb.to(DEVICE)
            optimizer.zero_grad()
            pred = model(xb)
            loss = criterion(pred, yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            train_loss += loss.item() * len(xb)
        train_loss /= len(train_ds)

        # Validate
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for xb, yb in val_loader:
                xb, yb = xb.to(DEVICE), yb.to(DEVICE)
                val_loss += criterion(model(xb), yb).item() * len(xb)
        val_loss /= len(val_ds)

        scheduler.step()
        history.append({"epoch": epoch, "train": round(train_loss, 4), "val": round(val_loss, 4)})

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}

        if epoch % 20 == 0:
            print(f"  Epoch {epoch:3d}: train={train_loss:.4f} val={val_loss:.4f}")

    # Save best model
    model.load_state_dict(best_state)
    torch.save({
        "state_dict": best_state,
        "input_dim": X.shape[1],
        "trained_at": datetime.now().isoformat(),
        "n_samples": len(X),
    }, MODEL_PATH)

    metrics = {
        "trained_at": datetime.now().isoformat(),
        "device": str(DEVICE),
        "n_samples": len(X),
        "best_val_loss": round(best_val_loss, 4),
        "epochs": epochs,
        "history": history[-10:],  # last 10 epochs
    }
    METRICS_PATH.write_text(json.dumps(metrics, indent=2))

    print(f"[engagement_net] Done. Best val loss: {best_val_loss:.4f} | Saved → {MODEL_PATH}")
    return metrics


def load_model() -> EngagementNet | None:
    if not MODEL_PATH.exists():
        return None
    ckpt = torch.load(MODEL_PATH, map_location=DEVICE, weights_only=True)
    model = EngagementNet(input_dim=ckpt["input_dim"]).to(DEVICE)
    model.load_state_dict(ckpt["state_dict"])
    model.eval()
    return model


def predict(text: str, embedding: np.ndarray = None, created_at: str = None) -> dict:
    """
    Predict engagement for a tweet.
    Returns dict with predicted likes, rt, bookmarks and composite score.
    """
    model = load_model()
    if model is None:
        return {"score": 0.5, "likes": 0, "rt": 0, "bookmarks": 0}

    text_feats = extract(text, created_at or "")

    if embedding is None:
        from pipeline.vector_store import embed_text
        embedding = embed_text(text)

    x = np.concatenate([embedding, text_feats]).astype(np.float32)
    x_norm = normalize_features(x.reshape(1, -1), fit=False)
    x_tensor = torch.FloatTensor(x_norm).to(DEVICE)

    with torch.no_grad():
        pred = model(x_tensor).cpu().numpy()[0]

    likes = float(np.expm1(pred[0]))
    rt = float(np.expm1(pred[1]))
    bm = float(np.expm1(pred[2]))

    # Composite score (0-1, normalized)
    score = min(1.0, (likes * 1.0 + rt * 1.5 + bm * 2.0) / 500.0)

    return {
        "score": round(score, 3),
        "predicted_likes": max(0, round(likes)),
        "predicted_rt": max(0, round(rt)),
        "predicted_bookmarks": max(0, round(bm)),
    }


def get_status() -> str:
    if not MODEL_PATH.exists():
        return "not trained"
    if not METRICS_PATH.exists():
        return "trained (no metrics)"
    m = json.loads(METRICS_PATH.read_text())
    return (
        f"trained — {m.get('n_samples',0)} samples, "
        f"val_loss={m.get('best_val_loss',0):.4f}, "
        f"device={m.get('device','?')}, "
        f"at {m.get('trained_at','?')[:10]}"
    )


if __name__ == "__main__":
    metrics = train()
    print(json.dumps(metrics, indent=2, default=str))
