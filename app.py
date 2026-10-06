import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("churn_model.pkl")

# Encoding functions
def encode_geo(geo):
    mapping = {
        "Australia": 0,
        "Japan": 1,
        "USA": 2
    }
    return mapping[geo]

def encode_gender(g):
    mapping = {
        "Female": 0,
        "Male": 1
    }
    return mapping[g]

# Page settings
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="centered"
)

# Title
st.title("📊 Customer Churn Prediction")
st.write("Fill customer details to predict whether the customer will churn.")

# Two column layout
col1, col2 = st.columns(2)

with col1:
    CreditScore = st.number_input("Credit Score", 300, 900, 600)
    Geography = st.selectbox("Geography", ["Australia", "Japan", "USA"])
    Gender = st.selectbox("Gender", ["Female", "Male"])
    Age = st.number_input("Age", 18, 100, 35)
    Tenure = st.number_input("Tenure", 0, 10, 3)

with col2:
    Balance = st.number_input("Balance", 0.0, 250000.0, 50000.0)
    NumOfProducts = st.number_input("Number of Products", 1, 4, 1)
    HasCrCard = st.selectbox("Has Credit Card", [0, 1])
    IsActiveMember = st.selectbox("Is Active Member", [0, 1])
    EstimatedSalary = st.number_input("Estimated Salary", 0.0, 200000.0, 50000.0)

st.write("")

# Predict button
if st.button("🔍 Predict Churn"):

    geo = encode_geo(Geography)
    gender = encode_gender(Gender)

    features = np.array([[CreditScore,
                          geo,
                          gender,
                          Age,
                          Tenure,
                          Balance,
                          NumOfProducts,
                          HasCrCard,
                          IsActiveMember,
                          EstimatedSalary]])

    prediction = model.predict(features)

    try:
        probability = model.predict_proba(features)[0][1]
    except:
        probability = None

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠️ Customer will EXIT (Churn)")
    else:
        st.success("✅ Customer will STAY")

    if probability is not None:
        st.write(f"**Churn Probability:** {probability:.2f}")