import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Heart Disease Risk Calculator", page_icon="❤️")

st.title("❤️ Heart Disease Risk Predictor")
st.write("Enter your health metrics to check your 10-year heart disease risk. This tool uses a machine learning model trained on real data.")


age = st.number_input("Age", min_value=20, max_value=100, value=50)
gender = st.radio("Gender", ["Male", "Female"])
cigs = st.number_input("Cigarettes per day", min_value=0, max_value=60, value=0)
chol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=400, value=200)
sysbp = st.number_input("Systolic BP", min_value=80, max_value=250, value=120)
diabp = st.number_input("Diastolic BP", min_value=50, max_value=150, value=80)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
hr = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)
glucose = st.number_input("Glucose", min_value=60, max_value=200, value=85)


gender_val = 1 if gender == "Male" else 0


model = joblib.load("models/heart_risk_model.pkl")


if st.button("Check Risk"):
    input_data = pd.DataFrame([{
        "age": age,
        "gender": gender_val,
        "cigsPerDay": cigs,
        "totChol": chol,
        "sysBP": sysbp,
        "diaBP": diabp,
        "BMI": bmi,
        "heartRate": hr,
        "glucose": glucose
    }])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader(f"🔍 Prediction: {'At Risk' if prediction == 1 else 'Not At Risk'}")
    st.info(f"📊 Probability of risk: `{probability * 100:.2f}%`")


st.markdown("---")
st.warning("⚠️ This is a learning project and not a medical diagnosis tool. Please consult a doctor for professional medical advice.")
