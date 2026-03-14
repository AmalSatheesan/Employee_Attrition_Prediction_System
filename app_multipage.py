import streamlit as st

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HR Analytics Dashboard")

st.markdown(
"""
Welcome to the **Employee Attrition Analytics System**.

This dashboard helps HR teams:

• Predict employee attrition risk  
• Identify key drivers of employee turnover  
• Support proactive retention strategies
"""
)

st.divider()

col1, col2, col3 = st.columns(3)

col1.metric("Dataset Size", "74,000+")
col2.metric("Model Accuracy", "75%")
col3.metric("Attrition Recall", "0.75")

st.divider()

st.subheader("Dashboard Sections")

st.markdown(
"""
### 1️⃣ Attrition Prediction
Predict whether an employee is likely to leave the organization.

### 2️⃣ Model Insights
Understand which factors influence attrition risk.

### 3️⃣ HR Analytics Dashboard
Use insights to guide employee retention strategies.
"""
)

st.info(
"""
Use the navigation menu on the **left sidebar** to explore the dashboard.
"""
)

st.markdown("---")
st.caption("Employee Attrition Prediction System | HR Analytics Dashboard")