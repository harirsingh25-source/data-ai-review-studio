#!/usr/bin/env bash
set -euo pipefail

STUDIO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DAILY_REVIEW_ROOT="${1:-$HOME/UniProjects/ds-matcha-transformers-220626-daily-review}"

if [[ ! -d "$DAILY_REVIEW_ROOT/.git" ]]; then
  echo "Daily-review repo not found: $DAILY_REVIEW_ROOT" >&2
  exit 1
fi

mkdir -p "$DAILY_REVIEW_ROOT/kahoot"

cp "$STUDIO_ROOT/protocols/2026-09-11_model-selection-mystery.md" \
   "$DAILY_REVIEW_ROOT/protocols/2026-09-11_Model_Selection_GridSearch_Hari.md"

cp "$STUDIO_ROOT/kahoot/2026-09-11_model-selection.csv" \
   "$DAILY_REVIEW_ROOT/kahoot/2026-09-11_model-selection.csv"

cp "$STUDIO_ROOT/kahoot/2026-09-11_model-selection.xlsx" \
   "$DAILY_REVIEW_ROOT/kahoot/2026-09-11_model-selection.xlsx"

python3 - "$DAILY_REVIEW_ROOT/protocols/README.md" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
if not path.exists():
    print("NOTE: protocols/README.md not found; skipping index update.")
    raise SystemExit(0)

text = path.read_text()

text = text.replace(
    "## Interactive SQL daily review",
    "## Interactive daily reviews",
)
text = text.replace(
    "| Date | Topic | Participant protocol | Browser playground |",
    "| Date | Topic | Participant protocol | Interactive resource |",
)

row = (
    "| 2026-09-11 | Pokémon Model-Selection Mystery | "
    "[Open protocol](2026-09-11_Model_Selection_GridSearch_Hari.md) | "
    "[Data & AI Review Studio](https://github.com/harirsingh25-source/data-ai-review-studio) |"
)

if row not in text:
    sql_row = (
        "| 2026-07-14 | SQL Dinner-Party Mystery | "
        "[Open protocol](2026-07-14_SQL_Daily_Review_Hari.md) | "
        "[Launch playground](https://neuefische.github.io/ds-matcha-transformers-220626-daily-review/) |"
    )
    if sql_row in text:
        text = text.replace(sql_row, sql_row + "\n" + row, 1)
    else:
        text += "\n\n## Interactive daily reviews\n\n"
        text += "| Date | Topic | Participant protocol | Interactive resource |\n"
        text += "|---|---|---|---|\n"
        text += row + "\n"

path.write_text(text)
print("Updated protocols/README.md index.")
PY

echo
echo "Copied official-review artifacts and indexed the new review."
echo
git -C "$DAILY_REVIEW_ROOT" status --short
