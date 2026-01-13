import streamlit as st
import pandas as pd
import joblib

# Load model and features
model = joblib.load("models/final_attrition_model.pkl")
features = joblib.load("models/model_features.pkl")

st.set_page_config(page_title="Employee Attrition Predictor", layout="centered")

st.title("Employee Attrition Prediction System")
st.write("Predict whether an employee is likely to leave the organization.")

st.sidebar.header("Employee Details")

def user_input():
    age = st.sidebar.slider("Age", 18, 60, 30)
    monthly_income = st.sidebar.number_input("Monthly Income", 1000, 20000, 5000)
    distance = st.sidebar.slider("Distance from Home", 1, 50, 10)
    tenure = st.sidebar.slider("Company Tenure (Years)", 0, 40, 5)
    promotions = st.sidebar.slider("Number of Promotions", 0, 10, 1)
    dependents = st.sidebar.slider("Number of Dependents", 0, 5, 1)
    remote = st.sidebar.selectbox("Remote Work", ["Yes", "No"])
    overtime = st.sidebar.selectbox("Overtime", ["Yes", "No"])

    data = {
        "Age": age,
        "Monthly_Income": monthly_income,
        "Distance_from_Home": distance,
        "Company_Tenure": tenure,
        "Number_of_Promotions": promotions,
        "Number_of_Dependents": dependents,
        "Remote_Work_Yes": 1 if remote == "Yes" else 0,
        "Overtime_Yes": 1 if overtime == "Yes" else 0,
    }

    df = pd.DataFrame([data])

    # Add missing columns
    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df[features]
    return df

input_df = user_input()

if st.button("Predict Attrition"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Employee likely to leave (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Employee likely to stay (Probability: {1 - probability:.2f})")
