
import html
import streamlit as st


CSS = r"""
<style>
:root {
    --rs-ink: #13283A;
    --rs-muted: #587086;
    --rs-paper-2: #FBF9F4;
    --rs-line: #DCD7CE;
    --rs-orange: #C96535;
    --rs-teal: #187E7A;
    --rs-teal-soft: #E3F0EE;
    --rs-hero: #073E53;
    --rs-hero-2: #345F67;
    --rs-purple: #71568D;
}

html, body, [class*="css"] { color: var(--rs-ink); }
.stApp { background: var(--rs-paper-2); }

header[data-testid="stHeader"] {
    background: rgba(251, 249, 244, 0.90);
    border-bottom: 1px solid var(--rs-line);
}

.block-container {
    max-width: 1320px;
    padding-top: 0.7rem;
    padding-bottom: 4rem;
}

[data-testid="stSidebar"] {
    border-right: 1px solid var(--rs-line);
    background: #F1EEE7;
}

.rs-sitebar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1.2rem;
    padding: .45rem .1rem .75rem;
    font-size: .82rem;
    color: #566B7C;
}

.rs-sitebar strong {
    color: #20384B;
    opacity: 1;
}

.rs-sitebar-links a {
    text-decoration: none;
    color: #20384B !important;
    font-weight: 800;
    margin-left: 1rem;
    opacity: 1 !important;
}

.rs-hero {
    position: relative;
    overflow: hidden;
    min-height: 305px;
    border-top: 3px solid var(--rs-orange);
    background:
        radial-gradient(circle at 98% 8%, rgba(255,255,255,.08) 0 70px, transparent 71px),
        radial-gradient(circle at 98% 8%, rgba(255,255,255,.05) 0 115px, transparent 116px),
        linear-gradient(115deg, var(--rs-hero) 0%, #0D4C60 52%, var(--rs-hero-2) 100%);
    color: white;
    margin: 0 -1.2rem 1.45rem;
    padding: 2.25rem 3.15rem 2.15rem;
}

.rs-hero-grid {
    display: grid;
    grid-template-columns: 1.18fr 0.82fr;
    gap: 2.5rem;
    align-items: center;
}

.rs-hero-eyebrow {
    color: #FF9C78;
    font-size: .80rem;
    font-weight: 850;
    letter-spacing: .16em;
    text-transform: uppercase;
    margin-bottom: .5rem;
}

.rs-hero h1 {
    margin: 0;
    max-width: 620px;
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(2.25rem, 4.7vw, 4.2rem);
    line-height: .92;
    color: white;
    letter-spacing: -.03em;
}

.rs-hero p {
    margin: .95rem 0 0;
    max-width: 660px;
    color: #F0F6F7;
    font-size: 1rem;
    line-height: 1.55;
}

.rs-hero-art {
    min-height: 215px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.rs-progress {
    position: absolute;
    right: 4rem;
    bottom: 1.2rem;
    color: #0A2F43;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1.2rem;
    font-weight: 800;
}

.rs-progress::after {
    content: "";
    display: block;
    width: 138px;
    height: 3px;
    margin-top: .35rem;
    background: linear-gradient(90deg, var(--rs-orange) 0 10%, rgba(255,255,255,.55) 10% 100%);
}

.rs-rail-title,
.rs-stage-label,
.rs-kicker,
.rs-side-title {
    font-weight: 850;
    letter-spacing: .15em;
    text-transform: uppercase;
}

.rs-rail-title {
    color: var(--rs-orange);
    font-size: .78rem;
    line-height: 1.2;
    margin-bottom: .4rem;
}

.rs-rail-count {
    font-family: Georgia, "Times New Roman", serif;
    font-size: 1rem;
    font-weight: 800;
    margin-bottom: .8rem;
}

.rs-stage-label {
    color: var(--rs-orange);
    font-size: .78rem;
    margin: .15rem 0;
}

.rs-stage-heading {
    font-family: Georgia, "Times New Roman", serif;
    color: var(--rs-ink);
    font-size: 2rem;
    line-height: 1.05;
    margin: 0 0 1.2rem;
}

.rs-kicker {
    color: var(--rs-orange);
    font-size: .74rem;
    margin-top: 1.5rem;
    margin-bottom: .38rem;
}

.rs-question {
    font-family: Georgia, "Times New Roman", serif;
    color: var(--rs-ink);
    font-size: 1.28rem;
    font-weight: 760;
    line-height: 1.4;
    margin-bottom: .85rem;
}

.rs-experiment-card {
    border: 1px solid var(--rs-line);
    border-radius: 10px;
    background: #F2EFE8;
    padding: .9rem 1rem;
    margin: .55rem 0 .7rem;
}

.rs-experiment-card .label {
    color: var(--rs-orange);
    font-size: .72rem;
    font-weight: 850;
    letter-spacing: .14em;
    text-transform: uppercase;
}

.rs-experiment-card .status {
    float: right;
    color: var(--rs-teal);
    font-size: .77rem;
    font-weight: 850;
}

.rs-workbench {
    border-radius: 9px;
    background: #102638;
    color: #F7FAFB;
    padding: 1rem 1.1rem;
    margin: .55rem 0 .9rem;
    font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    font-size: .87rem;
    line-height: 1.65;
    min-height: 126px;
    white-space: pre-wrap;
}

.rs-side-block {
    border-bottom: 1px solid var(--rs-line);
    padding: .25rem 0 1rem;
    margin-bottom: 1rem;
}

.rs-side-title { font-size: .76rem; margin-bottom: .38rem; }
.rs-side-title.orange { color: var(--rs-orange); }
.rs-side-title.teal { color: var(--rs-teal); }
.rs-side-title.purple { color: var(--rs-purple); }

.rs-side-copy {
    color: var(--rs-muted);
    line-height: 1.52;
    font-size: .93rem;
}

.rs-lock {
    border-left: 3px solid var(--rs-teal);
    padding: .65rem .8rem;
    background: var(--rs-teal-soft);
    color: var(--rs-ink);
    border-radius: 0 8px 8px 0;
}

.rs-daily {
    border-top: 1px solid var(--rs-line);
    margin-top: 1.25rem;
    padding-top: 1.15rem;
}

div[data-testid="stMetric"] {
    border: 1px solid var(--rs-line);
    border-radius: 9px;
    background: #FAF8F3;
    padding: .68rem .8rem;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--rs-line);
    border-radius: 8px;
}

.stButton > button {
    border-radius: 8px;
    border: 1px solid #D3CCC1;
    font-weight: 720;
    white-space: normal;
    height: auto;
    min-height: 46px;
    line-height: 1.15;
    padding: .52rem .66rem;
    text-align: left;
}

.stButton > button[kind="primary"] {
    background: var(--rs-orange);
    border-color: var(--rs-orange);
}

.rs-journey-divider {
    height: 1px;
    background: var(--rs-line);
    margin: .7rem 0;
}

.rs-small {
    color: var(--rs-muted);
    font-size: .84rem;
    line-height: 1.5;
}

@media (max-width: 900px) {
    .rs-hero {
        margin-left: -.6rem;
        margin-right: -.6rem;
        padding: 1.6rem 1.25rem 2.8rem;
    }
    .rs-hero-grid { grid-template-columns: 1fr; }
    .rs-hero-art { display: none; }
    .rs-progress { right: 1.3rem; }
}

header[data-testid="stHeader"] {
    display: none !important;
}

.rs-hero-art img {
    display: block;
    width: 100%;
    max-width: 420px;
    height: auto;
    margin: 0 auto;
}


.rs-hero-art {
    min-height: 225px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.rs-ui-graphic {
    width: 100%;
    max-width: 430px;
    min-height: 205px;
    display: grid;
    grid-template-columns: 118px 1fr;
    overflow: hidden;

    background: #FAF9F6;
    border: 1px solid rgba(255,255,255,.60);
    border-radius: 16px;

    box-shadow:
        0 18px 38px rgba(7, 32, 44, .24),
        0 3px 8px rgba(7, 32, 44, .16);
}

.rs-ui-sidebar {
    background: #EEECE7;
    border-right: 1px solid #D8D4CC;
    padding: 16px 13px;
}

.rs-ui-brand {
    color: #E86D4A;
    font-size: .61rem;
    font-weight: 900;
    letter-spacing: .12em;
    margin-bottom: 17px;
}

.rs-ui-field {
    height: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    background: #D3D9DB;
}

.rs-ui-field.short {
    width: 72%;
}

.rs-ui-slider {
    position: relative;
    height: 4px;
    margin: 16px 3px 17px;
    border-radius: 4px;
    background: #C7D0D2;
}

.rs-ui-slider::after {
    content: "";
    position: absolute;
    left: 57%;
    top: 50%;
    transform: translate(-50%, -50%);
    width: 11px;
    height: 11px;
    border-radius: 50%;
    background: #E86D4A;
}

.rs-ui-submit {
    margin-top: 9px;
    padding: 8px 5px;

    background: #E86D4A;
    color: white;

    border-radius: 7px;

    text-align: center;
    font-size: .62rem;
    font-weight: 900;
    letter-spacing: .06em;
}

.rs-ui-main {
    padding: 15px 17px 14px;
    color: #173044;
}

.rs-ui-topline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 11px;
}

.rs-ui-title {
    font-size: .67rem;
    font-weight: 900;
    letter-spacing: .10em;
    color: #576E7E;
}

.rs-ui-status {
    padding: 4px 7px;
    border-radius: 10px;

    background: #DDEEEB;
    color: #177D78;

    font-size: .56rem;
    font-weight: 900;
}

.rs-ui-chart {
    position: relative;
    height: 91px;
    margin: 6px 2px 13px 6px;

    border-left: 2px solid #CBD4D6;
    border-bottom: 2px solid #CBD4D6;
}

.rs-ui-bar {
    position: absolute;
    bottom: 0;

    width: 19px;

    background: #1A8580;
    border-radius: 4px 4px 0 0;
}

.rs-ui-bar.one {
    height: 42%;
    left: 13%;
}

.rs-ui-bar.two {
    height: 68%;
    left: 34%;
}

.rs-ui-bar.three {
    height: 55%;
    left: 55%;
}

.rs-ui-bar.four {
    height: 82%;
    left: 76%;
    background: #E86D4A;
}

.rs-ui-metrics {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 9px;
}

.rs-ui-metric {
    border: 1px solid #DDD8CF;
    background: white;
    border-radius: 9px;
    padding: 8px 10px;
}

.rs-ui-metric small {
    display: block;
    color: #667A88;
    font-size: .52rem;
    font-weight: 850;
    letter-spacing: .08em;
    margin-bottom: 2px;
}

.rs-ui-metric strong {
    display: block;
    color: #173044;
    font-size: 1.1rem;
}

.rs-ui-flow {
    margin-top: 9px;
    color: #657B88;
    text-align: center;
    font-size: .58rem;
    font-weight: 750;
    letter-spacing: .04em;
}

</style>
"""


