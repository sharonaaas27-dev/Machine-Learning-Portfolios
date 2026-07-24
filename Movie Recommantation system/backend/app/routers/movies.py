from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional

from app.database import get_db
from app.services.movie import (
    get_movies,
    get_movie_by_id,
    get_movies_by_genre,
    get_top_rated_movies,
    get_trending_movies,
    search_movies,
)
from app.schemas.movie import MovieResponse, MovieListResponse

router = APIRouter(tags=["Movies"])


@router.get("/movies", response_model=MovieListResponse)
def list_movies(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    genre: Optional[str] = None,
    year: Optional[int] = None,
    db: Session = Depends(get_db),
):
    movies, total = get_movies(db, page=page, page_size=page_size, genre=genre, year=year)
    return MovieListResponse(
        movies=[MovieResponse.model_validate(m) for m in movies],
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/movies/search", response_model=list[MovieResponse])
def search(
    q: str = Query("", min_length=1),
    db: Session = Depends(get_db),
):
    movies = search_movies(db, q)
    return [MovieResponse.model_validate(m) for m in movies]


@router.get("/movies/genre/{genre}", response_model=list[MovieResponse])
def by_genre(genre: str, limit: int = Query(50, ge=1), db: Session = Depends(get_db)):
    movies = get_movies_by_genre(db, genre, limit)
    return [MovieResponse.model_validate(m) for m in movies]


@router.get("/movies/top-rated", response_model=list[MovieResponse])
def top_rated(limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    movies = get_top_rated_movies(db, limit)
    return [MovieResponse.model_validate(m) for m in movies]


@router.get("/movies/trending", response_model=list[MovieResponse])
def trending(limit: int = Query(10, ge=1), db: Session = Depends(get_db)):
    movies = get_trending_movies(db, limit)
    return [MovieResponse.model_validate(m) for m in movies]


@router.get("/movies/{movie_id}", response_model=MovieResponse)
def movie_detail(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie_by_id(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return MovieResponse.model_validate(movie)