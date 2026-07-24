import os
import zipfile
import urllib.request
import pandas as pd
from app.config import settings


def download_movielens():
    dataset_dir = settings.DATASET_DIR
    zip_path = os.path.join(dataset_dir, "ml-latest-small.zip")
    extract_path = dataset_dir

    if os.path.exists(os.path.join(dataset_dir, "ml-latest-small", "movies.csv")):
        return os.path.join(dataset_dir, "ml-latest-small")

    os.makedirs(dataset_dir, exist_ok=True)

    if not os.path.exists(zip_path):
        print(f"Downloading MovieLens dataset from {settings.MOVIELENS_URL}...")
        urllib.request.urlretrieve(settings.MOVIELENS_URL, zip_path)
        print("Download complete.")

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)
    print(f"Extracted to {extract_path}")

    return os.path.join(dataset_dir, "ml-latest-small")


def load_movies(data_dir: str = None) -> pd.DataFrame:
    if data_dir is None:
        data_dir = download_movielens()
    movies_path = os.path.join(data_dir, "movies.csv")
    return pd.read_csv(movies_path)


def load_ratings(data_dir: str = None) -> pd.DataFrame:
    if data_dir is None:
        data_dir = download_movielens()
    ratings_path = os.path.join(data_dir, "ratings.csv")
    return pd.read_csv(ratings_path)


def load_tags(data_dir: str = None) -> pd.DataFrame:
    if data_dir is None:
        data_dir = download_movielens()
    tags_path = os.path.join(data_dir, "tags.csv")
    if os.path.exists(tags_path):
        return pd.read_csv(tags_path)
    return pd.DataFrame(columns=["userId", "movieId", "tag", "timestamp"])