import time
import numpy as np
from .model_loader import load_model
from .feature_engineering import extract_features
from .preprocessing import preprocess_text


SPAM_KEYWORDS = [
    "free", "win", "winner", "won", "cash", "prize", "congratulations",
    "claim", "click", "limited", "offer", "urgent", "guaranteed",
    "act now", "exclusive", "reward", "bonus", "credit", "selected",
    "expires", "trial", "subscribe", "discount", "promo", "sms",
    "text", "call", "rate", "stop", "opt", "txt",
]


def predict_message(message: str):
    start_time = time.time()

    model, vectorizer = load_model()
    features = extract_features([message], vectorizer, fit=False)

    spam_prob = model.predict_proba(features)[0, 1]
    ham_prob = model.predict_proba(features)[0, 0]

    prediction = "spam" if spam_prob >= 0.5 else "ham"
    confidence = max(spam_prob, ham_prob)

    feature_names = vectorizer.get_feature_names_out()
    feature_coeffs = features.toarray()[0]
    nonzero_indices = feature_coeffs.nonzero()[0]

    word_contributions = []
    for idx in nonzero_indices:
        word = feature_names[idx]
        contrib = feature_coeffs[idx]
        word_contributions.append((word, contrib))

    word_contributions.sort(key=lambda x: x[1], reverse=True)
    top_keywords = [w for w, _ in word_contributions[:5]]

    processed_message = preprocess_text(message)
    found_keywords = [kw for kw in SPAM_KEYWORDS if kw in processed_message.lower()]

    if prediction == "spam":
        if found_keywords:
            explanation = f"This message is classified as Spam because it contains promotional words like '{', '.join(found_keywords[:5])}'."
        elif top_keywords:
            explanation = f"This message is classified as Spam because it contains suspicious words like '{', '.join(top_keywords)}'."
        else:
            explanation = "This message is classified as Spam based on its overall pattern and structure."
    else:
        explanation = "This message is classified as Ham (not spam) as it appears to be a legitimate personal or business message."

    processing_time = time.time() - start_time

    return {
        "prediction": prediction,
        "confidence": round(float(confidence), 4),
        "spam_probability": round(float(spam_prob), 4),
        "ham_probability": round(float(ham_prob), 4),
        "processing_time": round(processing_time, 4),
        "top_keywords": top_keywords,
        "explanation": explanation,
    }


def predict_batch(messages: list):
    results = []
    for msg in messages:
        result = predict_message(msg)
        results.append(result)
    return results
