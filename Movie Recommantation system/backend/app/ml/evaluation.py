import pandas as pd
from app.ml.metrics import calculate_rmse, calculate_mae, precision_at_k, recall_at_k, f1_score_at_k
from app.ml.data_loader import load_ratings, load_movies
from app.ml.collaborative import CollaborativeFiltering
from app.ml.content_based import ContentBasedFiltering
from app.ml.hybrid import HybridRecommender
from app.ml.preprocessing import split_ratings


def evaluate_collaborative(model: CollaborativeFiltering = None) -> dict:
    ratings_df = load_ratings()
    train_df, test_df = split_ratings(ratings_df)

    if model is None:
        model = CollaborativeFiltering()
        from surprise import Dataset, Reader
        from surprise.model_selection import train_test_split
        reader = Reader(rating_scale=(0.5, 5.0))
        data = Dataset.load_from_df(train_df[["userId", "movieId", "rating"]], reader)
        trainset, _ = train_test_split(data, test_size=0.2, random_state=42)
        model.model.fit(trainset)

    y_true = []
    y_pred = []
    for _, row in test_df.iterrows():
        pred = model.predict_rating(row["userId"], row["movieId"])
        y_true.append(row["rating"])
        y_pred.append(pred)

    return {
        "rmse": calculate_rmse(y_true, y_pred),
        "mae": calculate_mae(y_true, y_pred),
    }


def evaluate_content_based(movie_id: int = 1, k: int = 10) -> dict:
    movies_df = load_movies()
    model = ContentBasedFiltering()
    model.fit(movies_df)
    recs = model.get_recommendations(movie_id, top_n=k)
    return {
        "movie_id": movie_id,
        "recommendations": len(recs),
        "top_similarity": recs[0]["similarity_score"] if recs else 0,
    }