import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, precision_recall_curve, auc
)
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import os
import time
import numpy as np

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

# 5. Train model
model = xgb.XGBClassifier(eval_metric='logloss', use_label_encoder=False)

start_time = time.time()
model.fit(X_train, y_train)
end_time = time.time()

training_time = end_time - start_time
print(f'Training Time: {training_time:.4f} seconds')

# === Overfitting check: Evaluate on training set ===
y_train_pred = model.predict(X_train)
y_train_pred_proba = model.predict_proba(X_train)[:, 1]
train_accuracy = accuracy_score(y_train, y_train_pred)
train_roc_auc = roc_auc_score(y_train, y_train_pred_proba)
print(f"Train Accuracy: {train_accuracy:.4f}")
print(f"Train AUC:      {train_roc_auc:.4f}")

# 6. Evaluation on test set
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

# Overfitting warning
if (train_accuracy - accuracy > 0.1) or (train_roc_auc - roc_auc > 0.1):
    print("\n⚠️  CẢNH BÁO: Mô hình có thể đang bị overfitting!")
else:
    print("\n✅ Không có dấu hiệu rõ ràng của overfitting.")

# 7. Feature importance plot
feature_importances = model.feature_importances_
feature_names = X.columns

plt.figure(figsize=(10, 6))
plt.barh(feature_names, feature_importances)
plt.xlabel("Importance")
plt.tight_layout()

os.makedirs("metrics", exist_ok=True)
feature_plot_path = os.path.join("metrics", "xgboost_feature_importance.png")
plt.savefig(feature_plot_path)
plt.close()
print(f"Feature importance plot saved to: {feature_plot_path}")

# 8. Confusion matrix plot
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['No Diabetes', 'Diabetes'],
            yticklabels=['No Diabetes', 'Diabetes'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('XGBoost Confusion Matrix')
plt.tight_layout()

confusion_matrix_path = os.path.join("metrics", "xgboost_confusion_matrix.png")
plt.savefig(confusion_matrix_path)
plt.close()
print(f"Confusion matrix plot saved to: {confusion_matrix_path}")

# 9. Save model and encoders
os.makedirs(os.path.join("..", "models"), exist_ok=True)

model_output_path = os.path.join("models", "xgboost_model.pkl")
encoders_output_path = os.path.join("models", "xgboost_label_encoders.pkl")

joblib.dump(model, model_output_path)
joblib.dump(label_encoders, encoders_output_path)

print(f"Model saved to: {model_output_path}")
print(f"Label encoders saved to: {encoders_output_path}")

# 10. Save evaluation metrics to CSV
metrics_df = pd.DataFrame([{
    "model": "XGBoost",
    "train_accuracy": train_accuracy,
    "train_auc": train_roc_auc,
    "test_accuracy": accuracy,
    "test_auc": roc_auc,
    "precision": precision,
    "recall": recall,
    "f1_score": f1,
    "training_time": training_time
}])

metrics_output_path = os.path.join("metrics", "xgboost_metrics.csv")
metrics_df.to_csv(metrics_output_path, index=False)
print(f"Evaluation metrics saved to: {metrics_output_path}")

# 11. Save ROC curve data
fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
roc_auc_val = auc(fpr, tpr)
np.savez_compressed("metrics/xgboost_roc.npz", fpr=fpr, tpr=tpr, auc=roc_auc_val)

# 12. Save Precision-Recall curve data
precision_vals, recall_vals, _ = precision_recall_curve(y_test, y_pred_proba)
pr_auc = auc(recall_vals, precision_vals)
np.savez_compressed("metrics/xgboost_pr.npz", precision=precision_vals, recall=recall_vals, auc=pr_auc)

print("ROC and PR curve data saved for XGBoost.")
