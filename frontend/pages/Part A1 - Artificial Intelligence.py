import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="AI Fields", layout="wide", page_icon="⚕️")

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

colDS, colAI = st.columns(2)

with colDS:
    st.markdown("""### 1. What is Data Science?""")
    st.markdown("""
    When we mention “Data Science”, typically we are referring a slum of jobs that it’s goal to support another industry by driven-data such as:
    - Finance, military, healthcare
    - Retails & e-commerce
    - Transportaion & logistic
    - Sport, entertainment & media
    
    Data Science is an interdisciplinary field that being combined from many fields. 
    - Data Engineering
    - Big Data Analytics
    - Business Intelligence
    - Using Machine Learning models as Engineering
    - Using Deep Learning models as Engineering
    """)

with colAI:
    st.markdown("""### 2. What is Artificial Intelligence?""")
    st.markdown("""
    Artificial Intelligence (AI) refers to the broader concept of machines being able to carry out tasks in a way that we would consider “smart” or “intelligent.”
    - Understanding language
    - Recognizing images
    - Playing games
    - Driving a car
    
    The most common and cutting-edge fields of AI nowadays:
    - Machine Learning
    - Deep Learning
    - Natural Language Processing
    - Computer Vision
    - Robotics
    """)

st.markdown("""### 3. Difference between Data Science and AI?""")

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()
image1 = Image.open("../images/ai_ml_dl.jpg")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{image_to_base64(image1)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

colML, colDL = st.columns(2)

with colML:
    st.markdown("""### 4. Machine Learning (ML)""")
    st.markdown("""
        Machine Learning is a branch of Artificial Intelligence (AI) that enables systems to learn from data, identify patterns, 
        and make decisions with minimal human intervention. Instead of being explicitly programmed for a specific task, 
        Machine Learning algorithms are "trained" on large amounts of data to automatically discover rules or relationships.
    
        **Key types of learning in Machine Learning:**
        - Supervised Learning: Models are trained on a labeled dataset (with both input and desired output). 
        The goal is to learn a mapping from inputs to outputs. Examples: regression (predicting house prices), classification (spam/non-spam email classification).
        - Unsupervised Learning: Models are trained on unlabeled data. 
        The goal is to find hidden structures or patterns within the data. Examples: clustering (grouping customers), dimensionality reduction. 
        It is useful when manual labeling is impractical or too costly.
        - Reinforcement Learning: An agent learns to make decisions through interaction with an environment. 
        The agent receives rewards or penalties based on its actions, and the goal is to maximize cumulative rewards. Examples: playing games, robot control.
    
        **Common Machine Learning algorithms:** 
        - Linear Regression: predicts continuous values by modeling a linear relationship between in&outputs.
        - Logistic Regression: predicts the probability of binary classes using a sigmoid function.
        - Decision Trees: splits data into branches based on conditions to perform classification or regression.
        - Random Forests: combines multiple decision trees to improve accuracy and reduce overfitting.
        - K-Nearest Neighbors (KNN): classifies or predicts based on the labels of the k nearest data points.
        - Support Vector Machines (SVMs): finds the optimal hyperplane to separate data into different classes.
        - Naive Bayes: classifies data based on Bayes’ Theorem with the assumption of feature independence.
        - k-Means: clusters data into k groups based on the nearest mean of each group.
    """)
with colDL:
    st.markdown("""### 5. Deep Learning (DL)""")
    st.markdown("""
        Deep Learning is a subfield of Machine Learning, inspired by the structure and function of the human brain, specifically neural networks. 
        Deep Learning uses Artificial Neural Networks (ANNs) with multiple hidden layers (hence "deep") to learn complex representations of data. 
        It has achieved remarkable success in fields such as computer vision, natural language processing, and speech recognition.
    
        **Key characteristics of Deep Learning:**
        - Deep Neural Networks: consist of many layers (often tens, hundreds, or even thousands of layers) 
        allowing the model to learn features from low-level to more high-level and abstract representations.
         This hierarchical learning is key to its effectiveness in tasks like image and speech recognition.
        - Automatic Feature Learning: unlike traditional Machine Learning which often requires engineers to perform manual feature engineering, 
        Deep Learning can automatically extract and learn important features directly from raw data. 
        - Ability to Process Large Data: deep Learning typically requires large amounts of data to achieve optimal performance and 
        is particularly effective with unstructured data like images, audio, and text. 
        As the volume of data increases, deep learning models often continue to improve in accuracy.
        
        **Types of Network Architectures:**
        - Convolutional Neural Networks (CNNs): highly effective for Computer Vision tasks like image recognition, object detection.
        - Recurrent Neural Networks (RNNs): suitable for sequential data and Natural Language Processing (NLP) tasks like machine translation, text generation.
        - Long Short-Term Memory (LSTMs) and Gated Recurrent Units (GRUs): variants of RNNs designed to overcome the vanishing/exploding gradient problem in long sequences.
        - Generative Adversarial Networks (GANs): used to generate new, realistic data (e.g., images, music) by training two neural networks.
    
        """)

st.markdown("""### 6. Differences between Machine Learning and Deep Learning""")
st.markdown("""
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        thead {
            background-color: #f2f2f2;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
            vertical-align: top;
            word-wrap: break-word;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        tr:hover {
            background-color: #f1f1f1;
        }
    </style>

    <table>
        <thead>
            <tr>
                <th>Characteristic</th>
                <th>Machine Learning (ML)</th>
                <th>Deep Learning (DL)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Subset Of</td>
                <td>A branch of AI</td>
                <td>A subfield of ML</td>
            </tr>
            <tr>
                <td>Architecture</td>
                <td>Traditional algorithms like SVM, decision trees, regression.</td>
                <td>Artificial Neural Networks with multiple hidden layers (deep networks).</td>
            </tr>
            <tr>
                <td>Feature Engineering</td>
                <td>Requires manual feature engineering.</td>
                <td>Automatically learns and extracts features from raw data.</td>
            </tr>
            <tr>
                <td>Data Requirements</td>
                <td>Performs well with small to medium amounts of data.</td>
                <td>Requires very large amounts of data for optimal performance.</td>
            </tr>
            <tr>
                <td>Computational Power</td>
                <td>Requires less computational resources.</td>
                <td>Requires significant computational resources (GPU/TPU).</td>
            </tr>
            <tr>
                <td>Performance</td>
                <td>Performance generally plateaus as data increases beyond a point.</td>
                <td>Performance continues to increase significantly with more data.</td>
            </tr>
            <tr>
                <td>Interpretability</td>
                <td>Traditional ML models are often more interpretable.</td>
                <td>DL models are often "black boxes," harder to explain.</td>
            </tr>
            <tr>
                <td>Typical Applications</td>
                <td>Email spam classification, house price prediction, recommendation systems.</td>
                <td>Face recognition, self-driving cars, machine translation, chatbots.</td>
            </tr>
        </tbody>
    </table>
""", unsafe_allow_html=True)


image2 = Image.open("../images/ml_vs_dl.jpg")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{image_to_base64(image2)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)