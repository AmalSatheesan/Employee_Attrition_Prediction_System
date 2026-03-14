# import streamlit as st
# import pandas as pd
# import joblib
# import plotly.express as px

# st.set_page_config(layout="wide")

# st.title("📈 Model Insights")

# model = joblib.load("models/final_attrition_model.pkl")
# features = joblib.load("models/model_features.pkl")

# st.subheader("Top Influencing Features")

# if hasattr(model, "feature_importances_"):

#     importance = pd.DataFrame({
#         "Feature": features,
#         "Importance": model.feature_importances_
#     })

#     importance = importance.sort_values(
#         by="Importance",
#         ascending=False
#     ).head(10)

#     fig = px.bar(
#         importance,
#         x="Importance",
#         y="Feature",
#         orientation="h",
#         title="Feature Importance"
#     )

#     st.plotly_chart(fig, use_container_width=True)

# st.divider()

# st.subheader("Model Interpretation")

# st.info(
# """
# The Random Forest model identifies the most important factors contributing
# to employee attrition.

# Key drivers typically include:

# • Monthly Income  
# • Distance from Home  
# • Company Tenure  
# • Job Satisfaction  
# • Work-Life Balance  

# These insights can help HR teams design better employee retention strategies.
# """
# )