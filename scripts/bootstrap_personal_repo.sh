#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

REPO_SLUG="${REPO_SLUG:-harirsingh25-source/data-ai-review-studio}"
VISIBILITY="${VISIBILITY:-public}"

echo "Preparing $REPO_SLUG"

if ! command -v gh >/dev/null 2>&1; then
  echo "ERROR: GitHub CLI (gh) is required." >&2
  echo "Install it, then run: gh auth status" >&2
  exit 1
fi

gh auth status

if [[ ! -d .git ]]; then
  git init -b main
fi

git add .

if ! git diff --cached --quiet; then
  git commit -m "Launch Data & AI Review Studio"
fi

if git remote get-url origin >/dev/null 2>&1; then
  echo "Origin already exists: $(git remote get-url origin)"
  git push -u origin HEAD
else
  gh repo create "$REPO_SLUG" \
    "--$VISIBILITY" \
    --source=. \
    --remote=origin \
    --push
fi

echo
echo "Repository:"
echo "https://github.com/$REPO_SLUG"
