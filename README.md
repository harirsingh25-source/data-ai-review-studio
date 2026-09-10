# Data & AI Review Studio

An interactive classroom-review system built with Streamlit.

The design follows the teaching pattern used by the SQL Dinner-Party Mystery:

> **Predict → experiment → inspect evidence → decide → reveal → final mystery**

## First production module

### 🏆 Pokémon Model-Selection Mystery

A 30-minute daily review covering:

- train / validation / test separation
- locked final test sets
- cross-validation
- `StratifiedKFold`
- leakage
- preprocessing pipelines
- KNN scaling
- Random Forest complexity
- `GridSearchCV`
- train-validation generalization gaps
- final untouched test evaluation

A Kahoot-ready question CSV and presenter protocol are included.

## Future modules

The repository is intentionally modular. Planned reviews:

- 📈 Time-Series Investigation
- 🧠 Attention Detective (Transformers)
- 🔬 Deep Learning Lab (CNN / RNN / LSTM)
- 🧪 A/B Testing Case
- 🚀 MLOps Mission (MLflow / serving / cloud)
- 🍽️ SQL Dinner-Party Mystery integration

## Repository structure

```text
data-ai-review-studio/
├── app.py
├── review_studio/
│   ├── home.py
│   ├── registry.py
│   └── ui.py
├── reviews/
│   └── model_selection/
│       ├── content.py
│       ├── experiments.py
│       └── page.py
├── data/
│   └── pokemon.csv
├── kahoot/
│   └── 2026-09-11_model-selection.csv
├── protocols/
│   └── 2026-09-11_model-selection-mystery.md
├── tests/
│   └── test_model_selection.py
├── pyproject.toml
└── .python-version
```

## Fastest launch

```bash
cd ~/UniProjects/data-ai-review-studio
./scripts/launch.sh
```

This syncs dependencies, runs tests, and launches the app at `http://localhost:8503`.

## Run locally

```bash
uv sync
uv run streamlit run app.py --server.port 8503
```

Then open:

```text
http://localhost:8503
```

Streamlit reruns on save.

## Test

```bash
uv run pytest -q
```

## Create the GitHub repository

From the parent directory:

```bash
cd ~/UniProjects
mv ~/Downloads/data-ai-review-studio ./data-ai-review-studio
cd data-ai-review-studio

git init
git add .
git commit -m "Launch Data & AI Review Studio with model-selection mystery"

gh repo create data-ai-review-studio --private --source=. --remote=origin --push
```

Use `--public` instead if you want the repository public.

## Tomorrow

Present the **Model Selection Mystery** module only. The home screen shows the wider roadmap, but the classroom session stays focused on one polished experience.

## Official daily-review handoff

The long-lived product lives here. Only the class-facing protocol and Kahoot source are mirrored into the official neuefische daily-review repository.

See:

- `OFFICIAL_DAILY_REVIEW_HANDOFF.md`
- `scripts/sync_official_review.sh`
- `REFERENCES.md`

To copy the class artifacts into your already-cloned daily-review repository:

```bash
./scripts/sync_official_review.sh
```

Review the resulting `git diff` before committing or pushing.

## From download to presentation

After downloading and extracting this repo into `~/UniProjects/data-ai-review-studio`:

```bash
cd ~/UniProjects/data-ai-review-studio

./scripts/bootstrap_personal_repo.sh
./scripts/launch.sh
```

This creates/pushes the long-lived public GitHub repository at:

```text
https://github.com/harirsingh25-source/data-ai-review-studio
```

Then mirror only the class-facing artifacts into the official daily-review repository:

```bash
./scripts/sync_official_review.sh
```

Review the official-repo changes:

```bash
cd ~/UniProjects/ds-matcha-transformers-220626-daily-review
git status
git diff
```

Then commit and push them from `hari/review-roadmap`.

### Kahoot

The repository includes both:

```text
kahoot/2026-09-11_model-selection.xlsx
kahoot/2026-09-11_model-selection.csv
```

Use the `.xlsx` workbook for Kahoot's spreadsheet import. The CSV is retained as a simple source/editable representation.
