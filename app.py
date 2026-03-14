import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="HR Attrition Prediction", layout="centered")

st.title("📊 HR Attrition Prediction System")
st.write("Predict whether an employee is likely to leave the company.")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Load scaler
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Load feature columns
with open("columns.pkl", "rb") as f:
    feature_columns = pickle.load(f)

st.subheader("Employee Details")

satisfactoryLevel = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)

lastEvaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.6)

numberOfProjects = st.number_input("Number of Projects", 1, 10, 3)

avgMonthlyHours = st.number_input("Average Monthly Hours", 50, 400, 200)

timeSpent_company = st.number_input("Years at Company", 1, 20, 3)

workAccident = st.selectbox("Work Accident", [0, 1])

promotionInLast5years = st.selectbox("Promotion in Last 5 Years", [0, 1])

dept = st.selectbox(
    "Department",
    ["sales","technical","support","IT","product_mng","marketing","RandD","accounting","hr","management"]
)

salary = st.selectbox("Salary Level", ["low","medium","high"])

if st.button("Predict Attrition"):

    input_data = {
        "satisfactoryLevel": satisfactoryLevel,
        "lastEvaluation": lastEvaluation,
        "numberOfProjects": numberOfProjects,
        "avgMonthlyHours": avgMonthlyHours,
        "timeSpent.company": timeSpent_company,
        "workAccident": workAccident,
        "promotionInLast5years": promotionInLast5years,
        "dept": dept,
        "salary": salary
    }

    input_df = pd.DataFrame([input_data])

    # Apply same encoding used during training
    input_df = pd.get_dummies(input_df)

    # Align columns with training data
    input_df = input_df.reindex(columns=feature_columns, fill_value=0)

    # Scale input
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Employee Attrition")
        st.write("This employee is likely to leave the company.")
    else:
        st.success("✅ Low Risk of Attrition")
        st.write("This employee is likely to stay in the company.")

st.write("---")
st.caption("HR Attrition Prediction App | Built using Python, Scikit-learn, and Streamlit")