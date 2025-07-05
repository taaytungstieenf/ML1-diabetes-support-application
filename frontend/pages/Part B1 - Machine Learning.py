import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Machine Learning", layout="wide", page_icon="⚕️")

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

def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

st.markdown("### 1. Machine Learning Knowledge Reminder")
st.markdown("""
Machine Learning is a field of artificial intelligence that allows systems to learn from data, recognize patterns, 
and make predictions or decisions without being explicitly programmed for each task. 
Instead of writing specific rules, we “train” Machine Learning models by showing them large amounts of data, 
and from there, they automatically discover hidden relationships and structures.

**Main goals of Machine Learning:**
- Prediction: For example, predicting house prices, predicting stock market trends, or predicting the likelihood of a customer churning.
- Classification: For example, classifying spam/non-spam emails, recognizing pictures of cats/dogs, or diagnosing diseases based on symptoms.
- Anomaly detection: Finding unusual data points, for example in credit card fraud detection.
- Clustering: Grouping similar data points together without prior labels, for example in customer segmentation.
""")

st.markdown("### 2. The Fundamentals Supervised Learning Models")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ##### a. Linear Regression
    
    **Purpose:**
    
    Predict a continuous value, e.g. house price, temperature, sales.
    
    **Idea:**
    
    Linear Regression assumes that the output has a linear relationship with the input. 
    The model learns to find a best fit line to predict the output based on the input features.
    
    **Specifications:**
    
    Fast training speed, suitable for low noise and linear problems, easy to interpret results
    """)

    st.markdown("""**Basic formula:**""")
    st.latex(r"y = w_1 x_1 + w_2 x_2 + \ldots + w_n x_n + b")
    st.latex(r"w_i: \text{weight to learn}")
    st.latex(r"x_i: \text{input variable}")
    st.latex(r"b: \text{bias}")
    st.latex(r"y: \text{predicted output}")

    st.markdown("""
    **Diagram:**
    """)

    image1 = Image.open("../images/line_chart_linear_regression.jpg")
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image1)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("""
        ##### b. Logistic Regression

        **Purpose:**

        Binary classification, e.g. whether an email is spam or not, whether a customer will churn.
        
        **Idea:**

        Despite the name “Regression”, it is actually a classification algorithm. 
        Logistic Regression uses a sigmoid function to transform a linear output into a probability of belonging to a certain class (0 or 1).

        **Specifications:**

        Easy to implement, good for basic classification often a good baseline for classification problems
        """)

    st.markdown("""**Basic formula:**""")
    st.latex(r"\sigma(z) = \frac{1}{1 + e^{-z}}, \quad \text{with } z = w^T x + b")

    st.markdown("""- ***Output of the sigmoid function, the value is always in the interval (0, 1)***""")

    col_1, col_0 = st.columns(2)
    with col_1:
        st.latex(r"\sigma(z) > 0.5 \text{ predict for layer 1}")
    with col_0:
        st.latex(r"\sigma(z) < 0.5 \text{ predict for layer 0}")
    st.markdown("""- ***Input of the sigmoid function, is calculated by linear combination of features and weights***""")
    st.latex(r"z = w^T x + b = w_1 x_1 + w_2 x_2 + \ldots + w_n x_n + b")

    st.markdown("""
        **Diagram:**
        """)

    image2 = Image.open("../images/line_chart_logistic_regression.png")
    st.markdown(
        f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(image2)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
            </div>
            """,
        unsafe_allow_html=True
    )