def inject_css():
    st.markdown(CSS, unsafe_allow_html=True)


def sitebar():
    st.markdown(
        """
<div class="rs-sitebar">
  <div><strong>DATA &amp; AI REVIEW STUDIO</strong> · Hari Raj Singh</div>
  <div class="rs-sitebar-links">
    <a href="https://hari-raj-singh.com/data-ai/supervised-ml/" target="_blank">Supervised ML</a>
    <a href="https://hari-raj-singh.com/data-ai/sql/" target="_blank">SQL Mystery</a>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(stage_number: int, total: int):
    stage_text = f"{stage_number:02d} / {total:02d}"

    graphic = (
        '<div class="rs-hero-art">'
        '<div class="rs-ui-graphic">'

        '<div class="rs-ui-sidebar">'
        '<div class="rs-ui-brand">STREAMLIT REVIEW</div>'
        '<div class="rs-ui-field"></div>'
        '<div class="rs-ui-field short"></div>'
        '<div class="rs-ui-field"></div>'
        '<div class="rs-ui-slider"></div>'
        '<div class="rs-ui-submit">RUN FORM</div>'
        '</div>'

        '<div class="rs-ui-main">'
        '<div class="rs-ui-topline">'
        '<div class="rs-ui-title">MODEL EVIDENCE</div>'
        '<div class="rs-ui-status">READY</div>'
        '</div>'

        '<div class="rs-ui-chart">'
        '<div class="rs-ui-bar one"></div>'
        '<div class="rs-ui-bar two"></div>'
        '<div class="rs-ui-bar three"></div>'
        '<div class="rs-ui-bar four"></div>'
        '</div>'

        '<div class="rs-ui-metrics">'
        '<div class="rs-ui-metric">'
        '<small>CV SCORE</small>'
        '<strong>92.5%</strong>'
        '</div>'

        '<div class="rs-ui-metric">'
        '<small>FINAL TEST</small>'
        '<strong>LOCKED</strong>'
        '</div>'
        '</div>'

        '<div class="rs-ui-flow">'
        'INPUT → VALIDATE → DECIDE → TEST ONCE'
        '</div>'

        '</div>'
        '</div>'
        '</div>'
    )

    hero_html = (
        '<section class="rs-hero">'
        '<div class="rs-hero-grid">'

        '<div>'
        '<div class="rs-hero-eyebrow">'
        'Data &amp; AI · Interactive model selection lab'
        '</div>'
        '<h1>Pokémon<br>Model-Selection<br>Mystery</h1>'
        '<p>'
        'Ask one model-selection question. '
        'Run one experiment. Inspect the evidence. '
        'Lock the decision. Test once.'
        '</p>'
        '</div>'

        + graphic +

        '</div>'
        f'<div class="rs-progress">{stage_text}</div>'
        '</section>'
    )

    st.html(hero_html)


def rail_title(text: str, count: str | None = None):
    st.markdown(f'<div class="rs-rail-title">{html.escape(text)}</div>', unsafe_allow_html=True)
    if count:
        st.markdown(f'<div class="rs-rail-count">{html.escape(count)}</div>', unsafe_allow_html=True)


def stage_label(text: str):
    st.markdown(f'<div class="rs-stage-label">{html.escape(text)}</div>', unsafe_allow_html=True)


def stage_heading(text: str):
    st.markdown(f'<div class="rs-stage-heading">{html.escape(text)}</div>', unsafe_allow_html=True)


def eyebrow(text: str):
    st.markdown(f'<div class="rs-stage-label">{html.escape(text)}</div>', unsafe_allow_html=True)


def lede(text: str):
    st.markdown(f'<div class="rs-small">{html.escape(text)}</div>', unsafe_allow_html=True)


def kicker(text: str):
    st.markdown(f'<div class="rs-kicker">{html.escape(text)}</div>', unsafe_allow_html=True)


def question(text: str):
    st.markdown(f'<div class="rs-question">{html.escape(text)}</div>', unsafe_allow_html=True)


def experiment_card(copy: str, status: str):
    st.markdown(
        f"""
<div class="rs-experiment-card">
  <span class="label">Experiment</span>
  <span class="status">{html.escape(status)}</span>
  <div style="clear:both; margin-top:.35rem; color:#587086; line-height:1.45;">{html.escape(copy)}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def workbench(text: str):
    st.markdown(f'<div class="rs-workbench">{html.escape(text)}</div>', unsafe_allow_html=True)


def side_block(title: str, copy: str, tone: str = "orange"):
    st.markdown(
        f"""
<div class="rs-side-block">
  <div class="rs-side-title {tone}">{html.escape(title)}</div>
  <div class="rs-side-copy">{html.escape(copy)}</div>
</div>
""",
        unsafe_allow_html=True,
    )


def panel(text: str):
    st.markdown(f'<div class="rs-experiment-card">{text}</div>', unsafe_allow_html=True)


def lock_panel(text: str):
    st.markdown(f'<div class="rs-lock">{text}</div>', unsafe_allow_html=True)
