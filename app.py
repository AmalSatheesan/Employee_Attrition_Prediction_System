import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import plotly.express as px

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Employee Attrition Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("models/final_attrition_model.pkl")
features = joblib.load("models/model_features.pkl")

# ---------------------------
# Title Section
# ---------------------------
st.title("📊 Employee Attrition Prediction Dashboard")

st.markdown(
"""
This dashboard predicts **employee attrition risk** based on HR attributes.  
It can help HR teams **identify employees who may leave the organization**.
"""
)

st.divider()

# ---------------------------
# Employee Input Section
# ---------------------------
st.header("Employee Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider(
        "Age",
        18, 60, 30,
        help="Employee's age. Younger employees may have higher mobility."
    )

    income = st.number_input(
        "Monthly Income",
        1000, 20000, 5000,
        help="Lower salary may increase attrition risk."
    )

with col2:
    distance = st.slider(
        "Distance from Home",
        1, 50, 10,
        help="Long commute distances may increase attrition."
    )

    tenure = st.slider(
        "Company Tenure",
        0, 40, 5,
        help="Years the employee has worked in the company."
    )

with col3:
    promotions = st.slider(
        "Promotions",
        0, 10, 1,
        help="Lack of career growth may lead to attrition."
    )

    dependents = st.slider(
        "Dependents",
        0, 5, 1,
        help="Employees with dependents may prefer job stability."
    )

st.divider()

# ---------------------------
# Work Conditions
# ---------------------------
st.header("Work Conditions")

col4, col5 = st.columns(2)

with col4:
    remote = st.selectbox(
        "Remote Work",
        ["Yes", "No"],
        help="Remote work flexibility can affect attrition."
    )

with col5:
    overtime = st.selectbox(
        "Overtime",
        ["Yes", "No"],
        help="Frequent overtime may cause burnout."
    )

# ---------------------------
# Prepare Input Data
# ---------------------------
def prepare_input():

    data = {
        "Age": age,
        "Monthly_Income": income,
        "Distance_from_Home": distance,
        "Company_Tenure": tenure,
        "Number_of_Promotions": promotions,
        "Number_of_Dependents": dependents,
        "Remote_Work_Yes": 1 if remote == "Yes" else 0,
        "Overtime_Yes": 1 if overtime == "Yes" else 0
    }

    df = pd.DataFrame([data])

    for col in features:
        if col not in df.columns:
            df[col] = 0

    df = df[features]

    return df


# ---------------------------
# Prediction Section
# ---------------------------
st.divider()

if st.button("🔍 Predict Attrition Risk"):

    input_df = prepare_input()

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    colA, colB = st.columns([1,1])

    # ---------------------------
    # Result Card
    # ---------------------------
    with colA:

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error("⚠️ High Risk Employee")
        else:
            st.success("✅ Employee Likely to Stay")

        st.metric(
            label="Attrition Probability",
            value=f"{probability:.2%}"
        )

        st.info(
        """
        **Risk Interpretation**

        🟢 0–40% → Low Risk  
        🟡 40–70% → Moderate Risk  
        🔴 70–100% → High Risk
        """
        )

    # ---------------------------
    # Gauge Chart
    # ---------------------------
    with colB:

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={'text': "Attrition Risk"},
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

        st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # ---------------------------
    # Employee Profile Card
    # ---------------------------
    st.subheader("Employee Profile Summary")

    profile = pd.DataFrame({
        "Attribute": [
            "Age",
            "Monthly Income",
            "Distance from Home",
            "Company Tenure",
            "Promotions",
            "Dependents",
            "Remote Work",
            "Overtime"
        ],
        "Value": [
            age,
            income,
            distance,
            tenure,
            promotions,
            dependents,
            remote,
            overtime
        ]
    })

    st.table(profile)

    # ---------------------------
    # Feature Importance Chart
    # ---------------------------
    if hasattr(model, "feature_importances_"):

        st.subheader("Key Feature Influence")

        importance = pd.DataFrame({
            "Feature": features,
            "Importance": model.feature_importances_
        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        ).head(10)

        fig2 = px.bar(
            importance,
            x="Importance",
            y="Feature",
            orientation="h",
            title="Top Influencing Features"
        )

        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("Employee Attrition Prediction System | Machine Learning Project")