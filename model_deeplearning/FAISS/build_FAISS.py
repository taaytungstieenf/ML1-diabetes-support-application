import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

# Load Q&A pairs
df = pd.read_csv("data/qa_pairs.csv")

# Load sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Encode the questions
embeddings = model.encode(df["question"].tolist(), show_progress_bar=True)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings).astype("float32"))

# Save index and data
faiss.write_index(index, "faiss_index.bin")
df.to_pickle("qa_data.pkl")
with open("model/embedding_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ FAISS index and data saved.")
