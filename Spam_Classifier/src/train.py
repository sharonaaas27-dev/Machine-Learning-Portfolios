import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from preprocess import clean_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR,'data','combined_data.csv')
model_path = os.path.join(BASE_DIR,'model')

os.makedirs(model_path, exist_ok=True)

df = pd.read_csv(data_path)
df = df[['label', 'text']]

df['text'] = df['text'].fillna("")
df['text'] = df['text'].astype(str)
df['text'] = df['text'].apply(clean_text)

df = df[df['text'].str.strip() != ""]

X = df['text']
y = df['label']

vectorizer = TfidfVectorizer()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model =  MultinomialNB()
model.fit(X_train, y_train)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

y_pred = model.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

joblib.dump(model,os.path.join(model_path,'model.pkl'))
joblib.dump(vectorizer,os.path.join(model_path,'vectorizer.pkl'))
print("Model and vectorizer saved successfully.")