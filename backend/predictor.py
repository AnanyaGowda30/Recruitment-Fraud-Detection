import joblib
import scipy.sparse as sp
import numpy as np

from cyber_features import extract_cyber_features

model = joblib.load("../models/xgboost_fusion.pkl")
tfidf = joblib.load("../models/tfidf_fusion.pkl")


def predict_job(job_text):
    cyber = extract_cyber_features(job_text)

    cyber_vector = np.array([
        cyber["has_email"],
        cyber["has_url"],
        cyber["gmail_email"],
        cyber["whatsapp"],
        cyber["phone"],
        cyber["registration_fee"],
        cyber["urgency_score"],
        cyber["immediate_joining"],
        cyber["freshers"],
        cyber["work_from_home"],
        cyber["salary_present"],
        cyber["high_salary"],
        cyber["company_score"]
    ]).reshape(1, -1)

    tfidf_vector = tfidf.transform([job_text])
    final_vector = sp.hstack([tfidf_vector, cyber_vector])

    prediction = int(model.predict(final_vector)[0])
    probability = model.predict_proba(final_vector)[0]
    confidence = round(float(max(probability) * 100), 2)

    risk = 0

    if cyber["registration_fee"]:
        risk += 3
    if cyber["gmail_email"]:
        risk += 2
    if cyber["whatsapp"]:
        risk += 2
    if cyber["phone"]:
        risk += 1
    if cyber["immediate_joining"]:
        risk += 1
    if cyber["high_salary"]:
        risk += 2
    if cyber["urgency_score"] >= 2:
        risk += 2

    if prediction == 1 or risk >= 6:
        result = "Fraudulent Job"
        confidence = max(confidence, 95.0)
    else:
        result = "Genuine Job"

    return {
        "prediction": result,
        "confidence": confidence,
        "cyber_features": cyber
    }