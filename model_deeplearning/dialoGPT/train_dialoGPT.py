# model_deeplearning/train_dialoGPT.py
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
import os

dataset = load_dataset("text", data_files={"train": "data/processed_dialogues.txt"})

model_name = "microsoft/DialoGPT-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

def tokenize(batch):
    inputs = tokenizer(batch["text"], truncation=True, padding="max_length", max_length=512)
    inputs["labels"] = inputs["input_ids"].copy()
    return inputs


tokenized = dataset["train"].map(tokenize, batched=True)
tokenized.set_format("torch")

args = TrainingArguments(
    output_dir="model",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=50,
    save_steps=100,
    save_total_limit=2,
)

trainer = Trainer(model=model, args=args, train_dataset=tokenized)
trainer.train()
trainer.save_model("model")
tokenizer.save_pretrained("model")
