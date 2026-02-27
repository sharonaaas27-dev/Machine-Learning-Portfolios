import os
import sys

# when the package modules are imported from outside the src folder we need to
# make sure the project root is on sys.path so that `src` is discoverable.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import joblib
from src.preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
models_dir = os.path.join(BASE_DIR, "models")

model = joblib.load(os.path.join(models_dir, "model.pkl"))
vectorizer = joblib.load(os.path.join(models_dir, "vectorizer.pkl"))

print("Models directory:", models_dir)
print("Full model path:", os.path.join(models_dir, "model.pkl"))

def predict_resume(text):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)
    return prediction[0]