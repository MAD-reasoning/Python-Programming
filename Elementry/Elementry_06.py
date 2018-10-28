""" Write a program that asks the user for a number n and gives them the possibility to choose between computing the sum
 and computing the product of 1 to n.
"""

num_sum = 0
product = 1
try:
    number = int(input("Enter a natural number: "))
    choice = str(input("Sum(s) or Product(p): "))
    for i in range(1, number+1):
        if choice.lower() == 's':
            num_sum += i
        elif choice.lower() == 'p':
            product *= i
except ValueError:
    print("Enter a valid number")
else:
    if choice.lower() == 's':
        print("Sum = ", num_sum)
    elif choice.lower() == 'p':
        print("Product = ", product)
