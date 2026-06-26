import streamlit as st
import pandas as pd
import joblib
import os
from src.preprocess import preprocess_for_prediction

model = joblib.load("models/model.pkl")

st.title("🎓 Student Final Grade Predictor")

age = st.number_input("Age", min_value=15, max_value=25)
studytime = st.slider("Study Time (1-4)", 1, 4)
failures = st.slider("Failures", 0, 4)
absences = st.number_input("Absences", 0, 100)
G1 = st.slider("G1 Grade", 0, 20)
G2 = st.slider("G2 Grade", 0, 20)

if st.button("Predict Final Grade"):
    
    sample = {
        "school": "GP",
        "sex": "F",
        "age": age,
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
        "studytime": studytime,
        "failures": failures,
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
        "absences": absences,
        "G1": G1,
        "G2": G2
    }

    df = pd.DataFrame([sample])
    df = preprocess_for_prediction(df)

    prediction = model.predict(df)

    st.success(f"🎯 Predicted Final Grade: {round(prediction[0],2)}")