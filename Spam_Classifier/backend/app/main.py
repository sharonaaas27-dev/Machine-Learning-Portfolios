from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth, prediction, model
from .ml.model_loader import is_model_trained
from .ml.train import train_model
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Spam Classifier API",
    description="AI-powered spam detection system",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(prediction.router)
app.include_router(model.router)


@app.on_event("startup")
def startup_event():
    model_path = "models/spam_classifier.pkl"
    vec_path = "models/vectorizer.pkl"
    if not os.path.exists(model_path) or not os.path.exists(vec_path):
        print("No trained model found. Training model on startup...")
        try:
            train_model()
        except Exception as e:
            print(f"Warning: Could not train model on startup: {e}")
            print("You can train the model by calling POST /retrain later.")


@app.get("/")
def root():
    return {
        "message": "Spam Classifier API",
        "version": "1.0.0",
        "docs": "/docs",
    }
