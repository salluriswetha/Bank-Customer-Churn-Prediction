# 🏦 Bank Customer Churn Prediction

## 📌 Project Overview

Bank Customer Churn Prediction is a machine learning-based application designed to predict whether a bank customer is likely to leave the bank or continue using its services.

The system analyzes important customer attributes such as credit score, geography, gender, age, tenure, account balance, number of products, credit card status, active membership, and estimated salary.

A trained machine learning model processes these customer details and generates a churn prediction. The application also provides the churn probability when supported by the trained model.

This project demonstrates the practical application of machine learning for customer behavior analysis and supports data-driven decision-making in the banking domain.

---

## 🎯 Project Objective

The main objective of this project is to predict customer churn and identify customers who may be at risk of leaving a bank.

Customer churn prediction can help organizations:

- Identify customers who may leave
- Understand important customer characteristics
- Support customer retention strategies
- Make data-driven business decisions
- Reduce potential customer loss

---

## 💡 Problem Statement

Customer retention is an important challenge in the banking industry.

When customers leave a bank, the organization may lose revenue and future business opportunities. Therefore, predicting which customers are more likely to churn can help banks take preventive actions.

This project uses machine learning to analyze customer information and predict whether the customer is likely to:

- ✅ Stay with the bank
- ⚠️ Leave the bank (Churn)

---

## 📊 Input Features

The trained machine learning model uses the following 10 customer attributes:

| Feature | Description |
|---|---|
| CreditScore | Customer's credit score |
| Geography | Customer's country or region |
| Gender | Customer's gender |
| Age | Customer's age |
| Tenure | Number of years the customer has been with the bank |
| Balance | Customer's bank account balance |
| NumOfProducts | Number of bank products used by the customer |
| HasCrCard | Indicates whether the customer has a credit card |
| IsActiveMember | Indicates whether the customer is an active bank member |
| EstimatedSalary | Customer's estimated salary |

---

## 🤖 Machine Learning Model

A trained machine learning model is used to predict customer churn.

The trained model is stored in:

`churn_model.pkl`

The application takes the customer's information as input and passes the required features to the trained model.

The model generates a prediction indicating whether the customer is likely to stay or churn.

When probability prediction is available, the application also displays the estimated churn probability.

---

## 🔄 How the Application Works

The application follows the following process:

```text
Customer Details
       ↓
Input Collection
       ↓
Feature Encoding
       ↓
Trained Machine Learning Model
       ↓
Churn Prediction
       ↓
Churn Probability
       ↓
Display Prediction Result

----
---

## 🛠️ Technologies Used

- Python
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Machine Learning

---

## 📁 Project Structure

```text
Bank-Customer-Churn-Prediction/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md
