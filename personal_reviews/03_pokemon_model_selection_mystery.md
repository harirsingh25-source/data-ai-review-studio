# 03 · 🏆 Pokémon Model-Selection Mystery

**Date:** 11 September 2026  
**Duration:** approximately 30 minutes  
**Format:** interactive daily review  
**Tools:** Kahoot + Streamlit browser playground  
**Mission:** choose a trustworthy Legendary-Pokémon classifier without learning from the final test set.

## Connected learning sequence

This review deliberately connects three Data & AI learning experiences:

1. **Supervised ML**  
   https://hari-raj-singh.com/data-ai/supervised-ml/  
   Foundation: model behavior, evaluation, failure analysis and ensembles.

2. **SQL Dinner-Party Mystery**  
   https://hari-raj-singh.com/data-ai/sql/  
   Interaction pattern: ask a precise question, predict, run, inspect evidence, decide, reveal.

3. **Pokémon Model-Selection Mystery**  
   This review.  
   Focus: cross-validation, leakage, pipelines, `GridSearchCV`, generalization gaps and final-test discipline.

The connection is:

```text
Supervised ML
models → errors → evaluation → ensembles
             ↓
Model Selection Mystery
cross-validation → tune → select → lock decision → test once

SQL Mystery contributes the teaching pattern:
question → predict → run → inspect evidence → decide → reveal
```

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
| 28–29 min | Prediction Arena: enter one Pokémon and compare tuned KNN vs Random Forest | Streamlit |
| 29–30 min | Kahoot finale, including one new Streamlit execution-flow question | Kahoot |

## Facilitation rule

> **Predict first. Run second. Explain third.**

## Story

The Pokémon League has a classifier that reports about **92.5% accuracy**.

Management asks:

> **Can we deploy it?**

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
11. Prediction arena — **Is my Pokémon Legendary?**

## Final reveal

The class should arrive at:

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

## Streamlit bonus question

**Which Streamlit feature batches several widget changes into one submit-triggered rerun?**

1. `st.session_state`
2. `st.form`
3. `st.cache_data`
4. `st.sidebar`

**Answer:** `st.form`.

This adds one execution-flow concept beyond the earlier Streamlit scaffold: widgets inside a form are submitted together instead of each individual widget change immediately triggering its normal update cycle.

## References

### Connected experiences

- Supervised ML: https://hari-raj-singh.com/data-ai/supervised-ml/
- SQL Dinner-Party Mystery: https://hari-raj-singh.com/data-ai/sql/
- neuefische daily-review repository: https://github.com/neuefische/ds-matcha-transformers-220626-daily-review

### Technical references

- Cross-validation: https://scikit-learn.org/stable/modules/cross_validation.html
- `GridSearchCV`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html
- `StratifiedKFold`: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedKFold.html
- `Pipeline`: https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html
- KNN: https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html
- Random Forest: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
- Streamlit forms: https://docs.streamlit.io/develop/concepts/architecture/forms


## Prediction Arena — Is my Pokémon Legendary?

After model selection and the final-test reveal, the class enters one custom Pokémon once.

The same six features are sent to:

- the tuned KNN finalist
- the tuned Random Forest finalist

The interface shows:

- each model's Legendary score
- each model's predicted class
- whether the finalists agree
- which model actually won the model-selection tournament

The teaching point is important:

> A model does not become the preferred model because it gives the more exciting prediction on one example. The preferred model is selected using validation evidence.

The input controls are wrapped in `st.form`, so this stage also demonstrates the Streamlit concept used in the closing Kahoot question: multiple widget changes are submitted together.
