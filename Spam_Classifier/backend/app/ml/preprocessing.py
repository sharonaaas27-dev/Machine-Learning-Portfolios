import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("punkt", quiet=True)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize(text: str) -> list:
    return nltk.word_tokenize(text)


def remove_stopwords(tokens: list) -> list:
    return [t for t in tokens if t not in stop_words]


def stem_tokens(tokens: list) -> list:
    return [stemmer.stem(t) for t in tokens]


def lemmatize_tokens(tokens: list) -> list:
    return [lemmatizer.lemmatize(t) for t in tokens]


def preprocess_text(text: str) -> str:
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    return " ".join(tokens)
