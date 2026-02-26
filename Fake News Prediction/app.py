import os
import sys
import streamlit as st
import joblib


src_path = os.path.join(os.path.dirname(__file__), "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from preprocess import clean_text

# Use project-relative model paths
models_dir = os.path.join(os.path.dirname(__file__), "models")
model = joblib.load(os.path.join(models_dir, "model.pkl"))
vectorizer = joblib.load(os.path.join(models_dir, "vectorizer.pkl"))

st.title("Fake News Detection App")

input_text = st.text_area("Enter News Text")

if st.button("Predict"):
    clean = clean_text(input_text)
    vec = vectorizer.transform([clean])
    prediction = model.predict(vec)
    
    # In dataset `real==1` means real news; show messages accordingly
    if prediction[0] == 0:
        st.success("This is Real News")
    else:
        st.error("This is Fake News")