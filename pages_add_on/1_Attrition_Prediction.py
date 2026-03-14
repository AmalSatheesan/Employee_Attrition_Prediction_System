# import streamlit as st
# import pandas as pd
# import joblib
# import plotly.graph_objects as go

# st.set_page_config(layout="wide")

# st.title("🔮 Employee Attrition Prediction")

# model = joblib.load("models/final_attrition_model.pkl")
# features = joblib.load("models/model_features.pkl")

# st.sidebar.header("Employee Inputs")

# age = st.sidebar.slider("Age", 18, 60, 30)
# income = st.sidebar.number_input("Monthly Income", 1000, 20000, 5000)
# distance = st.sidebar.slider("Distance from Home", 1, 50, 10)
# tenure = st.sidebar.slider("Company Tenure", 0, 40, 5)
# promotions = st.sidebar.slider("Promotions", 0, 10, 1)
# dependents = st.sidebar.slider("Dependents", 0, 5, 1)

# remote = st.sidebar.selectbox("Remote Work", ["Yes", "No"])
# overtime = st.sidebar.selectbox("Overtime", ["Yes", "No"])

# def prepare_input():

#     data = {
#         "Age": age,
#         "Monthly_Income": income,
#         "Distance_from_Home": distance,
#         "Company_Tenure": tenure,
#         "Number_of_Promotions": promotions,
#         "Number_of_Dependents": dependents,
#         "Remote_Work_Yes": 1 if remote == "Yes" else 0,
#         "Overtime_Yes": 1 if overtime == "Yes" else 0
#     }

#     df = pd.DataFrame([data])

#     for col in features:
#         if col not in df.columns:
#             df[col] = 0

#     df = df[features]

#     return df


# if st.sidebar.button("Predict"):

#     input_df = prepare_input()

#     prediction = model.predict(input_df)[0]
#     probability = model.predict_proba(input_df)[0][1]

#     col1, col2 = st.columns(2)

#     with col1:

#         if prediction == 1:
#             st.error("⚠️ High Attrition Risk")
#         else:
#             st.success("✅ Employee Likely to Stay")

#         st.metric("Attrition Probability", f"{probability:.2%}")

#     with col2:

#         fig = go.Figure(go.Indicator(
#             mode="gauge+number",
#             value=probability * 100,
#             title={'text': "Attrition Risk"},
#             gauge={
#                 'axis': {'range': [0, 100]},
#                 'bar': {'color': "red"},
#                 'steps': [
#                     {'range': [0, 40], 'color': "lightgreen"},
#                     {'range': [40, 70], 'color': "yellow"},
#                     {'range': [70, 100], 'color': "lightcoral"}
#                 ],
#             }
#         ))

#         st.plotly_chart(fig, use_container_width=True)