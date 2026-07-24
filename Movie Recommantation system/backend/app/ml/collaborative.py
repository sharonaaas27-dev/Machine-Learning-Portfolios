import pickle
import os
import pandas as pd
import numpy as np
from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split

from app.ml.data_loader import load_ratings

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)


class CollaborativeFiltering:
    def __init__(self, n_factors: int = 100, n_epochs: int = 20):
        self.model = SVD(n_factors=n_factors, n_epochs=n_epochs, random_state=42)
        self.trainset = None
        self.testset = None
        self.ratings_df = None
        self.rmse = None
        self.mae = None

    def fit(self, ratings_df: pd.DataFrame = None):
        if ratings_df is None:
            ratings_df = load_ratings()
        self.ratings_df = ratings_df

        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(
            ratings_df[["userId", "movieId", "rating"]], reader
        )
        self.trainset, self.testset = train_test_split(
            data, test_size=0.2, random_state=42
        )
        self.model.fit(self.trainset)

        predictions = self.model.test(self.testset)
        self.rmse = accuracy.rmse(predictions, verbose=False)
        self.mae = accuracy.mae(predictions, verbose=False)
        return self

    def predict_rating(self, user_id: int, movie_id: int) -> float:
        prediction = self.model.predict(user_id, movie_id)
        return prediction.est

    def get_recommendations(
        self, user_id: int, movie_ids: list, rated_movie_ids: list, top_n: int = 10
    ) -> list[dict]:
        unseen = [mid for mid in movie_ids if mid not in rated_movie_ids]
        predictions = []
        for mid in unseen:
            est = self.predict_rating(user_id, mid)
            predictions.append({"movieId": mid, "predicted_rating": round(est, 4)})

        predictions.sort(key=lambda x: x["predicted_rating"], reverse=True)
        return predictions[:top_n]

    def save(self, path: str = None):
        if path is None:
            path = os.path.join(MODEL_DIR, "collaborative.pkl")
        with open(path, "wb") as f:
            pickle.dump({
                "model": self.model,
                "rmse": self.rmse,
                "mae": self.mae,
            }, f)

    def load(self, path: str = None):
        if path is None:
            path = os.path.join(MODEL_DIR, "collaborative.pkl")
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = pickle.load(f)
            self.model = data["model"]
            self.rmse = data.get("rmse")
            self.mae = data.get("mae")
            return True
        return False