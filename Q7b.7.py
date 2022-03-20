answer = ''
while len(answer) != 5:
    print("Please enter a five letter word")
    answer = input("what will the answer be? ").lower()
guess = ""
while guess != answer:
    guess = input("Guess the word ").lower()
    if len(guess) != len(answer):
        print("please enter a five letter guess ")
    else:
        correct_letters = 0
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                correct_letters += 1
        print(f"You got {correct_letters} letters correct")
print("Well done you guessed the word!")