from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess import df

vectorizer = TfidfVectorizer(max_features=5000,
                             ngram_range=(1, 2),
                             max_df=0.8,
                             min_df=5)
X = vectorizer.fit_transform(df['cleaned'])
y = df['real']