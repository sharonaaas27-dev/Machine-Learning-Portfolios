import streamlit as st
from src.predict import predict

st.set_page_config(page_title="News Classifier", layout="centered")

st.title("📰 News Topic Classifier")
st.write("This model predicts the category of a news article.")

user_input = st.text_area("Enter News Article Text")

if st.button("Classify"):
    if user_input.strip():
        prediction = predict(user_input)
        if prediction == 0:
            prediction = "business"
        elif prediction == 1:
            prediction = "entertainment"
        elif prediction == 2:
            prediction = "politics"
        elif prediction == 3:
            prediction = "sports"
        elif prediction == 4:
            prediction = "technology"
        st.success(f"The predicted category is   **{prediction}**")
    else:
        st.warning("Please enter some text to classify.")