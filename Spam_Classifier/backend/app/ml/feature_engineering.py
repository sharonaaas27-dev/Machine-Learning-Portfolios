from sklearn.feature_extraction.text import TfidfVectorizer
from .preprocessing import preprocess_text


def get_vectorizer(max_features: int = 5000, ngram_range: tuple = (1, 2)):
    return TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        preprocessor=preprocess_text,
        analyzer="word",
        sublinear_tf=True,
    )


def extract_features(texts, vectorizer=None, fit: bool = True):
    if vectorizer is None:
        vectorizer = get_vectorizer()
    if fit:
        features = vectorizer.fit_transform(texts)
    else:
        features = vectorizer.transform(texts)
    return features, vectorizer


def get_feature_names(vectorizer):
    return vectorizer.get_feature_names_out()
