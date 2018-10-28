# Write a program that asks the user for a number and prints the sum of the numbers 1 to number.

try:
    num_sum = 0
    number = int(input("Enter a natural number: "))
    for i in range(1, number+1):
        num_sum += i
except ValueError:
    print("Enter a valid number")
else:
    print("Sum = ", num_sum)
