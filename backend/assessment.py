from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from database.database_functions import save_prediction

# Singleton Pattern
class ModelSingleton:
    _instance = None
    _model = None

    @classmethod
    def get_model(cls):
        if cls._instance is None:
            cls._instance = cls()
            model_path = os.path.join("model_machinelearning/models", "xgboost_model.pkl")
            cls._model = joblib.load(model_path)
        return cls._model

# Factory Pattern
class InputFactory:
    @staticmethod
    def create_input(data):
        return np.array([[
            int(data["gender"]),
            float(data["age"]),
            int(data["hypertension"]),
            int(data["heart_disease"]),
            int(data["smoking_history"]),
            float(data["bmi"]),
            float(data["HbA1c_level"]),
            float(data["blood_glucose_level"]),
        ]])

# Facade Pattern
class PredictionService:
    @staticmethod
    def predict(data):
        model = ModelSingleton.get_model()
        input_data = InputFactory.create_input(data)
        prediction = model.predict(input_data)[0]
        save_prediction(data, int(prediction))
        return int(prediction)

# Flask Application
app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    try:
        prediction = PredictionService.predict(data)
        return jsonify({"diabetes_prediction": prediction})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)