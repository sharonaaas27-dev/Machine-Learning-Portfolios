import os 
import joblib
from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR,'models', 'sentiment_model.pkl')

def predict_sentiment(review):
    model = joblib.load(model_path)
    cleaned_review = clean_text(review)
    prediction = model.predict([cleaned_review])
    return prediction[0]