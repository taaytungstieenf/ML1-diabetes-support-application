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

st.markdown("### 1. What is Deep Learning?")
st.markdown("""
Deep Learning is a specialized and advanced subfield of Machine Learning, 
which focuses on algorithms inspired by the structure and function of the human brain, known as artificial neural networks (ANNs). 
While traditional Machine Learning often requires manual feature engineering and struggles with high-dimensional data, 
Deep Learning enables models to automatically learn hierarchical representations from raw data through multiple layers of abstraction.
""")
cola, colb = st.columns(2)
with cola:
    st.markdown("""
    **Key ideas:**
    - Learns features automatically from raw data using hierarchical layers
    - Can model non-linear, high-dimensional relationships
    - Requires large datasets and computational resources
    - Each layer in the network extracts increasingly abstract representations of the data
    
    **Applications include:**
    - Computer vision (e.g. facial recognition, object detection)
    - Speech recognition (e.g. voice assistants)
    - Natural language processing (e.g. language translation, sentiment analysis)
    - Autonomous systems (e.g. self-driving cars, robotics)
    """)

with colb:
    image1 = Image.open("../images/deep_learning.jpg")
    st.markdown(
        f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image1)}" alt="Deep Learning Neural Network" style="width: 400px; height: auto; border-radius: 10px;">
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("### 2. Fundamental Neural Network")
col1, col2 = st.columns(2)
with col1:
    st.markdown("##### a. Artificial Neural Network (ANN)")
    st.markdown("""
    **Purpose:** Predicting sales, detecting fraud, binary classification tasks, etc.
    
    **Structure:**
    - Input layer: Receives the raw data.
    - Hidden layers: Perform computations and extract patterns through multiple layers.
    - Output layer: Produces the final prediction.
    
    **Key characteristics:**
    - Can model non-linear relationships.
    - Works well with tabular data and basic prediction/classification tasks.
    - Requires careful tuning (number of layers, neurons, learning rate, etc.).
    
    **Activation function:**
    """)
    st.latex(r"ReLU(x) = \max(0, x)")
    st.latex(r"""
        x: \text{Input value of a node (neuron)} \\
        ReLU(x): \text{Output value after applying ReLU function} \\
        """)
    st.markdown("""
    **Architecture:**
    """)
    image2 = Image.open("../images/network_ann.jpg")
    st.markdown(
        f"""
                <div style="text-align: center;">
                    <img src="data:image/png;base64,{image_to_base64(image2)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
                </div>
                """,
        unsafe_allow_html=True)

with col2:
    st.markdown("##### b. Convolutional Neural Network (CNN)")
    st.markdown("""
**Purpose:** Image recognition and processing

**Structure:**
- Convolutional layers: Apply filters to extract features from small regions of the image.
- Pooling layers: Downsample feature maps to reduce dimensionality and computation.
- Fully connected layers: Combine extracted features for final classification.

**Key characteristics:**
- Automatically learns spatial hierarchies of patterns.
- Requires fewer parameters than traditional ANNs when handling large images.
- More robust to translation and distortion in images.

**Example layer output formula:**
""")
    st.latex(r"(I * K)(x, y) = \sum_m \sum_n I(m, n) \cdot K(x - m, y - n)")
    st.latex(r"""
    I: \text{Input image (matrix)} \\
    K: \text{Filter (kernel)} \\
    x, y: \text{Output pixel coordinates} \\
    m, n: \text{Coordinates in filter} \\
    \cdot: \text{Element-wise multiplication}
    """)

    st.markdown("""
       **Architecture:**
       """)
    image3 = Image.open("../images/network_cnn.jpg")
    st.markdown(
        f"""
                   <div style="text-align: center;">
                       <img src="data:image/png;base64,{image_to_base64(image3)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
                   </div>
                   """,
        unsafe_allow_html=True)

st.markdown("### 3. Neural Networks for Sequence Data")

col1, col2 = st.columns(2)

with col1:
    st.markdown("##### a. Recurrent Neural Network (RNN)")
    st.markdown("""
    Recurrent Neural Networks (RNNs) are a class of neural networks designed to process sequential data, where the order of inputs matters. 
    Unlike traditional feedforward networks, RNNs have loops in their architecture that allow information to persist across time steps.
    
    **Key idea:** 
    - Keeps memory across steps to capture sequence context.
    - Good for time series, text, speech, and audio tasks.
    - Struggles with long-term patterns (vanishing gradient).
    - Processes input one element at a time in order.
        
    **RNN formular:**
    """)
    st.latex(r"h_t = \tanh(W_h h_{t-1} + W_x x_t + b)")
    st.latex(r"""
        h_t: \text{hidden state at time t} \\
        x_t: \text{input at time t} \\
        W_h, W_x: \text{weight matrices} \\
        b: \text{bias term} \\
        """)

