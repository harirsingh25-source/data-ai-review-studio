import pandas as pd
import plotly.express as px
import streamlit as st

from review_studio.ui import (
    experiment_card,
    hero,
    kicker,
    lock_panel,
    question,
    rail_title,
    side_block,
    sitebar,
    stage_heading,
    stage_label,
    workbench,
)
from reviews.model_selection.content import STAGES
from reviews.model_selection.experiments import (
    TARGET,
    baseline_cv_scores,
    knn_scaling_scores,
    predict_with_finalists,
    rf_complexity_scores,
    run_tournament,
    split_data,
    stratification_comparison,
)


@st.cache_data(show_spinner=False)
def load_data(path: str = "data/pokemon.csv") -> pd.DataFrame:
    return pd.read_csv(path)


def _presenter_sidebar():
    st.sidebar.markdown("### Presenter controls")
    classroom = st.sidebar.toggle(
        "Classroom mode",
        value=True,
        help="Keeps answers behind reveal controls.",
    )
    st.sidebar.caption("Target duration: ~30 minutes.")

    st.sidebar.markdown("### Connected labs")
    st.sidebar.link_button(
        "01 · Supervised ML ↗",
        "https://hari-raj-singh.com/data-ai/supervised-ml/",
        use_container_width=True,
    )
    st.sidebar.link_button(
        "02 · SQL Mystery ↗",
        "https://hari-raj-singh.com/data-ai/sql/",
        use_container_width=True,
    )
    st.sidebar.caption("03 · Model Selection Mystery · you are here")

    with st.sidebar.expander("Review lineage & references"):
        st.markdown(
            """
- [SQL Dinner-Party Mystery](https://hari-raj-singh.com/data-ai/sql/)
- [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html)
- [scikit-learn: GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)
- [scikit-learn: Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [Streamlit concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
"""
        )

    with st.sidebar.expander("Kahoot cues"):
        st.markdown(
            """
**Warm-up**
1. What is CV mainly for?
2. When should the final test set be used?
3. What does stratification preserve?
4. Why can KNN require scaling?

**Finale**
5. What does GridSearchCV select?
6. Highest training score wins — true/false?
7. What is the forbidden move?
8. When do we unlock the test set?
9. Streamlit bonus: which feature batches widget changes into one submit-triggered rerun?
"""
        )
    return classroom



def _journey_rail():
    if "journey_stage" not in st.session_state:
        st.session_state.journey_stage = 0

    rail_title(
        "Learning journey",
        f"{st.session_state.journey_stage + 1:02d} / {len(STAGES):02d}",
    )

    short_titles = [
        "92.5%?",
        "Lock test",
        "Cross-val",
        "Stratify",
        "KNN scaling",
        "RF complexity",
        "GridSearch",
        "Scoreboard",
        "Forbidden",
        "Final mystery",
        "Prediction arena",
    ]

    for idx, item in enumerate(STAGES):
        label = f"{idx + 1:02d}  {short_titles[idx]}"
        is_current = idx == st.session_state.journey_stage

        if st.button(
            label,
            key=f"journey_{idx}",
            type="primary" if is_current else "secondary",
            use_container_width=True,
        ):
            st.session_state.journey_stage = idx
            st.rerun()

    st.markdown('<div class="rs-journey-divider"></div>', unsafe_allow_html=True)
    st.caption(
        f"{st.session_state.journey_stage + 1} / {len(STAGES)} · "
        f"Stage {st.session_state.journey_stage + 1}"
    )

    return int(st.session_state.journey_stage)


def _stage_controls(stage_idx: int):
    prev_col, next_col = st.columns(2)

    with prev_col:
        if st.button(
            "← Previous",
            disabled=stage_idx == 0,
            use_container_width=True,
            key="stage_previous",
        ):
            st.session_state.journey_stage -= 1
            st.rerun()

    with next_col:
        if st.button(
            "Next →",
            disabled=stage_idx == len(STAGES) - 1,
            use_container_width=True,
            key="stage_next",
            type="primary",
        ):
            st.session_state.journey_stage += 1
            st.rerun()


