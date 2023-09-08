def scrub_phone(phone=None):
    return (
        phone.replace("-", "")
        .replace(".", "")
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
    )
