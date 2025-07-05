"""
We have 2 types of data of diabetes
    Type 1: 200 Q&A pairs in cleaned_output.txt
    Type 2: A long chat between doctor and patient in "DM Dialogs.xlsx"

IDEA
    Step 1: extract data from "DM Dialogs.xlsx" to dm_dialogs.txt
    Step 2: turn dm_dialogs.txt to JSON format in structured_dialogue.json
    Step 3: Combine cleaned_output.txt and structured_dialogue.json to get diabetes_dialogues.json.
"""

# Step 1: extract data from "DM Dialogs.xlsx" to dm_dialogs.txt
#   $ pip install csvkit
#   $ in2csv "DM Dialogs.xlsx" > dm_dialogs.csv
#   $ csvlook dm_dialogs.csv
#   $ csvcut -c 1 dm_dialogs.csv > dm_dialogs.txt.


# Step 2: turn dm_dialogs.txt to JSON format in structured_dialogue.json
import json
import random
import os

input_path = "data/dm_dialogs.txt"  # Your raw conversation text file
output_path = "structured_dialogue.json"    # Output JSON file

speakers = ["Doctor", "Patient"]

with open(input_path, "r", encoding="utf-8") as f:
    raw_lines = f.readlines()
    lines = [line.strip() for line in raw_lines if line.strip()]  # Remove blank lines and trim spaces

dialogue_data = {
    "dialogue_id": "conv1",
    "turns": []
}

for i, line in enumerate(lines):
    speaker = speakers[i % 2]  # Alternate speakers
    dialogue_data["turns"].append({
        "speaker": speaker,
        "text": line
    })

with open(output_path, "w", encoding="utf-8") as f:
    json.dump([dialogue_data], f, ensure_ascii=False, indent=2)

print(f"Saved structured conversation to {output_path}")

# Step 3: Combine cleaned_output.txt and structured_dialogue.json to get diabetes_dialogues.json.
def parse_cleaned_output():
    conversations = []
    with open("data/cleaned_output.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    i = 0
    while i < len(lines) - 1:
        q = lines[i]
        a = lines[i + 1]
        conversations.append(["Hi!", "Hello, how can I help?", q, a])
        i += 2
    return conversations

def parse_structure_dialogue():
    conversations = []
    with open("structured_dialogue.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    for dialogue in data:
        turns = [turn["text"].strip('" ') for turn in dialogue["turns"]]
        if len(turns) >= 2:
            conversations.append(turns)
    return conversations

def combine_and_save():
    type1 = parse_cleaned_output()
    type2 = parse_structure_dialogue()
    all_conversations = type1 + type2
    random.shuffle(all_conversations)

    output = {"conversations": all_conversations}
    output_file = "diabetes_dialogues.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    if os.path.exists(output_file):
        print(f"✅ Success: Created '{output_file}' with {len(all_conversations)} conversations.")
    else:
        print("❌ Error: File not created.")

if __name__ == "__main__":
    combine_and_save()