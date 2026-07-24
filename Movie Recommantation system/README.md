# Movie Recommendation System

An intelligent movie recommendation web application that suggests movies using content-based filtering, collaborative filtering, and a hybrid approach.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Frontend (React + Vite)              │
│                    TailwindCSS + Chart.js                │
└────────────────────────┬────────────────────────────────┘
                         │ HTTP / REST
┌────────────────────────▼────────────────────────────────┐
│                Backend (FastAPI + Python)                 │
│   ┌──────────┐  ┌──────────┐  ┌──────────────────────┐  │
│   │  Auth    │  │  Movies  │  │  Recommendations     │  │
│   │  JWT     │  │  CRUD    │  │  Content/Collab/Hybrid│  │
│   └──────────┘  └──────────┘  └──────────────────────┘  │
│   ┌──────────────────────────────────────────────────┐   │
│   │           ML Pipeline (Scikit-Learn, Surprise)    │   │
│   │   TF-IDF · SVD · Cosine Similarity · Hybrid      │   │
│   └──────────────────────────────────────────────────┘   │
└────────────────────────┬────────────────────────────────┘
                         │
┌────────────────────────▼────────────────────────────────┐
│                    SQLite Database                        │
│              Users · Movies · Ratings                    │
└─────────────────────────────────────────────────────────┘
```

## Features

- **Content-Based Filtering**: TF-IDF on genres, cosine similarity for similar movies
- **Collaborative Filtering**: Surprise SVD algorithm trained on user ratings
- **Hybrid Recommendations**: Weighted combination of content + collaborative scores
- **User Authentication**: JWT-based register/login with bcrypt password hashing
- **Movie Browsing**: Search, filter by genre, pagination
- **User Ratings**: Rate, update, and delete movie ratings
- **Dashboard**: Stats, genre distribution chart, top-rated & trending movies
- **Dark Netflix-Inspired UI**: Responsive, animated cards, loading skeletons

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React, TypeScript, Vite, TailwindCSS, React Query, Chart.js |
| Backend | FastAPI, Python 3.12, SQLAlchemy, Pydantic, JWT |
| ML | Scikit-Learn, Surprise, Pandas, NumPy, SciPy |
| Database | SQLite |
| Deployment | Docker, Docker Compose, GitHub Actions |

## Dataset

Uses the [MovieLens Latest Small Dataset](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip) (100,000 ratings, 9,000 movies). Automatically downloaded on first run.

## Installation

### Prerequisites

- Python 3.12+
- Node.js 20+
- npm

### Local Development

**Backend**

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:3000` with the API proxied to `http://localhost:8000`.

### Docker Setup

```bash
docker compose up --build
```

Access the app at `http://localhost`.

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive Swagger docs.

## Project Structure

```
movie-recommendation-system/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── config.py            # Settings & env vars
│   │   ├── database.py          # SQLAlchemy setup
│   │   ├── models/              # SQLAlchemy models
│   │   ├── schemas/             # Pydantic schemas
│   │   ├── routers/             # API endpoints
│   │   ├── services/            # Business logic
│   │   └── ml/                  # ML pipeline
│   │       ├── content_based.py # TF-IDF + cosine similarity
│   │       ├── collaborative.py # Surprise SVD
│   │       ├── hybrid.py        # Weighted combination
│   │       ├── trainer.py       # Model training
│   │       ├── predict.py       # Prediction cache
│   │       └── evaluation.py    # Model evaluation
│   ├── datasets/                # MovieLens data (auto-downloaded)
│   ├── models/                  # Trained model pickles
│   └── tests/
├── frontend/
│   ├── src/
│   │   ├── components/          # Reusable UI components
│   │   ├── pages/               # Route pages
│   │   ├── hooks/               # React Query hooks
│   │   ├── services/            # API client layer
│   │   ├── context/             # Auth context
│   │   └── types/               # TypeScript types
│   └── Dockerfile
├── docker-compose.yml
├── .github/workflows/ci.yml
└── README.md
```

## Screenshots

*Coming soon*

## Future Improvements

- TMDB API integration for movie posters
- Watchlist / Favorites functionality
- Genre analytics page
- Cold-start recommendations for new users
- Redis caching for recommendations
- PostgreSQL support for production
- Unit test coverage expansion
- OAuth social login
- Recommendation explanation detail page