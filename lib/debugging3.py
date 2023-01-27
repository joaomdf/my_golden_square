def get_most_common_letter(text):
    counter = {}
    for char in text:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])
    for i in range(1,len(letter)):
        if letter[-i][0].isalpha() == True:
            return letter[-i][0]


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")