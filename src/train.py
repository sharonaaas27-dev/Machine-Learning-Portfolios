import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib

from src.preprocess import clean_text

os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), "models"), exist_ok=True)

data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "resume_data.csv")

df = pd.read_csv(data_path)

text_col = "career_objective" if "career_objective" in df.columns else df.columns[0]
df[text_col] = df[text_col].fillna("")

df['clean_text'] = df[text_col].apply(clean_text)



vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1,2),
    min_df=5,
    max_df=0.8
)

X = vectorizer.fit_transform(df['clean_text'])

y = df['skills'].astype(str)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

joblib.dump(model, "models/model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")


print("Model saved successfully!")