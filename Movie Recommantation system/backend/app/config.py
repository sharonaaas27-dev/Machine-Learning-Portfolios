from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./movie_recommender.db"
    SECRET_KEY: str = "a3f8b2c1d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f0"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1440
    TMDB_API_KEY: str = ""
    MOVIELENS_URL: str = "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    DATASET_DIR: str = "datasets"

    class Config:
        env_file = ".env"


settings = Settings()