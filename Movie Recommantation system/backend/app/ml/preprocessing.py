import pandas as pd
import numpy as np
from typing import Tuple


def preprocess_movies(movies_df: pd.DataFrame) -> pd.DataFrame:
    df = movies_df.copy()
    df["genres"] = df["genres"].fillna("")
    df["year"] = df["title"].str.extract(r"\((\d{4})\)").fillna(0).astype(int)
    df["title_clean"] = df["title"].str.replace(r"\s*\(\d{4}\)\s*", "", regex=True)
    return df


def preprocess_ratings(ratings_df: pd.DataFrame) -> pd.DataFrame:
    df = ratings_df.copy()
    df = df.dropna(subset=["rating"])
    df["rating"] = df["rating"].astype(float)
    return df


def create_user_item_matrix(ratings_df: pd.DataFrame) -> pd.DataFrame:
    return ratings_df.pivot_table(
        index="userId", columns="movieId", values="rating"
    ).fillna(0)


def split_ratings(
    ratings_df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    from sklearn.model_selection import train_test_split
    return train_test_split(
        ratings_df, test_size=test_size, random_state=random_state
    )


def get_genre_list(movies_df: pd.DataFrame) -> list:
    all_genres = set()
    for genres in movies_df["genres"].str.split("|"):
        if isinstance(genres, list):
            all_genres.update(genres)
    return sorted([g for g in all_genres if g and g != "(no genres listed)"])