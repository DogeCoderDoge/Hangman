print("Welcome to Hangman!")

import random
from words import words
word = random.choice(words)
list(word)
letters_guessed = []
wrong_letters = [""]
guesses_left = 14
win_confirm = 0

for i in word:
        letters_guessed.append("_")

while guesses_left > 0:
    print("\nThe word contains {} letters".format(len(word)))
    print("You have {} guesses left".format(guesses_left))
    
    print(*letters_guessed)
    user = input("\nEnter a letter --> ")

    if user in letters_guessed or user in wrong_letters:
        print("You have already entered '{}', enter another letter!".format(user))
        guesses_left += 1

    if user in word:
        for letter, num in zip(word, range(len(word))):
            if user == letter: #If guess is there in actual word then according to the index add it
                letters_guessed[num] = user
                win_confirm += 1

        if win_confirm == len(word):
            print("You've won")        
            print("The word was '{}' ".format(word))
            break

    else:
        guesses_left -= 1
        wrong_letters.append(user)

        if guesses_left <= 0:
            print("You don't have any chances left :(")
            print("The word was '{}' ".format(word))
