from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class RatingCreate(BaseModel):
    movie_id: int
    rating: float = Field(..., ge=0.5, le=5.0)


class RatingUpdate(BaseModel):
    rating: float = Field(..., ge=0.5, le=5.0)


class RatingResponse(BaseModel):
    id: int
    user_id: int
    movie_id: int
    rating: float
    timestamp: datetime
    movie_title: Optional[str] = None
    movie_genres: Optional[str] = None
    movie_poster: Optional[str] = None

    class Config:
        from_attributes = True