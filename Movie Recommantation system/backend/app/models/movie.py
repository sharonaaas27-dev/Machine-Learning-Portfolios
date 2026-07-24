from sqlalchemy import Column, Integer, String, Float, DateTime, func

from app.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, autoincrement=True)
    movieId = Column(Integer, unique=True, index=True, nullable=False)
    title = Column(String(255), nullable=False)
    genres = Column(String(500), nullable=False)
    poster_path = Column(String(500), default="")
    overview = Column(String(2000), default="")
    release_date = Column(String(20), default="")
    average_rating = Column(Float, default=0.0)
    rating_count = Column(Integer, default=0)
    created_at = Column(DateTime, server_default=func.now())