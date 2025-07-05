import streamlit as st
import matplotlib.pyplot as plt
import sys
import os
import io

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from database.database_functions import get_predictions_from_db

st.set_page_config(page_title="Visualization", layout="wide", page_icon="⚕️")
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

predictions = get_predictions_from_db()

if not predictions:
    st.warning("⚠️ No data available for visualization.")
else:
    latest = predictions[0]
    name, dob = latest[1], latest[2]
    age, gender, bmi, glucose, hba1c, prediction, timestamp = latest[3:]

    st.markdown(f"""
    <div style="font-size: 16px; padding: 4px 0;">
        <b>Name:</b> {name} | <b>Date of Birth:</b> {dob} | <b>Time:</b> {timestamp} | <b>Result:</b> {'<span style="color:red;"> At Risk of Diabetes</span>' if prediction == 1 else '<span style="color:green;">Not at Risk</span>'}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

    metrics = {
        'BMI (kg/m²)': {'value': bmi, 'threshold': 24.9},
        'Glucose (mg/dL)': {'value': glucose, 'threshold': 130},
        'HbA1c (%)': {'value': hba1c, 'threshold': 7}
    }

    def get_color(val, threshold):
        if val <= threshold:
            return '#58D68D'
        elif val <= threshold * 1.15:
            return '#F4D03F'
        else:
            return '#EC7063'

    labels = list(metrics.keys())
    values = [metrics[label]['value'] for label in labels]
    thresholds = [metrics[label]['threshold'] for label in labels]
    colors = [get_color(val, thr) for val, thr in zip(values, thresholds)]

    fig, ax = plt.subplots(figsize=(7, 5))
    bars = ax.bar(labels, values, color=colors, width=0.5, edgecolor='black', linewidth=0.7)

    for label in labels:
        threshold = metrics[label]['threshold']
        ax.axhline(y=threshold, color='blue', linestyle='-', linewidth=1, label=f'{label}: {threshold}')

    handles, legend_labels = ax.get_legend_handles_labels()
    unique = dict(zip(legend_labels, handles))
    ax.legend(unique.values(), unique.keys(), loc='upper right', fontsize=9)

    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim())
    ax2.set_yticks(thresholds)
    ax2.set_yticklabels([str(t) for t in thresholds], fontsize=9, color='blue')
    ax2.tick_params(axis='y', length=0)
    ax2.get_xaxis().set_visible(False)

    ax.set_ylabel("Value", fontsize=12, rotation=0, labelpad=40)
    ax.set_title("Health Metrics Chart", fontsize=15, color='#333')
    ax.bar_label(bars, fmt='%.1f', fontsize=10, rotation=0, label_type='edge', padding=3)
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=10)

    plt.tight_layout()
    plt.show()

    col1, col2 = st.columns([1.25, 1])
    with col1:
        st.pyplot(fig)
        img_buffer = io.BytesIO()
        fig.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        st.download_button(
            label="Download Chart",
            data=img_buffer,
            file_name='health_chart.png',
            mime='image/png'
        )

    with col2:
        st.markdown("<h3 style='text-align: center; color: #21130d;'>🤓 Metric Assessment</h3>", unsafe_allow_html=True)

        # BMI
        if bmi < 18.5:
            st.warning(f"**BMI = {bmi:.1f}**: Underweight. Consider consulting a doctor for nutritional advice.")
        elif bmi <= 24.9:
            st.success(f"**BMI = {bmi:.1f}**: Normal. You are at a healthy weight.")
        elif bmi <= 29.9:
            st.warning(f"**BMI = {bmi:.1f}**: Overweight. Monitor your diet and exercise.")
        else:
            st.error(f"**BMI = {bmi:.1f}**: Obese. High risk for metabolic diseases. Consult a healthcare professional.")

        # Glucose
        if glucose < 80:
            st.warning(f"**Glucose = {glucose:.1f} mg/dL**: Possibly hypoglycemia. Check again during fasting.")
        elif glucose <= 130:
            st.success(f"**Glucose = {glucose:.1f} mg/dL**: Within normal range.")
        elif glucose <= 180:
            st.warning(f"**Glucose = {glucose:.1f} mg/dL**: Slightly high after meals. Monitor closely.")
        else:
            st.error(f"**Glucose = {glucose:.1f} mg/dL**: Exceeds healthy limit. High diabetes risk.")

        # HbA1c
        if hba1c < 5.7:
            st.success(f"**HbA1c = {hba1c:.1f}%**: Normal.")
        elif hba1c <= 6.4:
            st.warning(f"**HbA1c = {hba1c:.1f}%**: Pre-diabetic. Manage your diet and physical activity.")
        else:
            st.error(f"**HbA1c = {hba1c:.1f}%**: Clear risk of diabetes. Seek medical advice.")

        st.info("👉 Please update your health indicators regularly to prevent diseases early.")

        st.markdown("<h3 style='text-align: center; color: #21130d;'>🤔 Advice for You</h3>", unsafe_allow_html=True)

        if prediction == 1:
            st.markdown(
                """
                <div style="
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-left: 5px solid gray;
                    border-radius: 8px;
                    font-size: 16px;
                ">
                    - Daily blood sugar control helps you stay healthy and avoid complications. Stick to a suitable diet and exercise routine.<br>
                    - Schedule regular health check-ups and maintain communication with your doctor for optimal care.
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                """
                <div style="
                    background-color: #f9f9f9;
                    padding: 15px;
                    border-left: 5px solid gray;
                    border-radius: 8px;
                    font-size: 16px;
                ">
                    - You're maintaining a healthy lifestyle. Keep up with regular exercise and a balanced diet.<br>
                    - Your indicators are within safe ranges — great job! Continue practicing good habits daily.
                </div>
                """,
                unsafe_allow_html=True
            )

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)