def _experiment(stage_idx: int, df: pd.DataFrame):
    X_train, X_test, y_train, y_test = split_data(df)

    if stage_idx == 0:
        c1, c2, c3 = st.columns(3)
        c1.metric("Pokémon", len(df))
        c2.metric("Legendary", int(df[TARGET].sum()))
        c3.metric("Non-Legendary", int((df[TARGET] == 0).sum()))

        answer = st.radio(
            "Would you deploy from one 92.5% accuracy result?",
            [
                "Yes — 92.5% is high enough.",
                "No — I need validation evidence and an untouched test set.",
                "Only if Random Forest has the most trees.",
            ],
            index=None,
        )
        if answer:
            if answer.startswith("No"):
                st.success("Good. The score is evidence, but the selection procedure still matters.")
            else:
                st.warning("Keep investigating: what data influenced the decision?")

    elif stage_idx == 1:
        c1, c2, c3 = st.columns(3)
        c1.metric("Development data", len(X_train))
        c2.metric("Final test 🔒", len(X_test))
        c3.metric("Test fraction", f"{len(X_test)/len(df):.0%}")
        lock_panel(
            "<b>🔒 Test set locked.</b><br>"
            "Model family, preprocessing and hyperparameters must be chosen "
            "without repeatedly consulting final-test performance."
        )

    elif stage_idx == 2:
        folds = st.slider("Cross-validation folds", 3, 10, 5)
        scores = baseline_cv_scores(df, folds)

        c1, c2, c3 = st.columns(3)
        c1.metric("Mean validation ROC-AUC", f"{scores.validation_roc_auc.mean():.3f}")
        c2.metric("Fold-to-fold SD", f"{scores.validation_roc_auc.std():.3f}")
        c3.metric("Validation folds", folds)

        long = scores.melt(
            id_vars="fold",
            value_vars=["train_roc_auc", "validation_roc_auc"],
            var_name="split",
            value_name="roc_auc",
        )
        fig = px.line(
            long,
            x="fold",
            y="roc_auc",
            color="split",
            markers=True,
            title="Performance across cross-validation folds",
        )
        st.plotly_chart(fig, use_container_width=True)

    elif stage_idx == 3:
        folds = st.slider("Folds", 3, 10, 5)
        comp = stratification_comparison(df, folds)
        fig = px.line(
            comp,
            x="fold",
            y="legendary_fraction",
            color="strategy",
            markers=True,
            title="Legendary fraction in each validation fold",
        )
        fig.add_hline(
            y=float(y_train.mean()),
            line_dash="dash",
            annotation_text="development-set proportion",
        )
        st.plotly_chart(fig, use_container_width=True)

    elif stage_idx == 4:
        folds = st.slider("Folds", 3, 10, 5)
        scores = knn_scaling_scores(df, folds)
        summary = (
            scores.groupby("preprocessing", as_index=False)["validation_roc_auc"]
            .mean()
            .sort_values("validation_roc_auc", ascending=False)
        )
        fig = px.bar(
            summary,
            x="preprocessing",
            y="validation_roc_auc",
            title="KNN validation ROC-AUC: raw vs scaled features",
        )
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(summary, use_container_width=True, hide_index=True)

    elif stage_idx == 5:
        c1, c2 = st.columns(2)
        with c1:
            depth_label = st.select_slider(
                "Maximum tree depth",
                options=["3", "5", "10", "20", "None"],
                value="10",
            )
        with c2:
            trees = st.select_slider(
                "Number of trees",
                options=[50, 100, 200, 400],
                value=200,
            )
        depth = None if depth_label == "None" else int(depth_label)
        scores = rf_complexity_scores(df, 5, depth, trees)

        m1, m2, m3 = st.columns(3)
        m1.metric("Train ROC-AUC", f"{scores['train']:.3f}")
        m2.metric("CV ROC-AUC", f"{scores['validation']:.3f}")
        m3.metric("Generalization gap", f"{scores['gap']:.3f}")

    elif stage_idx == 6:
        c1, c2 = st.columns(2)
        with c1:
            folds = st.slider("CV folds", 3, 10, 5)
        with c2:
            scoring = st.selectbox("Scoring metric", ["roc_auc", "accuracy"])

        st.write("**Tournament:** 10 KNN configurations + 12 Random Forest configurations.")
        st.caption(f"{22 * folds} cross-validation fits before the winner is refit.")

        if st.button("Run model tournament →", type="primary"):
            with st.spinner("Cross-validating every candidate..."):
                results, summary = run_tournament(df, folds, scoring)
            st.session_state.tournament_results = results
            st.session_state.tournament_summary = summary
            st.success("Tournament complete. Continue to the scoreboard.")

        if "tournament_summary" in st.session_state:
            summary = st.session_state.tournament_summary
            a, b, c = st.columns(3)
            a.metric("Candidates", summary["n_candidates"])
            b.metric("CV fits", summary["n_fits"])
            c.metric("Best CV score", f"{summary['best_score']:.3f}")

    elif stage_idx == 7:
        if "tournament_results" not in st.session_state:
            st.info("Run the tournament first.")
            if st.button("Run default 5-fold tournament"):
                with st.spinner("Running tournament..."):
                    results, summary = run_tournament(df, 5, "roc_auc")
                st.session_state.tournament_results = results
                st.session_state.tournament_summary = summary
                st.rerun()
            return

        results = st.session_state.tournament_results.sort_values("rank_test_score")
        top = results.head(10).copy()

        fig = px.scatter(
            top,
            x="mean_train_score",
            y="mean_test_score",
            color="model_name",
            size="mean_fit_time",
            hover_data=["rank_test_score", "parameters", "generalization_gap"],
            labels={
                "mean_train_score": "Mean training score",
                "mean_test_score": "Mean validation score",
            },
            title="Top candidates: training evidence vs validation evidence",
        )
        st.plotly_chart(fig, use_container_width=True)

        display = top[
            [
                "rank_test_score",
                "model_name",
                "mean_train_score",
                "mean_test_score",
                "generalization_gap",
                "parameters",
            ]
        ].rename(
            columns={
                "rank_test_score": "rank",
                "model_name": "model",
                "mean_train_score": "train",
                "mean_test_score": "validation",
                "generalization_gap": "gap",
            }
        )
        st.dataframe(
            display,
            use_container_width=True,
            hide_index=True,
            column_config={
                "train": st.column_config.NumberColumn(format="%.3f"),
                "validation": st.column_config.NumberColumn(format="%.3f"),
                "gap": st.column_config.NumberColumn(format="%.3f"),
            },
        )

    elif stage_idx == 8:
        answer = st.radio(
            "Grid Search → test → expand grid → test again. What happened?",
            [
                "Nothing. The test set remains independent.",
                "The test set has effectively become part of model selection.",
                "The model becomes unsupervised.",
                "Cross-validation is no longer needed.",
            ],
            index=None,
        )
        if answer:
            if answer.startswith("The test set has"):
                st.success("Correct. Test performance influenced a later modeling decision.")
            else:
                st.warning("Ask whether test performance influenced what you did next.")

    elif stage_idx == 9:
        if "tournament_summary" not in st.session_state:
            st.info("Run the tournament first.")
            if st.button("Run default tournament now"):
                with st.spinner("Running tournament..."):
                    results, summary = run_tournament(df, 5, "roc_auc")
                st.session_state.tournament_results = results
                st.session_state.tournament_summary = summary
                st.rerun()
            return

        summary = st.session_state.tournament_summary
        c1, c2, c3 = st.columns(3)
        c1.metric("Winning model", summary["best_model_name"])
        c2.metric("Best CV score", f"{summary['best_score']:.3f}")
        c3.metric("Scoring rule", summary["scoring"])

        st.write("**Best hyperparameters**")
        st.json(summary["best_params"])

        if "test_unlocked" not in st.session_state:
            st.session_state.test_unlocked = False

        if not st.session_state.test_unlocked:
            lock_panel(
                "<b>🔒 Final test set remains locked.</b><br>"
                "Ask the class to predict whether final performance will be "
                "above, near, or below the CV estimate."
            )
            if st.button("Unlock untouched test set →", type="primary"):
                st.session_state.test_unlocked = True
                st.rerun()
        else:
            t1, t2 = st.columns(2)
            t1.metric("Test ROC-AUC", f"{summary['test_roc_auc']:.3f}")
            t2.metric("Test accuracy", f"{summary['test_accuracy']:.3f}")
            st.success(
                "Final question: do CV and the untouched test set tell a consistent story?"
            )
            st.caption("Next: use both tuned finalists in the Prediction Arena.")

    elif stage_idx == 10:
        if "tournament_summary" not in st.session_state:
            st.info("Run the model tournament first so both finalists are tuned.")
            if st.button("Run default tournament for the arena"):
                with st.spinner("Tuning both finalists..."):
                    results, summary = run_tournament(df, 5, "roc_auc")
                st.session_state.tournament_results = results
                st.session_state.tournament_summary = summary
                st.rerun()
            return

        summary = st.session_state.tournament_summary

        st.write("### ⚡ Is my Pokémon Legendary?")
        st.caption(
            "Enter one Pokémon. The exact same six features are sent to both tuned finalists."
        )

        with st.form("prediction_arena"):
            a, b, c = st.columns(3)

            with a:
                hit_points = st.number_input("Hit Points", 1, 255, 70)
                attack = st.number_input("Attack", 1, 255, 80)

            with b:
                defense = st.number_input("Defense", 1, 255, 80)
                sp_attack = st.number_input("Special Attack", 1, 255, 75)

            with c:
                sp_defense = st.number_input("Special Defense", 1, 255, 75)
                speed = st.number_input("Speed", 1, 255, 70)

            submitted = st.form_submit_button(
                "Run both finalists →",
                type="primary",
                use_container_width=True,
            )

        if submitted:
            features = {
                "hit_points": hit_points,
                "attack": attack,
                "defense": defense,
                "sp_attack": sp_attack,
                "sp_defense": sp_defense,
                "speed": speed,
            }

            arena = predict_with_finalists(df, features, summary)
            st.session_state.prediction_arena = arena

        if "prediction_arena" in st.session_state:
            arena = st.session_state.prediction_arena

            left, right = st.columns(2)
            for container, (_, row) in zip([left, right], arena.iterrows()):
                with container:
                    winner = " · 🏆 tournament winner" if row["tournament_winner"] else ""
                    st.markdown(f"### {row['model']}{winner}")
                    st.metric("Legendary score", f"{row['legendary_score']:.1%}")
                    st.metric("Model says", row["prediction"])
                    st.caption(f"Validation score used for selection: {row['cv_score']:.3f}")

            agree = arena["prediction"].nunique() == 1
            if agree:
                st.success(
                    f"Both finalists agree: **{arena.iloc[0]['prediction']}**."
                )
            else:
                st.warning(
                    "The finalists disagree. That is useful evidence: different model "
                    "families learned different decision boundaries."
                )

            chart = px.bar(
                arena,
                x="model",
                y="legendary_score",
                hover_data=["prediction", "cv_score", "tournament_winner"],
                labels={"legendary_score": "Legendary score", "model": "Finalist"},
                title="Same Pokémon, two tuned model views",
            )
            chart.update_yaxes(range=[0, 1], tickformat=".0%")
            st.plotly_chart(chart, use_container_width=True)

            st.info(
                "The tournament winner is chosen from validation evidence. "
                "A more dramatic prediction on one custom Pokémon does not change that selection rule."
            )



