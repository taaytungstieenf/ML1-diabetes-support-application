import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, f1_score,
    roc_curve, precision_recall_curve, auc, confusion_matrix
)
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os
import time

# 1. Load dataset
df = pd.read_csv("../diabetes_dataset.csv")

# 2. Encode categorical variables
label_encoders = {}
categorical_cols = ['gender', 'smoking_history']
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 3. Split features and target
X = df.drop(columns=['diabetes'])
y = df['diabetes']

# 4. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Train CatBoost model
model = CatBoostClassifier(verbose=0)  # silent training
start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

training_time = end_time - start_time
print(f'Training Time: {training_time:.4f} seconds')

# === Evaluation on training set ===
y_train_pred = model.predict(X_train)
y_train_pred_proba = model.predict_proba(X_train)[:, 1]
train_accuracy = accuracy_score(y_train, y_train_pred)
train_auc = roc_auc_score(y_train, y_train_pred_proba)

print(f"Train Accuracy: {train_accuracy:.4f}")
print(f"Train AUC:      {train_auc:.4f}")

# === Evaluation on test set ===
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, y_pred_proba)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Test Accuracy: {accuracy:.4f}")
print(f"Test AUC:      {roc_auc:.4f}")
print(f"Precision:     {precision:.4f}")
print(f"Recall:        {recall:.4f}")
print(f"F1-score:      {f1:.4f}")

# === Overfitting warning ===
if (train_accuracy - accuracy > 0.1) or (train_auc - roc_auc > 0.1):
    print("\n⚠️  CẢNH BÁO: Mô hình có thể đang bị overfitting!")
else:
    print("\n✅ Không có dấu hiệu rõ ràng của overfitting.")

# 6. Feature importance plot
feature_importances = model.get_feature_importance()
feature_names = X.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names, feature_importances)
plt.xlabel("Importance")
plt.tight_layout()

os.makedirs("metrics", exist_ok=True)
feature_plot_path = os.path.join("metrics", "catboost_feature_importance.png")
plt.savefig(feature_plot_path)
plt.close()
print(f"Feature importance plot saved to: {feature_plot_path}")

# 7. Confusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['No Diabetes', 'Diabetes'],
            yticklabels=['No Diabetes', 'Diabetes'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('CatBoost Confusion Matrix')
plt.tight_layout()

confusion_matrix_path = os.path.join("metrics", "catboost_confusion_matrix.png")
plt.savefig(confusion_matrix_path)
plt.close()
print(f"Confusion matrix plot saved to: {confusion_matrix_path}")

# 8. Save model and encoders
os.makedirs(os.path.join("..", "models"), exist_ok=True)

model_output_path = os.path.join("models", "catboost_model.cbm")
encoders_output_path = os.path.join("models", "catboost_label_encoders.pkl")

model.save_model(model_output_path)
joblib.dump(label_encoders, encoders_output_path)

print(f"Model saved to: {model_output_path}")
print(f"Label encoders saved to: {encoders_output_path}")

# 9. Save evaluation metrics to CSV
metrics_df = pd.DataFrame([{
    "model": "CatBoost",
    "train_accuracy": train_accuracy,
    "train_auc": train_auc,
    "test_accuracy": accuracy,
    "test_auc": roc_auc,
    "precision": precision,
    "recall": recall,
    "f1_score": f1,
    "training_time": training_time
}])

metrics_output_path = os.path.join("metrics", "catboost_metrics.csv")
metrics_df.to_csv(metrics_output_path, index=False)
print(f"Evaluation metrics saved to: {metrics_output_path}")

# 10. Save ROC curve data
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc_val = auc(fpr, tpr)
np.savez_compressed("metrics/catboost_roc.npz", fpr=fpr, tpr=tpr, auc=roc_auc_val)

# 11. Save Precision-Recall curve data
precision_vals, recall_vals, _ = precision_recall_curve(y_test, y_pred_proba)
pr_auc = auc(recall_vals, precision_vals)
np.savez_compressed("metrics/catboost_pr.npz", precision=precision_vals, recall=recall_vals, auc=pr_auc)

print("ROC and PR curve data saved for CatBoost.")
