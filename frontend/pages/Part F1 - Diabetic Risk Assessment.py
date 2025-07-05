import streamlit as st
import requests
import sys
import os
from datetime import date

# Add parent folder to path to import database functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from database.database_functions import delete_all_predictions, get_predictions_from_db

st.set_page_config(page_title="Assessment", layout="wide", page_icon="⚕️")
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important;
        }
        .header {
            padding-top: 10px;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .main-content {
            padding-top: 30px;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #f0f2f6;
            color: #333;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <h1 style="font-size: 80px; font-weight: 800; color: #e74c3c; margin: 0;">GlucoMate</h1>
        <h1 style="font-size: 40px; font-weight: 600; color: #1e81b0; margin: 0;">AI-based Diabetes Support System</h1>
    </div>

    <div class="main-content"></div>
""", unsafe_allow_html=True)

# --- SUPPORT FUNCTIONS ---
def display_predictions(predictions):
    if not predictions:
        st.write("No prediction history found.")
    else:
        for pred in predictions:
            st.markdown(
                f"""
                <div style="font-size:21.7px; color:#1f77b4; font-weight:bold;">
                    Time: {pred[9]}
                </div>
                """,
                unsafe_allow_html=True
            )
            col1, col2, col3, col4 = st.columns([1.25, 1, 1, 1.25])
            with col1:
                st.write(f"👤 **Name:** {pred[1]}")
                st.write(f"📅 **Date of Birth:** {pred[2]}")
            with col2:
                st.write(f"🔢 **Age:** {pred[3]}")
                st.write(f"⚧️ **Gender:** {'Male' if pred[4] == 1 else 'Female'}")
            with col3:
                st.write(f"📐 **BMI:** {pred[5]}")
                st.write(f"🩸 **Glucose Level:** {pred[6]}")
            with col4:
                st.write(f"💉 **HbA1c:** {pred[7]}")
                result = '🔴 At Risk' if pred[8] == 1 else '🟢 Not at Risk'
                st.write(f"🔔 **Result:** {result}")

def set_confirm_delete():
    st.session_state.confirm_delete = True

# --- MAIN INTERFACE ---
col_left, col_right = st.columns([1, 2])

# --- Input Form ---
with col_left:
    st.markdown("<h3 style='text-align: center;'>📝 Enter Personal Information</h3>", unsafe_allow_html=True)
    with st.form("patient_form"):
        name = st.text_input("👤 Full Name")
        dob = st.date_input("📅 Date of Birth", value=date(1990, 1, 1), min_value=date(1900, 1, 1), max_value=date.today())
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("🔢 Current Age", 0, 120, 30)
            gender = st.selectbox("⚧️ Gender", ["Male", "Female"])
            smoking_history = st.selectbox("🚬 Smoking History", ["None", "Moderate", "Heavy"])
            bmi = st.number_input("📐 Body Mass Index (BMI)", 10.0, 60.0, 22.5)
        with col2:
            hypertension = st.selectbox("💓 Hypertension?", ["No", "Yes"])
            heart_disease = st.selectbox("❤️ Heart Disease History?", ["No", "Yes"])
            glucose = st.number_input("🩸 Glucose Level", 50.0, 400.0, 120.0)
            hba1c = st.number_input("💉 Blood Sugar (HbA1c)", 3.0, 15.0, 5.5)

        submit_btn = st.form_submit_button("Run Prediction")

    gender_map = {"Male": 1, "Female": 0}
    smoke_map = {"None": 0, "Moderate": 1, "Heavy": 2}

    if submit_btn:
        if not name or not dob:
            st.warning("❗ Please enter both name and date of birth.")
        else:
            with st.spinner("⏳ Analyzing..."):
                input_data = {
                    "name": name,
                    "dob": dob.strftime("%Y-%m-%d"),
                    "age": age,
                    "bmi": bmi,
                    "gender": gender_map[gender],
                    "smoking_history": smoke_map[smoking_history],
                    "hypertension": 1 if hypertension == "Yes" else 0,
                    "heart_disease": 1 if heart_disease == "Yes" else 0,
                    "blood_glucose_level": glucose,
                    "HbA1c_level": hba1c
                }

                try:
                    response = requests.post("http://localhost:5000/predict", json=input_data)
                    result = response.json()
                    pred = result.get("diabetes_prediction", -1)
                    if pred == 1:
                        st.error("🔴 **Result:** At RISK of diabetes.")
                    elif pred == 0:
                        st.success("🟢 **Result:** No signs of diabetes.")
                    else:
                        st.warning("Invalid result received from the server.")
                except Exception as e:
                    st.error(f"❌ Error connecting to API: {e}")

# --- Prediction History ---
with col_right:
    st.markdown("<h3 style='text-align: center;'>📜 Recent Prediction History</h3>", unsafe_allow_html=True)
    with st.expander("Click to view"):
        predictions = get_predictions_from_db()
        display_predictions(predictions)

    if st.session_state.get("confirm_delete", False):
        st.warning("Are you sure you want to delete all history?")
        col_confirm, col_cancel = st.columns(2)
        with col_confirm:
            if st.button("✅ Confirm Delete"):
                try:
                    delete_all_predictions()
                    st.success("✅ All history deleted.")
                except Exception as e:
                    st.error(f"❌ Error deleting history: {e}")
                st.session_state.confirm_delete = False
        with col_cancel:
            if st.button("❌ Cancel"):
                st.info("Deletion cancelled.")
                st.session_state.confirm_delete = False
    else:
        st.button("Delete All Prediction History", on_click=set_confirm_delete)

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)
