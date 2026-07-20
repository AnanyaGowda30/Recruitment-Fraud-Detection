import re

def mask_pii(text):
    """
    Detect and mask sensitive information from job descriptions.
    """

    detected = []

    # -------------------------
    # Email
    # -------------------------
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    emails = re.findall(email_pattern, text)

    if emails:
        detected.extend(emails)

    text = re.sub(email_pattern, "<EMAIL>", text)

    # -------------------------
    # Phone Number
    # -------------------------
    phone_pattern = r'(\+?\d[\d\s\-]{8,}\d)'

    phones = re.findall(phone_pattern, text)

    if phones:
        detected.extend(phones)

    text = re.sub(phone_pattern, "<PHONE>", text)

    # -------------------------
    # Aadhaar Number (12 digits)
    # -------------------------
    aadhaar_pattern = r'\b\d{4}\s?\d{4}\s?\d{4}\b'

    aadhaar = re.findall(aadhaar_pattern, text)

    if aadhaar:
        detected.extend(aadhaar)

    text = re.sub(aadhaar_pattern, "<AADHAAR>", text)

    # -------------------------
    # Bank Account Number
    # -------------------------
    bank_pattern = r'\b\d{9,18}\b'

    bank = re.findall(bank_pattern, text)

    if bank:
        detected.extend(bank)

    text = re.sub(bank_pattern, "<BANK>", text)

    return {
        "clean_text": text,
        "detected": detected
    }