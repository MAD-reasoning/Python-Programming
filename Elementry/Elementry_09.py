"""Write a guessing game where the user has to guess a secret number. After every guess the program tells the user
whether their number was too large or too small. At the end the number of tries needed should be printed. It counts
only as one try if they input the same number multiple times."""

from random import randint

lists = []
guess = 0
guess_num = 0
number = randint(1, 100)

while guess != number:
    guess = int(input("Guess the number: "))

    if guess > number:
        print("\nnumber is smaller than guessed number")
    elif guess < number:
        print("\nnumber is greater than guessed number")

    if lists.__contains__(guess):
        print("Enter new number")
    else:
        lists.append(guess)
        guess_num += 1

print("\nnumber of guess taken: ", guess_num)
