#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

echo "Data & AI Review Studio"
echo "-----------------------"
echo "Syncing environment..."
uv sync

echo
echo "Running tests..."
uv run pytest -q

echo
echo "Launching Streamlit on http://localhost:8503"
exec uv run streamlit run app.py --server.port 8503
