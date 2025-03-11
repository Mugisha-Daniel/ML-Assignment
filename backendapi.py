from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
model = load("house_model.pkl")

@app.route("/")
def home():
    return jsonify({"message": "House Price Prediction API is running!"})

@app.route("/predict", methods=["POST"])
def predict_price():
    data = request.json  
    try:
        num_rooms = int(data["num_rooms"])
        area = float(data["area"])
        features = np.array([[area, num_rooms]])
        prediction = model.predict(features)[0][0] * 1_000_000
        return jsonify({"predicted_price": f"{prediction:,.0f} Rwf"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
