import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="ML for Project", layout="wide", page_icon="⚕️")

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

st.markdown("""### 1. Introduction to Decision Tree""")

col1, col2 = st.columns([1.5,1])
with col1:
    st.markdown("""
    ##### a. Basic Concepts
    - It is a simple yet powerful supervised learning model that works as binary questions to classify or predict values.
    - It works in a tree structure: each node is a condition, each branch is a branch, and the leaf is the output.
    ##### b. How it works
    - Find the best attribute to split the data → use criteria like Gini, Entropy, Information Gain.
    - Predict by going from root to leaf according to the conditions.
    """)
    colp, colc = st.columns(2)
    with colp:
        st.markdown("""
        ##### Pros
        - Easy to understand, intuitive
        - No data normalization required
        - Can handle missing data
        """)
    with colc:
        st.markdown("""
        ##### Cons
        - Easy to overfit without constraints
        - Sensitive to noise
        - Simple model, less accurate
        """)
with col2:
    image1 = Image.open("../images/decision_tree.jpg")
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image1)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("""### 2. Introduction to Boosting""")
col3, col4 = st.columns([1.5,1])
with col3:
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

        <h5>a. General Concept of Boosting</h5>
        <ul>
            <li>Boosting = combine the strength of many weak models → into a strong model.</li>
            <li>Instead of training one large model, it trains many small models in succession — each one correcting the previous.</li>
        </ul>

        <h5>b. How it works</h5>
        <ul>
            <li>The initial model makes errors → the next model focuses on these errors.</li>
            <li>This continues iteratively to reduce overall error.</li>
        </ul>

        <h5>c. Common Boosting Models</h5>
        <table>
            <thead>
                <tr>
                    <th>Algorithm</th>
                    <th>Characteristic</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AdaBoost</td>
                    <td>The following model focuses on the more difficult points.</td>
                </tr>
                <tr>
                    <td>Gradient Boosting</td>
                    <td>The following model optimizes the error according to the gradient.</td>
                </tr>
                <tr>
                    <td>LightGBM</td>
                    <td>Uses histogram-based algorithm, very fast, and good for large datasets.</td>
                </tr>
                <tr>
                    <td>CatBoost</td>
                    <td>Performs well on categorical data, often with little preprocessing.</td>
                </tr>
                <tr>
                    <td>XGBoost</td>
                    <td>Balanced in speed and accuracy; highly regularized and widely used in competitions.</td>
                </tr>
            </tbody>
        </table>
    """, unsafe_allow_html=True)

with col4:
    image2 = Image.open("../images/gradient_boosting.jpg")
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    st.markdown(
        f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{image_to_base64(image2)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
            </div>
            """,
        unsafe_allow_html=True)

st.markdown("""### 3. Gradient Boosting: XGBoost""")
st.markdown("""
##### a. Overview
XGBoost (Extreme Gradient Boosting) is a decision tree-based boosting machine learning algorithm. 
It is designed to optimize performance (speed + accuracy) and generalization in prediction problems.
- Launched in 2016, it quickly became a "key" model in Kaggle competitions, thanks to its fast training speed, 
ability to handle missing data, and outstanding efficiency.
- An upgrade of traditional Gradient Boosting, with many improvements in algorithm optimization, memory optimization, and regularization (anti-overfitting).
""")
st.markdown("""
##### b. How it Works
Instead of building a large model from scratch, XGBoost gradually builds many small models (weak trees) and each tree learns from the errors of the previous tree.

The general formula:""")

st.latex(r"\hat{y}_i = \sum_{k=1}^{K} f_k(x_i), \quad f_k \in \mathcal{F}")
st.latex(r"\hat{y}_i: \text{ predict output for data sample } i")
st.latex(r"K: \text{ total number of trees (number of boosting rounds)}")
st.latex(r"f_k(x_i): \text{ prediction from the second tree } k \text{ corresponding to the input } x_i")
st.latex(r"\mathcal{F}: \text{ space of tree models (decision trees)}")

