import streamlit as st
from src.predict import predict_resume

st.title("Resume Screening System")

resume_input = st.text_area("Paste Resume Text")

if st.button("Predict Job Role"):
    result = predict_resume(resume_input)
    st.success(f"Predicted Role: {result}")