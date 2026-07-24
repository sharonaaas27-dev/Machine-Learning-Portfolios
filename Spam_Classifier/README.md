# SpamGuard - AI-Powered Spam Classification System

A production-ready, AI-powered web application for classifying SMS and email messages as Spam or Ham (not spam). Built with FastAPI, React, and Scikit-learn.

## Architecture

```
spam-classifier/
├── backend/              # FastAPI Python backend
│   ├── app/
│   │   ├── ml/          # Machine learning pipeline
│   │   ├── models/      # SQLAlchemy database models
│   │   ├── routers/     # API endpoints
│   │   ├── schemas/     # Pydantic request/response schemas
│   │   └── utils/       # Security & auth utilities
│   └── tests/           # Pytest test suite
├── frontend/             # React + Vite + TypeScript
│   └── src/
│       ├── components/  # Reusable UI components
│       ├── pages/       # Application pages
│       ├── hooks/       # React Query hooks
│       ├── services/    # API client (Axios)
│       ├── context/     # Auth context provider
│       └── types/       # TypeScript interfaces
├── docker/               # Docker configuration
├── models/               # Trained model storage
└── datasets/             # Dataset storage
```

## Features

### Authentication
- User registration and login
- JWT-based authentication
- Protected routes and API endpoints

### Spam Detection
- Real-time message classification
- Confidence score and probability breakdown
- Explainable AI with keyword analysis
- Batch prediction support

### Dashboard & Analytics
- Prediction statistics (total, spam, ham counts)
- Model accuracy and performance metrics
- Interactive charts (distribution, confusion matrix, model comparison)
- Cross-validation scores

### Prediction History
- Searchable prediction history
- Export predictions as JSON
- Paginated results
- Delete individual predictions

### Model Management
- Train/retrain via API
- Automatic best model selection (Naive Bayes, Logistic Regression, SVM, Random Forest, etc.)
- Performance comparison across models
- NLTK-based text preprocessing (stemming, lemmatization, stopword removal)

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | React 18, TypeScript, Vite, Tailwind CSS, Chart.js |
| Backend | FastAPI, Python 3.12, SQLAlchemy, Pydantic |
| ML | Scikit-learn, Pandas, NumPy, NLTK, Joblib |
| Database | SQLite |
| Auth | JWT (python-jose), bcrypt |
| Deployment | Docker, Docker Compose |

## Dataset

Uses the SMS Spam Collection dataset from UCI / Kaggle. The dataset is automatically downloaded on first run.

Format: `label,text` where label is `ham` or `spam`.

## Installation

### Prerequisites
- Python 3.12+
- Node.js 20+
- npm or yarn

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### Docker Setup

```bash
docker-compose up --build
```

## Training the Model

The model trains automatically on first startup. To manually retrain:

```bash
# Via API
curl -X POST http://localhost:8000/retrain

# Via Python
python -c "from app.ml.train import train_model; train_model()"
```

## API Documentation

Once running, visit `http://localhost:8000/docs` for interactive Swagger documentation.

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | `/register` | Register new user | No |
| POST | `/login` | Login & get JWT token | No |
| GET | `/profile` | Get current user profile | Yes |
| POST | `/predict` | Classify a single message | Yes |
| POST | `/predict/bulk` | Batch classify messages | Yes |
| GET | `/history` | Get prediction history | Yes |
| DELETE | `/history/{id}` | Delete a prediction | Yes |
| GET | `/history/export` | Export all predictions | Yes |
| GET | `/metrics` | Get model metrics | No |
| POST | `/retrain` | Retrain the model | No |
| GET | `/health` | Health check | No |
| GET | `/model/info` | Get model information | No |

## Running Tests

```bash
cd backend
pytest tests/ -v
```

## Environment Variables

Create a `.env` file in the project root:

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./spam_classifier.db
MODEL_PATH=models/spam_classifier.pkl
VECTORIZER_PATH=models/vectorizer.pkl
METRICS_PATH=models/metrics.json
DATASET_PATH=datasets/sms_spam.csv
```

## ML Pipeline

1. **Data Loading** - Downloads SMS Spam Collection dataset
2. **Preprocessing** - Lowercase, remove punctuation/numbers/URLs/HTML, tokenization, stopword removal, stemming, lemmatization
3. **Feature Engineering** - TF-IDF vectorization with n-grams (1,2)
4. **Model Training** - Trains 6 models, selects best by accuracy
5. **Evaluation** - Accuracy, precision, recall, F1, ROC-AUC, confusion matrix, cross-validation

## Screenshots

*(Screenshots to be added)*

## Future Improvements

- Email spam detection via IMAP integration
- CSV file upload for bulk analysis
- Multi-language spam detection
- Real-time SMS filtering
- Admin dashboard with user analytics
- Model versioning and A/B testing
- WebSocket for real-time predictions
