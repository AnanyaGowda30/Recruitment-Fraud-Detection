import joblib

# Load trained model and TF-IDF vectorizer
model = joblib.load("../models/xgboost_model.pkl")
tfidf = joblib.load("../models/tfidf_vectorizer.pkl")

def predict_job(job_text):

    text_vector = tfidf.transform([job_text])

    prediction = int(model.predict(text_vector)[0])

    probability = model.predict_proba(text_vector)[0]

    confidence = round(float(max(probability) * 100), 2)

    if prediction == 1:
        result = "Fraudulent Job"
    else:
        result = "Genuine Job"

    return {
        "prediction": result,
        "confidence": confidence
    }