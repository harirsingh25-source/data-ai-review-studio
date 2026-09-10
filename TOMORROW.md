# Tomorrow · 11 September 2026

## What to present

Present **three connected personal daily reviews**, but only the third is the new live teaching session.

### 01 · Supervised ML — The Model Jury

Public lab:  
https://hari-raj-singh.com/data-ai/supervised-ml/

Say:

> This earlier review focused on how individual models and ensembles behave, where they fail, and why validation evidence matters.

### 02 · SQL Dinner-Party Mystery

Public lab:  
https://hari-raj-singh.com/data-ai/sql/

Say:

> This established the interaction pattern I am reusing today: predict first, run something, inspect the evidence, then decide before revealing the reasoning.

### 03 · Pokémon Model-Selection Mystery

Live Streamlit review.

Central question:

> A model scored about 92.5% accuracy. Is that enough evidence to deploy it?

Core flow:

```text
Kahoot warm-up
      ↓
lock final test set
      ↓
cross-validation
      ↓
stratification
      ↓
KNN scaling
      ↓
Random Forest complexity
      ↓
GridSearchCV tournament
      ↓
training vs validation evidence
      ↓
unlock test set once
      ↓
Prediction Arena:
Is my Pokémon Legendary?
      ↓
tuned KNN vs tuned Random Forest
      ↓
Kahoot finale
```

## 30-minute timing

| Time | Activity |
|---|---|
| 0–4 | Kahoot warm-up |
| 4–7 | Story + 92.5% question |
| 7–11 | Locked test set + CV |
| 11–16 | Stratification + folds + KNN scaling |
| 16–22 | GridSearchCV tournament |
| 22–25 | Read scoreboard / generalization gap |
| 25–27 | Unlock final test set |
| 27–29 | Prediction Arena — both tuned finalists |
| 29–30 | Kahoot finale + Streamlit `st.form` question |

## One sentence to finish

> The lesson is not “Grid Search finds the best model”; it is that model choice, preprocessing and tuning must happen inside a validation design that preserves an independent final test.
