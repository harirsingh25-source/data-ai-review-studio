from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class ReviewModule:
    slug: str
    title: str
    icon: str
    status: str
    description: str
    renderer: Callable[[], None] | None = None


def get_modules():
    from reviews.model_selection.page import render as render_model_selection

    return [
        ReviewModule(
            slug="model-selection",
            title="Model Selection Mystery",
            icon="🏆",
            status="Ready",
            description="Cross-validation, leakage, pipelines and GridSearchCV.",
            renderer=render_model_selection,
        ),
        ReviewModule(
            slug="time-series",
            title="Time-Series Investigation",
            icon="📈",
            status="Planned",
            description="Temporal splits, lags, leakage and forecasting evidence.",
        ),
        ReviewModule(
            slug="transformers",
            title="Attention Detective",
            icon="🧠",
            status="Planned",
            description="Tokens, embeddings, self-attention and Transformers.",
        ),
        ReviewModule(
            slug="cnn-rnn",
            title="Deep Learning Lab",
            icon="🔬",
            status="Planned",
            description="CNNs, RNNs, LSTMs and transfer learning.",
        ),
        ReviewModule(
            slug="experimentation",
            title="A/B Testing Case",
            icon="🧪",
            status="Planned",
            description="Hypotheses, effect sizes, uncertainty and decisions.",
        ),
        ReviewModule(
            slug="mlops",
            title="MLOps Mission",
            icon="🚀",
            status="Planned",
            description="MLflow, model serving, monitoring and cloud deployment.",
        ),
        ReviewModule(
            slug="sql-mystery",
            title="SQL Dinner-Party Mystery",
            icon="🍽️",
            status="Integrate next",
            description="Bring the existing SQL game into the same review shell.",
        ),
    ]
