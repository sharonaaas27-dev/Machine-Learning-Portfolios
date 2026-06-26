import streamlit as st
import sys
import os

BASE_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.join(BASE_DIR, "src")

sys.path.append(SRC_PATH)
from predict import predict_sentiment
st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to predict its sentiment (positive or negative).")
review = st.text_area("Movie Review", height=200)
if st.button("Predict Sentiment"):
    if review:
        sentiment = predict_sentiment(review)
        st.success("Predicted Sentiment: Positive") if sentiment == 1 else st.warning("Predicted Sentiment: Negative")
        
    else:
        st.warning("Please enter a movie review to predict its sentiment.")