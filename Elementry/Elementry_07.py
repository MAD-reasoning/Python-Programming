# Write a program that prints a multiplication table for numbers upto 12.

try:
    number = int(input("Enter a natural number(max 12): "))
    if number <= 12:
        for i in range(1, 11):
            print("{:2d} * {:2d} = {:02d}".format(number, i, number * i))
    else:
        print("Number greater than 12")
except ValueError:
    print("Enter a valid number")
