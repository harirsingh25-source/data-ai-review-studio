import streamlit as st

from review_studio.ui import eyebrow, lede


SUPERVISED_ML_URL = "https://hari-raj-singh.com/data-ai/supervised-ml/"
SQL_URL = "https://hari-raj-singh.com/data-ai/sql/"


def render_home():
    eyebrow("Data & AI · Connected learning experiences")
    st.title("Data & AI Review Studio")
    lede(
        "Three connected experiences for tomorrow: supervised-learning foundations, "
        "the SQL mystery interaction pattern, and a live model-selection investigation."
    )

    st.subheader("Tomorrow's sequence")

    left, middle, right = st.columns(3)

    with left:
        with st.container(border=True):
            st.markdown("### 01 · Supervised ML")
            st.write(
                "Model behavior, evaluation, failure analysis and ensembles: "
                "the conceptual foundation for choosing models responsibly."
            )
            st.link_button(
                "Open Supervised ML ↗",
                SUPERVISED_ML_URL,
                use_container_width=True,
            )

    with middle:
        with st.container(border=True):
            st.markdown("### 02 · SQL Dinner-Party Mystery")
            st.write(
                "The interaction pattern we reuse: ask a precise question, "
                "run an operation, inspect returned evidence, then decide."
            )
            st.link_button(
                "Open SQL Mystery ↗",
                SQL_URL,
                use_container_width=True,
            )

    with right:
        with st.container(border=True):
            st.markdown("### 03 · Pokémon Model-Selection Mystery")
            st.write(
                "Tomorrow's live review: cross-validation, leakage, pipelines, "
                "GridSearchCV, a locked final test set, and a two-finalist Prediction Arena."
            )
            st.success("Ready for tomorrow")
            st.caption("Open it from the Review Studio sidebar.")

    st.divider()

    st.subheader("How the three connect")
    st.code(
        """01 · SUPERVISED ML
models → errors → evaluation → ensembles
             ↓
03 · MODEL-SELECTION MYSTERY
cross-validation → GridSearchCV → lock decision → test once

02 · SQL MYSTERY supplies the classroom pattern
question → predict → run → inspect evidence → decide → reveal""",
        language=None,
    )

    st.info(
        "Tomorrow stays focused on these three. Additional review modules are "
        "reserved for the later public website expansion."
    )
