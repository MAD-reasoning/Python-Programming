# Write a program that prints the next 20 leap years.

flag, count = 0, 0
year = int(input("Enter a year: "))
while count < 20:
    if flag == 0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
        flag = 1
        print("leap year")
    elif flag == 1:
        print(year)
        count += 1
        year += 4
    elif flag == 0:
        year += 1
