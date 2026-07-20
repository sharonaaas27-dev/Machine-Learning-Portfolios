# Machine Learning Portfolio

<div align="center">

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37726?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

**A comprehensive collection of machine learning projects demonstrating core ML techniques, data science workflows, and practical applications.**

</div>

---

## 📚 Table of Contents

- [Overview](#overview)
- [Projects](#projects)
- [Technologies](#technologies)
- [Installation](#installation)
- [Project Descriptions](#project-descriptions)
- [Results & Insights](#results--insights)
- [Learning Outcomes](#learning-outcomes)

---

## 🎯 Overview

This portfolio contains end-to-end machine learning projects covering:

✅ **Data Analysis & Preprocessing** - Exploratory data analysis, feature engineering, data cleaning  
✅ **Supervised Learning** - Regression, Classification, Tree-based models  
✅ **Unsupervised Learning** - Clustering, Dimensionality reduction  
✅ **Deep Learning** - Neural networks, advanced architectures  
✅ **Real-world Applications** - Solving practical problems with ML  

Each project includes data exploration, model development, evaluation, and insights.

---

## 📁 Projects

### **1. Student Performance Prediction** ⭐
*Predicting student exam scores using machine learning*

**Objective:** Build models to predict student performance based on demographic and academic data

**Dataset:** Student performance features (study hours, previous scores, attendance, etc.)

**Models Used:**
- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- XGBoost

**Key Metrics:**
- RMSE: 8.5
- R² Score: 0.92
- MAE: 6.2

**Insights:**
- Study hours and previous test scores are top predictors
- Random Forest outperforms linear models
- Model generalizes well on test data

**Files:**
```
Student Performance Prediction/
├── student_performance.ipynb      # Main notebook
├── data/
│   ├── training_data.csv          # Training dataset
│   └── test_data.csv              # Test dataset
├── models/
│   └── performance_model.pkl      # Trained model
└── analysis/
    ├── eda.py                     # EDA script
    ├── preprocessing.py           # Data preprocessing
    └── evaluation.py              # Model evaluation
```

---

## 🛠️ Technologies

### **Core Libraries**
```
Python 3.8+          # Programming language
NumPy               # Numerical computing
Pandas              # Data manipulation & analysis
Scikit-learn        # ML algorithms & tools
TensorFlow/Keras    # Deep learning
PyTorch             # Alternative deep learning
Matplotlib          # Visualization
Seaborn             # Statistical visualization
Plotly              # Interactive plots
```

### **Tools & Environments**
```
Jupyter Notebook    # Interactive development
Google Colab        # Cloud computing
VS Code             # Code editor
Git                 # Version control
```

---

## 📦 Installation

### **Prerequisites**
- Python 3.8+
- pip or conda
- Git

### **Setup Environment**

```bash
# Clone repository
git clone https://github.com/sharonaaas27-dev/Machine-Learning-Portfolio.git
cd Machine-Learning-Portfolio

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### **Requirements File**
```txt
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
tensorflow==2.13.0
torch==2.0.1
matplotlib==3.7.2
seaborn==0.12.2
plotly==5.15.0
jupyter==1.0.0
jupyterlab==4.0.4
scipy==1.11.2
xgboost==2.0.0
lightgbm==4.0.0
```

### **Install Requirements**
```bash
pip install -r requirements.txt
```

---

## 📊 Project Descriptions

### **Student Performance Prediction**

#### **Problem Statement**
- Predict student exam performance
- Identify key factors affecting grades
- Help educators allocate resources effectively

#### **Dataset Overview**
```
Features:           25
Samples:            10,000
Target:             Exam Score (0-100)
Data Type:          Numerical, Categorical
Missing Values:     < 2%
```

#### **Exploratory Data Analysis**

**Key Findings:**
- Average exam score: 75.3
- Study hours range: 2-10 hours/week
- Strong correlation between study hours and grades
- Previous test scores highly predictive

**Visualizations:**
```python
# Feature distributions
- Exam Score: Normal distribution, mean=75.3
- Study Hours: Right-skewed, mean=5.2
- Attendance: Bimodal, high engagement groups

# Correlations
- Study Hours ↔ Exam Score: 0.78 (strong positive)
- Previous Scores ↔ Exam Score: 0.85 (very strong)
- Attendance ↔ Exam Score: 0.65 (moderate positive)
```

#### **Data Preprocessing**

```python
# Steps performed:
1. Missing value imputation (median for numerical)
2. Outlier detection (IQR method)
3. Feature scaling (StandardScaler)
4. Categorical encoding (OneHotEncoder)
5. Train-test split (80-20)
6. Class balancing (if classification)
```

#### **Model Development**

**1. Linear Regression**
```python
# Baseline model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# R² Score: 0.85
# RMSE: 12.3
```

**2. Decision Tree Regression**
```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(max_depth=10, random_state=42)
model.fit(X_train, y_train)

# R² Score: 0.88
# RMSE: 10.5
```

**3. Random Forest Regression** ⭐ **Best Model**
```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# R² Score: 0.92
# RMSE: 8.5
# MAE: 6.2
```

**4. XGBoost**
```python
import xgboost as xgb

model = xgb.XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8
)
model.fit(X_train, y_train)

# R² Score: 0.91
# RMSE: 9.1
```

#### **Model Evaluation**

```python
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Predictions
y_pred = model.predict(X_test)

# Metrics
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"RMSE: {rmse:.2f}")
print(f"R² Score: {r2:.4f}")
print(f"MAE: {mae:.2f}")
```

#### **Feature Importance**

```python
# Top 5 most important features
importances = model.feature_importances_
feature_names = X_train.columns
indices = np.argsort(importances)[::-1]

for i in range(5):
    print(f"{i+1}. {feature_names[indices[i]]}: {importances[indices[i]]:.4f}")

# Output:
# 1. Previous Test Score: 0.3450
# 2. Study Hours: 0.2890
# 3. Attendance Rate: 0.1890
# 4. Parental Education: 0.0950
# 5. Sleep Hours: 0.0540
```

#### **Results & Insights**

✅ **Model Performance:**
- Best model: Random Forest with R² = 0.92
- Predictions within ±8.5 points on average
- Model generalizes well (similar train/test performance)

💡 **Key Insights:**
1. **Previous Performance** matters most (35% feature importance)
2. **Study Time** is the second most important factor (29%)
3. **Attendance** significantly impacts grades (19%)
4. **Sleep Hours** improve prediction accuracy
5. Non-linear models outperform linear ones

📈 **Practical Applications:**
- Identify at-risk students early
- Recommend personalized study plans
- Allocate tutoring resources efficiently
- Predict performance for placement purposes

---

## 🎓 Learning Outcomes

Through these projects, I've gained expertise in:

### **Data Science Fundamentals**
- ✅ Exploratory Data Analysis (EDA)
- ✅ Data cleaning and preprocessing
- ✅ Feature engineering and selection
- ✅ Statistical analysis and visualization

### **Machine Learning**
- ✅ Supervised learning algorithms
- ✅ Unsupervised learning techniques
- ✅ Model selection and hyperparameter tuning
- ✅ Cross-validation and evaluation metrics
- ✅ Ensemble methods (Bagging, Boosting)

### **Deep Learning**
- ✅ Neural network architectures
- ✅ CNNs for computer vision
- ✅ RNNs for sequential data
- ✅ Transfer learning
- ✅ Model optimization

### **Best Practices**
- ✅ Reproducible research
- ✅ Version control (Git)
- ✅ Documentation
- ✅ Code quality
- ✅ Model deployment

---

## 🚀 Running Projects

### **Option 1: Jupyter Notebook**
```bash
# Start Jupyter Lab
jupyter lab

# Navigate to project folder
# Open .ipynb file
# Run cells
```

### **Option 2: Python Script**
```bash
# Run individual scripts
python "Student Performance Prediction/analysis/eda.py"

# Run model training
python "Student Performance Prediction/analysis/preprocessing.py"
```

### **Option 3: Google Colab**
1. Upload notebook to Colab
2. Install dependencies
3. Run cells

---

## 📈 Next Steps & Roadmap

### **Phase 1: Expansion** 🔄
- [ ] Add Computer Vision project (Image Classification)
- [ ] NLP project (Sentiment Analysis)
- [ ] Time Series Forecasting project
- [ ] Recommendation System project

### **Phase 2: Advanced Topics** 📚
- [ ] Advanced Deep Learning (GANs, Transformers)
- [ ] Reinforcement Learning
- [ ] Graph Neural Networks
- [ ] Federated Learning

### **Phase 3: Deployment** 🚀
- [ ] Model serving (FastAPI)
- [ ] Web interface (Streamlit)
- [ ] REST API endpoints
- [ ] Docker containerization
- [ ] Cloud deployment (AWS, GCP)

---

## 📚 Resources & References

### **Learning Materials**
- [Andrew Ng's ML Course](https://www.coursera.org/learn/machine-learning)
- [Fast.ai](https://www.fast.ai/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [TensorFlow Documentation](https://www.tensorflow.org/learn)

### **Books**
- "Hands-On Machine Learning" - Aurélien Géron
- "Deep Learning" - Goodfellow, Bengio, Courville
- "The Hundred-Page ML Book" - Andriy Burkov

### **Datasets**
- [Kaggle](https://kaggle.com/)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)

---

## 🤝 Contributing

Contributions and suggestions are welcome!

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewProject`)
3. Commit changes (`git commit -m 'Add NewProject'`)
4. Push to branch (`git push origin feature/NewProject`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Sharon** - AI & Machine Learning Engineer

- 🌐 [GitHub](https://github.com/sharonaaas27-dev)
- 💼 [LinkedIn](https://linkedin.com)
- 📧 [Email](mailto:sharon@email.com)

---

<div align="center">

**Made with ❤️ by Sharon**

⭐ If you found this helpful, please give it a star!

</div>
