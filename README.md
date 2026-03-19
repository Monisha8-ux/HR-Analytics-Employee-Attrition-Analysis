📊 HR Attrition Prediction System

This project is an end-to-end Machine Learning application that predicts whether an employee is likely to leave a company based on various factors such as satisfaction level, evaluation score, workload, and work conditions.

🚀 Project Overview
Employee attrition is a critical challenge for organizations. This project uses machine learning techniques to analyze employee data and predict attrition. The model is deployed using Streamlit, allowing users to input employee details and get real-time predictions.

🎯 Features

Predict employee attrition (Leave / Stay)

Interactive web interface using Streamlit

Real-time predictions

Data preprocessing and feature engineering

End-to-end ML pipeline

🧠 Machine Learning Workflow

Data Cleaning and Preprocessing

Feature Engineering

Encoding categorical variables

Train-Test Split

Feature Scaling using StandardScaler

Model Training using Logistic Regression

Model Evaluation

🛠️ Tech Stack
Python, Pandas, NumPy, Scikit-learn, Streamlit

📂 Project Structure
app.py – Streamlit web app
model.pkl – Trained machine learning model
scaler.pkl – Feature scaling object
columns.pkl – Feature columns used during training
employee.csv – Dataset
requirements.txt – Dependencies
train_model.py – Model training script

▶️ How to Run Locally

Clone the repository

Install dependencies using pip install -r requirements.txt

Run the app using streamlit run app.py

Open in browser at http://localhost:8501

🌐 Live Demo
Add your Streamlit app link here
https://hr-analytics-employee-attrition-analysis-tzbdmmuan7bezf3kv7t3w.streamlit.app/

📊 Model Details
Algorithm used: Logistic Regression
The model takes multiple employee-related features and predicts whether the employee is likely to leave or stay.

📈 Results

High accuracy in predicting employee attrition

Balanced precision and recall

Works effectively for real-time predictions

💡 Future Improvements

Use advanced models like Random Forest or XGBoost

Improve UI/UX of the application

Add data visualization dashboard

Deploy using Docker or cloud platforms

👩‍💻 Author
Monisha Sharma
Computer Science and Data Science Student

⭐ If you like this project
Give it a star on GitHub
