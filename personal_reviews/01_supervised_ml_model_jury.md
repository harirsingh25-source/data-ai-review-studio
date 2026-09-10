# 01 · Supervised ML — The Model Jury

**Original daily review:** Ensemble Methods — The Model Jury  
**Date:** 20 August 2026  
**Format:** interactive daily review  
**Public interactive lab:** https://hari-raj-singh.com/data-ai/supervised-ml/  
**Canonical course protocol:** `protocols/2026-08-20_Ensemble_Methods_Hari.md` in the neuefische daily-review repository.

## Central question

> Which model, or combination of models, gives the strongest evidence that it will generalise to unseen data?

## Review pattern

```text
prediction question
      ↓
valid information boundary
      ↓
leakage-safe preprocessing
      ↓
validation design
      ↓
individual model behaviour
      ↓
bias + variance
      ↓
error diversity / correlation
      ↓
ensemble evaluation
      ↓
decision
```

## Core ideas

- define the prediction problem before choosing an algorithm
- preprocessing must be fitted on training data only
- distinguish bias from variance
- compare model errors, not only headline scores
- hard voting vs soft voting
- bagging and bootstrap sampling
- out-of-bag observations
- Random Forest row and feature randomness
- AdaBoost / boosting intuition
- XGBoost and ensemble trade-offs

## Connection to tomorrow

This review supplies the **model behavior and ensemble foundation**.

Tomorrow's Model-Selection Mystery asks the next question:

> How should we choose among model families and hyperparameters without contaminating the final test set?

## References

- Public lab: https://hari-raj-singh.com/data-ai/supervised-ml/
- neuefische daily-review repository: https://github.com/neuefische/ds-matcha-transformers-220626-daily-review
