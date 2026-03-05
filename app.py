import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Load Model and Feature List
# -----------------------------
model = joblib.load("models/final_attrition_model.pkl")
features = joblib.load("models/model_features.pkl")

# -----------------------------
# Title Section
# -----------------------------
st.title("📊 Employee Attrition Prediction System")

st.markdown(
"""
This tool predicts whether an employee is **likely to leave the organization**
based on HR attributes.

Adjust the parameters below and click **Predict Attrition**.
"""
)

st.divider()

# -----------------------------
# Input Section
# -----------------------------
st.header("Employee Details")

col1, col2 = st.columns(2)

with col1:
    age = st.slider(
        "Age",
        18,
        60,
        30,
        help="Employee's age. Younger employees may change jobs more frequently."
    )

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=20000,
        value=5000,
        help="Employee monthly salary. Lower income may correlate with attrition risk."
    )

    distance = st.slider(
        "Distance from Home",
        1,
        50,
        10,
        help="Distance between home and workplace (km). Long commute may increase attrition."
    )

with col2:
    tenure = st.slider(
        "Company Tenure",
        0,
        40,
        5,
        help="Total years the employee has worked at the company."
    )

    promotions = st.slider(
        "Number of Promotions",
        0,
        10,
        1,
        help="Total promotions received. Lack of growth may increase attrition risk."
    )

    dependents = st.slider(
        "Number of Dependents",
        0,
        5,
        1,
        help="Employees with dependents may prefer job stability."
    )

st.divider()

# -----------------------------
# Work Conditions
# -----------------------------
st.header("Work Conditions")

col3, col4 = st.columns(2)

with col3:
    remote = st.selectbox(
        "Remote Work",
        ["Yes", "No"],
        help="Whether the employee works remotely."
    )

with col4:
    overtime = st.selectbox(
        "Overtime",
        ["Yes", "No"],
        help="Frequent overtime may lead to employee burnout."
    )

st.divider()

# -----------------------------
# Prepare Input Data
# -----------------------------
def prepare_input():

    data = {
        "Age": age,
        "Monthly_Income": monthly_income,
        "Distance_from_Home": distance,
        "Company_Tenure": tenure,
        "Number_of_Promotions": promotions,
        "Number_of_Dependents": dependents,
        "Remote_Work_Yes": 1 if remote == "Yes" else 0,
        "Overtime_Yes": 1 if overtime == "Yes" else 0
    }

    df = pd.DataFrame([data])

    # Add missing columns
    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df[features]

    return df


# -----------------------------
# Prediction Button
# -----------------------------
if st.button("🔍 Predict Attrition"):

    input_df = prepare_input()

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk: Employee likely to leave")
    else:
        st.success("✅ Low Risk: Employee likely to stay")

    st.write(f"**Attrition Probability:** {probability:.2%}")

    # -----------------------------
    # Risk Gauge Chart
    # -----------------------------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Attrition Risk (%)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "red"},
            'steps': [
                {'range': [0, 40], 'color': "lightgreen"},
                {'range': [40, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "lightcoral"}
            ],
        }
    ))

    st.plotly_chart(fig)

    st.divider()

    st.info(
        """
        **Interpretation**

        - **0–40%** → Low attrition risk  
        - **40–70%** → Moderate risk  
        - **70–100%** → High attrition risk
        """
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Employee Attrition Prediction System | Machine Learning Project")