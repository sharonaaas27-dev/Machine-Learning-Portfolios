from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import Optional

from app.models.movie import Movie


def get_movie_by_id(db: Session, movie_id: int) -> Optional[Movie]:
    return db.query(Movie).filter(Movie.id == movie_id).first()


def get_movie_by_movieId(db: Session, movieId: int) -> Optional[Movie]:
    return db.query(Movie).filter(Movie.movieId == movieId).first()


def get_movies(
    db: Session,
    page: int = 1,
    page_size: int = 20,
    genre: Optional[str] = None,
    query: Optional[str] = None,
    year: Optional[int] = None,
):
    q = db.query(Movie)

    if query:
        q = q.filter(Movie.title.ilike(f"%{query}%"))

    if genre:
        q = q.filter(Movie.genres.ilike(f"%{genre}%"))

    if year:
        q = q.filter(Movie.release_date.ilike(f"%{year}%"))

    total = q.count()
    movies = q.order_by(Movie.rating_count.desc()).offset(
        (page - 1) * page_size
    ).limit(page_size).all()

    return movies, total


def get_movies_by_genre(db: Session, genre: str, limit: int = 50):
    return db.query(Movie).filter(
        Movie.genres.ilike(f"%{genre}%")
    ).order_by(Movie.average_rating.desc()).limit(limit).all()


def get_top_rated_movies(db: Session, limit: int = 10):
    return db.query(Movie).filter(
        Movie.rating_count > 0
    ).order_by(Movie.average_rating.desc()).limit(limit).all()


def get_trending_movies(db: Session, limit: int = 10):
    return db.query(Movie).filter(
        Movie.rating_count > 0
    ).order_by(Movie.rating_count.desc()).limit(limit).all()


def search_movies(db: Session, query: str, limit: int = 20):
    return db.query(Movie).filter(
        or_(
            Movie.title.ilike(f"%{query}%"),
            Movie.genres.ilike(f"%{query}%"),
        )
    ).limit(limit).all()