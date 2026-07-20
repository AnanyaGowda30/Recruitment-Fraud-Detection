import joblib
import torch
from transformers import AutoTokenizer, AutoModel

MODEL_NAME = "distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
bert = AutoModel.from_pretrained(MODEL_NAME)

model = joblib.load("../models/distilbert_xgboost.pkl")


def predict_job(job_text):

    inputs = tokenizer(
        job_text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():
        outputs = bert(**inputs)

    embedding = outputs.last_hidden_state[:, 0, :].numpy()

    prediction = int(model.predict(embedding)[0])
    probability = model.predict_proba(embedding)[0]
    confidence = round(float(max(probability) * 100), 2)

    if prediction == 1:
        result = "Fraudulent Job"
    else:
        result = "Genuine Job"

    return {
        "prediction": result,
        "confidence": confidence
    }