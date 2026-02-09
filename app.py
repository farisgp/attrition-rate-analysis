import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Attrition Rate Prediction",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("attrition_model.pkl", "rb") as f:
        return pickle.load(f)

try:
    model = load_model()
except Exception as e:
    st.error("Model gagal dimuat")
    st.exception(e)
    st.stop()

st.title("🎓 Student Attrition Prediction")

st.subheader("Input Data")

age = st.number_input("Age", 15, 60, 20)
attendance = st.slider("Attendance (%)", 0, 100, 80)
gpa = st.slider("GPA", 0.0, 4.0, 3.0)
financial_aid = st.selectbox("Financial Aid", ["Yes", "No"])
financial_aid = 1 if financial_aid == "Yes" else 0

if st.button("Predict"):
    X = pd.DataFrame([{
        "age": age,
        "attendance": attendance,
        "gpa": gpa,
        "financial_aid": financial_aid
    }])

    prediction = model.predict(X)[0]

    if prediction == 1:
        st.error("⚠️ Berpotensi Dropout")
    else:
        st.success("✅ Tidak Berpotensi Dropout")
