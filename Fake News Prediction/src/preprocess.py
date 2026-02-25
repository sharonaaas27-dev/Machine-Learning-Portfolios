import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

df = pd.read_csv('data/FakeNewsNet.csv')

print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())


df = df.dropna(subset=['news_url'])
df['source_domain'] = df['source_domain'].fillna('unknown')

print(df.head())
print(df.info())
print(df.shape)
print(df.isnull().sum())

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\d+', '', text) 
    words = text.split()
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

df["cleaned"] = df["title"].apply(clean_text)
print(df[["title", "cleaned"]].head())