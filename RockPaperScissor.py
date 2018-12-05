# Game: rock paper scissor
import random


def check():
    my_set = ["r", "p", "s"]
    user_choice = input("rock(r) paper(p) scissor(s): ")
    rand = random.randint(0, 2)
    comp_choice = my_set[rand]
    user_choice = user_choice.lower()
    if user_choice == "r" or user_choice == "p" or user_choice == "s":
        print("\nYour choice: " + user_choice)
        print("Computer choice: " + comp_choice+"\n")
        if comp_choice == user_choice:
            print("its a draw")
        else:
            if user_choice == 'r':
                if comp_choice == 'p':
                    print("you lose")
                else:
                    print("you win")
            elif user_choice == 'p':
                if comp_choice == 's':
                    print("you lose")
                else:
                    print("you win")
            else:
                if comp_choice == 'r':
                    print("you lose")
                else:
                    print("you win")
    else:
        print("incorrect input\n")
        check()


check()