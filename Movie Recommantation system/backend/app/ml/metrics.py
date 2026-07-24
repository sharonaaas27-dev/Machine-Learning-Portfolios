import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error


def calculate_rmse(y_true: list, y_pred: list) -> float:
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def calculate_mae(y_true: list, y_pred: list) -> float:
    return float(mean_absolute_error(y_true, y_pred))


def precision_at_k(relevant: list, recommended: list, k: int = 10) -> float:
    if not recommended or k == 0:
        return 0.0
    top_k = recommended[:k]
    relevant_set = set(relevant)
    hits = sum(1 for item in top_k if item in relevant_set)
    return hits / min(k, len(top_k))


def recall_at_k(relevant: list, recommended: list, k: int = 10) -> float:
    if not relevant:
        return 0.0
    top_k = recommended[:k]
    relevant_set = set(relevant)
    hits = sum(1 for item in top_k if item in relevant_set)
    return hits / len(relevant)


def f1_score_at_k(relevant: list, recommended: list, k: int = 10) -> float:
    p = precision_at_k(relevant, recommended, k)
    r = recall_at_k(relevant, recommended, k)
    if p + r == 0:
        return 0.0
    return 2 * (p * r) / (p + r)