import os
import joblib
from ..config import MODEL_PATH, VECTORIZER_PATH


def load_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError("Model not found. Train the model first.")
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    return model, vectorizer


def is_model_trained() -> bool:
    return os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH)
