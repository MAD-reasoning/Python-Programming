# Modify the previous program such that only the users Alice and Bob are greeted with their names.

name = input("Enter your name: ")
if name.lower() == 'alice' or name.lower() == 'bob':
    print("Hi, ", name, " !")
else:
    print("shoo! Shoo!")
