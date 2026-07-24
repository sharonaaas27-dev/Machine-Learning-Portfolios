from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.models.movie import Movie
from app.services.auth import get_current_user
from app.ml.predict import get_content_model, get_collaborative_model, get_hybrid_model
from app.ml.data_loader import load_movies

router = APIRouter(prefix="/recommend", tags=["Recommendations"])


@router.get("/content/{movie_id}")
def content_based_recommendations(
    movie_id: int,
    top_n: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
):
    movie = db.query(Movie).filter(Movie.movieId == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    model = get_content_model()
    recs = model.get_recommendations(movie_id, top_n)

    enriched = []
    for rec in recs:
        m = db.query(Movie).filter(Movie.movieId == rec["movieId"]).first()
        enriched.append({
            **rec,
            "poster_path": m.poster_path if m else "",
            "overview": m.overview if m else "",
            "average_rating": m.average_rating if m else 0,
        })
    return enriched


@router.get("/collaborative")
def collaborative_recommendations(
    top_n: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    model = get_collaborative_model()
    all_movies = db.query(Movie).all()
    all_movie_ids = [m.movieId for m in all_movies]

    from app.models.rating import Rating
    rated = db.query(Rating).filter(Rating.user_id == current_user.id).all()
    rated_ids = [r.movie_id for r in rated]

    recs = model.get_recommendations(current_user.id, all_movie_ids, rated_ids, top_n)

    enriched = []
    for rec in recs:
        m = db.query(Movie).filter(Movie.movieId == rec["movieId"]).first()
        if m:
            enriched.append({
                "movieId": rec["movieId"],
                "title": m.title,
                "genres": m.genres,
                "poster_path": m.poster_path,
                "overview": m.overview,
                "average_rating": m.average_rating,
                "predicted_rating": rec["predicted_rating"],
            })
    return enriched


@router.get("/hybrid")
def hybrid_recommendations(
    top_n: int = Query(10, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    model = get_hybrid_model()
    all_movies = db.query(Movie).all()
    all_movie_ids = [m.movieId for m in all_movies]

    from app.models.rating import Rating
    rated = db.query(Rating).filter(Rating.user_id == current_user.id).all()
    rated_ids = [r.movie_id for r in rated]

    if not rated_ids:
        raise HTTPException(status_code=400, detail="Rate some movies first to get hybrid recommendations")

    genre_prefs = db.query(Movie.genres).filter(Movie.movieId.in_(rated_ids)).all()
    genre_list = []
    for g in genre_prefs:
        genre_list.extend(g[0].split("|"))
    from collections import Counter
    top_genres = [g for g, _ in Counter(genre_list).most_common(3)]

    recs = model.get_recommendations(
        current_user.id, rated_ids[0] if rated_ids else 1,
        all_movie_ids, rated_ids, top_n
    )

    enriched = []
    for rec in recs:
        m = db.query(Movie).filter(Movie.movieId == rec["movieId"]).first()
        if m:
            enriched.append({
                "movieId": rec["movieId"],
                "title": m.title,
                "genres": m.genres,
                "poster_path": m.poster_path,
                "overview": m.overview,
                "average_rating": m.average_rating,
                "hybrid_score": rec["hybrid_score"],
                "content_score": rec["content_score"],
                "collaborative_score": rec["collaborative_score"],
                "explanation": f"Recommended because you liked {', '.join(top_genres[:2])} movies.",
            })
    return enriched


@router.get("/dashboard")
def dashboard_data(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    total_movies = db.query(Movie).count()
    from app.models.rating import Rating
    total_ratings = db.query(Rating).count()
    user_ratings_count = db.query(Rating).filter(
        Rating.user_id == current_user.id
    ).count()

    genre_counts = {}
    movies = db.query(Movie).all()
    for m in movies:
        for g in m.genres.split("|"):
            g = g.strip()
            if g and g != "(no genres listed)":
                genre_counts[g] = genre_counts.get(g, 0) + 1
    top_genres = sorted(genre_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    user_ratings = db.query(Rating).filter(Rating.user_id == current_user.id).all()
    rated_movie_ids = [r.movie_id for r in user_ratings]
    rated_movies = db.query(Movie).filter(Movie.movieId.in_(rated_movie_ids)).all() if rated_movie_ids else []

    return {
        "total_movies": total_movies,
        "total_ratings": total_ratings,
        "user_ratings_count": user_ratings_count,
        "top_genres": [{"name": g, "count": c} for g, c in top_genres],
        "recently_rated": [
            {
                "movieId": m.movieId,
                "title": m.title,
                "genres": m.genres,
                "rating": next((r.rating for r in user_ratings if r.movie_id == m.movieId), 0),
            }
            for m in rated_movies[-5:]
        ][::-1],
    }