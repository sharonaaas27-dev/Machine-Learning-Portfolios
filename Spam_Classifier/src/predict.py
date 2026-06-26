import os
import joblib
from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR,'model','model.pkl')
vectorizer_path = os.path.join(BASE_DIR,'model','vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_message(text):
    text = clean_text(text)
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]
print(predict_message("Congratulations! You've won a free ticket to the Bahamas!"))