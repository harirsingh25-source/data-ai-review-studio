import streamlit as st

from review_studio.registry import get_modules
from review_studio.ui import eyebrow, lede


def render_home():
    eyebrow("Data & AI · Interactive review system")
    st.title("Data & AI Review Studio")
    lede(
        "Short, evidence-led classroom reviews: predict first, run an experiment, "
        "inspect the evidence, then reveal the reasoning."
    )

    st.subheader("Review modules")
    for module in get_modules():
        with st.container(border=True):
            left, right = st.columns([5, 1])
            with left:
                st.markdown(f"### {module.icon} {module.title}")
                st.write(module.description)
            with right:
                st.caption(module.status)

    st.subheader("Design pattern")
    st.code(
        """STORY / CENTRAL QUESTION
        ↓
PREDICT
        ↓
INTERACTIVE EXPERIMENT
        ↓
EVIDENCE RETURNED
        ↓
DECISION
        ↓
HINT / REVEAL
        ↓
FINAL MYSTERY
        ↓
PYTHON CODE COMPANION""",
        language=None,
    )

    st.info(
        "Tomorrow's presentation is the first production module: "
        "Pokémon Model-Selection Mystery."
    )
