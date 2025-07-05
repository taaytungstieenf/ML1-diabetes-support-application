import json
import os

with open("../../../diabetes_dialogues.json", "r") as f:
    data = json.load(f)["conversations"]

os.makedirs("data", exist_ok=True)

with open("data/processed_dialogues.txt", "w") as f:
    for conv in data:
        if len(conv) < 4:
            continue
        formatted = ""
        for i, utterance in enumerate(conv):
            speaker = "<|user|>" if i % 2 == 0 else "<|bot|>"
            formatted += f"{speaker} {utterance.strip()} "
        f.write(formatted.strip() + "\n")