def _future_bridge():
    st.divider()
    eyebrow("One-point bridge · What comes next")
    st.subheader("How today's model-selection logic connects to the rest of Data & AI")
    st.caption(
        "These are deliberately one-point previews — not full lessons. "
        "Each becomes its own future interactive review."
    )

    items = [
        ("🧠 Transformers", "Self-attention lets each token weigh other tokens that matter for its context."),
        ("🖼️ CNNs", "Convolutions learn local spatial patterns and reuse the same detector across an image."),
        ("🔁 RNNs", "A recurrent hidden state carries sequence information from one step to the next."),
        ("📈 Time Series", "Validation must respect time order; shuffled splits can leak future information."),
        ("🧪 A/B Testing", "Define the hypothesis and success metric before inspecting the experimental result."),
        ("🌳 LightGBM", "LightGBM is a gradient-boosted decision-tree system designed for efficient tabular learning."),
        ("📚 MLflow", "Track parameters, metrics, artifacts and model versions so experiments are reproducible."),
        ("🌐 Model Serving", "Serving turns a trained model into a stable interface that applications can query."),
        ("☁️ GCP", "Cloud deployment separates the local experiment from scalable compute, hosting and operations."),
        ("⚡ Streamlit", "`st.form` batches widget changes and submits them together, changing the normal rerun flow."),
    ]

    for label, point in items:
        with st.container(border=True):
            st.markdown(f"**{label}**")
            st.write(point)

    st.info(
        "Connection: today's discipline — separate development evidence from final evaluation — "
        "continues through every one of these topics."
    )



