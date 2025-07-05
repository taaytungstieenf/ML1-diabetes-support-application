import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json

st.set_page_config(page_title="EDA", layout="wide", page_icon="⚕️",)

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

# --- File uploader ---
uploaded_file = st.sidebar.file_uploader("", type=["csv", "json"])

if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    st.session_state.uploaded_file = uploaded_file

    try:
        if file_type == "csv":
            df = pd.read_csv(uploaded_file)

            # Cast data types
            for col in ["gender", "hypertension", "diabetes", "smoking_history", "heart_disease"]:
                if col in df.columns:
                    df[col] = df[col].astype('category')
            for col in ["age", "blood_glucose_level"]:
                if col in df.columns:
                    df[col] = df[col].astype('int64')

        elif file_type == "json":
            raw = json.load(uploaded_file)
            convos = raw["conversations"]

            qa_pairs = []
            for convo in convos:
                for i in range(len(convo) - 1):
                    q, a = convo[i].strip(), convo[i + 1].strip()
                    if q.endswith("?"):
                        qa_pairs.append({"question": q, "answer": a})
            df = pd.DataFrame(qa_pairs)

        st.session_state.df = df

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
        st.stop()
else:
    if "df" not in st.session_state or st.session_state.df is None:
        st.info("⏳ Please upload a CSV or JSON file.")
        st.stop()

df = st.session_state.df

# --- Check for conversational data ---
if set(df.columns) == {"question", "answer"}:
    st.subheader("📄 Detected conversational JSON file")
    st.dataframe(df)
    df["question_length"] = df["question"].apply(len)
    df["answer_length"] = df["answer"].apply(len)

    with st.expander("📊 Length statistics of questions and answers"):
        col1, col2 = st.columns(2)
        with col1:
            st.write(df["question_length"].describe())
            fig, ax = plt.subplots()
            sns.histplot(df["question_length"], bins=20, kde=True, ax=ax)
            ax.set_title("Distribution of question lengths")
            st.pyplot(fig)

        with col2:
            st.write(df["answer_length"].describe())
            fig, ax = plt.subplots()
            sns.histplot(df["answer_length"], bins=20, kde=True, ax=ax)
            ax.set_title("Distribution of answer lengths")
            st.pyplot(fig)

    st.stop()

# --- EDA Menu (for tabular/csv) ---
chart_choice = st.sidebar.radio("",
    (
        "Chart 1 – Category Histogram",
        "Chart 2 – Numerical Histogram",
        "Chart 3 – Numerical Outliers Boxplot",
        "Chart 4 – Cat vs Num Boxplot",
        "Chart 5 – Significances Scatterplot",
        "Chart 6 – Correlation Heatmap"
    )
)

col1, col2, col3, col4 = st.columns([1, 0.15, 1.75, 0.15])

with col1:
    st.markdown("<h3 style='text-align: center; color: #21130d;'>📋 Data Types</h3>", unsafe_allow_html=True)
    st.dataframe(df.dtypes.reset_index().rename(columns={"index": "Column Name", 0: "Data Type"}))

# --- EDA Charts ---
if chart_choice == "Chart 1 – Category Histogram":
    with col3:
        cat_columns = df.select_dtypes(include=['category']).columns.tolist()
        selected_col = st.selectbox("", cat_columns)
        st.write(f"### Distribution of `{selected_col}`")

        fig, ax = plt.subplots()
        sns.countplot(x=selected_col, data=df, ax=ax)
        plt.xticks(rotation=0)
        st.pyplot(fig)

    with col1:
        st.markdown("<h3 style='text-align: center; color: #21130d;'>📋 Attribute Statistics</h3>", unsafe_allow_html=True)
        st.write(df[selected_col].value_counts())

elif chart_choice == "Chart 2 – Numerical Histogram":
    with col3:
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        selected_num_col = st.selectbox("", num_cols)
        st.write(f"### Distribution of `{selected_num_col}`")

        fig, ax = plt.subplots()
        sns.histplot(df[selected_num_col], kde=True, ax=ax)
        st.pyplot(fig)

    with col1:
        st.markdown("<h3 style='text-align: center; color: #21130d;'>📋 Attribute Statistics</h3>", unsafe_allow_html=True)
        st.write(df[selected_num_col].describe())

elif chart_choice == "Chart 3 – Numerical Outliers Boxplot":
    with col3:
        num_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
        selected_num_col = st.selectbox("", num_cols)
        st.write(f"### Boxplot of `{selected_num_col}`")

        fig, ax = plt.subplots()
        sns.boxplot(x=df[selected_num_col], ax=ax)
        st.pyplot(fig)

    with col1:
        st.markdown("<h3 style='text-align: center; color: #21130d;'>📋 Attribute Statistics</h3>", unsafe_allow_html=True)
        st.write(df[selected_num_col].describe())

elif chart_choice == "Chart 4 – Cat vs Num Boxplot":
    with col1:
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        cat_cols = df.select_dtypes(include='category').columns.tolist()
        selected_y = st.selectbox("Select numerical attribute", num_cols)
        selected_x = st.selectbox("Select categorical attribute", cat_cols)

    with col3:
        st.write(f"### Boxplot: `{selected_y}` by `{selected_x}`")

        fig, ax = plt.subplots()
        sns.boxplot(x=selected_x, y=selected_y, data=df, ax=ax)
        plt.xticks(rotation=0)
        st.pyplot(fig)

elif chart_choice == "Chart 5 – Significances Scatterplot":
    with col1:
        cat_cols = df.select_dtypes(include='category').columns.tolist()
        hue_col = st.selectbox("Select hue category", ["(Click to choose)"] + cat_cols)
        num_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        y_col = st.selectbox("Select numeric attribute", [col for col in num_cols if col != 'age'])

    with col3:
        fig, ax = plt.subplots()
        if hue_col != "(Click to choose)":
            sns.scatterplot(data=df, x="age", y=y_col, hue=hue_col, ax=ax)
            st.write(f"### Scatter: `age` vs `{y_col}` by `{hue_col}`")
        else:
            sns.scatterplot(data=df, x="age", y=y_col, ax=ax)
            st.write(f"### Scatter: `age` vs `{y_col}`")
        st.pyplot(fig)

elif chart_choice == "Chart 6 – Correlation Heatmap":
    with col3:
        fig4, ax4 = plt.subplots(figsize=(10, 6))
        sns.heatmap(
            df.select_dtypes(include=['float64', 'int64']).corr(),
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            ax=ax4
        )
        ax4.set_yticklabels(ax4.get_yticklabels(), rotation=360)
        st.pyplot(fig4)

    st.markdown("### 🔎 Observations:")
    st.markdown("- `bmi` has the highest correlation with `age` because people tend to gain weight as they get older.")
    st.markdown("- `HbA1c_level` has the second-highest correlation with `blood_glucose_level` because it is directly related to blood sugar levels.")

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)
