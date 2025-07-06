# DIABETES SUPPORT APPLICATION

### A. Project Introduction

The Diabetes Support Application is a comprehensive health-tech solution designed to help individuals in managing and understanding diabetes. 
This application integrates advanced machine learning and natural language processing (NLP) techniques to deliver both predictive insights and interactive support for users.

##### 1. Diabetes prediction module
This module utilizes the latest Gradient Boosting algorithms: CatBoost, LightGBM, XGBoost. 
These models are trained on health-related features to predict the likelihood of diabetes in users. 
[OMIT] ensemble learning ensures high prediction accuracy, model interpretability, and performance across diverse datasets.

##### 2. Interactive diabetes chatbot
The chatbot component combines: FAISS for fast vector similarity search using embedding-based semantic retrieval, 
DialoGPT for generating natural and contextual responses.
This allows users to ask questions related to diabetes and receive accurate, conversational, and medically relevant responses in real-time.

##### 3. Objective
By combining predictive modeling and conversational AI, this application aims to:
- Provide early detection support through accurate predictions.
- Educate and help users with an interactive chatbot.
- Empower patients and caregivers with accessible diabetes knowledge.

---
### B. Project Structure

```
./ML1-diabetes-support-application
|
|______ ./venv
|
|______ ./backend
|       |______ assessment.py
|
|______ ./database
|       |______ __init__.py
|       |______ database_config.py
|       |______ database_functions.py
|
|______ ./frontend
|       |______ ./pages
|       |       |______ Part A1 - Artificial Intelligence.py
|       |       |______ Part A2 - Diabetes Information.py
|       |       |______ Part B1 - Machine Learning.py
|       |       |______ Part B2 - Machine Learning for Project.py
|       |       |______ Part C1 - Deep Learning.py
|       |       |______ Part C2 - Deep Learning for Project.py
|       |       |______ Part D1 - Datasets Introduction.py
|       |       |______ Part D2 - Exploratory Data Analysis.py
|       |       |______ Part E1 - ML Model Evaluation.py
|       |       |______ Part E2 - DL Model Evaluation.py
|       |       |______ Part F1 - Diabetic Risk Assessment.py
|       |       |______ Part F2 - Metrics Visualization.py
|       |       |______ Part F3 - Retrieval-Based & AI Chatbot.py
|       |______ Home.py
|
|______ ./images
|       |______ network_ann.jpg
|       |______ network_cnn.jpg
|       |______ structure_catboost.jpg
|       |______ structure_lightgbm.jpg
|       |______ structure_xgboost.jpg
|       |______ ...
|
|______ ./model_deeplearning
|       |______ ./dialoGPT
|       |       |______ ./data
|       |       |       |______ processed_dialogues.txt
|       |       |______ ./model
|       |       |       |______ config.json
|       |       |       |______ generation_config.json
|       |       |       |______ tokenizer.json
|       |       |       |______ tokenize_config.json
|       |       |       |______ ...
|       |       |______ preprocess_data.py
|       |       |______ train_dialoGPT.py
|       |
|       |______ ./FAISS
|               |______ ./data
|               |       |______ qa_pairs.csv
|               |______ ./model
|               |       |______ embedding_model.pkl
|               |       |______ faiss_index.bin
|               |       |______ qa_data.pkl
|               |______ build_faiss.py
|               |______ preprocess_data.py
|
|______ ./model_machinelearning
|       |______ ./metrics
|       |       |______ catboost_confusion_matrix.png
|       |       |______ catboost_feature_important.png
|       |       |______ catboost_metrics.csv
|       |       |______ catboost_pr.npz
|       |       |______ catboost_roc.npz
|       |       |______ lightgbm_confusion_matrix.png
|       |       |______ lightgbm_feature_important.png
|       |       |______ lightgbm_metrics.csv
|       |       |______ lightgbm_pr.npz
|       |       |______ lightgbm_roc.npz
|       |       |______ xgboost_confusion_matrix.png
|       |       |______ xgboost_feature_important.png
|       |       |______ xgboost_metrics.csv
|       |       |______ xgboost_pr.npz
|       |       |______ xgboost_roc.npz
|       |
|       |______ ./models
|       |       |______ catboost_label_encoders.pkl
|       |       |______ catboost_model.cbm
|       |       |______ lightgbm_label_encoders.pkl
|       |       |______ lightgbm_model.pkl
|       |       |______ xgboost_label_encoders.pkl
|       |       |______ xgboost_model.pkl
|       |______ catboost_model.py
|       |______ lightgbm_model.py
|       |______ xgboost_model.py
|
|______ ./processing_data_for_chatbots
|       |______ ./data
|       |       |______ cleaned_output.txt
|       |       |______ DM Dialogs.xlsx
|       |       |______ dm_dialogs.csv
|       |       |______ dm_dialogs.txt
|       |______ data_manipulation.py
|       |______ diabetes_dialogues.json
|       |______ structured_dialogue.json
|
|______ .gitignore
|______ diabetes_dataset.csv
|______ diabetes_dialogues.json
|______ main.py
|______ README.md
|______ requirements.txt

```
---

### C. Core Technologies Recap

- Backend: Built using Flask to handle requests and serve machine learning predictions.
- Database: Managed with MySQL for storing user data and prediction logs.
- Frontend: An interactive user interface developed with Streamlit.
- Machine Learning Models: Implemented XGBoost, LightGBM, and CatBoost to predict diabetes risk.
- Deep Learning Chatbot: A conversational chatbot built using the DialoGPT model, fine-tuned on data.
- Retrieval-based Chatbot: A question-answering system powered by FAISS for fast and information retrieval.
- Evaluation Tools: Visualization of accuracy, confusion matrix, and feature importance for model assessment.
- Machine Learning Comparison: ROC & Precision-Recall curves.

---

### D. Project Installation

```bash
# Step 1 - Clone repo
$ git clone https://github.com/taaytungstieenf/ML1-diabetes-support-application.git

# Step 2 - Delete current virtual environment 
$ cd ML1-diabetes-support-application
$ rm -r .venv

# Step 3 - Create new virtual environment
$ python -m venv venv
$ source venv/bin/activate

# Step 4 - Install libraries into new .venv
$ pip install -r requirements.txt

# Step 4 - Config MySQL database
$ cd database
$ python3 database_functions.py 

# Step 5 - Train Deep Learning model by yourself (because of limitation of GitHub upload capacity)
$ cd ../model_deeplearning/dialoGPT; python3 train_dialoGPT.py      # ETA: 30 minutes
$ cd ../FAISS; python3 build_FAISS.py                               # ETA: 15 minutes

# Step 6 - Initialize backend
$ cd ../..; python3 main.py

# Step 7 - Initialize frontend
$ cd frontend; streamlit run HOME.py
```

---

### E. Notes

In case of you guys get confused:
- The final dataset for diabetes prediction is `diabetes_dataset.csv`.
- The final dataset for diabetes chatbots is `diabetes_dialogue.json`.
- When developed frontend, I used a lot of icons in code to make the UI less bland.
- This project was completed with the help of ChatGPT but not much, please respect the author.
- If you want to use this project, then feel free to use it, no need to contact me.

---

### F. About Author

- Name: Nguyễn Đức Tây
- University / major: HCMC University of Techology and Education / Data Engineering
- Degree: Bachelor of Science in Data Engineering
- Email: nguyenductay121999@gmail.com
- Last modified date: 05/07/2025

<p align="center">
    <img src="https://i.pinimg.com/originals/98/4e/81/984e81934046c3050464525dfcacb6bc.gif" width="800"/>
</p>

