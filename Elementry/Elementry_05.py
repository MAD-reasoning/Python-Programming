# Modify the previous program such that only multiples of three or five are considered in the sum.

try:
    multiple_sum = 0
    number = int(input("Enter a natural number: "))
    for i in range(1, number+1):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
except ValueError:
    print("Enter a valid number ")
else:
    print("Sum = ", multiple_sum)
