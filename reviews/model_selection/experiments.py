from __future__ import annotations

from typing import Any

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import (
    GridSearchCV,
    KFold,
    StratifiedKFold,
    cross_validate,
    train_test_split,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


FEATURE_ORDER = [
    "hit_points",
    "attack",
    "defense",
    "sp_attack",
    "sp_defense",
    "speed",
]
TARGET = "is_legendary"
RSEED = 33


def split_data(df: pd.DataFrame):
    X = df[FEATURE_ORDER]
    y = df[TARGET]
    return train_test_split(
        X, y,
        test_size=0.20,
        random_state=RSEED,
        stratify=y,
    )


def baseline_cv_scores(df: pd.DataFrame, n_splits: int) -> pd.DataFrame:
    X_train, _, y_train, _ = split_data(df)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=RSEED)
    model = RandomForestClassifier(n_estimators=100, random_state=RSEED)
    scores = cross_validate(
        model, X_train, y_train,
        cv=cv,
        scoring="roc_auc",
        return_train_score=True,
        n_jobs=-1,
    )
    return pd.DataFrame({
        "fold": range(1, n_splits + 1),
        "train_roc_auc": scores["train_score"],
        "validation_roc_auc": scores["test_score"],
    })


def stratification_comparison(df: pd.DataFrame, n_splits: int) -> pd.DataFrame:
    X_train, _, y_train, _ = split_data(df)
    rows: list[dict[str, Any]] = []

    splitters = {
        "KFold": KFold(n_splits=n_splits, shuffle=True, random_state=RSEED),
        "StratifiedKFold": StratifiedKFold(
            n_splits=n_splits, shuffle=True, random_state=RSEED
        ),
    }
    for name, splitter in splitters.items():
        for fold, (_, valid_idx) in enumerate(
            splitter.split(X_train, y_train), start=1
        ):
            y_valid = y_train.iloc[valid_idx]
            rows.append({
                "strategy": name,
                "fold": fold,
                "legendary_fraction": float(y_valid.mean()),
            })
    return pd.DataFrame(rows)


def knn_scaling_scores(df: pd.DataFrame, n_splits: int) -> pd.DataFrame:
    X_train, _, y_train, _ = split_data(df)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=RSEED)

    candidates = {
        "Raw features": Pipeline([
            ("scale", "passthrough"),
            ("model", KNeighborsClassifier(n_neighbors=11)),
        ]),
        "StandardScaler": Pipeline([
            ("scale", StandardScaler()),
            ("model", KNeighborsClassifier(n_neighbors=11)),
        ]),
    }

    rows = []
    for label, candidate in candidates.items():
        scores = cross_validate(
            candidate, X_train, y_train,
            cv=cv,
            scoring="roc_auc",
            return_train_score=True,
            n_jobs=-1,
        )
        for fold, (tr, va) in enumerate(
            zip(scores["train_score"], scores["test_score"]), start=1
        ):
            rows.append({
                "preprocessing": label,
                "fold": fold,
                "train_roc_auc": float(tr),
                "validation_roc_auc": float(va),
            })
    return pd.DataFrame(rows)


def rf_complexity_scores(
    df: pd.DataFrame,
    n_splits: int,
    max_depth: int | None,
    n_estimators: int,
) -> dict[str, float]:
    X_train, _, y_train, _ = split_data(df)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=RSEED)
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=RSEED,
    )
    scores = cross_validate(
        model, X_train, y_train,
        cv=cv,
        scoring="roc_auc",
        return_train_score=True,
        n_jobs=-1,
    )
    train = float(scores["train_score"].mean())
    valid = float(scores["test_score"].mean())
    return {"train": train, "validation": valid, "gap": train - valid}


def run_tournament(
    df: pd.DataFrame,
    n_splits: int = 5,
    scoring: str = "roc_auc",
):
    X_train, X_test, y_train, y_test = split_data(df)
    cv = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=RSEED)

    pipeline = Pipeline([
        ("scale", "passthrough"),
        ("model", KNeighborsClassifier()),
    ])

    parameter_grid = [
        {
            "scale": [StandardScaler()],
            "model": [KNeighborsClassifier()],
            "model__n_neighbors": [3, 5, 7, 9, 11],
            "model__weights": ["uniform", "distance"],
        },
        {
            "scale": ["passthrough"],
            "model": [RandomForestClassifier(random_state=RSEED)],
            "model__n_estimators": [100, 200],
            "model__max_depth": [None, 5, 10],
            "model__min_samples_split": [2, 5],
        },
    ]

    search = GridSearchCV(
        pipeline,
        parameter_grid,
        scoring=scoring,
        cv=cv,
        n_jobs=-1,
        return_train_score=True,
        refit=True,
    )
    search.fit(X_train, y_train)

    results = pd.DataFrame(search.cv_results_).copy()
    results["generalization_gap"] = (
        results["mean_train_score"] - results["mean_test_score"]
    )
    results["model_name"] = results["param_model"].map(
        lambda model: model.__class__.__name__
    )
    results["parameters"] = results["params"].map(str)

    best = search.best_estimator_
    pred = best.predict(X_test)
    prob = best.predict_proba(X_test)[:, 1]

    summary = {
        "best_model_name": best.named_steps["model"].__class__.__name__,
        "best_score": float(search.best_score_),
        "best_params": {
            key: (
                value.__class__.__name__
                if hasattr(value, "fit")
                else value
            )
            for key, value in search.best_params_.items()
        },
        "test_accuracy": float(accuracy_score(y_test, pred)),
        "test_roc_auc": float(roc_auc_score(y_test, prob)),
        "n_candidates": int(len(results)),
        "n_fits": int(len(results) * n_splits),
        "scoring": scoring,
        "folds": n_splits,
    }
    return results, summary
