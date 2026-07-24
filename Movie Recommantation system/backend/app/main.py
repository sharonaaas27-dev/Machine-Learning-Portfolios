from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, movies, ratings, recommendations


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    from app.ml.trainer import train_all_models
    try:
        train_all_models()
    except Exception as e:
        print(f"Model training skipped: {e}")
    yield


app = FastAPI(
    title="Movie Recommendation System API",
    description="Content-Based & Collaborative Filtering Movie Recommendations",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(recommendations.router)


@app.get("/")
def root():
    return {"message": "Movie Recommendation System API", "version": "1.0.0"}


@app.get("/health")
def health():
    return {"status": "healthy"}