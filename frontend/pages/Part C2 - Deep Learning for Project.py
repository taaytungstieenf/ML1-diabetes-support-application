import streamlit as st
from PIL import Image
import base64
from io import BytesIO

st.set_page_config(page_title="Deep Learning", layout="wide", page_icon="⚕️")

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

st.markdown("### 1. What is Transformer Models?")
st.markdown("""
The Transformer is a neural network architecture introduced in 2017 by Vaswani et al. in the paper "Attention is All You Need". 
Unlike older models like RNN or LSTM (which read sequences one step at a time), Transformers read the entire input all at once.""")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    **Key concepts:**
    - Self-Attention: The model can look at all words in a sentence at the same time and weigh how important each word is for understanding the others.
    - Positional Encoding: Since Transformers don't process words in order, they use special math tricks to inject position (word order) into the model.
    - Multi-Head Attention: Instead of one "attention", the model uses multiple heads to look at different parts of the sentence in parallel.
    - Layer Normalization and Residual Connections: Help the model train faster, stay stable, and improve performance in deep layers.
    
    **Why it's powerful?**
    - No recurrence = faster training
    - Parallelization = better for GPUs
    - Scalable = can be made very large (like GPT-3 or GPT-4)
    """)
with col2:
    image1 = Image.open("../images/ml_models.jpg")
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image1)}" alt="DS vs AI" style="max-width: 90%; height: auto;">
        </div>
        """,
        unsafe_allow_html=True)

st.markdown("### 2. Encoder and Decoder. Why GPT Uses Decoder Only?")
col3, col4 = st.columns(2)

with col3:
    st.markdown("""##### a. Encoder""")
    st.markdown("""
    The encoder is responsible for understanding the input sequence and turning it into a contextualized representation.
    
    **What it does:**
    - Takes an entire input sequence (like a sentence).
    - Applies self-attention: each word attends to all other words in the input.
    - Produces a sequence of embedding vectors that capture meaning, relationships, and context.
    
    **Example use:**
    - BERT uses only the encoder because it’s designed to understand language.
    - Used in tasks like:
        - Sentence classification
        - Question answering
        - Text embeddings
    """)
with col4:
    st.markdown("""##### b. Decoder""")
    st.markdown("""
    The decoder is responsible for generating a new sequence (like translated text, a summary, or future tokens).
    
    **What it does:**
    - Takes the encoder’s output and previously generated tokens.
    - Uses masked self-attention so it doesn’t “see” future tokens.
    - Also attends to the encoder’s outputs (in models like translation).

    **Example use:**
    - GPT uses only the decoder: It generates text from left to right, predicting one token at a time.
    - Used in tasks like:
        - Text generation
        - Translation
        - Summarization (with encoder)
    """)

image2 = Image.open("../images/transformers.jpg")
st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/png;base64,{image_to_base64(image2)}" alt="DS vs AI" style="max-width: 70%; height: auto;">
    </div>
    """,unsafe_allow_html=True)


st.markdown("### 3. The Versions of GPT")
col5, col6 = st.columns(2)
with col5:
    st.markdown("""
    **GPT-2**
    - Open-source (by OpenAI)
    - Comes in sizes: 117M, 345M, 762M, 1.5B parameters
    - Trained on ~40GB of Internet text
    - Basis of DialoGPT
    - Can be fine-tuned on your own data
    
    **GPT-4**
    - Architecture not fully revealed (as of now)
    - Handles text + images
    - Much more accurate, safe, and logical
    - Still not open-source
    - Used via ChatGPT or API
    """)

with col6:
    st.markdown("""
    **GPT-3**
    - 175 billion parameters
    - Can write essays, code, poetry
    - Available only through OpenAI API (not open-source)
    - Cannot be fine-tuned unless you use OpenAI tools (paid)
    - Supports few-shot learning: it can perform tasks with just a few examples provided in the prompt

    **GPT-4o**
    - Multimodal: Understands text, images, audio, and video
    - Faster and cheaper than GPT-4-turbo
    - Can hold real-time conversations
    - Available via ChatGPT (free and Plus), API, and desktop app
    - Architecture details still not public
    """)

st.markdown("### 4. DialoGPT and Fine-Tuning for Diabetes Conversations")
st.markdown("""
DialoGPT is a conversational AI model fine-tuned from GPT-2 on 147M conversations from Reddit. 
It’s designed to generate dialogue-style text, making it more suitable for chatbots.

**Version:**
""")
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
          <th>Version</th>
          <th>Parameters</th>
          <th>Pros</th>
          <th>Cons</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>DialoGPT-small</td>
          <td>~117M</td>
          <td>Fast, low memory use</td>
          <td>Limited expressiveness, may produce short or dull responses</td>
        </tr>
        <tr>
          <td>DialoGPT-medium</td>
          <td>~345M</td>
          <td>Balanced between quality and performance</td>
          <td>Requires more memory and computing power</td>
        </tr>
        <tr>
          <td>DialoGPT-large</td>
          <td>~762M</td>
          <td>Most fluent and human-like responses</td>
          <td>Needs strong GPU and more RAM to run or train</td>
        </tr>
      </tbody>
    </table>
""", unsafe_allow_html=True)


col7, col8 = st.columns(2)
with col7:
    st.markdown("""
    **Why it's good for this project?**
    - Already trained for conversation, not just general text.
    - You don’t have to start from scratch—just fine-tune it on diabetes data.
    - Runs well with Hugging Face Transformers and PyTorch.
    
    **What I need for the next step:**
    - Dataset of real or synthetic dialogues about diabetes
        - Example: Q&A pairs, doctor-patient dialogues, FAQs
        - Can include topics like symptoms, treatment, insulin, diet, etc.
    - Hugging Face Transformers library
    - A training script that loads DialoGPT and trains it on your data
    - Validation data to check how well the chatbot responds
    """)
with col8:
    st.markdown("""
    **My goal to turn DialoGPT into a medical chatbot that:**
    - Answers questions about diabetes
    - Chats like a human, but stays accurate
    - Is friendly, supportive, and helpful
    
    **Standard of chatbot:**
    - Keep your dataset clean and medically accurate
    - Fine-tune slowly to avoid overfitting
    - Test with example questions like:
        - "What is type 1 diabetes?"
        - "How should I manage my blood sugar?"
        - "Can I eat rice if I have diabetes?"
    """)

st.markdown("""### 5. Starting Step for The Project""")
st.code("""
# Step 1: Import Libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Step 2: Load DialoGPT Model and Tokenizer
model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 3: Define Chat Function with Memory (for Gradio)
def chat(user_input, history=[]):
    # Encode input and append EOS token
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Append new input to chat history
    bot_input_ids = torch.cat([history, new_input_ids], dim=-1) if history != [] else new_input_ids

    # Generate a response
    history = model.generate(
        bot_input_ids, max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True, top_k=50, top_p=0.95,
        temperature=0.7
    )

    # Decode and return response and updated history
    response = tokenizer.decode(history[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, history

# Step 4: Build Gradio Chat Interface
gr.ChatInterface(fn=chat).launch()

# Notes:
# - This version uses the pre-trained DialoGPT-small model for general conversations.
# - To specialize it for diabetes, fine-tuning is recommended (see next notebook).
# - Works well for small demos and can be deployed on Hugging Face Spaces or locally.
""")

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)