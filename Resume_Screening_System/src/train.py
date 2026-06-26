import pandas as pd
import os
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "Resume Screening.csv")
model_dir = os.path.join(BASE_DIR, "models")

os.makedirs(model_dir, exist_ok=True)

df = pd.read_csv(data_path, encoding= "ISO-8859-1") 
df['cleaned'] = df['Resume'].apply(clean_text)

X = df['cleaned']
le = LabelEncoder()
y = le.fit_transform(df['Category'])
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1,2), max_features=6000)),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)

pred = pipeline.predict(X_test)

print(classification_report(y_test, pred))

joblib.dump(pipeline, os.path.join(model_dir, "models.pkl"))

print("Resume Screening Model Saved.")