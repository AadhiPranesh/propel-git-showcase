def is_valid_email(email):

    if not isinstance(email, str):
        return False
    cleaned = email.strip()
    return "@" in cleaned and "." in cleaned.split("@")[-1]