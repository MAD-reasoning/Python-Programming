# Write a program that prints all prime numbers.

try:
    up_to = int(input("Enter a natural number to find prime numbers up to: ")) + 1
    print("Prime numbers are: ")
    for n in range(2, up_to):
        flag = 1
        limit = n // 2
        for i in range(2, limit):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            print(n)
except ValueError:
    print("Enter a valid number")
