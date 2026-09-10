# 🏆 Pokémon Model-Selection Mystery

**Date:** 11 September 2026  
**Duration:** approximately 30 minutes  
**Format:** interactive daily review  
**Tools:** Kahoot + Streamlit browser playground  
**Mission:** choose a trustworthy Legendary-Pokémon classifier without learning from the final test set.

## Run of show

| Time | What the class does | Tool |
|---|---|---|
| 0–4 min | Kahoot warm-up: validation, leakage, test set | Kahoot |
| 4–7 min | Story: Pokémon League needs a Legendary classifier | Streamlit |
| 7–11 min | Predict: train/test split vs cross-validation | Streamlit |
| 11–16 min | Change number of folds and inspect the effect | Streamlit |
| 16–23 min | GridSearchCV tournament: KNN vs Random Forest | Streamlit |
| 23–26 min | Diagnose CV score, train score and generalization gap | Streamlit |
| 26–28 min | Final mystery: unlock the untouched test set | Streamlit |
| 28–30 min | Kahoot finale | Kahoot |

## Facilitation rule

> Predict first. Run second. Explain third.

## Story

The Pokémon League has a classifier that reports about **92.5% accuracy**.  
Management asks: **Can we deploy it?**

The class must select between KNN and Random Forest without repeatedly consulting the final test set.

## Learning journey

1. The 92.5% question
2. Lock the test set
3. Cross-validation
4. Stratification
5. KNN scaling challenge
6. Random Forest complexity
7. GridSearchCV tournament
8. Read the scoreboard
9. The forbidden move
10. Final mystery

## Final reveal

The class should arrive at the workflow:

```text
TRAIN
  ↓
CROSS-VALIDATE
  ↓
TUNE
  ↓
SELECT
  ↓
LOCK DECISION
  ↓
TEST ONCE
```

## Finished early

- Change ROC-AUC to accuracy.
- Change the number of folds.
- Remove scaling from KNN.
- Expand the Random Forest grid.
- Discuss runtime versus search coverage.
- Add a third model family.

## Links and references

### Review lineage

- SQL Dinner-Party Mystery: https://hari-raj-singh.com/data-ai/sql/
- Long-lived Review Studio source: https://github.com/harirsingh25-source/data-ai-review-studio
- Official neuefische daily-review repository: https://github.com/neuefische/ds-matcha-transformers-220626-daily-review

### Technical references

- Cross-validation: https://scikit-learn.org/stable/modules/cross_validation.html
- `GridSearchCV`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
- `StratifiedKFold`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
- `Pipeline`: https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
- Streamlit concepts: https://docs.streamlit.io/get-started/fundamentals/main-concepts

### Presentation links

- Presenter/local app: http://localhost:8503
- Kahoot import workbook: `kahoot/2026-09-11_model-selection.xlsx`
- Kahoot source CSV: `kahoot/2026-09-11_model-selection.csv`

After a public Streamlit deployment is created, add its share URL here and in the official daily-review protocol.
