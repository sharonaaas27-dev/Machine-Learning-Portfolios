import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report, confusion_matrix
from preprocess import clean_text
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, 'data', 'IMDB Dataset.csv')
model_path = os.path.join(BASE_DIR,'models')

df = pd.read_csv(data_path)
df['cleaned_text'] = df['review'].apply(clean_text)
X = df['cleaned_text']

df['sentiment'] = le.fit_transform(df['sentiment'])
y = df['sentiment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000)),
    ('clf', LinearSVC())
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))    
print(confusion_matrix(y_test, y_pred))
joblib.dump(pipeline, os.path.join(model_path, 'sentiment_model.pkl'))

print("Model trained and saved successfully.")