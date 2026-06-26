import os
import joblib
from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_dir = os.path.join(BASE_DIR, "models", "models.pkl")

def predict_category(text):
    model = joblib.load(model_dir)
    cleaned_text = clean_text(text)
    prediction = model.predict([cleaned_text])
    return prediction[0]
