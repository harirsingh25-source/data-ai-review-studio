import streamlit as st


CSS = r'''
<style>
.block-container {
    max-width: 1180px;
    padding-top: 2.25rem;
    padding-bottom: 4rem;
}
[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128,128,128,.15);
}
.rs-eyebrow {
    font-size: .72rem;
    font-weight: 750;
    letter-spacing: .14em;
    text-transform: uppercase;
    opacity: .62;
    margin-bottom: .45rem;
}
.rs-lede {
    font-size: 1.08rem;
    line-height: 1.7;
    opacity: .78;
    max-width: 850px;
    margin-top: -.45rem;
    margin-bottom: 1.4rem;
}
.rs-kicker {
    font-size: .70rem;
    font-weight: 800;
    letter-spacing: .13em;
    text-transform: uppercase;
    opacity: .58;
    margin-top: 2.0rem;
    margin-bottom: .45rem;
}
.rs-question {
    font-size: 1.42rem;
    line-height: 1.45;
    font-weight: 640;
    max-width: 950px;
    margin-bottom: .8rem;
}
.rs-panel {
    border: 1px solid rgba(128,128,128,.22);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    background: rgba(128,128,128,.045);
}
.rs-lock {
    border: 1px solid rgba(128,128,128,.28);
    border-radius: 14px;
    padding: 1rem 1.1rem;
    background: rgba(128,128,128,.055);
}
.rs-status-ready {
    display: inline-block;
    font-size: .72rem;
    padding: .18rem .48rem;
    border: 1px solid rgba(128,128,128,.24);
    border-radius: 999px;
    margin-left: .3rem;
}
div[data-testid="stMetric"] {
    border: 1px solid rgba(128,128,128,.18);
    border-radius: 12px;
    padding: .78rem .95rem;
}
div[data-testid="stDataFrame"] {
    border: 1px solid rgba(128,128,128,.15);
    border-radius: 10px;
}
</style>
'''


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)


def eyebrow(text: str):
    st.markdown(f'<div class="rs-eyebrow">{text}</div>', unsafe_allow_html=True)


def lede(text: str):
    st.markdown(f'<div class="rs-lede">{text}</div>', unsafe_allow_html=True)


def kicker(text: str):
    st.markdown(f'<div class="rs-kicker">{text}</div>', unsafe_allow_html=True)


def question(text: str):
    st.markdown(f'<div class="rs-question">{text}</div>', unsafe_allow_html=True)


def panel(text: str):
    st.markdown(f'<div class="rs-panel">{text}</div>', unsafe_allow_html=True)


def lock_panel(text: str):
    st.markdown(f'<div class="rs-lock">{text}</div>', unsafe_allow_html=True)
