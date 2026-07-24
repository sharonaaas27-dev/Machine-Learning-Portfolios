import os
import pandas as pd
from app.ml.data_loader import load_movies, load_ratings
from app.ml.content_based import ContentBasedFiltering
from app.ml.collaborative import CollaborativeFiltering
from app.ml.hybrid import HybridRecommender

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)


def train_all_models(force: bool = False):
    cb_path = os.path.join(MODEL_DIR, "content_based.pkl")
    col_path = os.path.join(MODEL_DIR, "collaborative.pkl")

    movies_df = load_movies()
    ratings_df = load_ratings()

    print("Training Content-Based Filtering model...")
    cb = ContentBasedFiltering()
    if os.path.exists(cb_path) and not force:
        cb.load(cb_path)
        print("Content-Based model loaded from cache.")
    else:
        cb.fit(movies_df)
        cb.save(cb_path)
        print("Content-Based model trained and saved.")

    print("Training Collaborative Filtering model...")
    col = CollaborativeFiltering()
    if os.path.exists(col_path) and not force:
        col.load(col_path)
        print(f"Collaborative model loaded from cache. RMSE: {col.rmse:.4f}, MAE: {col.mae:.4f}")
    else:
        col.fit(ratings_df)
        col.save(col_path)
        print(f"Collaborative model trained and saved. RMSE: {col.rmse:.4f}, MAE: {col.mae:.4f}")

    print("All models trained successfully!")
    return cb, col