with col2:
    st.markdown("##### b. Long Short-Term Memory (LSTM)")
    st.markdown("""
    LSTM is an advanced version of RNN, designed to learn long-term dependencies in sequences. 
    It introduces a memory cell and a set of gates that control the flow of information—what to keep, what to forget, and what to output.
    
    **Key components:** 
    - Forget gate: decides what information to discard
    - Input gate: decides what new information to store
    - Output gate: decides what information to output
    - Cell state: acts as memory through time

    **Core formular:**
    """)
    st.latex(r"c_t = f_t \cdot c_{t-1} + i_t \cdot \tilde{c}_t")
    st.latex(r"""
            f_t: \text{forget gate} \\
            i_t: \text{input gate} \\
            o_t: \text{output gate} \\
            c_t: \text{cell gate}
            """)

st.markdown("##### c. Gated Recurrent Unit (GRU)")
st.markdown("""
        Gated Recurrent Unit (GRU) is a variant of LSTM that also aims to capture long-term dependencies in sequential data but with a simpler architecture. 
        GRUs combine the forget and input gates into a single update gate, 
        and they merge the cell state and hidden state, making the model more computationally efficient.
        """)
cole, colf = st.columns(2)
with cole:
    st.markdown("""
    **Key components:** 
    - Update gate: decides how much past information to keep
    - Reset gate: controls how much of the past to forget
    - Hidden state: directly carries the memory, no separate cell state
        """)

with colf:
    st.markdown("""
    **Key advantages:**
    - Simpler than LSTM (fewer gates and parameters)
    - Comparable performance on many sequence tasks
    - Faster to train and easier to tune
    """)

st.markdown("""**GRU formular:**""")
cola, colb, colc, cold = st.columns(4)
with cola:
        st.latex(r"z_t = \sigma(W_z x_t + U_z h_{t-1} + b_z)")
with colb:
        st.latex(r"r_t = \sigma(W_r x_t + U_r h_{t-1} + b_r)")
with colc:
        st.latex(r"\tilde{h}_t = \tanh(W_h x_t + U_h (r_t \odot h_{t-1}) + b_h)")
with cold:
        st.latex(r"h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t")

colg, colh = st.columns(2)
with colg:
    st.latex(r"""
        z_t: \text{update gate} \\
        r_t: \text{reset gate} \\
        \tilde{h}_t: \text{candidate hidden state} \\
        h_t: \text{new hidden state} \\
        """)
with colh:
    st.latex(r"""
            \sigma: \text{sigmoid function} \\
            \odot: \text{element-wise multiplication} \\
            W, U: \text{weight matrices} \\
            b: \text{bias terms}
            """)

st.markdown("""##### d. Architecture""")
image4 = Image.open("../images/rnn-lstm-gru-transformers.jpg")
st.markdown(
    f"""
        <div style="text-align: center;">
            <img src="data:image/png;base64,{image_to_base64(image4)}" alt="DS vs AI" style="max-width: 100%; height: auto;">
        </div>
    """,
        unsafe_allow_html=True)

# Section 4: Model Initialization
st.markdown("### 4. Initializing Deep Learning Models")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Artificial Neural Network (ANN)", "Convolutional Neural Network (CNN)", \
                                        "Recurrent Neural Network (Simple RNN)", "Long Short-Term Memory (LSTM)", \
                                        "Gated Recurrent Unit (GRU)"])

with tab1:
    st.code("""
        import tensorflow as tf
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Dense

        model = Sequential([
            Dense(32, activation='relu', input_shape=(10,)),
            Dense(16, activation='relu'),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    """)

with tab2:
    st.code("""
        import tensorflow as tf
        from tensorflow.keras.models import Sequential
        from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

        model = Sequential([
            Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(64, 64, 1)),
            MaxPooling2D(pool_size=(2, 2)),
            Flatten(),
            Dense(64, activation='relu'),
            Dense(10, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    """)
with tab3:
    st.code("""
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import SimpleRNN, Dense
    
    model_rnn = Sequential([
        SimpleRNN(64, input_shape=(10, 8)),  # 10 time steps, 8 features
        Dense(1, activation='sigmoid')
    ])
    model_rnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    """)
with tab4:
    st.code("""
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import LSTM, Dense
    
    model_lstm = Sequential([
        LSTM(64, input_shape=(10, 8)),  # 10 time steps, 8 features
        Dense(1, activation='sigmoid')
    ])
    model_lstm.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    """)
with tab5:
    st.code("""
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import GRU, Dense
    
    model_gru = Sequential([
        GRU(64, input_shape=(10, 8)),  # 10 time steps, 8 features
        Dense(1, activation='sigmoid')
    ])
    model_gru.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    """)

st.markdown("""<div class="footer">© 2025 Nguyễn Đức Tây | All rights reserved.</div>""", unsafe_allow_html=True)