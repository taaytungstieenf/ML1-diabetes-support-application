import os
import faiss
import pickle
import torch
import numpy as np
import pandas as pd
import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
from sentence_transformers import SentenceTransformer

# --- Paths ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FAISS_MODEL_DIR = os.path.join(BASE_DIR, "model_deeplearning", "FAISS", "model")
DIALOGPT_MODEL_PATH = os.path.join(BASE_DIR, "model_deeplearning", "dialoGPT", "model")

FAISS_PATH = os.path.join(FAISS_MODEL_DIR, "faiss_index.bin")
QA_DATA_PATH = os.path.join(FAISS_MODEL_DIR, "qa_data.pkl")
EMBEDDING_MODEL_PATH = os.path.join(FAISS_MODEL_DIR, "embedding_model.pkl")

# --- Load models and data for Retrieval-based Chatbot ---
index = faiss.read_index(FAISS_PATH)
df = pd.read_pickle(QA_DATA_PATH)
with open(EMBEDDING_MODEL_PATH, "rb") as f:
    embedding_model = pickle.load(f)

# --- Load DialoGPT model ---
dialogpt_tokenizer = AutoTokenizer.from_pretrained(DIALOGPT_MODEL_PATH)
dialogpt_model = AutoModelForCausalLM.from_pretrained(DIALOGPT_MODEL_PATH)

# --- Page settings ---
st.set_page_config(page_title="Chatbots", layout="wide", page_icon="⚕️")
st.markdown("""
    <style>
        .block-container {
            padding-top: 0rem !important; /* remove default top padding */
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

# --- Split into 2 columns ---
col1, col2 = st.columns(2)

# === LEFT CHATBOT – Retrieval-Based ===
with col1:
    st.subheader("🤖 Chatbot 1: Retrieval-Based (FAISS)")
    if "retrieval_history" not in st.session_state:
        st.session_state["retrieval_history"] = []

    user_input_left = st.text_input("", key="input_left", placeholder="Ask something about diabetes...")

    if user_input_left:
        query_vector = embedding_model.encode([user_input_left])
        D, I = index.search(np.array(query_vector).astype("float32"), k=1)
        response = df.iloc[I[0][0]]["answer"]

        st.session_state["retrieval_history"].append(("You", user_input_left))
        st.session_state["retrieval_history"].append(("Bot", response))

    for speaker, msg in st.session_state["retrieval_history"]:
        st.markdown(f"**{speaker}:** {msg}")

# === RIGHT CHATBOT – DialoGPT ===
with col2:
    st.subheader("🤖 Chatbot 2: Generative (DialoGPT)")
    if "dialogpt_history" not in st.session_state:
        st.session_state["dialogpt_history"] = None

    user_input_right = st.text_input("", key="input_right", placeholder="Ask a question...")

    if user_input_right:
        input_ids = dialogpt_tokenizer.encode(f"<|user|> {user_input_right} <|bot|>", return_tensors="pt")
        full_input = (
            torch.cat([st.session_state["dialogpt_history"], input_ids], dim=-1)
            if st.session_state["dialogpt_history"] is not None
            else input_ids
        )

        # 🔧 Limit input length to avoid generate() errors
        MAX_LENGTH = 800
        if full_input.shape[-1] > MAX_LENGTH:
            full_input = full_input[:, -MAX_LENGTH:]

        output_ids = dialogpt_model.generate(
            full_input,
            max_length=1000,
            pad_token_id=dialogpt_tokenizer.eos_token_id
        )

        response = dialogpt_tokenizer.decode(
            output_ids[:, full_input.shape[-1]:][0],
            skip_special_tokens=True
        )

        st.session_state["dialogpt_history"] = output_ids
        st.markdown(f"**Bot:** {response}")

st.markdown("""<div class="footer">© 2025 Nguyen Duc Tay | All rights reserved.</div>""", unsafe_allow_html=True)
