import pickle
import os
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.ml.data_loader import load_movies

MODEL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "models")
os.makedirs(MODEL_DIR, exist_ok=True)


class ContentBasedFiltering:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(tokenizer=self._split_genres, token_pattern=None)
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.movies_df = None
        self.movie_indices = None

    def _split_genres(self, text: str):
        return text.split("|")

    def fit(self, movies_df: pd.DataFrame = None):
        if movies_df is None:
            movies_df = load_movies()
        self.movies_df = movies_df
        self.movies_df["genres"] = self.movies_df["genres"].fillna("")

        self.tfidf_matrix = self.vectorizer.fit_transform(self.movies_df["genres"])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        self.movie_indices = pd.Series(
            self.movies_df.index, index=self.movies_df["movieId"]
        ).drop_duplicates()
        return self

    def get_recommendations(self, movie_id: int, top_n: int = 10) -> list[dict]:
        if self.cosine_sim is None:
            self.fit()

        if movie_id not in self.movie_indices:
            return []

        idx = self.movie_indices[movie_id]
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1 : top_n + 1]
        movie_indices_list = [i[0] for i in sim_scores]
        scores = [float(i[1]) for i in sim_scores]

        results = []
        for idx, score in zip(movie_indices_list, scores):
            movie = self.movies_df.iloc[idx]
            results.append({
                "movieId": int(movie["movieId"]),
                "title": movie["title"],
                "genres": movie["genres"],
                "similarity_score": round(score, 4),
            })
        return results

    def save(self, path: str = None):
        if path is None:
            path = os.path.join(MODEL_DIR, "content_based.pkl")
        with open(path, "wb") as f:
            pickle.dump({
                "vectorizer": self.vectorizer,
                "tfidf_matrix": self.tfidf_matrix,
                "cosine_sim": self.cosine_sim,
                "movies_df": self.movies_df,
                "movie_indices": self.movie_indices,
            }, f)

    def load(self, path: str = None):
        if path is None:
            path = os.path.join(MODEL_DIR, "content_based.pkl")
        if os.path.exists(path):
            with open(path, "rb") as f:
                data = pickle.load(f)
            self.vectorizer = data["vectorizer"]
            self.tfidf_matrix = data["tfidf_matrix"]
            self.cosine_sim = data["cosine_sim"]
            self.movies_df = data["movies_df"]
            self.movie_indices = data["movie_indices"]
            return True
        return False