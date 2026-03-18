#!/usr/bin/env bash
# Pull latest vault changes and re-index QMD
set -e

echo "Pulling latest changes..."
git pull --ff-only

echo "Updating index..."
qmd update

echo "Refreshing embeddings..."
qmd embed

echo "Done. Run 'qmd query \"your question\"' to search."
