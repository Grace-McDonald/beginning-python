word = input("Please enter a word: ")
count = 1
for i in range(9):
    if input("enter another word: ") == word:
        count += 1

print(f"{word} word was entered {count} times")
# dont know how I could make it so that if the word was entered once the tense would change