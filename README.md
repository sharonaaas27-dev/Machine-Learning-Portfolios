# 🤖 Machine Learning Portfolios

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)

**A professional collection of machine learning projects showcasing data science, deep learning, NLP, and production-ready applications.**

[View Projects](#-projects) • [Quick Start](#-quick-start) • [Technologies](#-technologies) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Projects](#-projects)
- [Technologies](#-technologies)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Learning Outcomes](#-learning-outcomes)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)

---

## 🎯 Overview

This portfolio demonstrates expertise in **end-to-end machine learning workflows**, from data analysis to production deployment. It covers:

✅ **Data Science** - EDA, feature engineering, data preprocessing  
✅ **Supervised Learning** - Classification, regression, ensemble methods  
✅ **Unsupervised Learning** - Clustering, dimensionality reduction  
✅ **NLP & Text Analysis** - Sentiment analysis, text classification, fake news detection  
✅ **Recommendation Systems** - Content-based, collaborative, and hybrid approaches  
✅ **Full-Stack ML Apps** - Web applications with frontend + backend + ML pipeline  
✅ **Deep Learning** - Neural networks, embeddings, and advanced architectures  

---

## 📁 Projects

### **1. 🎬 Movie Recommendation System** ⭐ **Production Ready**

An intelligent web application that recommends movies using multiple ML approaches.

**Key Features:**
- Content-based filtering (TF-IDF + Cosine Similarity)
- Collaborative filtering (Surprise SVD)
- Hybrid recommendations (weighted combination)
- JWT-based authentication
- Real-time dashboard with charts
- Dark Netflix-inspired UI

**Tech Stack:** React + TypeScript, FastAPI, Scikit-Learn, SQLite, Docker

**Dataset:** MovieLens 100K (9,000 movies, 100,000 ratings)

**Performance:**
- Hybrid RMSE: < 0.9
- Cold-start recommendations active
- Sub-100ms response time

📂 [View Project](Movie%20Recommantation%20system/)

---

### **2. 📰 Fake News Detection**

A classification system to identify and predict misinformation in news articles.

**Objectives:**
- Distinguish between credible and fake news
- Identify common misinformation patterns
- Feature importance analysis for interpretability

**Models Trained:**
- Logistic Regression (baseline)
- Random Forest Classifier
- Gradient Boosting (XGBoost)
- Neural Networks (Deep Learning)

**Evaluation Metrics:**
- Accuracy: ~95%
- Precision/Recall: Balanced
- Feature importance visualization

📂 [View Project](Fake%20News%20Prediction/)

---

### **3. 💬 Sentiment Analysis**

Comprehensive sentiment classification on text data (reviews, tweets, comments).

**Approaches:**
- Traditional ML (Naive Bayes, SVM)
- TF-IDF vectorization
- Word embeddings (Word2Vec, GloVe)
- LSTM neural networks
- BERT transformers

**Applications:**
- Product review sentiment
- Social media sentiment tracking
- Customer feedback analysis

📂 [View Project](Sentimental_analysis/)

---

### **4. 📧 Spam Classifier**

Email/SMS spam detection using various classification techniques.

**Models:**
- Naive Bayes (TF-IDF)
- Random Forest
- SVM with RBF kernel
- XGBoost ensemble

**Metrics:**
- Precision: >98% (minimize false positives)
- Recall: >95%
- AUC-ROC: 0.99

📂 [View Project](Spam_Classifier/)

---

### **5. 📑 Resume Screening System**

Automated resume ranking and candidate matching using NLP.

**Features:**
- Resume parsing and text extraction
- Job description matching
- Candidate ranking algorithm
- Skills extraction
- Experience level classification

**Technology:**
- spaCy for NLP
- TF-IDF similarity
- Cosine similarity ranking
- Custom scoring algorithm

📂 [View Project](Resume_Screening_System/)

---

### **6. 🏢 E-Commerce Sales Analysis Dashboard**

Business intelligence dashboard analyzing sales trends, patterns, and forecasting.

**Analysis Includes:**
- Time-series sales forecasting
- Product performance analysis
- Customer segmentation
- Revenue predictions
- Seasonal trend detection

**Tools:** Pandas, Plotly, Streamlit/Jupyter

📂 [View Project](E-Commerce%20Sales%20Analysis%20Dashboard/)

---

### **7. 🎵 Song Recommendation System**

Music recommendation engine using collaborative and content-based filtering.

**Approaches:**
- User-based collaborative filtering
- Item-based filtering
- Playlist generation
- Genre similarity matching

**Features:**
- Personalized playlists
- Discovery recommendations
- Similar artist suggestions

📂 [View Project](Song%20Recommentation%20System/)

---

### **8. 📰 Multi-Class News Classification**

Classify news articles into multiple categories using deep learning.

**Categories:** Politics, Sports, Technology, Business, Entertainment, etc.

**Models:**
- Traditional classifiers (NB, SVM, RF)
- Neural networks with embeddings
- CNN for text
- LSTM architectures
- Transfer learning with BERT

**Performance:** Multi-class accuracy ~92%

📂 [View Project](Multi-Class%20News%20Classification/)

---

## 🛠️ Technologies

### **Programming & Data Science**
```
Python 3.8+          Core language
NumPy               Numerical computing
Pandas              Data manipulation
SciPy               Scientific computing
Matplotlib          Static visualizations
Seaborn             Statistical plots
Plotly              Interactive dashboards
```

### **Machine Learning**
```
Scikit-Learn        Classical ML algorithms
XGBoost             Gradient boosting
LightGBM            Fast boosting
Surprise            Recommendation systems
```

### **Deep Learning**
```
TensorFlow/Keras    Neural networks
PyTorch             Alternative framework
```

### **NLP**
```
spaCy               Industrial NLP
NLTK                Text processing
Transformers        BERT, GPT models
TF-IDF              Text vectorization
```

### **Web Stack**
```
FastAPI             High-performance backend
React + TypeScript  Modern frontend
TailwindCSS         Styling
SQLAlchemy          ORM
SQLite              Database
```

### **DevOps & Tools**
```
Docker              Containerization
Docker Compose      Multi-container setup
Jupyter             Interactive notebooks
Git                 Version control
GitHub Actions      CI/CD pipeline
```

---

## 🚀 Quick Start

### **Prerequisites**
```bash
Python 3.8+
Node.js 20+ (for web projects)
pip / conda
Docker (optional)
```

### **Clone Repository**
```bash
git clone https://github.com/sharonaaas27-dev/Machine-Learning-Portfolios.git
cd Machine-Learning-Portfolios
```

### **Setup Python Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Run a Project (Jupyter Notebook)**
```bash
jupyter lab
# Navigate to project folder and open .ipynb file
```

### **Run Web Applications**

**Movie Recommendation System:**
```bash
# Backend
cd "Movie Recommantation system/backend"
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend (new terminal)
cd "Movie Recommantation system/frontend"
npm install
npm run dev
```

**Docker Compose:**
```bash
docker compose up --build
```

---

## 📁 Project Structure

```
Machine-Learning-Portfolios/
├── E-Commerce Sales Analysis Dashboard/
│   ├── dashboard.ipynb
│   ├── data/
│   └── analysis/
│
├── Fake News Prediction/
│   ├── fake_news_prediction.ipynb
│   ├── data/
│   ├── models/
│   └── README.md
│
├── Movie Recommendation System/        ⭐ Full-stack app
│   ├── backend/
│   │   ├── app/
│   │   │   ├── models/
│   │   │   ├── routers/
│   │   │   ├── services/
│   │   │   └── ml/
│   │   ├── requirements.txt
│   │   └── Dockerfile
│   ├── frontend/
│   │   ├── src/
│   │   ├── package.json
│   │   └── Dockerfile
│   ├── docker-compose.yml
│   └── README.md
│
├── Multi-Class News Classification/
│   ├── news_classification.ipynb
│   └── data/
│
├── Resume Screening System/
│   ├── resume_screening.ipynb
│   ├── resume_parser.py
│   └── data/
│
├── Sentimental Analysis/
│   ├── sentiment_analysis.ipynb
│   ├── models/
│   └── data/
│
├── Song Recommendation System/
│   ├── song_recommendation.ipynb
│   └── data/
│
├── Spam_Classifier/
│   ├── spam_classifier.ipynb
│   ├── models/
│   └── data/
│
├── requirements.txt
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── README.md
```

---

## 📊 Language Composition

- **TypeScript:** 44.1% (Frontend, type safety)
- **Python:** 37.1% (ML, backend logic)
- **Jupyter Notebook:** 16.2% (Interactive analysis)
- **CSS:** 1.3% (Styling)
- **JavaScript:** 0.8% (Web utilities)
- **HTML:** 0.3% (Templates)
- **Dockerfile:** 0.2% (Containerization)

---

## 🎓 Learning Outcomes

### **Data Science & Analytics**
✅ Exploratory Data Analysis (EDA)  
✅ Data cleaning and preprocessing  
✅ Statistical analysis  
✅ Feature engineering  
✅ Data visualization  

### **Machine Learning**
✅ Supervised learning (classification, regression)  
✅ Unsupervised learning (clustering)  
✅ Ensemble methods (Random Forest, Boosting)  
✅ Model selection and hyperparameter tuning  
✅ Cross-validation techniques  
✅ Feature importance analysis  

### **Deep Learning & NLP**
✅ Neural network architectures  
✅ RNNs and LSTMs  
✅ CNNs for text  
✅ Word embeddings  
✅ Transfer learning (BERT, GPT)  
✅ Transformer models  

### **Recommendation Systems**
✅ Content-based filtering  
✅ Collaborative filtering  
✅ Hybrid approaches  
✅ Matrix factorization  
✅ Evaluation metrics  

### **Software Engineering**
✅ Full-stack web development  
✅ REST API design  
✅ Database design (SQL)  
✅ Authentication (JWT)  
✅ Docker containerization  
✅ CI/CD pipelines  
✅ Code quality and testing  

---

## 🗺️ Roadmap

### **Phase 1: Project Expansion** 🔄
- [ ] Computer Vision (Image Classification)
- [ ] Time Series Forecasting
- [ ] Advanced NLP (Named Entity Recognition)
- [ ] Anomaly Detection System

### **Phase 2: Advanced Topics** 📚
- [ ] Reinforcement Learning
- [ ] Graph Neural Networks
- [ ] Federated Learning
- [ ] AutoML pipelines

### **Phase 3: Production & Deployment** 🚀
- [ ] Model serving with TorchServe/TensorFlow Serving
- [ ] REST API optimization
- [ ] PostgreSQL integration
- [ ] Redis caching
- [ ] AWS/GCP deployment
- [ ] Kubernetes orchestration
- [ ] Monitoring & logging

### **Phase 4: Documentation** 📖
- [ ] API documentation (Swagger/OpenAPI)
- [ ] Architecture diagrams
- [ ] Performance benchmarks
- [ ] Deployment guides

---

## 📚 Resources & References

### **Learning Platforms**
- [Andrew Ng's Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction)
- [Fast.ai](https://www.fast.ai/)
- [Kaggle Competitions](https://www.kaggle.com/)

### **Key Documentation**
- [Scikit-Learn](https://scikit-learn.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [PyTorch](https://pytorch.org/)
- [FastAPI](https://fastapi.tiangolo.com/)

### **Recommended Books**
- *Hands-On Machine Learning* - Aurélien Géron
- *Deep Learning* - Goodfellow, Bengio, Courville
- *The Hundred-Page ML Book* - Andriy Burkov
- *Natural Language Processing with Transformers* - Tunstall, von Rutte, Wolf

### **Datasets**
- [Kaggle](https://www.kaggle.com/datasets)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [MovieLens](https://grouplens.org/datasets/movielens/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch
   ```bash
   git checkout -b feature/YourNewProject
   ```
3. **Make** your changes
4. **Commit** with clear messages
   ```bash
   git commit -m 'Add YourNewProject with XYZ features'
   ```
5. **Push** to your branch
   ```bash
   git push origin feature/YourNewProject
   ```
6. **Open** a Pull Request with a detailed description

### **Guidelines**
- Follow Python PEP 8 style guide
- Add docstrings to functions
- Include unit tests for new features
- Update documentation
- Add your project to the README

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this code for personal and commercial purposes.

---

## 👨‍💼 About Me

**Sharon** - AI & Machine Learning Engineer

Passionate about building intelligent systems and solving real-world problems with data science and machine learning.

### **Connect**
- 🌐 [GitHub](https://github.com/sharonaaas27-dev)
- 💼 [LinkedIn](https://linkedin.com/in/sharon)
- 📧 [Email](mailto:sharon@example.com)

---

## 🙏 Acknowledgments

- Thanks to the open-source ML community
- Kaggle for datasets and competitions
- MovieLens for the recommendation dataset
- All contributors and supporters

---

<div align="center">

**Made with ❤️ and ☕ by Sharon**

⭐ If you found this helpful, please give it a star!

[⬆ back to top](#-machine-learning-portfolios)

</div>
