from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)
from .model_loader import load_model
from .feature_engineering import extract_features
from .data_loader import load_dataset
from .preprocessing import preprocess_text
from sklearn.model_selection import train_test_split


def evaluate_model():
    model, vectorizer = load_model()
    df = load_dataset()

    X = df["message"]
    y = (df["label"] == "spam").astype(int)

    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    X_test_vec = extract_features(X_test, vectorizer, fit=False)

    y_pred = model.predict(X_test_vec)
    y_prob = model.predict_proba(X_test_vec)[:, 1] if hasattr(model, "predict_proba") else None

    results = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, zero_division=0),
        "recall": recall_score(y_test, y_pred, zero_division=0),
        "f1_score": f1_score(y_test, y_pred, zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
        "classification_report": classification_report(y_test, y_pred, output_dict=True, zero_division=0),
    }

    if y_prob is not None:
        results["roc_auc"] = roc_auc_score(y_test, y_prob)

    return results
