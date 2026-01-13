# Employee Attrition Prediction System

## 📌 Project Overview
This project predicts whether an employee is likely to leave an organization using machine learning techniques.

## 🎯 Objective
To help HR teams proactively identify employees at risk of attrition and take retention actions.

## 📊 Dataset
- Source: Kaggle Employee Attrition Dataset
- Size: ~74,000 records
- Target Variable: Attrition (Stayed / Left)

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn, Imbalanced-learn
- Streamlit
- Joblib

## 🔍 Methodology
- Exploratory Data Analysis (EDA)
- Feature selection using Chi-Square and Random Forest importance
- Class imbalance handling using SMOTE
- Model comparison (Logistic Regression vs Random Forest)
- Hyperparameter tuning using GridSearchCV

## 📈 Model Performance
- Accuracy: ~75%
- Recall (Attrition): ~0.75

## 🚀 Streamlit Application
The app allows users to input employee details and predicts attrition probability.

## ▶️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
