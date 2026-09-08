import re


def validate_phone(phone):
    pattern = r"^[0-9]{10}$"
    return re.fullmatch(pattern, phone) is not None


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.fullmatch(pattern, email) is not None