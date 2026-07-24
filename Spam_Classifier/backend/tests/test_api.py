import pytest
from fastapi.testclient import TestClient
from ..app.main import app
from ..app.database import Base, engine, get_db
from sqlalchemy.orm import sessionmaker
from ..app.ml.predict import predict_message

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


class TestAuth:
    def test_register(self):
        response = client.post("/register", json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123",
        })
        assert response.status_code == 201
        assert response.json()["username"] == "testuser"

    def test_login(self):
        response = client.post("/login", json={
            "username": "testuser",
            "password": "testpass123",
        })
        assert response.status_code == 200
        assert "access_token" in response.json()

    def test_register_duplicate(self):
        response = client.post("/register", json={
            "username": "testuser",
            "email": "test2@example.com",
            "password": "testpass123",
        })
        assert response.status_code == 400


class TestPrediction:
    def test_predict_spam(self):
        result = predict_message("Congratulations! You won a free iPhone. Click here to claim your prize now!")
        assert result["prediction"] == "spam"
        assert result["confidence"] > 0.5

    def test_predict_ham(self):
        result = predict_message("Hey, are you coming to the party tonight?")
        assert result["prediction"] == "ham"


class TestHealth:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "healthy"
