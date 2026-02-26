# src/predict.py

import joblib
import pandas as pd
import os
from preprocess import preprocess_for_prediction as preprocess_data

# make file paths robust by computing relative to this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "model.pkl")
model = joblib.load(MODEL_PATH)

def predict_student(input_dict):
    df = pd.DataFrame([input_dict])
    df = preprocess_data(df)
    prediction = model.predict(df)
    return prediction[0]

sample = {
    "school": "GP",
    "sex": "F",
    "age": 18,
    "address": "U",
    "famsize": "GT3",
    "Pstatus": "A",
    "Medu": 4,
    "Fedu": 4,
    "Mjob": "at_home",
    "Fjob": "teacher",
    "reason": "course",
    "guardian": "mother",
    "traveltime": 2,
    "studytime": 2,
    "failures": 0,
    "schoolsup": "yes",
    "famsup": "no",
    "paid": "no",
    "activities": "no",
    "nursery": "yes",
    "higher": "yes",
    "internet": "no",
    "romantic": "no",
    "famrel": 4,
    "freetime": 3,
    "goout": 4,
    "Dalc": 1,
    "Walc": 1,
    "health": 3,
    "absences": 6,
    "G1": 5,
    "G2": 6
}

print("Predicted Final Grade:", predict_student(sample))