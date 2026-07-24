from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.models.movie import Movie
from app.services.auth import get_current_user
from app.services.rating import create_rating, update_rating, delete_rating, get_user_ratings
from app.schemas.rating import RatingCreate, RatingUpdate, RatingResponse

router = APIRouter(tags=["Ratings"])


@router.post("/ratings", response_model=RatingResponse, status_code=201)
def rate_movie(
    payload: RatingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    movie = db.query(Movie).filter(Movie.movieId == payload.movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    rating = create_rating(db, current_user.id, payload.movie_id, payload.rating)
    return RatingResponse(
        id=rating.id,
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        rating=rating.rating,
        timestamp=rating.timestamp,
        movie_title=movie.title,
        movie_genres=movie.genres,
        movie_poster=movie.poster_path,
    )


@router.put("/ratings/{rating_id}", response_model=RatingResponse)
def update_user_rating(
    rating_id: int,
    payload: RatingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    rating = update_rating(db, rating_id, current_user.id, payload.rating)
    if not rating:
        raise HTTPException(status_code=404, detail="Rating not found")
    movie = db.query(Movie).filter(Movie.movieId == rating.movie_id).first()
    return RatingResponse(
        id=rating.id,
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        rating=rating.rating,
        timestamp=rating.timestamp,
        movie_title=movie.title if movie else None,
        movie_genres=movie.genres if movie else None,
        movie_poster=movie.poster_path if movie else None,
    )


@router.delete("/ratings/{rating_id}", status_code=204)
def delete_user_rating(
    rating_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = delete_rating(db, rating_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Rating not found")


@router.get("/ratings/user", response_model=list[RatingResponse])
def user_ratings(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    ratings = get_user_ratings(db, current_user.id)
    result = []
    for r in ratings:
        movie = db.query(Movie).filter(Movie.movieId == r.movie_id).first()
        result.append(RatingResponse(
            id=r.id,
            user_id=r.user_id,
            movie_id=r.movie_id,
            rating=r.rating,
            timestamp=r.timestamp,
            movie_title=movie.title if movie else None,
            movie_genres=movie.genres if movie else None,
            movie_poster=movie.poster_path if movie else None,
        ))
    return result