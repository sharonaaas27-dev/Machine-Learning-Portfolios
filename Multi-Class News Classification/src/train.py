import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'news.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'models')

df = pd.read_csv(DATA_PATH, encoding='latin1', on_bad_lines='skip')
df['cleaned_text'] = df['news'].apply(clean_text)
X = df['cleaned_text']
le = LabelEncoder()
y = le.fit_transform(df['type'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,stratify=y)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=5000 , ngram_range=(1,2))),
    ('clf', LogisticRegression(max_iter=1000 , solver='lbfgs'))
])

pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred, target_names=le.classes_))
if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)
joblib.dump(pipeline, os.path.join(MODEL_PATH, 'news_classifier.pkl'))
joblib.dump(le, os.path.join(MODEL_PATH, 'label_encoder.pkl'))

print("Model and label encoder saved successfully.")