st.markdown("### 3. The Fundamentals Unsupervised Learning Models")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ##### a. K-Means Clustering

    **Purpose:**

    Group data into clusters so that points in the same cluster have similar properties.
    
    **Idea:**

    K-Means assumes that the data can be divided into K distinct clusters. Each cluster has a center (centroid), 
    and the algorithm assigns each data point to the cluster with the closest center, then updates the center until convergence.

    **Specifications:**

    Fast, easy to understand, effective on data with clear clusters, requires user to specify number of clusters K, 
    not suitable for data with complex cluster shapes or density differences
    """)

    st.markdown("""**Distance formula:**""")
    st.latex(r"\text{dist}(x, \mu_k) = \sqrt{ \sum_{i=1}^{n} (x_i - \mu_{k,i})^2 }")

    st.latex(r"x_i: \text{a point of data}")
    st.latex(r"μ_k: \text{center of kth cluster}")
    st.latex(r"n: \text{number of dimensions}")
    st.latex(r"\text{dist}(x, \mu_k): \text{distance from point x to cluster center k}")

    st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
    st.markdown("""
    **Diagram:**
    """)

    image3 = Image.open("../images/k-means.jpg")
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image3)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown("""
        ##### b. PCA – Principal Component Analysis

        **Purpose:**

        Reduce the dimensionality of data while retaining most of the important information (variance of data).

        **Idea:**

        PCA finds new directions (principal components) in the data space that are "most evenly spread" in those directions. 
        These directions are orthogonal vectors with the largest variance in the data. 
        By selecting the first few principal components, we can represent the data in a lower-dimensional space.

        **Algorithm process:**

        - Normalize the data (zero mean, unit variance)
        - Calculate the covariance matrix
        - Calculate the eigenvectors and eigenvalues
        - Select the largest principal components
        - Project the data into the new 
        
        **Pros and cons:**
        - Pros
            - Reduce data dimensionality, help the model learn quickly and avoid overfitting
            - Easily visualize data (e.g. from 100 dimensions → 2D to draw a chart)
            - Help detect key features of the data
            
        - Cons
            - Does not retain the original meaning of each feature
            - Only captures the linear relationship between variables
        """)

    st.markdown("""**Diagram:**""")
    image4 = Image.open("../images/k-means_guided_by_pca.jpg")
    st.markdown(
        f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(image4)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
            </div>
            """,
        unsafe_allow_html=True
    )

st.markdown("### 4. Initializing Models")
tab1, tab2, tab3, tab4 = st.tabs(["Linear Regression", "Logistic Regression", "K-Means", "K-Means + PCA"])

with tab1:
    st.code("""
            from sklearn.datasets import make_regression
            from sklearn.linear_model import LinearRegression
            from sklearn.model_selection import train_test_split
            
            # Create data
            X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
            
            # Train/test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Train model
            model = LinearRegression()
            model.fit(X_train, y_train)
            
            # Predict
            y_pred = model.predict(X_test)
    """)

with tab2:
    st.code("""
            from sklearn.datasets import make_classification
            from sklearn.linear_model import LogisticRegression
            from sklearn.model_selection import train_test_split
            
            # Create data
            X, y = make_classification(n_samples=100, n_features=2, n_classes=2, random_state=42)
            
            # Train/test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            # Train
            model = LogisticRegression()
            model.fit(X_train, y_train)
            
            # Predict
            y_pred = model.predict(X_test)
    """)

with tab3:
    st.code("""
            from sklearn.datasets import make_blobs
            from sklearn.cluster import KMeans
            
            # Create data
            X, _ = make_blobs(n_samples=150, centers=3, n_features=2, random_state=42)
            
            # Apply K-Means
            kmeans = KMeans(n_clusters=3, random_state=42)
            kmeans.fit(X)
            
            # Cluster label predict
            labels = kmeans.labels_
    """)

with tab4:
    st.code("""
            from sklearn.decomposition import PCA
            from sklearn.datasets import make_blobs
            from sklearn.cluster import KMeans
            
            # Create multidimensional data
            X, _ = make_blobs(n_samples=200, centers=4, n_features=5, random_state=42)
            
            # Dimensionality reduction with PCA
            pca = PCA(n_components=2)
            X_pca = pca.fit_transform(X)
            
            # K-Means on reduced dimensionality data
            kmeans = KMeans(n_clusters=4, random_state=42)
            kmeans.fit(X_pca)
            
            # Cluster label
            labels = kmeans.labels_
    """)


st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)