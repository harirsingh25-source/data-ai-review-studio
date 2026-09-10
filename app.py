import streamlit as st

from review_studio.home import render_home
from review_studio.registry import get_modules
from review_studio.ui import inject_css


st.set_page_config(
    page_title="Data & AI Review Studio",
    page_icon="◉",
    layout="wide",
)

inject_css()

modules = get_modules()
ready = [m for m in modules if m.renderer is not None]

page_labels = ["Home"] + [f"{m.icon} {m.title}" for m in ready]
selected = st.sidebar.radio("Review Studio", page_labels)

st.sidebar.divider()
st.sidebar.caption("Predict → experiment → inspect → reveal")

if selected == "Home":
    render_home()
else:
    for module in ready:
        if selected == f"{module.icon} {module.title}":
            module.renderer()
            break
