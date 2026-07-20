from flask import Flask, request, jsonify
from flask_cors import CORS
from predictor import predict_job

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Recruitment Fraud Detection API Running"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    text = data["job_description"]

    result = predict_job(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)