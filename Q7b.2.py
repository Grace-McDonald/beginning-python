word_1 = input("What is your first word? ")
word_2 = input("What is your second word? ")
if word_1[0] == word_2[0]:
    print(f"{word_1} and {word_2} both begin with {word_1[0]} ")
else:
    print(f"{word_1} and {word_2} both begin with different letters")
