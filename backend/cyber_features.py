import re

def extract_cyber_features(text):

    text = str(text).lower()

    features = {}

    # -----------------------------
    # Email
    # -----------------------------
    features["has_email"] = int(
        bool(re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text))
    )

    features["gmail_email"] = int(
        "gmail.com" in text or
        "yahoo.com" in text or
        "hotmail.com" in text
    )

    # -----------------------------
    # URL
    # -----------------------------
    features["has_url"] = int(
        bool(re.search(r'https?://|www\.', text))
    )

    # -----------------------------
    # WhatsApp
    # -----------------------------
    features["whatsapp"] = int(
        "whatsapp" in text
    )

    # -----------------------------
    # Phone Number
    # -----------------------------
    features["phone"] = int(
        bool(re.search(r'\d{10}', text))
    )

    # -----------------------------
    # Registration Fee
    # -----------------------------
    fee_words = [
        "registration fee",
        "processing fee",
        "pay",
        "payment",
        "deposit"
    ]

    features["registration_fee"] = sum(
        word in text
        for word in fee_words
    )

    # -----------------------------
    # Urgency
    # -----------------------------
    urgency_words = [
        "urgent",
        "immediately",
        "apply immediately",
        "limited time",
        "hiring now"
    ]

    features["urgency_score"] = sum(
        word in text
        for word in urgency_words
    )

    # -----------------------------
    # Immediate Joining
    # -----------------------------
    features["immediate_joining"] = int(
        "immediate joining" in text
    )

    # -----------------------------
    # Freshers
    # -----------------------------
    features["freshers"] = int(
        "fresher" in text or
        "freshers" in text
    )

    # -----------------------------
    # Work From Home
    # -----------------------------
    features["work_from_home"] = int(
        "work from home" in text
    )

    # -----------------------------
    # Salary Mention
    # -----------------------------
    features["salary_present"] = int(
        "salary" in text
    )

    # -----------------------------
    # Very High Salary
    # -----------------------------
    numbers = re.findall(r'\d+', text)

    high = 0

    for n in numbers:
        try:
            if int(n) >= 1000000:
                high = 1
        except:
            pass

    features["high_salary"] = high

    # -----------------------------
    # Company
    # -----------------------------
    company_words = [
        "company",
        "pvt",
        "private",
        "ltd",
        "limited",
        "inc"
    ]

    features["company_score"] = sum(
        word in text
        for word in company_words
    )

    return features