def render():
    classroom_mode = _presenter_sidebar()
    df = load_data()

    sitebar()

    if "journey_stage" not in st.session_state:
        st.session_state.journey_stage = 0

    stage_idx = int(st.session_state.journey_stage)
    hero(stage_idx + 1, len(STAGES))

    rail_col, main_col, evidence_col = st.columns(
        [1.25, 3.65, 1.45],
        gap="large",
    )

    with rail_col:
        stage_idx = _journey_rail()

    stage = STAGES[stage_idx]

    with main_col:
        header_left, header_right = st.columns([4.2, 1.8])
        with header_left:
            stage_label(f"Stage {stage_idx + 1} · {stage.title}")
            stage_heading(stage.title)
        with header_right:
            _stage_controls(stage_idx)

        kicker("Central question")
        question(stage.question)

        experiment_card(
            stage.why,
            "READY · 801 Pokémon · 6 features",
        )

        _experiment(stage_idx, df)

        kicker("Model selection workbench")
        if stage_idx <= 1:
            workbench(
                """ALL POKÉMON
   │
   ├──────────────► FINAL TEST SET 🔒
   │
   ▼
DEVELOPMENT / TRAINING DATA"""
            )
        elif stage_idx <= 6:
            workbench(
                """DEVELOPMENT DATA
   │
   ▼
CROSS-VALIDATION
   │
   ▼
CANDIDATE CONFIGURATIONS
   │
   ▼
RANK BY VALIDATION EVIDENCE
   │
   └──────────────► FINAL TEST SET remains 🔒"""
            )
        else:
            workbench(
                """TRAIN
  ↓
CROSS-VALIDATE
  ↓
TUNE
  ↓
SELECT
  ↓
LOCK DECISION
  ↓
TEST ONCE"""
            )

        kicker("Evidence returned")
        st.caption(
            "Use the controls above. The plots, metrics and tables returned by "
            "the experiment are the evidence for the stage decision."
        )

        st.markdown('<div class="rs-daily"></div>', unsafe_allow_html=True)
        kicker("Daily review")

        daily_question = (
            "What must be true before we are allowed to unlock the final test set?"
            if stage_idx == 9
            else ("Do both tuned finalists agree, and which one earned our trust?" if stage_idx == 10 else "What evidence would change your decision at this stage?")
        )
        st.write(daily_question)

        if classroom_mode:
            with st.expander("Reveal reasoning"):
                st.write(stage.why)
                st.write(f"**Boundary:** {stage.boundary}")
        else:
            st.write(stage.why)

        kicker("Python code companion")
        st.caption("Runnable implementation pattern")
        st.code(stage.companion, language="python")


    with evidence_col:
        side_block("Why it matters", stage.why, "orange")
        side_block(
            "Evidence to inspect",
            " · ".join(stage.evidence),
            "orange",
        )
        side_block("Boundary", stage.boundary, "teal")

        decision_copy = (
            "Would you advance this finalized workflow? Defend the decision using "
            "cross-validation and final-test evidence."
            if stage_idx == len(STAGES) - 1
            else "State the decision before moving on. What evidence would make you revise it?"
        )
        side_block("Decision", decision_copy, "orange")

        if stage_idx <= 3:
            connection = "Split design determines whether later scores are trustworthy."
        elif stage_idx <= 6:
            connection = "Model complexity and preprocessing belong inside the validation workflow."
        else:
            connection = "Model selection ends before the untouched final-test reveal."
        side_block("Model connection", connection, "purple")

    st.divider()
    st.caption(
        "Connected sequence · Supervised ML → SQL Mystery teaching pattern → "
        "Pokémon Model-Selection Mystery"
    )
