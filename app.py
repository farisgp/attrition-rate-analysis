import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -----------------------------------------------
# Fungsi untuk load model
# -----------------------------------------------
@st.cache_resource
def load_model():
    with open("attrition_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -----------------------------------------------
# Halaman Aplikasi
# -----------------------------------------------
st.title("Employee Attrition Prediction")
st.write("""
Aplikasi ini memprediksi kemungkinan seorang karyawan keluar (attrition) berdasarkan fitur input.
""")

# -----------------------------------------------
# Input User (Sesuaikan dengan fitur dataset)
# -----------------------------------------------
st.header("Masukkan Data Employee")

age = st.number_input("Age", min_value=18, max_value=70, value=30)
monthly_income = st.number_input("Monthly Income", min_value=1000, value=5000)
years_at_company = st.number_input("Years at Company", min_value=0, value=3)
job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 2)
over_time = st.selectbox("OverTime", ["Yes", "No"])

# Encoding sederhana (ubah sesuai model)
overtime_encoded = 1 if over_time == "Yes" else 0

# -----------------------------------------------
# Trigger Prediksi
# -----------------------------------------------
if st.button("Predict Attrition"):
    X = np.array([[age, monthly_income, years_at_company, job_satisfaction, overtime_encoded]])
    
    # Prediksi
    pred = model.predict(X)[0]
    proba = model.predict_proba(X)[0][1] if hasattr(model, "predict_proba") else None
    
    st.write("### Hasil Prediksi:")
    st.write("➡️ **Attrition = Yes**" if pred == 1 else "➡️ **Attrition = No**")
    
    if proba is not None:
        st.write(f"💡 Probability Attrition: {proba*100:.2f}%")

# -----------------------------------------------
# Visualisasi (opsional)
# -----------------------------------------------
st.header("Tentang Model")
st.markdown("""
Model prediksi dibangun menggunakan Python dan scikit-learn.
Model dilatih untuk mengestimasi risiko attrition berdasarkan fitur employee.
""")
