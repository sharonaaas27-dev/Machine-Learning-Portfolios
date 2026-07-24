import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./spam_classifier.db")
MODEL_PATH = os.getenv("MODEL_PATH", "models/spam_classifier.pkl")
VECTORIZER_PATH = os.getenv("VECTORIZER_PATH", "models/vectorizer.pkl")
METRICS_PATH = os.getenv("METRICS_PATH", "models/metrics.json")
DATASET_URL = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/sms.tsv"
DATASET_PATH = os.getenv("DATASET_PATH", "datasets/sms_spam.csv")
