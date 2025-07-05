import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home", layout="wide", page_icon="⚕️")

st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important; /* delete default spacing between all content and top padding */
        }
        .header {
            padding-top: 10px; /* spacing between header and top padding */
            display: flex; /* place child divs in horizontal */
            justify-content: center;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .main-content {
            padding-top: 30px; /* spacing between main content and header */
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

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("""
    ### What Is This Project ❓❓❓
    - ℹ️ Introduction to artificial intelligence
    - ℹ️ Basic information about diabetes
    
    - 🤖 Machine learning fundamental guide
    - 🤖 The machine learning method to predict diabetes
    - 🧠 Deep learning fundamental guide
    - 🧠 The deep learning method to build chatbot
    
    - 🔍 Overview of the datasets
    - 🔍 Exploratory data analysis of the datasets
    - ⚖️ Machine Learning model evaluation
    - ⚖️ Deep Learning model evaluation 
    
    ---
    
    - 🚀 Interactive diabetes risk assessment tool
    - 🚀 Visualizing metrics and prediction results
    - 🚀 Retrieval-based & AI chatbot for diabetes
    """)

with col2:
    image = Image.open("../images/wallpaper.jpg")
    st.image(image, caption="", use_container_width=True)

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)