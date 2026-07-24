from app.ml.content_based import ContentBasedFiltering
from app.ml.collaborative import CollaborativeFiltering


class HybridRecommender:
    def __init__(self):
        self.content_based = ContentBasedFiltering()
        self.collaborative = CollaborativeFiltering()
        self.content_weight = 0.3
        self.collaborative_weight = 0.7

    def fit(self, movies_df=None, ratings_df=None):
        self.content_based.fit(movies_df)
        self.collaborative.fit(ratings_df)

    def get_recommendations(
        self,
        user_id: int,
        movie_id: int,
        all_movie_ids: list,
        rated_movie_ids: list,
        top_n: int = 10,
    ) -> list[dict]:
        content_recs = self.content_based.get_recommendations(movie_id, top_n=20)
        collab_recs = self.collaborative.get_recommendations(
            user_id, all_movie_ids, rated_movie_ids, top_n=20
        )

        content_map = {
            r["movieId"]: r["similarity_score"] for r in content_recs
        }
        collab_map = {
            r["movieId"]: r["predicted_rating"] / 5.0 for r in collab_recs
        }

        all_ids = set(content_map.keys()) | set(collab_map.keys())
        scored = []
        for mid in all_ids:
            c_score = content_map.get(mid, 0)
            col_score = collab_map.get(mid, 0)
            hybrid = (
                self.content_weight * c_score
                + self.collaborative_weight * col_score
            )
            scored.append({
                "movieId": mid,
                "hybrid_score": round(hybrid, 4),
                "content_score": c_score,
                "collaborative_score": round(col_score * 5, 4),
            })

        scored.sort(key=lambda x: x["hybrid_score"], reverse=True)
        return scored[:top_n]