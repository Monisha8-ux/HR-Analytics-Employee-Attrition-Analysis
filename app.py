import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("HR Analytics - Employee Attrition Analysis")

# Load dataset
df = pd.read_csv("HR_Analytics.csv")

st.subheader("Dataset Overview")
st.write(df.head())

# Attrition count
st.subheader("Attrition Distribution")

attrition_count = df['Attrition'].value_counts()

fig, ax = plt.subplots()
ax.pie(attrition_count, labels=attrition_count.index, autopct='%1.1f%%')
st.pyplot(fig)

# Department analysis
st.subheader("Attrition by Department")

dept_attrition = df.groupby("Department")["Attrition"].value_counts().unstack()

fig2, ax2 = plt.subplots()
dept_attrition.plot(kind='bar', ax=ax2)
st.pyplot(fig2)