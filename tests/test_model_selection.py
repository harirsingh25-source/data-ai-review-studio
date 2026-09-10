import pandas as pd

from reviews.model_selection.experiments import (
    FEATURE_ORDER,
    TARGET,
    split_data,
    baseline_cv_scores,
    run_tournament,
)


def load():
    return pd.read_csv("data/pokemon.csv")


def test_expected_columns_exist():
    df = load()
    for col in FEATURE_ORDER + [TARGET]:
        assert col in df.columns


def test_split_preserves_total_rows():
    df = load()
    X_train, X_test, y_train, y_test = split_data(df)
    assert len(X_train) + len(X_test) == len(df)
    assert len(y_train) + len(y_test) == len(df)


def test_cv_returns_requested_number_of_folds():
    df = load()
    scores = baseline_cv_scores(df, 3)
    assert len(scores) == 3
    assert scores["validation_roc_auc"].between(0, 1).all()


def test_small_tournament_runs():
    df = load()
    results, summary = run_tournament(df, n_splits=3, scoring="roc_auc")
    assert len(results) == 22
    assert 0 <= summary["best_score"] <= 1
    assert 0 <= summary["test_accuracy"] <= 1
    assert 0 <= summary["test_roc_auc"] <= 1
