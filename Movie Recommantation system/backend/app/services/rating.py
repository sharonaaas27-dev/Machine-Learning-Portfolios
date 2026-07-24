from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Optional

from app.models.rating import Rating
from app.models.movie import Movie


def create_rating(db: Session, user_id: int, movie_id: int, rating_value: float) -> Rating:
    existing = db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.movie_id == movie_id,
    ).first()
    if existing:
        existing.rating = rating_value
        db.commit()
        db.refresh(existing)
        _update_movie_rating(db, movie_id)
        return existing

    rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating_value)
    db.add(rating)
    db.commit()
    db.refresh(rating)
    _update_movie_rating(db, movie_id)
    return rating


def update_rating(db: Session, rating_id: int, user_id: int, rating_value: float) -> Optional[Rating]:
    rating = db.query(Rating).filter(
        Rating.id == rating_id,
        Rating.user_id == user_id,
    ).first()
    if not rating:
        return None
    rating.rating = rating_value
    db.commit()
    db.refresh(rating)
    _update_movie_rating(db, rating.movie_id)
    return rating


def delete_rating(db: Session, rating_id: int, user_id: int) -> bool:
    rating = db.query(Rating).filter(
        Rating.id == rating_id,
        Rating.user_id == user_id,
    ).first()
    if not rating:
        return False
    movie_id = rating.movie_id
    db.delete(rating)
    db.commit()
    _update_movie_rating(db, movie_id)
    return True


def get_user_ratings(db: Session, user_id: int):
    return db.query(Rating).filter(Rating.user_id == user_id).order_by(
        Rating.timestamp.desc()
    ).all()


def get_user_rating_for_movie(db: Session, user_id: int, movie_id: int) -> Optional[Rating]:
    return db.query(Rating).filter(
        Rating.user_id == user_id,
        Rating.movie_id == movie_id,
    ).first()


def _update_movie_rating(db: Session, movie_id: int):
    stats = db.query(
        func.avg(Rating.rating).label("avg"),
        func.count(Rating.id).label("cnt"),
    ).filter(Rating.movie_id == movie_id).first()
    movie = db.query(Movie).filter(Movie.movieId == movie_id).first()
    if movie and stats.avg is not None:
        movie.average_rating = round(float(stats.avg), 2)
        movie.rating_count = int(stats.cnt)
        db.commit()