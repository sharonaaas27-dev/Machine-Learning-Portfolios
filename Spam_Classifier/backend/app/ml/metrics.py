import json
import os
from ..config import METRICS_PATH


def load_metrics():
    if not os.path.exists(METRICS_PATH):
        return None
    with open(METRICS_PATH, "r") as f:
        return json.load(f)


def get_model_comparison():
    metrics = load_metrics()
    if metrics is None:
        return {}
    return metrics.get("model_comparison", {})


def get_best_model_name():
    metrics = load_metrics()
    if metrics is None:
        return "Unknown"
    return metrics.get("best_model", "Unknown")


def get_confusion_matrix():
    metrics = load_metrics()
    if metrics is None:
        return [[0, 0], [0, 0]]
    return metrics.get("confusion_matrix", [[0, 0], [0, 0]])
