import streamlit as st
from src.predict import predict_category
from src.utils import extract_text_from_pdf

st.title("Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    text = extract_text_from_pdf(uploaded_file)
    
    if st.button("Predict Job Domain"):
        result = predict_category(text)
        st.success(f"Predicted Job Domain: {result}")
    else:
        st.warning("Click the button to predict the job domain.")

else :
    st.info("Please upload a PDF resume to get started.")