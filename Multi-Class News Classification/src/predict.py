import os
import joblib
from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "news_classifier.pkl")

model = joblib.load(model_path)

def predict(text):
    cleaned = clean_text(text)
    prediction = model.predict([cleaned])
    return prediction[0]