st.markdown("""

##### c. Outstanding features
- Anti-overfitting: thanks to regularization (L1, L2)
- Automatic data shortage handling
- Efficient parallel running, more optimized speed than many other libraries
- Highly customizable: many parameters to adjust such as max_depth, learning_rate, n_estimators, subsample...
- Supports both regression and classification

##### d. When should I use CatBoost?
- Tabular data (table format: csv, excel, database…)
- No need for complex feature processing (XGBoost automatically finds important features)
- When you want high performance, good accuracy, good scalability
- When you want an easy-to-explain model (can analyze which features are important)
""")
st.markdown("""
##### e. Tree growth example
""")

col5, col6 = st.columns([1, 3])
with col5:
    image5 = Image.open("../images/structure_xgboost.jpg")
    st.markdown(
        f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(image5)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
                </div>
                """,
        unsafe_allow_html=True)
with col6:
    st.markdown("""
    Tree Growth Mechanism (as seen in the example):
    - XGBoost grows trees by splitting nodes in a level-wise fashion, meaning it explores all potential splits at a given depth before moving to the next level. 
    However, within each level, it prioritizes splits that yield the largest gain (reduction in loss function).
    - The example shows X7 > 0.5 as the initial split. Then, the left branch is split by X3 < 0.33, while the right branch is split by X5 > 0.43. 
    This demonstrates that different features and thresholds can be chosen for different branches at the same depth if they provide a better gain.
    - Subsequent splits (X9 < 3.6, X6 < 96, X2 < 0.6, X1 > 9) also show this flexible, best-first approach, 
    where the algorithm continuously looks for the most impactful splits.

    Why this approach? This strategy allows XGBoost to be highly optimized and parallelizable. 
    By evaluating all possible splits at a given level, it aims to find the globally best splits at that level, leading to often deeper but effective trees.
    """)

st.markdown("""### 4. Gradient Boosting: CatBoost""")
st.markdown("""
##### a. Overview
CatBoost (Categorical Boosting) is an advanced Boosting algorithm developed by Yandex (a large Russian technology company). 
It is designed to handle classification and regression problems well, especially optimized for data with categorical features.
- It is a member of the gradient boosting models group, such as XGBoost and LightGBM.
- Outstanding advantages: no need to manually encode categorical variables, reducing data processing effort.

##### b. How it Works
Like other boosting models, CatBoost works by building multiple decision trees in order. 
Each new tree learns from the residual error of the previous tree ensemble. However, CatBoost has important differences:
- Processing categorical variables with a special algorithm (mean target encoding + permutation)
- Using Ordered Boosting to avoid target leakage and reduce overfitting
- Optimizing gradient descent with Symmetric Trees technique → more speed and stability

##### c. Outstanding features
- Automatic processing of categorical features
- No LabelEncoder or OneHotEncoder required
- Less hyperparameter tuning required
- Good overfitting resistance thanks to "Ordered Boosting"
- Supports classification, regression, and ranking

##### d. When should I use CatBoost?
- When the data contains many categorical columns (such as "Gender", "Country", "Product Type"...)
- When you want to reduce manual data processing
- When you need a powerful model but less tuning
""")
st.markdown("""
##### e. Tree growth example
""")

col5, col6 = st.columns([1, 3])
with col5:
    image3 = Image.open("../images/structure_catboost.jpg")
    st.markdown(
        f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(image3)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
                </div>
                """,
        unsafe_allow_html=True)
with col6:
    st.markdown("""
    Tree Growth Mechanism (as seen in the example):
    - CatBoost typically builds symmetric trees (also known as oblivious trees or decision trees with a fixed number of splits at each level). 
    This means that all leaves at the same level of the tree are split by the same feature and threshold.
    
    - In the example, the tree starts with X7 > 0.5. 
    Both resulting branches are then consistently split by X3 < 0.33, and then all subsequent branches are further split by X4 < 4.6.
    
    Why this approach? This symmetric growth helps reduce overfitting by limiting the complexity of individual trees and 
    promoting a more global understanding of the data. 
    The ordered boosting mechanism, which is a core part of CatBoost, also benefits from this structure to provide more robust gradient estimates.
    """)

st.markdown("""### 5. Gradient Boosting: LightGBM""")
st.markdown("""
##### a. Overview
LightGBM (Light Gradient Boosting Machine) is a boosting algorithm developed by Microsoft, which is notable for its fast training and low memory consumption.
- Belongs to the Gradient Boosting family, similar to XGBoost and CatBoost.
- Optimized for processing large data and many features.
- Suitable for both regression and classification problems, and is especially good for ranking problems.

##### b. How it Works
LightGBM also builds multiple decision trees incrementally, each learning from the errors of the previous tree ensemble. Key differences from other boosting:
- Leaf-wise tree growth (growing down the branch with the largest loss) → higher accuracy than level-wise like XGBoost.
- Uses Histogram-based algorithm to increase speed and reduce memory.
- Supports Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB) to increase computational efficiency on large datasets.

##### c. Outstanding features
- Fast training, low RAM consumption
- Supports large data, many features
- Supports many problems: classification, regression, ranking
- Integrates well with scikit-learn & pandas
- Can flexibly adjust parameters such as num_leaves, max_depth, learning_rate,...

##### d. When should I use CatBoost?
- When you need to train quickly on big data
- When the data has many features
- When you need a powerful, deeply customizable model
""")
st.markdown("""
##### e. Tree growth example
""")

col5, col6 = st.columns([1, 3])
with col5:
    image4 = Image.open("../images/structure_lightgbm.jpg")
    st.markdown(
        f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(image4)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
                </div>
                """,
        unsafe_allow_html=True)
with col6:
    st.markdown("""
    Tree Growth Mechanism (as seen in the example):

    - Unlike XGBoost's level-wise approach, 
    LightGBM grows trees by always choosing the leaf that will result in the largest reduction in loss (the largest gain) to split. 
    This means it doesn't necessarily grow symmetrically or breadth-first.
    - In the example, after the initial X7 > 0.5 and X3 < 0.33 splits, LightGBM continues splitting the left-most branch with X9 < 3.6 and X6 < 96. 
    Noticeably, the right branch from the X7 split is not further expanded in this illustration, 
    suggesting that splitting its leaves did not yield the highest gain compared to the left branch's leaves.

    Why this approach? This leaf-wise strategy allows LightGBM to find highly effective splits very quickly, often leading to deeper and more complex trees with fewer nodes overall compared to a level-wise approach. This significantly speeds up training, particularly for large datasets. However, because it greedily optimizes, it can be more prone to overfitting if not properly regularized.
    """)

st.markdown("""### 7. Initializing Models""")
tab1, tab2, tab3 = st.tabs(["XGBoost", "CatBoost", "LightGBM"])

with tab1:
    st.code("""
            import xgboost as xgb
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import accuracy_score
            
            # Suppose you have data X, y
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            
            # Model initialization and training
            model = xgb.XGBClassifier()  # Or XGBRegressor() if it is a regression problem
            model.fit(X_train, y_train)
            
            # Forecast
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            print(f"Accuracy: {acc}")
""")

with tab2:
    st.code("""
            from catboost import CatBoostClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import accuracy_score
            
            # Suppose you have data X, y
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            
            # If there are categorical columns, specify their indices.
            cat_features = [0, 2]  # For example, columns 0 and 2 are categorical variables.
            
            # Model initialization and training
            model = CatBoostClassifier(verbose=0)  # verbose=0 to not print log
            model.fit(X_train, y_train, cat_features=cat_features)
            
            # Forecast
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            print(f"Accuracy: {acc}")
""")

with tab3:
    st.code("""
            import lightgbm as lgb
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import accuracy_score
            
            # Suppose you have data X, y
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            
            # Model initialization and training
            model = lgb.LGBMClassifier()
            model.fit(X_train, y_train)
            
            # Forecast
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            print(f"Accuracy: {acc}")
""")

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)