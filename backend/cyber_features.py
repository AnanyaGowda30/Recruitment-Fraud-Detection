import re

def extract_cyber_features(text):

    features = {}

    # -----------------------------
    # Email Presence
    # -----------------------------
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    features["has_email"] = int(
        bool(re.search(email_pattern, text))
    )

    # -----------------------------
    # URL Presence
    # -----------------------------
    url_pattern = r'https?://\S+|www\.\S+'

    features["has_url"] = int(
        bool(re.search(url_pattern, text))
    )

    # -----------------------------
    # Urgency Keywords
    # -----------------------------
    urgency_words = [
        "urgent",
        "immediately",
        "hiring now",
        "apply today",
        "limited time"
    ]

    text_lower = text.lower()

    urgency_score = sum(
        word in text_lower
        for word in urgency_words
    )

    features["urgency_score"] = urgency_score

    # -----------------------------
    # Salary Mention
    # -----------------------------
    salary_pattern = r'₹?\$?\d[\d,]*'

    features["salary_present"] = int(
        bool(re.search(salary_pattern, text))
    )

    # -----------------------------
    # Company Mention
    # -----------------------------
    company_keywords = [
        "company",
        "pvt",
        "private",
        "ltd",
        "limited",
        "inc"
    ]

    company_score = sum(
        word in text_lower
        for word in company_keywords
    )

    features["company_score"] = company_score

    return features