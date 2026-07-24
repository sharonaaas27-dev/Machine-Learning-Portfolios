from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class MovieResponse(BaseModel):
    id: int
    movieId: int
    title: str
    genres: str
    poster_path: str
    overview: str
    release_date: str
    average_rating: float
    rating_count: int

    class Config:
        from_attributes = True


class MovieListResponse(BaseModel):
    movies: list[MovieResponse]
    total: int
    page: int
    page_size: int


class MovieSearchParams(BaseModel):
    query: str = ""
    genre: Optional[str] = None
    year: Optional[int] = None
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=20, ge=1, le=100)