from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db, SessionLocal, engine, Base

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json()["message"] == "Movie Recommendation System API"


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "healthy"


def test_register_login():
    resp = client.post("/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
    })
    assert resp.status_code == 201
    data = resp.json()
    assert "access_token" in data
    assert data["user"]["username"] == "testuser"

    resp = client.post("/login", json={
        "username": "testuser",
        "password": "testpass123",
    })
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data


def test_movies():
    resp = client.get("/movies?page=1&page_size=5")
    assert resp.status_code == 200
    data = resp.json()
    assert "movies" in data
    assert "total" in data


def test_movie_search():
    resp = client.get("/movies/search?q=Toy")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, list)


def test_top_rated():
    resp = client.get("/movies/top-rated?limit=5")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) <= 5