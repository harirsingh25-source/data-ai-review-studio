from dataclasses import dataclass


@dataclass(frozen=True)
class Stage:
    title: str
    question: str
    why: str
    evidence: tuple[str, ...]
    boundary: str
    companion: str


STAGES = [
    Stage(
        "The 92.5% question",
        "A Random Forest scored about 92.5% accuracy on one split. Is that enough evidence to deploy it?",
        "One score is evidence, but it does not tell us whether the model-selection process was trustworthy.",
        ("class balance", "which data produced the score", "whether the test set influenced later decisions"),
        "Do not choose a model because one test result looks impressive.",
        """X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.20,
    stratify=y,
    random_state=33,
)""",
    ),
    Stage(
        "Lock the test set",
        "What is the final test set actually for?",
        "The test set is the independent check used after model-development decisions are locked.",
        ("development-set size", "test-set size", "target prevalence"),
        "Repeatedly reacting to the test score makes it part of model development.",
        """# Develop on X_train / y_train.
# Leave X_test / y_test untouched until the final reveal.""",
    ),
    Stage(
        "Cross-validation",
        "Why use several validation folds instead of trusting one split of the development data?",
        "Cross-validation exposes performance across several train/validation partitions.",
        ("mean validation score", "fold-to-fold spread", "computational cost"),
        "Cross-validation happens inside the development data. The final test set remains locked.",
        """cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=33,
)""",
    ),
    Stage(
        "Stratification",
        "Legendary Pokémon are rare. Should each fold contain roughly the same class proportion?",
        "Stratification makes class proportions more consistent across classification folds.",
        ("Legendary fraction by fold", "KFold vs StratifiedKFold"),
        "Stratification addresses class-balance variation; it does not solve every leakage problem.",
        """cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=33,
)""",
    ),
    Stage(
        "KNN scaling challenge",
        "Why can feature scaling change KNN performance?",
        "KNN uses distances, so features with large numerical ranges can dominate.",
        ("raw-feature KNN", "scaled KNN", "same CV and metric"),
        "Preprocessing must be fitted inside each training fold. Use a Pipeline.",
        """pipe = Pipeline([
    ("scale", StandardScaler()),
    ("model", KNeighborsClassifier())
])""",
    ),
    Stage(
        "Random Forest complexity",
        "What happens when a tree ensemble is allowed to become more complex?",
        "Training performance can improve while validation performance stalls, creating a generalization gap.",
        ("train ROC-AUC", "validation ROC-AUC", "generalization gap"),
        "A gap is evidence to investigate, not an automatic rejection rule.",
        """model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=33,
)""",
    ),
    Stage(
        "GridSearchCV tournament",
        "How do we compare many hyperparameter combinations without touching the final test set?",
        "GridSearchCV evaluates each configuration with cross-validation and ranks candidates using a chosen scoring rule.",
        ("candidate count", "CV fits", "best mean CV score", "best hyperparameters"),
        "Grid Search selects configurations; it does not replace final test evaluation.",
        """search = GridSearchCV(
    pipeline,
    parameter_grid,
    scoring="roc_auc",
    cv=cv,
    return_train_score=True,
    refit=True,
)""",
    ),
    Stage(
        "Read the scoreboard",
        "Should the model with the highest training score automatically win?",
        "Model selection is about generalization, so validation evidence matters more than memorizing the training data.",
        ("rank", "mean train score", "mean validation score", "generalization gap"),
        "Do not rank candidates using final-test performance.",
        """results = pd.DataFrame(search.cv_results_)
results["gap"] = (
    results["mean_train_score"] - results["mean_test_score"]
)""",
    ),
    Stage(
        "The forbidden move",
        "What happens if we inspect the test score, change the grid, test again, and repeat?",
        "Later modeling decisions are now influenced by test performance: the test set has leaked into model selection.",
        ("which later decisions changed", "whether a fresh independent holdout remains"),
        "The test set is independent only if it did not influence model-development decisions.",
        """# Avoid:
# tune -> test -> retune -> test

# Prefer:
# tune with CV -> lock decision -> test once""",
    ),
    Stage(
        "Final mystery",
        "Which model should advance, and does the untouched test set tell a consistent story?",
        "The final reveal asks whether a workflow chosen through CV generalizes to unseen data.",
        ("winning model", "best parameters", "CV score", "test ROC-AUC", "test accuracy"),
        "After final evaluation, do not keep tuning against the same test set.",
        """best_model = search.best_estimator_
prob = best_model.predict_proba(X_test)[:, 1]
test_auc = roc_auc_score(y_test, prob)""",
    ),
]
