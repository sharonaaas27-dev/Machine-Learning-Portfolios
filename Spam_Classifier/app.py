import streamlit as st
import sys
import os

BASE_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.join(BASE_DIR, "src")
sys.path.append(SRC_PATH)
from predict import predict_message

st.title("Spam Detection App")

user_input = st.text_area("Enter your message here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to predict.")
    else:
        prediction = predict_message(user_input)
        if prediction == 1:
            st.error("🚨 This is SPAM.")
        else:
            st.success("✅ This is HAM (Not Spam)")