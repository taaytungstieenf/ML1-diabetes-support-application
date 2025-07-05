import json
import pandas as pd

# Load your JSON file
with open("../../diabetes_dialogues.json", "r", encoding="utf-8") as f:
    data = json.load(f)

pairs = []

# Loop through each conversation
for convo in data["conversations"]:
    # Ensure it has at least 2 turns
    for i in range(0, len(convo) - 1, 2):
        user_input = convo[i]
        bot_reply = convo[i + 1]
        pairs.append({"question": user_input.strip(), "answer": bot_reply.strip()})

# Convert to DataFrame and save
df = pd.DataFrame(pairs)
df.to_csv("qa_pairs.csv", index=False, encoding="utf-8")
print(f"Saved {len(df)} Q&A pairs to qa_pairs.csv")
