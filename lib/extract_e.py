def extract_e(s):
    new_s = ""
    for i in range(len(s)):
        if s[i] == "e":
            new_s = "e" + new_s
        else:
            new_s += s[i]
    return new_s