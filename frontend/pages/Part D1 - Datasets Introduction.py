import streamlit as st
import pandas as pd
import io

# --- Page configuration ---
st.set_page_config(page_title="Introduction", layout="wide", page_icon="⚕️")

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

# --- Initialize state ---
if "uploaded_file_obj" not in st.session_state:
    st.session_state["uploaded_file_obj"] = None
    st.session_state["preview_data"] = None
    st.session_state["summary_data"] = None

# --- Data processing ---
def process_file(file_io, file_type):
    if file_type == "csv":
        df = pd.read_csv(file_io)
    elif file_type == "json":
        df = pd.read_json(file_io)
    else:
        raise ValueError("❌ Unsupported file format.")

    preview = df.head(15).to_dict(orient="records")
    summary = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "describe": df.describe(include='all').fillna("").to_dict()
    }
    return preview, summary

# --- File upload ---
uploaded_file = st.sidebar.file_uploader("", type=["csv", "json"], key="file_uploader")

if uploaded_file is not None and uploaded_file != st.session_state["uploaded_file_obj"]:
    st.session_state["uploaded_file_obj"] = uploaded_file
    st.cache_data.clear()
    try:
        file_type = uploaded_file.name.split(".")[-1].lower()
        file_bytes = uploaded_file.read()
        file_io = io.BytesIO(file_bytes)
        preview, summary = process_file(file_io, file_type)
        st.session_state["preview_data"] = preview
        st.session_state["summary_data"] = summary
    except Exception as e:
        st.error(f"❌ File processing error: {e}")
        st.session_state["preview_data"] = None
        st.session_state["summary_data"] = None

# --- Display data ---
preview = st.session_state["preview_data"]
summary = st.session_state["summary_data"]

if preview or summary:
    tab1, tab2, tab3 = st.tabs([
        "📄 Data Preview",
        "🆔 Column Names & Data Types",
        "📊 Summary Statistics"
    ])

    with tab1:
        if preview:
            st.dataframe(pd.DataFrame(preview), use_container_width=True, height=600)
        else:
            st.info("⏳ No preview data available.")

    with tab2:
        if summary:
            st.markdown(
                f"**🔢 Rows:** `{summary['num_rows']}` &nbsp; "
                f"**🔠 Columns:** `{summary['num_columns']}`",
                unsafe_allow_html=True
            )
            col_info = pd.DataFrame({
                "Column Name": summary["columns"],
                "Data Type": [summary["dtypes"].get(col, "Unknown") for col in summary["columns"]]
            })
            st.dataframe(col_info, use_container_width=True)
        else:
            st.info("⏳ No summary data available.")

    with tab3:
        if summary:
            st.dataframe(pd.DataFrame(summary["describe"]), use_container_width=True, height=420)
        else:
            st.info("⏳ No summary data available.")
else:
    st.info("⏳ Please upload a CSV or JSON file.")

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)
