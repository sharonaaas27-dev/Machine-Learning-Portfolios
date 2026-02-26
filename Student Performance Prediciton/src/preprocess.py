# src/preprocess.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os


def load_data(path: str) -> pd.DataFrame:
    """Load dataset from CSV file path."""
    return pd.read_csv(path)

def preprocess_and_save_encoders(df):
    df = df.copy()
    categorical_cols = df.select_dtypes(include=['object']).columns
    
    encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
    
    os.makedirs("../models", exist_ok=True)
    joblib.dump(encoders, "../models/encoders.pkl")
    
    return df

def preprocess_for_prediction(df):
    encoders = joblib.load("../models/encoders.pkl")
    
    for col, le in encoders.items():
        df[col] = le.transform(df[col])
        
    return df