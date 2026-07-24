import os
import json
import joblib
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix
from .data_loader import load_dataset
from .feature_engineering import extract_features
from .preprocessing import preprocess_text
from ..config import MODEL_PATH, VECTORIZER_PATH, METRICS_PATH


MODELS = {
    "Naive Bayes": MultinomialNB(),
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
    "Linear SVM": LinearSVC(random_state=42, dual=False),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=42),
}


def train_model():
    df = load_dataset()
    df["processed"] = df["message"].apply(preprocess_text)

    X = df["message"]
    y = (df["label"] == "spam").astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    X_train_vec, vectorizer = extract_features(X_train, fit=True)
    X_test_vec, _ = extract_features(X_test, vectorizer, fit=False)

    best_model = None
    best_score = 0
    best_name = ""
    results = {}

    for name, model in MODELS.items():
        model.fit(X_train_vec, y_train)
        y_pred = model.predict(X_test_vec)
        y_prob = model.predict_proba(X_test_vec)[:, 1] if hasattr(model, "predict_proba") else None

        acc = accuracy_score(y_test, y_pred)

        if acc > best_score:
            best_score = acc
            best_model = model
            best_name = name

        results[name] = {
            "accuracy": acc,
            "precision": precision_score(y_test, y_pred, zero_division=0),
            "recall": recall_score(y_test, y_pred, zero_division=0),
            "f1_score": f1_score(y_test, y_pred, zero_division=0),
        }

        if y_prob is not None:
            try:
                results[name]["roc_auc"] = roc_auc_score(y_test, y_prob)
            except Exception:
                results[name]["roc_auc"] = 0.0

    cv_scores = cross_val_score(best_model, X_train_vec, y_train, cv=5, scoring="accuracy")
    y_pred_best = best_model.predict(X_test_vec)
    y_prob_best = best_model.predict_proba(X_test_vec)[:, 1] if hasattr(best_model, "predict_proba") else None

    cm = confusion_matrix(y_test, y_pred_best).tolist()

    metrics = {
        "best_model": best_name,
        "accuracy": best_score,
        "precision": precision_score(y_test, y_pred_best, zero_division=0),
        "recall": recall_score(y_test, y_pred_best, zero_division=0),
        "f1_score": f1_score(y_test, y_pred_best, zero_division=0),
        "roc_auc": roc_auc_score(y_test, y_prob_best) if y_prob_best is not None else 0.0,
        "cross_val_mean": float(np.mean(cv_scores)),
        "cross_val_std": float(np.std(cv_scores)),
        "confusion_matrix": cm,
        "model_comparison": results,
        "training_samples": len(df),
        "feature_count": X_train_vec.shape[1],
    }

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(best_model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    with open(METRICS_PATH, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Best model: {best_name} (accuracy: {best_score:.4f})")
    print(f"Model saved to {MODEL_PATH}")
    print(f"Vectorizer saved to {VECTORIZER_PATH}")
    print(f"Metrics saved to {METRICS_PATH}")

    return metrics
