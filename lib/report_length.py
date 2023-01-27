def report_length(strg):
    if isinstance(strg, str):
        length = len(strg)
        return f"This string was {length} characters long."
    else:
        return "This is not a string!"